from tkinter import *
from tkinter import messagebox
import re

root = Tk()
root.geometry("260x180")
root.title("Cadastro")

# labels
Label(root, text="Nome completo: ").grid(row=0, column=0)
Label(root, text="Email: ").grid(row=1, column=0)

# inputs
input_nome = Entry(root)
input_email = Entry(root)

# posicionar inputs na tela
input_nome.grid(row=0, column=1)
input_email.grid(row=1, column=1)

# função para validar as informações de login
def fazer_login():
    usuario_cadastrado = {"Joao Silva": "joao@gmail.com", "Maria Souza": "maria@gmail.com", "Pedro": "pedro@gmail.com"}

    nome = input_nome.get()
    email = input_email.get()

    if nome+" "+email in usuario_cadastrado:
        messagebox.showinfo("Sucesso", f"Usuário {nome} fez login com êxito!")
        root.quit()
    else:
        messagebox.showerror("Erro", "Usuário não encontrado ou informações de login incorretas.")

# botão para fazer login
Button(root, text="Entrar", command=fazer_login).grid(row=2, column=1)

# função para validar o e-mail com @
def validar_email():
    email = input_email.get()
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Houve um erro", "O endereço de e-mail é inválido!")
        input_email.delete(0, END)
        input_email.focus()
        return False
    return True

# função para validar o nome
def validar_nome():
    nome = input_nome.get()
    if not nome.replace(" ", "").isalpha():
        messagebox.showerror("Houve um erro", "Nesse campo só é aceito letras e espaços")
        input_nome.delete(0, END)
        input_nome.focus()
        return False
    return True

# labels
Label(root, text="Telefone: ").grid(row=2, column=0)

# input
input_telefone = Entry(root)

# posicionar input na tela
input_telefone.grid(row=2, column=1)

# função para validar o telefone
def validar_telefone():
    telefone = input_telefone.get()
    if not telefone.isdigit():
        messagebox.showerror("Houve um erro", "Por favor, nesse campo só é aceito números")
        input_telefone.delete(0, END)
        input_telefone.focus()
        return False
    return True

# função para salvar dados
def salvar():
    valido = True
    if not validar_nome():
        valido = False
    if not validar_email():
        valido = False
    if not validar_telefone():
        valido = False

    if valido:
        nome = input_nome.get()
        email = input_email.get()
        telefone = input_telefone.get()

        # salvar em um arquivo, banco de dados, etc.
        print(f"Nome: {nome}, Email: {email}, Telefone: {telefone} foi cadastrado com êxito!")
        root.quit()
    else:
        messagebox.showerror("Houve um erro", "Não foi possível fazer o cadastro, verifique se pôs alguma informação incorreta")

# botão para salvar dados
Button(root, text="Salvar", command=salvar).grid(row=3, column=1)

root.mainloop()
