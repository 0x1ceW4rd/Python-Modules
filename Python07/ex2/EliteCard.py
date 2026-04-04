from ex0.Card import Card
from ex2.Magical import Magical
from ex2.Combatable import Combatable


class EliteCard(Card, Magical, Combatable):
    def __init__(self, name, cost, rarity, attack, health, mana):
        super().__init__(name, cost, rarity)
        self.attackp = attack
        self.health = health
        self.mana = mana

    def play(self, game_state) -> dict:
        return game_state

    def attack(self, target):
        return {
            "attacker": self.name,
            "target": target,
            "damage": 5,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage):
        return {
            "defender": self.name,
            "damage_taken": incoming_damage - 1,
            "damage_blocked": incoming_damage - 2,
            "still_alive": True if incoming_damage < self.health else False,
        }

    def cast_spell(self, spell_name, targets):
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.mana - 6,
        }

    def channel_mana(self, amount):
        return {"channeled": amount, "total_mana": self.mana - amount}

    def get_combat_stats(self):
        return super().get_combat_stats()

    def get_magic_stats(self):
        return super().get_magic_stats()
