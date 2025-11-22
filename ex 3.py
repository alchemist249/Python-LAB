import random

arr = [[random.randint(1, 100) for i in range(5)] for j in range(5)]

for row in arr:
    print(row)

for row in arr:
    row.sort()
print()

print("after sorting")

for row in arr:
    print(row)

for col in range(5):
    column = []
    for row in range(5):
        column.append(arr[row][col])

    for i in range(5):
        for j in range(i + 1, 5):
            if column[i] > column[j]:
                column[i], column[j] = column[j], column[i]

    for row in range(5):
        arr[row][col] = column[row]

print("\nFinal Matrix after sorting each column:")
for row in arr:
    print(row)
print()