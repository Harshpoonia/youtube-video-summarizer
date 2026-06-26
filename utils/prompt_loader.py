from pathlib import Path


PROMPTS_DIR = Path("prompts")


def load_prompt(filename: str) -> str:
    """
    Load a prompt template from the prompts directory.
    """

    prompt_path = PROMPTS_DIR / filename

    if not prompt_path.exists():
        raise FileNotFoundError(
            f"Prompt file not found: {prompt_path}"
        )

    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()