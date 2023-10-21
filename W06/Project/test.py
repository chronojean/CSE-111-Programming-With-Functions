import tkinter as tk

class RoundedLabel(tk.Canvas):
    def __init__(self, master=None, radius=10, **kwargs):
        super().__init__(master, **kwargs)
        self.radius = radius
        self.config(bg=kwargs.get('bg', 'white'))

    def create_rounded_rectangle(self, x1, y1, x2, y2, **kwargs):
        self.create_arc(x1, y1, x1 + 2 * self.radius, y1 + 2 * self.radius, start=90, extent=90, **kwargs)
        self.create_arc(x2 - 2 * self.radius, y1, x2, y1 + 2 * self.radius, start=0, extent=90, **kwargs)
        self.create_arc(x1, y2 - 2 * self.radius, x1 + 2 * self.radius, y2, start=180, extent=90, **kwargs)
        self.create_arc(x2 - 2 * self.radius, y2 - 2 * self.radius, x2, y2, start=270, extent=90, **kwargs)
        self.create_rectangle(x1 + self.radius, y1, x2 - self.radius, y2, **kwargs)
        self.create_rectangle(x1, y1 + self.radius, x2, y2 - self.radius, **kwargs)

def create_modal_window(message):
    modal_window = tk.Toplevel()
    modal_window.overrideredirect(True)
    
    label = RoundedLabel(
        modal_window,
        radius=10,  # Adjust the radius as needed
        bg="#337a2c",
        width=400,  # Adjust the width
        height=200  # Adjust the height
    )
    label.pack()

    text = tk.Label(
        label,
        text=message,
        background="#337a2c",
        fg="white",
        font=("Calibri", 16, "bold"),
        justify="left",
        wraplength=380,  # Adjust the wraplength
        padx=10,
        pady=10
    )
    text.pack()

create_modal_window("This is a rounded label just like 'border-radius' in CSS")
