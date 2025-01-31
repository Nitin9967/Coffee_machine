while True:
    def check_resources(rec):
        for key,value in resources.items():
            print(f"{key} : {value}")
    def espresso(tot):
        print(tot)
        if tot < MENU['espresso']['cost']:
            print("Sorry that's not enough money. Money refunded.")
        elif tot > MENU['espresso']['cost']:
            change = round(tot - int(MENU['espresso']['cost']), 2)
            print(f'Here is ${change}.0 in change.')
            print("Here is your espresso ☕️. Enjoy!")
    def latte(tot):
        print(tot)
        if tot < MENU['latte']['cost']:
            print("Sorry that's not enough money. Money refunded.")
        elif tot > MENU['latte']['cost']:
            change = round(tot - int(MENU['latte']['cost']), 2)
            print(f'Here is ${change}.0 in change.')
            print("Here is your latte ☕️. Enjoy!")
    def cappuccino(tot):
        print(tot)
        if tot < MENU['cappuccino']['cost']:
            print("Sorry that's not enough money. Money refunded.")
        elif tot > MENU['cappuccino']['cost']:
            change = round(tot - int(MENU['cappuccino']['cost']), 2)
            print(f'Here is ${change}.0 in change.')
            print("Here is your cappuccino ☕️. Enjoy!")
    def input_coins():
        print("Please insert coins.\n")
        quaters = int(input("how many quarters?:"))
        dimes = int(input("how many dimes?:"))
        nickles = int(input("how many nickles?:"))
        pennies = int(input("how many pennies?:"))
        return int((quaters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01))
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

    coffee = input("What would you like? (espresso/latte/cappuccino):")
    if coffee == 'report':
        check_resources(resources)
    if coffee == 'espresso':
        espresso(input_coins())
    elif coffee == 'latte':
        latte(input_coins())
    elif coffee == 'cappuccino':
        cappuccino(input_coins())

