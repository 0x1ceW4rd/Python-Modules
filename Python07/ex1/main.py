from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard

print("\n=== DataDeck Deck Builder ===\n")
print("Building deck with different card types...")

cards = [
    SpellCard("Lightning Bolt", 3, "Rare", "Deal 3 damage to target"),
    ArtifactCard("Mana Crystal", 2, "Epic", 5, "Permanent: +1 mana per turn"),
    CreatureCard("Fire Dragon", 5, "Legendary", 4, 10),
]

deck = Deck()

for card in cards:
    deck.add_card(card)


print(deck.get_deck_stats())
print("\nDrawing and playing cards:")

print("\nDrew: Lightning Bolt (Spell)")
print(cards[0].play())

print("\nDrew: Mana Crystal (Artifact)")
print(cards[1].play())

print("\nDrew: Fire Dragon (Creature)")
print(cards[2].play("Creature summoned to battlefield"))

print("\nPolymorphism in action: Same interface, different card behaviors!")
