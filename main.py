import tkinter as tk
from tkinter import PhotoImage
from src.database.database import *
from users import *
from login_ui import login_ui

try:
    connect()
except:
    create_db()

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
# nao abre a pagina de login
menu_utilizadores.add_command(label="Login", command=login_ui)
menu_utilizadores.add_command(label="Remover", command=delete_user)

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
menu_pagamentos.add_command(label="Adicionar")
menu_pagamentos.add_command(label="Remover")

menu_bar.add_command(label="Sair", command=sair)

root.config(menu=menu_bar)

logo = PhotoImage(file="assets/logo.png")
label_logo = tk.Label(root, image=logo, bg="#1f286d")
label_logo.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()
