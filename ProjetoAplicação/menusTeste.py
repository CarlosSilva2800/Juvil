import tkinter as tk
from tkinter import messagebox

# Funções para cada opção do menu
def opcao1():
    messagebox.showinfo("Opção 1", "Você escolheu a Opção 1")

def opcao2():
    messagebox.showinfo("Opção 2", "Você escolheu a Opção 2")

def opcao3():
    messagebox.showinfo("Opção 3", "Você escolheu a Opção 3")

def sair():
    janela.quit()

# Criando a janela principal
janela = tk.Tk()
janela.title("Tela de Menu")
janela.geometry("400x300")

# Criando o Menu
menu_bar = tk.Menu(janela)

# Menu Principal
menu_opcoes = tk.Menu(menu_bar, tearoff=0)
menu_opcoes.add_command(label="Opção 1", command=opcao1)
menu_opcoes.add_command(label="Opção 2", command=opcao2)
menu_opcoes.add_command(label="Opção 3", command=opcao3)
menu_opcoes.add_separator()
menu_opcoes.add_command(label="Sair", command=sair)

# Adicionando o menu principal à barra de menus
menu_bar.add_cascade(label="Opções", menu=menu_opcoes)

# Exibindo a barra de menu na janela
janela.config(menu=menu_bar)

# Loop da janela
janela.mainloop()
