# THIS IS NOT AI GENERATED CODE, I WROTE THIS MYSELF.

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

print("_____________________class declarations part 2________________________________")

numberClass2 = MyComplexNumber(60,70)
# introduces a new attribute
numberClass2.new_attribute = 80
numberClass2.displayComplex()
print((numberClass2.real_part, numberClass2.image_part, numberClass2.new_attribute))


print("_____________________Delete variables and class________________________________")

# delete object
del numberClass1.real_part

# delete properties
del numberClass1

# IMPORTANT ---------->>>>>> COMMENT OUT print() to see results
# this will fail this script, because number class 1 has been disposed and print is calling out a null pointer
# print(numberClass1)

