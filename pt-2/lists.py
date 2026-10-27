mylist = ["apple", "banana", "cherry"]

# Ading new elements
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
for i in range(len(mylist)):
    print(mylist[i])
print()

for fruit in mylist:
    print(fruit)

