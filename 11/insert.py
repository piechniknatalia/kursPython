import rand

def cmp(a, b):
    return (a > b) - (a < b)


def insertsort(L, left, right, cmpfunc=cmp):
    for i in range(left+1, right+1):
        for j in range(i, left, -1):
            if cmpfunc(L[j-1], L[j]) > 0:
                L[j-1], L[j] = L[j], L[j-1]
    return L

import unittest

class TestSort(unittest.TestCase):

    def insert_test(self):
        self.assertEqual(insertsort(rand.basic(10), 0, 9, cmp), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(insertsort(rand.basic(5), 0, 4, cmp), [0, 1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()     # wszystkie testy
