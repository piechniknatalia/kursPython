class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):   # podglqdanie kolejki
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):   # nigdy nie jest pusta
        return False

    def put(self, data):
        self.items.append(data)

    def get(self):
        if self.is_empty():
            raise Exception('Kolejka jest pusta')
        return self.items.pop(0)   # malo wydajne!

import unittest

class TestStack(unittest.TestCase):


    def test_init(self):
        q1 = Queue()
        self.assertEqual(1, q1.is_empty())

    def test_str(self):
        q1 = Queue()
        q1.put(5)
        self.assertEqual('[5]', str(q1))

    def test_empty(self):
        q1 = Queue()
        self.assertTrue(q1.is_empty())
        q1.put(1)
        self.assertFalse(q1.is_empty())

    def test_full(self):
        q1 = Queue()
        self.assertFalse(q1.is_full())

    def test_put(self):
        q1 = Queue()
        self.assertEqual('[]', str(q1))
        q1.put(5)
        self.assertEqual('[5]', str(q1))

    def test_get(self):
        q1 = Queue()
        q1.put(5)
        self.assertEqual('[5]', str(q1))
        q1.get()
        self.assertEqual('[]', str(q1))

    def test_exception(self):
        q1 = Queue()
        with self.assertRaises(Exception) as context:
            q1.get()
        self.assertTrue('Kolejka jest pusta' in context.exception)




if __name__ == "__main__":
    unittest.main()  # wszystkie testy