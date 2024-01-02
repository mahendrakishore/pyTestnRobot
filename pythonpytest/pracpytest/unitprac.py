import pytest


def test_value():
    a=1
    b=2
    assert a+b==3,"test failed"

def value_test():
    a=1
    b=2
    assert a+b==3;"value test failed"

@pytest.mark.login
def test_login_meth():
    print("this is marker")
    assert True

def test_parallel1():
      assert True
      print("this is prallel1")


def test_parallel2():
    assert True
    print("this is prallel2")