import math


def word_count(text: str) -> int:
    return len(text.split())


def character_count(text: str) -> int:
    return len(text)


def reading_time(text: str) -> int:
    """
    Reading speed ≈ 200 words/minute
    """
    return math.ceil(word_count(text) / 200)