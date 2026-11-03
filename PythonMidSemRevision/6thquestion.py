#Write a python programs to illustrate the various functions of the "Math" module, "Statistics" module in python
import math
import statistics
print("---Math Module Functions---")
print(f"Square root of 16:{math.sqrt(16)}")
print(f"Factorial of 5 is: {math.factorial(5)}")
print(f"Ceil of 4.3 is :{math.ceil(4.3)}")
print(f"Floor of 4.7: {math.floor(4.7)}")
print(f"Power (2 ^ 3) :{math.pow(2,3)}")
data = [2,4,4,4,5,5,7,9]
print("\n---Statistics Module Functions---")
print(f"Data Sets:{data}")
print(f"Mean:{statistics.mean(data)}")
print(f"Median:{statistics.median(data)}")
print(f"Mode:{statistics.mode(data)}")
print(f"Standard Deviation:{statistics.stdev(data)}")