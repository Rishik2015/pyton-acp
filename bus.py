class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        # Get the base fare from the parent Vehicle class
        amount = super().fare()
        # Add a 10% maintenance charge
        amount += amount * (10 / 100)
        return amount

# Create an instance of the Bus class
School_bus = Bus("School Volvo", 12, 50)

# Print the final result
print("Total Bus fare is:", School_bus.fare())
