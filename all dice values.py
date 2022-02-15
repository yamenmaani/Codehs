"""
Write a program that prints all possible dice rolls with two dice. To do so, you should use a nested for loop.

Hint: You can’t use i for both for loops.

Here’s what your program should print

1,1
1,2
1,3
1,4
1,5
1,6
2,1
...
...
6,4
6,5
6,6
"""
dic1 = 0
dic2 = 1
for i in range(6):
    dic1 = dic1 +1
    print (dic1,",",dic2)
    dic2 = 1
    for i in range(5):
        dic2+=1
        print(dic1,",",dic2)
