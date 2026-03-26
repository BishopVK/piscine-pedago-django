class HotBeverage:
    # Atributos de clase (valores por defecto)
    name = "hot beverage"
    price = 0.30
    desc = "Just some hot water in a cup."

    def description(self):
        return self.desc

    def __str__(self):
        return (f"name : {self.name}\n"
                f"price : {self.price:.2f}\n"
                f"description : {self.description()}")

class Coffee(HotBeverage):
    name = "coffee"
    price = 0.40
    desc = "A coffee, to stay awake."

class Tea(HotBeverage):
    name = "tea"

class Chocolate(HotBeverage):
    name = "chocolate"
    price = 0.50
    desc = "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    name = "cappuccino"
    price = 0.45
    desc = "Un po’ di Italia nella sua tazza!"



if __name__ == "__main__":
    hotBeverage = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()

    print(hotBeverage)
    print("---")
    print(coffee)
    print("---")
    print(tea)
    print("---")
    print(chocolate)
    print("---")
    print(cappuccino)