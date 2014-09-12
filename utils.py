import math


def mCn(m, n):
    f = math.factorial
    return f(m) / f(n) / f(m-n)

