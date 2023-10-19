import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Grid con Scrollbar")

# Crear un marco
marco = tk.Frame(ventana)
marco.pack(fill="both", expand=True)

# Crear una barra de desplazamiento vertical
scrollbar = ttk.Scrollbar(marco, orient="vertical")

# Crear una cuadrícula dentro del marco
cuadricula = ttk.Treeview(marco, yscrollcommand=scrollbar.set)

# Define las columnas en base a la cantidad de columnas en tu matriz
columnas = ["Columna 1", "Columna 2"]
cuadricula["columns"] = columnas

for col in columnas:
    cuadricula.heading(col, text=col)

# Configurar la barra de desplazamiento
scrollbar.config(command=cuadricula.yview)

# Agregar los datos del array bidimensional a la cuadrícula
data = [
    ["Dato 1-1", "Dato 1-2"],
    ["Dato 2-1", "Dato 2-2"],
    ["Dato 3-1", "Dato 3-2"],
    # Agrega más filas según tu array
]

# Insertar los datos en la cuadrícula y ajustar el ancho de las columnas automáticamente
for row in data:
    cuadricula.insert("", "end", values=(row[0], row[1]))
    for i, col in enumerate(columnas):
        col_width = tkFont.nametofont("TkDefaultFont").measure(row[i])
        if cuadricula.column(col, option="width") < col_width:
            cuadricula.column(col, width=col_width)

# Empacar la cuadrícula y la barra de desplazamiento en el marco
cuadricula.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Iniciar la aplicación
ventana.mainloop()
