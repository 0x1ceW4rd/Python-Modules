#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    """Checks if the temperature is reasonable for plants(0 to 40 degrees)"""
    try:
        temp_str = int(temp_str)
        if temp_str > 40:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)\n")
        elif temp_str < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)\n")
        else:
            print(f"Temperature {temp_str}°C is perfect for plants!\n")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_temperature_input():
    """shows how my program keeps running despite errors"""
    print("=== Garden Temperature Checker ===\n")

    print("Testing temperature: 25")
    check_temperature(25)
    print("Testing temperature: abc")
    check_temperature("abc")
    print("Testing temperature: 100")
    check_temperature(100)
    print("Testing temperature: -50")
    check_temperature(-50)

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
