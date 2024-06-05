import tkinter as tk
from tkinter import ttk
from src.database.users import *
from src.takePic import takePic
from tkinter import messagebox

def admin():
    admin_login = tk.Toplevel()
    admin_login.title("Login Adminstrador")
    tk.Label(admin_login, text="Nome de utilizador:").grid(row=0, column=0)
    tk.Label(admin_login, text="Password:").grid(row=1, column=0)
    eUsername = tk.Entry(admin_login)
    ePassword = tk.Entry(admin_login, show="*")
    eUsername.grid(row=0, column=1)
    ePassword.grid(row=1, column=1)
    
    def aLogin():
        login(eUsername.get(), ePassword.get())

    tk.Button(admin_login, text="Login", command=aLogin).grid(row=4, columnspan=2)
    admin_login.mainloop()

