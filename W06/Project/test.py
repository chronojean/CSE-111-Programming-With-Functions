import tkinter as tk
from tkinter import ttk

def create_grid(data):
    # Crear ventana principal
    root = tk.Tk()
    root.title("Grid con Scrollbar")
    
    # Crear un frame contenedor para la cuadrícula
    frame = ttk.Frame(root)
    frame.pack(fill='both', expand=True)
    
    # Crear un canvas
    canvas = tk.Canvas(frame)
    canvas.pack(side='left', fill='both', expand=True)
    
    # Agregar una barra de desplazamiento vertical
    scrollbar = ttk.Scrollbar(frame, orient='vertical', command=canvas.yview)
    scrollbar.pack(side='right', fill='y')
    
    # Configurar el canvas para que se desplace con la barra de desplazamiento
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    
    # Crear otro frame dentro del canvas para colocar la cuadrícula
    inner_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor='nw')
    
    # Crear la cuadrícula usando labels
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            label = ttk.Label(inner_frame, text=value, width=10, relief='ridge')
            label.grid(row=i, column=j, padx=5, pady=5)
    
    # Configurar el tamaño de la ventana principal
    root.geometry("400x300")
    
    # Ejecutar el bucle principal de la ventana
    root.mainloop()

# Ejemplo de data en una lista bidimensional
data = [
    ["Dato 1", "Dato 2", "Dato 3"],
    ["Dato 4", "Dato 5", "Dato 6"],
    ["Dato 7", "Dato 8", "Dato 9"],
    ["Dato 10", "Dato 11", "Dato 12"],
    ["Dato 13", "Dato 14", "Dato 15"],
    ["Dato 16", "Dato 17", "Dato 18"],
    ["Dato 19", "Dato 20", "Dato 21"],
    # Agrega más filas si es necesario
]

# Llamar a la función para crear la cuadrícula
create_grid(data)