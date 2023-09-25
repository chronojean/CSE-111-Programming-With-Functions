from PIL import Image, ImageTk
import tkinter as tk

def draw_image():
    # Cargar la imagen
    imagen = Image.open("birds_alpha.png")

    # Convertir la imagen a mapa de bits
    imagen = imagen.convert("1")

    # Obtener las dimensiones de la imagen
    ancho, alto = imagen.size

    # Crear una ventana
    ventana = tk.Tk()

    # Crear un canvas del tamaño de la imagen
    canvas = tk.Canvas(ventana, width=ancho, height=alto)
    canvas.pack()

    # Pintar pixel por pixel en el canvas
    for y in range(alto):
        for x in range(ancho):
            # Obtener el valor del píxel
            pixel = imagen.getpixel((x, y))

            # Determinar el color a utilizar en el canvas
            color = "#FFFFFF" if pixel == 0 else None

            # Pintar el píxel en el canvas
            canvas.create_rectangle(x, y, x+1, y+1, fill=color, outline="")

    # Mostrar la ventana
    ventana.mainloop()

# Llamar a la función draw_image desde tu función main
def main():
    # Resto del código
    
    draw_image()

# Llamar a la función main para ejecutar el programa
main()