from google import genai

from config import GEMINI_API_KEY, MODEL_NAME


class AIService:
    """
    Handles communication with the Gemini API.
    """

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, prompt: str) -> str:
        """
        Sends a prompt to Gemini and returns the generated response.
        """

        try:

            response = self.client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
            )

            if not response.text:
                raise ValueError("Gemini returned an empty response.")

            return response.text.strip()

        except Exception as e:

            raise RuntimeError(
                f"Gemini API Error:\n{str(e)}"
            )