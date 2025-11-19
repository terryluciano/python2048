import tkinter as tk
from tkinter import Tk, ttk

root = tk.Tk()
root.title("2048")

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenmmwidth()

window_width = 400
window_height = 400

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.resizable(True, True)


def main():
    style = ttk.Style()
    style.configure("Main.TFrame", background="blue", borderwidth=1)

    main_frame = ttk.Frame(root, padding=(4), style="Main.TFrame")
    main_frame.grid(column=4, row=4, padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
