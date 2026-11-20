numbers = [10, -5, 3 , -1 , 0 , 8 , -12 , 14]
pos_count = sum(1 for x in numbers if x > 0)
neg_count = sum(1 for x in numbers if x < 0)
print(f"List: {numbers}")
print(f"Positive numbers: {pos_count}")
print(f"Negative numbers: {neg_count}")