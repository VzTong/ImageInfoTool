import ttkbootstrap as tb
from ui import start_ui

def main():
    app = tb.Window(themename="darkly")  # theme darkly, cyborg, superhero...
    app.title("ImageInfoViewer")
    app.geometry("1200x700")
    start_ui(app)
    app.mainloop()

if __name__ == "__main__":
    main()
