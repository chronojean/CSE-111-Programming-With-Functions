import tkinter as tk

def create_modal_window():
    modal_window = tk.Toplevel()
    modal_window.attributes('-topmost', True)
    modal_window.geometry('200x100+1000+700')  # Ajusta las dimensiones y la posición
    modal_window.overrideredirect(True)  # Quita la decoración de ventana
    label = tk.Label(modal_window, text="Ventana modal")
    label.pack()

root = tk.Tk()
button = tk.Button(root, text="Abrir ventana modal", command=create_modal_window)
button.pack()

root.mainloop()
