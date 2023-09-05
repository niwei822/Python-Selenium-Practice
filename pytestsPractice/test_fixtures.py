import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    
    def test_example1(self):
        print("test_example1")
    
    def test_example2(self):
        print("test_example2")
    
    def test_example3(self):
        print("test_example3")
    
    def test_example4(self):
        print("test_example4")