mylist = ["apple", "banana", "cherry"]

# Adding new elements
mylist.append("grape")

# Accessing data
print("mylist[0]: " + mylist[0])
print("mylist[-1]: " + mylist[-1])
print()

mylist.pop()
# Modifying data (notice duplicate data)
mylist[1] = "apple"
print("mylist: " + str(mylist))
print()

# Iterating through data
size = len(mylist)
for i in range(size):
    print(mylist[i])
print()

for fruit in mylist:
    print(fruit)

