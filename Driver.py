from nemo_api import *
from kiwer_api import *

class Driver:
    def __init__(self, brocker:str):
        self._broker = brocker
        self._driver = None

    def login(self, id, password):
        if self._broker == "nemo":
            self._driver = NemoAPI()
            self._driver.cerification(id, password)
        elif self._broker== "kiwer":
            self._driver = KiwerAPI()
            self._driver.login(id, password)
        else:
            raise Exception("Broker Name is not valid")

    def buy(self, stock_code, count, price):
        pass

    def sell(self, stock_code, count, price):
        pass

    def get_price(self, stock_code, minute=0):
        pass