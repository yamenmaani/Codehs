"""
Write a program to draw ghosts on the screen. You must do this by writing a function called draw_ghost, which takes three parameters, the x location of the ghost, the y location of the ghost and the color of the ghost. x and y for the ghost define where the center of the head should go.

Note: Be sure to include comments for all functions that you use or create.

def draw_ghost(center_x, center_y, color):

Final Product
Here is a screenshot of a sample run of the ghosts program with these function calls.

center_x = get_width()/2
center_y = get_height()/2
draw_ghost(center_x, center_y, Color.red)
draw_ghost(100, 100, Color.green)
draw_ghost(370, 150, Color.black)
draw_ghost(40, 200, Color.orange)
draw_ghost(300, 50, Color.yellow)
"""
# Constants for body
HEAD_RADIUS = 35
BODY_WIDTH = HEAD_RADIUS * 2
BODY_HEIGHT = 60
NUM_FEET = 3
FOOT_RADIUS = (BODY_WIDTH) / (NUM_FEET * 2)

# Constants for eyes
PUPIL_RADIUS = 6
PUPIL_LEFT_OFFSET = 8
PUPIL_RIGHT_OFFSET = 20
EYE_RADIUS = 10
EYE_OFFSET = 14


# Put your function(s) here
def draw_ghost(x,y,color):
    body = Rectangle(BODY_WIDTH,BODY_HEIGHT)
    body.set_position(x-BODY_WIDTH/2,y-BODY_HEIGHT/2)
    body.set_color(color)
    add(body)
    
    head = Circle(HEAD_RADIUS)
    head.set_position(x,y-BODY_HEIGHT/2)
    head.set_color(color)
    add(head)
    
    foot1 = Circle(FOOT_RADIUS)
    foot1.set_position(x-BODY_WIDTH/2+FOOT_RADIUS,y+BODY_HEIGHT/2)
    foot1.set_color(color)
    add(foot1)
    
    foot2 = Circle(FOOT_RADIUS)
    foot2.set_position(x,y+BODY_HEIGHT/2)
    foot2.set_color(color)
    add(foot2)
    
    foot3 = Circle(FOOT_RADIUS)
    foot3.set_position(x+BODY_WIDTH/2-FOOT_RADIUS,y+BODY_HEIGHT/2)
    foot3.set_color(color)
    add(foot3)
    
    eye = Circle(EYE_RADIUS)
    eye.set_position(x-HEAD_RADIUS/2,y-BODY_HEIGHT/2)
    eye.set_color(Color.white)
    add(eye)
    
    eye = Circle(EYE_RADIUS)
    eye.set_position(x+HEAD_RADIUS/2,y-BODY_HEIGHT/2)
    eye.set_color(Color.white)
    add(eye)
    
    pupil = Circle(PUPIL_RADIUS)
    pupil.set_position(x+HEAD_RADIUS/2 + EYE_RADIUS/2,y-BODY_HEIGHT/2)
    pupil.set_color(Color.blue)
    add(pupil)
    
    pupil = Circle(PUPIL_RADIUS)
    pupil.set_position(x-HEAD_RADIUS/2 + EYE_RADIUS/2,y-BODY_HEIGHT/2)
    pupil.set_color(Color.blue)
    add(pupil)

draw_ghost(200,100,Color.black)
draw_ghost(200,200,Color.green)
draw_ghost(300,300,Color.red)
