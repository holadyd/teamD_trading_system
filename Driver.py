from nemo_api import *
from kiwer_api import *

class Driver:
    def __init__(self, broker:str):
        self._broker = broker
        if self._broker == "nemo":
            self._driver = NemoAPI()
        elif self._broker == "kiwer":
            self._driver = KiwerAPI()

    def login(self, id, password):
        if self._broker == "nemo":
            self._driver.cerification(id, password)
        elif self._broker== "kiwer":
            self._driver.login(id, password)
        else:
            pass

    def buy(self, stock_code, count, price):
        pass

    def sell(self, stock_code, count, price):
        pass

    def get_price(self, stock_code):
        if self._broker == "nemo":
            return self._driver.get_market_price(stock_code, 0)
        elif self._broker == "kiwer":
            return self._driver.current_price(stock_code)
        else:
            return None
