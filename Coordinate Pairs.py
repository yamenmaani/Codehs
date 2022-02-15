"""
Complete the distance function! It should take two arguments, each of which is a tuple with two elements. It should treat these tuples like points in a 2d coordinate plane. It should return the distance between them using the Pythagorean Theorem:

Square the difference between the x values.
Square the difference between the y values.
Add the two squares.
Take the square root of the result.
In order to compute the square root of something, you need to use the sqrt function. This function belongs to a module in Python called math. The first line of the code provided imports this module, so that you can use the functions in it. To take the square root of a number, simply do something like the following:

number = ...
result = math.sqrt(number)
You can also use the built-in Python function pow to take the square of a number, like this:

number = ...
square = pow(number, 2)
"""
import math


# fill in this function to return the distance between the two points!



def distance(first_point, second_point):
    first_x = first_point[0]
    first_y = first_point[1]
    second_x = second_point[0]
    second_y = second_point[1]
    
    both_x = first_x - second_x
    both_y = first_y - second_y
    final_x = math.pow(both_x,2)
    final_y = math.pow(both_y,2)
    both = final_x + final_y
    final = math.sqrt(both)
    print(final)
    return final
    

distance((0,0),(1,1))
distance((12,-10),(6,3))
distance((100,100),(65,12))
distance((200,100),(500,100))
