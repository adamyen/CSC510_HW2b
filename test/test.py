# content of test_sample.py

def pow(base, exponent):
    res = base
    for i in range(exponent - 1):
        res = res * base
    return res

def test_pow():
    assert pow(9, 3) == 729
    assert pow(7, 3) == 343
    assert pow(13, 4) == 28561