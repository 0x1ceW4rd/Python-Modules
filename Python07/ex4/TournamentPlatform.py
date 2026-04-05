import random
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Manages tournament cards, matches, leaderboards, and reports."""

    def __init__(self):
        self.cards = {}
        self.match_history = []

    def register_card(self, card: TournamentCard) -> str:
        """Register a card, assign a unique ID, and return the ID."""
        base_id = card.name.lower().replace(" ", "_")
        counter = 1
        card_id = f"{base_id}_{counter:03d}"
        while card_id in self.cards:
            counter += 1
            card_id = f"{base_id}_{counter:03d}"
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Simulate a match between two registered cards.
        Returns match result."""
        if card1_id not in self.cards or card2_id not in self.cards:
            raise ValueError("One or both card IDs not found")

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.attack > card2.attack:
            winner, loser = card1, card2
        elif card2.attack > card1.attack:
            winner, loser = card2, card1
        else:
            winner, loser = random.choice([(card1, card2), (card2, card1)])

        winner.update_wins(1)
        loser.update_losses(1)

        result = {
            "winner": [id for id, c in self.cards.items() if c is winner][0],
            "loser": [id for id, c in self.cards.items() if c is loser][0],
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }
        self.match_history.append(result)
        return result

    def get_leaderboard(self) -> list:
        """Return sorted list of cards by rating (highest first)."""
        leaderboard = []
        for card_id, card in self.cards.items():
            leaderboard.append(
                {
                    "id": card_id,
                    "name": card.name,
                    "rating": card.calculate_rating(),
                    "wins": card.wins,
                    "losses": card.losses,
                }
            )
        leaderboard.sort(key=lambda x: x["rating"], reverse=True)
        for i, entry in enumerate(leaderboard, 1):
            entry["rank"] = i
        return leaderboard

    def generate_tournament_report(self) -> dict:
        """Generate a summary report of the tournament."""
        total_cards = len(self.cards)
        matches_played = len(self.match_history)
        avg_rating = 0
        if total_cards > 0:
            avg_rating = (
                sum(c.calculate_rating()
                    for c in self.cards.values()) // total_cards
            )
        return {
            "total_cards": total_cards,
            "matches_played": matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active",
        }
