#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color.capitalize()

    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides 78 square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value.capitalize()


print("=== Garden Plant Types ===\n")

f1 = Flower("Rose", 25, 30, "red")
f2 = Flower("Tulip", 31, 45, "pink")

print(f"{f1.name} ({f1.__class__.__name__}): "
      f"{f1.height}cm, {f1.age} days, {f1.color} color")
f1.bloom()
print(f"{f2.name} ({f2.__class__.__name__}): "
      f"{f2.height}cm, {f2.age} days, {f2.color} color")
f2.bloom()

t1 = Tree("oak", 500, 1825, 50)
t2 = Tree("Pine", 120, 475, 20)

print(f"{t1.name} ({type(t1).__name__}): {t1.height}cm, "
      f"{t1.age} days, {t1.trunk_diameter}cm diameter")
t1.produce_shade()
print(f"{t2.name} ({type(t2).__name__}): {t2.height}cm, "
      f"{t2.age} days, {t2.trunk_diameter}cm diameter")
t2.produce_shade()

v1 = Vegetable("Tomato", 80, 90, "summer", 'c')
v2 = Vegetable("Carrot", 69, 70, "Winter", 'A')

print(f"{v1.name} ({type(v1).__name__}): {v1.height}cm, "
      f"{v1.age} days, {v1.harvest_season} harvest"
      f"\n{v1.name} is rich in vitamin {v1.nutritional_value}\n")

print(f"{v2.name} ({type(v2).__name__}): {v2.height}cm, "
      f"{v2.age} days, {v2.harvest_season} harvest"
      f"\n{v2.name} is rich in vitamin {v2.nutritional_value}\n")
