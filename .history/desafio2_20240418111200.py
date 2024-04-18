import textwrap

from desafio import LIMITE_SAQUES


def menu():
    menu = """\n
    ================ MENU =================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar contas
    [nc]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor = 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        
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
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)   
            
        elif opcao == "nu":
            criar_usuario(usuarios)     
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios) 
            
            if conta:
                contas.append(conta)
                
        elif opcao == "lc":
            listar_contas(conta) 
            
        elif opcao == "q":
            break          