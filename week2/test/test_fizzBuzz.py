import pytest
from lib.fizzBuzz import PepsiCoke

def test_one():
    fizz = PepsiCoke(1)
    assert fizz == 1

def test_one():
    fizz = PepsiCoke(2)
    assert fizz == 2


def test_two():
    fizz = PepsiCoke(3)
    assert fizz == 'Pepsi'


def test_three():
    fizz = PepsiCoke(5)
    assert fizz == 'Coke'


def test_four():
    fizz = PepsiCoke(6)
    assert fizz == 'Pepsi'


def test_five():
    fizz = PepsiCoke(10)
    assert fizz == 'Coke'


def test_six():
    fizz = PepsiCoke(15)
    assert fizz == 'PepsiCoke'

def test_fail():
    fizz = PepsiCoke(4)
    assert fizz == 'Coke'

def test_pass():
    fizz = PepsiCoke(13)
    assert fizz == False