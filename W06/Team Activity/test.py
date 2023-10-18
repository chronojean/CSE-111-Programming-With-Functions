import tkinter as tk

# Crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Inputs y Labels")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Introduce tu nombre:")
etiqueta.pack()

# Crear una entrada de texto
entrada = tk.Entry(ventana)
entrada.pack()

# Función para mostrar el nombre ingresado
def mostrar_nombre():
    nombre = entrada.get()
    etiqueta_salida.config(text=f"Hola, {nombre}!")

# Crear un botón
boton = tk.Button(ventana, text="Saludar", command=mostrar_nombre)
boton.pack()

# Etiqueta de salida
etiqueta_salida = tk.Label(ventana, text="")
etiqueta_salida.pack()

# Iniciar la aplicación
ventana.mainloop()
