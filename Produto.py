import tkinter as tk
from tkinter import messagebox

produtos = []

class CadastroProduto:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Cadastro de Produtos')
        
        self.lbl_nome = tk.Label(janela, text='Nome:')
        self.lbl_tipo = tk.Label(janela, text='Tipo:')
        self.lbl_preco = tk.Label(janela, text='Preço:')
        
        self.entry_nome = tk.Entry(janela)
        self.entry_preco = tk.Entry(janela)
        
        self.var_tipo = tk.StringVar(janela)
        self.var_tipo.set('Selecione um tipo')
        self.opt_tipo = tk.OptionMenu(janela, self.var_tipo, 'Eletrônico', 'Roupa', 'Alimento')
        
        self.btn_cadastrar = tk.Button(janela, text='Cadastrar', command=self.cadastrar_produto)
        self.btn_remover = tk.Button(janela, text='Remover', command=self.remover_produto)
        
        self.lbl_nome.grid(row=0, column=0)
        self.entry_nome.grid(row=0, column=1)
        
        self.lbl_tipo.grid(row=1, column=0)
        self.opt_tipo.grid(row=1, column=1)
        
        self.lbl_preco.grid(row=2, column=0)
        self.entry_preco.grid(row=2, column=1)
        
        self.btn_cadastrar.grid(row=4, column=0)
        self.btn_remover.grid(row=4, column=1)
        
    def cadastrar_produto(self):
        nome = self.entry_nome.get()
        tipo = self.var_tipo.get()
        preco = float(self.entry_preco.get())
        
        if tipo == 'Eletrônico':
            produto = Eletronico(nome, preco)
        elif tipo == 'Roupa':
            produto = Roupa(nome, preco)
        elif tipo == 'Alimento':
            produto = Alimento(nome, preco)
        
        produtos.append(produto)

        messagebox.showinfo('Cadastro de Produto', 'Produto cadastrado com sucesso!')
        
        self.entry_nome.delete(0, tk.END)
        self.var_tipo.set('Selecione um tipo')
        self.entry_preco.delete(0, tk.END)
    
    
    def remover_produto(self):
        remover_janela = tk.Toplevel(self.janela)
        remover_janela.title('Remover Produto')

        lista_produtos = tk.Listbox(remover_janela)
        for produto in produtos:
            lista_produtos.insert(tk.END, str(produto))
        lista_produtos.pack(side=tk.LEFT, fill=tk.BOTH)

        btn_selecionar = tk.Button(remover_janela, text='Selecionar', command=lambda: self.selecionar_produto(lista_produtos, remover_janela))
        btn_selecionar.pack(side=tk.BOTTOM, padx=5, pady=5)

    def selecionar_produto(self, lista_produtos, remover_janela):
      selecao = lista_produtos.curselection()
      if len(selecao) == 0:
         messagebox.showerror('Remover Produto', 'Selecione um produto para remover.')
         return
      produto_selecionado = produtos.pop(selecao[0])
      lista_produtos.delete(selecao[0])
      messagebox.showinfo('Remover Produto', f'O produto {produto_selecionado.nome} foi removido com sucesso.')
      remover_janela.destroy()




class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'{self.nome} - R${self.preco:.2f}'

class Eletronico(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)
        self.garantia = 12

class Roupa(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)
        self.tamanho = 'M'

class Alimento(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)
        self.validade = '10/2023'

root = tk.Tk()
app = CadastroProduto(root)
root.mainloop()