import tkinter as tk
from tkinter import messagebox
import datetime
import time
import threading
import platform
import os

# ---------------- SOUND FUNCTION ----------------
def play_sound():
    system = platform.system()

    if system == "Windows":
        import winsound
        for _ in range(5):
            winsound.Beep(1000, 1000)
    else:
        for _ in range(5):
            print("\a")
            time.sleep(1)

# ---------------- ALARM FUNCTION ----------------
def start_alarm(hour, minute, period):
    if period == "PM" and hour != 12:
        hour += 12
    if period == "AM" and hour == 12:
        hour = 0

    status_label.config(text="Alarm Is Set", bg="green")

    while True:
        now = datetime.datetime.now()

        if now.hour == hour and now.minute == minute:
            status_label.config(text="⏰ Alarm Ringing!", bg="red")
            play_sound()
            break

        time.sleep(10)

# ---------------- BUTTON FUNCTION ----------------
def set_alarm():
    try:
        hour = int(hour_entry.get())
        minute = int(minute_entry.get())
        period = period_entry.get().upper()

        if period not in ["AM", "PM"]:
            messagebox.showerror("Error", "Enter AM or PM")
            return

        t = threading.Thread(target=start_alarm, args=(hour, minute, period))
        t.start()

    except:
        messagebox.showerror("Error", "Invalid Input")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Alarm Management System")
root.geometry("400x300")

# Title
title = tk.Label(root, text="Alarm Management System",
                 bg="blue", fg="white", font=("Arial", 16))
title.pack(fill="x", pady=10)

# Hour
tk.Label(root, text="Enter Hour").pack()
hour_entry = tk.Entry(root)
hour_entry.pack()

# Minute
tk.Label(root, text="Enter Minute").pack()
minute_entry = tk.Entry(root)
minute_entry.pack()

# AM/PM
tk.Label(root, text="AM / PM").pack()
period_entry = tk.Entry(root)
period_entry.pack()

# Button
set_btn = tk.Button(root, text="Set Alarm", bg="blue", fg="white",
                    command=set_alarm)
set_btn.pack(pady=10)

# Status
status_label = tk.Label(root, text="Alarm Is Not Set", bg="blue", fg="white")
status_label.pack(pady=10)

# Run app
root.mainloop()
