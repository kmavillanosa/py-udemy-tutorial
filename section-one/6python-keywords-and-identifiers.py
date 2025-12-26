# THIS IS NOT AI GENERATED CODE, I WROTE THIS MYSELF.

print("___________________python keywords and identifiers______________________________")

# import the keyword module to access Python keywords
import keyword

# get the list of all Python keywords
keywords = keyword.kwlist

# print out the python keywords
print(f"Total Python keywords: {len(keywords)}")
print(keywords)

print("\n" + "="*80)
print("IMPLEMENTATIONS OF ALL PYTHON KEYWORDS")
print("="*80)

# ============================================================================
# BOOLEAN LITERALS: False, None, True
# ============================================================================
print("\n___________________1. BOOLEAN LITERALS (False, None, True)______________________________")

# False - represents the boolean value false
is_active = False
print(f"is_active = {is_active} (type: {type(is_active).__name__})")

# None - represents the absence of a value (null in other languages)
result = None
print(f"result = {result} (type: {type(result).__name__})")

# True - represents the boolean value true
is_complete = True
print(f"is_complete = {is_complete} (type: {type(is_complete).__name__})")

# ============================================================================
# LOGICAL OPERATORS: and, or, not
# ============================================================================
print("\n___________________2. LOGICAL OPERATORS (and, or, not)______________________________")

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

# ============================================================================
# CONDITIONAL STATEMENTS: if, elif, else
# ============================================================================
print("\n___________________3. CONDITIONAL STATEMENTS (if, elif, else)______________________________")

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

# ============================================================================
# LOOPS: for, while
# ============================================================================
print("\n___________________4. LOOPS (for, while)______________________________")

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

# ============================================================================
# LOOP CONTROL: break, continue
# ============================================================================
print("\n___________________5. LOOP CONTROL (break, continue)______________________________")

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

# ============================================================================
# FUNCTIONS: def, return
# ============================================================================
print("\n___________________6. FUNCTIONS (def, return)______________________________")

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

# ============================================================================
# CLASSES: class
# ============================================================================
print("\n___________________7. CLASSES (class)______________________________")

# class - define a class
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def introduce(self):
		return f"I'm {self.name}, {self.age} years old"

person = Person("Alice", 30)
print(person.introduce())

# ============================================================================
# IMPORTS: import, from, as
# ============================================================================
print("\n___________________8. IMPORTS (import, from, as)______________________________")

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

# ============================================================================
# EXCEPTION HANDLING: try, except, finally, raise
# ============================================================================
print("\n___________________9. EXCEPTION HANDLING (try, except, finally, raise)______________________________")

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

# ============================================================================
# CONTEXT MANAGERS: with
# ============================================================================
print("\n___________________10. CONTEXT MANAGERS (with)______________________________")

# with - context manager (automatic resource management)
# Example with file handling
with open("temp_example.txt", "w") as file:
	file.write("This is a test file")
	print("File written successfully")

# File is automatically closed after the with block
import os
if os.path.exists("temp_example.txt"):
	os.remove("temp_example.txt")
	print("Temporary file cleaned up")

# ============================================================================
# ASSERTIONS: assert
# ============================================================================
print("\n___________________11. ASSERTIONS (assert)______________________________")

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

# ============================================================================
# DELETION: del
# ============================================================================
print("\n___________________12. DELETION (del)______________________________")

# del - delete variables, items, or attributes
my_list = [1, 2, 3, 4, 5]
print(f"Before deletion: {my_list}")

del my_list[2]  # delete item at index 2
print(f"After deleting index 2: {my_list}")

my_var = 100
print(f"my_var = {my_var}")
del my_var
# print(my_var)  # This would raise NameError

# ============================================================================
# SCOPE: global, nonlocal
# ============================================================================
print("\n___________________13. SCOPE (global, nonlocal)______________________________")

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

# ============================================================================
# MEMBERSHIP AND IDENTITY: in, is
# ============================================================================
print("\n___________________14. MEMBERSHIP AND IDENTITY (in, is)______________________________")

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

# ============================================================================
# LAMBDA FUNCTIONS: lambda
# ============================================================================
print("\n___________________15. LAMBDA FUNCTIONS (lambda)______________________________")

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

# ============================================================================
# PLACEHOLDER: pass
# ============================================================================
print("\n___________________16. PLACEHOLDER (pass)______________________________")

# pass - do nothing (placeholder for empty code blocks)
def future_function():
	pass  # function body to be implemented later

class FutureClass:
	pass  # class body to be implemented later

if True:
	pass  # empty if block

print("pass statement used as placeholder")

# ============================================================================
# GENERATORS: yield
# ============================================================================
print("\n___________________17. GENERATORS (yield)______________________________")

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

# ============================================================================
# ASYNCHRONOUS PROGRAMMING: async, await
# ============================================================================
print("\n___________________18. ASYNCHRONOUS PROGRAMMING (async, await)______________________________")

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

# Note: In a script, we use asyncio.run() to execute async functions
# Uncomment the line below to run async code (requires asyncio)
# asyncio.run(main())
print("async/await example defined (commented out - requires asyncio.run() to execute)")

print("\n" + "="*80)
print("ALL KEYWORD IMPLEMENTATIONS COMPLETE")
print("="*80)
