"""Testing the various functions of the turtle library."""
from turtle import Turtle, colormode, done
colormode(255)


side_length: float = 300.0
myturt: Turtle = Turtle()
myturt.color("blue")
myturt.speed(2)
myturt.begin_fill()
i = 0
while i < 3:
    myturt.forward(side_length)
    myturt.left(120)
    i += 1

myturt.end_fill()

myturt.ht()

bob: Turtle = Turtle()
bob.color("black")
bob.speed(50)

j = 0
while j < 300:
    bob.forward(side_length)
    bob.left(121.5)
    j += 1
    side_length *= 0.97

done()