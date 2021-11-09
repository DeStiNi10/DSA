# Decimal to Binary - Recursion
"""
divide num by 2
get int quotient for next iteration
remainder for binary digit
repeat until quotient is 0
"""

def decimal_to_binary(n):
    if int(n/2) == 0:
        return n%2
    else:
        return (n%2) + 10 * decimal_to_binary(int(n/2))

print(decimal_to_binary(13))

# Test commit message