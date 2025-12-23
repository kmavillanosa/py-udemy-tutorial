# File Methods

![Step 5 Preview](../img/step5.gif)

Comprehensive guide to working with files in Python, including reading, writing, and file operations.

## Concepts Covered

- Opening and closing files
- Reading from files
- Writing to files
- Appending to files
- File modes (r, w, a, x, b, t, +)
- Using context managers (with statement)
- Error handling with files
- File position and seeking
- Checking file existence

## Try It Yourself

Click the "▶ Run Code" button below each code block to execute the code and see the output!

### Example 1: Writing to a File

Writing data to a file using write mode ('w').

```python
# Writing to a file
# 'w' mode creates a new file or overwrites existing file
file = open("example.txt", "w")
file.write("Hello, World!\n")
file.write("This is a Python file operations example.\n")
file.write("Python makes file handling easy!")
file.close()
print("File created and written successfully!")
```

### Example 2: Reading from a File

Reading the entire contents of a file.

```python
# Reading from a file
# 'r' mode opens file for reading (default mode)
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

### Example 3: Reading Line by Line

Reading a file line by line using readlines().

```python
# Reading file line by line
file = open("example.txt", "r")
lines = file.readlines()
for i, line in enumerate(lines, 1):
    print(f"Line {i}: {line.strip()}")
file.close()
```

### Example 4: Appending to a File

Adding content to the end of an existing file.

```python
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
```

### Example 5: Using Context Manager (Recommended)

Using the `with` statement for automatic file closing.

```python
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
```

### Example 6: File Modes

Understanding different file modes in Python.

```python
print("File modes:")
print("'r' - Read mode (default)")
print("'w' - Write mode (overwrites existing file)")
print("'a' - Append mode (adds to end of file)")
print("'x' - Exclusive creation (fails if file exists)")
print("'b' - Binary mode (e.g., 'rb', 'wb')")
print("'t' - Text mode (default, e.g., 'rt', 'wt')")
print("'+' - Read and write mode (e.g., 'r+', 'w+')")
```

### Example 7: Checking File Existence

Checking if a file exists and its permissions.

```python
import os

# Check if file exists
if os.path.exists("example.txt"):
    print("File exists: True")
    print(f"File is readable: {os.access('example.txt', os.R_OK)}")
    print(f"File is writable: {os.access('example.txt', os.W_OK)}")
else:
    print("File does not exist")
```

### Example 8: Error Handling

Reading files with proper error handling.

```python
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
```

### Example 9: Writing Multiple Lines

Writing multiple lines at once using writelines().

```python
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
```

### Example 10: File Position and Seeking

Understanding file position and using seek() to navigate.

```python
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
```

## Running Locally

To run the complete file on your computer:

```bash
python ./section-one/5file-methods.py
```

## Best Practices

1. **Always use `with` statement**: It automatically closes files, even if errors occur
2. **Handle exceptions**: Use try-except blocks when working with files
3. **Check file existence**: Verify files exist before reading them
4. **Close files properly**: If not using `with`, always call `file.close()`
5. **Use appropriate modes**: Choose the right mode (r, w, a) for your operation

