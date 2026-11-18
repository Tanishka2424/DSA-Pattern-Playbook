# Pattern 01: Recursion
# Problem: Calculate factorial of n.


def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n-1)


result = factorial(5)
print("Factorial:", result)