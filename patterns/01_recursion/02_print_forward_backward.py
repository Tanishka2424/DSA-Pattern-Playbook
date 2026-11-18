# Pattern 01: Recursion
# Problem: Understand execution before and after recursive calls.

def fun(n):

    if n == 0:
        return

    print("Going:", n)

    fun(n - 1)

    print("Returning:", n)


fun(3)    