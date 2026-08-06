import os
from tkinter import filedialog
from PIL import Image

def get_image_info(file_path):
    try:
        with Image.open(file_path) as img:
            width, height = img.size
        return f"{os.path.basename(file_path)} (size: {width}x{height})"
    except Exception:
        return f"{os.path.basename(file_path)} (Not an image)"

def browse_folder(file_list):
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        list_files(folder_selected, file_list)

def list_files(folder_path, file_list):
    file_list.delete(*file_list.get_children())
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            info = get_image_info(file_path)
            file_list.insert("", "end", values=(info,), tags=(file_path,))
