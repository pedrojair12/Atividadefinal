import tkinter as tk
from tkinter import messagebox

# Cria a janela principal
janela = tk.Tk()

# Define o tamanho da janela principal
janela.geometry('300x220')

# Define o título da janela principal
janela.title('Compra e Venda de Produtos')

# Dicionário para armazenar a quantidade e preço de cada produto
produtos = {}

# Cria os rótulos e entradas para o nome do produto
label_nome = tk.Label(janela, text='Nome do Produto')
label_nome.pack()

entrada_nome = tk.Entry(janela)
entrada_nome.pack()

# Cria os rótulos e entradas para a quantidade do produto
label_quantidade = tk.Label(janela, text='Quantidade')
label_quantidade.pack()

entrada_quantidade = tk.Entry(janela)
entrada_quantidade.pack()

# Cria os rótulos e entradas para o preço do produto
label_preco = tk.Label(janela, text='Preço')
label_preco.pack()

entrada_preco = tk.Entry(janela)
entrada_preco.pack()

# Cria o botão de compra
def comprar_produto():
    nome = entrada_nome.get()
    quantidade = int(entrada_quantidade.get())
    preco = float(entrada_preco.get())
    
    if nome not in produtos:
        produtos[nome] = {'quantidade': 0, 'preco': preco}
    
    produtos[nome]['quantidade'] += quantidade
    
    # Atualiza o preço se o preço do produto mudar
    if preco != produtos[nome]['preco']:
        produtos[nome]['preco'] = preco
    
    tk.messagebox.showinfo('Ação realizada', f'Produto {nome} comprado: {abs(quantidade)} unidades a R$ {preco} reais')
    
botao_compra = tk.Button(janela, text='Comprar', command=comprar_produto)
botao_compra.pack()

# Cria o botão de venda
def vender_produto():
    nome = entrada_nome.get()
    quantidade = int(entrada_quantidade.get())
    preco = float(entrada_preco.get())
    
    if nome not in produtos:
        tk.messagebox.showinfo('Ação não realizada', f'Produto {nome} não encontrado.')
        return
    
    if quantidade > produtos[nome]['quantidade']:
        tk.messagebox.showinfo('Ação não realizada', f'Não há unidades suficientes do produto {nome}.')
        return
    
    acao = 'vendido' if quantidade > 0 else 'comprado'
    
    produtos[nome]['quantidade'] -= quantidade
    
    tk.messagebox.showinfo('Ação realizada', f'Produto {nome} {acao}: {abs(quantidade)} unidades a R$ {preco:.2f} reais')

    

botao_venda = tk.Button(janela, text='Vender', command=vender_produto)
botao_venda.pack()

# Inicia a janela principal
janela.mainloop()
