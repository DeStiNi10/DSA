# Power Calculation - Recursion
"""
x^n = x * x^n-1
2 ^ 5 = 2 * 2 ^ 4

"""

def power(x, n):
    assert (int(x) >= 0 and int(n) >= 0) and (int(x)==x and int(n)==n), 'x and n have to be positive'
    if n<1:
        return 1
    else:
        return x * power(x, n-1)

print(power(3,3))