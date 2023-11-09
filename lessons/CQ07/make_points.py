"""Testing the point class."""
from point import Point

x = Point(5, 5)
x.scale_by(5)

print(x.x, x.y)