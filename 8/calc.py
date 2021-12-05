
import random
import math
def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    num_inside = 0
    for i in range(n):
        x = random.random()*2-1
        y = random.random()*2-1
        if math.sqrt(x * x + y * y) <= 1:
            num_inside+=1
    return 4*num_inside/n

print(calc_pi(1000))
print(calc_pi(10000))
print(calc_pi(100000))
print(calc_pi(1000000))
print(calc_pi())
print(calc_pi(10))





