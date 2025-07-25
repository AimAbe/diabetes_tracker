import os
import csv
from datetime import datetime

DATA_FILE = "storage.csv"
HEADER = ["Date", "Type", "Kind", "Value", "Time", "Note"]

def ensure_header():
    if not os.path.isfile(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        with open(DATA_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(HEADER)

def log_blood_sugar(value, time=None, note=""):
    ensure_header()
    time = time or datetime.now().strftime("%H:%M")
    date = datetime.now().date()
    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, "blood_sugar", "", value, time, note])
    print(f"[✓] Logged blood sugar: {value} mg/dL at {time}")

def log_insulin(kind, amount, time=None, note=""):
    ensure_header()
    time = time or datetime.now().strftime("%H:%M")
    date = datetime.now().date()
    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, "insulin", kind, amount, time, note])
    print(f"[✓] Logged insulin: {amount} units ({kind}) at {time}")