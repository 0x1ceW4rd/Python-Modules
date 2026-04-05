from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        sorted_hand = sorted(hand, key=lambda c: c.cost)
        cards_played = []
        mana_used = 0
        total_damage = 0

        available_mana = 10
        for card in sorted_hand:
            if card.cost <= available_mana:
                cards_played.append(card.name)
                available_mana -= card.cost
                mana_used += card.cost
                total_damage += card.cost

        targets_attacked = ["Enemy Player"]

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": total_damage,
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets
