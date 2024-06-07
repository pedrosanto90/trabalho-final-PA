# Importação dos módulos e bibliotecas
import tkinter as tk
from tkinter import ttk
from src.database.payments import *
from tkinter import messagebox


# Função para finalizar um pagamento
def finish_payment():
    # Cria uma nova janela para finalizar o pagamento
    finalizar_pagamento = tk.Toplevel()
    finalizar_pagamento.title("Finalizar pagamento")

    # Adiciona uma label e uma caixa de entrada para o ID do serviço
    tk.Label(finalizar_pagamento, text="ID serviço:").grid(row=0, column=0)
    eId = tk.Entry(finalizar_pagamento)
    eId.grid(row=0, column=1)

    def procurar():
        # Obtém o ID do serviço inserido pelo utilizador
        id = eId.get()
        if id:
            # Verifica se o pagamento é válido
            if verify_payment(id):
                # Se o pagamento for válido, cria uma nova janela para selecionar o método de pagamento
                pedir_metodo = tk.Toplevel()
                pedir_metodo.title("Método de pagamento")

                # Adiciona uma label e uma combobox para selecionar o método de pagamento
                tk.Label(pedir_metodo, text="Método de pagamento:").grid(row=0, column=0)
                eMetodo = ttk.Combobox(pedir_metodo, values=["Numerário", "Multibanco", "MB Way", "Apple Pay",
                                                             "Transferencia Bancária", "Cheque"])
                eMetodo.grid(row=0, column=1)

                def guardar():
                    # Obtém o método de pagamento selecionado
                    metodo = eMetodo.get()
                    if metodo:
                        # Atualiza o pagamento com o método selecionado e exibe uma mensagem de sucesso
                        update_payment(id, metodo)
                        messagebox.showinfo("Sucesso", "Pagamento finalizado com sucesso!")

                        # Fecha as janelas
                        pedir_metodo.destroy()
                        finalizar_pagamento.destroy()
                    else:
                        # Exibe uma mensagem de erro se o método de pagamento não for selecionado
                        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

                # Adiciona um botão para guardar o método de pagamento selecionado
                tk.Button(pedir_metodo, text="Guardar", command=guardar).grid(row=4, columnspan=2)
                pedir_metodo.mainloop()
            else:
                # Exibe uma mensagem de erro se o ID do serviço não for válido
                messagebox.showerror("Erro", "Serviço não existe.")
        else:
            # Exibe uma mensagem de erro se o ID do serviço não for preenchido
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    # Adiciona um botão para procurar o ID do serviço
    tk.Button(finalizar_pagamento, text="Procurar", command=procurar).grid(row=3, columnspan=2)
    finalizar_pagamento.mainloop()


# Função para listar todos os pagamentos
def list_all_payments():
    # Cria uma nova janela para listar todos os pagamentos
    listar_pagamentos = tk.Toplevel()
    listar_pagamentos.title("Lista de Pagamentos")

    # Adiciona cabeçalhos para a tabela de pagamentos
    tk.Label(listar_pagamentos, text="ID Serviço").grid(row=0, column=0)
    tk.Label(listar_pagamentos, text="Data").grid(row=0, column=1)
    tk.Label(listar_pagamentos, text="Valor").grid(row=0, column=2)
    tk.Label(listar_pagamentos, text="Estado").grid(row=0, column=3)
    tk.Label(listar_pagamentos, text="Tipo de Pagamento").grid(row=0, column=4)

    # Obtém a lista de pagamentos
    payments = list_payments()

    if not payments:
        # Exibe uma mensagem de informação se não houver pagamentos para mostrar
        messagebox.showinfo("Info", "Não há pagamentos para mostrar.")
        listar_pagamentos.destroy()
        return

    # Popula a tabela com os dados dos pagamentos
    for i, element in enumerate(payments, start=1):
        service_id, date, value, state, typePayment = element
        tk.Label(listar_pagamentos, text=service_id).grid(row=i, column=0)
        tk.Label(listar_pagamentos, text=date).grid(row=i, column=1)
        tk.Label(listar_pagamentos, text=value).grid(row=i, column=2)
        tk.Label(listar_pagamentos, text=state).grid(row=i, column=3)
        tk.Label(listar_pagamentos, text=typePayment).grid(row=i, column=4)

    listar_pagamentos.mainloop()
