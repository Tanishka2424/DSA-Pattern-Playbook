arr = [ 12, 45, 7, 41, 31, 10]

largest = arr[0]
smallest = arr[0]

for num in arr:
    if num > largest:
        largest = num

    else:
        if num < smallest:
            smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)


