#Write a python program to print Fibonacci series up to a certain limit (use 'While')
limit = int(input("Enter the limit for the Fibonacci series: "))
a,b = 0,1
print("Fibonacci series: ")
while a <= limit:
    print(a , end= " ")
    a , b = b, a+b
    print()