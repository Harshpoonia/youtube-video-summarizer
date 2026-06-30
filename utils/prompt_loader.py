"""
utils/prompt_loader.py

Reusable helper for loading prompt templates from the prompts/
directory and safely formatting them with runtime values.

Prompt engineering must always live in prompts/*.txt files, never
hardcoded inside service or UI code. This module is the single
place that reads those files.
"""

from functools import lru_cache
from pathlib import Path

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"


@lru_cache(maxsize=None)
def _read_prompt_file(filename: str) -> str:
    path = PROMPTS_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Prompt file not found: {path}")
    return path.read_text(encoding="utf-8")


def load_prompt(filename: str, **kwargs: str) -> str:
    """
    Load a prompt template by filename and format it with the
    given keyword arguments.

    Example:
        load_prompt("quiz_prompt.txt", transcript=text, num_questions=5)
    """
    template = _read_prompt_file(filename)
    try:
        return template.format(**kwargs)
    except KeyError as exc:
        raise ValueError(
            f"Missing placeholder value for prompt '{filename}': {exc}"
        ) from exc
