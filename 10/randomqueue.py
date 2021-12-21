import random
class RandomQueue:

    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def remove(self):   # zwraca losowy element
        r = random.randint(0, len(self.items))
        self.items = self.items[0:r] + self.items[(r+1):]
        return r

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False

    def clear(self):     # czyszczenie listy
        del self.items[:]
