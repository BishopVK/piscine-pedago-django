import beverages
import random

class CoffeeMachine:
    def __init__(self):
        self.counter = 0

    class EmptyCup(beverages.HotBeverage):
        name = "empty cup"
        price = 0.90
        desc = "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.counter = 0

    def serve(self, drink):
        if self.counter >= 10:
            raise self.BrokenMachineException()

        result = random.choice([drink, self.EmptyCup])
        self.counter += 1
        return result()


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()

    drink_list = [
        beverages.Coffee,
        beverages.Tea,
        beverages.Cappuccino,
        beverages.Chocolate
    ]

    for i in range(0,15):
        try:
            print(coffee_machine.serve(random.choice(drink_list)))
        except Exception as e:
            if str(e):
                print("\x1b[31m" + "Error: " + "\x1b[37m" + f"{e}")
        print(f"Served drinks: {coffee_machine.counter}")
        print("---")

    coffee_machine.repair()
    print("\x1b[36m" + "Coffee machine was repaired" + "\x1b[37m")
    print("---")


    for i in range(0,15):
        try:
            print(coffee_machine.serve(random.choice(drink_list)))
        except Exception as e:
            if str(e):
                print("\x1b[31m" + "Error: " + "\x1b[37m" + f"{e}")
        print(f"Served drinks: {coffee_machine.counter}")
        print("---")
