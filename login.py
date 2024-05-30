import tkinter as tk
from tkinter import PhotoImage
from takePic import takePic

root = tk.Tk()
root.title("Norauto - Login")
root.geometry("600x400")
root.configure(bg="#1f286d")

logo = PhotoImage(file="assets/logo.png")

canvas = tk.Canvas(root, width=logo.width(), height=logo.height(), bg="#1f286d", highlightthickness=0)
canvas.pack(expand=True)
canvas.create_image(0, 0, anchor="nw", image=logo)

button_login = tk.Button(root, text="Login", command=takePic)
button_window = canvas.create_window(logo.width()//2, (logo.height()//2)+150, anchor="center", window=button_login)

root.mainloop()
