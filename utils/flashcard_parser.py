"""
utils/flashcard_parser.py

Parses Gemini's JSON flashcard output into Flashcard model objects.

This is a dedicated parser, intentionally separate from quiz_parser.py,
per the v2.2 requirement that flashcards have their own pipeline
rather than reusing quiz code.
"""

import json
import re

from models.flashcard import Flashcard

_CODE_FENCE_PATTERN = re.compile(r"^```(?:json)?\s*|\s*```$", re.MULTILINE)
_VALID_DIFFICULTIES = {"Easy", "Medium", "Hard"}


def parse_flashcard_json(raw_response: str) -> list[Flashcard]:
    """
    Parse raw JSON text (possibly wrapped in Markdown code fences)
    into a list of Flashcard objects.

    Raises ValueError if the response cannot be parsed or does not
    match the expected schema.
    """
    cleaned = _strip_code_fences(raw_response).strip()

    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Failed to parse flashcard JSON from Gemini: {exc}") from exc

    if not isinstance(data, list):
        raise ValueError("Expected flashcard JSON to be a list of card objects.")

    cards: list[Flashcard] = []
    for i, item in enumerate(data):
        try:
            cards.append(_parse_card(item))
        except (KeyError, TypeError) as exc:
            raise ValueError(f"Malformed flashcard at index {i}: {exc}") from exc

    if not cards:
        raise ValueError("Gemini returned an empty flashcard list.")

    return cards


def _parse_card(item: dict) -> Flashcard:
    front = item["front"]
    back = item["back"]
    topic = item.get("topic", "General")
    difficulty = item.get("difficulty")

    if difficulty is not None and difficulty not in _VALID_DIFFICULTIES:
        # Don't hard-fail on a minor schema deviation; normalize instead.
        difficulty = None

    return Flashcard(front=front, back=back, topic=topic, difficulty=difficulty)


def _strip_code_fences(text: str) -> str:
    return _CODE_FENCE_PATTERN.sub("", text)