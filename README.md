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
---

<img width="1182" height="626" alt="image" src="https://github.com/user-attachments/assets/e18ddcef-30d9-4c68-82d8-4585f819efb4" />


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
