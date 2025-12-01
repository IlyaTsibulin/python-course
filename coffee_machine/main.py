def coffee_machine():
    power = True
    menu = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
                "milk": 0,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "coffee": 24,
                "milk": 150,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "coffee": 24,
                "milk": 100,
            },
            "cost": 3.0,
        },
        "coffee_machine": {
            "water":  250,
            "milk": 250,
            "coffee": 150,
            "money": 0
        }
    }

    while power:
        prompt = input("What would you like? (espresso/latte/cappuccino): ")
        if prompt == "off":
            return False
        elif prompt == "report":
            print(
                f"Water: {menu["coffee_machine"]["water"]}ml\nMilk: {menu["coffee_machine"]["milk"]}ml\nCoffee: {menu["coffee_machine"]["coffee"]}g\nMoney: ${menu["coffee_machine"]["money"]}")
        elif prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
            water = menu[prompt]["ingredients"]["water"]
            coffee = menu[prompt]["ingredients"]["coffee"]
            milk = menu[prompt]["ingredients"]["milk"]
            cost = menu[prompt]["cost"]
            if menu["coffee_machine"]["water"] < water:
                print(
                    f"Insufficient water.\n")
            elif menu["coffee_machine"]["coffee"] < coffee:
                print(
                    f"Insufficient coffee.\n")
            elif menu["coffee_machine"]["milk"] < milk:
                print(
                    f"Insufficient milk.\n")
            else:
                while menu["coffee_machine"]["money"] < cost:
                    coin = input(
                        f"Insert coin. Current amount: {menu["coffee_machine"]["money"]}$\n")
                    if coin == "quarter":
                        menu["coffee_machine"]["money"] += 0.25
                    elif coin == "dime":
                        menu["coffee_machine"]["money"] += 0.10
                    elif coin == "nickle":
                        menu["coffee_machine"]["money"] += 0.05
                    elif coin == "pennie":
                        menu["coffee_machine"]["money"] += 0.01
                    else:
                        print("Invalid coin")
                print(f"Thanks for the purchase! You'r {prompt} is ready!")
                if menu["coffee_machine"]["money"] > cost:
                    print(
                        f"Giving your change... Returned {menu["coffee_machine"]["money"] - cost}")
                menu["coffee_machine"]["money"] = 0
                menu["coffee_machine"]["milk"] -= milk
                menu["coffee_machine"]["coffee"] -= coffee
                menu["coffee_machine"]["water"] -= water


while coffee_machine():
    coffee_machine()
