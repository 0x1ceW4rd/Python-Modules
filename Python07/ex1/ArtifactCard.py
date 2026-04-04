from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name, cost, rarity, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self):
        self.played = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect,
        }
        return self.played

    def activate_ability(self) -> dict:
        pass
