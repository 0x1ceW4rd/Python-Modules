from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name, cost, rarity, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self):
        self.played = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type,
        }
        return self.played

    def resolve_effect(self, targets: list) -> dict:
        pass
