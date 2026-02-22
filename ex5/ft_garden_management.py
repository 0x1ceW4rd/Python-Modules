#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class PlantError(GardenError):
    def __init__(self):
        super().__init__("Error adding plant: Plant name cannot be empty!\n")


class WaterError(GardenError):
    def __init__(self):
        super().__init__("Caught WaterError: Not enough water in the tank!")


class Plant:
    def __init__(self, name, water_level, sunlight_hours):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    def __init__(self):
        self.water_tank = 2
        self.plants = []

    def add_plants(self, plants: list):
        try:
            print("Adding plants to garden...")
            for plant in plants:
                if not plant:
                    raise PlantError
                self.plants.append(plant)
                print(f"Added {plant.name} successfully")
        except PlantError as e:
            print(e)

    def water_plants(self, water_level):
        try:
            if 10 < water_level or water_level > 1:
                raise WaterError
            print("Watering plants...")
            print("Opening watering system")
            for plant in self.plants:
                plant.water_level += water_level
                self.water_tank -= water_level
                print(f"Watering {plant.name} - success")
        except WaterError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self):
        try:
            print("Checking plant health...")
            for plant in self.plants:
                if plant.water_level < 1:
                    raise Exception(
                        f"Error checking {plant.name}: Water level "
                        f"{plant.water_level} is too low (min 1)")
                elif plant.water_level > 10:
                    raise Exception(
                        f"Error checking {plant.name}: Water level "
                        f"{plant.water_level} is too high (max 10)")
                elif plant.sunlight_hours < 2:
                    raise Exception(
                            f"Error checking {plant.name}: Sunlight hours "
                            f"{plant.sunlight_hours} is too low (min 2)")
                elif plant.sunlight_hours > 12:
                    raise Exception(
                            f"Error checking {plant.name}: Sunlight hours "
                            f"{plant.sunlight_hours} is too high (max 12)")
                else:
                    print(f"{plant.name}: healthy (water: "
                          f"{plant.water_level}, sun: {plant.sunlight_hours})")
        except Exception as e:
            print(e)

    def recovery(self):
        try:
            if self.water_tank <= 0:
                raise GardenError
        except GardenError:
            print("Caught GardenError: Not enough water in tank")


def test_garden_management():
    print("=== Garden Management System ===\n")
    manager = GardenManager()

    tomato = Plant("tomato", 4, 8)
    lettuce = Plant("lettuce", 14, 5)
    plants = [tomato, lettuce, None]

    manager.add_plants(plants)

    manager.water_plants(1)
    print("")
    manager.check_plant_health()

    print("\nTesting error recovery...")
    manager.recovery()
    print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
