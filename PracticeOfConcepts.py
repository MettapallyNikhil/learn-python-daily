# import sys
# sys.set_int_max_str_digits(0)

# # Basics - input() int() float() str bool comparison == if-else variables type()
# name = input("Enter Name: ")
# print(type(name))

# Age = int(input("Enter your Age: "))
# print(type(Age))

# Height = float(input("Enter in Numbers(Cms): "))
# print(type(Height))

# Learning_Python = input("Are you learning Python?True/False: ")
# if Learning_Python == "True":
#     Learning_Python = True
# else:
#     Learning_Python = False
# print(Learning_Python)
# print(type(Learning_Python))

# # Arithmetic Operators - addition subtraction multiplication division remainder (%) power (**) floor division (//)
# a = int(input("Enter any Number: "))
# b = int(input("Enter any Number: "))
# print("Addition:", a+b)
# print("Subtraction:",a-b)
# print("Multiplication:",a*b)
# print("Division:",a/b)
# print("Remainder:",a%b)
# print("Power:",a**b)
# print("Floor Division:",a//b)

# # Comparison Operators
# a = int(input("Enter any Number: "))
# b = int(input("Enter any Number: "))

# print(a>b)
# print(a<b)
# print(a==b)
# print(a!=b)

# # Assignment Operators
# a = 10

# a += 5
# print(a)
# a -= 5
# print(a)
# a *= 5
# print(a)
# a /= 5
# print(a)
# a %= 5
# print(a)
# a **= 5
# print(a)
# a //= 5
# print(a)

# Logical Operators
# age = int(input("Enter Age: "))
# print(age, type)
# has_id = input("Do you have Valid ID? True/False: ")
# if has_id == "True":
#     has_id = True
# else:
#     has_id = False

# print(age >= 18 and has_id)
# print(type(age))
# print(age < 18 or not has_id)
# print(type(age))

# in and not in
# fruits = ["apple", "banana", "orange", "mango", "grape"]
# A = input("Enter Fruit1: ")
# print(A)
# print(A in fruits)
# print(A not in fruits)

# if / elif / else
score = int(input("Enter your Score: "))
if  score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 50:
    print("Pass")
else:
    print("Fail")

# Nested if
a = input("Are you a student? True/False: ")
b = input("Do you have a student ID? True/False: ")
if a == "True":
    if b == "True":
        print("Student access granted")
    else:
        print("Please show your student ID")
else:
    print("Regular access")
    