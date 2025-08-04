class Driver:
    def __init__(self, brocker):
        self._broker = brocker

    def login(self, id, password):
        if self._broker.name == "nemo":
            self._broker.cerification(id, password)
        elif self._broker.name == "kiwer":
            self._broker.login(id, password)
        else:
            raise Exception("Broker Name is not valid")

    def buy(self, stock_code, count, price):
        pass

    def sell(self, stock_code, count, price):
        pass

    def get_price(self, stock_code, minute=0):
        pass
