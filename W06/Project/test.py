import tkinter as tk
from tkinter import ttk

# Función para mostrar la selección en una etiqueta
def seleccionar_opcion():
    seleccion = combo.get()
    label.config(text="Opción seleccionada: " + seleccion)

# Función para imprimir la selección en la terminal
def imprimir_seleccion():
    seleccion = combo.get()
    print("Opción seleccionada: " + seleccion)

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de ComboBox")

# Configurar un nuevo estilo para el ComboBox
combostyle = ttk.Style()
combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'BLUE',
                                       'fieldbackground': 'WHITE',
                                       'background': 'CYAN'
                                       }}}
                         )
combostyle.theme_use('combostyle')

# Crear una etiqueta para instrucciones
label = tk.Label(ventana, text="Selecciona una opción:")
label.pack(pady=10)

# Definir opciones, incluyendo una opción muy larga
opciones = ["Opción 1", "Opción 2", "Opción 3", "Opción muy larga que debería ajustar el ancho del ComboBox"]

# Calcular el ancho necesario para acomodar la opción más larga
ancho_maximo = max(map(lambda x: len(x), opciones))

# Crear un ComboBox con las opciones
combo = ttk.Combobox(ventana, values=opciones, state="readonly")
combo.set("Opción 1")  # Establecer la opción predeterminada
combo.config(width=ancho_maximo + 2)  # Establecer el ancho para ajustarse a la opción más larga
combo.pack()

# Crear un botón para mostrar la selección en una etiqueta
boton_mostrar = tk.Button(ventana, text="Mostrar selección", command=seleccionar_opcion)
boton_mostrar.pack()

# Crear un botón para imprimir la selección en la terminal
boton_imprimir = tk.Button(ventana, text="Imprimir selección", command=imprimir_seleccion)
boton_imprimir.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()
