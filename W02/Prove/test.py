from PIL import Image, ImageTk
import tkinter as tk

# Cargar la imagen
imagen = Image.open("my_image.jpg")

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
        # Obtener el valor del píxel en formato RGB
        r, g, b = imagen.getpixel((x, y))
        
        # Convertir los valores RGB a color hexadecimal
        color = "#%02x%02x%02x" % (r, g, b)
        
        # Pintar el píxel en el canvas
        canvas.create_rectangle(x, y, x+1, y+1, fill=color, outline="")
        
# Mostrar la ventana
ventana.mainloop()