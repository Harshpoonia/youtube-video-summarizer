"""
utils/markdown_parser.py

Parses Gemini's Markdown learning-content output into discrete
sections. Splits ONLY on top-level (single "#") headings, so
nested headings inside Study Notes (##, ###) are preserved as
part of that section's content.
"""

import re

from models.learning_content import LearningContent

# Matches a top-level heading line, e.g. "# Executive Summary"
# but not "## Sub heading" or "### Sub-sub heading".
_TOP_LEVEL_HEADING_PATTERN = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)

_EXPECTED_SECTIONS = (
    "Executive Summary",
    "Key Points",
    "Study Notes",
    "Important Concepts",
)


def parse_learning_markdown(markdown_text: str) -> LearningContent:
    """
    Parse raw Markdown into a LearningContent model.

    Raises ValueError if any of the four expected top-level
    sections cannot be found.
    """
    sections = _split_top_level_sections(markdown_text)

    missing = [name for name in _EXPECTED_SECTIONS if name not in sections]
    if missing:
        raise ValueError(
            f"Learning content is missing expected section(s): {', '.join(missing)}. "
            f"Found sections: {list(sections.keys())}"
        )

    return LearningContent(
        executive_summary=sections["Executive Summary"].strip(),
        key_points=sections["Key Points"].strip(),
        study_notes=sections["Study Notes"].strip(),
        important_concepts=sections["Important Concepts"].strip(),
    )


def _split_top_level_sections(markdown_text: str) -> dict[str, str]:
    """
    Split Markdown text into a dict of {heading_title: section_body},
    splitting only on top-level "# " headings.
    """
    matches = list(_TOP_LEVEL_HEADING_PATTERN.finditer(markdown_text))
    sections: dict[str, str] = {}

    for i, match in enumerate(matches):
        heading_title = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(markdown_text)
        sections[heading_title] = markdown_text[start:end]

    return sections