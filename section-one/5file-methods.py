# THIS IS NOT AI GENERATED CODE, I WROTE THIS MYSELF.

# to run the code, type: python ./section-one/5file-methods.py , or install python debugger

print("___________________file writing _____________________________")

# OUTPUT
# File created and written successfully!

# Writing to a file
# 'w' mode creates a new file or overwrites existing file
file = open("example.txt", "w")
file.write("Hello, World!\n")
file.write("This is a Python file operations example.\n")
file.write("Python makes file handling easy!")
file.close()
print("File created and written successfully!")

print("___________________file reading _____________________________")

# OUTPUT
# Hello, World!
# This is a Python file operations example.
# Python makes file handling easy!

# Reading from a file
# 'r' mode opens file for reading (default mode)
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

print("___________________file reading line by line _____________________________")

# OUTPUT
# Line 1: Hello, World!
# Line 2: This is a Python file operations example.
# Line 3: Python makes file handling easy!

# Reading file line by line
file = open("example.txt", "r")
lines = file.readlines()
for i, line in enumerate(lines, 1):
    print(f"Line {i}: {line.strip()}")
file.close()

print("___________________file appending _____________________________")

# OUTPUT
# File appended successfully!
# Hello, World!
# This is a Python file operations example.
# Python makes file handling easy!
# This line was appended!

# Appending to a file
# 'a' mode appends to the end of the file
file = open("example.txt", "a")
file.write("\nThis line was appended!")
file.close()
print("File appended successfully!")

# Read the file again to see appended content
file = open("example.txt", "r")
print(file.read())
file.close()

print("___________________using with statement (context manager) _____________________________")

# OUTPUT
# File written using 'with' statement!
# File read using 'with' statement!

# Using 'with' statement (recommended way)
# Automatically closes the file, even if an error occurs
with open("example2.txt", "w") as file:
    file.write("File written using 'with' statement!\n")
    file.write("No need to manually close the file.")
print("File written using 'with' statement!")

with open("example2.txt", "r") as file:
    content = file.read()
    print(content)
print("File read using 'with' statement!")

print("___________________file modes _____________________________")

# OUTPUT
# File modes:
# 'r' - Read mode (default)
# 'w' - Write mode (overwrites existing file)
# 'a' - Append mode (adds to end of file)
# 'x' - Exclusive creation (fails if file exists)
# 'b' - Binary mode (e.g., 'rb', 'wb')
# 't' - Text mode (default, e.g., 'rt', 'wt')
# '+' - Read and write mode (e.g., 'r+', 'w+')

print("File modes:")
print("'r' - Read mode (default)")
print("'w' - Write mode (overwrites existing file)")
print("'a' - Append mode (adds to end of file)")
print("'x' - Exclusive creation (fails if file exists)")
print("'b' - Binary mode (e.g., 'rb', 'wb')")
print("'t' - Text mode (default, e.g., 'rt', 'wt')")
print("'+' - Read and write mode (e.g., 'r+', 'w+')")

print("___________________checking if file exists _____________________________")

# OUTPUT
# File exists: True
# File is readable: True
# File is writable: True

import os

# Check if file exists
if os.path.exists("example.txt"):
    print("File exists: True")
    print(f"File is readable: {os.access('example.txt', os.R_OK)}")
    print(f"File is writable: {os.access('example.txt', os.W_OK)}")
else:
    print("File does not exist")

print("___________________reading file with error handling _____________________________")

# OUTPUT
# File read successfully!
# Content: Hello, World!
# This is a Python file operations example.
# Python makes file handling easy!
# This line was appended!

# Reading file with try-except for error handling
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print("File read successfully!")
        print(f"Content: {content}")
except FileNotFoundError:
    print("Error: File not found!")
except IOError:
    print("Error: Could not read file!")
except Exception as e:
    print(f"Error: {e}")

print("___________________writing multiple lines at once _____________________________")

# OUTPUT
# Multiple lines written successfully!

# Writing multiple lines using writelines()
lines_to_write = [
    "Line 1\n",
    "Line 2\n",
    "Line 3\n",
    "Line 4\n"
]

with open("example3.txt", "w") as file:
    file.writelines(lines_to_write)
print("Multiple lines written successfully!")

# Read it back
with open("example3.txt", "r") as file:
    print(file.read())

print("___________________file position and seeking _____________________________")

# OUTPUT
# Current position: 0
# First 10 characters: Hello, Wor
# Current position: 10
# Next 10 characters: ld!
# This is

# File position and seeking
with open("example.txt", "r") as file:
    print(f"Current position: {file.tell()}")
    
    # Read first 10 characters
    first_part = file.read(10)
    print(f"First 10 characters: {first_part}")
    print(f"Current position: {file.tell()}")
    
    # Read next 10 characters
    next_part = file.read(10)
    print(f"Next 10 characters: {next_part}")
    
    # Go back to beginning
    file.seek(0)
    print(f"Position after seek(0): {file.tell()}")

print("___________________cleaning up test files _____________________________")

# OUTPUT
# Test files cleaned up!

# Clean up test files
import os

test_files = ["example.txt", "example2.txt", "example3.txt"]
for filename in test_files:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Removed {filename}")

print("Test files cleaned up!")

