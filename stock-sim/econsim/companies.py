import math
import random

class NoCeoError(Exception):
    pass 

class NoAppraisalError(Exception):
    pass

class Ceo:
    def __init__(self, name):
        self.talent = random.expovariate(1)
        self.name = name
        self.age = 0

    def age(self, amount=1):
        self.age = self.age + 1
    
    def retiring(self):
        return self.age >= Ceo.max_age 

    def __repr__(self):
        return 'CEO %4.4f' % self.talent

    max_age = 40 * 50 * 25

class Company:
    def __init__(self, name):
        self.stock_history = []
        self.ceo_history = []
        self.name = name

    def __repr__(self):
        stock_val = self.current_stock_value()
        if stock_val is None:
            return '%s IPO  ' % self.name
        elif self.is_bankrupt():
            return '%s -----' % self.name
        return '%s %5.2f' % (self.name, stock_val, )

    def current_stock_value(self):
        last_stock_value = None

        len_stock = len(self.stock_history)
        if len_stock is not 0:
            last_stock_value = self.stock_history[len_stock - 1]

        return last_stock_value

    def current_ceo(self):
        last_ceo_value = None

        len_ceos = len(self.ceo_history)
        if len_ceos is not 0:
            last_ceo_value = self.ceo_history[len_ceos - 1]

        return last_ceo_value

    def flux_stock(self, volatility):
        if self.needs_new_ceo():
            raise NoCeoError

        flux = random.gauss(self.current_ceo().talent, volatility) 

        last_stock = self.current_stock_value();
        if last_stock is None:
            new_stock = flux
        else:
            new_stock = last_stock + flux
        self.stock_history.append(
            new_stock
        )

    def progress(self, volatility):
        try:
            self.flux_stock(volatility)
        except NoCeoError:
            self.ceo_history.append(Ceo('Anonymous'))
            self.flux_stock(volatility)

    def needs_new_ceo(self):
        return not self.ceo_history or self.current_ceo().retiring()

    def is_bankrupt(self):
        """ Note that bankruptcy is when you have less money than possible """
        stock_val = self.current_stock_value()

        if stock_val is None or stock_val >= 0.0:
            return False

        return True

