import pytest
from pytest_mock import MockerFixture
from abc import ABC,abstractmethod

class TestBroker(ABC):
    @abstractmethod
    def select_stock_broker(self):
        ...

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

    @abstractmethod
    def buy_nice_timing(self):
        ...

    @abstractmethod
    def sell_nice_timing(self):
        ...


@pytest.mark.skip
def test_auto_trader_import():
    trader_app = AutoTradingSystem()
    assert trader_app is not None

@pytest.mark.skip
def test_auto_trader_select_broker(mocker: MockerFixture):
    trader_app = AutoTradingSystem()
    trader_app.select_broker(TestBroker)
    assert trader_app.broker is not None

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

