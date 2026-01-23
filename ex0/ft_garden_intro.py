#!/usr/bin/env python3

def ft_garden_intro():
    """
    Print a simple garden introduction with plant details.

    This function prints the plant name, height, and age
    in a formatted wat to the console.
    """

    # Define plant information
    plant_name = "Rose"
    height = "25cm"
    age = "30 days"

    # Print the formatted garden introduction
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant_name}")
    print(f"Height: {height}")
    print(f"Age: {age}")
    print("=== End of Program ===")


if __name__ == "__main__":
    # Execute the function only when the script is run directly
    ft_garden_intro()
