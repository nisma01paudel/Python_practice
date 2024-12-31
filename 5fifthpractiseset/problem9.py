# #  Can you change the values inside a list which is contained in set S? 
# # s = {8, 7, 12, "HNisu", [1,2]}
# s = {8, 7, 12, "Nisu", [1,2]}

# s[4][0] = 9
# No, the code you provided will raise an error because sets in Python cannot contain mutable objects like lists. Lists are mutable (i.e., their contents can be changed), and since sets require all their elements to be immutable and hashable, you cannot include a list in a set.