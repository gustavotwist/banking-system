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
          print("Operação falhou! O valor informado é inválido. Tente novamente!")    
          
    if opcao == 's':
        
        valor = float(input("Informe o valor do saque: "))   
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES  
        
    if excedeu_saldo:
        print("Operação falhou! Voçê não possui saldo suficiente.")   
                  
    elif excedeu_limite              