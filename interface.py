import tkinter as tk
from tkinter import messagebox
from banco import depositar, sacar, exibir_extrato
from users import contas

usuario_atual = None

def login():
    global usuario_atual
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    if usuario in contas and contas[usuario]["senha"] == senha:
        usuario_atual = usuario
        tela_login.destroy()
        abrir_tela_principal()
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos!")

def operacao(tipo):
    try:
        valor = float(entry_valor.get())
        if valor <= 0:
            messagebox.showerror("Erro", "Valor deve ser maior que zero!")
        else:
            if tipo == "depositar" and depositar(usuario_atual, valor):
                messagebox.showinfo("Sucesso", "Depósito realizado com sucesso!")
            elif tipo == "sacar":
                resultado = sacar(usuario_atual, valor)
                if resultado is True:
                    messagebox.showinfo("Sucesso", "Saque realizado com sucesso!")
                else:
                    messagebox.showerror("Erro", resultado)
            atualizar_saldo()
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido!")

def operacao_extrato():
    extrato_texto = exibir_extrato(usuario_atual)
    messagebox.showinfo("Extrato", extrato_texto)

def atualizar_saldo():
    label_saldo.config(text=f"Saldo: R$ {contas[usuario_atual]['saldo']:.2f}")

def abrir_tela_principal():
    global label_saldo, entry_valor, tela_principal
    
    tela_principal = tk.Tk()
    tela_principal.title("Sistema Bancário")
    tela_principal.geometry("300x300")
    
    
    tk.Label(tela_principal, text=f"Bem-vindo, {usuario_atual}!", font=("Arial", 12)).pack(pady=10)
    
    label_saldo = tk.Label(tela_principal, text=f"Saldo: R$ {contas[usuario_atual]['saldo']:.2f}", font=("Arial", 12))
    label_saldo.pack(pady=5)
    
    entry_valor = tk.Entry(tela_principal)
    entry_valor.pack(pady=5)
    
    tk.Button(tela_principal, text="Depositar", command=lambda: operacao("depositar")).pack(pady=5)
    tk.Button(tela_principal, text="Sacar", command=lambda: operacao("sacar")).pack(pady=5)
    tk.Button(tela_principal, text="Extrato", command=operacao_extrato).pack(pady=5)
    tk.Button(tela_principal, text="Sair", command=tela_principal.quit).pack(pady=10)
    
    tela_principal.mainloop()

# Tela de login
tela_login = tk.Tk()
tela_login.title("Login")
tela_login.geometry("250x200")

tk.Label(tela_login, text="Usuário: ").pack(pady=5)
entry_usuario = tk.Entry(tela_login)
entry_usuario.pack(pady=5)

tk.Label(tela_login, text="Senha: ").pack(pady=5)
entry_senha = tk.Entry(tela_login, show="*")
entry_senha.pack(pady=5)

tk.Button(tela_login, text="Entrar", command=login).pack(pady=10)

tela_login.mainloop()
