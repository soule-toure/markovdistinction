"""
@Souleman Toure
Due: 09-15-2022 @10PM
What would a Markov chain look like in code?
This program creates an image of the day and using a markov chain determines what the next image of a day will be drawn. We have Day, Night, Full Moon, Double Moon, and Double Sun
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
               current_landscape (str): the current landscape
        """
        return np.random.choice(
            self.landscapes,
            p=[self.transition_matrix[current_landscape][next_landscape] \
                for next_landscape in self.landscapes]
        )

    def compose_image(self, time, drawings=5):
        """ Draws the images.
           Args:
                time (int): a number selected by the user
                drawings (int): how many drawings we should generate for the portfolio.
        """
        
        my_images = []
        current_landscape = " "
  
        if (time < 0) | (time > 23):
          print("Invalid Time...Sorry Try Again!")
          exit()
        elif time < 4:
            current_landscape = "Nice Moon"
        elif 4 < time < 7:
            current_landscape = "Night"
        elif 7 < time < 13:
            current_landscape = "Day"
        elif 13 < time < 19:
            current_landscape = "Double Sun"
        elif 19 < time < 24:
            current_landscape = "Double Moon"
          
        my_images.append(current_landscape)
      
        while len(my_images) < drawings:
            next_landscape = self.getnextimage(current_landscape)
            my_images.append(next_landscape)
            current_landscape = next_landscape
        return my_images

    def draw_star(self, turtle_dude, x, y, angle, side_length, filled):
        """ This function draw the stars in the picture
        Args:
          turtle_dude (obj): the turtle
          color (str): the color of the star
          x (int): x-coordinate
          y (int): y-coordinte
          angle (int): angle for the turtle to draw
          side_length (int): size of the stars
          filled (boolean): fill star or not
        """
        turtle_dude.speed("slowest")
        turtle_dude.color("yellow")
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
        turtle_dude.up()
        turtle_dude.home()
        turtle_dude.hideturtle()
      
    def draw_sun(self, turt, x, y):
        """ This function draw the stars in the picture
        Args:
          turt (obj): the turtle
          x (int): x-coordinate
          y (int): y-coordinte
        """
        turt.color("orange","orange")
        turt.up()
        turt.goto(x, y)
        turt.down()
        turt.begin_fill()
        turt.circle(50,360)
        turt.end_fill()
        for i in range(18):
            turt.right(90)
            turt.penup()
            turt.forward(10)
            turt.pendown()
            turt.forward(10)
            turt.penup()
            turt.backward(20)
            turt.left(90)
            turt.circle(50,20)
        turt.hideturtle()
          
    def draw_moon(self, turt, x, y):
        """ This function draw the stars in the picture
        Args:
          turt (obj): the turtle
          x (int): x-coordinate
          y (int): y-coordinte
        """
        turt.up()
        turt.goto(x,y)
        turt.color('grey')
        turt.begin_fill()
        turt.circle(50)
        turt.end_fill()
        turt.hideturtle()

    def draw_landscapes(self, my_images):
        """Takes the images from my list and paints them into real "landscapes" or drawings
        Args:
        my_images (list): Landscapes 
        """
        window = turtle.Screen()
        bert = turtle.Turtle()
        for painting in my_images:
            print("Here is my " + painting + " art!")   
            if painting == "Day":
                window.bgcolor("yellow")      
                self.draw_sun(bert, 100, 50)
              
            elif painting == "Night":
                window.bgcolor("black")
                self.draw_star(bert, -100, 25, 0, 10, True)      
                self.draw_moon(bert, -40, 0)
                self.draw_star(bert, 100, 75, 0, 10, True)

            elif painting == "Nice Moon":
                window.bgcolor("dark blue")
                self.draw_star(bert, -100, 25, 0, 10, True)      
                self.draw_moon(bert, -40, 0)
                self.draw_star(bert, 100, 75, 0, 10, True)
              
            elif painting == "Double Moon":
                window.bgcolor("dark blue")
                self.draw_star(bert, 0, 25, 0, 10, True)
                self.draw_moon(bert, -120, 0)
                self.draw_moon(bert, 120, 0)
                self.draw_star(bert, 50, 75, 0, 10, True)
                self.draw_star(bert, 0, 75, 0, 10, True)

            elif painting == "Double Sun":
                window.bgcolor("yellow")
                self.draw_sun(bert, 100, 25)
                self.draw_sun(bert, -100, 25)
            turtle.clearscreen()
        turtle.bye()


def main():

    art_maker = MarkovArtist({
        "Day": {"Day": 0.1, "Night": 0.55, "Nice Moon": 0.15, "Double Moon": .1, "Double Sun":.1 },
        "Night": {"Day": 0.50, "Night": 0.15, "Nice Moon": 0.15, "Double Moon": .1, "Double Sun": .1 },
        "Nice Moon": {"Day": 0.5, "Night": 0.15, "Nice Moon": 0.05, "Double Moon": .2, "Double Sun": .1 },
        "Double Moon": {"Day": 0.65, "Night": 0.05, "Nice Moon": 0.1, "Double Moon": .05, "Double Sun": .15 },
        "Double Sun": {"Day": 0.55, "Night": 0.15, "Nice Moon": 0.1, "Double Moon": .15, "Double Sun": .05 }
    })

    image_list = art_maker.compose_image(time=int(input("Pick a number from 0-23: ")), drawings=5)
    print("Current States:", image_list)
    art_maker.draw_landscapes(image_list)
    print("Thank you for visiting my portfolio! I hope you enjoyed, and come back again sometime.")

main()