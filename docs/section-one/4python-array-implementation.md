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

## Try It Yourself

Click the "▶ Run Code" button below each code block to execute the code and see the output!

### Example 1: Creating Arrays and Indexing

Arrays in Python are called lists. They can contain any type of data.

```python
print("___________________arrays (integer) _____________________________")

# define array of integers
arr = [10, 20, 30, 40, 50]
print(arr)

# select values by index (from first to last)
print(arr[0])
print(arr[1])
print(arr[2])

# negative indexing (inverse indexing, from last to first)
print(arr[-1])
print(arr[-2])
```

### Example 2: Array Operations - Append and Length

```python
print("___________________arrays (brands) _____________________________")

brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
print(brands)

# print out the length of array
print("the total count of this brand array is {0}".format(len(brands)))

# append (add new item) and print
brands.append("Intel")
print(brands)
```

### Example 3: Removing Elements from Arrays

```python
print("___________________arrays (colors) _____________________________")

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

# delete by index
del colors[4] #removes yellow

# delete by value
colors.remove("blue")

# delete by index
colors.pop(3) # removes orange

print(colors)
```

### Example 4: Modifying Array Elements

```python
print("___________________arrays (fruits) _____________________________")

fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(fruits)

fruits[1] = "Pineapple" #override banana to pineapple
print(fruits)

fruits[-1] = "Guava" #override orange to guava
print(fruits)
```

### Example 5: Array Concatenation

```python
print("___________________concat arrays _____________________________")

concat = [1, 2, 3]
print(concat)

concat + [4, 5, 6]
print(concat)

# increment
concat = concat + [4, 5, 6]
print(concat)
```

### Example 6: Repeating Elements

```python
print("___________________array repeating elements_____________________________")

repeat = ["a"]

#repeat the same value 5 times
repeat = repeat * 5

print(repeat)
```

### Example 7: Array Slicing

Extract portions of an array:

```python
print("___________________ array slicing _____________________________")

fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(fruits[1:4])
print(fruits[:3])
print(fruits[-4:])
print(fruits[-3:-1])
```

### Example 8: Multi-dimensional Arrays

Arrays can contain other arrays:

```python
print("___________________ Multi-dimensional array _____________________________")

multd = [[1,2], [3,4], [5,6], [7,8]]
print(multd)
print(multd[0])
print(multd[3])
print(multd[2][1])
print(multd[3][0])
```

## Running Locally

To run the complete file on your computer:

```bash
python ./section-one/4python-array-implementation.py
```

