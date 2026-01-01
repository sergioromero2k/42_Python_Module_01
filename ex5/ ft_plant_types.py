class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def describe(self):
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        return f"{self.name} is blooming beautifully!"

    def describe(self):
        base = super().describe()
        return f"{base} (Flower), {self.color} color"


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        return f"{self.name} provides 78 square meters of shade"

    def describe(self):
        base = super().describe()
        return f"{base} (Tree), {self.trunk_diameter} diameter"


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def nutritional_value(self):
        return f"{self.name} is rich in vitamin C"

    def describe(self):
        base = super().describe()
        return f"{base} (Vegetable), {self.harvest_season} harvest"


def main():
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 30, 20, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 400, 1460, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer")
    carrot = Vegetable("Carrot", 40, 60, "fall")

    plants = [rose, tulip, oak, pine, tomato, carrot]

    print("=== Garden Plant Types ===")
    for plant in plants:
        print(plant.describe())
        if isinstance(plant, Flower):
            print(plant.bloom())
        elif isinstance(plant, Tree):
            print(plant.produce_shade())
        elif isinstance(plant, Vegetable):
            print(plant.nutritional_value())
        print("")


if __name__ == "__main__":
    main()
