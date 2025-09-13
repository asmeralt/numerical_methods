from src.examples.example1 import very_important_function

import pytest


def test_1():
    assert very_important_function(3, 2) == 1


def test_2():
    assert very_important_function(3.0, 2.0) == 1.0


def test_3():
    with pytest.raises(ZeroDivisionError) as e_info:
        very_important_function(3, 0)

    assert str(e_info.value) == "integer division or modulo by zero"
