
class Car:
    def __init__(self, model, year, name, price, colour, for_sale):
        self.model = model
        self.year = year
        self.name = name
        self.price = price
        self.colour = colour
        self.for_sale = for_sale

    def drive(self  ):
        print(f"You drive the {self.colour}, {self.name}, {self.model}")

    def stop(self):
        print(f"You stop the {self.colour}, {self.name}, {self.model}")

    def describe(self):
        print(f"The car is {self.colour}, {self.name}, {self.model}, {self.year},"
              f"the car is for sale {self.for_sale}, the cost is {self.price}")