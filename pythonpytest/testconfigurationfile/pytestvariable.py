import pytest
@pytest.mark.parametrize("num,result",[(1,11),(2,22),(3,33)])
def test_param(num,result):
    assert 11*num==result