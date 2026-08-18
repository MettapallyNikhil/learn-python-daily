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
