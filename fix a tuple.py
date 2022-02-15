"""
In this exercise, you are given the following tuple:

my_tuple = (0, 1, 2, "hi", 4, 5)
Make it so that it instead holds:

(0, 1, 2, 3, 4, 5)
Remember that you cannot change a tuple, so this will not work:

# Error!
my_tuple[3] = 3
You also shouldn’t just do something like this:

# Incorrect! Too easy!
my_tuple = (0, 1, 2, 3, 4, 5)
Instead, use slices of the old tuple, and concatenate them with the element you want to add. Note that you should not just add the integer 3, but rather the tuple (3,).
"""
my_tuple = (0, 1, 2, "hi", 4, 5)
hello = (3,)
my_tuple = my_tuple[:3] +hello+ my_tuple[4:]

print (len(my_tuple))


print(my_tuple)
