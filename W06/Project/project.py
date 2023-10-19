import tkinter as tk
from tkinter import Frame, Label, Button,ttk,Entry
from number_entry import IntEntry
import sys

frame_background="brown"
lbl_item_color = "WHITE"
lbl_item_font = ("Calibri",12)
lbl_item_padx=1

def load_history(filename):
    try:
        arr = []
        with open(filename, 'r+') as archivo:
            for linea in archivo:
                #print(linea.strip("\n"))
                row = linea.strip("\n").split(", ")
                for i in range(len(row)):
                    try:
                        row[i]=round(float(row[i]))
                    except:
                        None
                arr.append(row)
        return arr
    except (FileNotFoundError,PermissionError):
        print("Couldn't open the history file")
        sys.exit(0) 
def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
def create_form(frame):
    def imprimir_seleccion():
        seleccion = combo.get()
        print("Opción seleccionada: " + seleccion)
        
    frame_save_income_outcome = Frame(frame, relief="flat", borderwidth=1,background=frame_background)
    frame_save_income_outcome.pack(padx=0, pady=2, fill=tk.BOTH, expand=1)

    # Crear un Frame adicional para organizar los elementos en la misma fila
    frame_row = Frame(frame_save_income_outcome,relief="flat")
    frame_row.pack()

    lbl_save_income_outcome = Label(frame_row, text="Amount: ",background=frame_background,fg=lbl_item_color,font=lbl_item_font,relief="flat")
    lbl_save_income_outcome.pack(side="left")  # Alinea la etiqueta a la izquierda

    entry_amount = Entry(frame_row, width=12)
    entry_amount.pack(side="left")  # Alinea la caja de texto a la izquierda

    # lbl_of = Label(frame_row, text=" of ",fg=lbl_item_color,font=lbl_item_font,relief="flat")
    # lbl_of.pack(side="left")  # Alinea la etiqueta "of" a la izquierda

    # Definir opciones para el ComboBox
    opciones = ["Income", "Outcome"]

    # Calcular el ancho necesario para acomodar la opción más larga
    ancho_maximo = max(map(lambda x: len(x), opciones))
    # Configurar un nuevo estilo para el ComboBox
    combostyle = ttk.Style()
    combostyle.theme_create('combostyle', parent='alt',
                            settings = {'TCombobox':
                                        {'configure':
                                        {'selectbackground': 'BLACK',
                                         'selectedforeground': 'RED',
                                        'fieldbackground': 'WHITE',
                                        'background': 'BROWN1'
                                        }}}
                            )
    combostyle.theme_use('combostyle')
    # Crear un ComboBox con las opciones
    combo = ttk.Combobox(frame_row, values=opciones, state="readonly")
    combo.set(opciones[0])  # Establecer la opción predeterminada
    combo.config(width=ancho_maximo + 2)  # Establecer el ancho para ajustarse a la opción más larga
    combo.pack(side="left")  # Alinea el ComboBox a la izquierda

    # Crear un botón para imprimir la selección en la terminal
    boton_imprimir = tk.Button(frame_save_income_outcome, text="Imprimir selección", command=imprimir_seleccion)
    boton_imprimir.pack(side="left")  # Alinea el botón a la izquierda
    



def create_grid(frame,data):    
    # Recorrer los datos y mostrarlos en una cuadrícula en el marco
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            if j==2 and es_numero(item) and float(item)>0:
                label = Label(frame, text=f'{item:,}', anchor="e",justify="left",bg=lbl_item_color,font=lbl_item_font)
                label.grid(row=i, column=j, padx=lbl_item_padx, pady=0, sticky="nsew")
                label = Label(frame, text="", anchor="e",justify="left",background=lbl_item_color,font=lbl_item_font)
                label.grid(row=i, column=j+1, padx=lbl_item_padx, pady=0, sticky="nsew")
            elif j==2 and es_numero(item) and not float(item)>0:
                label = Label(frame, text="", anchor="e",justify="left",background=lbl_item_color,font=lbl_item_font)
                label.grid(row=i, column=j, padx=lbl_item_padx, pady=0, sticky="nsew")
                label = Label(frame, text=f'{item:,}', anchor="e",justify="left",background=lbl_item_color,font=lbl_item_font)
                label.grid(row=i, column=j+1, padx=lbl_item_padx, pady=0, sticky="nsew")
            else:
                label = Label(frame, text=item, anchor="e",justify="left",background=lbl_item_color,font=lbl_item_font)
                label.grid(row=i, column=j, padx=lbl_item_padx, pady=0, sticky="nsew")
    label = Label(frame,text="Current Money: ",background=frame_background,fg="White",relief="sunken")
    label.grid(row=i+1,columnspan=2,sticky="nsew")
    label = Label(frame,text=f'{sum([row[2] for row in data]):,}',background=frame_background,fg="White",relief="sunken")
    label.grid(row=i+1,column=2,columnspan=2,sticky="nsew")
            

    # Configurar las filas y columnas para expandirse con el marco
    for i in range(len(data)):
        frame.grid_rowconfigure(i, weight=1)
    for j in range(len(data[0])):
        frame.grid_columnconfigure(j, weight=1)
        
def main():
    # Crear una ventana
    ventana = tk.Tk()
    #ventana.geometry("1024x768")
    #Gets history from file and stores it into an array
    history = load_history("history.txt")

    #Create a frame inside ventana, this frame will contain most of the widgets
    body = Frame(ventana, background=frame_background,relief=tk.RAISED,borderwidth=1)
    body.master.title("My Finances")
    body.pack(padx=0, pady=2, fill=tk.BOTH, expand=1)

    #Create the structure of the frame
    create_form(body)
    #create_grid(body,history)

    ventana.mainloop()

if __name__ == "__main__":
    main()
