#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def info_print(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


p1 = Plant("Rose", 25, 30)
p2 = Plant("Sunflower", 80, 45)
p3 = Plant("Cactus", 15, 120)
print("=== Garden Plant Registry ===")
print(p1.info_print())
print(p2.info_print())
print(p3.info_print())
