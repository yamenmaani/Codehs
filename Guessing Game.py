"""
Overview
The computer picks a number between 1 and 100, and you have to guess it.
The computer will tell you whether your guess was too high, too low, or correct.
Your assignment is to generate a random number and let the user guess numbers until they guess the correct number.
"""
import random
# Enter your code here ok thanks for telling me ;)
random_num = random.randint(1,100)
hello = input("guess a number please: ")
print(random_num)
while hello != str(random_num):
    if hello > str(random_num):
        print("the number is lower: ")
    if hello< str(random_num):
        print("the number is higher: ")
    hello = input("guss a number please: ")
else:
    print ("welldone correct the is the number "+str(random_num))
