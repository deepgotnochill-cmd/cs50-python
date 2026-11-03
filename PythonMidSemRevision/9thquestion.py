numbers = [12, -7 , 5 , 64, -14, 0 , -3 ,8]
pos_count = 0
neg_count = 0
for num in numbers:
    if num > 0:
        pos_count += 1
    elif num < 0:
        neg_count = 1
print(f"List:{numbers}") 
print(f"Positive Numbers count: {pos_count}")     
print(f"Negative Numbers count: {neg_count}")    