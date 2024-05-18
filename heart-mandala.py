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
    turtle.begin_fill()
    for k in range(600):
        x = hearta(k)
        y = heartb(k)
        turtle.goto(x * 20, y * 20)
    turtle.end_fill()

    # Esconde la tortuga al finalizar el dibujo
    turtle.hideturtle()
    # Mantiene la ventana abierta
    turtle.done()


def hearta(k):
    return 16 * math.sin(k) ** 3


def heartb(k):
    return (
        13 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)
    )


# Llama a la función para dibujar el corazón
draw_heart()
