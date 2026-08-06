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
