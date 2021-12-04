import math
class Point:
    """Klasa reprezentujaca punkty na plaszczyznie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):
        return("({}, {})".format(self.x, self.y))

    def __repr__(self):
        """zwraca string Point(x, y)"""
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        """obsluga point1 == point2"""
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """obsluga point1 != point2"""
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):
        """ v1 + v2"""
        a = self.x + other.x
        b = self.y + other.y
        return Point(a, b)

    def __sub__(self, other):
        """v1 - v2"""
        a = self.x - other.x
        b = self.y - other.y
        return Point(a, b)

    def __mul__(self, other):
        """v1 * v2, iloczyn skalarny, zwraca liczbe"""
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        """v1 x v2, iloczyn wektorowy 2D, zwraca liczbe"""
        return self.x * other.y - self.y * other.x

    def length(self):
        """ dlugosc wektora"""
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __hash__(self):
        return hash((self.x, self.y))

# Kod testujacy modul.

import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(3, 4)

    def test_print(self):       # test str() i repr()
        self.assertEqual(str(self.p1), "(3, 4)")
        self.assertEqual(repr(self.p1), "Point(3, 4)")

    def test_cmp(self):
        self.assertTrue(Point(2, 4) == Point(2, 4))
        self.assertFalse(Point(2, 4) == Point(1, 4))
        self.assertTrue(Point(2, 4) != Point(1, 4))
        self.assertFalse(Point(2, 4) != Point(2, 4))

    def test_add(self):
        self.assertEqual(self.p1 + Point(2, 3), Point(5, 7))

    def test_sub(self):
        self.assertEqual(self.p1 - Point(2, 3), Point(1, 1))

    def test_mul(self):
        self.assertEqual(Point(2, 3) * Point(1, 2), 8)

    def test_cross(self):
        self.assertEqual(self.p1.cross(Point(1, 2)), 2)

    def test_length(self):
        self.assertEqual(self.p1.length(), 5)

    def test_hash(self):
        self.assertEqual(hash(self.p1), hash((self.p1.x, self.p1.y)))

if __name__ == "__main__":
     unittest.main()     # wszystkie testy



