# Python Practice

## Comparison Operators

```Python
a = int(input("Enter any Number: "))
b = int(input("Enter any Number: "))

print(a > b)
print(a < b)
print(a == b)
print(a != b)
````

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

# for loop

for i in range(1, 11):

    print(i)


# for loop + condition

for i in range(1, 11):

# for loop + condition

for i in range(1, 11):

    if i % 2 != 0:
    
        print(i)


# for loop + list

fruits = ["apple", "banana", "orange", "mango", "grape"]

for fruit in fruits:

    print(fruit)
    
    if i % 2 == 0:
        
        print(i)
        
# for loop + list + if
 fruits = ["apple", "banana", "orange", "mango", "grape"]
 for fruit in fruits:
     if fruit == "apple" or fruit == "mango":
        print(fruit)

# fruit = ("orange")
 if fruit == "apple":
     print(fruit)
 if fruit == "orange":
     print(fruit)
 if fruit == "apple" or fruit == "orange":
     print(fruit)   

# if
```python
# age = 20
 if age < 18:
     print(age)
 if age > 30:
     print(age)
 if age > 18 and age < 30:
     print(age)
```
```python
# if
 age = 25
 if age >= 18:
     print("Adult")
```
# number is positive, negative, or zero.
```python
 number = int(input("Enter a number: "))
 if number > 0:
     print("Positive")
 elif number < 0:
     print("Negative")
 else:
     print("Zero")
```

## Number Checker

The program takes a number as input and checks whether the number is:

- Positive
- Negative
- Zero

If the number is positive, it performs an additional check to determine whether the number is:

- Even
- Odd

```python
number = int(input("Enter a Number: "))

if number > 0:
    print("Positive")

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

elif number < 0:
    print("Negative")

else:
    print("Zero")
```

# Simple age checker

```python
number = int(input("Enter Your Age: "))

if number < 13:
    print("Child")
elif number >= 13 and number <= 17:
    print("Teenager")
elif number >= 18 and number <= 59:
    print("Adult")
else:
    print("Senior")
````

# Even/Odd + Positive/Negative

```python
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

elif number < 0:
    print("Negative")
else:
    print("Zero")
````

# Small Exercise

```python
age = int(input("Enter age: "))

if age >= 18 and age <= 30:
    print("Young Adult")
else:
    print("Other")
````

# Ask the user for two numbers

```python
a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))

if a > 0 and b > 0:
    print("Both positive")
else:
    print("At least one is negative")
````

# Ask for two numbers and print:
"Both are even" if both numbers are even

"At least one is odd" otherwise
```python
a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))

if a % 2 == 0 and b % 2 == 0:
    print("Both are even")
else:
    print("At least one is odd")
````

# Ask the user for two numbers.
"At least one is positive" if either number is positive

"Neither is positive" otherwise
```python
a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))

if a > 0 or b > 0:
    print("At least one is positive")
else:
    print("Neither is positive")
````
# Combination of (and + or)

# Print "Valid" if:
# both numbers are positive AND
# at least one of them is even.
# Otherwise print "Invalid".

a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))

if (a > 0 and b > 0) and (a % 2 == 0 or b % 2 == 0):
    print("both numbers are positive AND at least one of them is even")
else:
    print("Invalid")
