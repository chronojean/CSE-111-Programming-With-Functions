import tkinter as tk

# Función para validar la entrada de números
def solo_numeros(val):
    try:
        float(val)  # Intenta convertir la entrada en un número de punto flotante
        return True
    except ValueError:
        return False

# Crear la ventana
root = tk.Tk()
root.title("Validación de notas")

# Función para validar la entrada
validacion = root.register(solo_numeros)

# Cuadro de texto para ingresar las notas
t2 = tk.Entry(root, validate="key", validatecommand=(validacion, "%P"))
t2.pack()

# Mostrar la ventana
root.mainloop()
