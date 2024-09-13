import tkinter as tk
from tkinter import messagebox

# Dados fictícios para visualização
dados = [
    {"ID": 1, "Nome": "João", "Email": "joao@email.com", "Usuário": "joao123", "Senha": "1234"},
    {"ID": 2, "Nome": "Maria", "Email": "maria@email.com", "Usuário": "maria456", "Senha": "5678"},
    {"ID": 3, "Nome": "Pedro", "Email": "pedro@email.com", "Usuário": "pedro789", "Senha": "abcd"}
]


# Função para visualizar os dados
def visualizar_dados():
    janela_dados = tk.Toplevel()  # Cria uma nova janela
    janela_dados.title("Visualizar Dados")
    janela_dados.geometry("500x300")

    # Cabeçalhos
    tk.Label(janela_dados, text="ID", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=5)
    tk.Label(janela_dados, text="Nome", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=10, pady=5)
    tk.Label(janela_dados, text="Email", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=10, pady=5)
    tk.Label(janela_dados, text="Usuário", font=("Arial", 10, "bold")).grid(row=0, column=3, padx=10, pady=5)
    tk.Label(janela_dados, text="Senha", font=("Arial", 10, "bold")).grid(row=0, column=4, padx=10, pady=5)

    # Exibir dados
    for idx, dado in enumerate(dados):
        tk.Label(janela_dados, text=dado["ID"]).grid(row=idx + 1, column=0, padx=10, pady=5)
        tk.Label(janela_dados, text=dado["Nome"]).grid(row=idx + 1, column=1, padx=10, pady=5)
        tk.Label(janela_dados, text=dado["Email"]).grid(row=idx + 1, column=2, padx=10, pady=5)
        tk.Label(janela_dados, text=dado["Usuário"]).grid(row=idx + 1, column=3, padx=10, pady=5)
        tk.Label(janela_dados, text=dado["Senha"]).grid(row=idx + 1, column=4, padx=10, pady=5)


# Função de saída
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
menu_opcoes.add_command(label="Visualizar Dados", command=visualizar_dados)
menu_opcoes.add_separator()
menu_opcoes.add_command(label="Sair", command=sair)

# Adicionando o menu principal à barra de menus
menu_bar.add_cascade(label="Opções", menu=menu_opcoes)

# Exibindo a barra de menu na janela
janela.config(menu=menu_bar)

# Loop da janela
janela.mainloop()
