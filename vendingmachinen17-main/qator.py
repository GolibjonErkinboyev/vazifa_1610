from beverage import Beverage

class Qator:
    def __init__(self, number) -> None:
        self._number = number
        self.ichimlik:Beverage = None
        self._number_beverage:int = None

    def add_beverage(self, beverage: Beverage, number_beverage):
        self._name = beverage.name
        self.ichimlik = beverage
        self._number_beverage = number_beverage
        return 'qo\'shildi'
    
    def getinfo(self):
        return f'{self._number} -- qatorda, {self.ichimlik}, ichimliklar soni {self._number_beverage}'

    def get_price(self, name):
        beverage = self.ichimlik
        if beverage == None:
            return None
        elif name == beverage.name:
            return self.ichimlik.price
        return None



    