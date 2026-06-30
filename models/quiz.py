"""
models/quiz.py

Data models representing quiz questions and quiz state.
Contains no business logic — only structure.
"""

from dataclasses import dataclass, field


@dataclass
class QuizQuestion:
    """Represents a single multiple-choice quiz question."""

    question: str
    options: list[str]
    correct_answer: str
    explanation: str

    def is_correct(self, selected_option: str) -> bool:
        return selected_option.strip() == self.correct_answer.strip()


@dataclass
class QuizState:
    """Represents the in-progress state of a quiz session."""

    questions: list[QuizQuestion] = field(default_factory=list)
    current_index: int = 0
    score: int = 0
    answered: bool = False
    selected_option: str | None = None

    @property
    def total_questions(self) -> int:
        return len(self.questions)

    @property
    def is_complete(self) -> bool:
        return self.current_index >= self.total_questions

    @property
    def current_question(self) -> QuizQuestion | None:
        if self.is_complete:
            return None
        return self.questions[self.current_index]