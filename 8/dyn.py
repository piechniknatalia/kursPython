
P = {(0, 0):0.5, (1, 0):0.0, (0, 1):1.0}   # globalny słownik

def p(x, y):
    if x < 0 or y < 0:
        raise ValueError("x i y musza byc dodatnie")
    global P
    if (x, y) not in P:
        if y == 0:
            P[(x, y)] = 0.0
        elif x == 0:
            P[(x, y)] = 1.0
        else:
            P[(x, y)] = 0.5 * (p(x-1, y) + p(x, y-1))
    return P[(x, y)]

print(p(1, 1))
