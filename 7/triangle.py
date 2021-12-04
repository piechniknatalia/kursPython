from points import Point
import math


class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        if x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) == 0:
            raise ValueError("Punkty sa wspolliniowe")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):          # "[(x1, y1), (x2, y2), (x3, y3)]"
        return "[({}, {}), ({}, {}), ({}, {})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)

    def __repr__(self):         # "Triangle(x1, y1, x2, y2, x3, y3)"
        return "Triangle({}, {}, {}, {}, {}, {})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)

    def __eq__(self, other):   # obsługa tr1 == tr2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2 and self.pt3 == other.pt3

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):           # zwraca środek trójkąta
        return Point((self.pt1.x + self.pt2.x + self.pt3.x) / 3, (self.pt1.y + self.pt2.y + self.pt3.y) / 3)

    def area(self):            # pole powierzchni
        return 0.5 * abs((self.pt2.x - self.pt1.x)*(self.pt3.y - self.pt1.y) - (self.pt2.y - self.pt1.y)*(self.pt3.x - self.pt1.x))

    def move(self, x, y):       # przesunięcie o (x, y)
        return Triangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y, self.pt3.x + x, self.pt3.y + y)

    def make4(self):          # zwraca krotkę czterech mniejszych
        a = Point((self.pt1.x+self.pt3.x)/2, (self.pt1.y+self.pt3.y)/2)
        b = Point((self.pt1.x+self.pt2.x)/2, (self.pt1.y+self.pt2.y)/2)
        c = Point((self.pt2.x+self.pt3.x)/2, (self.pt2.y+self.pt3.y)/2)
        t1 = Triangle(self.pt1.x, self.pt1.y, a.x, a.y, b.x, b.y)
        t2 = Triangle(a.x, a.y, b.x, b.y, c.x, c.y)
        t3 = Triangle(a.x, a.y, self.pt3.x, self.pt3.y, c.x, c.y)
        t4 = Triangle(c.x, c.y, b.x, b.y, self.pt2.x, self.pt2.y)
        return (t1, t2, t3, t4)
#     A       po podziale    A
#    / \                    / \
#   /   \                  a---b
#  /     \                / \ / \
# C-------B              C---c---B

# Kod testujący moduł.

import unittest

class TestTriangle(unittest.TestCase):

    def test_print(self):  # test str() i repr()
        self.assertEqual(str(Triangle(2, 1, 5, 4, 8, 1)), "[(2, 1), (5, 4), (8, 1)]")
        self.assertEqual(repr(Triangle(2, 1, 5, 4, 8, 1)), "Triangle(2, 1, 5, 4, 8, 1)")

    def test_cmp(self):
        self.assertTrue(Triangle(2, 1, 5, 4, 8, 1) == Triangle(2, 1, 5, 4, 8, 1))
        self.assertFalse(Triangle(2, 1, 5, 4, 8, 1) == Triangle(2, 1, 5, 4, 8, 2))
        self.assertTrue(Triangle(2, 1, 5, 4, 8, 1) != Triangle(2, 1, 5, 4, 8, 2))
        self.assertFalse(Triangle(2, 1, 5, 4, 8, 1) != Triangle(2, 1, 5, 4, 8, 1))

    def test_center(self):
        self.assertEqual(Triangle(2, 1, 5, 4, 8, 1).center(), Point(5, 2))
        #self.assertTrue(Triangle(2, 1, 5, 4, 8, 1).center == Point(5, 2))

    def test_area(self):
        self.assertEqual(Triangle(2, 1, 5, 4, 8, 1).area(), 9)

    def test_move(self):
        self.assertEqual(Triangle(2, 1, 5, 4, 8, 1).move(1, 1), Triangle(3, 2, 6, 5, 9, 2))

    def test_make4(self):
        self.assertEqual(Triangle(4, 4, 8, 0, 0, 0).make4(), ((Triangle(4, 4, 2, 2, 6, 2), Triangle(2, 2, 6, 2, 4, 0), Triangle(2, 2, 0, 0, 4, 0), Triangle(4, 0, 6, 2, 8, 0))))

if __name__ == "__main__":
    unittest.main()  # wszystkie testy



