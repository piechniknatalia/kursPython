class Time:
    """Klasa reprezentujaca odcinek czasu."""

    def __init__(self, s=0):
        """Zwraca instancje klasy Time."""
        if s < 0:
            raise ValueError("ujemny czas")
        self.s = int(s)

    def __str__(self):
        """Zwraca string 'hh:mm:ss'."""
        h = self.s // 3600
        sec = self.s - h * 3600
        m = sec // 60
        sec = sec - m * 60
        return "{0:02d}:{1:02d}:{2:02d}".format(h, m, sec)

    def __repr__(self):
        """Zwraca string 'Time(s)'."""
        return "Time({})".format(self.s)

    def __add__(self, other):
        """Dodawanie odcinkow czasu."""
        return Time(self.s + other.s)

    #def __cmp__(self, other): # Py2, porownywanie, -1|0|+1
    #    """Porownywanie odcinkow czasu."""
    #    return cmp(self.s, other.s)

    # Py2.7 i Py3, rich comparisons.
    def __eq__(self, other):
        return self.s == other.s

    def __ne__(self, other):
        return self.s != other.s

    def __lt__(self, other):
        return self.s < other.s

    def __le__(self, other):
        return self.s <= other.s

    # nadmiarowe
    #def __gt__(self, other):
    #    return self.s > other.s

    # nadmiarowe
    #def __ge__(self, other):
    #    return self.s >= other.s

    def __int__(self):                  # int(time1)
        """Konwersja odcinka czasu do int."""
        return self.s

# Kod testujacy modul - dopisac co najmniej dwa testy do kazdej sekcji.

import unittest

class TestTime(unittest.TestCase):


    def setUp(self):
        self.t1 = Time(3723)

    def test_print(self):       # test str() i repr()
        self.assertEqual(str(self.t1), "01:02:03")
        self.assertEqual(repr(self.t1), "Time(3723)")
        self.assertEqual(repr(Time(234)), "Time(234)")
        self.assertEqual(str(Time(234)), "00:03:54")

    def test_cmp(self):
        # Trzeba sprawdzac ==, !=, >, >=, <, <=.
        self.assertTrue(Time(2) == Time(2))
        self.assertFalse(Time(2) == Time(3))
        self.assertTrue(Time(2) != Time(3))
        self.assertFalse(Time(2) != Time(2))
        self.assertTrue(Time(2) < Time(3))
        self.assertFalse(Time(4) < Time(3))
        self.assertTrue(Time(2) <= Time(3))
        self.assertFalse(Time(4) <= Time(3))
        self.assertTrue(Time(4) > Time(3))
        self.assertFalse(Time(2) > Time(3))
        self.assertTrue(Time(4) >= Time(3))
        self.assertFalse(Time(2) >= Time(3))
        self.assertTrue(Time(54) == Time(54))
        self.assertFalse(Time(54) == Time(2))

    def test_add(self):   # musi dzialac porownywanie
        self.assertEqual(Time(1) + Time(2), Time(3))
        self.assertEqual(Time(4) + Time(1), Time(5))
        self.assertEqual(Time(2) + Time(5), Time(7))

    def test_int(self):
        self.assertEqual(int(Time(5632)), 5632)
        self.assertEqual(int(Time(232)), 232)
        self.assertEqual(int(Time(2232)), 2232)


if __name__ == "__main__":
    unittest.main()     # wszystkie testy