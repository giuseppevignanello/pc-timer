import subprocess
import time

def shutdown():
    subprocess.call('shutdown /s /f /t 0', shell=True)

def start_timer(seconds):
    shutdown()
