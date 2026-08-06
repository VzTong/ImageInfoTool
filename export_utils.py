import csv
import pandas as pd
import os
from tkinter import messagebox

def ensure_output_dir():
    if not os.path.exists("output"):
        os.makedirs("output")

def export_csv(file_list):
    ensure_output_dir()
    rows = file_list.get_children()
    data = [file_list.item(row)["values"][0] for row in rows]
    with open("output/image_info.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["File Info"])
        for row in data:
            writer.writerow([row])
    messagebox.showinfo("Xuất CSV", "Đã lưu file output/image_info.csv")

def export_excel(file_list):
    ensure_output_dir()
    rows = file_list.get_children()
    data = [file_list.item(row)["values"][0] for row in rows]
    df = pd.DataFrame(data, columns=["File Info"])
    df.to_excel("output/image_info.xlsx", index=False)
    messagebox.showinfo("Xuất Excel", "Đã lưu file output/image_info.xlsx")
