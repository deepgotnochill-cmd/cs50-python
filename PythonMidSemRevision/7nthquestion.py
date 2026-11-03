#Write a Python program to count number of vowels using sets in given string.
user_string = input("Enter a string: ")
vowels = {'a','e','i','o','u','A','E','I','O','U'}
count = 0
for char in user_string:
    if char in vowels:
      count += 1
print(f"Total number of vowels: {count}")      