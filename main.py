# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         return f"Hello, my name is {self.name}. I am {self.age} years old."

# person = Person("Alice", 30)
# print(person.introduce())

# class rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)
# rect = rectangle(8, 5)
# print("Area:", rect.area())
# print("Perimeter:", rect.perimeter())

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def get_info(self):
#         return f"{self.year} {self.brand} {self.model}"
# car = Car("Skoda", "Fabia", 2018)
# print(car.get_info())

# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)
# student = Student("Oleg", [85, 90, 78, 92])
# print("Average Grade:", student.average_grade())

# class BankAccount:
#     def __init__(self, __balance=0, deposit_amount=0, withdraw_amount=0):
#         self.__balance = __balance
#         self.deposit_amount = deposit_amount
#         self.withdraw_amount = withdraw_amount
#     def deposit(self, amount):
#         self.__balance += amount
#         return self.__balance
#     def withdraw(self, amount):
#         if amount > self.__balance:
#             return "No enough funds"
#         self.__balance -= amount
#         return self.__balance
# account = BankAccount()
# print("Deposit:", account.deposit(500))
# print("Withdraw:", account.withdraw(200))

# class Book:
#     count = 0

#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         Book.count += 1
# book1 = Book("Title1", "Autor1")
# book2 = Book("Title2", "Autor2")
# print("Total books:", Book.count)

# class Animal:
#     def make_sound(self):
#         pass
# class Dog(Animal):
#     def make_sound(self):
#         return "Woof"
# class Cat(Animal):
#     def make_sound(self):
#         return "Meow"
# dog = Dog()
# cat = Cat()
# print(dog.make_sound())
# print(cat.make_sound())

# class Employee:
#     def __init__(self, name, base_salary):
#         self.name = name
#         self.base_salary = base_salary

#     def get_salary(self):
#         return self.base_salary

# class Manager(Employee):
#     def __init__(self, name, base_salary, bonus):
#         super().__init__(name, base_salary)
#         self.bonus = bonus

#     def get_salary(self):
#         return self.base_salary + self.bonus
# manager = Manager("Max", 5000, 1500)
# print("Manager Salary:", manager.get_salary())

# class Animal:
#     def make_sound(self):
#         pass
# class Dog(Animal):
#     def make_sound(self):
#         return "Woof"
# class Cat(Animal):
#     def make_sound(self):
#         return "Meow"
# class Cow(Animal):
#     def make_sound(self):
#         return "Moo"
# animals = [Dog(), Cat(), Cow()]
# for animal in animals:
#     print(animal.make_sound())

# from abc import ABC, abstractmethod
# import math
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius ** 2
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#     def area(self):
#         return self.side ** 2
# circle = Circle(3)
# square = Square(5)
# print("Circle:", circle.area())
# print("Square:", square.area())

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f"Vector({self.x}, {self.y})"
# vector1 = Vector(9, 5)
# vector2 = Vector(3, 6)
# result = vector1 + vector2
# print(result)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def display_books(self):
        for book in self.books:
            print(book)
library = Library()
book1 = Book("1984", "Author")
book2 = Book("Title", "Author2")
library.add_book(book1)
library.add_book(book2)
library.display_books()
found_book = library.find_book("1984")
if found_book:
    print("Found:", found_book)
else:
    print("Not found")