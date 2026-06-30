"""
modules/transcript.py

Responsible for:
- Extracting the video ID from a YouTube URL
- Fetching the raw transcript via youtube-transcript-api
- Cleaning the transcript text
- Producing a TranscriptData model

No AI logic and no UI logic belongs here.
"""

import re

from youtube_transcript_api import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
    YouTubeTranscriptApi,
)

from models.transcript import TranscriptData
from utils.text_cleaning import clean_transcript_text

_VIDEO_ID_PATTERNS = (
    re.compile(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"),
    re.compile(r"youtu\.be\/([0-9A-Za-z_-]{11})"),
)


class TranscriptError(Exception):
    """Raised when a transcript cannot be fetched or extracted."""


def extract_video_id(youtube_url: str) -> str:
    """Extract the 11-character YouTube video ID from a URL."""
    youtube_url = youtube_url.strip()

    for pattern in _VIDEO_ID_PATTERNS:
        match = pattern.search(youtube_url)
        if match:
            return match.group(1)

    # Fall back: maybe the user pasted a bare video ID.
    if re.fullmatch(r"[0-9A-Za-z_-]{11}", youtube_url):
        return youtube_url

    raise TranscriptError(f"Could not extract a video ID from URL: {youtube_url}")


def fetch_transcript(youtube_url: str, languages: list[str] | None = None) -> TranscriptData:
    """
    Fetch and clean a transcript for the given YouTube URL.

    Raises TranscriptError on any failure (disabled captions,
    unavailable video, no transcript found, IP blocked, etc.)
    """
    video_id = extract_video_id(youtube_url)
    languages = languages or ["en"]

    try:
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id, languages=languages)
    except TranscriptsDisabled as exc:
        raise TranscriptError("Transcripts are disabled for this video.") from exc
    except NoTranscriptFound as exc:
        raise TranscriptError(
            "No transcript found in the requested language(s) for this video."
        ) from exc
    except VideoUnavailable as exc:
        raise TranscriptError("This video is unavailable.") from exc
    except Exception as exc:  # noqa: BLE001 - surface as a domain error
        raise TranscriptError(
            f"Failed to fetch transcript. This may be caused by an IP block "
            f"from YouTube (common on cloud hosts) — consider using a "
            f"residential proxy. Original error: {exc}"
        ) from exc

    raw_segments = [snippet.text for snippet in fetched]
    raw_text = " ".join(raw_segments)
    cleaned_text = clean_transcript_text(raw_text)

    if not cleaned_text:
        raise TranscriptError("Transcript was fetched but contained no usable text.")

    duration = None
    if fetched and hasattr(fetched[-1], "start") and hasattr(fetched[-1], "duration"):
        duration = fetched[-1].start + fetched[-1].duration

    return TranscriptData(
        video_id=video_id,
        video_url=youtube_url,
        raw_text=raw_text,
        cleaned_text=cleaned_text,
        language=fetched.language_code if hasattr(fetched, "language_code") else languages[0],
        duration_seconds=duration,
    )