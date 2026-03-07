#!/usr/bin/env python3

class Plant:
    """Represents a plant with encapsulated height and age attributes."""

    def __init__(self, name, height=0, age=0):
        """Initialize a Plant instance."""
        self.name = name.capitalize()
        self.__height = height  # private attribute
        self.__age = age        # private attribute
        print(f"Plant created: {self.name}")

    def set_height(self, nheight):
        """
        Set the plant's height after validating it's non-negative.

        nheight: New height in centimeters.
        """
        if nheight < 0:
            print(f"\nInvalid operation attempted: "
                  f"height {nheight}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = nheight
            print(f"Height updated: {nheight}cm [OK]")

    def set_age(self, nage):
        """
        Set the plant's age after validating it's non-negative.

        nage : New age in days.
        """
        if nage < 0:
            print(f"\nInvalid operation attempted: "
                  f"age {nage} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = nage
            print(f"Age updated: {nage} days [OK]")

    def get_height(self):
        """Return the current height in centimeters."""
        return self.__height

    def get_age(self):
        """Return the current age in days."""
        return self.__age

    def get_info(self):
        """Return a formatted string with plant information."""
        return (f"\nCurrent plant: {self.name} "
                f"({self.get_height()}cm, {self.get_age()} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p1 = Plant("rose")
    p1.set_height(25)
    p1.set_age(30)

    p1.set_height(-5)
    print(p1.get_info())
