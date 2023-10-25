import tkinter as tk

def es_numero(valor):
    if valor == "":
        return True
    try:
        float(valor)
        return True
    except ValueError:
        return False
root = tk.Tk()

validate_cmd = root.register(es_numero)

entry = tk.Entry(root, validate="key", validatecommand=(validate_cmd, "%P"))
entry.pack()

root.mainloop()