from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffe_maker = CoffeeMaker()

while True:
    options = menu.get_items()
    users_choise = input(f"What would you like? {options}")
    if users_choise == 'off':
        print('Turning off')
        break
    elif users_choise == 'report':
        coffe_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(users_choise)
        if order:
            can_make = coffe_maker.is_resource_sufficient(order)
            if can_make:
                print('It will be: $', order.cost)
                paid = money_machine.make_payment(order.cost)
                if paid:
                    coffe_maker.make_coffee(order)
