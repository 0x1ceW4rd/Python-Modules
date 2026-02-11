#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: aezzirar <aezzirar@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/06 19:12:25 by aezzirar        #+#    #+#               #
#  Updated: 2026/02/11 11:27:52 by aezzirar        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    """Base plant class"""
    def __init__(self, name: str, height: float,) -> None:
        self.name = name
        self.height = height

    def get_info(self) -> str:
        """Returns plant information as string"""
        return f"{self.name}: {self.height}cm"

    def grow(self, amount: float) -> None:
        """Increases plant height"""
        self.height += amount
        print(f"{self.name} grew {amount}cm")
    
    def get_type(self):
        return "regular"


class FloweringPlant(Plant):
    """Plant that can flower"""
    def __init__(self, name: str, height: float, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def bloom(self) -> str:
        """Returns bloom status"""
        return f"{self.color} (blooming)"

    def get_type(self):
        return "flowering"

class PrizeFlower(FloweringPlant):
    """Prize-winning flowering plant"""
    def __init__(self, name: str, height: float, color: str, prize_points: int) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def display_prize_info(self) -> str:
        """Returns prize information"""
        return f"{self.name} won in {self.prize_points}"

    def get_type(self):
        return "prize flowers"


class GardenManager:
    """Manages multiple gardens and provides analytics"""

    # Class attribute
    total_managers = 0

    def __init__(self, name: str) -> None:
        """Initialize a garden manager"""
        self.name = name
        self.gardens = {}  
        GardenManager.total_managers += 1

    # INSTANCE METHOD - works on specific manager
    def add_garden(self, garden_name: str, plants: list) -> None:
        """Add a garden with its plants"""
        garden_data = {
            'name': garden_name,
            'plants': plants
        }
        self.gardens [garden_data['name']]= (garden_data)
        print(f"Added garden: {garden_name}")

    def garden_report(self) -> None:
        """Display all gardens and their plants"""
        print(f"\n=== {self.gardens}'s Garden Report ===")
        for garden in self.gardens:
            print(f"\nGarden: {garden['name']}")
            for plant in garden['plants']:
                print(f"  - {plant.get_info()}")

    @classmethod
    def create_garden_network(cls, network_name: str) -> 'GardenManager':
        """Create a network of garden managers"""
        print(f"\nCreating garden network: {network_name}")
        new_network = cls(network_name)
        
        # Add some default gardens
        alice_plants = [
            Plant("Oak Tree", 100),
            FloweringPlant("Rose", 25, "red"),
            PrizeFlower("Sunflower", 50, "yellow", 10)
        ]
        new_network.add_garden("Alice's Garden", alice_plants)
        bob_plants = [None]
        new_network.add_garden("Bob's Garden", bob_plants)
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




firstgarden = GardenManager.create_garden_network("Alice")

firstgarden.garden_report()