#Write a python program to print the pascal triangle.
rows = int(input("Enter the number of rows for Pascal's Triangle: "))
for i in range(rows):
    print(" " * (rows - i), end = " ")
    val = 1
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()    