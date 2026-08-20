# Python Practice

## Comparison Operators

a = int(input("Enter any Number: "))
b = int(input("Enter any Number: "))

print(a > b)
print(a < b)
print(a == b)
print(a != b)


## Assignment Operators

a = 10

a += 5
print(a)

a -= 5
print(a)

a *= 5
print(a)

a /= 5
print(a)

a %= 5
print(a)

a **= 5
print(a)

a //= 5
print(a)

## Logical Operators

Logical operators are used to combine or modify conditions and return a Boolean result (`True` or `False`).

The logical operators practiced are:

- `and`
- `or`
- `not`

# Practice Code

age = int(input("Enter Age: "))
print(age, type)

has_id = input("Do you have Valid ID? True/False: ")

if has_id == "True":
    has_id = True
else:
    has_id = False

print(age >= 18 and has_id)
print(type(age))

print(age < 18 or not has_id)
print(type(age))


## Membership Operators

Membership operators are used to check whether a value is present in a sequence or collection.

The membership operators practiced are:

- `in`
- `not in`

---

# Membership Operators

fruits = ["apple", "banana", "orange", "mango", "grape"]

A = input("Enter Fruit1: ")

print(A)
print(A in fruits)
print(A not in fruits)

## Conditional Statements

# if / elif / else

score = int(input("Enter your Score: "))

if score >= 90:
    print("Excellent")

elif score >= 70:
    print("Good")

elif score >= 50:
    print("Pass")

else:
    print("Fail")


## Nested if

a = input("Are you a student? True/False: ")
b = input("Do you have a student ID? True/False: ")

if a == "True":

    if b == "True":
    
        print("Student access granted")
        
    else:
    
        print("Please show your student ID")
        
else:

    print("Regular access")
