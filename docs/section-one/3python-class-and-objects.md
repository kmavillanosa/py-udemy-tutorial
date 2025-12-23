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

## Class Definition

A class is a blueprint for creating objects. It defines attributes and methods that the objects will have.

```python
class MyComplexNumber:
    def __init__(self, real = 0, image = 0):
        self.real_part = real
        self.image_part = image
    
    def displayComplex(self):
        print("{0} + {1}j".format(self.real_part, self.image_part))
```

## Constructor

The `__init__` method is the constructor that initializes a new instance of the class. The `self` parameter refers to the instance being created.

## Creating Objects

Objects are created by calling the class name with arguments:

```python
numberClass1 = MyComplexNumber(40, 50)
numberClass1.displayComplex()
```

## Modifying Attributes

You can modify object attributes after creation:

```python
numberClass1.image_part += 10
```

You can also add new attributes dynamically:

```python
numberClass2.new_attribute = 80
```

## Deleting Objects

Objects and their attributes can be deleted using the `del` statement:

```python
del numberClass1.real_part  # Delete an attribute
del numberClass1            # Delete the entire object
```

## Running the Code

```bash
python ./section-one/3python-class-and-objects.py
```

