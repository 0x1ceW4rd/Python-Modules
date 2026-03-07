#!/usr/bin/env python3

class Plant:
    """A class representing a plant with basic attributes and a counter."""

    total = 0

    def __init__(self, name, height, age):
        """Initialize a Plant instance."""
        self.name = name.capitalize()
        self.height = height
        self.age = age
        Plant.total += 1

    def get_info(self):
        """Return a formatted string with the plant's details."""
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"

    def get_total(self):
        """Return a message indicating the total number of plants created."""
        return f"\nTotal plants created: {Plant.total}"


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Oak", 200, 365)
    p3 = Plant("Cactus", 5, 90)
    p4 = Plant("Sunflower", 80, 45)
    p5 = Plant("Fern", 15, 120)

    print(p1.get_info())
    print(p2.get_info())
    print(p3.get_info())
    print(p4.get_info())
    print(p5.get_info())
    print(p1.get_total())
