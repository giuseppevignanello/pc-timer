import time
import os
import psutil

def timer(seconds, pids_to_terminate):
    for i in range(seconds, 0, -1):
        print(f"Spegnimento in {i} secondi...", end="\r")
        time.sleep(1)

    print("Spegnimento in corso...")

    for pid in pids_to_terminate:
        try:
            process = psutil.Process(pid)
            process.terminate()  
            print(f"Process {pid} terminated.")
        except psutil.NoSuchProcess:
            print(f"Process {pid} not found o terminated.")

    
    os.system("shutdown /s /t 1")  
