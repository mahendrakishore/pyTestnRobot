import pytest


@pytest.fixture(scope="module")
def setup():
    print("setup===============")

    yield
    print("tear down============")
# def teardown():
#     print("tear down")

def test_func(setup):
    assert True
    print("main funcctions")
