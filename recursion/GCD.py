# Greatest Common Divisor - Recursion
"""
Greatest common divisor for 2 numbers
not all 0
gcd(x,y)
"""

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

print(gcd(8,12))