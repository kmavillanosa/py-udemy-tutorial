# THIS IS NOT AI GENERATED CODE, I WROTE THIS MYSELF.

print("___________________arrays (integer) _____________________________")

# OUTPUT
# [10, 20, 30, 40, 50]
# 10
# 20
# 30
# 50
# 40

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


print("___________________arrays (brands) _____________________________")

# OUTPUT
# ['Coke', 'Apple', 'Google', 'Microsoft', 'Toyota', 'Intel']

brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
print(brands)

# print out the length of array
print("the total count of this brand array is {0}".format(len(brands)))

# append (add new item) and print
brands.append("Intel")
print(brands)



print("___________________arrays (colors) _____________________________")

# OUTPUT
# ['violet', 'indigo', 'green', 'red']

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

# delete by index
del colors[4] #removes yellow

# delete by value
colors.remove("blue")

# delete by index
colors.pop(3) # removes orange


print(colors)

print("___________________arrays (fruits) _____________________________")

# OUTPUT
# ['Apple', 'Banana', 'Mango', 'Grapes', 'Orange']
# ['Apple', 'Pineapple', 'Mango', 'Grapes', 'Orange']
# ['Apple', 'Pineapple', 'Mango', 'Grapes', 'Guava']

fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(fruits)

fruits[1] = "Pineapple" #override banana to pineapple
print(fruits)

fruits[-1] = "Guava" #override orange to guava
print(fruits)


print("___________________concat arrays _____________________________")

# OUTPUT
# [1, 2, 3]
# [1, 2, 3]
# [1, 2, 3, 4, 5, 6]

concat = [1, 2, 3]
print(concat)

concat + [4, 5, 6]
print(concat)

# increment
concat = concat + [4, 5, 6]
print(concat)



print("___________________array repeating elements_____________________________")

# OUTPUT
# ['a', 'a', 'a', 'a', 'a']

repeat = ["a"]

#repeat the same value 5 times
repeat = repeat * 5

print(repeat)


print("___________________ array slicing _____________________________")

# OUTPUT
# ['Banana', 'Mango', 'Grapes']
# ['Apple', 'Banana', 'Mango']
# ['Banana', 'Mango', 'Grapes', 'Orange']
# ['Mango', 'Grapes']

fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(fruits[1:4])
print(fruits[:3])
print(fruits[-4:])
print(fruits[-3:-1])

print("___________________ Multi-dimensional array _____________________________")

# OUTPUT
# [1, 2]
# [7, 8]
# 6
# 7

multd = [[1,2], [3,4], [5,6], [7,8]]
print(multd)
print(multd[0])
print(multd[3])
print(multd[2][1])
print(multd[3][0])
