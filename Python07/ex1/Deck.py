from ex0.Card import Card
from random import shuffle


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        if self.cards.remove(card_name):
            return True
        else:
            return False

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        info = {
            "total_cards": len(self.cards),
            "creatures": len(
                [
                    card
                    for card in self.cards
                    if card.__class__.__name__ == "CreatureCard"
                ]
            ),
            "spells": len(
                [card for card in self.cards
                 if card.__class__.__name__ == "SpellCard"]
            ),
            "artifacts": len(
                [
                    card
                    for card in self.cards
                    if card.__class__.__name__ == "ArtifactCard"
                ]
            ),
            "avg_cost":
            sum([card.cost for card in self.cards]) / len(self.cards),
        }
        return info
