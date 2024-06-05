import tkinter as tk
from tkinter import ttk
from src.database.clients import *
from tkinter import messagebox

def add_client():
    adicionar_cliente = tk.Toplevel()
    adicionar_cliente.title("Criar cliente")
    tk.Label(adicionar_cliente, text="Nome:").grid(row=0, column=0)
    tk.Label(adicionar_cliente, text="Morada:").grid(row=1, column=0)
    tk.Label(adicionar_cliente, text="NIF:").grid(row=2, column=0)
    tk.Label(adicionar_cliente, text="Número de telefone:").grid(row=3, column=0)
    tk.Label(adicionar_cliente, text="Email:").grid(row=4, column=0)
    eName = tk.Entry(adicionar_cliente)
    eAddress = tk.Entry(adicionar_cliente)
    def validar9char(P):
        if len(P) > 9:
            return False
        else:
            return True
    valNif = (adicionar_cliente.register(validar9char), "%P")
    eNif = tk.Entry(adicionar_cliente, validate="key", validatecommand=valNif)
    valMobile = (adicionar_cliente.register(validar9char), "%P")
    eMobile = tk.Entry(adicionar_cliente, validate="key", validatecommand=valMobile)
    eMail = tk.Entry(adicionar_cliente)
    eName.grid(row=0, column=1)
    eAddress.grid(row=1, column=1)
    eNif.grid(row=2, column=1)
    eMobile.grid(row=3, column=1)
    eMail.grid(row=4, column=1)
    def adicionar():
        name = eName.get()
        address = eAddress.get()
        nif = eNif.get()
        mobile = eMobile.get()
        mail = eMail.get()
        if name and address and nif and mobile and mail:
            create_client(name, address, nif, mobile, mail)
            messagebox.showinfo("Sucesso", "Utilizador criado com sucesso!")
            adicionar_cliente.destroy()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    tk.Button(adicionar_cliente, text="Adicionar", command=adicionar).grid(row=5, columnspan=2)
    adicionar_cliente.mainloop()