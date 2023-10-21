import tkinter as tk
from screeninfo import get_monitors
from tkinter import Frame, Label, Button,ttk,Entry
from number_entry import IntEntry
import sys

palette = {
    "bg_main": "#002400",               #Main Background Color
    "bg_1": "#556B2F",                  #Background color for lesser elements
    "bg_2": "#000000",                  #Background color 2 for lesser elements
    "font_color_main": "#FFFFFF",       #Main Text Color
    "font_main": ("Calibri", 14),       #Main Font
    "font_1": ("Calibri", 12),          #Font for lesser elements
    "font_2": ("Calibri Bold", 14),     #Font 2 for lesser elements
    "pad_1": 1                          #Global padding option 1
}


def main():
    ventana = tk.Tk()
    ventana.title("My finances")
    
    create_all_widgets(ventana)

    ventana.mainloop()

def create_all_widgets(ventana):
    #form
    create_section0(ventana)
    #grid
    create_section1(ventana)
    
def create_section0(ventana):
    section0 = Frame(ventana,background=palette["bg_main"],relief="flat",borderwidth=0,name="section0")
    section0.pack(padx=0, pady=0, fill=tk.BOTH, expand=1,side="top",anchor="center")
    create_form(ventana)

def create_form(ventana):
    section0 = ventana.children.get("section0")
    
    lbl_amount = Label(section0, text="Amount: ",background=palette["bg_main"],fg=palette["font_color_main"],font=palette["font_1"])
    entry_amount = Entry(section0,width=12,name="entry_amount")    
    lbl_of = Label(section0, text=" of ",background=palette["bg_main"],fg=palette["font_color_main"],font=palette["font_main"])
    income_outcome = ttk.Combobox(section0, values=["Income", "Outcome"],font=palette["font_1"],state="readonly")
    income_outcome["width"] = max(len(option) for option in income_outcome["values"])+2
    income_outcome.set("Income")
    btn_save_income_outcome = Button(section0, text="Save",relief="solid",background=palette["bg_2"],fg=palette["font_color_main"],font=palette["font_1"],command=lambda: save_income_outcome(ventana,entry_amount.get(),income_outcome.get()))
    
    lbl_amount.pack(side=tk.LEFT)
    entry_amount.pack(side=tk.LEFT)
    lbl_of.pack(side=tk.LEFT)
    income_outcome.pack(side=tk.LEFT)
    btn_save_income_outcome.pack(side=tk.LEFT)

def save_income_outcome(ventana,amount,income_outcome):
    try:
        monto=float(amount)
        create_modal_window(f"{income_outcome} saved.")
        try:
            ventana.children.get("section0").children.get("entry_amount").delete(0,tk.END)
            reset_grid(ventana)
        except:
            None
    except:
        create_modal_window("Please enter a valid number. Use a period (.) as the thousands separator and a comma (,) as the decimal separator.")   

def create_modal_window(message):
    modal_window = tk.Toplevel()
    modal_window.overrideredirect(True)
    label = tk.Label(
        modal_window,
        text=message,
        background="#337a2c",
        fg="white",
        font=("Calibri", 16, "bold"),
        justify="left",
        wraplength=800,
        padx=10,
        pady=5,
        relief="solid",
        border=3
    )
    label.pack()
    def close_modal_window(event):
        modal_window.destroy()
    modal_window.bind("<Button-1>", close_modal_window)
    #print(f'{label.winfo_reqwidth()}x{label.winfo_reqheight()}')
    resolution= obtener_resolucion_monitor_actual()
    #print(resolution)
    modal_window.geometry(f'{label.winfo_reqwidth()}x{label.winfo_reqheight()}+{resolution[0]-label.winfo_reqwidth()}+{resolution[1]-label.winfo_reqheight()}')
    modal_window.after(5000, lambda: close_modal_window(None))

def create_section1(ventana):
    section1 = Frame(ventana, background=palette["bg_main"], relief="flat", borderwidth=0,name="section1")
    section1.pack(padx=0, pady=0, fill=tk.BOTH, expand=1)
    create_grid(ventana,load_history("history.txt"))

def create_grid(ventana,data):
    frame = ventana.children.get("section1")
    rows_to_display = 50
    for i, row in enumerate(data if len(data)<=rows_to_display else data[-rows_to_display:]):
        for j, item in enumerate(row):
            if j==2 and es_numero(item) and float(item)>0:
                label = Label(frame, text=f'{item:,}', anchor="e",justify="left",background=palette["bg_1"],font=palette["font_main"],fg=palette["font_color_main"])
                label.grid(row=i, column=j, padx=palette["pad_1"], pady=0, sticky="nsew")
                label = Label(frame, text="", anchor="e",justify="left",background=palette["bg_1"],font=palette["font_main"],fg=palette["font_color_main"])
                label.grid(row=i, column=j+1, padx=palette["pad_1"], pady=0, sticky="nsew")
            elif j==2 and es_numero(item) and not float(item)>0:
                label = Label(frame, text="", anchor="e",justify="left",background=palette["bg_1"],font=palette["font_main"],fg=palette["font_color_main"])
                label.grid(row=i, column=j, padx=palette["pad_1"], pady=0, sticky="nsew")
                label = Label(frame, text=f'{item:,}', anchor="e",justify="left",background=palette["bg_1"],font=palette["font_main"],fg=palette["font_color_main"])
                label.grid(row=i, column=j+1, padx=palette["pad_1"], pady=0, sticky="nsew")
            else:
                label = Label(frame, text=item, anchor="e",justify="left",background=palette["bg_1"],font=palette["font_main"],fg=palette["font_color_main"])
                label.grid(row=i, column=j, padx=palette["pad_1"], pady=0, sticky="nsew")
    label = Label(frame,text="Current Money: ",background=palette["bg_main"],fg="White",relief="sunken",font=palette["font_2"])
    label.grid(row=i+1,columnspan=2,sticky="nsew")
    label = Label(frame,text=f'{sum([row[2] for row in data]):,}',background=palette["bg_2"],fg="White",relief="sunken",font=palette["font_2"])
    label.grid(row=i+1,column=2,columnspan=2,sticky="nsew")
    for i in range(len(data)):
        frame.grid_rowconfigure(i, weight=1)
    for j in range(len(data[0])):
        frame.grid_columnconfigure(j, weight=1)

def reset_grid(ventana):
    ventana.children.get("section1").destroy()
    create_section1(ventana)

def load_history(filename):
    try:
        arr = []
        with open(filename, 'r+') as archivo:
            for linea in archivo:
                row = linea.strip("\n").split(", ")
                for i in range(len(row)):
                    try:
                        row[i]=round(float(row[i]))
                    except:
                        None
                arr.append(row)
        return arr
    except (FileNotFoundError,PermissionError):
        #print("Couldn't open the history file")
        sys.exit(0)
         
def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def obtener_resolucion_monitor_actual():
    # Obtiene una lista de todos los monitores conectados
    monitores = get_monitors()

    if monitores:
        # El primer monitor en la lista es el monitor principal
        monitor_principal = monitores[0]
        ancho = monitor_principal.width
        alto = monitor_principal.height
        return [ancho,alto]
    else:
        return "No se encontraron monitores."   



if __name__ == "__main__":
    main()
