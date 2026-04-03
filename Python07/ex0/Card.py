from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.info = {"name": self.name,
                     "cost": self.cost,
                     "rarity": self.rarity}

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return self.info

    def is_playable(self, available_mana: int) -> bool:
        return True if available_mana >= self.cost else False
