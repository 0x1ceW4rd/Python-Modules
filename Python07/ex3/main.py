from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.__class__.__name__}")

    supported = factory.get_supported_types()
    print(f"Available types: {supported}\n")

    engine = GameEngine()
    engine.configure_engine(factory, strategy)
    print("Simulating aggressive turn...")
    engine.simulate_turn()

    print("\nGame Report:")
    print(engine.get_engine_status())
    print("\nAbstract Factory + Strategy Pattern: Maximum "
          "flexibility achieved!")


if __name__ == "__main__":
    main()
