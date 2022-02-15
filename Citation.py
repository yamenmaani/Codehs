"""
Help your friend write their bibliography!

Write the function called citation that takes a tuple like this as input:

("Martin", "Luther", "King, Jr.")
and returns a name with the format:

Last, First Middle
In this example, the output should be:

King, Jr., Martin Luther
Here are some more examples:

citation(("J.", "D.", "Salinger"))
# => "Salinger, J. D."
citation(("Ursula", "K.", "Le Guin"))
# => "Le Guin, Ursula K."
citation(("J.", "K.", "Rowling"))
# => "Rowling, J. K."
"""
def citation(author_name):
    return author_name[-1] + ", " + author_name[0] + " " + author_name[1]

citation(("yamen","mohammed","maani"))
