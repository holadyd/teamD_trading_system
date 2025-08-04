import pytest


class TestBroker:
    def login(self):
        ...

    def buy(self):
        ...

    def sell(self):
        ...

    def get_price(self):
        ...

def test_auto_trader_import():
    trader_app = AutoTradingSystem()
    assert trader_app is not None


@pytest.mark.skip
def test_auto_trader_select_broker(mocker):
    trader_app = AutoTradingSystem()
    trader_app.select_broker(TestBroker)
    assert trader_app.broker is not None

@pytest.mark.skip
def test_auto_trader_sell_stock():
    ...


@pytest.mark.skip
def test_auto_trader_sell_stock():
    ...


@pytest.mark.skip
def test_auto_trader_buy_auto_system_():
    ...


@pytest.mark.skip
def test_auto_trader_sell_auto_stock():
    ...

