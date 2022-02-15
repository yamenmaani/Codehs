"""
task
Write a program that asks the user for two numbers. Using a for loop, add all of the numbers from the first to the second.

For example if the first number is 6 and the second number is 8 the result is 21 (6 + 7 + 8).

Print out the results when you are finished.
"""

MIN = int(input("Enter a number: "))
MAX = int(input("Enter another number: "))
sum = 0
for i in range(MIN, (MAX+1)):
     sum =sum + i
print("The sum is: " + str(sum))
