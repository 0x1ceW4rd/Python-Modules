#!/usr/bin/env python3

def water_plants(plant_list):
    """waters the plants and handles errors"""
    try:
        print("Opening watering system")
        for plant in plant_list:
            print(f"Watering {plant.lower()}")
    except Exception:
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """tests the watering system"""
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    plants = ["tomato", None]
    water_plants(plants)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
