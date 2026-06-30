"""
config.py

Centralized configuration for the YouTube AI Learning Assistant.
Loads environment variables and exposes typed, validated settings
to the rest of the application.

No other module should read os.environ directly — everything
related to configuration flows through this file.
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Immutable application settings."""

    gemini_api_key: str
    gemini_model: str
    app_title: str
    max_transcript_chars: int


def _get_env(key: str, default: str | None = None, required: bool = False) -> str:
    value = os.getenv(key, default)
    if required and not value:
        raise EnvironmentError(
            f"Missing required environment variable: {key}. "
            f"Please set it in your .env file."
        )
    return value


def load_settings() -> Settings:
    """Load and validate settings from environment variables."""
    return Settings(
        gemini_api_key=_get_env("GEMINI_API_KEY", required=True),
        gemini_model=_get_env("GEMINI_MODEL", default="gemini-2.0-flash"),
        app_title=_get_env("APP_TITLE", default="YouTube AI Learning Assistant"),
        max_transcript_chars=int(_get_env("MAX_TRANSCRIPT_CHARS", default="100000")),
    )


settings = load_settings()