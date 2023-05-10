import unittest
from tkinter import *
from tkinter import messagebox
import re
from Tela_cadastro import *

class TestValidarEmail(unittest.TestCase):
    def test_validar_email_valido(self):
        root = Tk()
        input_email = Entry(root)
        input_email.insert(0, "Crocodilo@gmail.com")
        result = validar_email(input_email)
        self.assertTrue(result)

    def test_validar_email_invalido(self):
        root = Tk()
        input_email = Entry(root)
        input_email.insert(0, "Crocodilo")
        result = validar_email(input_email)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
