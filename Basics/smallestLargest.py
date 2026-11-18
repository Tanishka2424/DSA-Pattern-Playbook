arr = [12, 45, 2, 41, 31, 10]

smallest = arr[0]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print(largest)    