#!/usr/bin/env python3

class Plant:
    """
    Base class representing common traits of any plant.
    """
    def __init__(self, name, height, age):
        # Initialize common plant attributes
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        # Call the parent constructor to set common attributes
        super().__init__(name, height, age)
        # Initialize flower-specific attribute
        self.color = color

    def bloom(self):
        # Print a message indicating the flower is blooming
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        # Call the parent constructor to set common attributes
        super().__init__(name, height, age)
        # Initialize tree-specific attribute
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        # Print a message indicating how much shade the tree produces
        shade_area = self.trunk_diameter * 1.5
        print(f"{self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        # Call the parent constructor to set common attributes
        super().__init__(name, height, age)
        # Initialize vegetable-specific attributes
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


def main():
    # Print the header for the plant types output
    print("=== Garden Plant Types ===")

    # Create two instances of each plant type
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 600, 2000, 60)

    tomato = Vegetable(
        "Tomato", 80, 90, "summer", "vitamin C"
    )
    carrot = Vegetable(
        "Carrot", 30, 70, "fall", "beta-carotene"
    )

    # Display information and special behaviors for each plant
    print(
        f"{rose.name} (Flower): {rose.height}cm, {rose.age} days, "
        f"{rose.color} color"
    )
    rose.bloom()

    print(
        f"{tulip.name} (Flower): {tulip.height}cm, {tulip.age} days, "
        f"{tulip.color} color"
    )
    tulip.bloom()

    print(
        f"{oak.name} (Tree): {oak.height}cm, {oak.age} days, "
        f"{oak.trunk_diameter}cm diameter"
    )
    oak.produce_shade()

    print(
        f"{pine.name} (Tree): {pine.height}cm, {pine.age} days, "
        f"{pine.trunk_diameter}cm diameter"
    )
    pine.produce_shade()

    print(
        f"{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} days, "
        f"{tomato.harvest_season} harvest"
    )
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")

    print(
        f"{carrot.name} (Vegetable): {carrot.height}cm, {carrot.age} days, "
        f"{carrot.harvest_season} harvest"
    )
    print(f"{carrot.name} is rich in {carrot.nutritional_value}")


if __name__ == "__main__":
    main()
