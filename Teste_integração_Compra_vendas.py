import unittest
import tkinter as tk
from tkinter import messagebox
from Compras_Vendas import *
class TestCompraProduto(unittest.TestCase):
    def setUp(self):

        self.janela = tk.Tk()
        self.janela.geometry('300x220')
        self.janela.title('Compra e Venda de Produtos')

        self.entrada_nome = tk.Entry(self.janela)
        self.entrada_quantidade = tk.Entry(self.janela)
        self.entrada_preco = tk.Entry(self.janela)
        self.botao_compra = tk.Button(self.janela, text='Comprar', command=self.comprar_produto)
        self.botao_venda = tk.Button(self.janela, text='Vender', command=self.vender_produto)

        self.produtos = {}

    def tearDown(self):
        self.janela.destroy()

    def comprar_produto(self):
        nome = self.entrada_nome.get()
        quantidade = int(self.entrada_quantidade.get())
        preco = float(self.entrada_preco.get())
        
        if nome not in self.produtos:
            self.produtos[nome] = {'quantidade': 0, 'preco': preco}
        
        self.produtos[nome]['quantidade'] += quantidade
        
        if preco != self.produtos[nome]['preco']:
            self.produtos[nome]['preco'] = preco
        
        tk.messagebox.showinfo('Ação realizada', f'Produto {nome} comprado: {abs(quantidade)} unidades a R$ {preco} reais')

    def test_comprar_produto(self):

        self.entrada_nome.insert(0, 'Arroz')
        self.entrada_quantidade.insert(0, '5')
        self.entrada_preco.insert(0, '10.0')
        
        self.botao_compra.invoke()
 
        self.assertEqual(tk.messagebox._show_called, {'message': 'Produto Arroz comprado: 5 unidades a R$ 10.0 reais', 'title': 'Ação realizada', 'type': 'ok'})

        self.assertEqual(self.produtos, {'Arroz': {'quantidade': 5, 'preco': 10.0}})

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)