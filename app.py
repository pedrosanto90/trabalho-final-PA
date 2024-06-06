#from src.faceRec import *
from src.database.database import *
from main import *
from src.database.users import create_user

try:
    connect()
except:
    create_db()
    create_tables()
    create_user("admin", "Admin", "admin", "Admin")

def admin():
    admin_login = tk.Toplevel()
    admin_login.title("Login Adminstrador")
    tk.Label(admin_login, text="Nome de utilizador:").grid(row=0, column=0)
    tk.Label(admin_login, text="Password:").grid(row=1, column=0)
    eUsername = tk.Entry(admin_login)
    ePassword = tk.Entry(admin_login, show="*")
    eUsername.grid(row=0, column=1)
    ePassword.grid(row=1, column=1)
    def aLogin():
        username = eUsername.get()
        password = ePassword.get()
        if username and password:
            if login(username, password):
                messagebox.showinfo("Sucesso", "Login efetuado com sucesso!")
                admin_login.destroy()
                root.destroy()
                main_window("Admin")
            else:
                messagebox.showerror("Erro", "Nome de utilizador ou palavra-passe incorretos.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    tk.Button(admin_login, text="Login", command=aLogin).grid(row=4, columnspan=2)
    admin_login.mainloop()

root = tk.Tk()
root.title("Norauto - Login")
root.geometry("600x400")
root.configure(bg="#1f286d")

logo = PhotoImage(file="assets/logo.png")

canvas = tk.Canvas(root, width=logo.width(), height=logo.height(), bg="#1f286d", highlightthickness=0)
canvas.pack(expand=True)
canvas.create_image(0, 0, anchor="nw", image=logo)

#button_login = tk.Button(root, text="Login", command=faceRec)
button_admin_login = tk.Button(root, text="Admin Login", command=admin)

#button_window = canvas.create_window(logo.width() // 2, (logo.height() // 2) + 125, anchor="center", window=button_login)
button_window_admin_login = canvas.create_window(logo.width() // 2, (logo.height() // 2) + 160, anchor="center", window=button_admin_login)

root.mainloop()