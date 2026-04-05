from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == "dragon":
            return CreatureCard(
                "Fire Dragon", cost=5, rarity="rare", attack=5, health=5
            )
        elif name_or_power == "goblin":
            return CreatureCard(
                "Goblin Warrior", cost=2, rarity="common", attack=2, health=2
            )
        else:
            return CreatureCard(
                "Mystic Beast", cost=4, rarity="uncommon", attack=4, health=4
            )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == "fireball":
            return SpellCard(
                "Lightning Bolt", cost=3, rarity="common", effect_type="damage"
            )
        else:
            return SpellCard(
                "Frost Nova", cost=2, rarity="common", effect_type="freeze"
            )

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == "mana_ring":
            return ArtifactCard(
                "Mana Ring", cost=1, rarity="uncommon",
                durability=3, effect="+1 mana"
            )
        else:
            return ArtifactCard(
                "Stone Shield",
                cost=2,
                rarity="common",
                durability=2,
                effect="+2 defense",
            )

    def create_themed_deck(self, size: int) -> list:
        return []

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }
