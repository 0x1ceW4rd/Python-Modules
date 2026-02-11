#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height=0, age=0):
        self.name = name.capitalize()
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.name}")

    def set_height(self, nheight):
        if nheight < 0:
            print(f"\nInvalid operation attempted: "
                  f"height {nheight}cm [REJECTED]"
                  )
            print("Security: Negative height rejected")
        else:
            self.__height = nheight
            print(f"Height updated: {nheight}cm [OK]")

    def set_age(self, nage):
        if nage < 0:
            print(f"\nInvalid operation attempted: "
                  f"age {nage} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = nage
            print(f"Age updated: {nage} days [OK]")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def get_info(self):
        return (f"\nCurrent plant: {self.name} "
                f"({self.get_height()}cm, {self.get_age()} days)"
                )


print("=== Garden Security System ===")
p1 = Plant("rose")
p1.set_height(25)
p1.set_age(30)

p1.set_height(-5)
print(p1.get_info())
