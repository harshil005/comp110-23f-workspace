from turtle import Turtle, colormode, done
"""EX05- Constructing a scenery using the turtle module."""
__author__ = "730711765"
"""for part 2., i have made the mountains 3 times instead of 2 to give it a better look.
for extra credit, i have made use of the functions bgfill and circle"""

colormode(255)


def mountain(mountain_object: Turtle, mountain_x: float, mountain_y: float, side_len: float) -> None:
    """Draws a  mountain shaped like a triangle starting from a point (x,y) of a given length."""
    j: int = 0
    mountain_object.penup()
    mountain_object.color("brown")
    mountain_object.goto((mountain_x), mountain_y)
    mountain_object.pendown()
    mountain_object.begin_fill()
    while (j < 3):
        mountain_object.forward(side_len)
        mountain_object.left(120)
        j = j + 1
    mountain_object.end_fill()
    mountain_object.ht()


def sun(sun_object: Turtle, sun_x: float, sun_y: float, radius: float) -> None:
    """Draw a circular-shaped sun at centre (x,y) with a given radius."""
    sun_object.color("yellow", "yellow")
    sun_object.begin_fill()
    sun_object.penup()
    sun_object.goto(sun_x, sun_y)
    sun_object.pendown()
    
    sun_object.circle(radius)
    sun_object.end_fill()
    sun_object.ht()


def river(river_object: Turtle, river_x: float, river_y: float, side_len: float) -> None:
    """Draw a rectangular-shaped river from a point x,y of a given length."""
    i: int = 0
    river_object.penup()
    river_object.color(0, 204, 255)
    river_object.goto(river_x, river_y)
    river_object.pendown()
    river_object.begin_fill()
    while (i < 2):
        
        river_object.forward(side_len)
        river_object.left(90)
        river_object.forward(side_len / 3)
        river_object.left(90)
        i = i + 1
    river_object.end_fill()
    river_object.ht()


drawing = Turtle()
drawing.screen.bgcolor("orange")
drawing.ht()
mysun = Turtle()
sun(mysun, 0.0, 120.0, 80.0)

mymountains = Turtle()
for i in range(3):
    mountain(mymountains, (-400 + (i * (400 // 2))), -100, 400.0)

myriver = Turtle()
river(myriver, -400.0, -400, 1000.0)

if __name__ == "main":
    main()

done()