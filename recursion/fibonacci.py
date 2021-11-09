#Fibonacci Number - Recursion

def fibonacci(n):
    #Unintentional Case
    assert n >= 0 and int(n) == n, 'n cannot be less than 1 and n has to be an integer'
    #Base Case
    if n in [0,1]:
        return n
    else:
        #Recursive case
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))