# Python Variables

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


# Python Type Conversion

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


# Python Input and Output

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

date_of_birth = 2024 - age

# print(f"Hello, {name}! You were born in {date_of_birth}.")


# Arithmetic Operators in Python

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


# Comparison Operators

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


# Python if…else Statement

# number = int(input("Enter a number: "))

# if number > 0:
#     print("The number is positive.")
# else:
#     print("The number is not positive.")


# Python if…elif…else Statement

# if number == 0:
#     print("The number is zero.")
# elif number > 0:
#     print("The number is positive.")
# else:
#     print("The number is negative.")


# Python Nested if Statements

# age = int(input("Enter your age: "))

if age >= 19:
    if age == 21:
        print("You are 21 years old, the age of majority in many countries!")
    elif age > 60:
        print("You are a senior citizen.")
    elif age > 30:
        print("You are a middle-aged adult.")
    else:
        print("You are an teenager.")
    
else:
    if age == 18:
        print("Now you can vote for the first time!")
    else:
        print("You are an kid.")
