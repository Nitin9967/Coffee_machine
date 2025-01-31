def check_resources(rec):
    for key,value in resources.items():
        print(f"{key} : {value}")
def espresso(tot):
    if resources['water']>MENU['espresso']['ingredients']['water']:
        resources['water'] -= MENU['espresso']['ingredients']['water']
        if resources['coffee'] > MENU['espresso']['ingredients']['coffee']:
            resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
        else:
            print("Sorry there is not enough coffee !!")
    else:
        print("Sorry there is not enough water !!")
    print(tot)
    if tot < MENU['espresso']['cost']:
        print("Sorry that's not enough money. Money refunded.")
    elif tot > MENU['espresso']['cost']:
        change = round(tot - int(MENU['espresso']['cost']), 3)
        print(f'Here is ${change}.0 in change.')
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
        else:
            print("Sorry there is not enough coffee !!")
    else:
        print("Sorry there is not enough water !!")
    print(tot)
    if tot < MENU['latte']['cost']:
        print("Sorry that's not enough money. Money refunded.")
    elif tot > MENU['latte']['cost']:
        change = round((tot - float(MENU['latte']['cost'])))
        print(f'Here is ${change}.0 in change.')
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
        else:
            print("Sorry there is not enough coffee !!")
    else:
        print("Sorry there is not enough water !!")
    print(tot)
    if tot < MENU['cappuccino']['cost']:
        print("Sorry that's not enough money. Money refunded.")
    elif tot > MENU['cappuccino']['cost']:
        change = (tot - float(MENU['cappuccino']['cost']))
        print(f'Here is ${change}.0 in change.')
        print("Here is your cappuccino ☕️. Enjoy!")
        resources['money'] += MENU['cappuccino']['cost']
def input_coins():
    print("Please insert coins.\n")
    quaters = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickles = int(input("how many nickles?:"))
    pennies = int(input("how many pennies?:"))
    return float((quaters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01))
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
    if coffee == 'espresso':
        espresso(input_coins())
    elif coffee == 'latte':
        latte(input_coins())
    elif coffee == 'cappuccino':
        cappuccino(input_coins())
    elif coffee == 'off':
        print("Coffee Maachine Turned Of Successfully")
        break


