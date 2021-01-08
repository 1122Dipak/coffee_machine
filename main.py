MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffee = input("What would you like?  (espresso,latte,cappuccino): ").lower()
if coffee != "espresso" and coffee != "latte" and coffee != "cappuccino" and coffee != "report":
    print("Sorry but that's not an option!!!")
else:
    if coffee == "espresso":
        print("Please insert coins: ")
        quarters = int(input("How many Quarters?: "))
        dimes = int(input("How many Dimes?: "))
        nickles = int(input("How many Nickles?: "))
        pennies = int(input("How many Pennies?: "))
        total_money = round((pennies * 0.01) + (nickles * 0.05) + (dimes * 0.1) + (quarters * 0.25), 3)
        return_money = 0
        if resources["water"] < MENU["espresso"]["ingredients"]["water"] or resources["coffee"] < \
                MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry not enough resources!!!")
            print(f"Here is your ${total_money}.")
        elif total_money < MENU["espresso"]["cost"]:
            print("Sorry Not Enough Money!!!")
            print(f"Here is your ${total_money}.")
        else:
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            return_money = round(total_money - MENU["espresso"]["cost"], 2)
            print("Here is your Espresso!!!")
            if return_money != 0:
                print(f"Here is your change ${return_money}")

    if coffee == "latte":
        print("Please insert coins: ")
        quarters = int(input("How many Quarters?: "))
        dimes = int(input("How many Dimes?: "))
        nickles = int(input("How many Nickles?: "))
        pennies = int(input("How many Pennies?: "))
        total_money = round((pennies * 0.01) + (nickles * 0.05) + (dimes * 0.1) + (quarters * 0.25), 3)
        return_money = 0
        if resources["water"] < MENU["latte"]["ingredients"]["water"] or resources["coffee"] < \
                MENU["latte"]["ingredients"]["coffee"] or resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry not enough resources!!!")
            print(f"Here is your ${total_money}.")
        elif total_money < MENU["latte"]["cost"]:
            print("Sorry Not Enough Money!!!")
            print(f"Here is your ${total_money}.")
        else:
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            return_money = round(total_money - MENU["latte"]["cost"], 2)
            print("Here is your Latte!!!")
        if return_money != 0:
            print(f"Here is your change ${return_money}")

    if coffee == "cappuccino":
        print("Please insert coins: ")
        quarters = int(input("How many Quarters?: "))
        dimes = int(input("How many Dimes?: "))
        nickles = int(input("How many Nickles?: "))
        pennies = int(input("How many Pennies?: "))
        total_money = round((pennies * 0.01) + (nickles * 0.05) + (dimes * 0.1) + (quarters * 0.25), 3)
        return_money = 0
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"] or resources["coffee"] < \
               MENU["cappuccino"]["ingredients"]["coffee"] or resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry not enough resources!!!")
            print(f"Here is your ${total_money}.")
        elif total_money < MENU["cappuccino"]["cost"]:
            print("Sorry Not Enough Money!!!")
            print(f"Here is your ${total_money}.")
        else:
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            return_money = round(total_money - MENU["cappuccino"]["cost"], 2)
            print("Here is your Cappuccino!!!")
            if return_money != 0:
                print(f"Here is your change ${return_money}")

    if coffee == "report":
        print(f'coffee = {resources["coffee"]}')
        print(f'milk = {resources["milk"]}')
        print(f'water = {resources["water"]}')
