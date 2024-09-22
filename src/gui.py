import tkinter as tk
from tkinter import ttk
import psutil
from timer import start_timer

def get_all_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            processes.append((proc.info['pid'], proc.info['name']))
        except (psutil.NoSuchProcess, FileNotFoundError):
            pass
    return processes

def terminate_all_processes():
    selected_time = timer_var.get()

    if selected_time == "Testing":
        seconds = 3  
    else:
        seconds = int(selected_time) * 60  

    start_timer(seconds)


root = tk.Tk()
root.title("Shutdown scheduled")


style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 12))


timer_var = tk.StringVar(root)
timer_choices = ["Testing"] + [str(i) for i in range(5, 121, 5)]  
timer_menu = ttk.Combobox(root, textvariable=timer_var, values=timer_choices)
timer_menu.current(0)  
timer_menu.pack(pady=10)


process_list = tk.Listbox(root, height=15, width=50)
process_list.pack(pady=10)


terminate_button = tk.Button(root, text="Terminate all processes and shutdown", command=terminate_all_processes)
terminate_button.pack(pady=10)


timer_label = tk.Label(root, text="")
timer_label.pack(pady=10)


processes = get_all_processes()
for pid, name in processes:
    process_list.insert(tk.END, f"{pid}: {name}")


root.mainloop()
