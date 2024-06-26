# Importação dos módulos e bibliotecas
import tkinter as tk
from tkinter import ttk, messagebox
import re
from src.database.clients import create_client, delete_client, list_clients, existe_cliente, verify_client


# Função para adicionar um novo cliente
def add_client():
    adicionar_cliente = tk.Toplevel()
    adicionar_cliente.title("Criar cliente")

    # Labels e campos de entrada para os detalhes do cliente
    tk.Label(adicionar_cliente, text="Nome:").grid(row=0, column=0)
    tk.Label(adicionar_cliente, text="Morada:").grid(row=1, column=0)
    tk.Label(adicionar_cliente, text="NIF:").grid(row=2, column=0)
    tk.Label(adicionar_cliente, text="Número de telefone:").grid(row=3, column=0)
    tk.Label(adicionar_cliente, text="Email:").grid(row=4, column=0)
    eName = tk.Entry(adicionar_cliente)
    eAddress = tk.Entry(adicionar_cliente)

    # Função para validar o comprimento de 9 caracteres
    def validar9char(P):
        return len(P) <= 9

    # Configuração da validação de entrada para NIF e número de telefone
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

    # Função para validar o formato do email
    def validar_email(email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    # Função para adicionar o cliente à base de dados
    def adicionar():
        name = eName.get()
        address = eAddress.get()
        nif = eNif.get()
        mobile = eMobile.get()
        mail = eMail.get()
        if name and address and nif and mobile and mail:
            if not validar_email(mail):
                messagebox.showerror("Erro", "Email inválido.")
                return
            if not (nif.isdigit() and len(nif) == 9):
                messagebox.showerror("Erro", "NIF deve conter exatamente 9 dígitos.")
                return
            if not (mobile.isdigit() and len(mobile) == 9):
                messagebox.showerror("Erro", "Número de telefone deve conter exatamente 9 dígitos.")
                return
            if existe_cliente(nif):
                messagebox.showerror("Erro", "Cliente já existe.")
                return
            create_client(name, address, nif, mobile, mail)
            messagebox.showinfo("Sucesso", "Cliente criado com sucesso!")
            adicionar_cliente.destroy()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    # Botão para adicionar o cliente
    tk.Button(adicionar_cliente, text="Adicionar", command=adicionar).grid(row=5, columnspan=2)
    adicionar_cliente.mainloop()


# Função para remover um cliente existente
def remove_client():
    remover_cliente = tk.Toplevel()
    remover_cliente.title("Remover cliente")

    # Label e campo de entrada para o ID do cliente
    tk.Label(remover_cliente, text="ID do cliente:").grid(row=0, column=0)
    eID = tk.Entry(remover_cliente)
    eID.grid(row=0, column=1)

    # Função para remover o cliente da base de dados
    def remover():
        id = eID.get()
        if id:
            if verify_client(id):
                delete_client(id)
                messagebox.showinfo("Sucesso", "Cliente removido com sucesso!")
                remover_cliente.destroy()
            else:
                messagebox.showerror("Erro", "Cliente não existe.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    # Botão para remover o cliente
    tk.Button(remover_cliente, text="Remover", command=remover).grid(row=3, columnspan=2)
    remover_cliente.mainloop()


# Função para listar todos os clientes
def list_all_clients():
    listar_clients = tk.Toplevel()
    listar_clients.title("Lista de Clientes")

    # Labels para os cabeçalhos das colunas
    tk.Label(listar_clients, text="ID").grid(row=0, column=0)
    tk.Label(listar_clients, text="Nome").grid(row=0, column=1)
    tk.Label(listar_clients, text="Morada").grid(row=0, column=2)
    tk.Label(listar_clients, text="NIF").grid(row=0, column=3)
    tk.Label(listar_clients, text="Telefone").grid(row=0, column=4)
    tk.Label(listar_clients, text="Email").grid(row=0, column=5)
    tk.Label(listar_clients, text="Criado a").grid(row=0, column=6)

    # Obtém a lista de clientes da base de dados
    clients = list_clients()

    # Verificação se há clientes para mostrar
    if not clients:
        messagebox.showinfo("Info", "Não há clientes para mostrar.")
        listar_clients.destroy()
        return

    # Preenchimento dos dados dos clientes nas colunas correspondentes
    for i, element in enumerate(clients, start=1):
        id, name, address, nif, phone, email, created = element
        tk.Label(listar_clients, text=id).grid(row=i, column=0)
        tk.Label(listar_clients, text=name).grid(row=i, column=1)
        tk.Label(listar_clients, text=address).grid(row=i, column=2)
        tk.Label(listar_clients, text=nif).grid(row=i, column=3)
        tk.Label(listar_clients, text=phone).grid(row=i, column=4)
        tk.Label(listar_clients, text=email).grid(row=i, column=5)
        tk.Label(listar_clients, text=created).grid(row=i, column=6)

    listar_clients.mainloop()