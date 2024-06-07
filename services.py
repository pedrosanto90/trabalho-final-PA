# Importação dos módulos e bibliotecas
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from src.database.services import *
from src.database.clients import verify_client


# Função para criar a página de criação de serviços
def create_service_page():
    # Cria uma nova janela para criar um serviço
    add_window = tk.Toplevel()
    add_window.title("Começar Serviço")

    # Define os rótulos e os campos de entrada para a criação de serviços
    labels = ["Cliente", "Tipo de serviço", "Descrição", "Preço"]
    entries = []
    for i, label in enumerate(labels):
        tk.Label(add_window, text=label).grid(row=i, column=0)
        if label == "Tipo de serviço":
            entry = ttk.Combobox(add_window, values=["Manutenção", "Colisão"])
        elif label == "Preço":
            entry = tk.Entry(add_window)
            entry.insert(0, "0.0")  # Define o valor inicial como 0.0
        else:
            entry = tk.Entry(add_window)
        entry.grid(row=i, column=1)
        entries.append(entry)

    # Função chamada ao submeter o formulário
    def on_submit():
        client_id = entries[0].get().strip()
        service_type = entries[1].get().strip()
        description = entries[2].get().strip()
        price = entries[3].get().strip()

        # Verifica se todos os campos foram preenchidos
        if not client_id or not service_type or not description or not price:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        # Verifica se o tipo de serviço é válido
        if service_type not in ["Manutenção", "Colisão"]:
            messagebox.showerror("Erro", "Tipo de serviço inválido.")
            return

        # Verifica se o preço é um valor numérico válido
        try:
            price = float(price)
            if price < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Preço inválido.")
            return

        # Verifica se o ID do cliente existe
        if verify_client(client_id):
            try:
                # Cria o serviço na base de dados
                create_service(client_id, service_type, description, price)
                messagebox.showinfo("Sucesso", "Serviço criado com sucesso!")
                add_window.destroy()
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao criar serviço: {e}")
        else:
            messagebox.showerror("Erro", "ID do cliente não existe.")

    # Botão para submeter o formulário
    tk.Button(add_window, text="Começar", command=on_submit).grid(row=len(labels), column=1)
    add_window.mainloop()


# Função para criar a página de atualização de serviços
def update_service_page():
    # Cria uma nova janela para atualizar um serviço
    update_window = tk.Toplevel()
    update_window.title("Finalizar Serviço")

    # Rótulo e campo de entrada para o ID do serviço
    tk.Label(update_window, text="ID do serviço:").grid(row=0, column=0)
    eId = tk.Entry(update_window)
    eId.grid(row=0, column=1)

    # Função chamada ao clicar no botão "Terminar"
    def terminar():
        service_id = eId.get().strip()
        if service_id:
            try:
                # Atualiza o serviço na base de dados
                update_service(service_id)
                messagebox.showinfo("Sucesso", "Serviço finalizado com sucesso!")
                update_window.destroy()
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao finalizar serviço: {e}")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    # Botão para finalizar o serviço
    tk.Button(update_window, text="Terminar", command=terminar).grid(row=3, columnspan=2)
    update_window.mainloop()


# Função para criar a página de listagem de serviços
def list_service_page():
    # Cria uma nova janela para listar todos os serviços
    list_window = tk.Toplevel()
    list_window.title("Lista de Serviços")

    # Rótulo e campo de entrada para filtrar serviços por data
    tk.Label(list_window, text="Filtrar por data:").grid(row=0, column=2, columnspan=3)
    date_entry = DateEntry(list_window, date_pattern="dd/mm/yyyy")
    date_entry.grid(row=0, column=4, columnspan=4)
    tk.Button(list_window, text="Filtrar", command=lambda: filter_services(date_entry.get_date())).grid(row=0, column=6, columnspan=3)

    # Definir colunas para a listagem de serviços
    columns = ["ID", "ID Cliente", "Tipo", "Descrição", "Data de início", "Data de fim", "Estado"]
    for i, column in enumerate(columns):
        tk.Label(list_window, text=column).grid(row=1, column=i)

    # Função para filtrar e listar os serviços com base na data
    def filter_services(date):
        # Limpar listagem existente
        for widget in list_window.grid_slaves():
            if int(widget.grid_info()["row"]) > 1:
                widget.grid_forget()

        # Obter lista de serviços filtrada por data
        services = list_services_by_date(date)
        if not services:
            messagebox.showinfo("Info", "Não há serviços para mostrar.")
            return

        # Exibir os serviços filtrados
        for i, element in enumerate(services, start=2):
            id, client, type, desc, date_inic, date_fim, state = element
            tk.Label(list_window, text=id).grid(row=i, column=0)
            tk.Label(list_window, text=client).grid(row=i, column=1)
            tk.Label(list_window, text=type).grid(row=i, column=2)
            tk.Label(list_window, text=desc).grid(row=i, column=3)
            tk.Label(list_window, text=date_inic).grid(row=i, column=4)
            tk.Label(list_window, text=date_fim).grid(row=i, column=5)
            tk.Label(list_window, text=state).grid(row=i, column=6)

    list_window.mainloop()
