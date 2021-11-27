from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()

print(my_menu.get_items())

response = ""
while response != "off":
    response = input("What would you like to drink? ")

    if response == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        my_drink = my_menu.find_drink(response)

        if my_drink is not None:
            print(f"You selected {my_drink.name}.  Cost {my_drink.cost}")

            if my_coffee_maker.is_resource_sufficient(my_drink):
                my_money_machine.make_payment(my_drink.cost)
                my_coffee_maker.make_coffee(my_drink)
            else:
                print(f"There are not enough resources!")