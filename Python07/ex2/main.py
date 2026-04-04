from ex2.EliteCard import Card, Combatable, Magical, EliteCard

print("\n=== DataDeck Ability System ===\n")

print("EliteCard capabilities:")
cards = [Card, Combatable, Magical]
for card in cards:
    methods = [m for m in dir(card)
               if not m.startswith("__") and not m.startswith("_")]
    print(f"- {card.__name__}: {methods}")

print("\nPlaying Arcane Warrior (Elite Card):\n")
elite = EliteCard("Arcane Warrior", 5, "Rare", 7, 10, 10)
print("Combat phase:")
print(f"Attack result: {elite.attack('Enemy')}")
print(f"Defense result: {elite.defend(4)}")

print("\nMagic phase:")
print(f"Spell cast: {elite.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
print(f"Mana channel: {elite.channel_mana(3)}")

print("\nMultiple interface implementation successful!")
