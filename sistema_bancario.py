from datetime import datetime

### Variável que contém a mensagem do Menu do sistema
menu =  '''
=========Sistema Bancário==========

        [s] Saque
        [d] Depósito
        [e] Extrato

        [q] Sair do sistema

===================================
        '''

### Função responsável por efetuar o saque na conta e registrar log da operação
def sacar(valor) -> list:
    data_hora = datetime.now()
    data_hora = data_hora.strftime('%d/%m/%y %H:%M:%S')
    return ([saldo - valor, data_hora])

### Função responsável por efetuar o depósito na conta e registrar log da operação
def depositar(valor, saldo) -> list:
    data_hora = datetime.now()
    data_hora = data_hora.strftime('%d/%m/%y %H:%M:%S')
    saldo += valor
    return ([saldo, data_hora])

### Função responsável por imprimir na tela o extrato do correntista
def extrato_conta(saque, deposito):
    for i in saque:
        print(f'Saque -> {i}')

    for i in deposito:
        print(f'Deposito -> {i}')

    return

LIMITE_SAQUE = 500
contador_saque = 3
saque = []
deposito = []

saldo = 1500.00

### Menu do sistema
while True:
    print(menu)

    print('Olá, seja bem vindo ao nosso sistema!\n',)
    
    opcao = input('Em que podemos ajudar: ')
    print('\n\n\n\n')
    if opcao.lower() == 'q':
        print('Obrigado por usar nossos serviços!\n')
        break

    elif opcao.lower() == 's':
        if contador_saque == 0:
            print("ATENÇÂO: Você atingiu o limite diário de saque\n")
        else:
            valor = float(input('Por favor, informe o valor de saque: '))
            print('\n\n')
            if valor <= 500 and saldo >= valor:
                saque.append(sacar(valor))
                contador_saque -= 1
                saldo -= valor
                print(f'O saque de R${valor} foi realizado com sucesso!')
            else:
                print('ATENÇÃO: Saldo menor que o valor de saque solicitado!')
    elif opcao.lower() == 'd':
        print('O deposito na conta deve ser a partir de R$10,00')
        valor = float(input('Por favor, informe o valor a depositar: '))
        print('\n\n')
        if valor >= 10:
            deposito.append(depositar(valor, saldo))
            saldo += valor
            print(f'O valor {valor} foi depositado com sucesso!')
        else:
            print('ATENÇÃO: Depósitos devem ser a partir de R$10,00')
            print('\n\n')
    elif opcao.lower() == 'e':
        print('Extrato da conta:\n\n')
        extrato_conta(saque, deposito)
    elif opcao.lower() == 'q':
        break