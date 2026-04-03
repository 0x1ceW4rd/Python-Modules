#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard

print("\n=== DataDeck Card Foundation ===\n")
print("\nTesting Abstract Base Class Design:\n")

creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

print("CreatureCard Info:")
print(creature.get_card_info(), end="\n\n")

print("Playing Fire Dragon with 6 mana available:")
print(f"Playable: {creature.is_playable(6)}")

print("Play result: ", end="")
print(creature.play("Creature summoned to battlefield"), end="\n\n")

print(creature.attack_target("Goblin Warrior"))

print("\nTesting insufficient mana (3 available):")
print(f"Playable: {creature.is_playable(3)}")

print("\nAbstract pattern successfully demonstrated!")
