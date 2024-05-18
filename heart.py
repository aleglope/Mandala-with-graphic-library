import turtle
import math

"""
The Python code uses the turtle module to draw a heart shape by plotting mathematical functions for
x and y coordinates.
"""


def draw_heart():
    """Dibuja un corazón utilizando el módulo turtle."""
    # Establece la velocidad del dibujo al máximo
    turtle.speed("fastest")
    # Establece el color de fondo
    turtle.bgcolor("black")
    # Establece el color del lápiz
    turtle.color("red")

    # Comienza el dibujo del corazón
    turtle.penup()
    turtle.goto(0, -200)  # Ajusta la posición inicial
    turtle.pendown()

    turtle.begin_fill()
    for k in range(0, 360):
        x = heart_x(k)
        y = heart_y(k)
        turtle.goto(x * 20, y * 20)
    turtle.end_fill()

    # Esconde la tortuga al finalizar el dibujo
    turtle.hideturtle()
    # Mantiene la ventana abierta
    turtle.done()


def heart_x(t):
    """Función que define la coordenada x del corazón"""
    return 16 * math.sin(math.radians(t)) ** 3


def heart_y(t):
    """Función que define la coordenada y del corazón"""
    return (
        13 * math.cos(math.radians(t))
        - 5 * math.cos(math.radians(2 * t))
        - 2 * math.cos(math.radians(3 * t))
        - math.cos(math.radians(4 * t))
    )


# Llama a la función para dibujar el corazón
draw_heart()
