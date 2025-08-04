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
def test_auto_trader_sell_stock(mocker: MockerFixture):
    ...


@pytest.mark.skip
def test_auto_trader_sell_stock(mocker: MockerFixture):
    ...


@pytest.mark.skip
def test_auto_trader_buy_auto_system_(mocker: MockerFixture):
    ...


@pytest.mark.skip
def test_auto_trader_sell_auto_stock(mocker: MockerFixture):
    ...

