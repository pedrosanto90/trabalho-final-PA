import tkinter as tk
from tkinter import PhotoImage
from src.takePic import takePic
from src.database.database import *
<<<<<<< HEAD
from src.database.users import create_user

=======
from user_admin import *
>>>>>>> pedro

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

button_login = tk.Button(root, text="Login", command=takePicture)
button_admin_login = tk.Button(root, text="Admin Login", command=admin)

button_window = canvas.create_window(logo.width()//2, (logo.height()//2)+150, anchor="center", window=button_login)
button_window_admin_login = canvas.create_window(logo.width()//2, (logo.height()//2) + 200, anchor="center", window=button_admin_login)

root.mainloop()

