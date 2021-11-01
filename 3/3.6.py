while True:
    x = input("Wysokosc:")
    try:
        number1 = int(x)
    except ValueError:
        print("To nie jest liczba!")
    else:
        if number1 > 15:
            print("Liczba jest za duza")
        else:
            break
while True:
    y = input("Szerokosc:")
    try:
        number2 = int(y)
    except ValueError:
        print("To nie jest liczba!")
    else:
        if number2 > 15:
            print("Liczba jest za duza")
        else:
            break
s =''
for i in range(number1):
    for j in range(number2):
        s+="+---"
    s+="+\n"
    for j in range(number2):
        s+="|   "
    s+="|\n"
for k in range(number2):
    s+="+---"
s+="+"
print(s)



