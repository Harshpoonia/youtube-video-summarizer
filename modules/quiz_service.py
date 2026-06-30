"""
modules/quiz_service.py

QuizService is responsible for:
- Loading the quiz prompt template
- Sending the transcript to Gemini via AIService
- Returning a list of QuizQuestion objects

JSON parsing is delegated to utils/quiz_parser.py.
Prompt text itself lives in prompts/quiz_prompt.txt.
"""

from config import settings
from models.quiz import QuizQuestion
from models.transcript import TranscriptData
from modules.ai_service import AIService
from utils.prompt_loader import load_prompt
from utils.quiz_parser import parse_quiz_json
from utils.text_cleaning import truncate_text


class QuizService:
    """Generates an interactive quiz from a transcript."""

    def __init__(self, ai_service: AIService | None = None) -> None:
        self._ai_service = ai_service or AIService()

    def generate_quiz(
        self, transcript_data: TranscriptData, num_questions: int = 5
    ) -> list[QuizQuestion]:
        """
        Generate a list of quiz questions from a transcript.

        Raises ValueError if Gemini's output cannot be parsed into
        the expected JSON schema.
        """
        transcript_text = truncate_text(
            transcript_data.cleaned_text, settings.max_transcript_chars
        )

        prompt = load_prompt(
            "quiz_prompt.txt",
            transcript=transcript_text,
            num_questions=str(num_questions),
        )
        raw_response = self._ai_service.generate(prompt, temperature=0.7)

        return parse_quiz_json(raw_response)