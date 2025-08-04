from Driver import *

class AutoTradingSystem:
    def __init__(self):
        self.driver = None

    def login(self, id, password):
        self.driver.login(id, password)

    def select_stock_broker(self, broker):
        self.driver: Driver = Driver(broker)

    def buy_nice_timing(self):
        '''
            • 200ms 주기로 3회 가격을 읽고, 가격이 올라가는 추세인지 파악한다.
            • 가격이 올라가는 추세라면, 총 금액을 최대한 사용하여 최대 수량만큼 매수한다.
            • 마지막에 읽은 가격으로 매수한다.
            :return:
        '''
        pass

    def buy(self,code,price,count):
        self.driver.buy(code,count,price)

    def sell_nice_timing(self):
        '''
            • 200ms 주기로 3회 가격을 읽고, 가격이 내려가는 추세인지 파악한다.
            • 가격이 내려가는 추세라면, 사용자가 설정한 수량만큼 주식을 모두 매도한다.
            • 마지막에 읽은 가격으로 매도한다.
            :return:
        '''
        pass

