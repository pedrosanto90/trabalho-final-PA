import tkinter as tk
from tkinter import PhotoImage
from src.database.database import *
from users import *
from payments import *

def main_window():
    def sair():
        root.quit()

    root = tk.Tk()
    root.title("Norauto")
    root.geometry("600x400")
    root.configure(bg="#1f286d")

    menu_bar = tk.Menu(root, tearoff=0)

    menu_utilizadores = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Utilizadores", menu=menu_utilizadores)
    menu_utilizadores.add_command(label="Adicionar", command=add_user)
    menu_utilizadores.add_command(label="Remover", command=remove_user)
    menu_utilizadores.add_command(label="Mudar palavra-passe", command=change_password)

    menu_clientes = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Clientes", menu=menu_clientes)
    menu_clientes.add_command(label="Adicionar")
    menu_clientes.add_command(label="Remover")

    menu_manutencoes = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Manutenções", menu=menu_manutencoes)
    menu_manutencoes.add_command(label="Adicionar")
    menu_manutencoes.add_command(label="Remover")

    menu_pagamentos = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Pagamentos", menu=menu_pagamentos)
    menu_pagamentos.add_command(label="Adicionar", command=add_payment)
    menu_pagamentos.add_command(label="Lista de Pagamentos", command=list_all_payments)

    menu_veiculos = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Veículos", menu=menu_veiculos)
    menu_veiculos.add_command(label="Adicionar")
    menu_veiculos.add_command(label="Remover")

    menu_bar.add_command(label="Sair", command=sair)

    root.config(menu=menu_bar)

    logo = PhotoImage(file="assets/logo.png")
    label_logo = tk.Label(root, image=logo, bg="#1f286d")
    label_logo.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    root.mainloop()

main_window()