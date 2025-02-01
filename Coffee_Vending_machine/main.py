def check_resources(rec):
    for key, value in resources.items():
        print(f"{key} : {value}")

def espresso(tot):
    if resources['water'] > MENU['espresso']['ingredients']['water']:
        resources['water'] -= MENU['espresso']['ingredients']['water']
        if resources['coffee'] > MENU['espresso']['ingredients']['coffee']:
            resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
        else:
            print("Sorry there is not enough coffee !!")
            return
    else:
        print("Sorry there is not enough water !!")
        return

    print(tot)
    if tot < MENU['espresso']['cost']:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = round(tot - MENU['espresso']['cost'], 2)
        print(f'Here is ${change} in change.') if change > 0 else None
        print("Here is your espresso ☕️. Enjoy!")
        resources['money'] += MENU['espresso']['cost']

def latte(tot):
    if resources['water'] > MENU['latte']['ingredients']['water']:
        resources['water'] -= MENU['latte']['ingredients']['water']
        if resources['coffee'] > MENU['latte']['ingredients']['coffee']:
            resources['coffee'] -= MENU['latte']['ingredients']['coffee']
            if resources['milk'] > MENU['latte']['ingredients']['milk']:
                resources['milk'] -= MENU['latte']['ingredients']['milk']
            else:
                print("Sorry there is not enough milk !!")
                return
        else:
            print("Sorry there is not enough coffee !!")
            return
    else:
        print("Sorry there is not enough water !!")
        return

    print(tot)
    if tot < MENU['latte']['cost']:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = round(tot - MENU['latte']['cost'], 2)
        print(f'Here is ${change} in change.') if change > 0 else None
        print("Here is your latte ☕️. Enjoy!")
        resources['money'] += MENU['latte']['cost']

def cappuccino(tot):
    if resources['water'] > MENU['cappuccino']['ingredients']['water']:
        resources['water'] -= MENU['cappuccino']['ingredients']['water']
        if resources['coffee'] > MENU['cappuccino']['ingredients']['coffee']:
            resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
            if resources['milk'] > MENU['cappuccino']['ingredients']['milk']:
                resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
            else:
                print("Sorry there is not enough milk !!")
                return
        else:
            print("Sorry there is not enough coffee !!")
            return
    else:
        print("Sorry there is not enough water !!")
        return

    print(tot)
    if tot < MENU['cappuccino']['cost']:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = round(tot - MENU['cappuccino']['cost'], 2)
        print(f'Here is ${change} in change.') if change > 0 else None
        print("Here is your cappuccino ☕️. Enjoy!")
        resources['money'] += MENU['cappuccino']['cost']

def input_coins():
    print("Please insert coins.\n")
    quaters = int(input("how many quarters?:")) * 0.25
    dimes = int(input("how many dimes?:")) * 0.10
    nickles = int(input("how many nickles?:")) * 0.05
    pennies = int(input("how many pennies?:")) * 0.01
    return round(quaters + dimes + nickles + pennies, 2)

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
    "money": 0
}

while True:
    coffee = input("What would you like? (espresso/latte/cappuccino):").lower()
    if coffee == 'report':
        check_resources(resources)
    elif coffee == 'espresso':
        espresso(input_coins())
    elif coffee == 'latte':
        latte(input_coins())
    elif coffee == 'cappuccino':
        cappuccino(input_coins())
    elif coffee == 'off':
        print("Coffee Machine Turned Off Successfully.")
        break
