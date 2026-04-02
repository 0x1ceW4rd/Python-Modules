#!/usr/bin/env python3

print("=== Import Transmutation Mastery ===\n")

print("Method 1 - Full module import:")
import alchemy

print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")

print()

print("Method 2 - Specific function import:")
from alchemy.elements import create_water

print(f"create_water(): {create_water()}")

print()

print("Method 3 - Aliased import:")
from alchemy.potions import healing_potion as heal

print(f"heal(): {heal()}")

print()

print("Method 4 - Multiple imports:")
from alchemy.elements import create_earth

print(f"create_earth(): {create_earth()}")
from alchemy import create_fire

print(f"create_fire(): {create_fire()}")
from alchemy.potions import strength_potion

print(f"strength_potion(): {strength_potion()}")

print()

print("All import transmutation methods mastered!")
