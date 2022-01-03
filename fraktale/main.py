import turtle
import fractals
LENGTH = 30 #zmieniane przez uzytkownika (20 - 50 tree) (1-12 muszla)
ITERATIONS = 3 # tylko do sniezynki

set_of_types = {'d', 's', 'm'}
type = input("Jaki fraktal chcesz narysowac? Do wyboru mamy drzewo, sniezynke i muszle. Wybierz d, s lub m :)\n")
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

set_of_colors = {'czerwony': 'brown1',
                 'pomaranczowy': 'chocolate1',
                 'zolty': 'DarkGoldenrod2',
                 'zielony':'DarkOliveGreen3',
                 'niebieski' :'CadetBlue',
                 'granatowy' : 'blue2',
                 'fioletowy':'BlueViolet'}

while True:
    x = input("Bedziemy rysowac dwukolorowy fraktal, jaki bedzie pierwszy kolor"
               "\n1 - czerwony\n2 - pomaranczowy\n3 - zolty\n4 - zielony\n"
               "5 - niebieski\n6 - granatowy\n7 - fioletowy\n")
    try:
        color1 = int(x)
    except ValueError:
        print("Powinienes wprowadzic liczbe od 1 do 7.")
    else:
        if color1 not in range(1, 8):
            print("Liczba nie jest z odpowiedniego przedzialu")
        else:
            break
while True:
    x = input("Jaki bedzie drugi kolor fraktala"
               "\n1 - czerwony\n2 - pomaranczowy\n3 - zolty\n4 - zielony\n"
               "5 - niebieski\n6 - granatowy\n7 - fioletowy\n")
    try:
        color2 = int(x)
    except ValueError:
        print("Powinienes wprowadzic liczbe od 1 do 7.")
    else:
        if color2 not in range(1, 8):
            print("Liczba nie jest z odpowiedniego przedzialu")
        else:
            break

turtle.bgcolor("black")
turtle.pensize(800) # moze zmienic jeszcze
turtle1 = turtle.Turtle()
turtle1.hideturtle()
turtle1.color(color1)

if type == 'd':
    length = 20 + (size-1) * 3
    turtle1.setheading(90)
    fractals.tree(color1, color2, turtle1, length)

elif type == 's':
    length = round(1 + (size - 1) * 0.5)
    turtle1.up()
    turtle1.forward(LENGTH/2)
    turtle1.left(180)
    turtle1.down()
    turtle.right(90)
    for i in range(3):
        fractals.snowflake(color1, color2, turtle1, length, 300)
        turtle1.right(120)

elif type == 'm':
    length = round(1 + (size - 1) * 1.2)
    fractals.fiboshell(color1, color2, turtle1, length)

turtle1.mainloop()





#LENGTH = 300 dla śnieżynki












#fiboshell(turtle1, 12)

#SNOW
#turtle1.up()
#turtle1.forward(LENGTH/2)
#turtle1.left(180)
#turtle1.down()
#turtle.right(90)
#for i in range(3):
#    snowflake(COLOR2, turtle1, ITERATIONS, LENGTH)
#    turtle1.right(120)

#


