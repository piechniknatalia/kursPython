# Modul z fraktalami

import math

def tree(color1, color2, t, length):
    angle = 30
    length_change = 5
    miniumum_length = 5
    if length > miniumum_length:
        t.color(color1)
        t.forward(length)
        new_length = length - length_change

        t.left(angle)
        tree(color1, t, new_length)

        t.right(2 * angle)
        tree(color2, t, new_length)

        t.left(angle)
        t.color(color1)
        t.backward(length)

def snowflake(color1, color2, turtle, iterations, length):
    turtle.color(color1)
    if iterations == 0:
        turtle.forward(length)
    else:
        iterations = iterations - 1
        length = length / 3
        snowflake(color1, turtle, iterations, length)
        turtle.left(60)
        snowflake(color2, turtle, iterations, length)
        turtle.right(60 * 2)
        snowflake(color1, turtle, iterations, length)
        turtle.left(60)
        snowflake(color2, turtle, iterations, length)




def fiboshell(color1, color2, turtle, n):
    factor = 3
    a = 0
    b = 1
    for i in range(n):
        if i % 2 == 0:
            turtle.color(color1)
        else:
            turtle.color(color2)
        curve = math.pi * b * factor / 2
        curve = curve / 90
        for j in range(90):
            turtle.forward(curve)
            turtle.left(1)
        temp = a
        a = b
        b = temp + b
