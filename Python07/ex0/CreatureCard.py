from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name, cost, rarity, attack: int, health: int):
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.attack = attack
        self.health = health
        self.info.update({"type": "Creature",
                          "attack": attack,
                          "health": health})

    def play(self, game_state):
        self.played = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": game_state,
        }
        return self.played

    def attack_target(self, target) -> dict:
        attackresult = {
            "attacker": "Fire Dragon",
            "target": "Goblin Warrior",
            "damage_dealt": 7,
            "combat_resolved": True,
        }
        return (f"{self.name} attacks {target}:\n"
                f"Attack result: {attackresult}")
