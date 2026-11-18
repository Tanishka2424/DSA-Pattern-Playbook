# Pattern 01: Recursion
# Problem: Calculate the sum of numbers from 1 to n.

def sum_n(n):

    if n == 0:
        return 0


    return n + sum_n(n - 1)


result = sum_n(6)

print("Sum:", result)