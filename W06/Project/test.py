import tkinter as tk

def create_modal_window():
    modal_window = tk.Toplevel()
    modal_window.attributes('-topmost', True)
    modal_window.geometry('200x100+1000+700')
    modal_window.overrideredirect(True)
    label = tk.Label(modal_window, text="Ventana modal")
    label.pack()

    # Función para cerrar la ventana modal al hacer clic
    def close_modal_window(event):
        modal_window.destroy()

    # Configurar el enlace de clic para cerrar la ventana modal
    label.bind("<Button-1>", close_modal_window)

    # Programar el cierre automático después de 3 segundos
    modal_window.after(3000, lambda: close_modal_window(None))

root = tk.Tk()
button = tk.Button(root, text="Abrir ventana modal", command=create_modal_window)
button.pack()

root.mainloop()
