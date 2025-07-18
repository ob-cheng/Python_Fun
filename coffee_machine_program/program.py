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
    "money":0
}

# Prompt user by asking "What would you like?"
def user_prompt():
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while choice not in ["espresso", "latte", "cappuccino", "off", "report"]:
        choice = input("Please enter only espresso, latte, or cappuccino: ").lower()

    return choice

# Check if resources sufficient
def check_resource(command):
    missing = []

    for ingredient in MENU[command]["ingredients"]:
        if MENU[command]["ingredients"][ingredient] > resources[ingredient]:
            missing.append(ingredient)

    if missing:
        for item in missing:
            print(f"Sorry, there is not enough {item}.")
        return False
    else:
        # print("Resources are sufficient.")
        return True



# Check if transaction is successful
def check_transaction(choice):

    #  Process coins if resources are sufficient
    def process_coin():
        quarters = input("How many quarters?: ")
        while not quarters.isdigit():
            quarters = input("How many quarters? Please enter a number: ")
        dimes = input("How many dimes?: ")
        while not dimes.isdigit():
            dimes = input("How many dimes? Please enter a number: ")
        nickles = input("How many nickles?: ")
        while not nickles.isdigit():
            nickles = input("How many nickles? Please enter a number: ")
        pennies = input("How many pennies?: ")
        while not pennies.isdigit():
            pennies = input("How many pennies? Please enter a number: ")
        # Calculate total amount of coins inserted
        return round((int(quarters) * 0.25 + int(dimes) * 0.10 + int(nickles) * 0.05 + int(pennies) * 0.01), 2)

    inserted_coin = process_coin()
    if inserted_coin < MENU[choice]["cost"]:
        print(f"Sorry, that's not enough money. Money refunded.\n"
              f"You inserted ${inserted_coin}, but {choice} costs ${MENU[choice]['cost']}.")
    else:
        resources["money"] += MENU[choice]["cost"]
        if inserted_coin - MENU[choice]["cost"] > 0:
            changes = round((inserted_coin - MENU[choice]['cost']),2)
            print(f"Here is ${changes} dollars in change.")
        return True

# Make coffee: ingredients to make the drink should be deducted from the coffee machine resources
def make_coffee(choice):
    for ingredient in MENU[choice]["ingredients"]:
        resources[ingredient] -= MENU[choice]["ingredients"][ingredient]
    print(f"Thank you! Here is your {choice}!")

def main(command):
    # Turn off the Coffee Machine by entering “off” to the prompt.
    global MACHINE_STATUS
    if command == "off":
        MACHINE_STATUS = False
    # When the user enters “report” to the prompt, a report should be generated that shows the current resource values
    elif command == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    else:
        if check_resource(command):
            if check_transaction(command):
                make_coffee(command)


# Run the coffee machine

MACHINE_STATUS = True

while MACHINE_STATUS:
    COMMAND = user_prompt()
    main(COMMAND)
