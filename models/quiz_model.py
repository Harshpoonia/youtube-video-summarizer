from dataclasses import dataclass


@dataclass
class QuizQuestion:

    question: str

    options: list[str]

    answer: str

    explanation: str