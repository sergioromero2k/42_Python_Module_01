class SecurePlant:
    def __init__(self, name, height, age):
        self._name = name
        if height < 0:
            print(f"Invalid initial height {height}cm [REJECTED]")
            self._height = 0
        else:
            self._height = height
        if age < 0:
            print(f"Invalid initial age {age}days [REJECTED]")
            self._age = 0
        else:
            self._age = age
        print("=== Garden Security System ===")
        print(f"Plant created: {self._name}")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, value):
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {value} cm [OK]")

    def set_age(self, value):
        if value < 0:
            print(f"Invalid operation attempted: age {value}days [REJECTED]")
            print("Security: Negative age rejected")

        else:
            self._age = value
            print(f"Age updated: {value} days [OK]")

    def get_info(self):
        return (
            f"Current plant: {self._name} "
            f"({self._height}cm, {self._age} days)"
        )


def main():
    plant = SecurePlant("Rose", 25, 30)
    plant.set_height(25)
    plant.set_age(30)
    print("\n")
    plant.set_height(-5)
    print("\n")
    print(plant.get_info())


if __name__ == "__main__":
    main()
