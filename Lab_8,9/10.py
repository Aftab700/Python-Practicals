# 10. Python function to Find Factorial of Number Using Recursion

def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(4))
