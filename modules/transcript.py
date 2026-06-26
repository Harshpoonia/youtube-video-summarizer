from youtube_transcript_api import YouTubeTranscriptApi
import re

from models.transcript_model import TranscriptData
from utils.text_statistics import (
    word_count,
    character_count,
    reading_time,
)


def extract_video_id(url: str):

    patterns = [
        r"(?:v=)([a-zA-Z0-9_-]{11})",
        r"(?:youtu\.be/)([a-zA-Z0-9_-]{11})",
        r"(?:embed/)([a-zA-Z0-9_-]{11})",
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None


def get_transcript(video_url: str) -> TranscriptData:

    video_id = extract_video_id(video_url)

    if not video_id:
        raise ValueError("Invalid YouTube URL.")

    api = YouTubeTranscriptApi()

    transcript = api.fetch(video_id)

    transcript_text = " ".join(
        snippet.text for snippet in transcript
    )

    language = transcript.language

    return TranscriptData(
        video_id=video_id,
        transcript=transcript_text,
        language=language,
        word_count=word_count(transcript_text),
        character_count=character_count(transcript_text),
        estimated_reading_time=reading_time(transcript_text),
    )