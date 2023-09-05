import pytest

@pytest.mark.smoke
@pytest.mark.skip
#-m smoke
#fixtures are used to set up and teardown the environment, conftest.py is used to set up the environment
#fixtures is available for all tests
def test_hello():
    print("hello")

@pytest.mark.xfail
def test_hello2():
    print("hello2")

def test_fixture(setup):
    print("I will execute fixture")