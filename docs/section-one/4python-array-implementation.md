# Array Implementation

Comprehensive guide to working with arrays (lists) in Python.

## Concepts Covered

- Array creation and indexing
- Positive and negative indexing
- Array operations (append, remove, pop)
- Modifying array elements
- Array concatenation
- Repeating elements
- Array slicing
- Multi-dimensional arrays

## Creating Arrays

Arrays in Python are called lists. They can contain any type of data:

```python
arr = [10, 20, 30, 40, 50]
brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
```

## Indexing

### Positive Indexing

Access elements from the beginning (0-based):

```python
arr[0]  # First element: 10
arr[1]  # Second element: 20
```

### Negative Indexing

Access elements from the end:

```python
arr[-1]  # Last element: 50
arr[-2]  # Second to last: 40
```

## Array Operations

### Adding Elements

```python
brands.append("Intel")  # Adds to the end
```

### Removing Elements

```python
del colors[4]              # Delete by index
colors.remove("blue")      # Delete by value
colors.pop(3)              # Delete by index and return value
```

### Modifying Elements

```python
fruits[1] = "Pineapple"   # Modify by index
fruits[-1] = "Guava"       # Modify using negative index
```

## Array Concatenation

```python
concat = [1, 2, 3]
concat = concat + [4, 5, 6]  # Result: [1, 2, 3, 4, 5, 6]
```

## Repeating Elements

```python
repeat = ["a"] * 5  # Result: ['a', 'a', 'a', 'a', 'a']
```

## Array Slicing

Extract portions of an array:

```python
fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
fruits[1:4]    # ['Banana', 'Mango', 'Grapes']
fruits[:3]     # ['Apple', 'Banana', 'Mango']
fruits[-4:]    # ['Banana', 'Mango', 'Grapes', 'Orange']
fruits[-3:-1]  # ['Mango', 'Grapes']
```

## Multi-dimensional Arrays

Arrays can contain other arrays:

```python
multd = [[1,2], [3,4], [5,6], [7,8]]
multd[0]      # [1, 2]
multd[2][1]   # 6 (accessing nested element)
```

## Running the Code

```bash
python ./section-one/4python-array-implementation.py
```

