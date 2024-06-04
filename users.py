import tkinter as tk
from tkinter import ttk
from src.database.users import *
from src.takePic import takePic

def add_user():
    adicionar_cliente = tk.Toplevel()
    adicionar_cliente.title("Criar utilizador")
    tk.Label(adicionar_cliente, text="Nome de utilizador:").grid(row=0, column=0)
    tk.Label(adicionar_cliente, text="Nome completo:").grid(row=1, column=0)
    tk.Label(adicionar_cliente, text="Cargo:").grid(row=2, column=0)
    eName = tk.Entry(adicionar_cliente)
    eFullName = tk.Entry(adicionar_cliente)
    eRole = ttk.Combobox(adicionar_cliente, values=["Admin", "Operador", "Contabilidade"])
    eName.grid(row=0, column=1)
    eFullName.grid(row=1, column=1)
    eRole.grid(row=2, column=1)
    def adicionar():
        name = eName.get()
        fullName = eFullName.get()
        role = eRole.get()
        if role == "Admin":
            pedir_password = tk.Toplevel()
            pedir_password.title("Introduza palavra-passe")
            tk.Label(pedir_password, text="Palavra-passe:").grid(row=0, column=0)
            ePassword = tk.Entry(pedir_password)
            ePassword.grid(row=0, column=1)
            def guardar():
                password = ePassword.get()
                create_user(name, fullName, password, role)
            tk.Button(pedir_password, text="Guardar", command=guardar).grid(row=4, columnspan=2)
            pedir_password.mainloop()
        else:
            takePic(name)
    tk.Button(adicionar_cliente, text="Adicionar", command=adicionar).grid(row=4, columnspan=2)
    adicionar_cliente.mainloop()

def remove_user():
    remover_cliente = tk.Toplevel()
    remover_cliente.title("Criar cliente")
    tk.Label(remover_cliente, text="Nome de utilizador:").grid(row=0, column=0)
    eName = tk.Entry(remover_cliente)
    eName.grid(row=0, column=1)
    def remover():
        name = eName.get()
        delete_user(name)
    tk.Button(remover_cliente, text="Remover", command=remover).grid(row=3, columnspan=2)
    remover_cliente.mainloop()
