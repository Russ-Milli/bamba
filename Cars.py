class Gari:
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.odometer_reading = 0

    def describe_gari(self):
        return f"{self.make} {self.model} {self.year} {self.colour}"

    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it"

    def update_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You cant roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_car = Gari("Ford", "Mustang", "2020", "White")
print(my_car.describe_gari())
print(my_car.read_odometer())
my_car.update_odometer(100)
print(my_car.read_odometer())
my_car.increment_odometer(50)
print(my_car.read_odometer())
my_car2 = Gari("Mercedes", "G Wagon", "2020", "black")
print(my_car2.describe_gari())
print(my_car2.read_odometer())
print(my_car2.update_odometer(160))
print(my_car2.read_odometer())
my_car2.increment_odometer(78)
print(my_car2.read_odometer())



