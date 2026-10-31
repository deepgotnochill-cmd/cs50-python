import math
print("1. circle\n2. Rectangle\n3. Square")
choice=int(input("Enter your choice (1-3): "))
if choice == 1:
    r=float(input("Enter Radius: "))
    print(f"Area of circle ={math.pi *(r**2):.2f}")
elif choice == 2:
    l= float(input("Enter length: "))
    b= float(input("Enter breadth: "))
    print(f"Area of Rectangle ={l*b:.2f}")
elif choice == 3:
    s= float(input("Enter side: "))
    print(f"Area of Square ={s**2:.2f}")
else:
    print("Invalid choice!")        