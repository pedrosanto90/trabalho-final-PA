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
        create_payment(date,value,state,typePayment)

    tk.Button(adicionar_pagamento, text="Adicionar", command=adicionar).grid(row=3, columnspan=2)
    adicionar_pagamento.mainloop()

def delete_payment():
    remover_pagamento = tk.Toplevel()
    remover_pagamento.title("Eliminar Pagamento")
    tk.Label(remover_pagamento, text="Nº do Pagamento:").grid(row=0, column=0)
    eNumber = tk.Entry(remover_pagamento)
    eNumber.grid(row=0, column=1)
    def remover():
        pass
    tk.Button(remover_pagamento, text="Remover", command=remover).grid(row=3, columnspan=2)
    remover_pagamento.mainloop()
