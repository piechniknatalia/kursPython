def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0:
        if b == 0:
            if c == 0:
                return("Rownanie ma nieskonczenie wiele rozwiazan.")
            else:
                return("Rownanie nie ma rozwiazan")
        else:
            if c == 0:
                return("Rownanie ma nieskonczenie wiele rozwiazan postaci (x, 0), gdzie x jest liczba rzeczywista")
            else:
                return("Rownanie ma nieskonczenie wiele rozwizan postaci (x, {}), gdzie y jest liczba rzeczywista".format(-c/b))
    else:
        if b == 0:
            if c == 0:
                return("Rownanie ma nieskonczenie wiele rozwiazan postaci (0, y), gdzie y jest liczba rzeczywista")
            else:
                return("Rownanie ma nieskonczenie wiele rozwizan postaci ({}, y), gdzie y jest liczba rzeczywista".format(-c/a))
        else:
            if c == 0:
                return("Rownanie ma nieskonczenie wiele rozwiazan postaci (x, {}x), gdzie x jest liczba rzeczywista". format(-a/b))
            else:
                return("Rownanie ma nieskonczenie wiele rozwiazan postaci (x, {}+{}x), gdzie x jest liczba rzeczywista".format(-c/b, -a/b))

print(solve1(1, 2, 3))
print(solve1(0, 0, 0))
print(solve1(0, 0, -2))





