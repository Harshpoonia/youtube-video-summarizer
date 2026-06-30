"""
models/learning_content.py

Data model representing parsed AI-generated learning content
(Executive Summary, Key Points, Study Notes, Important Concepts).
Contains no business logic — only structure.
"""

from dataclasses import dataclass


@dataclass
class LearningContent:
    """Represents structured learning material derived from a transcript."""

    executive_summary: str
    key_points: str
    study_notes: str
    important_concepts: str

    def as_dict(self) -> dict[str, str]:
        return {
            "Executive Summary": self.executive_summary,
            "Key Points": self.key_points,
            "Study Notes": self.study_notes,
            "Important Concepts": self.important_concepts,
        }