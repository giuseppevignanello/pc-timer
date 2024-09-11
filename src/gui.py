import tkinter as tk
from timer import timer

def start_timer():
    try:
        seconds = int(entry.get())
        if seconds <= 0:
            raise ValueError("Please enter a positive number.")
        timer(seconds)
    except ValueError as e:
        error_label.config(text=str(e))

root = tk.Tk()
root.title("Shutdown Timer")

label = tk.Label(root, text="Enter time in seconds:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Start Timer", command=start_timer)
button.pack()

error_label = tk.Label(root, text="", fg="red")
error_label.pack()

root.mainloop()