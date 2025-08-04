import pytest
from pytest_mock import MockerFixture
from abc import ABC,abstractmethod
from unittest.mock import call

class TestBroker(ABC):
    @abstractmethod
    def login(self):
        ...

    @abstractmethod
    def buy(self):
        ...

    @abstractmethod
    def sell(self):
        ...

    @abstractmethod
    def get_price(self):
        ...





@pytest.mark.skip
def test_auto_trader_import():
    trader_app = AutoTradingSystem()
    assert trader_app is not None

@pytest.mark.skip
def test_auto_trader_select_broker(mocker: MockerFixture):
    trader_app = AutoTradingSystem()
    trader_app.select_broker(TestBroker)
    driver = trader_app.driver

    assert driver._broker is not None
    assert isinstance(driver._broker, TestBroker)

@pytest.mark.skip
def test_auto_trader_login(mocker: MockerFixture):
    driver = mocker.Mock(spec=Driver)
    trader_app = AutoTradingSystem()
    trader_app.driver = driver

    trader_app.login('testid', 'testpw')

    driver.login.assert_has_calls([call('testid', 'testpw')])

@pytest.mark.skip
def test_auto_trader_buy(mocker: MockerFixture):
    driver = mocker.Mock(spec=Driver)
    trader_app = AutoTradingSystem()
    trader_app.driver = driver

    trader_app.buy('stock code', 3000, 5)

    driver.buy.assert_has_calls([call('stock code', 3000, 5)])



@pytest.mark.skip
def test_auto_trader_buy_1_stock(mocker: MockerFixture):
    trader_app = AutoTradingSystem()
    trader_app.select_broker(TestBroker)
    trader_app.driver.account.id = 'test_id'
    trader_app.driver.account.money = 1000
    trader_app.driver.account.stocks = []

    trader_app.buy('1234', 50, 5)

    assert trader_app.driver.account.money == 750
    assert trader_app.driver.account.stocks[0].stock_code == '1234'
    assert trader_app.driver.account.stocks[0].amount == 5



def test_auto_trader_sell(mocker: MockerFixture):
    driver = mocker.Mock(spec=Driver)
    trader_app = AutoTradingSystem()
    trader_app.driver = driver

    trader_app.sell('stock code', 3000, 5)

    driver.buy.assert_has_calls([call('stock code', 3000, 5)])

def test_auto_trader_get_price(mocker: MockerFixture):
    driver = mocker.Mock(spec=Driver)
    trader_app = AutoTradingSystem()
    trader_app.driver = driver

    trader_app.get_price('stock code')

    driver.get_price.assert_has_calls([call('stock code')])


@pytest.mark.skip
def test_auto_trader_sell_stock(mocker: MockerFixture):
    ...


@pytest.mark.skip
def test_auto_trader_buy_auto_system_(mocker: MockerFixture):
    ...


@pytest.mark.skip
def test_auto_trader_sell_auto_stock(mocker: MockerFixture):
    ...

