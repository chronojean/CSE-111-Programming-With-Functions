import tkinter as tk
from tkinter import messagebox

def show_alert():
    messagebox.showinfo("Alert", "This is an alert message!")

# Create the main window
window = tk.Tk()
window.title("Python Tkinter Alert")

# Create a button to trigger the alert
button = tk.Button(window, text="Show Alert", command=show_alert)
button.pack()

# Start the main loop
window.mainloop()
