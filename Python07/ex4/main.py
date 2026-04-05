from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    try:
        print("\n=== DataDeck Tournament Platform ===\n")
        print("Registering Tournament Cards...\n")

        platform = TournamentPlatform()

        dragon = TournamentCard(
            name="Fire Dragon",
            cost=5,
            rarity="rare",
            attack=5,
            health=5,
            mana=3,
            rating=1200,
        )
        wizard = TournamentCard(
            name="Ice Wizard",
            cost=4,
            rarity="uncommon",
            attack=4,
            health=4,
            mana=4,
            rating=1150,
        )

        dragon_id = platform.register_card(dragon)
        wizard_id = platform.register_card(wizard)

        print(f"{dragon.name} (ID: {dragon_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {dragon.calculate_rating()}")
        print(f"- Record: {dragon.wins}-{dragon.losses}\n")

        print(f"{wizard.name} (ID: {wizard_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {wizard.calculate_rating()}")
        print(f"- Record: {wizard.wins}-{wizard.losses}\n")

        print("Creating tournament match...")
        match_result = platform.create_match(dragon_id, wizard_id)
        print(f"Match result: {match_result}\n")

        print("Tournament Leaderboard:")
        leaderboard = platform.get_leaderboard()
        for entry in leaderboard:
            print(
                f"{entry['rank']}. {entry['name']} - "
                f"Rating: {entry['rating']} ({entry['wins']}"
                f"-{entry['losses']})"
            )

        print()

        report = platform.generate_tournament_report()
        print("Platform Report:")
        print(report)

        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
