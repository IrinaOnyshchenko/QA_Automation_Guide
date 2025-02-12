import pytest
import requests

def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        i = "hello"
        assert "e" in i

