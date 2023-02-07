#!/usr/bin/python3
 
class   HotBeverage:
    def __init__(self, name = "hot beverage", price = 0.30):
        self.price = price
        self.name = name

    def description(self):
        return "Just some hot water in a cup."
    
    def __str__(self) -> str:
        return "name : {}\nprice : {:.2f}\ndescription : {}".format(self.name, self.price, self.description())

class Coffee(HotBeverage):
    def __init__(self):
        super().__init__("coffee", 0.40)

    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self):
        super().__init__("tea")

class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__("chocolate", 0.50)

    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__("cappuccino", 0.45)

    def description(self):
        return "Un po' di Italia nella sua tazza!"


def beverages():
    hot_water = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()

    print("Menu:\n")
    print(f"{hot_water}\n")
    print(f"{coffee}\n")
    print(f"{tea}\n")
    print(f"{chocolate}\n")
    print(f"{cappuccino}\n")

if __name__ == '__main__':
    beverages()