# ==========================================
# MODULE 1: VARIABLE TYPES & OPERATORS
# ==========================================

# print("Hello, World of python!")

name = "Gazi Taoshif"
age = 21
height = 5.11
is_student = True

# print("Name:", name)
# print("Age:", age)
# print("Height:", height)
# print("Is Student:", is_student)

# print(
#     f"My name is {name}, I am {age} years old, my height is {height} feet and it is {is_student} that I am a student."
# )

# print("Type of name:", type(name))                <class 'str'>
# print("Type of age:", type(age))                  <class 'int'>
# print("Type of height:", type(height))            <class 'float'>
# print("Type of is_student:", type(is_student))    <class 'bool'>


# ==========================================
# MODULE 2: TYPE CONVERSION
# ==========================================

num_string = "23"
num_int = 27

# print(f"Type of {num_string} is {type(num_string)}")

num_string = int(num_string)

# print(f"Type of {num_string} is {type(num_string)}")

num_sum = num_string + num_int
# print(f"Sum is {num_sum} & type is {type(num_sum)}")

num1 = int(2.3)
# print(num1)

num2 = int(-2.8)
# print(num2)

num3 = float(5)
# print(num3)

num4 = complex("3+5j")
# print(num4)


# ==========================================
# MODULE 3: INPUT/OUTPUT
# ==========================================

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

date_of_birth = 2024 - age

# print(f"Hello, {name}! You were born in {date_of_birth}.")


# ==========================================
# MODULE 4: OPERATORS
# ==========================================

a = 7
b = 2

sum_result = a + b
difference_result = a - b
product_result = a * b
quotient_result = a / b

# print("Sum:", sum_result)
# print("Difference:", difference_result)
# print("Product:", product_result)
# print("Quotient:", quotient_result)
# print("Floor Division: ", a // b)
# print("Modulo: ", a % b)
# print("Power: ", a**b)

# print(f"sum: {a + b}, difference: {a - b}, product: {a * b}, quotient: {a / b}, floor division: {a // b}, modulo: {a % b}, power: {a ** b}")

a += b
# print(a)


# ==========================================
# MODULE 5: COMPARISON, LOGICAL & CONTROL FLOW
# ==========================================

a = 5
b = 2

#! equal to operator
# print('(a == b)--> ', a == b)

#! not equal to operator
# print('(a != b)--> ', a != b)

#! greater than operator
# print('(a > b)--> ', a > b)

#! less than operator
# print('(a < b)--> ', a < b)

#! greater than or equal to operator
# print('(a >= b)--> ', a >= b)

#! less than or equal to operator
# print('(a <= b)--> ', a <= b)


# Logical Operators

#! logical AND
# print(True and True)
# print(True and False)

#! logical OR
# print(True or False)

#! logical NOT
# print(not True)


# ==========================================
# MODULE 6: IF STATEMENTS
# ==========================================

# number = int(input("Enter a number: "))

# if number > 0:
#     print("The number is positive.")
# else:
#     print("The number is not positive.")


# ==========================================
# MODULE 7: IF-ELIF-ELSE STATEMENTS
# ==========================================

# if number == 0:
#     print("The number is zero.")
# elif number > 0:
#     print("The number is positive.")
# else:
#     print("The number is negative.")


# ==========================================
# MODULE 8: NESTED IF STATEMENTS
# ==========================================

# age = int(input("Enter your age: "))

# if age >= 19:
#     if age == 21:
#         print("You are 21 years old, the age of majority in many countries!")
#     elif age > 60:
#         print("You are a senior citizen.")
#     elif age > 30:
#         print("You are a middle-aged adult.")
#     else:
#         print("You are an teenager.")

# else:
#     if age == 18:
#         print("Now you can vote for the first time!")
#     else:
#         print("You are an kid.")


# ==========================================
# MODULE 9: FOR LOOPS
# ==========================================

# for i in range(stop):
# for i in range(start, stop):
# for i in range(stop, start, step):

# for i in range(5):
# print(f"Iteration {i+1}")

i = 1
inc = 2
end = 10
# for i in range(i, end, inc):
#     print(f"Current value: {i}")

numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(f"Numbers: {number*2}")

languages = ["Python", "Java", "C++", "JavaScript"]

# for language in languages:
#     print(f"I love {language}!")

# for number in numbers:
#     if number % 2 == 0:
#         print(f"{number} is even.")
#     else:
#         print(f"{number} is odd.")


# for number in numbers:
#     if number == 3:
#         # continue/break
#     print(f"Current number: {number}")


# ==========================================
# MODULE 10: NESTED FOR LOOPS
# ==========================================

fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "black"]

# for fruit in fruits:
#     for color in colors:
# print(fruit, color)


# ==========================================
# RIGHT-ANGLED DOT/NUMBER TRIANGLE
# ==========================================
# rows = 5

# for i in range(1, rows + 1):
#     for j in range(i):
#         # print(f"{j+1}", end="")   # prints numbers instead of dots
#         print(".", end="")          # end=" " keeps dots on the same line
#     print()                         # Moves to the next line after each row

# for i in range(1,6):
#     for j in range(i):
#         print(f"{j+1}", end=" ")
#     print()

# ==========================================
# FLOYD'S TRIANGLE
# ==========================================
# rows = 4
# current_number = 1

# for i in range(1, rows + 1):
#     for j in range(i):
#         print(f"{current_number}", end=" ")
#         current_number += 1
#     print()


# ==========================================
# MULTIPLICATION GRID
# ==========================================
# size = 5

# for i in range(1, size+1):
#     for j in range(1, size+1):
#         print(f"{i*j :3}", end=" ")  # :3 formats the number to be right aligned in a field of width 3
#     print()


# ==========================================
# PYRAMID OF STARS
# ==========================================
# rows = 5

# for i in range(rows):
#     for j in range(rows - i - 1):
#         print(" ", end="")
#     for k in range(2 * i + 1):
#         print("*", end="")
#     print()


# ==========================================
# MODULE 11: MATHEMATICAL FUNCTIONS
# ==========================================
import math

# ==========================================
# TRIGONOMETRIC FUNCTIONS
# ==========================================
# degrees = 30

# print(f"Sine {degrees} value: {math.sin(math.radians(degrees))}")
# print(f"Cosine {degrees} value: {math.cos(math.radians(degrees))}")
# print(f"Tangent {degrees} value: {math.tan(math.radians(degrees))}")


# ==========================================
# LOGARITHMIC & EXPONENTIAL FUNCTIONS
# ==========================================
# print(f"Natural logarithm of 10: {math.log(10)}")
# print(f"Base-10 logarithm of 100: {math.log10(100)}")
# print(f"Exponential of 2: {math.exp(2)}")


# ==========================================
# CONSTANTS
# ==========================================
# print(f"Value of Pi: {math.pi}")
# print(f"Value of Euler's number, e: {math.e}")


# ==========================================
# MODULE 12: PYTHON LISTS
# ==========================================
# colors = ["red", "black", "blue"]

# print("Colors: ", colors)

# ==========================================
# ACCESSING ELEMENTS IN A LIST
# ==========================================
# print("First color:", colors[0])
# print("Last color:", colors[2])
# print("Last color:", colors[-1])
# print("Sliced colors:", colors[-2:])

# colors[0] = 'Green'
# print("Modified list after changing the first color to Green:", colors)

# ==========================================
# LIST OPERATIONS
# ==========================================
# print("Number of colors in the list:", len(colors))
# print("Reversed list of colors:", list(reversed(colors)))

# Checking if an element is in the list
# print("Is 'Green' present in the list?", 'red' in colors)

# ==========================================
# ITERATING OVER A LIST
# ==========================================
# print("Iterating over the list of colors:")
# for color in colors:
#     print(color)

# ==========================================
# LIST SORTING
# ==========================================
# my_list = [2, 1, 4, 5, 3]
# print("Sorted list of colors:", sorted(my_list))

# ==========================================
# MODULE 13: TUPLES
# ==========================================

# TODO- 1. Once a tuple is created, its elements cannot be modified, added, or removed. (Immutable)
# TODO- 2. Elements in a tuple can be accessed using their index, starting from 0 for the first element.
# TODO- 3. A tuple can hold elements of different types, including other tuples.

# ==========================================
# DECLARING A TUPLE
# ==========================================
# my_tuple = (1, 2, 3, "a", "b", "c")

# print("Tuple:", *my_tuple)

# ==========================================
# ACCESSING ELEMENTS IN A TUPLE
# ==========================================
# print("First element:", my_tuple[0])
# print("Last element:", my_tuple[-1])
# print("Slicing tuple:", my_tuple[2:5])

# print(f"Length of the tuple: {len(my_tuple)}")
# print(f"Reversed tuple: {tuple(reversed(my_tuple))}")
# print(f"Is 'a' present in the tuple? {'a' in my_tuple}")

# ==========================================
# ITERATING OVER A TUPLE
# ==========================================
# print("Iterating through the tuple:")
# for item in my_tuple:
#     print(item)

# print("Iterating through the tuple: " + ", ".join(str(item) for item in my_tuple))
# print("Iterating through the tuple:", *my_tuple, sep=", ")


# ==========================================
# MODULE 14: LIST TUPLE CONVERSION
# ==========================================

# fruits = ('apple','banana','orange')

# Convert a tuple to a list
# tuple_as_list = list(fruits)
# print(f"Tuple converted to list: {tuple_as_list}")

# ==========================================
# CONVERT LIST TO TUPLE
# ==========================================
# list_as_tuple = tuple(tuple_as_list)
# print(f"List converted back to tuple: {list_as_tuple}")

# ==========================================
# LIST, TUPLE, SET & DICTIONARY SYNTAX COMPARISON
# ==========================================
# list = [1, 2, 3, 4, 5]
# tuple = (1, 2, 3, 4, 5)
# set = {1, 2, 3, 4, 5}
# dict = {"one": 1, "two": 2, "three": 3}

# ==========================================
# MODULE 15: CREATING A SET
# ==========================================
# toys = {'car', 'plane', 'animal'}
# print(f"Initial set: {toys}")

# toys.add('doll')
# print(f"After adding 'doll': {toys}")

# toys.remove('animal')
# print(f"After removing 'animal': {toys}")

# ==========================================
# CHECKING MEMBERS IN A SET
# ==========================================
# print(f"Is 'car' in the set? {'car' in toys}")
# print(f"Is 'ball' in the set? {'ball' in toys}")

# ==========================================
# LENGTH OF A SET
# ==========================================
# print(f"Length of the set: {len(toys)}")

# ==========================================
# CLEARING A SET
# ==========================================
# toys.clear()
# print(f"Cleared set: {toys}")
# print(f"Length of the set: {len(toys)}")


# ==========================================
# MODULE 16: SET OPERATIONS: UNION, INTERSECTION, DIFFERENCE & SYMMETRIC DIFFERENCE
# ==========================================

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# union_set = set1.union(set2)

# print(f"Union of set1 and set2: {union_set}")

# intersection_set = set1.intersection(set2)
# print(f"Intersection of set1 and set2: {intersection_set}")

# difference_set = set1.difference(set2)
# print(f"Difference of set1 and set2 ({set1} - {set2}): {difference_set}")

# difference_set2 = set2.difference(set1)
# print(f"Difference of set1 and set2 ({set2} - {set1}): {difference_set2}")

# symmetric_difference_set = set1.symmetric_difference(set2)
# print(f"Symmetric difference of {set1} & {set2}: {symmetric_difference_set}")     # {1, 2, 5, 6}


# ==========================================
# MODULE 17: PYTHON DICTIONARIES
# ==========================================

# TODO- A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.
# TODO- Dictionaries are mutable, meaning you can change their content after creation.

# ==========================================
# CREATING A DICTIONARY
# ==========================================
# student = {
#     "name": "Taoshif",
#     "age": 21,
#     "grade": "A+"
# }

# print(f"Student: {student}")
# print("Student:", *student.values(), sep=" - ")

# ==========================================
# ACCESSING VALUES IN A DICTIONARY
# ==========================================
# print(f"Name: {student['name']}")
# print(f"Age: {student['age']}")
# print(f"Grade: {student['grade']}")

# ==========================================
# MODIFYING VALUES IN A DICTIONARY
# ==========================================
# student["age"] = 21
# print(f"Modified student: {student}")
# print("Modified student", *student.values(), sep=" - ")

# ==========================================
# ADDING NEW KEY-VALUE PAIRS TO A DICTIONARY
# ==========================================
# student["major"] = "Computer Science"
# print(f"Student with major: {student}")
# print("Student with major:", *student.values(), sep=" - ")

# ==========================================
# REMOVING KEY-VALUE PAIRS FROM A DICTIONARY
# ==========================================
# del student["grade"]
# removed_value = student.pop('grade', None)  # Using pop to remove 'grade' and get its value, returns None if 'grade' doesn't exist
# print(f"Student without grade: {student}")
# print("Student without grade:", *student.values(), sep=" - ")

# ==========================================
# CHECKING IF A KEY EXISTS IN A DICTIONARY
# ==========================================
# print(f"Is 'name' a key in the dictionary? {'name' in student}")
# print(f"Is 'grade' a key in the dictionary? {'grade' in student}")

# ==========================================
# GETTING ALL KEYS-VALUES FROM A DICTIONARY
# ==========================================
# print(f"All keys: {list(student.keys())}")
# print(f"All values: {list(student.values())}")

# ==========================================
# CHECKING IF A KEY EXISTS IN A DICTIONARY IN IF STATEMENT
# ==========================================
# if 'age' in student:
# print("'age' is present in the dictionary.")
# else:
# print("'age' is not present in the dictionary.")

# ==========================================
# ITERATING OVER A DICTIONARY
# ==========================================
# print("Iterating over the dictionary:")
# for key, value in student.items():
#     print(f"{key}: {value}")


# ==========================================
# MODULE 18: ENUMERATE FUNCTION
# ==========================================
student = {
    "name": "Alice", 
    "age": 20, 
    "grade": "A"
    }

print("Iterating with a loop counter:")
for index, (key, value) in enumerate(student.items()):
    print(f"Item #{index + 1} -> {key}: {value}")
