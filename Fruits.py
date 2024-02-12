class fruit:

    def __init__(self, name, price):

        self.name = name
        self.price = price

    def show(self):
        print(f"I like eating {self.name} and the price is {self.price}")


myobj1 = fruit("mangoes", "20ksh")
myobj1.show()
myobj2 = fruit("Guava", "50ksh")
myobj2.show()
myobj3 = fruit("Apple", "100ksh")
myobj3.show()
myobj4 = fruit("Banana", "40ksh")
myobj4.show()
myobj5 = fruit("Grapes", "80ksh")
myobj5.show()
