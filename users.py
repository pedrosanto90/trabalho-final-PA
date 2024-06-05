from src.database.users import *
from src.takePic import takePic
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

def add_user():
    adicionar_utilizador = tk.Toplevel()
    adicionar_utilizador.title("Criar utilizador")
    tk.Label(adicionar_utilizador, text="Nome de utilizador:").grid(row=0, column=0)
    tk.Label(adicionar_utilizador, text="Nome completo:").grid(row=1, column=0)
    tk.Label(adicionar_utilizador, text="Cargo:").grid(row=2, column=0)
    eName = tk.Entry(adicionar_utilizador)
    eFullName = tk.Entry(adicionar_utilizador)
    eRole = ttk.Combobox(adicionar_utilizador, values=["Admin", "Operador", "Contabilidade"])
    eName.grid(row=0, column=1)
    eFullName.grid(row=1, column=1)
    eRole.grid(row=2, column=1)
    def adicionar():
        name = eName.get()
        fullName = eFullName.get()
        role = eRole.get()
        if name and fullName and role:
            if verify_user(name):
                messagebox.showerror("Erro", "Nome de utilizador já existe.")
            else:
                if role == "Admin":
                    pedir_password = tk.Toplevel()
                    pedir_password.title("Introduza palavra-passe")
                    tk.Label(pedir_password, text="Palavra-passe:").grid(row=0, column=0)
                    tk.Label(pedir_password, text="Repita palavra-passe:").grid(row=1, column=0)
                    ePassword = tk.Entry(pedir_password, show="*")
                    eRePassword = tk.Entry(pedir_password, show="*")
                    ePassword.grid(row=0, column=1)
                    eRePassword.grid(row=1, column=1)
                    def guardar():
                        password = ePassword.get()
                        rePassword = eRePassword.get()
                        if password and rePassword:
                            if password == rePassword:
                                create_user(name, fullName, password, role)
                                messagebox.showinfo("Sucesso", "Utilizador criado com sucesso!")
                                pedir_password.destroy()
                                adicionar_utilizador.destroy()
                            else:
                                messagebox.showerror("Erro", "Palavras-passe não correspondem.")
                        else:
                            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
                    tk.Button(pedir_password, text="Guardar", command=guardar).grid(row=4, columnspan=2)
                    pedir_password.mainloop()
                else:
                    takePic(name)
                    create_user(name, fullName, "", role)
                    messagebox.showinfo("Sucesso", "Utilizador criado com sucesso!")
                    adicionar_utilizador.destroy()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    tk.Button(adicionar_utilizador, text="Adicionar", command=adicionar).grid(row=4, columnspan=2)
    adicionar_utilizador.mainloop()

def remove_user():
    remover_utilizador = tk.Toplevel()
    remover_utilizador.title("Remover utilizador")
    tk.Label(remover_utilizador, text="Nome de utilizador:").grid(row=0, column=0)
    eName = tk.Entry(remover_utilizador)
    eName.grid(row=0, column=1)
    def remover():
        name = eName.get()
        if name:
            if verify_user(name):
                delete_user(name)
                messagebox.showinfo("Sucesso", "Utilizador removido com sucesso!")
                remover_utilizador.destroy()
            else:
                messagebox.showerror("Erro", "Utilizador não existe.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    tk.Button(remover_utilizador, text="Remover", command=remover).grid(row=3, columnspan=2)
    remover_utilizador.mainloop()

def change_password():
    mudar_password = tk.Toplevel()
    mudar_password.title("Mudar palavra-passe")
    tk.Label(mudar_password, text="Nome de utilizador:").grid(row=0, column=0)
    eName = tk.Entry(mudar_password)
    eName.grid(row=0, column=1)
    def mudar():
        name = eName.get()
        if name:
            if verify_user(name):
                pedir_password = tk.Toplevel()
                pedir_password.title("Introduza palavra-passe")
                tk.Label(pedir_password, text="Palavra-passe:").grid(row=0, column=0)
                tk.Label(pedir_password, text="Repita palavra-passe:").grid(row=1, column=0)
                ePassword = tk.Entry(pedir_password, show="*")
                eRePassword = tk.Entry(pedir_password, show="*")
                ePassword.grid(row=0, column=1)
                eRePassword.grid(row=1, column=1)
                def guardar():
                    password = ePassword.get()
                    rePassword = eRePassword.get()
                    if password and rePassword:
                        if password == rePassword:
                            update_password(name, password)
                            messagebox.showinfo("Sucesso", "Palavra-passe alterada com sucesso!")
                            pedir_password.destroy()
                            mudar_password.destroy()
                        else:
                            messagebox.showerror("Erro", "Palavras-passe não correspondem.")
                    else:
                        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
                tk.Button(pedir_password, text="Guardar", command=guardar).grid(row=4, columnspan=2)
                pedir_password.mainloop()
            else:
                messagebox.showerror("Erro", "Utilizador não existe.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    tk.Button(mudar_password, text="Mudar", command=mudar).grid(row=3, columnspan=2)
    mudar_password.mainloop()

def update_photo():
    atualizar_foto = tk.Toplevel()
    atualizar_foto.title("Atualizar fotografia")
    tk.Label(atualizar_foto, text="Nome de utilizador:").grid(row=0, column=0)
    eName = tk.Entry(atualizar_foto)
    eName.grid(row=0, column=1)
    def atualizar():
        name = eName.get()
        if name:
            if verify_user(name):
                takePic(name)
                messagebox.showinfo("Sucesso", "Fotografia atualizada com sucesso!")
                atualizar_foto.destroy()
            else:
                messagebox.showerror("Erro", "Utilizador não existe.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    tk.Button(atualizar_foto, text="Atualizar", command=atualizar).grid(row=1, columnspan=2)
    atualizar_foto.mainloop()

