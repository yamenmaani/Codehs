"""
Write a function that takes a height in feet and inches and converts it to meters.

For example, if you are 6 feet, 4 inches tall, then calling

convert_height_to_meters(6, 4)
should result in 1.9304 meters. With all these calls,

convert_height_to_meters(6, 4)
convert_height_to_meters(5, 8)
convert_height_to_meters(5, 2)
you should print:

6 feet, 4 inches = 1.9304 meters
5 feet, 8 inches = 1.7272 meters
5 feet, 2 inches = 1.5748 meters
Your function must be named convert_height_to_meters
"""

INCHES_TO_CM = 2.54
CM_TO_METERS = 0.01
FEET_TO_INCHES = 12
def convert_height_to_meters(feet,inches):
    hello = feet * FEET_TO_INCHES * INCHES_TO_CM * CM_TO_METERS
    mello = inches * INCHES_TO_CM * CM_TO_METERS
    print (hello + mello)

convert_height_to_meters(2,3)
convert_height_to_meters(9,4)
convert_height_to_meters(7,1)
