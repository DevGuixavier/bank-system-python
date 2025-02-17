import datetime
from users import contas, LIMITE_SAQUES, LIMITE_VALOR_SAQUE  # Importa o dicionário de contas

# Constantes de erro
VALOR_INVALIDO = "Valor inválido!"
LIMITE_SAQUE_EXCEDIDO = "Valor do saque excede o limite!"
SALDO_INSUFICIENTE = "Saldo insuficiente!"
LIMITE_SAQUES_EXCEDIDO = "Número máximo de saques excedido!"

usuarios = []  # Aqui fica a lista de usuários, não mexemos

def formatar_data():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def criar_usuario(nome, cpf, data_nascimento, endereco):
    usuario = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }
    usuarios.append(usuario)
    return usuario

def criar_conta(usuario):
    conta = {
        "usuario": usuario,
        "saldo": 0,
        "extrato": "",
        "numero_saques": 0
    }
    contas[usuario] = conta  # Alterei para armazenar a conta no dicionário de contas
    return conta

def listar_usuarios():
    return usuarios

def listar_contas():
    return contas

def encontrar_conta(usuario):
    return contas.get(usuario)  # Usando o método get() para procurar a conta diretamente no dicionário

def depositar(usuario, valor):
    conta = encontrar_conta(usuario)
    if conta and valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"{formatar_data()} - Depósito: R$ {valor:.2f}\n"
        return True
    return False

def sacar(usuario, valor):
    conta = encontrar_conta(usuario)
    if not conta:
        return "Conta não encontrada!"
    
    if valor <= 0:
        return VALOR_INVALIDO
    if valor > LIMITE_VALOR_SAQUE:
        return LIMITE_SAQUE_EXCEDIDO
    if valor > conta["saldo"]:
        return SALDO_INSUFICIENTE
    if conta["numero_saques"] >= LIMITE_SAQUES:
        return LIMITE_SAQUES_EXCEDIDO
    
    conta["saldo"] -= valor
    conta["extrato"] += f"{formatar_data()} - Saque: R$ {valor:.2f}\n"
    conta["numero_saques"] += 1
    return True

def exibir_extrato(usuario):
    conta = encontrar_conta(usuario)
    if not conta:
        return "Conta não encontrada!"
    
    extrato = conta["extrato"]
    saldo_atual = conta["saldo"]
    return f"{extrato}\nSaldo atual: R$ {saldo_atual:.2f}" if extrato else "Nenhuma movimentação registrada."
