"""
models/transcript.py

Data model representing a fetched and cleaned YouTube transcript.
Contains no business logic — only structure.
"""

from dataclasses import dataclass


@dataclass
class TranscriptData:
    """Represents a cleaned transcript for a single YouTube video."""

    video_id: str
    video_url: str
    raw_text: str
    cleaned_text: str
    language: str
    duration_seconds: float | None = None

    @property
    def char_count(self) -> int:
        return len(self.cleaned_text)

    @property
    def word_count(self) -> int:
        return len(self.cleaned_text.split())