"""
Learning Objectives
- Let's remember Python!
- What would a Markov chain look like in code?
Example of an Markov Chain implementation in Python (using concepts we learned
in 1101).
Dependencies: numpy,
"""

import numpy as np
import turtle

class MarkovArtist:

    def __init__(self, transition_matrix):
        """Simulates an artist that relies on a simple Markov chain.
           Args:
                transition_matrix (dict): transition probabilities
        """
        self.transition_matrix = transition_matrix
        self.landscapes = list(transition_matrix.keys())

    def getnextimage(self, current_landscape):
        """Decides which landscape to draw next based on the current landscape.
           Args:
               current_landscape (str): the current landscape being drawn.
        """
        return np.random.choice(
            self.landscapes,
            p=[self.transition_matrix[current_landscape][next_landscape] \
               for next_landscape in self.landscapes]
        )

    def compose_image(self, current_landscape="Day", drawings=3):
        """ Draws the images.
           Args:
                current_landscape (str): the current of the song that we are currently
                looking at.
                drawings (int): how many drawings we should generate for the portfolio.
        """
        my_images = []
        while len(my_images) < drawings:
            next_landscape = self.getnextimage(current_landscape)
            my_images.append(next_landscape)
            current_landscape = next_landscape
        return my_images

    def draw_star(self, turtle_dude, color, x, y, angle, side_length, filled):
        """ This function draw the stars in the picture
        Args:
          turtle_dude (obj):
          color (str):
          x (int): 
          y (int):
          angle (int):
          side_length (int)
          filled (boolean)
        
        """
        turtle_dude = turtle.Turtle()
        turtle_dude.speed("fast")
        turtle_dude.color(color)
        turtle_dude.seth(angle)
        turtle_dude.up()
        turtle_dude.goto(x,y)
        turtle_dude.down()
        if filled:
            turtle_dude.begin_fill()
        turtle_dude.right(150)
        turtle_dude.forward(side_length)
        turtle_dude.right(-60)
        turtle_dude.forward(side_length)
        turtle_dude.right(120)
        turtle_dude.forward(side_length)
        turtle_dude.right(-60)
        turtle_dude.forward(side_length)
        turtle_dude.right(120)
        turtle_dude.forward(side_length)
        turtle_dude.right(-60)
        turtle_dude.forward(side_length)
        turtle_dude.right(120)
        turtle_dude.forward(side_length)
        turtle_dude.right(-60)
        turtle_dude.forward(side_length)
        turtle_dude.right(120)
        turtle_dude.forward(side_length)
        turtle_dude.right(-60)
        turtle_dude.forward(side_length)
        turtle_dude.right(120)
        turtle_dude.forward(side_length)
        turtle_dude.right(-60)
        turtle_dude.forward(side_length)
        turtle_dude.right(120)
        turtle_dude.forward(side_length)
        if filled:
            turtle_dude.end_fill()
        turtle_dude.hideturtle()

    def draw_landscapes(self, my_images):
        """Transforms the string melody into a list of sound waves.
        Args:
        my_images (list): Landscapes 
        """
        window = turtle.Screen()
        for painting in my_images:
            print("Here is my " + painting + " art!")
            if painting == "Day":
                window.bgcolor("white")
                bert = turtle.Turtle()       
                bert.speed("slow")
                bert.up()
                bert.goto(100, 150)
                bert.down()
                #draw sun here

            elif painting == "Night":
                window.bgcolor("black")
                bert = turtle.Turtle()
                self.draw_star(bert, 'yellow', -300, 50, 0, 10, True)
                self.draw_star(bert, 'yellow', -225, 250, 0, 10, True)
                self.draw_star(bert, 'yellow', -125, 250, 0, 10, True)
                self.draw_star(bert, 'yellow', -25, 75, 0, 10, True)
                self.draw_star(bert, 'yellow', 75, 150, 0, 10, True)
                self.draw_star(bert, 'yellow', 150, 125, 0, 10, True)
                bert.up()
                bert.goto(175, 150)
                bert.down()
                #drawn half moon here

            elif painting == "Nice Moon":
                window.bgcolor("black")
                bert = turtle.Turtle()
                self.draw_star(bert, 'yellow', 20, 100, 0, 10, True)
                self.draw_star(bert, 'yellow', 100, 200, 0, 10, True)
                self.draw_star(bert, 'yellow', 175, 250, 0, 10, True)
                self.draw_star(bert, 'yellow', 260, 75, 0, 10, True)
                self.draw_star(bert, 'yellow', 350, 150, 0, 10, True)
                self.draw_star(bert, 'yellow', 500, 125, 0, 10, True)
                bert.up()
                bert.goto(175, 150)
                bert.down()
                #draw moon here
            turtle.clearscreen()
        turtle.bye()


def main():

    art_maker = MarkovArtist({
        "Day": {"Day": 0.2, "Night": 0.65, "Nice Moon": 0.15},
        "Night": {"Day": 0.55, "Night": 0.20, "Nice Moon": 0.25},
        "Nice Moon": {"Day": 0.7, "Night": 0.2, "Nice Moon": 0.1},
    })

    image_list = art_maker.compose_image(current_landscape="Day", drawings=5)
    print("Current States:", image_list)
    art_maker.draw_landscapes(image_list)


main()