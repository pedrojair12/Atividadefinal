import unittest
from tkinter import *
from tkinter import messagebox
import re
from Tela_login import fazer_login 

class TestLogin(unittest.TestCase):

    def test_login_sucesso(self):
        root = Tk()
        root.geometry("260x120")
        root.title("Login")

        input_nome = Entry(root)
        input_email = Entry(root)

        input_nome.insert(0, "crocodilo")
        input_email.insert(0, "crocodilo@gmail.com")

        fazer_login()

        self.assertEqual(messagebox.showinfo.call_args[0][1], "Bem-vindo, crocodilo!")

if __name__ == '__main__':
    unittest.main()
