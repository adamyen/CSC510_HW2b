from code import get_pow

def test_pow():
    assert get_pow(9, 3) == 729
    assert get_pow(7, 3) == 343
    assert get_pow(13, 4) == 28561