import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from src.database.services import *

def create_service_page():
    add_window = tk.Toplevel()
    add_window.title("Adicionar Serviço")

    labels = ["Cliente", "Tipo de serviço", "Descrição", "Início", "Fim", "Estado", "Preço"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(add_window, text=label).grid(row=i, column=0, padx=10, pady=5)
        if label in ["Início", "Fim"]:
            entry = DateEntry(add_window, date_pattern="dd/mm/yyyy")
        else:
            entry = tk.Entry(add_window)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    def on_submit():
        values = [entry.get_date() if isinstance(entry, DateEntry) else entry.get() for entry in entries]
        try:
            create_service(*values)
            messagebox.showinfo("Sucesso", "Serviço criado com sucesso!")
            add_window.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao criar serviço: {e}")

    tk.Button(add_window, text="Enviar", command=on_submit).grid(row=len(labels), column=1, pady=10)

def update_service_page():
    update_window = tk.Toplevel()
    update_window.title("Atualizar Serviço")

    tk.Label(update_window, text="Service ID").grid(row=0, column=0, padx=10, pady=5)
    service_id_entry = tk.Entry(update_window)
    service_id_entry.grid(row=0, column=1, padx=10, pady=5)

    labels = ["Cliente", "Tipo de serviço", "Descrição", "Início", "Fim", "Estado", "Preço"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(update_window, text=label).grid(row=i + 1, column=0, padx=10, pady=5)
        if label in ["Início", "Fim"]:
            entry = DateEntry(update_window, date_pattern="dd/mm/yyyy")
        else:
            entry = tk.Entry(update_window)
        entry.grid(row=i + 1, column=1, padx=10, pady=5 + len(labels))  # Ajuste na coluna
        entries.append(entry)

    def search_service():
        service_id = service_id_entry.get()
        try:
            service = get_service_by_id(service_id)
            if service:
                for i, key in enumerate(["service_client_id", "service_type", "service_description", "service_start_date", "service_end_date", "service_state", "service_price"]):
                    entry = entries[i]
                    entry.delete(0, tk.END)
                    value = service[key]
                    if isinstance(entry, DateEntry):
                        entry.set_date(value)
                    else:
                        entry.insert(0, value)
            else:
                messagebox.showinfo("Erro", "Serviço não encontrado")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao procurar o serviço: {e}")

    def on_submit():
        values = [entry.get_date() if isinstance(entry, DateEntry) else entry.get() for entry in entries]
        values.append(service_id_entry.get())  # Adiciona o ID do serviço aos valores para a função de atualização
        try:
            rows_affected = update_service(*values)
            if rows_affected > 0:
                messagebox.showinfo("Sucesso", "Serviço atualizado com sucesso!")
            else:
                messagebox.showinfo("Erro", "Nenhum serviço foi atualizado")
            update_window.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao atualizar serviço: {e}")

    tk.Button(update_window, text="Pesquisar", command=search_service).grid(row=0, column=2, padx=10, pady=5)
    tk.Button(update_window, text="Atualizar", command=on_submit).grid(row=len(labels) + 1, column=1, pady=10)


def delete_service_page():
    delete_window = tk.Toplevel()
    delete_window.title("Apagar Serviço")

    tk.Label(delete_window, text="Service ID").grid(row=0, column=0, padx=10, pady=5)
    service_id_entry = tk.Entry(delete_window)
    service_id_entry.grid(row=0, column=1, padx=10, pady=5)

    def on_submit():
        service_id = service_id_entry.get()
        try:
            rows_affected = delete_service(service_id)
            if rows_affected > 0:
                messagebox.showinfo("Sucesso", "Serviço apagado com sucesso!")
            else:
                messagebox.showinfo("Erro", "Nenhum serviço foi apagado")
            delete_window.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao apagar serviço: {e}")

    tk.Button(delete_window, text="Apagar", command=on_submit).grid(row=1, column=1, pady=10)

def show_services_by_date():
    show_window = tk.Toplevel()
    show_window.title("Mostrar Serviços por Data")
    show_window.geometry("600x400")

    tk.Label(show_window, text="Selecione a Data").pack(pady=10)
    date_entry = DateEntry(show_window, date_pattern="dd/mm/yyyy")
    date_entry.pack(pady=10)

    results_text = tk.Text(show_window, width=70, height=20)
    results_text.pack(pady=10)

    def on_date_select():
        selected_date = date_entry.get_date().strftime('%Y-%m-%d')
        try:
            services = get_services_by_date(selected_date)
            results_text.delete(1.0, tk.END)
            if services:
                for service in services:
                    service_info = f"""
Service ID: {service['service_id']}
Tipo de Serviço: {service['service_type']}
Descrição: {service['service_description']}
Início: {service['service_start_date']}
Fim: {service['service_end_date']}
State: {service['service_state']}
Preço: {service['service_price']}
Data de Criação: {service['service_created']}
"""
                    results_text.insert(tk.END, service_info)
                    results_text.insert(tk.END, "\n" + "-"*40 + "\n")
            else:
                results_text.insert(tk.END, "Não há serviços nesta data")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao buscar serviços: {e}")

    tk.Button(show_window, text="Mostrar Serviços", command=on_date_select).pack(pady=10)