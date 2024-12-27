# Define a tuple
my_tuple = (1, 3, 5, 7, 3, 9, 3)

# Using the count() method: Counts the occurrences of a value
count_of_3 = my_tuple.count(3)
print("Count of 3 in the tuple:", count_of_3)

# Using the index() method: Finds the first index of a value
index_of_7 = my_tuple.index(7)
print("Index of 7 in the tuple:", index_of_7)

# Accessing elements using indexing
first_element = my_tuple[0]
print("First element:", first_element)

# Accessing elements using slicing
slice_of_tuple = my_tuple[1:4]
print("Slice of tuple (1:4):", slice_of_tuple)

# Checking if an element exists in the tuple
is_5_present = 5 in my_tuple
print("Is 5 in the tuple?", is_5_present)

# Iterating over the tuple
print("Iterating over the tuple:")
for item in my_tuple:
    print(item)

# Converting tuple to a list (Tuples are immutable)
converted_list = list(my_tuple)
print("Converted to list:", converted_list)

# Length of the tuple
length_of_tuple = len(my_tuple)
print("Length of the tuple:", length_of_tuple)
