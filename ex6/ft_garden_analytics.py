#!/usr/bin/env python3

class Plant:
    """Base plant class"""

    total_growth_size = 0

    def __init__(self, name: str, height: float,) -> None:
        """initilizer/constructor; create the atributtes for each instance"""
        self.name = name
        self.height = height

    def get_info(self) -> str:
        """Returns plant information as string"""
        return f"{self.name}: {self.height}cm"

    def grow(self, amount: float) -> None:
        """Increases plant height"""
        self.height += amount
        Plant.total_growth_size += amount
        print(f"{self.name} grew {amount}cm")

    @classmethod
    def total_growth(cls):
        """return the total growth that has been done by the garden"""
        return f"{cls.total_growth_size}"

    def get_type(self):
        """Returns plant type"""
        return "regular"


class FloweringPlant(Plant):
    """Plant that can flower"""
    def __init__(self, name: str, height: float, color: str) -> None:
        super().__init__(name, height)
        self.color = color.capitalize()

    def bloom(self) -> str:
        """Returns bloom status"""
        return f"{self.color} flowers (blooming)"

    def get_type(self):
        """Return plant type"""
        return "flowering"

    def get_info(self) -> str:
        """Returns plant information as string"""
        return f"{self.name}: {self.height}cm, {self.bloom()}"


class PrizeFlower(FloweringPlant):
    """Prize-winning flowering plant"""
    def __init__(self, name: str, height, color: str, prize_points: int):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def display_prize_info(self) -> str:
        """Returns prize information"""
        return f"{self.name} won in {self.prize_points}"

    def get_type(self):
        """Return plant type"""
        return "prize flowers"

    def get_info(self) -> str:
        """Returns plant information as string"""
        return (f"{self.name}: {self.height}cm, {self.bloom()}, "
                f"Prize points: {self.prize_points}")


class GardenManager:
    """Manages multiple gardens and provides analytics"""

    total_managers = 0
    total_gardens = 0

    def __init__(self, name: str) -> None:
        """Initialize a garden manager"""
        self.name = name
        self.gardens = {}
        GardenManager.total_managers += 1

    def add_garden(self, garden_name: str, plants: list) -> None:
        """sets up a garden with its plants"""
        garden_data = {
            'name': garden_name.capitalize(),
            'plants': plants
        }
        self.gardens[garden_data['name']] = (garden_data)
        GardenManager.total_gardens += 1
        # print(f"\nAdded garden: {garden_name}'s Garden\n")
        for plant in plants:
            print(f"Added {plant.name} to {garden_name}'s garden")

    def garden_report(self, garden_name) -> None:
        """Display all gardens and their plants"""
        garden_key = garden_name.capitalize()
        garden = self.gardens[garden_key]

        print(f"\n=== {garden['name']}'s Garden Report ===")
        print("Plants in garden:")
        for plant in garden['plants']:
            print(f"  - {plant.get_info()}")

        plants_added = len(garden['plants'])

        # Count plants by type
        type_counts = {}
        for plant in garden['plants']:
            plant_type = plant.get_type()
            type_counts[plant_type] = type_counts.get(plant_type, 0) + 1

        print(f"\nPlants added: {plants_added}, "
              f"Total growth: {Plant.total_growth()}cm")
        output = ""
        for plant_type, count in type_counts.items():
            output += f"{count} {plant_type}, "
        output = output[:-2]
        print(f"Plant types: {output}")

    @classmethod
    def create_garden_network(cls, network_name: str) -> 'GardenManager':
        """Create a network of garden managers"""
        # print(f"\nCreating garden network: {network_name}")
        new_network = cls(network_name)

        # some default gardens
        alice_plants = [Plant("Oak Tree", 100),
                        FloweringPlant("Rose", 25, "Red"),
                        PrizeFlower("Sunflower", 50, 'Yellow', 10)]
        # bob_plants = []
        bob_plants = [PrizeFlower("Cherry Blossom", 450, "Pink", 92)]

        new_network.add_garden("Alice", alice_plants)
        new_network.add_garden("Bob", bob_plants)

        return new_network

    class GardenStats:
        """Statistics helper nested inside GardenManager"""

        def __init__(self, manager: 'GardenManager') -> None:
            """Initialize with a GardenManager instance"""
            self.manager = manager

        @staticmethod
        def validate_height(height: float):
            """validate the height of plants"""
            if not height:
                return "No height was given"
            return height > 0

        def calculate_garden_scores(self) -> dict:
            """Calculate total prize points for each garden"""
            scores = {}
            for garden_name, garden_data in self.manager.gardens.items():
                total = 0
                for plant in garden_data['plants']:
                    if hasattr(plant, 'prize_points'):
                        total += plant.prize_points
                scores[garden_name] = total
            return scores


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    main_manager = GardenManager("Main Manager")

    sub_manager = main_manager.create_garden_network("First Manager")

    def alice_grows():
        """adds 1cm to all of Alice's plants"""
        print("\nAlice is helping all plants grow...")
        for plant in sub_manager.gardens['Alice']['plants']:
            plant.grow(1)

    alice_grows()
    sub_manager.garden_report("alice")

    stats = GardenManager.GardenStats(sub_manager)

    print(f"\nHeight validation test: {stats.validate_height(12)}")

    scores = stats.calculate_garden_scores()
    score_string = ("Garden scores - " + ", "
                    .join(f"{garden}: {points}"
                          for garden, points in scores.items()))
    print(score_string)

    print(f"Total gardens managed: {sub_manager.total_gardens}")
