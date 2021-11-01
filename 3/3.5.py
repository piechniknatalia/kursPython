while True:
    x = input("Wpisz liczbe:")
    try:
        number = int(x)
    except ValueError:
        print("To nie jest liczba!")
    else:
        if number > 15:
            print("Liczba jest za duza")
        else:
            break
s =''
for i in range(number):
    s+=("|....")
s+=("|\n")
for i in range(number+1):
    if i < 9:
        s+=(str(i)+"    ")
    else:
        s+=(str(i)+"   ")
print(s)
