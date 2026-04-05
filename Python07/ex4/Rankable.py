from abc import ABC, abstractmethod


class Rankable(ABC):
    """Abstract interface for ranking capabilities."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Return the current rating of the card."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update the win count (adds wins)."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update the loss count (adds losses)."""
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Return a dict with wins, losses, and rating."""
        pass
