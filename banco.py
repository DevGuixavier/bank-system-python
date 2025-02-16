import datetime
from users import contas, LIMITE_SAQUES, LIMITE_VALOR_SAQUE

# Constantes de erro
VALOR_INVALIDO = "Valor inválido!"
LIMITE_SAQUE_EXCEDIDO = "Valor do saque excede o limite!"
SALDO_INSUFICIENTE = "Saldo insuficiente!"
LIMITE_SAQUES_EXCEDIDO = "Número máximo de saques excedido!"

def formatar_data():
    
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def depositar(usuario, valor):

    if valor > 0:
        contas[usuario]["saldo"] += valor
        contas[usuario]["extrato"] += f"{formatar_data()} - Depósito: R$ {valor:.2f}\n"
        return True
    return False

def sacar(usuario, valor):

    conta = contas[usuario]

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
    """Exibe o extrato e saldo atual do usuário."""
    extrato = contas[usuario]["extrato"]
    saldo_atual = contas[usuario]["saldo"]
    return f"{extrato}\nSaldo atual: R$ {saldo_atual:.2f}" if extrato else "Nenhuma movimentação registrada."
