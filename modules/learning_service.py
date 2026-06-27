from modules.ai_service import AIService
from utils.prompt_loader import load_prompt


class LearningService:
    """
    Generates AI-powered learning content from a transcript.
    """

    def __init__(self):
        self.ai = AIService()
        self.prompt_template = load_prompt("learning_prompt.txt")

    def generate_learning_content(self, transcript_data) -> str:
        """
        Generate structured learning material from a transcript.
        """

        prompt = self.prompt_template.replace(
            "{transcript}",
            transcript_data.transcript
        )

        return self.ai.generate(prompt)