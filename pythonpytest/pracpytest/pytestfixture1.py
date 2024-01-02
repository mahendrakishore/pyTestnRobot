import pytest
@pytest.f
def test_input_total_div_5(input_total):
    assert input_total%5==0

def test_input_total_div_10(input_total):
    assert input_total%10==0

def test_input_total_div_09(input_total):
    assert input_total%9==0
