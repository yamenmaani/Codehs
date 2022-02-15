"""
Your friend wants to try to make a word ladder! This is a list of words where each word has a one-letter difference from the word before it. Here’s an example:

cat
cot
cog
log
Write a program to help your friend. It should do the following:

Ask your friend for an initial word
Repeatedly ask them for an index and a letter
You should replace the letter at the index they provided with the letter they enter
You should then print the new word
Stop asking for input when the user enters -1 for the index
Here’s what should be happening behind the scenes:

You should have a function, get_index, that repeatedly asks the user for an index until they enter a valid integer that is within the acceptable range of indices for the initial string. (If they enter a number out of range, you should reply invalid index.)
You should have another function, get_letter, that repeatedly asks the user for a letter until they enter exactly one lowercase letter. (If they enter more than one character, you should reply Must be exactly one character!. If they enter a capital letter, you should reply Character must be a lowercase letter!.)
You should store a list version of the current word in a variable. This is what you should update each time the user swaps out a new letter.
Each time you have to print the current word, print the string version of the list you are keeping in your variable.
Here’s what an example run of your program might look like:

Enter a word: cat
Enter an index (-1 to quit): 1
Enter a letter: o
cot
Enter an index (-1 to quit): 2
Enter a letter: g
cog
Enter an index (-1 to quit): 5
Invalid index
Enter an index (-1 to quit): -3
Invalid index
Enter an index (-1 to quit): 0
Enter a letter: L
Character must be a lowercase letter!
Enter a letter: l
log
Enter an index (-1 to quit): -1
"""
def get_index(word):
    while True:
        try:
            pos = int(input("Enter an index: "))
            if pos == -1:
                return pos
            elif pos >= len(word):
                print ("Invalid index")
            elif pos <= -1:
                print ("Invalid index")
            else:
                return pos
        except ValueError:
            print ("invalid index")
            
def get_letter():
    
    while True:
        
        char = str(input("Enter a letter: "))
    
        if char.islower() and len(char)==1:
            return char
    
        elif  not char.islower():  
            print ("Character must be a lowercase letter!")
  
        elif len(char) > 1:
            print ("Must be exactly one character!")

def word_ladder(word):
    
    while True:
        pos = get_index(word)
        if pos == -1:
            return
        else:
            char=get_letter() 
            
            word = list(word)
            word[pos] = char
            word = ("").join(word)
            print (word)

word = input("Enter a word: ") 

word_ladder(word)
