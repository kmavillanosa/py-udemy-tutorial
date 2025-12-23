# THIS IS NOT AI GENERATED CODE, I WROTE THIS MYSELF.

# to run the code, type: python ./section-one/2variables-and-constants.py , or install python debugger


# variables - in general are mutable objects that can be shaped into different values


kount = 100 # count
emp_name = "Robin" # employee name
age1, age2, age3 = 44, 27, 32 #ages of three employees
print(f"____________________basic variables______________________________")
print(f"The count is {kount}")
print(f"The employee name is {emp_name}")
print(f"The ages of the employees are {age1}, {age2}, and {age3}")


#constants - in general are immutable objects that cannot be shaped into different values
# it is implied that we use naming convetions to identify constants, namely camelCase or UPPERCASE
PI = 3.14
GRAVITY = 9.8

print(f"____________________constants______________________________")
print(f"The value of PI is {PI}")
print(f"The value of GRAVITY is {GRAVITY}")


print(f"_____________________variable declarations and assignment_______________________________")

# variable changing, reassigning values to variables
a = "Apple"
print(f"The value of a is {a}")

a = "Aeroplane"
print(f"The value of a is changed to Aeroplane from Apple, so the current value of a is {a}")

a = 100
print(f"The value of a is changed to 100 from Aeroplane, so the current value of a is {a}")

print(f"_____________________multiple variable declarations and assignment_______________________________")

# multiple variable declarations, assigning multiple values to multiple variables
b , c, d = 1, 2.5, "Hello"
print(f"The value of b is {b}, the value of c is {c}, and the value of d is {d}")

# assigning the same value to multiple variables
b = c = d = 5
print(f"The value of b is {b}, the value of c is {c}, and the value of d is {d}")