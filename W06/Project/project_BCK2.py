import tkinter as tk
from screeninfo import get_monitors
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
total_font = ("Calibri bolder", 14)

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
        print("Couldn't open the history file")
        sys.exit(0)
         
def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def create_grid(ventana,data):
    frame = ventana.children.get("section1")
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
    label = Label(frame,text="Current Money: ",background=frame_background,fg="White",relief="sunken",font=total_font)
    label.grid(row=i+1,columnspan=2,sticky="nsew")
    label = Label(frame,text=f'{sum([row[2] for row in data]):,}',background=frame_background,fg="White",relief="sunken",font=total_font)
    label.grid(row=i+1,column=2,columnspan=2,sticky="nsew")
    for i in range(len(data)):
        frame.grid_rowconfigure(i, weight=1)
    for j in range(len(data[0])):
        frame.grid_columnconfigure(j, weight=1)
        
def append_to_file(ventana,amount,income_outcome):
    try:
        monto=float(amount)
        create_modal_window("Se ha guardado")
        try:
            ventana.children.get("section1").destroy()
            create_section1(ventana)
        except:
            None
    except:
        create_modal_window("Please enter a valid number. Use a period (.) as the thousands separator and a comma (,) as the decimal separator.")    

def create_form(ventana):
    section0 = ventana.children.get("section0")
    lbl_amount = Label(section0, text="Amount: ",background=frame_background,fg=lbl_font_color,font=lbl_opt_font)
    entry_amount = Entry(section0,width=12)
    lbl_of = Label(section0, text=" of ",background=frame_background,fg=lbl_font_color,font=lbl_opt_font)
    income_outcome = ttk.Combobox(section0, values=["Income", "Outcome"],font=lbl_opt_font,state="readonly")
    income_outcome["width"] = max(len(option) for option in income_outcome["values"])+2
    income_outcome.set("Income")
    btn_save_income_outcome = Button(section0, text="Save",relief="solid",background=btn_bg_color,fg=lbl_font_color,font=lbl_opt_font,command=lambda: append_to_file(ventana,entry_amount.get(),income_outcome.get()))
    
    lbl_amount.pack(side=tk.LEFT)
    entry_amount.pack(side=tk.LEFT)
    lbl_of.pack(side=tk.LEFT)
    income_outcome.pack(side=tk.LEFT)
    btn_save_income_outcome.pack(side=tk.LEFT)

def create_modal_window(message):
    modal_window = tk.Toplevel()
    modal_window.overrideredirect(True)
    label = tk.Label(
        modal_window,
        text=message,
        background="#337a2c",
        fg="white",
        font=("Calibri", 12, "bold")
    )
    label.pack()
    def close_modal_window(event):
        modal_window.destroy()
    modal_window.bind("<Button-1>", close_modal_window)
    modal_window.geometry(f'{label.winfo_reqwidth()}x{label.winfo_reqheight()}')
    modal_window.after(5000, lambda: close_modal_window(None))
    
def create_section1(ventana):
    section1 = Frame(ventana, background=frame_background, relief="flat", borderwidth=0,name="section1")
    section1.pack(padx=0, pady=0, fill=tk.BOTH, expand=1)
    create_grid(ventana,load_history("history.txt"))

def main():
    ventana = tk.Tk()
    ventana.title("My finances")
    history = load_history("history.txt")
    #form
    section0 = Frame(ventana,background=frame_background,relief="flat",borderwidth=0,name="section0")
    section0.pack(padx=0, pady=0, fill=tk.BOTH, expand=1,side="top",anchor="center")
    #grid
    create_section1(ventana)
    
    create_form(ventana)

    ventana.mainloop()

if __name__ == "__main__":
    main()
