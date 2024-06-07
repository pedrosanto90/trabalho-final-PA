from users import add_user, remove_user, change_password, update_photo
from payments import finish_payment, list_all_payments
from services import create_service_page, update_service_page, list_service_page
from clients import add_client, remove_client, list_all_clients
import tkinter as tk
from tkinter import PhotoImage
import sys

def main_window(role, user_fullname):
    root = tk.Tk()
    root.title("Norauto")
    root.geometry("600x400")
    root.configure(bg="#1f286d")

    # Configuração da barra de menu
    menu_bar = tk.Menu(root, tearoff=0)

    # Menu de Utilizadores (somente para Admin)
    if role == "Admin":
        menu_utilizadores = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Utilizadores", menu=menu_utilizadores)
        menu_utilizadores.add_command(label="Adicionar", command=add_user)
        menu_utilizadores.add_command(label="Remover", command=remove_user)
        menu_utilizadores.add_command(label="Mudar palavra-passe", command=change_password)
        menu_utilizadores.add_command(label="Atualizar fotografia", command=update_photo)

    # Menu de Clientes (para Admin e Operador)
    if role == "Admin" or role == "Operador":
        menu_clientes = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Clientes", menu=menu_clientes)
        menu_clientes.add_command(label="Adicionar", command=add_client)
        menu_clientes.add_command(label="Remover", command=remove_client)
        menu_clientes.add_command(label="Lista de Clientes", command=list_all_clients)

    # Menu de Pagamentos (para Admin e Contabilidade)
    if role == "Admin" or role == "Contabilidade":
        menu_pagamentos = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Pagamentos", menu=menu_pagamentos)
        menu_pagamentos.add_command(label="Finalizar", command=finish_payment)
        menu_pagamentos.add_command(label="Lista de Pagamentos", command=list_all_payments)

    # Menu de Serviços (para Admin e Operador)
    menu_services = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Serviços", menu=menu_services)
    if role == "Admin" or role == "Operador":
        menu_services.add_command(label="Começar", command=create_service_page)
        menu_services.add_command(label="Terminar", command=update_service_page)
    menu_services.add_command(label="Lista de Serviços", command=list_service_page)

    # Botão de Sair
    menu_bar.add_command(label="Sair", command=lambda: sys.exit())

    root.config(menu=menu_bar)

    # Configuração da logo
    logo = PhotoImage(file="assets/logo.png", master=root)
    label_logo = tk.Label(root, image=logo, bg="#1f286d")
    label_logo.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Mensagem de boas-vindas
    bem_vindo = tk.Label(root, text=f"Bem-vindo, {user_fullname}", bg="#1f286d", fg="white", font=("Helvetica", 20, "bold"))
    bem_vindo.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    root.mainloop()