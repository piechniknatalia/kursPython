import math
class Frac:
    """Klasa reprezentujaca ulamki."""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0
         if y == 0:
             raise ValueError("Nie dzielimy przez zero")
         self.x = x
         self.y = y
         a = math.gcd(x, y)
         if x == 0:
             self.x = 0
             self.y = 1
         else:
             self.x = x // a
             self.y = y // a

    def __str__(self):          # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return("{}".format(self.x))
        else:
            return("{}/ {}".format(self.x, self.y))

    def __repr__(self): # zwraca "Frac(x, y)"
        return "Frac({}, {})".format(self.x, self.y)

    # Py2
    #def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Py2.7 i Py3
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return float(self.x)/float(self.y) < float(other.x)/float(other.y)

    def __le__(self, other):
        return float(self.x) / float(self.y) <= float(other.x) / float(other.y)

    def __gt__(self, other):
        return float(self.x) / float(self.y) > float(other.x) / float(other.y)

    def __ge__(self, other):
        return float(self.x) / float(self.y) >= float(other.x) / float(other.y)

    def __add__(self, other):   # frac1+frac2, frac+int
        if isinstance(other, int):
            return Frac(other * self.y + self.x, self.y)
        else:
            if self.y != other.y:
                return Frac(self.x * other.y + other.x * self.y, self.y * other.y)
            else:
                return Frac(self.x + other.x, self.y)

    __radd__ = __add__              # int+frac

    def __sub__(self, other):   # frac1-frac2, frac-int
        if isinstance(other, int):
            return Frac(self.x - other * self.y, self.y)
        else:
            if self.y != other.y:
                return Frac(self.x * other.y - other.x * self.y, self.y * other.y)
            else:
                return Frac(self.x - other.x, self.y)

    def __rsub__(self, other):      # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):   # frac1*frac2, frac*int
        if isinstance(other, int):
            return Frac(self.x * other, self.y)
        else:
           return Frac(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__              # int*frac

    def __truediv__(self, other):   # frac1/frac2, frac/int, Py3
        if isinstance(other, int):
            return Frac(self.x, self.y * other)
        else:
            return Frac(self.x * other.y, self.y * other.x)

    def __rtruediv__(self, other):  # int/frac, Py3
        return Frac(self.y * other, self.x)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):          # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):       # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):        # float(frac)
        return float(self.x)/float(self.y)

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # assert set([2]) == set([2.0])

# Kod testujacy modul.

import unittest

class TestFrac(unittest.TestCase):

    def setUp(self):
        self.f1 = Frac(3, 4)

    def test_print(self):  # test str() i repr()
        self.assertEqual(str(self.f1), "3/ 4")
        self.assertEqual(repr(self.f1), "Frac(3, 4)")
        self.assertEqual(str(Frac(4, 1)), "4")
        self.assertEqual(repr(Frac(4, 1)), "Frac(4, 1)")


    def test_cmp(self):
        self.assertTrue(Frac(2, 4) == Frac(2, 4))
        self.assertFalse(Frac(2, 4) == Frac(1, 4))
        self.assertTrue(Frac(2, 4) != Frac(1, 4))
        self.assertFalse(Frac(2, 4) != Frac(2, 4))
        self.assertTrue(Frac(2, 4) < Frac(3, 4))
        self.assertFalse(Frac(2, 4) < Frac(1, 4))
        self.assertTrue(Frac(2, 4) <= Frac(2, 4))
        self.assertFalse(Frac(2, 4) <= Frac(1, 4))
        self.assertTrue(Frac(3, 4) > Frac(2, 4))
        self.assertFalse(Frac(2, 4) > Frac(3, 4))
        self.assertTrue(Frac(3, 4) >= Frac(2, 4))
        self.assertFalse(Frac(2, 4) >= Frac(3, 4))

    def test_add(self):
        self.assertEqual(Frac(3, 4) + Frac(4, 1), Frac(19, 4))
        self.assertEqual(Frac(3, 4) + 2, Frac(11, 4))
        self.assertEqual(2 + Frac(3, 4), Frac(11, 4))

    def test_sub(self):
        self.assertEqual(Frac(4, 1) - Frac(3, 4), Frac(13, 4))
        self.assertEqual(Frac(3, 4) - 2, Frac(-5, 4))
        self.assertEqual(2 - Frac(4, 1), Frac(-2, 1))

    def test_mul(self):
        self.assertEqual(Frac(1, 3) * Frac(2, 3), Frac(2, 9))
        self.assertEqual(Frac(1, 3) * 2, Frac(2, 3))
        self.assertEqual(2 * Frac(2, 3), Frac(4, 3))

    def test_truediv(self):
        self.assertEqual(Frac(1, 3) / Frac(2, 3), Frac(1, 2))
        self.assertEqual(Frac(4, 3) / 2, Frac(2, 3))
        self.assertEqual(2 / Frac(2, 3), Frac(3, 1))


    def test_pov(self):
        self.assertEqual(+Frac(3, 4), Frac(3, 4))

    def test_neg(self):
        self.assertEqual(-Frac(3, 4), Frac(-3, 4))

    def test_invert(self):
        self.assertEqual(~Frac(2, 1), Frac(1, 2))

    def test_float(self):
        self.assertAlmostEqual(float(Frac(3, 4)), 0.75, places=4)

    def test_hash(self):
        self.assertEqual(hash(self.f1), hash(Frac(self.f1.x, self.f1.y)))


if __name__ == "__main__":
    unittest.main()  # wszystkie testy