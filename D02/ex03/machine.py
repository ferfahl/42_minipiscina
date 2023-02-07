#!/usr/bin/python3

import random
from beverages import *

class CoffeeMachine:
    def __init__(self) -> None:
        self.counter = 0

    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__("empty cup", 0.90)
        
        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")
    
    def repair(self):
        self.counter = 0
        print("Repairing")

    def serve(self, beverage):
        if self.counter == 10:
            print("Machine broke... Calling repair")
            self.repair()
            return None
        temp = random.randint(0, 1)
        self.counter += 1
        if temp == 0:
            return self.EmptyCup()
        return beverage()
# Parameters : A unique parameter (other than self) that will be a class derived
# from HotBeverage.
# Return: Alternatively (randomly), the method returns an instance of the class set
# in parameter and alternatively, an EmptyCup instance.
# Obsolescence: The machine is cheap and breaks down after serving 10 drinks.
# When out of order: the call for the serve() method must raise a CoffeeMachine.BrokenMachi
# type exception until the repair() method is called.
# Fixing: After calling the repair() method, the serve() method can work again
# without raising the exception before it breaks down again after serving 10
# drinks

def coffe_place():
    machine = CoffeeMachine()
    beverage = [Coffee, Cappuccino, Chocolate, Tea, HotBeverage]

    for index in range(25):
        print(f"Order No. {index} - What's your order today?")
        value = random.randint(0, 4)
        menu = machine.serve(beverage[value])
        if not menu:
            print("Nothing was returned")
        else:
            print(f"Here it is:\n{menu}")
        print()

if __name__ == '__main__':
    coffe_place()