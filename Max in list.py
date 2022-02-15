"""
Write the function max_int_in_list that takes a list of ints and returns the biggest int in the list. You can assume that the list has at least one int in it. A call to this function would look like:

my_list = [5, 2, -5, 10, 23, -21]
biggest_int = max_int_in_list(my_list)
# biggest_int is now 23
Do not use the built-in function max in your program!
"""
# your function should return the maximum value in `my_list`
def max_int_in_list(my_list):
   hello = my_list
   hello.sort()
   return hello[-1]

max_int_in_list([1, 2, 3])
max_int_in_list([5, 2, -5, 10, 23, -21])
max_int_in_list([5, 2, -5, 10, 23, -21])
