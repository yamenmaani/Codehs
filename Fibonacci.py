"""
Write a program that prints out the numbers in the Fibonacci sequence up until the max number. You can figure out the next number in the Fibonacci sequence by adding the two previous numbers.

The first number is 1 and the second number is 1. To get the third number we take 1 + 1 = 2. To get the fourth number we take the second number plus the third number (1 + 2 = 3).

Here is a sample run of the program.

1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
"""
MAX = 1000
x = 0
y = 1
while x + y <MAX:
    print (y)
    x +=y
    print (x)
    y +=x
