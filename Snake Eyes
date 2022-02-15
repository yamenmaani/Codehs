"""
Write a program that rolls two dice until the user gets snake eyes. You should use a loop and a half to do this. Each round you should roll two dice (Hint: use the randint function!), and print out their values. If the values on both dice are 1, then it is called snake eyes, and you should break out of the loop. You should also use a variable to keep track of how many rolls it takes to get snake eyes.

Sample Run:

Rolled: 6 5
Rolled: 5 2
Rolled: 3 6
Rolled: 6 2
Rolled: 1 2
Rolled: 5 3
Rolled: 1 4
Rolled: 1 1
It took you 8 rolls to get snake eyes.
"""
import random 
hello = 0
while True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print ("Rolled:"+str(dice1) + " " + str(dice2)+"")
    hello += 1
    if dice1==1 and dice2==1:
        break
print ("It took you " + str(hello)+ (" rolls to get snake eyes."))
