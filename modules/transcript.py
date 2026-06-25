from youtube_transcript_api import YouTubeTranscriptApi
import re


def extract_video_id(url):
    patterns = [
        r"(?:v=)([a-zA-Z0-9_-]{11})",
        r"(?:youtu\.be/)([a-zA-Z0-9_-]{11})",
        r"(?:embed/)([a-zA-Z0-9_-]{11})"
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None


def get_transcript(video_url):
    video_id = extract_video_id(video_url)

    if not video_id:
        raise ValueError("Invalid YouTube URL")

    ytt_api = YouTubeTranscriptApi()

    transcript = ytt_api.fetch(video_id)

    transcript_text = " ".join(
        snippet.text for snippet in transcript
    )

    return transcript_text