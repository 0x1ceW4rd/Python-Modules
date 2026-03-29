#!/usr/bin/env python3

print("=== Pathway Debate Mastery ===\n")

print("Testing Absolute Imports (from basic.py):")
from alchemy.transmutation import basic
print(f"lead_to_gold(): {basic.lead_to_gold()}")
print(f"stone_to_gem(): {basic.stone_to_gem()}")

print()

print("Testing Relative Imports (from advanced.py):")
from alchemy.transmutation import advanced
print(f"philosophers_stone(): {advanced.philosophers_stone()}")
print(f"elixir_of_life(): {advanced.elixir_of_life()}")

print()

print("Testing Package Access:")
import alchemy
print(f"alchemy.transmutation.lead_to_gold(): {alchemy.transmutation.lead_to_gold()}")
print(f"alchemy.transmutation.philosophers_stone(): {alchemy.transmutation.philosophers_stone()}")

print("\nBoth pathways work! Absolute: clear, Relative: concise")
