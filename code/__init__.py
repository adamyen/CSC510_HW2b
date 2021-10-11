def pow(base, exponent):
    res = base
    for i in range(exponent - 1):
        res = res * base
    return res