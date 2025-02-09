# Dictionaries
# Creating a Dictionary
dict_name = {} # Creates an empty dictionary
person = { "name": "John",  "age": 30, "city": "New York"}

# Accessing Values
# Value = dict_name["key_name"]
name = person["name"]
age = person["age"]

# Add or modify
# dict_name[key] = value
person["Country"] = "USA" # A new entry will be created.
person["city"] = "Chicago"  # Update the existing value for the same key

# del
# del dict_name[key]
del person["Country"]

# updata()
# dict_name.update({key: value})
person.update({"Profession": "Doctor"})

# clear()
# dict_name.clear()
person.clear()

# key existence
if "name" in person:
    print("Name exists in the dictionary.")

# copy()
# new_dict = dict_name.copy()
new_person = person.copy()
new_person = dict(person) # another way to create a copy of dictionary

# keys()
# keys_list = list(dict_name.keys())
person_keys = list(person.keys())

# values()
# values_list = list(dict_name.values())
person_values = list(person.values())

# items
# items_list = list(dict_name.items())
info = list(person.items())

# Sets
# add()
# set_name.add(element) 
fruits = set([])
fruits.add("mango")
print(fruits)

# clear()
# set_name.clear() 
fruits.clear()

# copy()
# new_set = set_name.copy() 
new_fruits = fruits.copy()

# Defining Sets
empty_set = set() #Creating an Empty 
fruits = {"apple", "banana", "orange"}

# discard()
# set_name.discard(element) 
fruits.discard("apple")
fruits

# issubset()
# is_subset = set1.issubset(set2)
colors = {"red", "yellow", "green", "orange", "blue", "banana"}  # Includes some fruit names
is_subset = fruits.issubset(colors)

# issuperset()
# is_superset = set1.issuperset(set2)
is_superset = colors.issuperset(fruits)
is_superset

# pop()
# removed_element = set_name.pop() 
removed_fruit = fruits.pop()

# remove()
# set_name.remove(element) 
fruits.remove("banana")

# Set Operations
# union_set = set1.union(set2) 
# intersection_set = set1.intersection(set2) 
# difference_set = set1.difference(set2) 
# sym_diff_set = set1.symmetric_difference(set2) 
combined = fruits.union(colors) 
combined
common = fruits.intersection(colors) 
common
unique_to_fruits = fruits.difference(colors) 
unique_to_fruits
sym_diff = fruits.symmetric_difference(colors)
sym_diff

# update()
# set_name.update(iterable)
fruits.update(["kiwi", "grape"])
fruits