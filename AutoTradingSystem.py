

from Driver import Driver



class AutoTradingSystem:
    def __init__(self):
        self._driver = None


    def select_stock_broker(self, broker: str):
        self._driver = Driver(broker)


    def buy_nice_timing(self):
        '''
            • 200ms 주기로 3회 가격을 읽고, 가격이 올라가는 추세인지 파악한다.
            • 가격이 올라가는 추세라면, 총 금액을 최대한 사용하여 최대 수량만큼 매수한다.
            • 마지막에 읽은 가격으로 매수한다.
            :return:
        '''
        pass

    def sell_nice_timing(self):
        '''
            • 200ms 주기로 3회 가격을 읽고, 가격이 내려가는 추세인지 파악한다.
            • 가격이 내려가는 추세라면, 사용자가 설정한 수량만큼 주식을 모두 매도한다.
            • 마지막에 읽은 가격으로 매도한다.
            :return:
        '''
        pass


    def buy(self, stock_code, price, count):

        self._driver.buy(stock_code, price, count)

    def sell(self, stock_code, price, count):
        self._driver.sell(stock_code, price, count)

    def get_price(self, stock_code):
        self._driver.get_price(stock_code)

    def login(self, id, pw):
        self._driver.login(id, pw)


    def _trend_analysis(self, stock_code):
        if self._driver is None:
            raise Exception()

        ret1 = self._driver.get_price(stock_code)
        ret2 = self._driver.get_price(stock_code)
        ret3 = self._driver.get_price(stock_code)

        if ret1 < ret2 < ret3:
            return "up"
        elif ret1 > ret2 > ret3:
            return "down"

        return "-"

