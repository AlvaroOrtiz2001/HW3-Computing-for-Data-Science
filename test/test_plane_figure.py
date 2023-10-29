import pytest
from hw4 import Triangle, Rectangle, Circle

def test_triangle_perimeter_surface():
    triangle = Triangle(base=5, c1=4, c2=3, h=4)
    assert triangle.compute_perimeter() == 12
    assert triangle.compute_surface() == 10.0

def test_rectangle_perimeter_surface():
    rectangle = Rectangle(a=4, b=6)
    assert rectangle.compute_perimeter() == 20
    assert rectangle.compute_surface() == 24

def test_circle_perimeter_surface():
    circle = Circle(radius=3)
    assert round(circle.compute_perimeter(), 2) == 18.85  # Rounded to two decimal places
    assert round(circle.compute_surface(), 2) == 28.27
