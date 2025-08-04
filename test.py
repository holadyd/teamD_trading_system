from kiwer_api import KiwerAPI
from nemo_api import NemoAPI
import pytest

'''
print('[NEMO]' + '1234' + ' buy stock ( price : ' + str(50) + ' ) * ( count : ' + str(5) + ')')
print('5678' + ' : Buy stock ( ' + str(99) + ' * ' + str(10))
print(stock_code + ' : Buy stock ( ' + str(price) + ' * ' + str(count))
'''
print('5678' + ' : Sell stock ( ' + str(99) + ' * ' + str(10))
print('[NEMO]' + '1234' + ' sell stock ( price : ' + str(50) + ' ) * ( count : ' + str(5) + ')')

@pytest.mark.skip
def test_capsys(capsys):
    kiwer = KiwerAPI()
    nemo = NemoAPI()

    kiwer.login('teamD', '1234')
    captured = capsys.readouterr()
    assert captured.out == "teamD login success\n"

    kiwer.buy(1234, 50, 5)
    kiwer.sell(1234, 25, 10)

    nemo.cerification('teamD', '1234')
    nemo.purchasing_stock(5678, 100, 50)
    nemo.selling_stock(5678, 200, 25)

    captured = capsys.readouterr()
    assert captured.out == "hello\n"