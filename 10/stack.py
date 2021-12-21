class Stack:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False

    def push(self, item):
        if self.is_full():
            raise Exception('Stos jest przepelniony')
        self.items.append(item)         # dodajemy na koniec

    def pop(self):                      # zwraca element
        if self.is_empty():
            raise Exception('Stos jest pusty')
        return self.items.pop()         

import unittest

class TestStack(unittest.TestCase):


    def test_init(self):
        s1 = Stack()
        self.assertEqual(1, s1.is_empty())

    def test_str(self):
        s1 = Stack()
        s1.push(5)
        s1.push(4)
        self.assertEqual('[5, 4]', str(s1))

    def test_empty(self):
        s1 = Stack()
        self.assertTrue(s1.is_empty())
        s1.push(1)
        self.assertFalse(s1.is_empty())

    def test_full(self):
        s1 = Stack()
        self.assertFalse(s1.is_full())

    def test_push(self):
        s1 = Stack()
        self.assertEqual('[]', str(s1))
        s1.push(5)
        self.assertEqual('[5]', str(s1))

    def test_pop(self):
        s1 = Stack()
        s1.push(5)
        self.assertEqual('[5]', str(s1))
        s1.pop()
        self.assertEqual('[]', str(s1))
        self.assertEqual('[]', str(s1))

    def test_exception(self):
        s1 = Stack()
        with self.assertRaises(Exception) as context:
            s1.pop()
        self.assertTrue('Stos jest pusty' in context.exception)




if __name__ == "__main__":
    unittest.main()  # wszystkie testy