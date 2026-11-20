text = input("Enter a string: ").lower()
vowels = {'a' , 'e' , 'i' , 'o' , 'u'}
vowel_count = sum (1 for char in text if char in vowels)
print(f"Number of vowels in the string: {vowel_count}")