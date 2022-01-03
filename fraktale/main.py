import fractals

#zbior fraktali do wyboru
set_of_types = {'d', 's', 'm'}

type = input("Jaki fraktal chcesz narysowac? Do wyboru mamy drzewo, sniezynke i muszle.\nWybierz d, s lub m :)\n")
while type not in set_of_types:
    type = input("Do wyboru masz jedynie d dla drzewa, s dla sniezynki i m dla muszli.\n")

while True:
    x = input("Jakiej wielkosci w skali od 1 do 10 ma byc fraktal?\n")
    try:
        size = int(x)
    except ValueError:
        print("To nie jest liczba")
    else:
        if size not in range(1, 11):
            print("Liczba nie jest z odpowiedniego przedzialu")
        else:
            break
while True:
    y = input("Bedziemy rysowac dwukolorowy fraktal, jaki bedzie pierwszy kolor?"
               "\n1 - czerwony\n2 - pomaranczowy\n3 - zolty\n4 - zielony\n"
               "5 - niebieski\n6 - granatowy\n7 - fioletowy\n")
    try:
        color1 = int(y)
    except ValueError:
        print("Powinienes wprowadzic liczbe od 1 do 7.")
    else:
        if color1 not in range(1, 8):
            print("Liczba nie jest z odpowiedniego przedzialu")
        else:
            break
while True:
    z = input("Jaki bedzie drugi kolor fraktala?"
               "\n1 - czerwony\n2 - pomaranczowy\n3 - zolty\n4 - zielony\n"
               "5 - niebieski\n6 - granatowy\n7 - fioletowy\n")
    try:
        color2 = int(z)
    except ValueError:
        print("Powinienes wprowadzic liczbe od 1 do 7.")
    else:
        if color2 not in range(1, 8):
            print("Liczba nie jest z odpowiedniego przedzialu")
        else:
            break


fractals.draw(fractals.set_turtle, type, size, color1, color2)






