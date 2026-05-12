class BMW:
    def fuel_type(self):
        return "Diesel or Petrol"

    def max_speed(self):
        return "250 km/h"

class Ferrari:
    def fuel_type(self):
        return "High QUALITY Petrol"

    def max_speed(self):
        return "340 km/h"


car1 = BMW()
car2 = Ferrari()

for car in (car1, car2):
    print(f"--- {car.__class__.__name__} ---")
    print(f"Fuel: {car.fuel_type()}")
    print(f"Top Speed: {car.max_speed()}")
    print()
