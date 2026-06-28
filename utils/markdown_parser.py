import re


def parse_learning_content(markdown_text: str):
    """
    Parse Gemini markdown response into sections.
    """

    sections = {}

    pattern = r"^#\s+(.+)$"

    matches = list(
        re.finditer(
            pattern,
            markdown_text,
            flags=re.MULTILINE
        )
    )

    for i, match in enumerate(matches):

        heading = match.group(1).strip().lower()

        start = match.end()

        end = (
            matches[i + 1].start()
            if i + 1 < len(matches)
            else len(markdown_text)
        )

        content = markdown_text[start:end].strip()

        if "summary" in heading:
            sections["Executive Summary"] = content

        elif "key point" in heading:
            sections["Key Points"] = content

        elif "study" in heading:
            sections["Study Notes"] = content

        elif "concept" in heading or "term" in heading:
            sections["Important Concepts"] = content

    return sections