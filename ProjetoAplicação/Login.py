import tkinter as tk
from tkinter import messagebox

# Dados de exemplo
usuarios = {
    'user1': {'id': 1, 'nome': 'João', 'email': 'joao@example.com', 'senha': 'senha123', 'cidade': 'São Paulo'},
    'user2': {'id': 2, 'nome': 'Maria', 'email': 'maria@example.com', 'senha': 'senha456', 'cidade': 'Rio de Janeiro'}
}
cidades = ['São Paulo', 'Rio de Janeiro']


# Função de validação de login
def validar_login(usuario, senha):
    if usuario in usuarios and usuarios[usuario]['senha'] == senha:
        return True
    return False


# Função para excluir cidade
def excluir_cidade(cidade):
    for usuario in usuarios.values():
        if usuario['cidade'] == cidade:
            messagebox.showerror("Erro", "Não é possível excluir a cidade. Está sendo usada por um cliente.")
            return
    cidades.remove(cidade)
    messagebox.showinfo("Sucesso", "Cidade excluída com sucesso.")


# Função para exibir detalhes do cadastro
def mostrar_detalhes(usuario):
    if usuario in usuarios:
        user_info = usuarios[usuario]
        detalhes = (f"ID: {user_info['id']}\n"
                    f"Nome: {user_info['nome']}\n"
                    f"Email: {user_info['email']}\n"
                    f"Usuário: {usuario}\n"
                    f"Senha: {user_info['senha']}")
        messagebox.showinfo("Detalhes do Cadastro", detalhes)
    else:
        messagebox.showerror("Erro", "Usuário não encontrado.")


# Função de exibição principal
def exibir_tela_principal():
    root = tk.Tk()
    root.title("Sistema de Cadastro")

    tk.Label(root, text="Usuário:").pack()
    usuario_entry = tk.Entry(root)
    usuario_entry.pack()

    tk.Label(root, text="Senha:").pack()
    senha_entry = tk.Entry(root, show="*")
    senha_entry.pack()

    def login():
        usuario = usuario_entry.get()
        senha = senha_entry.get()
        if validar_login(usuario, senha):
            messagebox.showinfo("Login", "Login bem-sucedido!")
            root.destroy()
            exibir_detalhes(usuario)
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos.")

    tk.Button(root, text="Login", command=login).pack()
    root.mainloop()


# Função para exibir detalhes dos usuários após o login
def exibir_detalhes(usuario):
    root = tk.Tk()
    root.title("Detalhes dos Usuários")

    for user in usuarios:
        tk.Button(root, text=user, command=lambda u=user: mostrar_detalhes(u)).pack()

    root.mainloop()


# Iniciar o programa
exibir_tela_principal()
