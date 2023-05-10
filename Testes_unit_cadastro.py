import unittest
from tkinter import Tk, Entry, messagebox
from Tela_cadastro import validar_email, validar_nome, validar_telefone

class TestCadastro(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.root.withdraw()
        self.input_nome = Entry(self.root)
        self.input_email = Entry(self.root)
        self.input_telefone = Entry(self.root)

    def test_validar_nome(self):
        self.input_nome.insert(0, "Osvaldo Crocodilo")
        self.assertTrue(validar_nome())

        self.input_nome.insert(0, "Wesley crocodilo")
        self.assertFalse(validar_nome())

    def test_validar_email(self):
        self.input_email.insert(0, "osvaldo.crocodilo@gmail.com")
        self.assertTrue(validar_email())

        self.input_email.insert(0, "osvaldo.crocodilo")
        self.assertFalse(validar_email())

    def test_validar_telefone(self):
        self.input_telefone.insert(0, "123456")
        self.assertTrue(validar_telefone())

        self.input_telefone.insert(0, "12345a6")
        self.assertFalse(validar_telefone())

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()