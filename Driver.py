from nemo_api import *
from kiwer_api import *

class Driver:
    def __init__(self, broker:str):
        self._broker = broker
        if self._broker == "nemo":
            self._driver = NemoAPI()
        elif self._broker == "kiwer":
            self._driver = KiwerAPI()

        #self._driver = None

    def login(self, id, password):
        if self._broker == "nemo":
            self._driver.cerification(id, password)
        elif self._broker== "kiwer":
            self._driver.login(id, password)
        else:
            pass

    def buy(self, stock_code, count, price):
        if self._driver == None:
            raise Exception()
        if self._broker == "nemo":
            self._driver.purchasing_stock(stock_code,price,count)
        elif self._broker == "kiwer":
            self._driver.buy(stock_code,count,price)
        else:
            raise Exception("Broker Name is not valid")

    def sell(self, stock_code, count, price):
        pass

    def get_price(self, stock_code, minute=0):
        pass