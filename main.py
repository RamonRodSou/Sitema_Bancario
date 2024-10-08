from conta_bancaria import Conta_Bancaria
from colorama import init, Fore, Style

init()
operacao = -1
contador = 0
saldo_inicial = 1000
conta = Conta_Bancaria(saldo_inicial)

while operacao != 0:
    
    operacao = int(input(f"""
    
    {Fore.LIGHTWHITE_EX + "Menu".center(6).center(26, "#") + Style.RESET_ALL}
        
        {Fore.GREEN + "[1] Sacar" + Style.RESET_ALL}
        {Fore.CYAN + "[2] Depositar" + Style.RESET_ALL}
        {Fore.MAGENTA + "[3] Extrato" + Style.RESET_ALL}
        {Fore.RED + "[0] Sair" + Style.RESET_ALL}
        
    {Fore.LIGHTWHITE_EX + ''.center(26, '#')  + Style.RESET_ALL}
                
            """))
    
    if operacao == 1:
        
        if contador >= 3:
            print(Fore.YELLOW + 'Quantidade de saques excedeu o limite diário!' + Style.RESET_ALL)
        else:
            valor = float(input(Fore.YELLOW + "Digite o valor a ser sacado: " + Style.RESET_ALL))
            conta.sacar(3, valor)
            contador += 1

    elif operacao == 2:
        deposito = float(input( Fore.YELLOW + "Digite o valor do depósito: " + Style.RESET_ALL))
        conta.depositar(deposito)
            
    elif operacao == 3:
        conta.extrato()
            
    elif operacao == 0:
        print(Fore.YELLOW + 'Saindo...'  + Style.RESET_ALL)
    
    else:
        print(Fore.RED + 'Opção Inválida' + Style.RESET_ALL)

