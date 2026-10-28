# Notice duplicate data
mytuple = ("apple", "banana", "banana", "pear")

# Accessing data
print("mytuple[0]: " + mytuple[0])
print("mytuple[-1]: " + mytuple[-1])
print()

# Iterating through data
size = len(mytuple)
for i in range(size):
    print(mytuple[i])
print()

for fruit in mytuple:
    print(fruit)

# Modifying data will throw an error
# mytuple[1] = "apple" # will not work
