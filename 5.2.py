import fractions

def skracanie(frac):
    a = fractions.gcd(frac[0], frac[1])
    if frac[0] == 0:
        return [0, 0]
    else:
        return [frac[0]/a, frac[1]/a]

def add_frac(frac1, frac2):
    if frac1[1] != frac2[1]:
        return skracanie([frac1[0]*frac2[1]+frac2[0]*frac1[1], frac1[1]*frac2[1]])

    else:
        return[frac1[0]+frac2[0], frac1[0]]


def sub_frac(frac1, frac2):
    if frac1[1] != frac2[1]:
        return skracanie([frac1[0]*frac2[1]-frac2[0]*frac1[1], frac1[1]*frac2[1]])
    else:
        return skracanie([frac1[0]-frac2[0], frac1[0]])


def mul_frac(frac1, frac2):
    return skracanie([frac1[0]*frac2[0], frac1[1]*frac2[1]])


def div_frac(frac1, frac2):
    return skracanie([frac1[0]*frac2[1], frac1[1]*frac2[0]])


def is_positive(frac):
    return frac[0]*frac[1] > 0


def is_zero(frac):
    return frac[0] == 0


def cmp_frac(frac1, frac2):
    a = skracanie([frac1[0], frac1[1]])
    b = skracanie([frac2[0], frac2[1]])
    if a[0] == 0 and b[0] == 0:
        return 0
    elif a[0]/a[1] > b[0]/b[1]:
        return -1
    elif a[0] == b[0] and a[1] == b[1]:
        return 0
    else:
        return 1


def frac2float(frac):
    return float(frac[0])/float(frac[1])


f1 = [-1, 2]                  # -1/2
f2 = [0, 1]                   # zero
f3 = [3, 1]                   # 3
f4 = [6, 2]                   # 3 (niejednoznacznosc)
f5 = [0, 2]                   # zero (niejednoznacznosc)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([-1, 2], [1, 3]), [-1, 6])
    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
    def test_add_frac(self):
        self.assertEqual(add_frac([-1, -2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [0, 3]), [0, 0])
    def test_sub_frac(self):
        self.assertEqual(sub_frac([-1, 2], [1, 3]), [-4, 6])
    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [-1, -3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([2, 3], [4, 3]), [8, 9])
    def test_mul_frac(self):
        self.assertEqual(mul_frac([-2, 3], [4, 3]), [-8, 9])
    def test_mul_frac(self):
        self.assertEqual(mul_frac([2, 3], [0, 0]), [0, 0])

    def test_div_frac(self):
        self.assertEqual(div_frac([2, 3], [4, 3]), [1, 2])
    def test_div_frac(self):
        self.assertEqual(div_frac([2, 3], [0, 0]), [1, 2])
    def test_div_frac(self):
        self.assertEqual(div_frac([2, 3], [4, 3]), [1, 2])

    def test_is_positive(self):
        self.assertTrue(is_positive([2, 3]), True)
    def test_is_positive(self):
        self.assertFalse(is_positive([0, 3]), False)
    def test_is_positive(self):
        self.assertFalse(is_positive([-1, 3]), False)

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 3]), True)
    def test_is_zero(self):
        self.assertFalse(is_zero([1, 3]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([3, 4], [4, 4]), 1)
    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([0, 4], [0, 3]), 0)

    def test_frac2float(self):

        self.assertAlmostEqual(frac2float([3, 4]), 0.75, places=4)
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
