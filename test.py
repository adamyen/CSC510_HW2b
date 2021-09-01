import math

# content of test_sample.py
def inc(x):
    return x + 1

def pow(base, exponent):
    return math.pow(base, exponent)

def test_answer():
    assert inc(3) == 4

def test_pow():
    assert pow(9, 3) = 729.0