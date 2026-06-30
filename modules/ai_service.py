"""
modules/ai_service.py

AIService is the single point of contact with the Gemini API.

Responsible for:
- Connecting to Gemini using the configured API key
- Sending prompts
- Returning raw text responses

This service knows nothing about quizzes, flashcards, or learning
content structure — it only talks to the model. Higher-level
services (LearningService, QuizService, FlashcardService) build
prompts and parse responses; AIService just executes the call.
"""

import re

from google import genai

from config import settings


class AIServiceError(Exception):
    """Raised when the Gemini API call fails."""

    def __init__(self, message: str, code: str = "ai_error") -> None:
        super().__init__(message)
        self.code = code


class AIService:
    """Thin wrapper around the Gemini API for text generation."""

    def __init__(self, api_key: str | None = None, model: str | None = None) -> None:
        self._api_key = api_key or settings.gemini_api_key
        self._model = model or settings.gemini_model
        self._client = genai.Client(api_key=self._api_key)

    def generate(self, prompt: str, temperature: float = 0.7) -> str:
        """
        Send a prompt to Gemini and return the response text.

        Raises AIServiceError on failure or empty response.
        """
        try:
            response = self._client.models.generate_content(
                model=self._model,
                contents=prompt,
                config={"temperature": temperature},
            )
        except Exception as exc:  # noqa: BLE001 - surface as a domain error
            message = self._format_api_error(exc)
            raise AIServiceError(
                f"Gemini API call failed: {message}",
                code=self._classify_error(message),
            ) from exc

        text = getattr(response, "text", None)
        if not text:
            raise AIServiceError("Gemini returned an empty response.")

        return text

    def _format_api_error(self, exc: Exception) -> str:
        """Create a user-facing error message for Gemini API failures."""
        message = str(exc)
        if not message:
            return "Unknown Gemini API failure."

        if "RESOURCE_EXHAUSTED" in message or "quota exceeded" in message.lower() or "429" in message:
            retry_info = ""
            retry_match = re.search(r"retry in\s*([\d.]+s)", message, re.IGNORECASE)
            if retry_match:
                retry_info = f" Retry after {retry_match.group(1)}."

            return (
                "Gemini quota exhausted. Check your API plan, billing details, and rate limits."
                + retry_info
                + f" Details: {message}"
            )

        if (
            "UNAUTHENTICATED" in message
            or "401" in message
            or "invalid authentication credentials" in message.lower()
        ):
            return (
                "Gemini authentication failed. Check your GEMINI_API_KEY, .env configuration,"
                " and ensure your credentials are valid."
                + f" Details: {message}"
            )

        return message

    def _classify_error(self, message: str) -> str:
        lower_message = message.lower()
        if "resource_exhausted" in message or "quota exceeded" in lower_message or "429" in message:
            return "quota_exhausted"
        if "rate limit" in lower_message or "rate-limited" in lower_message:
            return "rate_limited"
        if "empty response" in lower_message or "returned an empty response" in lower_message:
            return "empty_response"
        return "api_error"