n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    c = 1

    for j in range(1, i + 1):
        print(c, end=" ")
        c = int(c * (i - j) / j)

    print()