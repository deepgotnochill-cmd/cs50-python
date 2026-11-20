import math
def add(x,y): return x + y
def substract(x,y): return x - y
def multiply(x,y): return x * y
def divide(x,y): return x / y if y != 0 else "Cannot divide by zero"

while True:
    print("\n---CALCULATOR MENU ---")
    print("1. Basic Arithmetic( + , - , * , /)")
    print("2. Log(x)")
    print("3. Sin(x)")
    print("4. Cos(x)")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter Second number: "))
        op = input("Enter operator ( + , - , * , /): ")
        if op == '+': print("Result: ", add(a,b))
        elif op == '-': print("Result: ", substract(a,b))
        elif op == '*': print("Result: ",multiply(a,b))
        elif op =='/': print("Result: ", divide(a,b))
    elif choice == 2:
        x = float(input("Enter value for x: "))
        print("Result: ",math.log10(x)) 
    elif choice == 3:
        x = float(input("Enter value for x (in radians):"))
        print("Result: ", math.sin(x))
    elif choice == 4:
        x = float(input("Enter value for x (in radians): "))
        print("Result:", math.cos(x))
    elif choice == 5:
        print('Exiting...')
        break
    else:
        print("Invalid choice!")            
