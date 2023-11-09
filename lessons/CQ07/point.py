"""CQ07- Intro To Object Oriented Programming."""
from __future__ import annotations
__author__ = "730711765"


class Point:
    """Creates a point with x and y values."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0) -> None:
        """Initializes the x and y variables to input values."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scales the value of x and y by a given factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Returns a point from a given point scaled by a given factor."""
        return Point(self.x * factor, self.y * factor)
    
    def __str__(outpoint: Point) -> str:
        """Ouputs the point's x and y values."""
        return f"x: {outpoint.x}; y: {outpoint.y}"

    def __mul__(multpoint: Point, factor: int | float) -> Point:
        """Multiplies the x and y values of a point by a factor."""
        return Point(multpoint.x * factor, multpoint.y * factor)
    
    def __add__(addpoint: Point, factor: int | float) -> Point:
        """Adds the x and y values of a point by a number."""
        return Point(addpoint.x + factor, addpoint.y + factor)
    

 