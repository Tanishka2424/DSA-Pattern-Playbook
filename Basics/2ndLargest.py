arr = [10, 20, 4, 45, 99]


second_largest = arr[0]
largest = arr[0]

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num

    else:
        if num > second_largest:
            second_largest = num
            


print("Second largest number:", second_largest)
