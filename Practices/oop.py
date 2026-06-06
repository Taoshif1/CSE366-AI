# ==========================================
# OOP IN PYTHON
# ==========================================

# 1. Class & Object
# 2. Inheritance
# 3. Polymorphism
# 4. Encapsulation
# 5. Abstraction
# 6. Method Overriding
# 7. Class & Instance Variables
# 8. Static Methods

# ==========================================
# MODULE 1: CLASS & OBJECT
# ==========================================


# class BankAccount:
#     def __init__(self, name, acc_num, balance):
#         self.name = name
#         self.acc_num = acc_num
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(
#             f"Deposited {amount} in {self.name}'s account. New balance: {self.balance}"
#         )

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print(
#                 f"Withdrew {amount} from {self.name}'s account. New balance: {self.balance}"
#             )
#         else:
#             print(f"Insufficient funds in {self.name}'s account.")


# account1 = BankAccount("Taoshif", "123456", 1000)
# account2 = BankAccount("Moon", "654321", 500)

# account1.deposit(200)
# account1.withdraw(1500)
# account2.withdraw(400)


# ====================================================


class Student:

    def __init__(self, name, id, dept, init_balance=0):
        self.name = name
        self.id = id
        self.dept = dept
        self.balance = init_balance
        self.enrolled_courses = []

    def enroll_course(self, course_name, credits):
        self.enrolled_courses.append(course_name)

        course_cost = credits * 300
        self.balance += course_cost
        print(
            f"{self.name} enrolled in {course_name}. Course cost: {course_cost} of {credits} credits. New balance: {self.balance} Tk."
        )

    def make_payment(self, amount):
        if amount <= 0:
            print("Invalid payment amount!")
            return

        self.balance += amount
        print(
            f"{self.name} made a payment of {amount} Tk. New balance: {self.balance} Tk."
        )

    def display_profile(self):
        print(f"\n--- Student Profile: {self.name} ---")
        print(f"ID: {self.id} | Dept: {self.dept}")
        print(
            f"Current Courses: {', '.join(self.enrolled_courses) if self.enrolled_courses else 'None'}"
        )
        print(f"Account Balance: {self.balance} tk")
        print("---------------------------------")


# student1 = Student("Taoshif", "123456", "CSE", 5000)
# student2 = Student("Moon", "654321", "CSE", 3000)

# student1.enroll_course("Data Structures", 4)
# student1.make_payment(1500)
# student1.display_profile()

# student2.enroll_course("Database Systems", 3)
# student2.display_profile()


# ====================================================
class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return b - a

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return "cannot divide by zero"


# calc = Calculator()

# print(f"Addition: {calc.add(3,7)}")
# print(f"Subtraction: {calc.sub(2,7)}")
# print(f"Multiplication: {calc.mul(2,7)}")
# print(f"Division: {int(calc.div(15,5))}")


# ==========================================
# MODULE 2: INHERITANCE
# ==========================================


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} | {self.make} | {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        return f"{super().display_info()}, {self.num_doors} doors"


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size

    def display_info(self):
        return f"{super().display_info()}, {self.engine_size}cc engine"


car = Car("Toyota", "Corolla", 2020, 4)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2023, 1200)

# print(car.display_info())
# print(motorcycle.display_info())


# ==========================================
# MODULE 3: POLYMORPHISM
# ==========================================


class Vehicle:
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        return "Car is driving"


class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is cycling"


class Airplane(Vehicle):
    def move(self):
        return "Airplane is flying"


vehicles = [Car(), Bicycle(), Airplane()]

# for vehicle in vehicles:
#     print(vehicle.move())


# ==========================================
# MODULE 4: ENCAPSULATION
# ==========================================

# _ is protected &  __ is private

# Ultimate Backdoor Cheat Code ( for private ):
# print(person1._Person__age)  # Output: 21


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Invalid age. Age must be non-negative.")


# person1 = Person("Moon", 20)

# print("Name:", person1.get_name())
# print("Age:", person1.get_age())

# person1.set_name("Taoshif")
# person1.set_age(21)

# print("Modified Name:", person1.get_name())
# print("Modified Age:", person1.get_age())


# ==========================================
# MODULE 5: ABSTRACTION
# ==========================================

# @abstractmethod symbol is a Decorator in Python. It acts like a strict contract or a rulebook for inheritance.

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


# rectangle = Rectangle(5, 4)
# print("Area of Rectangle:", rectangle.area())
# print("Perimeter of Rectangle:", rectangle.perimeter())

# circle = Circle(7)
# print("Area of Circle:", circle.area())
# print("Circumference of Circle:", circle.perimeter())


# ==========================================
# MODULE 6: METHOD OVER-RIDING
# ==========================================
class Animal:
    def make_sound(self):
        print("Some generic sound")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


class Cow(Animal):
    # This class does not override make_sound method
    pass


# animal = Animal()
# dog = Dog()
# cat = Cat()
# cow = Cow()

# animal.make_sound()
# dog.make_sound()
# cat.make_sound()
# cow.make_sound()


# ==========================================
#  METHOD OVERRIDING (REAL WORLD EXP)
# ==========================================


class Order:
    def __init__(self, amount):
        self.amount = amount

    def calc_total(self):
        return self.amount


class PremiumOrder(Order):
    def calc_total(self):
        discount = self.amount * 0.10
        return self.amount - discount


class EidFestivalOrder(Order):
    def calc_total(self):
        discount = self.amount * 0.25
        return self.amount - discount


base_price = 1000

# regular_customer = Order(base_price)
# vip_customer = PremiumOrder(base_price)
# festive_customer = EidFestivalOrder(base_price)

# print("Regular Customer Total:", egular_customer.calc_total(), "Tk.")
# print("Premium Customer Total:", vip_customer.calc_total(), "Tk.")
# print("Festival Customer Total:", festive_customer.calc_total(), "Tk.")


# ==========================================
# MODULE 7: CLASS & INSTANCE VARIABLES
# ==========================================
class Student:
    # Class variable
    school_name = "XYZ High School"

    def __init__(self, name, grade):
        # Instance variables
        self.name = name
        self.grade = grade
        self.attendance = 0

    def attend_school(self):
        self.attendance += 1
        print(f"{self.name} attended school today.")

    def display_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}")


# student1 = Student("Gazi", 10)
# student2 = Student("Moon", 11)

# student1.display_info()
# student2.display_info()

# Accessing class variable
# print(f"School Name for Student 1: {student1.school_name}")
# print(f"School Name for Student 2: {student2.school_name}")

# Modifying class variable
# Student.school_name = "ABC High School"
# print(f"School Name for Student 1 after modification: {student1.school_name}")
# print(f"School Name for Student 2 after modification: {student2.school_name}")

# Modifying instance variable
# student1.attend_school()
# student1.attend_school()
# student2.attend_school()
# print(f"Attendance for {student1.name}: {student1.attendance}")
# print(f"Attendance for {student2.name}: {student2.attendance}")

# ==========================================
#  CLASS & INSTANCE VARIABLES (EXP)
# ==========================================


class Employee:
    # CLASS VARIABLE: Shared across the whole company
    company_name = "TechCorp"
    total_employee_count = 0  # Global counter tracking total hires

    def __init__(self, name, salary):
        # INSTANCE VARIABLES: Unique to each person
        self.name = name
        self.salary = salary

        # Update the global tracker every time a new person is hired!
        Employee.total_employee_count += 1

    def display_details(self):
        print(
            f"Employee: {self.name} | Works at: {Employee.company_name} | Salary: {self.salary} Tk."
        )


# 1. Check total employees before hiring
# print(f"Initial Employee Count: {Employee.total_employee_count}")

# 2. Hire two unique employees
# emp1 = Employee("Gazi", 80000)
# emp2 = Employee("Taoshif", 95000)

# 3. Display their individual unique data
# emp1.display_details()
# emp2.display_details()

# 4. Check the shared class variable counter now
# print(f"Total Hired Employees: {Employee.total_employee_count}")

# 5. Company rebrands globally!
Employee.company_name = "GlobalTech"

# print("\n--- After Global Rebrand ---")
# emp1.display_details()
# emp2.display_details()


# ==========================================
# MODULE 8: STATIC METHOD
# ==========================================
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            return "Cannot divide by zero!"
        else:
            return x / y


# calc_instance = Calculator(10, 5)

# Call non-static methods on the instance
# print("Addition Result:", calc_instance.add())
# print("Subtraction Result:", calc_instance.subtract())

# Call static methods directly on the class
# print("Multiplication Result:", Calculator.multiply(4, 6))
# print("Division Result:", Calculator.divide(10, 2))

# ==========================================
# MODULE 8: STATIC METHODS (REAL WORLD EXP)
# ==========================================


class CurrencyConverter:
    def __init__(self, username):
        self.username = username

    # STATIC METHOD: Clean utility tool.
    # It just takes a number and does math. It doesn't care who the user is!
    @staticmethod
    def usd_to_bdt(usd_amount):
        exchange_rate = 118.50
        return usd_amount * exchange_rate


# Scenario A: You don't need to log in or create an account just to check a rate!
# We call the static method directly on the Class blueprint.
quick_check = CurrencyConverter.usd_to_bdt(100)
print(f"Direct Quick Conversion (100 USD): {quick_check} BDT")


# Scenario B: Standard instance creation when tracking user accounts
user1 = CurrencyConverter("Gazi")
print(f"Account created for: {user1.username}")

#  We CAN still call static methods from an instance variable if you want to:
print(f"User check (50 USD): {user1.usd_to_bdt(50)} BDT")
