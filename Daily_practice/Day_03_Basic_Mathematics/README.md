# Day 3 – Basic Mathematics

## Topics Covered

1. Factorial of a Number
2. Fibonacci Series
3. Multiplication Table

## 1. Factorial

Factorial means multiplying a number by all positive integers below it, down to 1.

Example:

`5! = 5 × 4 × 3 × 2 × 1 = 120`

**Important Concepts:**
- Initialize `fact = 1`.
- Use a `for` loop.
- Use `fact = fact * i` to calculate factorial.
- `0! = 1`.

## 2. Fibonacci Series

A series where each number is the sum of the previous two numbers.

Example:

`0, 1, 1, 2, 3, 5, 8, 13...`

**Important Concepts:**
- Initialize `a = 0` and `b = 1`.
- Calculate the next number using `c = a + b`.
- Update using `a = b` and `b = c`.
- Print the current number before updating if the series should start from 0.

## 3. Multiplication Table

Print the multiplication table of a given number.

Example:

For `n = 5`:

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

**Important Concepts:**
- Can be solved using both `for` and `while` loops.
- `range(1, 11)` generates numbers from 1 to 10.
- In a `while` loop, manually increment `i`.
- In a `for` loop, the iterator updates automatically.

## For Loop vs While Loop

| For Loop | While Loop |
|---|---|
| Used when the range is known | Used when a condition controls repetition |
| Automatically updates iterator | Requires manual increment |
| Uses `range()` when needed | Uses a condition |

## Practice Goal

- Solve all three programs independently.
- Practise both loop structures wherever applicable.
- Understand the logic instead of memorizing code.