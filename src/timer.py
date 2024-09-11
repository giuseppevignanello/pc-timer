import time
import os

def timer(seconds):
    for i in range(seconds, 0, -1):
        print(f"Shutting down in {i} seconds...", end="\r")
        time.sleep(1)
    print("Shutting down...")
    os.system("shutdown /s /t 1")