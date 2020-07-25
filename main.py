import tkinter as tk
import psutil
from time import sleep
from datetime import datetime




window = tk.Tk()

window.title("Welcome to LikeGeeks app")

memory = dict(psutil.virtual_memory()._asdict())
cpu_percent = psutil.cpu_percent()
used_memory = round(memory['used'] * 100 / memory['total'])
print("Avaialble Memory: " + str(used_memory) + "%")
# print("Memory: " + str(memory))
print("CPU usage: " + str(cpu_percent) + "%")

running = True

def close_window():
    global running
    running = False
    window.destroy()

window.protocol("WM_DELETE_WINDOW", close_window)


cpu_percent_text = tk.StringVar(window)
cpu_percent_label = tk.Label(window, textvariable=cpu_percent_text)
cpu_percent_label.pack()

used_memory_text = tk.StringVar(window)
used_memory_label = tk.Label(window, textvariable=used_memory_text)
used_memory_label.pack()

available_memory_text = tk.StringVar(window)
available_memory_label = tk.Label(window, textvariable=available_memory_text)
available_memory_label.pack()

# Exit button
btn = tk.Button(window, text="Exit", command = close_window)
btn.pack()

# Window Size
window.geometry('350x200')



while running:

    memory = dict(psutil.virtual_memory()._asdict())
    cpu_percent = round(psutil.cpu_percent())
    used_memory = round(memory['used'] * 100 / memory['total'])
    available_memory = round(memory['available'] * 100 / memory['total'])

    cpu_percent_text.set("Cpu Usage: " + str(cpu_percent) + '%')
    used_memory_text.set("RAM used: " + str(used_memory)+ '%')
    available_memory_text.set("RAM extra: " + str(available_memory)+ '%')
    print(datetime.now())
    print("Used Memory: " + str(used_memory) + "%")
    print("Memory: " + str(memory))
    print("CPU usage: " + str(cpu_percent) + "%")
    

    window.update()

    sleep(0.1)


