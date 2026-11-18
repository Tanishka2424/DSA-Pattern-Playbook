n = 17

if n % 2 ==0:
    print("Even")
else:
    print("Odd")




arr = [1, 2, 3, 4, 5, 6, 7, 8]


even = []
odd = []


for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)


print("Even numbers:", even)
print("Odd numbers:", odd)   