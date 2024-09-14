import tkinter as tk
from tkinter import ttk
import psutil
from timer import timer

selected_pids = set()

def get_all_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            processes.append((proc.info['pid'], proc.info['name']))
        except (psutil.NoSuchProcess, FileNotFoundError):
            pass
    return processes

def terminate_selected():
    global selected_pids
    selected_pids.clear()
    for index in process_list.curselection():
        pid = process_list.get(index).split(':')[0]
        selected_pids.add(int(pid))

    selected_time = timer_var.get()

    if selected_time == "Testing":
        seconds = 10  
    else:
        seconds = int(selected_time) * 60  

    timer(seconds, selected_pids)


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


terminate_button = ttk.Button(root, text="Terminate processes and shutdown", command=terminate_selected)
terminate_button.pack(pady=10)


timer_label = ttk.Label(root, text="")
timer_label.pack(pady=10)


processes = get_all_processes()
for pid, name in processes:
    process_list.insert(tk.END, f"{pid}: {name}")


root.mainloop()
