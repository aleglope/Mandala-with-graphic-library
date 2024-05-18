from turtle import *
import colorsys

# Configura la velocidad de la animación a un nivel más lento para ver el proceso de creación
# This Python code is using the Turtle graphics library to create an animated pattern. Here's a
# breakdown of what the code is doing:
speed(3)
bgcolor("black")
tracer(8)  # Ajusta este número para ralentizar aún más la animación
h = 0

# Dibuja el patrón, luego borra el último trazo antes de hacer el siguiente
for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.005
        right(90)
        circle(150 - j * 6, 90)
        left(90)
        circle(150 - j * 6, 90)
        right(180)
        circle(40, 24)
        update()  # Actualiza la pantalla después de dibujar cada figura
        if (
            j < 17
        ):  # Si no es el último trazo, borra este trazo antes de dibujar el siguiente
            undo()  # Esto deshará el último trazo del dibujo

done()  # finaliza
