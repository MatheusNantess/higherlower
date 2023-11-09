from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


options = menu.get_items()
while is_on:
    choice = input(f"What would you like: {options}")


    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


