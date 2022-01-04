import fractals


def type_input():
    """Sluzy uzyskaniu od uzytkownika informacji dotyczacej rysowanego ksztaltu"""
    set_of_types = {'d', 's', 'm'} #zbior ksztaltow do wyboru
    f_type = input("Jaki ksztalt chcesz narysowac? \nDo wyboru mamy drzewo, "
                 "sniezynke i muszle. Wybierz d, s lub m :)\n")
    while f_type not in set_of_types:
        f_type = input("Do wyboru masz jedynie d dla drzewa, s dla sniezynki"
                 " i m dla muszli.\n")
    return f_type


def length_input():
    """Sluzy uzyskaniu od uzytkownika informacji dotyczacej wielkosci rysowanego ksztaltu"""
    while True:
        x = input("Jakiej wielkosci w skali od 1 do 10 ma byc ksztalt?\n")
        try:
            size = int(x)
        except ValueError:
            print("To nie jest liczba")
        else:
            if size not in range(1, 11):
                print("Liczba nie jest z odpowiedniego przedzialu")
            else:
                break
    return size


def color1_input():
    """Sluzy uzyskaniu od uzytkownika informacji dotyczacej pierwszego koloru"""
    while True:
        y = input("Bedziemy rysowac dwukolorowy ksztalt, jaki bedzie pierwszy "
                "kolor?\n1 - czerwony\n2 - pomaranczowy\n3 - zolty\n4 - "
                "zielony\n5 - niebieski\n6 - granatowy\n7 - fioletowy\n")
        try:
            color1 = int(y)
        except ValueError:
            print("Powinienes wprowadzic liczbe od 1 do 7.")
        else:
            if color1 not in range(1, 8):
                print("Liczba nie jest z odpowiedniego przedzialu")
            else:
                break
    return color1


def color2_input():
    """Sluzy uzyskaniu od uzytkownika informacji dotyczacej drugiego koloru"""
    while True:
        z = input("Jaki bedzie drugi kolor?\n1 - czerwony\n2 - "
                "pomaranczowy\n3 - zolty\n4 - zielony\n5 - niebieski\n6 "
                "- granatowy\n7 - fioletowy\n")
        try:
            color2 = int(z)
        except ValueError:
            print("Powinienes wprowadzic liczbe od 1 do 7.")
        else:
            if color2 not in range(1, 8):
                print("Liczba nie jest z odpowiedniego przedzialu")
            else:
                break
    return color2

#wywolanie funkcji rysujacej wybrany przez uzytkownika ksztalt
fractals.draw(fractals.set_turtle(), type_input(), length_input(), color1_input(), color2_input())






