import tkinter as tk
from tkinter import Frame, Label, Button,ttk,Entry
from number_entry import IntEntry
import sys

frame_background="#002400"
lbl_bg_color = "darkolivegreen"
lbl_font_color = "WHITE"
btn_bg_color = "BLACK" 
lbl_item_font = ("Calibri",14)
lbl_opt_font = ("Calibri",12)
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

def create_grid(frame,data):    
    # Recorrer los datos y mostrarlos en una cuadrícula en el marco
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            if j==2 and es_numero(item) and float(item)>0:
                label = Label(frame, text=f'{item:,}', anchor="e",justify="left",background=lbl_bg_color,font=lbl_item_font,fg=lbl_font_color)
                label.grid(row=i, column=j, padx=lbl_item_padx, pady=0, sticky="nsew")
                label = Label(frame, text="", anchor="e",justify="left",background=lbl_bg_color,font=lbl_item_font,fg=lbl_font_color)
                label.grid(row=i, column=j+1, padx=lbl_item_padx, pady=0, sticky="nsew")
            elif j==2 and es_numero(item) and not float(item)>0:
                label = Label(frame, text="", anchor="e",justify="left",background=lbl_bg_color,font=lbl_item_font,fg=lbl_font_color)
                label.grid(row=i, column=j, padx=lbl_item_padx, pady=0, sticky="nsew")
                label = Label(frame, text=f'{item:,}', anchor="e",justify="left",background=lbl_bg_color,font=lbl_item_font,fg=lbl_font_color)
                label.grid(row=i, column=j+1, padx=lbl_item_padx, pady=0, sticky="nsew")
            else:
                label = Label(frame, text=item, anchor="e",justify="left",background=lbl_bg_color,font=lbl_item_font,fg=lbl_font_color)
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

def create_form(ventana):
    def append_to_file():
        print(income_outcome.get())
    lbl_amount = Label(ventana, text="Amount: ",background=frame_background,fg=lbl_font_color,font=lbl_opt_font)
    entry_amount = Entry(ventana,width=12)
    lbl_of = Label(ventana, text=" of ",background=frame_background,fg=lbl_font_color,font=lbl_opt_font)
    income_outcome = ttk.Combobox(ventana, values=["Income", "Outcome"],font=lbl_opt_font,state="readonly")  # Agrega un Combobox con opciones
    income_outcome["width"] = max(len(option) for option in income_outcome["values"])+2  # Ajusta el ancho al más largo
    income_outcome.set("Income")  # Establece "Income" como valor predeterminado
    btn_save_income_outcome = Button(ventana, text="Save",relief="solid",background=btn_bg_color,fg=lbl_font_color,font=lbl_opt_font,command=append_to_file)
    
    lbl_amount.pack(side=tk.LEFT)
    entry_amount.pack(side=tk.LEFT)
    lbl_of.pack(side=tk.LEFT)
    income_outcome.pack(side=tk.LEFT)  # Agrega el Combobox antes del botón
    btn_save_income_outcome.pack(side=tk.LEFT)
   
def main():
    # Crear una ventana
    ventana = tk.Tk()
    ventana.title("My finances")
    #ventana.geometry("1024x768")
    #Gets history from file and stores it into an array
    history = load_history("history.txt")

    section0 = Frame(ventana,background=frame_background,relief="flat",borderwidth=0)
    section0.pack(padx=0, pady=0, fill=tk.BOTH, expand=1,side="top",anchor="center")

    #Create a frame inside ventana, this frame will contain most of the widgets
    section1 = Frame(ventana, background=frame_background,relief="flat",borderwidth=0)
    section1.pack(padx=0, pady=0, fill=tk.BOTH, expand=1)

    #Create the structure of the frame
    create_form(section0)
    create_grid(section1,history)

    ventana.mainloop()

if __name__ == "__main__":
    main()
