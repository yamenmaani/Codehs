"""
Your school is hosting a diving contest, and they need a programmer to work on the scoreboard!

Your job is to calculate each diver’s total after the three judges hold up their individual scores.

Write the function calculate_score which takes a tuple of three numbers from 0 to 10 and calculate the sum. A perfect dive is worth 30 points, a belly flop is worth 0.

For example:

calculate_score((10, 10, 10))
# => 30
calculate_score((9, 9, 6))
# => 24
"""
# fill in this function to return the total of the three judges' scores!

def calculate_score(jude_scores):
    hello = jude_scores [0] + jude_scores[1] + jude_scores[2]
    print(hello)
    return hello
calculate_score((3,3,3))
calculate_score((1,1,1))
calculate_score((0,0,1))
