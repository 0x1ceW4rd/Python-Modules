#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, p_age):
        self.name = name
        self.height = height
        self.p_age = p_age

    def grow(self, added_height):
        self.height += added_height

    def age(self, added_age):
        self.p_age += added_age

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.p_age} days old"


print("=== Day 1 ===")
p1 = Plant("Rose", 25, 30)
print(p1.get_info())
print("=== Day 7 ===")
n = 7
p1.age(7)
p1.grow(n)
print(p1.get_info())
print(f"Growth this week: +{n}cm")
