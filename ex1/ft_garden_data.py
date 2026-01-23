#!/usr/bin/env python3
class Plant:
    """
    Represents a plant with a name, height (cm), and age (days).
    """
    def __init__(self, name, height, age):
        # Initialize the plant attributes
        self.name = name
        self.height = height
        self.age = age

    def display_info(self):
        # Print the plant information in a formatted way
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    # Print the header for the plant registry
    print("=== Garden Plant Registry ===")

    # Create at least three Plant objects
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    # Display information for each plant
    plant1.display_info()
    plant2.display_info()
    plant3.display_info()


if __name__ == "__main__":
    # Run the main function only when the script is executed directly
    main()
