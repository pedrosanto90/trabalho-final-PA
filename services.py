import tkinter as tk
from tkinter import messagebox
#from database.services import create_service, update_service, delete_service

def create_service_page():
    add_window = tk.Toplevel()
    add_window.title("Adicionar Serviço")
    add_window.geometry("400x400")

    labels = ["Vehicle ID", "Type ID", "State ID", "Description", "Start Date", "End Date", "State", "Price", "Price Material"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(add_window, text=label).grid(row=i, column=0)
        entry = tk.Entry(add_window)
        entry.grid(row=i, column=1)
        entries.append(entry)

    def on_submit():
        values = [entry.get() for entry in entries]
        create_service(*values)
        messagebox.showinfo("Sucesso", "Serviço criado com sucesso!")
        add_window.destroy()

    tk.Button(add_window, text="Submit", command=on_submit).grid(row=len(labels), column=1)

def update_service_page():
    update_window = tk.Toplevel()
    update_window.title("Atualizar Serviço")
    update_window.geometry("400x450")

    labels = ["Service ID", "Vehicle ID", "Type ID", "State ID", "Description", "Start Date", "End Date", "State", "Price", "Price Material"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(update_window, text=label).grid(row=i, column=0)
        entry = tk.Entry(update_window)
        entry.grid(row=i, column=1)
        entries.append(entry)

    def on_submit():
        values = [entry.get() for entry in entries]
        update_service(*values)
        messagebox.showinfo("Sucesso", "Serviço atualizado com sucesso!")
        update_window.destroy()

    tk.Button(update_window, text="Submit", command=on_submit).grid(row=len(labels), column=1)

def delete_service_page():
    delete_window = tk.Toplevel()
    delete_window.title("Apagar Serviço")
    delete_window.geometry("300x200")

    tk.Label(delete_window, text="Service ID").grid(row=0, column=0)
    service_id_entry = tk.Entry(delete_window)
    service_id_entry.grid(row=0, column=1)

    def on_submit():
        service_id = service_id_entry.get()
        delete_service(service_id)
        messagebox.showinfo("Sucesso", "Serviço apagado com sucesso!")
        delete_window.destroy()

    tk.Button(delete_window, text="Submit", command=on_submit).grid(row=1, column=1)