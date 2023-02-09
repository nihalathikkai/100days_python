from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



def coffee_machine():
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()
    
    while True:
        cmd = input(f"What would you like? ({menu.get_items()}): ").lower().strip()
        if cmd == 'report':
            coffee_maker.report()
            money_machine.report()
        elif cmd == 'off':
            print("Turning off...")
            return
        else:
            drink = menu.find_drink(cmd)
            if drink and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        


if __name__ == "__main__":
    coffee_machine()