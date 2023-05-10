from tkinter import *
from tkinter import messagebox
import re 

root = Tk()
root.geometry("260x120")
root.title("Login")

# labels
Label(root, text="Nome: ").grid(row=0, column=0)
Label(root, text="Email: ").grid(row=1, column=0)

# inputs
input_nome = Entry(root)
input_email = Entry(root)

# posicionar inputs na tela
input_nome.grid(row=0, column=1)
input_email.grid(row=1, column=1)

# função para validar as informações de login
def fazer_login():
    usuarios = [("João", "joao@gmail.com"), ("Maria", "maria@gmail.com"), ("Pedro", "pedro@gmail.com")]

    nome = input_nome.get()
    email = input_email.get()

    # verificar se as informações de login estão corretas
    if (nome, email) in usuarios:
        messagebox.showinfo("Sucesso", f"Bem-vindo, {nome}!")
        root.quit()
    else:
        messagebox.showerror("Erro", "Usuário não encontrado ou informações de login incorretas.")

# botão para fazer login
Button(root, text="Entrar", command=fazer_login).grid(row=3, column=1)

root.mainloop()
