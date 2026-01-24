#!/usr/bin/env python3
class GardenManager:
    """
    Manages multiple orchards and provides statistics for all plants.
    """

    def __init__(self, name):
        # Store manager name and a list of orchards
        self.name = name
        self.orchard = []
        # Create a stats helper that uses the same orchard list
        self.stats = self.GardenStats(self.orchard)

    def add_garden(self, orchard):
        # Add a new orchard to the manager
        self.orchard.append(orchard)

    def grow_all_plants(self):
        # Trigger growth for all plants in all orchards
        for huerto in self.orchard:
            huerto.grow_plants()

    @classmethod
    def create_garden_network(cls, name, list_huertos):
        # Create a manager and add multiple orchards at once
        manager = cls(name)
        for huerto in list_huertos:
            manager.add_garden(huerto)
        return manager

    @staticmethod
    def validate_height(height):
        # Ensure height is positive
        return height > 0

    class GardenStats:
        def __init__(self, orchard):
            # Store the orchard list for stats calculations
            self.orchard = orchard

        def count_plants(self):
            # Count total plants across all orchards
            count = 0
            for orchard in self.orchard:
                for plant in orchard.plants:
                    count += 1
            return count

        def total_growth(self):
            # Sum heights of all plants as a simple growth metric
            total = 0
            for orchard in self.orchard:
                for plant in orchard.plants:
                    total += plant.height
            return total

        def plant_types(self):
            # Count different types of plants using isinstance checks
            count = {Plant: 0, FloweringPlant: 0, PrizeFlower: 0}
            for orchard in self.orchard:
                for plant in orchard.plants:
                    if isinstance(plant, PrizeFlower):
                        count[PrizeFlower] += 1
                    elif isinstance(plant, FloweringPlant):
                        count[FloweringPlant] += 1
                    else:
                        count[Plant] += 1
            return count

        def garden_score(self):
            # Calculate a score based on plant types and prize points
            score = {Plant: 0, FloweringPlant: 0, PrizeFlower: 0}
            for orchard in self.orchard:
                for plant in orchard.plants:
                    if isinstance(plant, PrizeFlower):
                        score[PrizeFlower] += plant.prize_points + 1
                    elif isinstance(plant, FloweringPlant):
                        score[FloweringPlant] += 1
                    else:
                        score[Plant] += 1
            return score


class Orchard:
    def __init__(self, name):
        # Initialize an orchard with a name and empty plant list
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        # Add a plant to this orchard
        self.plants.append(plant)

    def grow_plants(self):
        # Grow every plant in the orchard
        for plant in self.plants:
            plant.grow()

    def calculate_stats(self):
        # Create a temporary GardenStats object for this orchard only
        stats = GardenManager.GardenStats([self])
        return {
            "total_plants": stats.count_plants(),
            "total_growth": stats.total_growth(),
            "plant_types": stats.plant_types(),
            "score": stats.garden_score(),
        }


class Plant:
    def __init__(self, name, height):
        # Initialize a basic plant with name and height
        self.name = name
        self.height = height

    def grow(self):
        # Validate height and increase it by 1 cm
        if not GardenManager.validate_height(self.height):
            self.height = 1
        self.height += 1


class FloweringPlant(Plant):
    def __init__(self, name, height, color, floracion):
        # Initialize shared attributes using the parent constructor
        super().__init__(name, height)
        # Store flower-specific attributes
        self.color = color
        self.floracion = floracion
        self.is_blooming = False

    def bloom(self):
        # Set the plant as blooming and print a message
        self.is_blooming = True
        print(f"{self.name} is blooming")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, floracion, prize_points):
        # Initialize shared attributes from FloweringPlant
        super().__init__(name, height, color, floracion)
        # Store prize-specific attribute
        self.prize_points = prize_points

    def award_point(self):
        # Increase prize points by one
        self.prize_points += 1


def main():
    # Print the demo header
    print("=== Garden Management System Demo ===")
    print("")

    # Create orchards for Alice and Bob
    alice_garden = Orchard("Alice")
    bob_garden = Orchard("Bob")

    # Create plants of different types
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red", "spring")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", "summer", 10)

    # Add plants to Alice's garden
    alice_garden.add_plant(oak)
    print("Added Oak Tree to Alice's garden")
    alice_garden.add_plant(rose)
    print("Added Rose to Alice's garden")
    alice_garden.add_plant(sunflower)
    print("Added Sunflower to Alice's garden")

    print("")
    print("Alice is helping all plants grow...")
    alice_garden.grow_plants()
    for plant in alice_garden.plants:
        print(f"{plant.name} grew 1cm")

    # Create a garden manager and add both orchards
    manager = GardenManager.create_garden_network(
        "Main Manager", [alice_garden, bob_garden]
    )

    # Calculate statistics for Alice's garden only
    stats = alice_garden.calculate_stats()
    print("")

    # Print the garden report
    print(f"=== {alice_garden.name}'s Garden Report ===")
    print("Plants in garden:")
    for plant in alice_garden.plants:
        desc = f"- {plant.name}: {plant.height}cm"
        if isinstance(plant, FloweringPlant):
            desc += f", {plant.color} flowers"
            if isinstance(plant, PrizeFlower):
                desc += f", Prize points: {plant.prize_points}"
            if plant.is_blooming:
                desc += " (blooming)"
        print(desc)
    print("")

    # Print basic stats
    print(
        f"Plants added: {stats['total_plants']}, "
        f"Total growth: {stats['total_growth']}cm"
    )
    pt = stats["plant_types"]
    print(
        f"Plant types: {pt[Plant]} regular, {pt[FloweringPlant]} "
        f"flowering, {pt[PrizeFlower]} prize flowers"
    )
    print("")

    # Validate height for the rose plant
    print(
        f"Height validation test: {GardenManager.validate_height(rose.height)}"
    )

    # Print garden scores
    scores = manager.stats.garden_score()
    total_score = scores[Plant] + scores[FloweringPlant] + scores[PrizeFlower]
    print(f"Garden scores - Alice: {total_score}, Bob: 0")

    # Print total gardens managed
    print(f"Total gardens managed: {len(manager.orchard)}")


if __name__ == "__main__":
    main()
