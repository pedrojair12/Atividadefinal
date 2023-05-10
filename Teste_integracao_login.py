
import unittest
from tkinter import Tk, Entry, Button
from tkinter.messagebox import _show as messagebox_show

from Tela_login import *


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.root.geometry("260x120")
        self.root.title("Login")

        # labels
        self.nome_label = Label(self.root, text="Nome: ")
        self.email_label = Label(self.root, text="Email: ")

        # inputs
        self.input_nome = Entry(self.root)
        self.input_email = Entry(self.root)

        # posicionar inputs na tela
        self.input_nome.grid(row=0, column=1)
        self.input_email.grid(row=1, column=1)

        # botão para fazer login
        self.botao_login = Button(self.root, text="Entrar", command=fazer_login)
        self.botao_login.grid(row=3, column=1)

    def test_interface(self):
        self.assertEqual(self.nome_label['text'], 'Nome: ')
        self.assertEqual(self.email_label['text'], 'Email: ')

    def test_login_sucesso(self):
        self.input_nome.insert(0, 'João')
        self.input_email.insert(0, 'joao@gmail.com')
        self.botao_login.invoke()
        self.assertEqual(messagebox_show.call_args[0][1], "Bem-vindo, João!")
        self.root.destroy()

    def test_login_falha(self):
        self.input_nome.insert(0, 'gabriel')
        self.input_email.insert(0, 'gabriel@gmail.com')
        self.botao_login.invoke()
        self.assertEqual(messagebox_show.call_args[0][1], "Usuário não encontrado ou informações de login incorretas.")
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()