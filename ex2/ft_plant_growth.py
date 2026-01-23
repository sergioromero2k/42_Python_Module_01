class Plant:
    """
    Represents a plant with a name, height (cm), and age (days).
    """
    def __init__(self, name, height, age1):
        # Initialize the plant with name, height (cm), and age (days)
        self.name = name
        self.height = height
        self.age1 = age1
        # Store the initial height to calculate growth later
        self.initial_height = height

    def get_info(self):
        # Return the plant information in a formatted string
        return f"{self.name}: {self.height}cm, {self.age1} days old"

    def grow(self, cm_per_day):
        # Increase the plant height by a certain number of centimeters
        self.height += cm_per_day
        return cm_per_day

    def age(self):
        # Increase the plant age by one day
        self.age1 += 1


def main():
    # Create a Plant object
    plant = Plant("Rose", 25, 30)

    # Print the initial day information
    print("=== Day 1 ===")
    print(plant.get_info())

    # Simulate 6 days of growth and aging
    for _ in range(6):
        plant.age()
        plant.grow(1)

    # Print the information after a week
    print("=== Day 7 ===")
    print(plant.get_info())

    # Calculate and display total growth over the week
    growth = plant.height - plant.initial_height
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    # Run the main function when the script is executed directly
    main()
