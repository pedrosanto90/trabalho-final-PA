from src.ui.user_admin import *
from src.faceRec import *
import tkinter as tk
from tkinter import PhotoImage

def takePicture():
    takePic('pedro')
try:
    connect()
except:
    create_db()
    create_tables()
    create_user("admin", "Admin", "admin", "Admin")

root = tk.Tk()
root.title("Norauto - Login")
root.geometry("600x400")
root.configure(bg="#1f286d")

logo = PhotoImage(file="assets/logo.png")

canvas = tk.Canvas(root, width=logo.width(), height=logo.height(), bg="#1f286d", highlightthickness=0)
canvas.pack(expand=True)
canvas.create_image(0, 0, anchor="nw", image=logo)

button_login = tk.Button(root, text="Login", command=faceRec)
button_admin_login = tk.Button(root, text="Admin Login", command=admin)

button_window = canvas.create_window(logo.width()//2, (logo.height()//2)+125, anchor="center", window=button_login)
button_window_admin_login = canvas.create_window(logo.width()//2, (logo.height()//2) + 160, anchor="center", window=button_admin_login)

root.mainloop()