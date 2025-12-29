class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


def main():
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]
    print("=== Plant Factory Output ===")
    for i, plant in enumerate(plants):
        print(plant.get_info())

    print(f"Total plants created: {i+1}")


if __name__ == "__main__":
    main()
