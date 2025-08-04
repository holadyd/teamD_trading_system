import pytest
from pytest_mock import MockerFixture
from abc import ABC, abstractmethod
from unittest.mock import call
from Driver import Driver
from AutoTradingSystem import AutoTradingSystem


def test_auto_trader_import():
    trader_app = AutoTradingSystem()
    assert trader_app is not None



def test_auto_trader_login(mocker: MockerFixture):
    driver = mocker.Mock(spec=Driver)
    trader_app = AutoTradingSystem()
    trader_app._driver = driver

    trader_app.login('testid', 'testpw')

    driver.login.assert_has_calls([call('testid', 'testpw')])


def test_auto_trader_buy(mocker: MockerFixture):
    driver = mocker.Mock(spec=Driver)
    trader_app = AutoTradingSystem()
    trader_app._driver = driver

    trader_app.buy('stock code', 3000, 5)

    driver.buy.assert_has_calls([call('stock code', 3000, 5)])


def test_auto_trader_sell(mocker: MockerFixture):
    driver = mocker.Mock(spec=Driver)
    trader_app = AutoTradingSystem()
    trader_app._driver = driver

    trader_app.sell('stock code', 3000, 5)

    driver.sell.assert_has_calls([call('stock code', 3000, 5)])


def test_auto_trader_get_price(mocker: MockerFixture):
    driver = mocker.Mock(spec=Driver)
    trader_app = AutoTradingSystem()
    trader_app._driver = driver

    trader_app.get_price('stock code')

    driver.get_price.assert_has_calls([call('stock code')])

def test_login_and_print_nemo(capsys):
    trader_app = AutoTradingSystem()

    trader_app.select_stock_broker("nemo")
    trader_app.login('test_id', 'test_pw')

    captured = capsys.readouterr()
    assert captured.out == "[NEMO]test_id login GOOD\n"

def test_login_and_print_kiwer(capsys):
    trader_app = AutoTradingSystem()

    trader_app.select_stock_broker("kiwer")
    trader_app.buy('test_id', 'test_pw')

    captured = capsys.readouterr()
    assert captured.out == "test_id login success\n"

def test_buy_and_print_nemo(capsys):
    trader_app = AutoTradingSystem()

    trader_app.select_stock_broker("nemo")
    trader_app.buy('1234', 50, 5)

    captured = capsys.readouterr()
    assert captured.out == "[NEMO]1234 buy stock(price: 50 ) *(count : 5)\n"

def test_buy_and_print_kiwer(capsys):
    trader_app = AutoTradingSystem()

    trader_app.select_stock_broker("kiwer")
    trader_app.buy('5678', 99, 10)

    captured = capsys.readouterr()
    assert captured.out == "5678 : Buy stock ( 99 * 10\n"

def test_sell_and_print_nemo(capsys):
    trader_app = AutoTradingSystem()

    trader_app.select_stock_broker("nemo")
    trader_app.sell('1234', 50, 5)

    captured = capsys.readouterr()
    assert captured.out == "[NEMO]1234 sell stock ( price : 50 ) * ( count : 5)\n"

def test_sell_and_print_kiwer(capsys):
    trader_app = AutoTradingSystem()

    trader_app.select_stock_broker("kiwer")
    trader_app.sell('5678', 99, 10)

    captured = capsys.readouterr()
    assert captured.out == "5678 : Sell stock ( 99 * 10\n"

def test_auto_trader_trend_analysis(mocker):
    trader_app = AutoTradingSystem()
    trader_app._driver = mocker.Mock()
    trader_app._driver.get_price.side_effect = [
        150, 100, 200,
        89,90,91,
        100, 0, 101,
        102, 101, 100,
        180, 150, 100,
        200, 103, 102
    ]
    test_stock_code = '1234'

    assert trader_app._trend_analysis(test_stock_code) == '-'
    assert trader_app._trend_analysis(test_stock_code) == 'up'
    assert trader_app._trend_analysis(test_stock_code) == '-'
    assert trader_app._trend_analysis(test_stock_code) == 'down'
    assert trader_app._trend_analysis(test_stock_code) == 'down'
    assert trader_app._trend_analysis(test_stock_code) == 'down'


def test_buy_nice_timing_kiwer_fail(mocker, capsys):
    trader_app = AutoTradingSystem()

    driver = mocker.Mock(spec=Driver)
    trader_app._driver = driver
    trader_app.select_stock_broker("kiwer")
    driver.get_price.side_effect = [150, 100, 200]

    trader_app.buy_nice_timing('1234', 1000)
    captured = capsys.readouterr()

    assert captured.out == ""

