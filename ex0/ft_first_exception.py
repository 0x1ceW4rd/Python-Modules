#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    try:
        temp_str = int(temp_str)
        if temp_str > 40:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)\n")
        elif temp_str < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)\n")
        else:
            print(f"Temperature {temp_str}°C is perfect for plants!\n")
    except:
        print(f"Error: '{temp_str}' is not a valid number\n")


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
