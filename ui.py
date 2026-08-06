import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from file_utils import browse_folder
from export_utils import export_csv, export_excel
from preview_utils import show_preview

def copy_all(file_list, root):
    rows = file_list.get_children()
    text_data = ", ".join([file_list.item(row)["values"][0] for row in rows])
    root.clipboard_clear()
    root.clipboard_append(text_data)
    root.update()
    messagebox.showinfo("Copy thành công", "Thông tin đã copy vào clipboard!")

def start_ui(app):
    # Sidebar trái
    sidebar = tb.Frame(app, bootstyle="dark")
    sidebar.pack(side="left", fill="y", padx=10, pady=10)

    tb.Button(sidebar, text="Chọn Folder", bootstyle="primary", command=lambda: browse_folder(file_list)).pack(fill="x", pady=5)
    tb.Button(sidebar, text="Xuất CSV", bootstyle="info", command=lambda: export_csv(file_list)).pack(fill="x", pady=5)
    tb.Button(sidebar, text="Xuất Excel", bootstyle="success", command=lambda: export_excel(file_list)).pack(fill="x", pady=5)
    tb.Button(sidebar, text="Copy Info", bootstyle="warning", command=lambda: copy_all(file_list, app)).pack(fill="x", pady=5)

    # Main content
    main_frame = tb.Frame(app, bootstyle="dark")
    main_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    file_list = tb.Treeview(main_frame, columns=("File Info",), show="headings", bootstyle="dark")
    file_list.heading("File Info", text="Tên file và kích thước")
    file_list.pack(fill="both", expand=True)
    file_list.bind("<<TreeviewSelect>>", lambda e: show_preview(file_list, preview_label))

    # Panel phải (preview ảnh)
    preview_frame = tb.Frame(app, bootstyle="secondary")
    preview_frame.pack(side="right", fill="both", padx=10, pady=10)

    preview_label = tb.Label(preview_frame, text="Preview ảnh", bootstyle="inverse-secondary")
    preview_label.pack(pady=10)
