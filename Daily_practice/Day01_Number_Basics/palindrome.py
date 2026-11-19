n = int(input("Enter a number: "))

temp = n 
rev = 0

while n > 0:
    digit = n % 10
    rev = rev  * 10 + digit
    n = n // 10


if rev == temp:
    print("The number is a palindrome.")

else:
    print("The number is not a palindrome.")        