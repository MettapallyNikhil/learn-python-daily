### 1. What is Python?
- Python is a high-level, interpreted programming language.
- It is easy to read and write.
- Python is widely used in:
  - Data Analysis
  - Artificial Intelligence
  - Machine Learning
  - Web Development
  - Automation
  - Scripting

### 2. Development Environment Setup
- Installed Visual Studio Code (VS Code).
- Installed Python Extension for VS Code.
- Configured the Codex AI Agent extension.
- Verified that the Python development environment is ready.

# Python Execution Modes

### Different Ways to Execute Python Programs

#### 1. Interactive Mode
- Executes one statement at a time.
- Useful for testing small pieces of code.
- Immediate output is displayed.

#### 2. Script Mode (.py)
- Write code in a `.py` file.
- Execute the complete program.
- Most commonly used for Python development.

#### 3. Python IDLE
- Python's built-in editor and interpreter.
- Suitable for beginners and small programs.

#### 4. PyCharm IDE
- A professional Python IDE.
- Provides features like debugging, auto-completion, and project management.

### 1. Comments in Python

Comments are used to explain the code and make it easier to understand. Python ignores comments during program execution.

#### Single-line Comment
```python
# This is a single-line comment
print("Hello, World!")
```

#### Multi-line Comment
```python
"""
This is a multi-line comment.
It can span multiple lines.
"""
print("Python")
```

### 2. Keywords in Python

Keywords are reserved words that have a predefined meaning in Python. They cannot be used as variable names, function names, or identifiers.
Some commonly used Python keywords are:
 if
- else
- elif
- for
- while
- break
- continue
- def
- return
- class
- try
- except
- import
- True
- False
- None

### 3. Variables

Variables are used to store data in memory. They allow us to save values and use them later in the program.

**Example:**

```python
name = "Nikhil"
age = 24
```

---

### 4. Multiple Variable Assignment

Python allows assigning values to multiple variables in a single line.

**Example:**

```python
x, y, z = 10, 20, 30

print(x)
print(y)
print(z)
```

The same value can also be assigned to multiple variables.

```python
a = b = c = 100

print(a)
print(b)
print(c)
```

---

### 5. Indentation

Python uses indentation (spaces) to define blocks of code instead of braces `{}`.

**Example:**

```python
if 10 > 5:
    print("10 is greater than 5")
```

Incorrect indentation results in an `IndentationError`.

---

### 6. Identifiers

Identifiers are the names given to variables, functions, classes, and other objects.

**Examples:**

```python
student_name = "John"
total_marks = 95
```

---

### Rules for Naming Identifiers

- Must start with a letter (A-Z or a-z) or an underscore (`_`).
- Cannot start with a number.
- Can contain letters, numbers, and underscores.
- Cannot contain spaces.
- Cannot use Python keywords.
- Python identifiers are case-sensitive (`age` and `Age` are different).

**Valid Identifiers**

```python
name
_age
student1
total_marks
```

**Invalid Identifiers**

```python
1name
student-name
total marks
for
```

---
### 1. Data Types in Python

A data type specifies the type of value a variable can store.

#### Integer (`int`)

Stores whole numbers without decimal points.

```python
age = 24
print(age)
print(type(age))
```

**Output:**

```
24
<class 'int'>
```

---

#### Float (`float`)

Stores decimal numbers.

```python
price = 99.99
print(price)
print(type(price))
```

**Output:**

```
99.99
<class 'float'>
```

---

#### Boolean (`bool`)

Stores one of two values: `True` or `False`.

```python
is_student = True
print(is_student)
print(type(is_student))
```

**Output:**

```
True
<class 'bool'>
```

---

### 2. Type Casting

Type casting is the process of converting one data type into another.

#### Integer to Float

```python
num = 10
result = float(num)

print(result)
print(type(result))
```

**Output:**

```
10.0
<class 'float'>
```

---

#### Float to Integer

```python
price = 15.8
result = int(price)

print(result)
print(type(result))
```

**Output:**

```
15
<class 'int'>
```

> **Note:** Converting a float to an integer removes the decimal part; it does not round the number.

---

#### Integer to Boolean

```python
print(bool(1))
print(bool(0))
```

**Output:**

```
True
False
```

---

#### Boolean to Integer

```python
print(int(True))
print(int(False))
```

**Output:**

```
1
0
```
<img width="1182" height="626" alt="image" src="https://github.com/user-attachments/assets/e18ddcef-30d9-4c68-82d8-4585f819efb4" />
---

### 1. Complex Data Type

Python supports complex numbers as a built-in data type.

A complex number consists of:

- A real part
- An imaginary part

The general form is:

```text

a + bj
---

# 1. Sequence Data Types

Sequence data types are used to store collections of elements in a particular order.

The main sequence data types covered are:

- String (`str`)
- List (`list`)
- Tuple (`tuple`)
- Range (`range`)

Common characteristics of sequence data types include:

- Elements have a defined position.
- Elements can generally be accessed using indexing.
- Many sequence types support slicing.
- Different sequence types have different rules regarding mutability and duplicates.

---

# 2. Strings (`str`)

A string is a sequence of characters enclosed within quotation marks.

### Creating Strings

Strings can be created using:

- Single quotes: `' '`
- Double quotes: `" "`
- Triple single quotes: `''' '''`
- Triple double quotes: `""" """`

Strings are represented by the `str` data type.

### String Characteristics

- Strings are ordered.
- Strings are immutable.
- Duplicate characters are allowed.
- Strings can contain letters, numbers, symbols, and spaces.
- Individual characters can be accessed using their index.
- Strings support indexing and slicing.

### String Immutability

A string cannot be modified after it has been created.

If a different value is assigned to the variable, a new string object is created rather than modifying the original string.

### Exploring String Methods

The available methods and attributes of the `str` class can be explored using:

```python
dir(str)
```

The documentation of the `str` class can be viewed using:

```python
help(str)
```

---

# 3. Lists (`list`)

A list is an ordered collection of elements enclosed in square brackets `[]`.

### List Characteristics

- Lists are ordered.
- Lists are mutable.
- Duplicate elements are allowed.
- Lists can contain elements of different data types.
- Elements can be accessed using indexes.
- Lists support indexing and slicing.
- Elements can be added, removed, or modified after the list is created.

### List Mutability

Lists are mutable, which means their contents can be changed after the list has been created.

This makes lists useful when the collection of data needs to change during program execution.

### Exploring List Methods

The available methods and attributes of the `list` class can be explored using:

```python
dir(list)
```

---

# 4. Tuples (`tuple`)

A tuple is an ordered collection of elements enclosed in parentheses `()`.

### Tuple Characteristics

- Tuples are ordered.
- Tuples are immutable.
- Duplicate elements are allowed.
- Tuples can contain elements of different data types.
- Elements can be accessed using indexes.
- Tuples support indexing and slicing.

### Tuple Immutability

Tuples cannot be modified after they have been created.

Individual elements of a tuple cannot be changed, added, or removed.

However, a variable containing a tuple can be reassigned to a completely new tuple.

### Single-Element Tuple

A tuple containing only one element requires a comma.

The comma is what makes it a tuple.

Without the comma, parentheses are treated as grouping parentheses rather than tuple creation.

### Tuple Without Parentheses

Parentheses are optional when creating tuples in many situations.

This is called tuple packing.

### Exploring Tuple Methods

The available methods and attributes of the `tuple` class can be explored using:

```python
dir(tuple)
```

---

# 5. Sets (`set`)

A set is a collection of unique elements enclosed in curly braces `{}`.

### Set Characteristics

- Sets do not maintain an index-based order.
- Sets are mutable.
- Duplicate elements are not allowed.
- Sets can contain elements of different data types, provided those elements are hashable.
- Sets do not support indexing.
- Sets are useful when we need to store unique values.

### Duplicate Elements

If duplicate values are provided while creating a set, only one occurrence of each value is retained.

Therefore, sets are commonly used when duplicate values need to be removed from a collection.

### Empty Set

An empty set cannot be created using `{}` because `{}` creates an empty dictionary.

An empty set is created using:

```python
set()
```

### Set Mutability

Sets are mutable, meaning elements can be added or removed after the set has been created.

However, the individual elements stored inside a set must be hashable.

### Exploring Set Methods

The available methods and attributes of the `set` class can be explored using:

```python
dir(set)
```

---

# 6. Dictionaries (`dict`)

A dictionary is a collection of **key-value pairs** enclosed in curly braces `{}`.

Each item in a dictionary consists of:

- A key
- A corresponding value

Dictionaries are commonly used for mapping one piece of information to another.

### Dictionary Characteristics

- Dictionaries store data as key-value pairs.
- Dictionary keys must be unique.
- Dictionary values can be duplicated.
- Keys must be hashable.
- Values can be of different data types.
- Dictionaries are mutable.
- Modern Python dictionaries preserve insertion order.
- Dictionaries do not use numerical indexes to access values; values are accessed using their keys.

### Dictionary Keys

Keys must be unique within a dictionary.

Keys must also be hashable, which means commonly used immutable data types such as strings, integers, and tuples can be used as keys.

### Dictionary Values

Values do not need to be unique.

Multiple keys can have the same value.

Values can be mutable or immutable depending on the object stored.

### Key-Value Mapping

Dictionaries are particularly useful for mapping one piece of information to another.

For example:

```text
Key → Value
```

A person's name can be mapped to their age, a product ID can be mapped to its price, or a country can be mapped to its capital.

### Exploring Dictionary Methods

The available methods and attributes of the `dict` class can be explored using:

```python
dir(dict)
```

---

# 7. Range (`range`)

`range` is an immutable sequence type used to represent a sequence of numbers.

It is commonly used with loops and iteration.

### Range Characteristics

- Range objects are ordered.
- Range objects are immutable.
- Range objects represent a sequence of numbers.
- The stop value is excluded.
- The start value is optional.
- The step value is optional.
- The default start value is `0`.
- The default step value is `1`.

### Range Structure

The general structure is:

```python
range(start, stop, step)
```

Where:

- `start` defines where the sequence begins.
- `stop` defines where the sequence ends, but is not included.
- `step` defines the difference between consecutive values.

### Using Range

`range()` is commonly used in `for` loops to generate a sequence of numbers for iteration.

### Exploring Range Methods

The available methods and attributes of the `range` class can be explored using:

```python
dir(range)
```

---

Operators in Python.

An operator is a symbol or keyword that performs an operation on one or more operands (values or variables).

Example concept:

```text
Operand  Operator  Operand
   10        +        20
```

Here:

- `10` and `20` are operands.
- `+` is the operator.

---

# 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical operations on numeric values.

| Operator | Name | Description |
|----------|------|-------------|
| `+` | Addition | Adds two values |
| `-` | Subtraction | Subtracts one value from another |
| `*` | Multiplication | Multiplies two values |
| `/` | Division | Divides one value by another and returns a float |
| `%` | Modulus | Returns the remainder after division |
| `**` | Exponentiation | Raises one value to the power of another |
| `//` | Floor Division | Performs division and returns the floor value |

### Arithmetic Operators

```text
+    Addition
-    Subtraction
*    Multiplication
/    Division
%    Modulus
**   Exponentiation
//   Floor Division
```

---

# 2. Relational (Comparison) Operators

Relational operators, also called comparison operators, are used to compare two values.

The result of a comparison is a Boolean value:

```text
True
```

or

```text
False
```

| Operator | Name |
|----------|------|
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |
| `==` | Equal to |
| `!=` | Not equal to |

### Important Note

`=` and `==` have different purposes.

- `=` is an **assignment operator**.
- `==` is a **comparison operator** used to check whether two values are equal.

---

# 3. Assignment Operators

Assignment operators are used to assign values to variables.

| Operator | Name | Meaning |
|----------|------|---------|
| `=` | Assignment | Assign a value |
| `+=` | Add and assign | Add a value and assign the result |
| `-=` | Subtract and assign | Subtract a value and assign the result |
| `*=` | Multiply and assign | Multiply by a value and assign the result |
| `/=` | Divide and assign | Divide by a value and assign the result |
| `%=` | Modulus and assign | Calculate the remainder and assign the result |
| `**=` | Power and assign | Raise to a power and assign the result |
| `//=` | Floor division and assign | Perform floor division and assign the result |

### Assignment Operators

```text
=      Assign
+=     Add and assign
-=     Subtract and assign
*=     Multiply and assign
/=     Divide and assign
%=     Modulus and assign
**=    Power and assign
//=    Floor division and assign
```

---

---

# 4. Logical Operators

Logical operators are used to combine or modify conditions.

They return Boolean results (`True` or `False`).

| Operator | Description |
|----------|-------------|
| `and` | Returns `True` if both conditions are `True` |
| `or` | Returns `True` if at least one condition is `True` |
| `not` | Reverses the Boolean result |

### `and`

Returns `True` only when both conditions are `True`.

### `or`

Returns `True` when at least one of the conditions is `True`.

### `not`

Reverses the result of a condition.

---

# 5. Membership Operators

Membership operators are used to check whether a value exists in a collection or sequence.

They can commonly be used with:

- Strings
- Lists
- Tuples
- Sets
- Dictionaries

| Operator | Description |
|----------|-------------|
| `in` | Returns `True` if the specified value is present |
| `not in` | Returns `True` if the specified value is not present |

### `in`

Checks whether a value exists in a collection.

### `not in`

Checks whether a value does not exist in a collection.

---

# 6. Identity Operators

Identity operators are used to determine whether two variables refer to the **same object**.

| Operator | Description |
|----------|-------------|
| `is` | Returns `True` if both variables refer to the same object |
| `is not` | Returns `True` if both variables do not refer to the same object |

### Important Difference: `is` vs `==`

These operators should not be confused.

- `==` checks whether two objects have equal values.
- `is` checks whether two variables refer to the same object.

```text
==  → Equality
is  → Identity
```

---

# 7. `id()` Function

`id()` is a built-in Python function used to obtain the unique identity of an object.

It returns an integer that identifies the object during its lifetime.

The identity can be used to investigate whether two variables refer to the same object.

### Important Note

The exact meaning of the returned integer depends on the Python implementation.

In CPython, the value returned by `id()` commonly corresponds to the object's memory address.

---

# 8. Bitwise Operators

Bitwise operators perform operations at the individual **bit level** of integer values.

They operate on the binary representation of numbers.

| Operator | Name | Description |
|----------|------|-------------|
| `&` | Bitwise AND | Performs AND operation on corresponding bits |
| `\|` | Bitwise OR | Performs OR operation on corresponding bits |
| `^` | Bitwise XOR | Performs exclusive OR operation on corresponding bits |
| `~` | Bitwise NOT | Inverts the bits of an integer |
| `<<` | Left Shift | Shifts bits to the left |
| `>>` | Right Shift | Shifts bits to the right |

### `&` — Bitwise AND

A bit becomes `1` only when both corresponding bits are `1`.

### `|` — Bitwise OR

A bit becomes `1` when at least one corresponding bit is `1`.

### `^` — Bitwise XOR

A bit becomes `1` when the corresponding bits are different.

### `~` — Bitwise NOT

Inverts the bits of an integer.

### `<<` — Left Shift

Shifts the bits to the left by the specified number of positions.

### `>>` — Right Shift

Shifts the bits to the right by the specified number of positions.

---

# 📊 Complete Python Operators Overview

| Category | Operators |
|----------|-----------|
| Arithmetic | `+`, `-`, `*`, `/`, `%`, `**`, `//` |
| Comparison / Relational | `<`, `>`, `<=`, `>=`, `==`, `!=` |
| Assignment | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=` |
| Logical | `and`, `or`, `not` |
| Membership | `in`, `not in` |
| Identity | `is`, `is not` |
| Bitwise | `&`, `|`, `^`, `~`, `<<`, `>>` |

---

# 📌 Operator Categories

```text
Arithmetic
    ↓
Comparison / Relational
    ↓
Assignment
    ↓
Logical
    ↓
Membership
    ↓
Identity
    ↓
Bitwise
```

---

<img width="680" height="386" alt="image" src="https://github.com/user-attachments/assets/b9710c57-d67e-4567-807b-56c5acabd15f" />

📚 Conditional Statements

Conditional statements are used to make decisions in a Python program based on whether a condition is True or False.
Python provides the following conditional structures:
•	if
•	if-else
•	elif
•	Nested if


1. if Statement
The if statement executes a block of code only when the given condition is True.
Syntax
if condition:
    statement


2. if-else Statement
The if-else statement provides two possible execution paths. If the condition is True, the if block is executed; otherwise, the else block is executed.
Syntax
if condition:
    statement
else:
    statement


3. elif Statement
The elif statement is the short form of else if. It is used to check additional conditions when the previous if or elif condition is False.
Syntax
if condition1:
    statement
elif condition2:
    statement
else:
    statement

4. Nested if Statement
A nested if statement means placing an if statement inside another if or else block. It is used to test another condition depending on the result of the first condition.
Syntax
if condition1:
    if condition2:
        statement
    else:
        statement
else:
    statement


Conditional Statement	Purpose
if	Executes a block when a condition is True.
if-else	Chooses between two possible outcomes.
elif	Checks additional conditions.
Nested if	Checks a condition inside another conditional block.

