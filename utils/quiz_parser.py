"""
utils/quiz_parser.py

Parses Gemini's JSON quiz output into QuizQuestion model objects.
Handles minor formatting issues (e.g. accidental Markdown code
fences) that LLMs sometimes add despite instructions not to.
"""

import json
import re

from models.quiz import QuizQuestion

_CODE_FENCE_PATTERN = re.compile(r"^```(?:json)?\s*|\s*```$", re.MULTILINE)


def parse_quiz_json(raw_response: str) -> list[QuizQuestion]:
    """
    Parse raw JSON text (possibly wrapped in Markdown code fences)
    into a list of QuizQuestion objects.

    Raises ValueError if the response cannot be parsed or does not
    match the expected schema.
    """
    cleaned = _strip_code_fences(raw_response).strip()

    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Failed to parse quiz JSON from Gemini: {exc}") from exc

    if not isinstance(data, list):
        raise ValueError("Expected quiz JSON to be a list of question objects.")

    questions: list[QuizQuestion] = []
    for i, item in enumerate(data):
        try:
            questions.append(_parse_question(item))
        except (KeyError, TypeError) as exc:
            raise ValueError(f"Malformed quiz question at index {i}: {exc}") from exc

    if not questions:
        raise ValueError("Gemini returned an empty quiz question list.")

    return questions


def _parse_question(item: dict) -> QuizQuestion:
    options = item["options"]
    if not isinstance(options, list) or len(options) != 4:
        raise ValueError(f"Expected exactly 4 options, got: {options}")

    correct_answer = item["correct_answer"]
    if correct_answer not in options:
        raise ValueError(
            f"correct_answer '{correct_answer}' does not match any option in {options}"
        )

    return QuizQuestion(
        question=item["question"],
        options=options,
        correct_answer=correct_answer,
        explanation=item.get("explanation", ""),
    )


def _strip_code_fences(text: str) -> str:
    return _CODE_FENCE_PATTERN.sub("", text)