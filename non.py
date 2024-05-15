import tkinter as tk

def create_window():
    global last_window
    if last_window is not None:
        last_window.destroy()
    last_window = tk.Tk()
    last_window.mainloop()

create_window()
