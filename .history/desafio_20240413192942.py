menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 2

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
    if valor > 0:
          saldo += valor
          extrato += f'Deposito: R$ {valor: .2f}\n'
    else:
          print("Operação falhou! O valor informado é inválido. tente novamente")            