import tkinter as tk
import calendar
from screeninfo import get_monitors
from tkinter import Frame, Label, Button,ttk,Entry,Scrollbar
from datetime import datetime
from tkcalendar import DateEntry

filename = "history.txt"
palette = {
    "bg_main": "#002400",               #Main Background Color
    "bg_0":"#657D37",                   #Background color 0 for lesser elements
    "bg_1": "#556B2F",                  #Background color 1 for lesser elements
    "bg_2": "#000000",                  #Background color 2 for lesser elements
    "bg_3": "#3F4D23",                  #Background color 3 for lesser elements
    "font_color_main": "#FFFFFF",       #Main Text Color
    "font_color_warning": "#FF0000",    #Red font color for negative balance
    "font_main": ("Calibri", 13),       #Main Font
    "font_1": ("Calibri", 13),          #Font for lesser elements
    "font_2": ("Calibri Bold", 18),     #Font 2 for lesser elements
    "font_balance":("Comic Sans MS",14),#Font for total balance
    "pad_1": 1                          #Global padding option 1
}
def set_styles(ventana):
    #Sets some styles
    s = ttk.Style(ventana)
    s.theme_use('classic')
    s.configure('TCombobox', arrowsize=26)
    s.configure('DateEntry', arrowsize=26)
    ventana.config(background=palette["bg_main"])

def main():
    #Create main window
    ventana = tk.Tk()
    ventana.title("My finances")
    create_window_sections(ventana)
    set_styles(ventana)
    ventana.mainloop()
    
def create_window_sections(ventana):
    #form
    create_section0(ventana)
    #grid
    create_section1(ventana)
    #summary
    create_section2(ventana)
    #ventana.update_idletasks()
    
def create_section0(ventana):
    section0 = Frame(ventana,background=palette["bg_main"],relief="flat",borderwidth=0,name="section0")
    section0.pack()
    create_form(ventana)

def create_form(ventana):
    section0 = ventana.children.get("section0")
    is_entry_number = section0.register(is_a_number)
    lbl_amount = Label(section0, text="Amount: ",background=palette["bg_main"],fg=palette["font_color_main"],font=palette["font_1"])
    entry_amount = Entry(section0,width=12,name="entry_amount",justify="right",validate="all",validatecommand=(is_entry_number, "%P"))
    lbl_of = Label(section0, text=" of ",background=palette["bg_main"],fg=palette["font_color_main"],font=palette["font_main"])
    income_outcome = ttk.Combobox(section0, values=["Income", "Outcome"],font=palette["font_1"],state="readonly",name="income_outcome")
    income_outcome["width"] = max(len(option) for option in income_outcome["values"])+2
    income_outcome.set("Income")
    cal = DateEntry(section0, width=12, background='darkblue',foreground='white', borderwidth=2, state="readonly",name="date_transaction",font=palette["font_1"])
    lbl_desc = Label(section0,text="Description",background=palette["bg_main"],fg=palette["font_color_main"],font=palette["font_1"])
    entry_desc = Entry(section0,name="entry_desc", justify="left")
    btn_save_income_outcome = Button(section0, text="Save",relief="solid",background=palette["bg_2"],highlightbackground=palette["bg_3"],activebackground=palette["bg_0"],activeforeground=palette["font_color_main"],fg=palette["font_color_main"],font=palette["font_1"],command=lambda: save_income_outcome(ventana,entry_amount.get(),income_outcome.get(),entry_desc.get(),cal.get_date()))
    lbl_amount.grid(row=0,column=0,sticky="nsew")
    entry_amount.grid(row=0,column=1,sticky="nsew")
    lbl_of.grid(row=0,column=2,sticky="nsew")
    income_outcome.grid(row=0,column=3,sticky="nsew")
    cal.grid(row=0,column=4,sticky="nsew")
    #Second Row
    lbl_desc.grid(row=1,column=0,sticky="nsew")
    entry_desc.grid(row=1,column=1,columnspan=3,sticky="nsew")
    btn_save_income_outcome.grid(row=1,column=4)
def is_a_number(val):
    if (val!="" or val.startswith(".") )and (not (es_numero(val)) or " " in str(val)):
        return False
    return True
def create_section1(ventana):
    section1 = Frame(ventana, background=palette["bg_main"], relief="flat", borderwidth=0,name="section1")
    section1.pack(padx=0, pady=0, fill="y", expand=1)
    create_grid(ventana,load_history(filename))

def create_grid(ventana, data):
    section1 = ventana.children.get("section1")
    
    # Crear un Canvas para contener el Frame con el grid
    canvas = tk.Canvas(section1,background=palette["bg_main"])
    canvas.pack(side="left", fill="both", expand=True)
    
    # Agregar un scrollbar vertical al Canvas
    scrollbar = tk.Scrollbar(section1, orient="vertical", command=canvas.yview,activebackground="GREEN2",background="GREEN4",border=4,highlightbackground=palette["bg_0"],highlightthickness=0,repeatdelay=50,repeatinterval=75,troughcolor=palette["bg_2"],width=25,relief="flat")
    scrollbar.pack(side="right", fill="y")
    
    canvas.configure(yscrollcommand=scrollbar.set)
    
    frame_grid = tk.Frame(canvas)
    frame_id = canvas.create_window((0, 0), window=frame_grid, anchor="nw")
    
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            grid_bg = f"bg_{(i%2)}"
            if j == 2 and es_numero(item) and float(item) > 0:
                label = Label(frame_grid, text=f'{item:,.2f}', anchor="se", justify="left", background=palette[grid_bg], font=palette["font_main"], fg=palette["font_color_main"])
                label.grid(row=i, column=j, padx=palette["pad_1"], pady=0, sticky="nsew")
                label = Label(frame_grid, text="", anchor="e", justify="right", background=palette[grid_bg], font=palette["font_main"], fg=palette["font_color_main"])
                label.grid(row=i, column=j + 1, padx=palette["pad_1"], pady=0, sticky="nsew")
            elif j == 2 and es_numero(item) and not float(item) > 0:
                label = Label(frame_grid, text="", anchor="e", justify="right", background=palette[grid_bg], font=palette["font_main"], fg=palette["font_color_main"])
                label.grid(row=i, column=j, padx=palette["pad_1"], pady=0, sticky="nsew")
                label = Label(frame_grid, text=f'{item:,.2f}', anchor="se", justify="left", background=palette[grid_bg], font=palette["font_main"], fg=palette["font_color_main"])
                label.grid(row=i, column=j + 1, padx=palette["pad_1"], pady=0, sticky="nsew")
            else:
                label = Label(frame_grid, text=date_short_day(item) if j == 0 else item.replace(";",","),wraplength=500, anchor="w", justify="left", background=palette[grid_bg], font=palette["font_main"], fg=palette["font_color_main"])
                label.grid(row=i, column=j, padx=palette["pad_1"], pady=0, sticky="nsew")
    
    # Ajustar el tamaño del canvas según el tamaño del contenido
    def adjust_canvas_size(event):
        canvas_width = canvas.winfo_reqwidth()
        if event.width > canvas_width:
            # expand canvas to the width of scrollable_frame
            canvas.configure(width=event.width)
        else:
            # expand scrollable_frame to the width of canvas
            canvas.itemconfigure(frame_id, width=canvas_width)
        canvas.configure(scrollregion=canvas.bbox("all"))
    
    frame_grid.bind("<Configure>", adjust_canvas_size)
    
    # Actualizar el canvas
    canvas.update()
    canvas.yview_moveto(1.0)
    

def reset_grid(ventana):
    ventana.children.get("section0").children.get("entry_amount").delete(0, "end")
    ventana.children.get("section0").children.get("entry_desc").delete(0, "end")

    ventana.children.get("section1").destroy()
    ventana.children.get("section2").destroy()
    
    create_section1(ventana)
    create_section2(ventana)
    
def create_section2(ventana):
    section2 = Frame(ventana,background=palette["bg_main"],relief="flat",borderwidth=0,name="section2")
    create_summary(ventana)
    section2.pack(padx=0, pady=0, fill=tk.BOTH, expand=1)

def create_summary(ventana):
    section2 = ventana.children.get("section2")
    section2.grid_rowconfigure(0, weight=1)
    section2.grid_columnconfigure((0, 1, 2, 3), weight=1)
    data = load_history(filename)
    
    try:
        label = Label(section2, text="Current Money: ", background=palette["bg_main"], fg="White", relief="sunken", font=palette["font_2"])
        label.grid(row=0, columnspan=2, sticky="nsew")
        label = Label(section2, text=f'{sum([row[2] for row in data]):,.2f}', background=palette["bg_2"], fg="White", relief="sunken", font=palette["font_2"])
        label.grid(row= 0, column=2, columnspan=2, sticky="nsew")
        for i in range(len(data)):
            section2.grid_rowconfigure(i, weight=1)
        for j in range(len(data[0])):
            section2.grid_columnconfigure(j, weight=1)
    except:
        pass
     
    lbl_summary_title_type = Label(section2, text="              ",background=palette["bg_main"],fg=palette["font_color_main"],font=palette["font_1"])
    lbl_summary_title_income = Label(section2, text="Income",background=palette["bg_main"],fg=palette["font_color_main"],font=palette["font_1"])
    lbl_summary_title_outcome = Label(section2, text="Outcome",background=palette["bg_main"],fg=palette["font_color_main"],font=palette["font_1"])
    lbl_summary_title_balance = Label(section2, text="Balance",background=palette["bg_main"],fg=palette["font_color_main"],font=palette["font_1"])
    
    inc_out = get_last_n_days_values(data,0)
    lbl_summary_daily_type = Label(section2, text="Daily Summary",background=palette["bg_main"],fg=palette["font_color_main"],font=palette["font_1"],anchor="w", justify="left")
    lbl_summary_daily_income = Label(section2, text=f"{inc_out['income']:,.2f}",background=palette["bg_1"],fg=palette["font_color_main"],font=palette["font_1"],anchor="e", justify="right")
    lbl_summary_daily_outcome = Label(section2, text=f"{inc_out['outcome']:,.2f}",background=palette["bg_1"],fg=palette["font_color_main"],font=palette["font_1"],anchor="e", justify="right")
    lbl_summary_daily_balance = Label(section2, text=f"{(inc_out['income']+inc_out['outcome']):,.2f}",background=palette["bg_1" if (inc_out['income']+inc_out['outcome'])>=0 else "font_color_warning"],fg=palette["font_color_main"],font=palette["font_balance"],anchor="e", justify="right")
    
    inc_out = get_last_n_days_values(data,7)
    lbl_summary_weekly_type = Label(section2, text="Weekly Summary",background=palette["bg_main"],fg=palette["font_color_main"],font=palette["font_1"],anchor="w", justify="left")
    lbl_summary_weekly_income = Label(section2, text=f"{inc_out['income']:,.2f}",background=palette["bg_3"],fg=palette["font_color_main"],font=palette["font_1"],anchor="e", justify="right")
    lbl_summary_weekly_outcome = Label(section2, text=f"{inc_out['outcome']:,.2f}",background=palette["bg_3"],fg=palette["font_color_main"],font=palette["font_1"],anchor="e", justify="right")
    lbl_summary_weekly_balance = Label(section2, text=f"{(inc_out['income']+inc_out['outcome']):,.2f}",background=palette["bg_3" if (inc_out['income']+inc_out['outcome'])>=0 else "font_color_warning"],fg=palette["font_color_main"],font=palette["font_balance"],anchor="e", justify="right")
    
    inc_out = get_last_n_days_values(data,30)
    lbl_summary_monthly_type = Label(section2, text="Monthly Summary",background=palette["bg_main"],fg=palette["font_color_main"],font=palette["font_1"],anchor="w", justify="left")
    lbl_summary_monthly_income = Label(section2, text=f"{inc_out['income']:,.2f}",background=palette["bg_1"],fg=palette["font_color_main"],font=palette["font_1"],anchor="e", justify="right")
    lbl_summary_monthly_outcome = Label(section2, text=f"{inc_out['outcome']:,.2f}",background=palette["bg_1"],fg=palette["font_color_main"],font=palette["font_1"],anchor="e", justify="right")
    lbl_summary_monthly_balance = Label(section2, text=f"{(inc_out['income']+inc_out['outcome']):,.2f}",background=palette["bg_1" if (inc_out['income']+inc_out['outcome'])>=0 else "font_color_warning"],fg=palette["font_color_main"],font=palette["font_balance"],anchor="e", justify="right")
    
    lbl_summary_title_type.grid(row=1,column=0,sticky="nsew",padx=1,pady=1)
    lbl_summary_title_income.grid(row=1,column=1,sticky="nsew",padx=1,pady=1)
    lbl_summary_title_outcome.grid(row=1,column=2,sticky="nsew",padx=1,pady=1)
    lbl_summary_title_balance.grid(row=1,column=3,sticky="nsew",padx=1,pady=1)
    
    lbl_summary_daily_type.grid(row=2,column=0,sticky="nsew",padx=1)
    lbl_summary_daily_income.grid(row=2,column=1,sticky="nsew",padx=1)
    lbl_summary_daily_outcome.grid(row=2,column=2,sticky="nsew",padx=1)
    lbl_summary_daily_balance.grid(row=2,column=3,sticky="nsew",padx=1)
    
    lbl_summary_weekly_type.grid(row=3,column=0,sticky="nsew",padx=1)
    lbl_summary_weekly_income.grid(row=3,column=1,sticky="nsew",padx=1)
    lbl_summary_weekly_outcome.grid(row=3,column=2,sticky="nsew",padx=1)
    lbl_summary_weekly_balance.grid(row=3,column=3,sticky="nsew",padx=1)
    
    lbl_summary_monthly_type.grid(row=4,column=0,sticky="nsew",padx=1)
    lbl_summary_monthly_income.grid(row=4,column=1,sticky="nsew",padx=1)
    lbl_summary_monthly_outcome.grid(row=4,column=2,sticky="nsew",padx=1)
    lbl_summary_monthly_balance.grid(row=4,column=3,sticky="nsew",padx=1)
   
def create_modal_window(message):
    modal_window = tk.Toplevel()
    modal_window.overrideredirect(True)
    label = tk.Label(modal_window,text=message,background="#337a2c",fg="white",font=("Calibri", 16, "bold"),justify="left",wraplength=800,padx=10,pady=5,relief="solid",border=3)
    label.pack()
    def close_modal_window(event):
        modal_window.destroy()
    modal_window.bind("<Button-1>", close_modal_window)
    resolution= obtener_resolucion_monitor_actual()
    modal_window.geometry(f'{label.winfo_reqwidth()}x{label.winfo_reqheight()}+{resolution[0]-label.winfo_reqwidth()}+{resolution[1]-label.winfo_reqheight()}')
    modal_window.after(5000, lambda: close_modal_window(None))

def load_history(filename):
    try:
        arr = []
        with open(filename, 'r+') as archivo:
            for linea in archivo:
                row = linea.strip("\n").split(", ")
                for i in range(len(row)):
                    try:
                        row[i]=round(float(row[i]),2)
                    except:
                        None
                arr.append(row)
        arr = sorted(arr, key=lambda x: x[0])
        return arr
    except (FileNotFoundError,PermissionError):
        create_modal_window("Couldn't open the history file")
        return []
         
def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
    
def date_short_day(given_date):
    # Convertir la fecha del archivo a un objeto datetime
    fecha_objeto = datetime.strptime(given_date, "%Y/%m/%d")

    # Obtener el nombre abreviado del día de la semana usando la clase calendar
    nombre_dia_abreviado = calendar.day_abbr[fecha_objeto.weekday()]

    # Formatear la fecha con el nombre abreviado del día de la semana
    fecha_formateada = f"{fecha_objeto.strftime('%Y/%m/%d')} {nombre_dia_abreviado}"

    return fecha_formateada

def save_income_outcome(ventana,amount,income_outcome,description,date_of_data):
    if validate_data(ventana,amount,income_outcome,description,date_of_data):
        try:
            append_to_file(f"{date_of_data.strftime('%Y/%m/%d')}, {description.replace(',',';')}, {round(float(amount),2) if income_outcome=='Income' else round(float(amount)*-1,2)}",filename)
            reset_grid(ventana)
            create_modal_window(f"{income_outcome.capitalize()} saved.")
        except:
            create_modal_window("An error ocurred on save, File is locked as read-only or you don't have the required permissions to work with the file.")
        
def get_last_n_days_values(data, num_days):
    current_date = datetime.now().date()
    last_n_days_values = []
    last_n_days_values = [entry[2] for entry in data if (current_date-datetime.strptime(entry[0], "%Y/%m/%d").date()).days<=num_days]
    inc_out = {}
    inc_out["income"] = sum([value for value in last_n_days_values if value>0])
    inc_out["outcome"] = sum([value for value in last_n_days_values if value<0])    
    return inc_out

def validate_data(ventana,amount,income_outcome,description,date_of_data):
    if not es_numero(amount) or float(amount) <=0:
        create_modal_window(f"The amount must be a positive number.")
        return False
    elif date_of_data>datetime.now().date():
        create_modal_window(f"The selected date is in the future. Please enter a valid date.")
        return False
    elif len(description)==0:
        create_modal_window(f"Please enter a description for this transaction.")
        return False
    return True

def obtener_resolucion_monitor_actual():
    monitores = get_monitors()

    if monitores:
        # El primer monitor en la lista es el monitor principal
        monitor_principal = monitores[0]
        ancho = monitor_principal.width
        alto = monitor_principal.height
        return [ancho,alto]
    else:
        return "No se encontraron monitores."

def append_to_file(linea,my_filename="test_history.txt"):
    try:
        with open(my_filename, "a+") as file:
            file.write(f"{linea}\n")
            file.seek(0)
            content = file.read()
            return content
    except IOError:
        input("An error occurred while opening the file. Maybe the file is blocked or marked as 'read only' or you don't have the permission to access the file")

if __name__ == "__main__":
    main()
