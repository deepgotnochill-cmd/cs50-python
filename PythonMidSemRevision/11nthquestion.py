n = int(input("How many numbers you want to add: "))
original_list = []
for i in range(n):
    num = int(input(f"Enter integer {i+1}: "))
    original_list.append(num)
positive_list = [x for x in original_list if x >= 0]
negative_list = [x for x in original_list if x <= 0]
print(f"\nOriginal List: {original_list}")
print(f"Positive Number List: {positive_list}")
print(f"Negative Numbers LIst: {negative_list}")
