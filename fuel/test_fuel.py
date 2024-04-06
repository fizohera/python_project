import pytest
from fuel import convert, gauge

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_numetator():
    with pytest.raises(ValueError):
        convert("3/1")
    with pytest.raises(ValueError):
        convert("cat/2")
    with pytest.raises(ValueError):
        convert("dog/cat")
def test_valid_value():
    assert convert("2/3") == 67
    assert convert("1/2") == 50
    assert convert("2/2") == 100

def test_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
def test_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
def test_any():
    assert gauge(78) == "78%"
    assert gauge(25) == "25%"

