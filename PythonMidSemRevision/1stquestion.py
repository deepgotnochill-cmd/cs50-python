#Write a python menu driven program to calculate the area of circle, rectangle , square using if - elif - else
#Answer :
import math
print("---Area Calculator Menu---")
print("1) Area of Circle")
print("2) Area of Rectangle")
print("3)Area of Square")
choice = int(input("Enter your choice(1-3):"))
if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is: {area:.2f}")
elif choice == 2:
    length = float(input("Enter the side of the rectangle"))
    breadth = float(input("Enter the width of the rectangle"))
    area = length * breadth
    print(f"The area of the square {area:.2f}")
elif choice == 3:
    side = float(input("Enter the side of the square: "))
    area = side ** 2
    print(f"The area of the square is: {area:.2f}")
else:
    print("Invalid choice! Please select a valid option.")    
        
