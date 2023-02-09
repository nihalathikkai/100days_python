## Requirements

# 1. Print report
# 2. Check resources sufficient
# 3. Process Coins
# 4. Check Transaction Successfull
# 5. Make Coffee

menu = {
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

money = 0


def print_report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}mg\nMoney: ${money}")
    
    
    
def check_resourse(cmd):
    emoji = {"water":'💧', "milk": '🥛', "coffee": '🟤'}
    for item in menu[cmd]["ingredients"]:
        if resources[item]<menu[cmd]["ingredients"][item]:
            print(f'Sorry there is not enough {item} {emoji[item]}')
            return -1
    return 0



def process_coins():
    print("Please insert coins.")
    total_coins = round((int(input("How many quarters?: "))*0.25
                +int(input("How many dimes?: "))*0.1
                +int(input("How many nickels?: "))*0.05
                +int(input("How many pennies?: "))*0.01),2)
    print(f"You have inserted ${total_coins}")
    return total_coins
    


def check_transaction(cmd):
    global money
    cost = menu[cmd]['cost']
    print(f"Price of one {cmd} is {cost}")
    total_coins = process_coins()
    
    if total_coins < cost:
        print("Sorry that's not enough money 💰, Money refunded.")
        return -1
    
    change = round((total_coins - cost),2)
    if total_coins > cost:
        print(f"Here is ${change} in change")
        
    money += cost
    return 0



def make_coffee(cmd):
    for item in menu[cmd]["ingredients"]:
        resources[item] -= menu[cmd]["ingredients"][item]
    print(f"Here is your {cmd} ☕. Enjoy!")



def coffee_machine():
    while True:
        cmd = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
        
        if cmd in ('espresso', 'latte', 'cappuccino'):
            if check_resourse(cmd) == -1 or check_transaction(cmd) == -1:
                print()
                continue
            make_coffee(cmd)
            
        elif cmd == 'report':
            print_report()
        
        elif cmd == 'off':
            print("Turning off....")
            return
        
        elif cmd == 'help':
            print("Supported commands:\n- espresso\n- latte\n- cappuccino\n- report\n- off")
            
        else:
            print(f"'{cmd}' not a valid command!")
        
        print()
        


if __name__ == "__main__":
    coffee_machine()
    """Please insert coins.
    How many quarters?:
    How many dimes?:
    How many nickels?:
    How many pennies?:
    Here is $3.14 in change
    Here is your Latte. Enjoy!
    Sorry there is not enough water
    Sorry that's not enough money, Money refunded."""
    
    
# penny : 0.01
# nickel:0.05
# dime: 0.1
# quarter: 0.25