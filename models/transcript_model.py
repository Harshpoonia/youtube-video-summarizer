from dataclasses import dataclass


@dataclass
class TranscriptData:
    """
    Stores all information related to a YouTube transcript.
    """

    video_id: str
    transcript: str
    language: str
    word_count: int
    character_count: int
    estimated_reading_time: int