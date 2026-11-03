import math

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error! Division by zero."

def log_base10(x): return math.log10(x) if x > 0 else "Error! Domain error."
def sine(x): return math.sin(math.radians(x))
def cosine(x): return math.cos(math.radians(x))

print("--- Calculator Menu ---")
print("1. Basic Operations (+, -, *, /)")
print("2. Scientific Operations (log10, sin, cos)")
choice = int(input("Select mode (1 or 2): "))

if choice == 1:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")
    
    if op == '+': print(f"Result: {add(a, b)}")
    elif op == '-': print(f"Result: {subtract(a, b)}")
    elif op == '*': print(f"Result: {multiply(a, b)}")
    elif op == '/': print(f"Result: {divide(a, b)}")
    else: print("Invalid operator choice.")

elif choice == 2:
    print("a. log10(x)\nb. sin(x) [in degrees]\nc. cos(x) [in degrees]")
    op = input("Select function (a, b, or c): ")
    val = float(input("Enter target value: "))
    
    if op == 'a': print(f"Result: {log_base10(val)}")
    elif op == 'b': print(f"Result: {sine(val):.4f}")
    elif op == 'c': print(f"Result: {cosine(val):.4f}")
    else: print("Invalid function choice.")
else:
    print("Invalid Selection.")
