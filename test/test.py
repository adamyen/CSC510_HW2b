def get_pow(base, exponent):
    res = base
    for i in range(exponent - 1):
        res = res * base
    return res

def test_pow():
    assert get_pow(9, 3) == 729
    assert get_pow(7, 3) == 343
    assert get_pow(13, 4) == 28561