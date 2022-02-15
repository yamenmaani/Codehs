"""
Write a program that keeps track of a simple inventory for a store. While there are still items left in the inventory, ask the user how many items they would like to buy. Then print out how many are left in inventory after the purchase. You should use a while loop for this problem. A sample run is below.

We have 20 items in inventory.
How many would you like to buy? 4
Now we have 16 left.
We have 16 items in inventory.
How many would you like to buy? 2
Now we have 14 left.
We have 14 items in inventory.
How many would you like to buy? 8
Now we have 6 left.
We have 6 items in inventory.
How many would you like to buy? 5
Now we have 1 left.
We have 1 items in inventory.
How many would you like to buy? 1
All out!
Make sure you catch the case where the user tries to buy more items than there are in the inventory. In that case, you should print a message to the user saying that their request isn’t possible. For example:

We have 5 items in inventory.
How many would you like to buy? 6
There is not enough in inventory for that purchase.
We have 5 items in inventory.
How many would you like to buy? 5
All out!
"""
num_items = 20
while num_items != 0:
    print("We have " + str(num_items) + " items in inventory.")
    buy = int(input("How many would you like to buy?"))
    num_items = num_items - buy
    if (num_items > 0) :
        print("Now we have " + str(num_items) + " left.")
    elif (num_items < 0):
        print("There is not enough in inventory for that purchase.")
        num_items = num_items +buy
    else:
       print("All out!")
