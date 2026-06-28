from modules.ai_service import AIService
from utils.prompt_loader import load_prompt
from utils.quiz_parser import parse_quiz


class QuizService:

    def __init__(self):

        self.ai = AIService()

        self.prompt = load_prompt(
            "quiz_prompt.txt"
        )

    def generate_quiz(self, transcript_data):

        prompt = self.prompt.replace(
            "{transcript}",
            transcript_data.transcript
        )

        response = self.ai.generate(prompt)

        return parse_quiz(response)