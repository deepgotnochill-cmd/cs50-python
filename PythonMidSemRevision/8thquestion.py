#Write a Python program to Remove all duplicates from a given string in python
user_string = input("Enter a string: ")
seen = set()
result = []
for char in user_string:
    if char not in seen:
        seen.add(char)
        result.append(char)
clean_string = "".join(result)
print(f"String after removing duplicates: {clean_string}")        