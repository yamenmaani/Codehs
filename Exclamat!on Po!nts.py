"""
Words are way more edgy when you replace the letter i with an exclamation point!

Write the function exclamations that takes a string and then returns the same string with every lowercase i replaced with an exclamation point. Your function should:

Convert the initial string to a list
Use a for loop to go through your list element by element
Whenever you see a lowercase i, replace it with an exclamation point in the list
Return the stringified version of the list when your for loop is finished
Here’s what an example run of your program might look like:

exclamations("I like music.")
# => I l!ke mus!c.
exclamations("Mississippi")
# => M!ss!ss!pp!"""
def exclamation(text):
    my_list = list(text)
    output = ""
    for item in my_list:
        if item == "!":
            output = output + "i"
        else:
            output = output + item
    print( output)
exclamation("hello there ! love python")
