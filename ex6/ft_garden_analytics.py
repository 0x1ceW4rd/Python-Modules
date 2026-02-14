#!/usr/bin/env python3

class Plant:
    """Base plant class"""

    total_growth_size = 0

    def __init__(self, name: str, height: float,) -> None:
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
    def __init__(self, name: str, height: float, color: str, prize_points: int) -> None:
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
        return f"{self.name}: {self.height}cm, {self.bloom()}, Prize points: {self.prize_points}"

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
        self.gardens [garden_data['name']]= (garden_data)
        GardenManager.total_gardens += 1
        print(f"\nAdded garden: {garden_name}'s Garden\n")
        for plant in plants:
            print(f"Added {plant.name} to {garden_name}'s garden")

    def garden_report(self, garden_name) -> None:
        """Display all gardens and their plants"""
        print(f"\n=== {self.gardens[garden_name.capitalize()]['name']}'s Garden Report ===")
        for plant in self.gardens[garden_name.capitalize()]['plants']:
            print(f"  - {plant.get_info()}")
        plants_added = len(self.gardens[garden_name.capitalize()]['plants'])
        print(f"\nPlants added: {plants_added}, Total growth: "
              f"{self.gardens[garden_name.capitalize()]['plants'][0].total_growth()}cm")
        print("Plant types: 1 regular, 1 flowering, 1 prize flowers") #fix this bitch

    @classmethod
    def create_garden_network(cls, network_name: str) -> 'GardenManager':
        """Create a network of garden managers"""
        print(f"\nCreating garden network: {network_name}")
        new_network = cls(network_name)
        
        # some default gardens
        alice_plants = [Plant("Oak Tree", 100),
                    FloweringPlant("Rose", 25, "Red"),
                    PrizeFlower("Sunflower", 50, 'Yellow', 10)]
        bob_plants = []

        new_network.add_garden("Alice", alice_plants)
        new_network.add_garden("Bob", bob_plants)
        
        return new_network

    class GardenStats:
        """Statistics helper nested inside GardenManager"""

        def __init__(self, manager: 'GardenManager') -> None:
            """Initialize with a GardenManager instance"""
            self.manager = manager

        # Instance method of nested class
        def get_garden_statistics(self) -> dict:
            """Calculate statistics for all gardens"""
            stats = {
                'total_gardens': len(self.manager.gardens),
                'total_plants': 0,
                'average_plants_per_garden': 0,
                'plant_types': {}
            }

            total_plants = 0
            for garden in self.manager.gardens:
                total_plants += len(garden['plants'])
                for plant in garden['plants']:
                    plant_type = plant.get_type()
                    stats['plant_types'][plant_type] = stats['plant_types'].get(plant_type, 0) + 1

            if stats['total_gardens'] > 0:
                stats['average_plants_per_garden'] = total_plants / stats['total_gardens']

            stats['total_plants'] = total_plants
            return stats

        # Static method inside nested class
        @staticmethod
        def calculate_average_height(plants: list) -> float:
            """Calculate average height of plants"""
            if not plants:
                return 0
            total_height = sum(plant.height for plant in plants)
            return round(total_height / len(plants), 2)

        @staticmethod
        def count_plant_types(plants: list) -> dict:
            """Count plant types in a list"""
            type_count = {}
            for plant in plants:
                plant_type = plant.get_type()
                type_count[plant_type] = type_count.get(plant_type, 0) + 1
            return type_count


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    main_manager = GardenManager("Main Manager")

    sub_manager = main_manager.create_garden_network("First Manager")
    

    print("Alice is helping all plants grow...")
    for plant in sub_manager.gardens['Alice']['plants']:
        plant.grow(1)

    sub_manager.garden_report("alice")