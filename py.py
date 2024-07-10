import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Login", "Nome de usuário ou senha incorretos.")


root = tk.Tk()
root.title("Tela de Login")


label_username = tk.Label(root, text="Nome de usuário")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)


label_password = tk.Label(root, text="Senha")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)


login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

root.mainloop()
