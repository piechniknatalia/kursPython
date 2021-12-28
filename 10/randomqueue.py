import random
class RandomQueue:

    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def remove(self):   # zwraca losowy element
        r = random.randint(0, len(self.items))
        a = self.items[r]
        self.items[r] = self.items[-1]
        self.items.pop()
        return a

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False

    def clear(self):     # czyszczenie listy
        del self.items[:]
