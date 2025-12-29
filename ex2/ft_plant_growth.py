class Plant:
    def __init__(self, name, height, age1):
        self.name = name
        self.height = height
        self.age1 = age1
        self.initial_height = height

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age1} days old"

    def grow(self, cm_per_day):
        self.height += cm_per_day
        return cm_per_day

    def age(self):
        self.age1 += 1


def main():
    plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(plant.get_info())

    for _ in range(6):
        plant.age()
        plant.grow(1)

    print("=== Day 6 ===")
    print(plant.get_info())
    growth = plant.height - plant.initial_height
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    main()
