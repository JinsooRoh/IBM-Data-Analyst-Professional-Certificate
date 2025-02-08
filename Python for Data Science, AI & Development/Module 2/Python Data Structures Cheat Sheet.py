# List

# append()
# list_name.append(element)
fruits = ["apple", "banana", "orange"] 
fruits.append("mango")
print(fruits)

# copy()
my_list = [1, 2, 3, 4, 5] 
new_list = my_list.copy()
print(new_list)

# count()
my_list = [1, 2, 2, 3, 4, 2, 5, 2] 
count = my_list.count(2)
print(count) 

# Creating a list()
fruits = ["apple", "banana", "orange", "mango"]

# del
# Removes the element at index 2 print(my_list) 
my_list = [10, 20, 30, 40, 50] 
del my_list[2] 

# extend()
# list_name.extend(iterable) 
fruits = ["apple", "banana", "orange"] 
more_fruits = ["mango", "grape"] 
fruits.extend(more_fruits) 
print(fruits)

# Indexing
my_list = [10, 20, 30, 40, 50] 
print(my_list[0]) 
print(my_list[-1]) 

# insert()
# list_name.insert(index, element) 
my_list = [1, 2, 3, 4, 5] 
my_list.insert(2, 6) 
print(my_list)

# Modifying a list
# Modifying the second element 
my_list = [10, 20, 30, 40, 50] 
my_list[1] = 25 
print(my_list) 

# pop()
# Removes and returns the element at index 2 
my_list = [10, 20, 30, 40, 50] 
removed_element = my_list.pop(2) 
print(removed_element) 
print(my_list) 

# Removes and returns the last element 
my_list = [10, 20, 30, 40, 50] 
removed_element = my_list.pop() 
print(removed_element)
print(my_list) 

# remove()
# Removes the element 30 
my_list = [10, 20, 30, 40, 50] 
my_list.remove(30) 
print(my_list) 

# reverse()
my_list = [1, 2, 3, 4, 5] 
my_list.reverse()
print(my_list) 

# Slicing
# list_name[start:end:step] 
my_list = [1, 2, 3, 4, 5] 
# elements from index 1 to 3
print(my_list[1:4])

# elements from the beginning up to index 2
print(my_list[:3]) 

# elements from index 2 to the end
print(my_list[2:]) 

# every second element
print(my_list[::2]) 

# sort()
# Ascending Order
my_list = [5, 2, 8, 1, 9] 
my_list.sort() 
print(my_list) 

# Descending Order
my_list = [5, 2, 8, 1, 9] 
my_list.sort(reverse=True) 
print(my_list) 

# Tuple

# count()
# tuple.count(value)
# Counts the number of times apple is found in tuple
fruits = ("apple", "banana", "apple", "orange")
print(fruits.count("apple"))

# index()
# tuple.index(value) 
#Returns the value at which apple is present
fruits = ("apple", "banana", "orange")
print(fruits[1]) 

# sum()
# sum(tuple) 
numbers = (10, 20, 5, 30)
print(sum(numbers))

# min() and max()
numbers = (10, 20, 5, 30)
print(min(numbers))  
print(max(numbers))

# len()
# len(tuple)
# Returns length of the tuple
fruits = ("apple", "banana", "orange")
print(len(fruits)) 
