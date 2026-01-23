#!/usr/bin/env python3
class Plant:
    """
    Represents a plant with a name, height (cm), and age (days)
    """
    def __init__(self, name, height, age):
        # Initialize the plant with its basic attributes
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        # Return the plant information formatted for output
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


def main():
    # Create a list of plants with different intitial values
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]

    # Print header for the factory output
    print("=== Plant Factory Output ===")
    for i, plant in enumerate(plants):
        print(plant.get_info())

    # Print the total number of plants created
    print(f"Total plants created: {i+1}")


if __name__ == "__main__":
    # Run the main function when the script is executed directly
    main()
