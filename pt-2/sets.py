# Notice duplicate data
myset = {"apple", "banana", "banana", "pear"}

# Duplicate data will not be added
print("Inital myset: " + str(myset))

myset.add("apple")
print("myset: " + str(myset))

# Removing data
myset.remove("banana")
print("myset: " + str(myset))


if "pear" in myset:
    print("Found pear!")
else:
    print("No pear!")


# Iterating through data
for fruit in myset:
    print(fruit)

# Modifying or indexing data will throw an error
# myset[1] = "apple" # will not work
# print(myset[0]) # will not work
