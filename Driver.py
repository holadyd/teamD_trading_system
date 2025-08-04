from kiwer_api import *
from nemo_api import *


class Driver:
    def __init__(self, brocker: str):
        self._broker = brocker

        if brocker == "kiwer":
            self._driver = KiwerAPI()
        elif brocker == "nemo":
            self._driver = NemoAPI()

    def login(self, id, password):
        if self._broker == "nemo":
            self._driver.cerification(id, password)
        elif self._broker == "kiwer":
            self._driver.login(id, password)
        else:
            pass

    def buy(self, stock_code, price, count):

        if self._driver == None:
            raise Exception()
        if self._broker == "nemo":
            self._driver.purchasing_stock(stock_code=stock_code, count=count, price=price)
        elif self._broker == "kiwer":
            self._driver.buy(stock_code=stock_code, count=count, price=price)
        else:
            raise Exception("Broker Name is not valid")

    def sell(self, stock_code, price, count):
        if self._broker == "nemo":
            self._driver.selling_stock(stock_code=stock_code, price=price, count=count)
        elif self._broker == "kiwer":
            self._driver.sell(stock_code=stock_code, price=price, count=count)
        else:
            pass

    def get_price(self, stock_code, minute=0):
        if self._broker == "nemo":
            return self._driver.get_market_price(stock_code)
        elif self._broker == "kiwer":
            return self._driver.current_price(stock_code)
        else:
            return None
