import pytest

@pytest.mark.parametrize("i", range(50))
def test_num(i):
    if i in (17, 25):
        pytest.fail("bad luck")

def test_functionality():
    if not 1==0:
        pytest.skip("Some condition not met")
    assert my_function() == expected_value

#def test_my_function():
    #with pytest.raises(ValueError):
        #my_function(-1)

# def test_my_function(monkeypatch):
#     def mock_function():
#         return "mocked result"
#     monkeypatch.setattr("my_module.my_function", mock_function)
    #assert my_module.my_function() == "mocked result"

#class TestMyClass:
    #@pytest.fixture
    #def my_fixture(self):
      #  return "my_fixture"

   # def test_my_function(self, my_fixture):
        # my_function(my_fixture) == "expected_result"