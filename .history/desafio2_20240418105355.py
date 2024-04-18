import textwrap

from desafio import LIMITE_SAQUES


def menu():
    menu = """\n
    ----------------- MENU -------------------
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar contas
    [nc]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == 'd':
            valor = float(input("Informe o valor do depósito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato) 
            
        elif opcao == 's':
            valor = float(input("Informe o valor do saque: "))   
            
            saldo, extrato = sacar(
                saldo:saldo,
                valor
            )