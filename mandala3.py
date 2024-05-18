# Importa todas las funciones del módulo turtle
from turtle import *

# Importa el módulo colorsys para trabajar con conversiones de color
import colorsys

# Establece la velocidad del dibujo al máximo
speed(0)
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
        rt(90)
        # Dibuja un arco de 90 grados con un radio que disminuye con cada iteración de 'j'
        circle(150 - j * 6, 90)
        # Gira la tortuga 90 grados a la izquierda
        lt(90)
        # Dibuja otro arco de 90 grados con el mismo radio que antes
        circle(150 - j * 6, 90)
        # Gira la tortuga 180 grados a la derecha
        rt(180)
        # Dibuja un pequeño círculo de radio 40 con 24 pasos, dando una forma más poligonal
        circle(40, 24)
# Finaliza el dibujo y mantiene abierta la ventana de turtle hasta que se cierre manualmente
done()
