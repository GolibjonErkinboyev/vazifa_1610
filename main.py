from vendingmachine import VendingMachine
from beverage import Beverage


machine = VendingMachine()

# cola1 = Beverage('cola', 11000)

# print(machine.add_beverage(1, cola1, 20))

# print(machine.info(3))
# print(machine.get_price('fanta'))
machine.recharge_card(24, 12000)
machine.recharge_card(24, 10000)
machine.recharge_card(4, 10329482893000)

