# Sum of Digits - Recursion
"""
12345 = 1 + 2 + 3 + 4 + 5 = 15

n = 12345
n/10 = 1234
n/10 = 123
n/10 = 12
n/10 = 1
1/10 = 0.1
x = n%10 = 5
x + sumdigit(n/10)
"""

def sumdigit(n):
    if int(n/10) < 1:
        return int(n)
    else:
        return int(n%10) + sumdigit(int(n/10))

print(sumdigit(12345))