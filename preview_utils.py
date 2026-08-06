from PIL import Image, ImageTk

def show_preview(file_list, preview_label):
    selected = file_list.selection()
    if selected:
        file_path = file_list.item(selected[0], "tags")[0]
        try:
            img = Image.open(file_path)
            img.thumbnail((300, 300))

            border_size = 4
            bordered_img = Image.new("RGB", (img.width + border_size*2, img.height + border_size*2), "white")
            bordered_img.paste(img, (border_size, border_size))

            img_tk = ImageTk.PhotoImage(bordered_img)
            preview_label.config(image=img_tk, text="")
            preview_label.image = img_tk
        except Exception:
            preview_label.config(image="", text="Không thể preview")
