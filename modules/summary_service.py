from modules.ai_service import AIService
from utils.prompt_loader import load_prompt


class SummaryService:
    """
    Handles all summary-related operations.
    """

    def __init__(self):

        self.ai = AIService()

        self.prompt_template = load_prompt(
            "summary_prompt.txt"
        )

    def generate_summary(self, transcript_data):
        prompt = self.prompt_template.replace(
            "{transcript}",
            transcript_data.transcript,
        )

        return self.ai.generate(prompt)