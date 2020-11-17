class Food:
    pass
class Drink:
    pass

def newFood(name, weight, price, quantity):
    food = Food()
    food.name  = name
    food.weight = weight
    food.price = price
    food.quantity = quantity
    return food

def newDrink(name, volume, price, quantity):
    drink = Drink()
    drink.name  = name
    drink.volume = volume
    drink.price = price
    drink.quantity = quantity
    return drink

def printFood(food):
    print(f"{food.name:^7} {food.weight:^2}g.  = {food.price:^3} MDL | {food.quantity} portions available")

def printDrink(drink):
    print(f"{drink.name:^7} {drink.volume:^2}ml. = {drink.price:^3} MDL | {drink.quantity} pieces available")

def printItem(item):
    if type(item) == Food:
        printFood(item)
    if type(item) == Drink:
        printDrink(item)


food1 = newFood("BORSH", 250, 50, 10)
drink1 = newDrink("PEPSI", 500, 15, 50)

printItem(food1)
printItem(drink1)
