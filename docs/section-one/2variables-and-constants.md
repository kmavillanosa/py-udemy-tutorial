# Variables and Constants

This lesson covers variables and constants in Python, including declaration, assignment, and naming conventions.

## Concepts Covered

- Variable declaration and assignment
- Constants and naming conventions
- Variable reassignment
- Multiple variable declarations
- Assigning the same value to multiple variables

## Try It Yourself

Click the "▶ Run Code" button below each code block to execute the code and see the output!

### Example 1: Basic Variables

Variables are mutable objects that can be assigned different values. In Python, variables are created when you assign a value to them.

```python
kount = 100 # count
emp_name = "Robin" # employee name
age1, age2, age3 = 44, 27, 32 #ages of three employees
print(f"____________________basic variables______________________________")
print(f"The count is {kount}")
print(f"The employee name is {emp_name}")
print(f"The ages of the employees are {age1}, {age2}, and {age3}")
```

### Example 2: Constants

Constants are immutable objects that should not be changed. Python uses naming conventions to identify constants (typically UPPERCASE).

```python
PI = 3.14
GRAVITY = 9.8

print(f"____________________constants______________________________")
print(f"The value of PI is {PI}")
print(f"The value of GRAVITY is {GRAVITY}")
```

### Example 3: Variable Reassignment

Variables can be reassigned to different values, even different types:

```python
print(f"_____________________variable declarations and assignment_______________________________")

# variable changing, reassigning values to variables
a = "Apple"
print(f"The value of a is {a}")

a = "Aeroplane"
print(f"The value of a is changed to Aeroplane from Apple, so the current value of a is {a}")

a = 100
print(f"The value of a is changed to 100 from Aeroplane, so the current value of a is {a}")
```

### Example 4: Multiple Variable Assignment

Python supports multiple variable declarations in a single line:

```python
print(f"_____________________multiple variable declarations and assignment_______________________________")

# multiple variable declarations, assigning multiple values to multiple variables
b , c, d = 1, 2.5, "Hello"
print(f"The value of b is {b}, the value of c is {c}, and the value of d is {d}")

# assigning the same value to multiple variables
b = c = d = 5
print(f"The value of b is {b}, the value of c is {c}, and the value of d is {d}")
```

## Running Locally

To run the complete file on your computer:

```bash
python ./section-one/2variables-and-constants.py
```

