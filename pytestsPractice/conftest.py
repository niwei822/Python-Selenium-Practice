import pytest

#scope="class": The fixture will be executed once per test class. 
#scope="class" sets up and tears down the fixture for each test class, while scope="session" sets up and tears down the fixture once 
# for the entire test session.
@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")