from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super(Paddle, self).__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.goto(position)

    def move_up(self):
        if self.heading() != 90:
            self.turtlesize(stretch_wid=1, stretch_len=5)
            self.setheading(90)
            self.forward(20)
        else:
            self.forward(20)


    def move_down(self):
        if self.heading() != 270:
            self.turtlesize(stretch_wid=1, stretch_len=5)
            self.setheading(270)
            self.forward(20)
        else:
            self.forward(20)
