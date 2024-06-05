import tkinter as tk
from src.database.users import *
from tkinter import messagebox
from src.ui.main import *
 
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
        username = eUsername.get()
        password = ePassword.get()
        if username and password:
            if login(username, password):
                messagebox.showinfo("Sucesso", "Login efetuado com sucesso!")
                main_window()
            else:
                messagebox.showerror("Erro", "Nome de utilizador ou palavra-passe incorretos.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
 
    tk.Button(admin_login, text="Login", command=aLogin).grid(row=4, columnspan=2)
    admin_login.mainloop()
