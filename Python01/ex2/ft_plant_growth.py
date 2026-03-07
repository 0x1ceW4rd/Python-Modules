#!/usr/bin/env python3

class Plant:
    """Represents a plant with name, height, and age."""

    def __init__(self, name, height, p_age):
        """Initialize a new plant instance."""
        self.name = name
        self.height = height
        self.p_age = p_age

    def grow(self, added_height):
        """Increase the plant's height."""
        self.height += added_height

    def age(self, added_age):
        """Increase the plant's age."""
        self.p_age += added_age

    def get_info(self):
        """Return a formatted string with plant details."""
        return f"{self.name}: {self.height}cm, {self.p_age} days old"


if __name__ == "__main__":
    print("=== Day 1 ===")
    p1 = Plant("Rose", 25, 30)
    print(p1.get_info())
    print("=== Day 7 ===")
    n = 6
    p1.age(6)
    p1.grow(n)
    print(p1.get_info())
    print(f"Growth this week: +{n}cm")
