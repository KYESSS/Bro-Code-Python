
from car import Car

car1 = Car("Mustang", 2026, "Ford", 100000, "blue", True)
car2 = Car("Corvette", 2024, "Chevrolet", 100000, "red", False)

print(car1.model)
print(car1.year)
print(car1.name)
print(car1.price)
print(car1.colour)
print(car1.for_sale)

car1.drive()
car1.stop()
car1.describe()