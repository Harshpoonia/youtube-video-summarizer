"""
utils/text_cleaning.py

Helper functions for cleaning raw YouTube transcript text before
it is sent to the AI model. Pure text-processing logic only.
"""

import re


def clean_transcript_text(raw_text: str) -> str:
    """
    Normalize whitespace and remove filler artifacts commonly found
    in auto-generated YouTube transcripts.
    """
    text = re.sub(r"\[.*?\]", "", raw_text)  # remove [Music], [Applause], etc.
    text = re.sub(r"\s+", " ", text)  # collapse whitespace
    return text.strip()


def truncate_text(text: str, max_chars: int) -> str:
    """Truncate text to a maximum character length, on a word boundary."""
    if len(text) <= max_chars:
        return text
    truncated = text[:max_chars]
    last_space = truncated.rfind(" ")
    if last_space > 0:
        truncated = truncated[:last_space]
    return truncated.strip()