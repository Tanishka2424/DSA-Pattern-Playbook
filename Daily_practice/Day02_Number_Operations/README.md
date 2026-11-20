# Day 2 – Number Operations

## Topics Covered
1. Reverse a Number
2. Sum of Digits
3. Count Digits

## Important Concepts

### 1. Reverse a Number
Example: 1234 → 4321

Logic:
- Extract the last digit.
- Add it to the reverse.
- Remove the last digit.

### 2. Sum of Digits
Example: 456 → 4 + 5 + 6 = 15

Logic:
- Extract each digit.
- Add it to total.
- Remove the last digit.

### 3. Count Digits
Example: 4567 → 4 digits

Logic:
- Initialize count = 0.
- Increase count by 1.
- Remove one digit in each iteration.

## Most Important: % 10 vs // 10

| Operator | Purpose | Example |
|---|---|---|
| `% 10` | Extract last digit | 456 % 10 = 6 |
| `// 10` | Remove last digit | 456 // 10 = 45 |

Remember:
- `% 10` gives the remainder (last digit for a positive integer).
- `// 10` gives the integer quotient (removes the last digit).

## Practice Goal
Solve all three programs independently without looking at previous solutions.

