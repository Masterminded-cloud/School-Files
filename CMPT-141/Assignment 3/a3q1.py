import turtle as t
import 
import random as rand

def

draw_spiral(num_segments,length):

    """

    Uses turtle graphics to draw a spiral with a random color,

    starting at random location.


    :param num_segments: The number of line segments in the spiral

    :param length: The number of pixels in the first segment

    :return: none

    """

    t.pencolor(rand.random(), rand.random(), rand.random())

    x = rand.randint(-100, 100)

    y = rand.randint(-100, 100)

    t.up()

    t.goto(x, y)

    t.down()


    for j in range(num_segments):

        t.pensize(rand.randint(1,6))

        t.forward(length * (j+1))

        t.right(45 - j/2)



------------- main program
 -----------

#Set up the turtle to draw fast


t.speed(10)

t.hideturtle()

t.title('Spiral Art')


# decide the length of the first spiral segment 

number_of_pixels = 2


# decide how many spirals will be drawn

# This should be between 1 and 7

number_of_spirals = 5


# draw the spirals using a loop calling a function draw_spiral()

# The first spiral should have 20 segments, and 2nd should have a random

# number of segments between 20 and 30, and the third should a random

# number of segments between 20 and 40, and so on...

for i in range(number_of_spirals):

        draw_spiral(rand.randint(20,20+10*i),number_of_pixels)


#tell the turtle we are done!

t.done()