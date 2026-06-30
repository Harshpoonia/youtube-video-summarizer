"""
models/flashcard.py

Data models representing flashcards and flashcard deck state.
Contains no business logic — only structure.

This is a dedicated model, separate from QuizQuestion, per the
v2.2 requirement that flashcards have their own pipeline.
"""

import random
from dataclasses import dataclass, field


@dataclass
class Flashcard:
    """Represents a single flashcard."""

    front: str
    back: str
    topic: str
    difficulty: str | None = None


@dataclass
class FlashcardDeckState:
    """Represents the in-progress state of a flashcard study session."""

    cards: list[Flashcard] = field(default_factory=list)
    current_index: int = 0
    is_flipped: bool = False

    @property
    def total_cards(self) -> int:
        return len(self.cards)

    @property
    def current_card(self) -> Flashcard | None:
        if not self.cards or self.current_index >= self.total_cards:
            return None
        return self.cards[self.current_index]

    def shuffle(self) -> None:
        random.shuffle(self.cards)
        self.current_index = 0
        self.is_flipped = False

    def next_card(self) -> None:
        if self.current_index < self.total_cards - 1:
            self.current_index += 1
            self.is_flipped = False

    def previous_card(self) -> None:
        if self.current_index > 0:
            self.current_index -= 1
            self.is_flipped = False

    def flip(self) -> None:
        self.is_flipped = not self.is_flipped