while True:
    x = input("Wpisz liczbe:")
    if x == "stop":
        break
    try:
        number = float(x)
    except ValueError:
        print ( "To nie jest liczba!" )
    else:
        print ( (number, pow(number,3)) )