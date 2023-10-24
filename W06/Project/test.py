import tkinter as tk
from tkinter import ttk

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def create_all_widgets(ventana):
    # Aquí debes agregar el código para crear todos los widgets de tu ventana
    pass

def main():
    ventana = tk.Tk()
    ventana.title("My finances")
    s = ttk.Style(ventana)
    s.theme_use('clam')
    s.configure('TCombobox', arrowsize=26)
    s.configure('DateEntry', arrowsize=26)
    
    create_all_widgets(ventana)

    # Centrar la ventana en la pantalla
    center_window(ventana)

    ventana.mainloop()

main()