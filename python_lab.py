
# ============================================================
# PYTHON LAB - 20 IN 1 PROGRAMMING TOOLKIT
# Author: Deep Datta Chaudhury
# Description: A collection of 20 Python programming problems
# ============================================================

def line():
    print("-" * 55)


def even_odd():
    n = int(input("Enter a number: "))
    print("Even" if n % 2 == 0 else "Odd")


def largest_three():
    a, b, c = map(int, input("Enter three numbers: ").split())
    print("Largest:", max(a, b, c))


def leap_year():
    year = int(input("Enter year: "))
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")


def factorial():
    n = int(input("Enter number: "))
    if n < 0:
        print("Factorial is not defined for negative numbers")
        return

    result = 1
    for i in range(1, n + 1):
        result *= i
    print("Factorial:", result)


def prime():
    n = int(input("Enter number: "))
    if n < 2:
        print("Not Prime")
        return

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            return
    print("Prime")


def fibonacci():
    n = int(input("Enter number of terms: "))
    if n < 0:
        print("Enter a non-negative number")
        return

    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


def armstrong():
    n = int(input("Enter number: "))
    if n < 0:
        print("Not Armstrong")
        return

    digits = str(n)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    print("Armstrong" if total == n else "Not Armstrong")


def reverse_number():
    n = int(input("Enter number: "))
    sign = -1 if n < 0 else 1
    reversed_num = int(str(abs(n))[::-1]) * sign
    print("Reversed:", reversed_num)


def palindrome_number():
    n = input("Enter number: ")
    print("Palindrome" if n == n[::-1] else "Not Palindrome")


def sum_digits():
    n = input("Enter number: ").strip()
    if not n.isdigit():
        print("Please enter a non-negative integer")
        return
    print("Sum of digits:", sum(int(d) for d in n))


def palindrome_string():
    text = input("Enter string: ")
    cleaned = text.replace(" ", "").lower()
    print("Palindrome" if cleaned == cleaned[::-1] else "Not Palindrome")


def count_vowels():
    text = input("Enter string: ").lower()
    vowels = sum(1 for ch in text if ch in "aeiou")
    consonants = sum(1 for ch in text if ch.isalpha() and ch not in "aeiou")
    print("Vowels:", vowels)
    print("Consonants:", consonants)


def largest_smallest_list():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    if not numbers:
        print("List is empty")
        return
    print("Largest:", max(numbers))
    print("Smallest:", min(numbers))


def list_sum_average():
    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
    if not numbers:
        print("List is empty")
        return
    print("Sum:", sum(numbers))
    print("Average:", sum(numbers) / len(numbers))


def remove_duplicates():
    numbers = list(map(int, input("Enter numbers: ").split()))
    unique = list(dict.fromkeys(numbers))
    print("Without duplicates:", unique)


def prime_function():
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    n = int(input("Enter number: "))
    print("Prime" if is_prime(n) else "Not Prime")


def gcd():
    a, b = map(int, input("Enter two numbers: ").split())
    x, y = abs(a), abs(b)

    while y:
        x, y = y, x % y

    print("GCD:", x)


def bubble_sort():
    numbers = list(map(int, input("Enter numbers: ").split()))

    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print("Sorted list:", numbers)


def student_topper():
    students = {}
    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input(f"Enter student {i+1} name: ")
        marks = float(input("Enter marks: "))
        students[name] = marks

    if not students:
        print("No student records")
        return

    topper = max(students, key=students.get)
    print("Student Records:", students)
    print("Topper:", topper)
    print("Marks:", students[topper])


def character_frequency():
    text = input("Enter a string: ")
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    print("Character Frequency:")
    for char, count in frequency.items():
        print(repr(char), ":", count)


# All 20 programs in one menu
PROGRAMS = {
    1: ("Even or Odd", even_odd),
    2: ("Largest of Three Numbers", largest_three),
    3: ("Leap Year", leap_year),
    4: ("Factorial", factorial),
    5: ("Prime Number", prime),
    6: ("Fibonacci Series", fibonacci),
    7: ("Armstrong Number", armstrong),
    8: ("Reverse a Number", reverse_number),
    9: ("Number Palindrome", palindrome_number),
    10: ("Sum of Digits", sum_digits),
    11: ("String Palindrome", palindrome_string),
    12: ("Count Vowels and Consonants", count_vowels),
    13: ("Largest and Smallest in List", largest_smallest_list),
    14: ("List Sum and Average", list_sum_average),
    15: ("Remove Duplicate Elements", remove_duplicates),
    16: ("Prime Using Function", prime_function),
    17: ("GCD / HCF", gcd),
    18: ("Bubble Sort", bubble_sort),
    19: ("Student Marks and Topper", student_topper),
    20: ("Character Frequency", character_frequency)
}


def main():
    while True:
        print("\n")
        line()
        print("       PYTHON LAB - PROGRAMMING TOOLKIT")
        line()

        for number, (name, _) in PROGRAMS.items():
            print(f"{number:02d}. {name}")

        print("00. Exit")
        line()

        try:
            choice = int(input("Select a program (0-20): "))

            if choice == 0:
                print("Thank you for using Python Lab!")
                break

            if choice in PROGRAMS:
                name, function = PROGRAMS[choice]
                print(f"\n>>> Running: {name}")
                line()
                function()
                line()
            else:
                print("Invalid choice. Select between 0 and 20.")

        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except (EOFError, KeyboardInterrupt):
            print("\nProgram terminated.")
            break


if __name__ == "__main__":
    main()
