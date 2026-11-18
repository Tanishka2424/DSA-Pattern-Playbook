arr = [1, 2, 3, 4, 5, 2, 3, 4]


seen = []
dup = []

for i in arr:
    if i in seen:
        if i not in dup:
            dup.append(i)

    else:
        seen.append(i)

print(dup)
