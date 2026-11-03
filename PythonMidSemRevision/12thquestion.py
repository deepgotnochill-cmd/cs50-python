numbers = [ 1 , 2 , 3 , 4 , 5 ]
cube_tuples = [(num,num ** 3) for num in numbers]
print(f"Original list: {numbers}")
print(f"List of Tuples (Number , Cube): {cube_tuples}")