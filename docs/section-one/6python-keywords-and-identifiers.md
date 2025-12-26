# Python Keywords and Identifiers

Comprehensive guide to all Python keywords with practical examples and implementations.

## Concepts Covered

- Boolean literals (False, None, True)
- Logical operators (and, or, not)
- Conditional statements (if, elif, else)
- Loops (for, while)
- Loop control (break, continue)
- Functions (def, return)
- Classes (class)
- Imports (import, from, as)
- Exception handling (try, except, finally, raise)
- Context managers (with)
- Assertions (assert)
- Deletion (del)
- Scope (global, nonlocal)
- Membership and identity (in, is)
- Lambda functions (lambda)
- Placeholder (pass)
- Generators (yield)
- Asynchronous programming (async, await)

## Try It Yourself

Click the "▶ Run Code" button below each code block to execute the code and see the output!

### Getting All Python Keywords

Python provides a built-in `keyword` module to access all keywords programmatically:

```python
import keyword

# get the list of all Python keywords
keywords = keyword.kwlist

# print out the python keywords
print(f"Total Python keywords: {len(keywords)}")
print(keywords)
```

### Example 1: Boolean Literals (False, None, True)

Python has three boolean literals that represent truth values and absence of value:

```python
# False - represents the boolean value false
is_active = False
print(f"is_active = {is_active}")

# None - represents the absence of a value (null in other languages)
result = None
print(f"result = {result}")

# True - represents the boolean value true
is_complete = True
print(f"is_complete = {is_complete}")
```

### Example 2: Logical Operators (and, or, not)

Logical operators are used to combine or negate boolean expressions:

```python
# and - logical AND operator
x = 5
y = 10
if x > 0 and y > 0:
	print(f"Both {x} and {y} are positive")

# or - logical OR operator
age = 25
if age < 18 or age > 65:
	print("Special category")
else:
	print(f"Age {age} is in normal range")

# not - logical NOT operator
is_available = False
if not is_available:
	print("Item is not available")
```

### Example 3: Conditional Statements (if, elif, else)

Conditional statements allow your program to make decisions:

```python
# if - conditional statement
score = 85
if score >= 90:
	grade = "A"
elif score >= 80:  # elif - else if condition
	grade = "B"
elif score >= 70:
	grade = "C"
else:  # else - default case
	grade = "F"

print(f"Score: {score}, Grade: {grade}")
```

### Example 4: Loops (for, while)

Loops allow you to execute code repeatedly:

```python
# for - iterate over a sequence
print("for loop example:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:  # in - membership operator
	print(f"  - {fruit}")

# while - execute while condition is true
print("\nwhile loop example:")
count = 0
while count < 3:
	print(f"  Count: {count}")
	count += 1
```

### Example 5: Loop Control (break, continue)

Control the flow of loops with break and continue:

```python
# break - exit the loop
print("break example:")
for i in range(10):
	if i == 5:
		break  # exit loop when i equals 5
	print(f"  i = {i}")

# continue - skip to next iteration
print("\ncontinue example:")
for i in range(5):
	if i == 2:
		continue  # skip iteration when i equals 2
	print(f"  i = {i}")
```

### Example 6: Functions (def, return)

Functions allow you to organize and reuse code:

```python
# def - define a function
def add_numbers(a, b):
	"""Add two numbers and return the result"""
	return a + b  # return - return a value from function

result = add_numbers(5, 3)
print(f"add_numbers(5, 3) = {result}")

# function without return (returns None)
def greet(name):
	print(f"Hello, {name}!")

greet("Python")
```

### Example 7: Classes (class)

Classes are blueprints for creating objects:

```python
# class - define a class
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def introduce(self):
		return f"I'm {self.name}, {self.age} years old"

person = Person("Alice", 30)
print(person.introduce())
```

### Example 8: Imports (import, from, as)

Import modules and functions to use in your code:

```python
# import - import a module
import math
print(f"math.pi = {math.pi}")

# from - import specific items from a module
from datetime import date
today = date.today()
print(f"Today's date: {today}")

# as - create an alias for imported module
import os as operating_system
print(f"Current directory: {operating_system.getcwd()}")
```

### Example 9: Exception Handling (try, except, finally, raise)

Handle errors gracefully with exception handling:

```python
# try, except - handle exceptions
try:
	result = 10 / 2
	print(f"Division result: {result}")
except ZeroDivisionError:
	print("Cannot divide by zero!")
except Exception as e:
	print(f"An error occurred: {e}")

# finally - always execute code
try:
	file_content = "test"
	print("File operation successful")
except:
	print("File operation failed")
finally:  # always executes
	print("Cleanup: Closing resources")

# raise - raise an exception
def check_age(age):
	if age < 0:
		raise ValueError("Age cannot be negative")
	return f"Age is valid: {age}"

try:
	print(check_age(25))
	print(check_age(-5))
except ValueError as e:
	print(f"Error: {e}")
```

### Example 10: Context Managers (with)

Context managers ensure proper resource management:

```python
# with - context manager (automatic resource management)
# Example with file handling
with open("temp_example.txt", "w") as file:
	file.write("This is a test file")
	print("File written successfully")

# File is automatically closed after the with block
```

### Example 11: Assertions (assert)

Use assertions to test conditions during development:

```python
# assert - test if condition is true, raise AssertionError if false
def calculate_average(numbers):
	assert len(numbers) > 0, "List cannot be empty"
	return sum(numbers) / len(numbers)

try:
	avg = calculate_average([10, 20, 30])
	print(f"Average: {avg}")
	calculate_average([])  # This will raise AssertionError
except AssertionError as e:
	print(f"Assertion failed: {e}")
```

### Example 12: Deletion (del)

Delete variables, items, or attributes:

```python
# del - delete variables, items, or attributes
my_list = [1, 2, 3, 4, 5]
print(f"Before deletion: {my_list}")

del my_list[2]  # delete item at index 2
print(f"After deleting index 2: {my_list}")

my_var = 100
print(f"my_var = {my_var}")
del my_var
# print(my_var)  # This would raise NameError
```

### Example 13: Scope (global, nonlocal)

Control variable scope with global and nonlocal:

```python
# global - declare global variable
counter = 0

def increment_global():
	global counter  # use global variable
	counter += 1
	return counter

print(f"Counter before: {counter}")
increment_global()
print(f"Counter after: {counter}")

# nonlocal - use variable from enclosing scope
def outer_function():
	outer_var = "outer"
	
	def inner_function():
		nonlocal outer_var  # modify outer function's variable
		outer_var = "modified"
		return outer_var
	
	inner_function()
	return outer_var

print(f"nonlocal example: {outer_function()}")
```

### Example 14: Membership and Identity (in, is)

Check membership in collections and object identity:

```python
# in - check membership
numbers = [1, 2, 3, 4, 5]
if 3 in numbers:
	print("3 is in the list")

if "python" in "python programming":
	print("'python' found in string")

# is - check identity (same object in memory)
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a is b: {a is b}")  # False - different objects
print(f"a is c: {a is c}")  # True - same object
print(f"a == b: {a == b}")  # True - same values

# None comparison should use 'is'
value = None
if value is None:
	print("Value is None")
```

### Example 15: Lambda Functions (lambda)

Create anonymous functions with lambda:

```python
# lambda - create anonymous function
square = lambda x: x ** 2
print(f"square(5) = {square(5)}")

# lambda with multiple arguments
add = lambda a, b: a + b
print(f"add(3, 7) = {add(3, 7)}")

# lambda in higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared}")
```

### Example 16: Placeholder (pass)

Use pass as a placeholder for empty code blocks:

```python
# pass - do nothing (placeholder for empty code blocks)
def future_function():
	pass  # function body to be implemented later

class FutureClass:
	pass  # class body to be implemented later

if True:
	pass  # empty if block

print("pass statement used as placeholder")
```

### Example 17: Generators (yield)

Create generator functions with yield:

```python
# yield - create a generator function
def countdown(n):
	while n > 0:
		yield n  # yield value and pause execution
		n -= 1

print("Generator example:")
for num in countdown(5):
	print(f"  {num}")

# generator with multiple yields
def number_generator():
	yield 1
	yield 2
	yield 3

gen = number_generator()
print(f"First value: {next(gen)}")
print(f"Second value: {next(gen)}")
print(f"Third value: {next(gen)}")
```

### Example 18: Asynchronous Programming (async, await)

Create asynchronous functions for concurrent operations:

```python
# async - define an asynchronous function (coroutine)
import asyncio

async def fetch_data():
	"""Simulate fetching data asynchronously"""
	await asyncio.sleep(1)  # await - wait for async operation to complete
	return "Data fetched successfully"

async def main():
	# await - wait for async function to complete
	result = await fetch_data()
	print(f"Async result: {result}")
	
	# Multiple async operations
	async def task1():
		await asyncio.sleep(0.5)
		return "Task 1 complete"
	
	async def task2():
		await asyncio.sleep(0.5)
		return "Task 2 complete"
	
	# Run tasks concurrently
	results = await asyncio.gather(task1(), task2())
	print(f"Concurrent tasks: {results}")

# Execute async function
asyncio.run(main())
```

## Complete List of Python Keywords

Python has 35 keywords (as of Python 3.11+):

1. **False** - Boolean literal for false
2. **None** - Represents absence of value
3. **True** - Boolean literal for true
4. **and** - Logical AND operator
5. **as** - Alias in import statements
6. **assert** - Assertion statement
7. **break** - Exit loop statement
8. **class** - Define a class
9. **continue** - Skip to next iteration
10. **def** - Define a function
11. **del** - Delete statement
12. **elif** - Else if condition
13. **else** - Else clause
14. **except** - Exception handler
15. **finally** - Finally clause
16. **for** - For loop
17. **from** - Import from module
18. **global** - Global variable declaration
19. **if** - If condition
20. **import** - Import module
21. **in** - Membership operator
22. **is** - Identity operator
23. **lambda** - Anonymous function
24. **nonlocal** - Nonlocal variable declaration
25. **not** - Logical NOT operator
26. **or** - Logical OR operator
27. **pass** - Placeholder statement
28. **raise** - Raise exception
29. **return** - Return from function
30. **try** - Try block
31. **while** - While loop
32. **with** - Context manager
33. **yield** - Generator function
34. **async** - Asynchronous function definition
35. **await** - Wait for async operation

## Identifiers

Identifiers are names given to variables, functions, classes, modules, etc. Rules for identifiers:

- Must start with a letter (a-z, A-Z) or underscore (_)
- Can contain letters, digits (0-9), and underscores
- Cannot be a Python keyword
- Case-sensitive (myVar and myvar are different)
- Cannot contain spaces or special characters

### Valid Identifiers:
```python
my_variable = 10
_private_var = 20
MyClass = "valid"
var123 = 30
```

### Invalid Identifiers:
```python
# 123var = 10  # Cannot start with digit
# my-var = 20  # Cannot contain hyphen
# class = 30   # Cannot use keyword
# my var = 40  # Cannot contain spaces
```

## Running Locally

To run the complete file on your computer:

```bash
python ./section-one/6python-keywords-and-identifiers.py
```

