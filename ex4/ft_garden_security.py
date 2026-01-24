#!/usr/binenv python3
class SecurePlant:
    """
    Represents a plant with protected height and age attributes
    It validates values before updating to prevent data corruption.
    """
    def __init__(self, name, height, age):
        # Store the plant name as a private attribute
        self._name = name

        # Validate initial height and reject negative values
        if height < 0:
            print(f"Invalid initial height {height}cm [REJECTED]")
            self._height = 0
        else:
            self._height = height

        # Validate initial age and reject negative values
        if age < 0:
            print(f"Invalid initial age {age}days [REJECTED]")
            self._age = 0
        else:
            self._age = age

        # Print security system header and plant creation confirmation
        print("=== Garden Security System ===")
        print(f"Plant created: {self._name}")

    def get_height(self):
        # Return the current height (protected access)
        return self._height

    def get_age(self):
        # Return the current age (protected access)
        return self._age

    def set_height(self, value):
        # Validate the new height before updating
        if value < 0:
            # Reject invalid height and print security warning
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            # Update height and confirm success
            self._height = value
            print(f"Height updated: {value} cm [OK]")

    def set_age(self, value):
        # Validate the new age before updating
        if value < 0:
            # Reject invalid age and print security warning
            print(f"Invalid operation attempted: age {value}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            # Update age and confirm success
            self._age = value
            print(f"Age updated: {value} days [OK]")

    def get_info(self):
        # Return a formatted string with the current plant status
        return (
            f"Current plant: {self._name} "
            f"({self._height}cm, {self._age} days)"
        )


def main():
    # Create a secure plant with valid initial values
    plant = SecurePlant("Rose", 25, 30)

    # Try to update height and age with valid values
    plant.set_height(25)
    plant.set_age(30)

    print("")

    # Attempt to update height with an invalid negative value
    plant.set_height(-5)

    print("")
    # Display current plant info
    print(plant.get_info())


if __name__ == "__main__":
    # Execute main only when running the script directly
    main()
