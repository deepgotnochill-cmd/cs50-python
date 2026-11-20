num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
def find_hcf(x,y):
    while y : 
        x , y = y , x % y
        return x
print(f"The HCF of {num1} and {num2} is {find_hcf(num1,num2)}")    
