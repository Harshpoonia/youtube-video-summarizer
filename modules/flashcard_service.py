"""
modules/flashcard_service.py

FlashcardService is responsible for:
- Loading the flashcard prompt template
- Sending the transcript to Gemini via AIService
- Returning a list of Flashcard objects

This service is intentionally independent of QuizService — it has
its own prompt, its own parser, and its own model, per the v2.2
requirement that flashcards do not reuse quiz code.
"""

from config import settings
from models.flashcard import Flashcard
from models.transcript import TranscriptData
from modules.ai_service import AIService
from utils.flashcard_parser import parse_flashcard_json
from utils.prompt_loader import load_prompt
from utils.text_cleaning import truncate_text


class FlashcardService:
    """Generates a flashcard deck from a transcript."""

    def __init__(self, ai_service: AIService | None = None) -> None:
        self._ai_service = ai_service or AIService()

    def generate_flashcards(
        self, transcript_data: TranscriptData, num_cards: int = 10
    ) -> list[Flashcard]:
        """
        Generate a list of flashcards from a transcript.

        Raises ValueError if Gemini's output cannot be parsed into
        the expected JSON schema.
        """
        transcript_text = truncate_text(
            transcript_data.cleaned_text, settings.max_transcript_chars
        )

        prompt = load_prompt(
            "flashcard_prompt.txt",
            transcript=transcript_text,
            num_cards=str(num_cards),
        )
        raw_response = self._ai_service.generate(prompt, temperature=0.7)

        return parse_flashcard_json(raw_response)