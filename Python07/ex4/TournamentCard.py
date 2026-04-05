from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """Card that supports tournament play:
    combat, ranking, and basic card features."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        mana: int = 0,
        wins: int = 0,
        losses: int = 0,
        rating: int = 1200,
    ):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.mana = mana
        self.wins = wins
        self.losses = losses
        self.rating = rating

    def play(self, game_state: dict) -> dict:
        """Simulate playing the card."""
        return {"card": self.name, "effect": "played",
                "game_state": game_state}

    def attack(self, target) -> dict:
        """Attack a target (creature or player)."""
        return {"attacker": self.name,
                "target": str(target),
                "damage": self.attack}

    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage."""
        self.health -= incoming_damage
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "remaining_health": self.health,
        }

    def get_combat_stats(self) -> dict:
        """Return combat statistics."""
        return {"attack": self.attack,
                "health": self.health,
                "mana": self.mana}

    def calculate_rating(self) -> int:
        """Return current rating."""
        return self.rating

    def update_wins(self, wins: int) -> None:
        """Increase win count and update
        rating accordingly (simplified Elo)."""
        self.wins += wins
        self.rating += wins * 16

    def update_losses(self, losses: int) -> None:
        """Increase loss count and update rating accordingly."""
        self.losses += losses
        self.rating -= losses * 16

    def get_rank_info(self) -> dict:
        """Return ranking information."""
        return {"wins": self.wins,
                "losses": self.losses, "rating": self.rating}

    def get_tournament_stats(self) -> dict:
        """Return combined stats for tournament display."""
        stats = self.get_rank_info()
        stats.update(self.get_combat_stats())
        stats["name"] = self.name
        return stats
