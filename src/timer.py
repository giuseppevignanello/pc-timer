import pygetwindow as gw
import win32api
import win32con
import time

def close_all_windows():
    # Ottieni tutti i titoli delle finestre attive
    windows = gw.getAllTitles()

    for window_title in windows:
        if window_title:  # Filtra finestre senza titolo
            try:
                all_windows = gw.getWindowsWithTitle(window_title)
                for window in all_windows:
                    print(f"Chiudendo finestra: {window_title}")
                    hwnd = window._hWnd
                    win32api.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
                    time.sleep(0.5)  # Aspetta mezzo secondo tra le chiusure
            except Exception as e:
                print(f"Errore nella chiusura di {window_title}: {str(e)}")

def start_timer(seconds):
    for i in range(seconds, 0, -1):
        print(f"Spegnimento in {i} secondi...", end="\r")
        time.sleep(1)

    print("Chiudendo le finestre e spegnimento in corso...")
    close_all_windows()
    shutdown_computer()

def shutdown_computer():
    print("Spegnimento del computer...")
    # os.system("shutdown /s /t 1")  # Abilita questa riga per spegnere il PC


