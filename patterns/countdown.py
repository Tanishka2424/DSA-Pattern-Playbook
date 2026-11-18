# Pattern 01: Recursion
# Problem: Print numbers from n down to 1.


def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n-1)

countdown(3)    