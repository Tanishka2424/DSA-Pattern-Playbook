arr = [1, 2, 3, 4, 5, 6, 7, 8]

freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1

    else:
        freq[i] = 1

print(freq)