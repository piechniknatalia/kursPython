import random
def basic(n):
    randomlist = range(n)
    random.shuffle(randomlist)
    return randomlist
def almost(n):
    a = n // 3
    randomlist = range(n)
    for i in range(a+1):
        randomlist[0 + i * 3: 3 + i * 3] = sorted(randomlist[0 + i * 3: 3 + i * 3], key=lambda x: random.random())
    return randomlist
def almost_r(n):
    randomlist = almost(n)
    randomlist.reverse()
    return randomlist
def gauss(n):
    randomlist = []
    for i in range(n):
        randomlist.append(random.gauss(10, 5))
    return randomlist
def square(n):
    listofsquares = []
    randomlist = []
    i = 1
    while i * i < n:
        listofsquares.append(i*i)
        i += 1
    for i in range(n):
        randomlist.append(random.choice(listofsquares))
    return randomlist

