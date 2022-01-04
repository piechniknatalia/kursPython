"""Modul obslugujacy rysowanie ksztaltow za pomoca modulu turtle"""

import math
import turtle

def set_turtle():
    """Funkcja ustawiajaca poczatkowe dane zolwia"""
    turtle.bgcolor("black")
    turtle1 = turtle.Turtle()
    turtle1.hideturtle()
    return turtle1


def tree(color1, color2, turtle, length):
    """Funkcja rysujaca fraktal przypominajacy drzewo"""
    turtle.color(color1)
    angle = 30
    miniumum_length = 5
    if length > miniumum_length:
        turtle.forward(length)
        new_length = length - 5
        turtle.left(angle)
        tree(color1, color2, turtle, new_length)
        turtle.right(2 * angle)
        tree(color2, color1, turtle, new_length)
        turtle.left(angle)
        turtle.color(color1)
        turtle.backward(length)


def snowflake(color1, color2, turtle, iterations, length=300):
    """Funkcja rysujaca fraktal przypominajacy sniezynke"""
    turtle.color(color1)
    if iterations == 0:
        turtle.forward(length)
    else:
        iterations = iterations - 1
        length = length / 3
        snowflake(color1, color2, turtle, iterations, length)
        turtle.left(60)
        snowflake(color2, color1, turtle, iterations, length)
        turtle.right(60 * 2)
        snowflake(color1, color2, turtle, iterations, length)
        turtle.left(60)
        snowflake(color2, color1, turtle, iterations, length)


def fiboshell(color1, color2, turtle, n):
    """Funkcja rysujaca ksztalt przypominajacy spirale """
    a = 0
    b = 1
    for i in range(n):
        if i % 2 == 0:
            turtle.color(color1)
        else:
            turtle.color(color2)
        curve = math.pi * b * 3 / 2 #mnozymy razy 3, zeby zwiekszyc skale
        curve = curve / 90
        for j in range(90):
            turtle.forward(curve)
            turtle.left(1)
        temp = a
        a = b
        b = temp + b


def draw(turtle, type, size, color1, color2):
    """Funkcja rysujaca ksztalty w zaleznosci od podanych danych"""
    # zbior kolorow do wyboru
    set_of_colors = {'1': 'brown1',
                     '2': 'chocolate1',
                     '3': 'DarkGoldenrod2',
                     '4': 'DarkOliveGreen3',
                     '5': 'CadetBlue',
                     '6': 'blue2',
                     '7': 'BlueViolet'
                     }
    turtle_color1 = set_of_colors[str(color1)]
    turtle_color2 = set_of_colors[str(color2)]
    if type == 'd':
        length = 20 + (size - 1) * 3
        turtle.setheading(90)
        tree(turtle_color1, turtle_color2, turtle, length)
    elif type == 's':
        size = round(1 + (size - 1) * 0.3)
        turtle.up()
        turtle.left(180)
        turtle.forward(300 / 2)
        turtle.right(180)
        turtle.down()
        for i in range(3):
            snowflake(turtle_color1, turtle_color2, turtle, size, 300)
            turtle.right(120)
    elif type == 'm':
        length = round(1 + (size - 1) * 1.2)
        fiboshell(turtle_color1, turtle_color2, turtle, length)
    input("Kliknij enter kiedy bedziesz chcial wylaczyc ekran")