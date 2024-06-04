from datetime import datetime
import tkinter as tk
from tkinter import ttk
from src.database.payments import *

def add_payment():
    adicionar_pagamento = tk.Toplevel()
    adicionar_pagamento.title("Criar pagamento")
    tk.Label(adicionar_pagamento, text="Valor:").grid(row=0, column=0)
    tk.Label(adicionar_pagamento, text="Estado:").grid(row=1, column=0)
    tk.Label(adicionar_pagamento, text="Tipo de Pagamento:").grid(row=2, column=0)
    eValue = tk.Entry(adicionar_pagamento)
    eState = ttk.Combobox(adicionar_pagamento, values=["Por Prestações","Completo"])
    eType = ttk.Combobox(adicionar_pagamento, values=["Numerário", "Multibanco", "MB Way", "Apple Pay", "Transferencia Bancária", "Cheque"])
    eValue.grid(row=0, column=1)
    eState.grid(row=1, column=1)
    eType.grid(row=2, column=1)

    def adicionar():
        value = eValue.get()
        typePayment = eType.get()
        state = eState.get()
        date = datetime.now()
        create_payment(date, value, state, typePayment)

    tk.Button(adicionar_pagamento, text="Adicionar", command=adicionar).grid(row=3, columnspan=2)
    adicionar_pagamento.mainloop()

def list_all_payments():
    listar_pagamentos = tk.Toplevel()
    listar_pagamentos.title("Lista de Pagamentos")

    tk.Label(listar_pagamentos, text="Data").grid(row=0, column=0)
    tk.Label(listar_pagamentos, text="Valor").grid(row=0, column=1)
    tk.Label(listar_pagamentos, text="Estado").grid(row=0, column=2)
    tk.Label(listar_pagamentos, text="Tipo de Pagamento").grid(row=0, column=3)

    payments = list_payments()

    for i, payment in enumerate(payments, start=1):
        date, value, state, typePayment = payment
        tk.Label(listar_pagamentos, text=date).grid(row=i, column=0)
        tk.Label(listar_pagamentos, text=value).grid(row=i, column=1)
        tk.Label(listar_pagamentos, text=state).grid(row=i, column=2)
        tk.Label(listar_pagamentos, text=typePayment).grid(row=i, column=3)

    listar_pagamentos.mainloop()

