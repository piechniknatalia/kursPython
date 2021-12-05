import math
def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Boki nie spelniaja warunku trojkata")
    p = 1/2*(a + b + c)
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
print(heron(3, 4, 5))