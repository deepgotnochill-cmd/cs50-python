n = int(input("How many numbers do you want to enter ? "))
original_list =[]
for i in range(n):
    num = int(input("Enter an integer {i+1} :"))
    original_list.append(num)
positive_list = [x for x in original_list if x > 0]    
negative_list = [x for x in original_list if x < 0]
print("\nOriginal List: ", original_list)
print("Positive List: ", positive_list)
print("Negative List: ", negative_list)
