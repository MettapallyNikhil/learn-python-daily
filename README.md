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

---

### 1. Complex Data Type

Python supports complex numbers as a built-in data type.

A complex number consists of:

- A real part
- An imaginary part

The general form is:

```text
a + bj

### 1. Sequence Data Types

Sequence data types are used to store multiple values in an ordered collection.

Python provides several sequence data types, including:

- String (`str`)
- List (`list`)
- Tuple (`tuple`)
- Range (`range`)

### 2. String

A string is a sequence of characters.

```python
name = "Python"

print(name)
print(name[0])
```

Output:

```text
Python
P
```

### 3. List

A list is an ordered collection of values. Lists are **mutable**, which means their values can be changed.

```python
numbers = [10, 20, 30, 40]

print(numbers)
print(numbers[0])
```

### 4. Tuple

A tuple is an ordered collection of values. Tuples are **immutable**, which means their values cannot be changed after creation.

```python
numbers = (10, 20, 30, 40)

print(numbers)
print(numbers[0])
```

### 5. Range

`range()` represents a sequence of numbers, commonly used with loops.

```python
numbers = range(1, 6)

print(list(numbers))
```

Output:

```text
[1, 2, 3, 4, 5]
```
