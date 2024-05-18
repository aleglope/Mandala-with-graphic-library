# Mandalas con Turtle

Este repositorio contiene varios scripts de Python que utilizan el módulo `turtle` para dibujar diferentes formas de mandalas y un corazón. Cada script demuestra el uso de funciones matemáticas y gráficos de tortuga para crear patrones visuales interesantes.

## Requisitos

- Python 3.x
- Módulo `turtle` (incluido en la biblioteca estándar de Python)
- Módulo `math` (incluido en la biblioteca estándar de Python)
- Módulo `colorsys` (incluido en la biblioteca estándar de Python)

## Contenido del Repositorio

### Script 1: Dibujo del Corazón

Este script dibuja un corazón utilizando funciones matemáticas para las coordenadas `x` e `y` y la biblioteca `turtle` para el trazado gráfico.

#### Código

```python
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
```

### Script 2: Dibujo del Corazón Alternativo

Este script dibuja una variación del corazón utilizando diferentes funciones matemáticas.

#### Código

```python
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
```

### Script 3: Dibujo de una Flor

Este script dibuja una flor utilizando colores cambiantes en un bucle.

#### Código

```python
import turtle
import colorsys

def draw_flower():
    # Establece el número de iteraciones y el incremento de color
    iterations = 36
    hue_increment = 1.0 / iterations

    # Configura la velocidad y el fondo
    turtle.speed("fastest")
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
turtle.setup(800, 600)

# Establece el rastreo a un valor deseado para ver la animación
turtle.tracer(1, 25)

# Dibuja la flor
draw_flower()

# Mantiene la ventana abierta hasta que se cierre manualmente
turtle.mainloop()
```

### Script 4: Dibujo de una Mandala

Este script dibuja una mandala utilizando colores cambiantes en un bucle.

#### Código

```python
from turtle import *
import colorsys

# Oculta la tortuga para acelerar el dibujo
hideturtle()
# Establece la velocidad del dibujo al máximo
speed("fastest")
# Establece el color de fondo de la ventana de turtle
bgcolor("black")
# Inicializa la variable 'h' que se utilizará para el tono en la conversión de color HSV a RGB
h = 0

# Inicia un bucle exterior que se repetirá 16 veces
for i in range(16):
    # Inicia un bucle interior que se repetirá 18 veces
    for j in range(18):
        # Convierte el color de HSV a RGB utilizando el tono actual 'h', saturación y brillo máximos (1)
        c = colorsys.hsv_to_rgb(h, 1, 1)
        # Establece el color de la pluma al color RGB calculado
        color(c)
        # Incrementa el valor de 'h' para cambiar el tono en la próxima iteración
        h += 0.005
        # Gira la tortuga 90 grados a la derecha
        right(90)
        # Dibuja un arco de 90 grados con un radio que disminuye con cada iteración de 'j'
        circle(150 - j * 6, 90)
        # Gira la tortuga 90 grados a la izquierda
        left(90)
        # Dibuja otro arco de 90 grados con el mismo radio que antes
        circle(150 - j * 6, 90)
        # Gira la tortuga 180 grados a la derecha
        right(180)
        # Dibuja un pequeño círculo de radio 40 con 24 pasos, dando una forma más poligonal
        circle(40, 24)

# Actualiza la ventana de Turtle con todo lo que se ha dibujado de una sola vez
update()
# Espera un clic del usuario para cerrar la ventana
exitonclick()
```

## Cómo Ejecutar los Scripts

Para ejecutar cualquiera de estos scripts, sigue estos pasos:

1. Guarda el código en un archivo con la extensión `.py` (por ejemplo, `heart.py`, `flower.py`, `mandala.py`).
2. Abre una terminal o línea de comandos.
3. Navega al directorio donde guardaste el archivo.
4. Ejecuta el script con el siguiente comando:

```bash
python nombre_del_script.py
```

Reemplaza `nombre_del_script.py` con el nombre del archivo que deseas ejecutar (por ejemplo, `heart.py`).

## Notas Adicionales

- Puedes personalizar los colores, tamaños y patrones modificando las funciones y los parámetros en los scripts.
- Estos scripts son una excelente manera de aprender sobre gráficos de tortuga y funciones matemáticas en Python.

¡Disfruta creando tus propios mandalas y patrones con `turtle` en Python!