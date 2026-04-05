from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turn_count = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            raise RuntimeError("Engine not configured")

        hand = [
            self.factory.create_creature("dragon"),
            self.factory.create_creature("goblin"),
            self.factory.create_spell("fireball"),
        ]
        self.cards_created = len(hand)

        hand_str = ", ".join(f"{card.name} ({card.cost})" for card in hand)
        print(f"Hand: [{hand_str}]\n")

        result = self.strategy.execute_turn(hand, [])
        self.turn_count += 1
        self.total_damage += result["damage_dealt"]

        print("Turn execution:")
        print(f"Strategy: {self.strategy.get_strategy_name()}")
        print(f"Actions: {result}")

        return result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turn_count,
            "strategy_used": (
                self.strategy.get_strategy_name() if self.strategy else "None"
            ),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
