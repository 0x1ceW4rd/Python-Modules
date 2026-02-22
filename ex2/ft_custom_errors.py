#!/usr/bin/env python3

class GardenError(Exception):
    """spesific exception/error GardenError"""
    def __init__(self, *args):
        super().__init__(*args)


class PlantError(GardenError):
    """spesific exception/error PlantError"""
    def __init__(self, plant):
        self.plant = plant.capitalize()
        super().__init__(f"Caught PlantError: The "
                         f"{self.plant} plant is wilting!")


class WaterError(GardenError):
    """spesific exception/error WaterError"""
    def __init__(self):
        super().__init__("Caught WaterError: Not enough water in the tank!")


def iswelting(days_with_no_water: int) -> bool:
    """checks plant welting status"""
    if days_with_no_water > 5:
        return True
    else:
        return False


def ismorewater(water_lvl: int) -> bool:
    """checks plant Water status"""
    if water_lvl > 5:
        return False
    else:
        return True


def test_custom_errors():
    """function that tests the custom Exceptions"""
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        isit = 7
        if iswelting(isit):
            raise PlantError("Tomato")
    except PlantError as e:
        print(e, end="\n\n")

    print("Testing WaterError...")
    try:
        water_lvl = 4
        if ismorewater(water_lvl):
            raise WaterError
    except WaterError as e:
        print(e, end="\n\n")

    print("Testing catching all garden errors...")
    try:
        isit = 6
        if iswelting(isit):
            raise PlantError("Tomato")
    except GardenError as e:
        print(e)
    try:
        water_lvl = 5
        if ismorewater(water_lvl):
            raise WaterError
    except GardenError as e:
        print(e)

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
