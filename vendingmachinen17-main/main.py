from vendingmachine import VendingMachine
from beverage import Beverage

machine = VendingMachine()

ichimlik1 = Beverage('cola', 12000)
machine.add_beverage(1, ichimlik1, 30)
machine.add_beverage(2, ichimlik1, 35)
print(machine.available_cans('cola'))


# machine.recharge_card(1319, 20000)
# machine.recharge_card(1313, 20000)
# print('old', machine.get_credit(1319))
# machine.recharge_card(1319, 1300000)
# print('new', machine.get_credit(1319))
# print(machine.get_credit(1))
# machine.recharge_card(1319, 20000)
# machine.recharge_card(1319, 20000)
# machine.recharge_card(1318, 20000)
# machine.recharge_card(1318, 20000)
# machine.recharge_card(1319, 20000)
# machine.recharge_card(1319, 20000)

# ichimlik1 = Beverage('cola', 12000)
# print(ichimlik1.name)
# ichimlik1.name = 'fanta'
# print(ichimlik1.name)

# machine.add_beverage(3, ichimlik1, 30)
# print(machine.get_price('cola'))
# print(machine.info(3))
# cola1 = Beverage('cola', 11000)

# print(machine.add_beverage(1, cola1, 20))

# print(machine.info(3))
# print(machine.get_price('fanta'))
# machine.recharge_card(24, 12000)
# machine.recharge_card(24, 10000)
# machine.recharge_card(4, 10329482893000)

