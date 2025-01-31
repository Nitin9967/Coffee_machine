# "C:\Users\nitin\PycharmProjects\100 Days of Code - The Complete Python Pro Bootcamp\.venv\Scripts\python.exe" "C:\Users\nitin\PycharmProjects\100 Days of Code - The Complete Python Pro Bootcamp\Day 15\Coffee Machine Project\solution.py"
# What would you like? (espresso/latte/cappuccino): report
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# What would you like? (espresso/latte/cappuccino): latte
# Please insert coins.
# how many quarters?: 5
# how many dimes?: 5
# how many nickles?: 5
# how many pennies?: 5
# Sorry that's not enough money. Money refunded.
# What would you like? (espresso/latte/cappuccino): latte
# Please insert coins.
# how many quarters?: 55
# how many dimes?: 55
# how many nickles?: 54
# how many pennies?: 55
# Here is $20.0 in change.
# Here is your latte ☕️. Enjoy!
# What would you like? (espresso/latte/cappuccino):

# *******************************************************************************************************************
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

