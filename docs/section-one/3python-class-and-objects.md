# Classes and Objects

Introduction to object-oriented programming in Python.

## Concepts Covered

- Class definition
- Constructors and initialization
- Class attributes
- Methods
- Object instantiation
- Attribute modification
- Object deletion

## Try It Yourself

Click the "▶ Run Code" button below each code block to execute the code and see the output!

### Example 1: Class Definition and Object Creation

A class is a blueprint for creating objects. It defines attributes and methods that the objects will have.

```python
# this is a class, this constitutes to an entity
class MyComplexNumber:
    #constructor, this is used to initialize a class, this has two input parameters, self is just the primitive initializer
    def __init__(self, real = 0, image = 0):
        print("MyComplexNumber constructor is executing...")
        #these are class attribute, can be used after calling 
        self.real_part = real
        self.image_part = image
    
    #this is a method/delegate, this prints out the current value of the class
    def displayComplex(self):
        print("{0} + {1}j".format(self.real_part, self.image_part))

print("_____________________class declarations part 1________________________________")

numberClass1 = MyComplexNumber(40,50)
# you can assign values of a initialized class
numberClass1.image_part += 10
#invoke/call the method
numberClass1.displayComplex()
```

### Example 2: Adding New Attributes

You can add new attributes dynamically to objects:

```python
print("_____________________class declarations part 2________________________________")

numberClass2 = MyComplexNumber(60,70)
# introduces a new attribute
numberClass2.new_attribute = 80
numberClass2.displayComplex()
print((numberClass2.real_part, numberClass2.image_part, numberClass2.new_attribute))
```

### Example 3: Deleting Objects and Attributes

Objects and their attributes can be deleted using the `del` statement:

```python
print("_____________________Delete variables and class________________________________")

# delete object attribute
del numberClass1.real_part

# delete the entire object
del numberClass1

# Note: Trying to use numberClass1 after deletion will cause an error
# print(numberClass1)  # This would fail
```

## Running Locally

To run the complete file on your computer:

```bash
python ./section-one/3python-class-and-objects.py
```

