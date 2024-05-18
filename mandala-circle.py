import turtle
import colorsys


def draw_flower():
    # Establece el número de iteraciones y el incremento de color
    iterations = 36
    hue_increment = 1.0 / iterations

    # Configura la velocidad y el fondo
    turtle.speed(
        "fastest"
    )  # 'fastest': 0, sin animación; 'slow': 3, 'slower': 6, 'slowest': 10
    turtle.bgcolor("black")

    hue = 0
    for i in range(iterations):
        # Calcula el color actual
        col = colorsys.hsv_to_rgb(hue, 1, 1)
        turtle.color(col)

        # Dibuja un círculo y rota
        turtle.circle(100)
        turtle.left(10)

        # Incrementa el tono para el siguiente color
        hue += hue_increment

        # Actualiza la pantalla después de cada iteración para ver la animación
        turtle.update()


# Prepara la ventana
turtle.setup(800, 600)  # Puede ajustar al tamaño de ventana que prefiera

# Establece el rastreo a un valor deseado para ver la animación
turtle.tracer(
    1, 25
)  # El segundo argumento es el delay de la actualización en milisegundos

# Dibuja la flor
draw_flower()

# Mantiene la ventana abierta hasta que se cierre manualmente
turtle.mainloop()
