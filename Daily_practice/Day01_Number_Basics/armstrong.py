n = int(input("Enter a number: "))
temp = n
power = len(str(n))
total = n

while n > 0:
    digit = n % 10
    total = total + digit ** power
    n = n // 10

if total == temp:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")