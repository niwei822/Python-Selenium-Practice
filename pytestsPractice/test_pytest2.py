import pytest

@pytest.mark.regression
def test_addition(setup):
    a = 2
    b = 3
    print("a + b = ", a + b)
    assert a + b == 5