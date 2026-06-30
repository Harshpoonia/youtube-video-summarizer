"""
modules/learning_service.py

LearningService is responsible for:
- Loading the learning prompt template
- Sending the transcript to Gemini via AIService
- Returning structured LearningContent

Markdown parsing is delegated to utils/markdown_parser.py.
Prompt text itself lives in prompts/learning_prompt.txt.
"""

from config import settings
from models.learning_content import LearningContent
from models.transcript import TranscriptData
from modules.ai_service import AIService
from utils.markdown_parser import parse_learning_markdown
from utils.prompt_loader import load_prompt
from utils.text_cleaning import truncate_text


class LearningService:
    """Generates structured learning material from a transcript."""

    def __init__(self, ai_service: AIService | None = None) -> None:
        self._ai_service = ai_service or AIService()

    def generate_learning_content(self, transcript_data: TranscriptData) -> LearningContent:
        """
        Generate Executive Summary, Key Points, Study Notes, and
        Important Concepts from a transcript.

        Raises ValueError if Gemini's output cannot be parsed into
        the expected section structure.
        """
        transcript_text = truncate_text(
            transcript_data.cleaned_text, settings.max_transcript_chars
        )

        prompt = load_prompt("learning_prompt.txt", transcript=transcript_text)
        raw_markdown = self._ai_service.generate(prompt, temperature=0.5)

        return parse_learning_markdown(raw_markdown)