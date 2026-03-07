#!/usr/bin/env python3

class Plant:
    """Represents a plant with name, height, and age."""

    def __init__(self, name, height, age):
        """Initialize a new plant instance."""
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def info_print(self):
        """Return a formatted string with the plant's details."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(p1.info_print())
    print(p2.info_print())
    print(p3.info_print())
