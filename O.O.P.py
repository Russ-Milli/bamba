class Car:

    def __init__(self, make, model, year, colour):

        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

    def onyesha(self):
        print(f"My dream car is {self.make} and my model is {self.model} and the year of manufacture is {self.year}")
        print(f"My dream car is {self.make} and my model is {self.model} and the year of manufacture is {self.year}")
        print(f"My dream car is {self.make} and my model is {self.model} and the year of manufacture is {self.year} and the colour is {self.colour}")


myobj = Car("Koinesegg", "Agera", "2021", "White")



myobj.onyesha()
