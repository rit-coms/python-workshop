mydict = {"Name": "Sean", "Major": "Computer Science", "Age": 21, 42: 8}

# We can use indexing syntax to get the value for a key
print(mydict["Name"])
print(mydict.get("Name"))
print()
# mydict["Last Name"] would throw an error
# mydict.get("Last Name") would return None

# We can also assign new values
mydict["Age"] = 40
print(mydict["Age"])
print()

# We can add new values
mydict["Year"] = 3
print(mydict["Year"])
print()

# We can remove values
mydict.pop("Year")
print(mydict.get("Year"))
print()

# We can use a dict to count the number of each value in another collection
mytuple = ("apple", "banana", "banana", "pear")
counts = {}
for fruit in mytuple:
    count = counts.get(fruit)
    if count is None:
        counts[fruit] = 1
    else:
        counts[fruit] += 1

print(counts)