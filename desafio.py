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
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0: 
            saldo += valor 
            extrato += f"Deposito : R$ {valor:.2f}\n"
        else: 
            print("Operacao falhou! O valor informado é invalido.")
    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operecao falhou! Voce nao tem saldo suficiente.")
        elif excedeu_limite:
            print("Operecao falhou! O valor do saque excede o limite")
        elif excedeu_saque:
             print("Operecao falhou! Numero maximo de saque execedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
        else:
            print("Operecao falhou! O valor informado é invalido.")

    elif opcao == "e":
        print("\n=================== EXTRATO ===================")
        print("Nao foram realizadas movimentações. " if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================================================")
    elif opcao == "q":
        print("Saindo...")
        break
    else:
        print("Opcao invalida digite outra opcao")