from colorama import init, Fore, Style

class Conta_Bancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        # self.saques = 0
        self.conta_operacao = []
    

    def sacar(self,saques_diarios, valor): 
        # if self.saques >= saques_diarios:
        #     print(Fore.YELLOW +  'Quantidade de saques excedeu o limite diário!' + Style.RESET_ALL)
        #     return
        
        try:
            if valor <= self.saldo and valor <= 500:
                self.saldo -= valor
                # self.saques += 1
                self.conta_operacao.append(f"Saque: R$ {valor:.2f}")
                print(Fore.GREEN + f"O saque no valor de R$ {valor:.2f} foi realizado com sucesso!" + Style.RESET_ALL)
            elif valor > 500:
                print(Fore.LIGHTRED_EX + "O valor do saque é maior que o permitido, que é R$ 500 por saque." + Style.RESET_ALL)
            else:
                print(Fore.LIGHTYELLOW_EX + f"Saldo insuficiente, seu saldo é de R$ {self.saldo:.2f}" + Style.RESET_ALL)
        except ValueError:
            print(Fore.GREEN + "Erro! Valor inválido!")

    def depositar(self, deposito):  
        try:
            if deposito > 0:
                self.saldo += deposito
                self.conta_operacao.append(f"Depósito: R$ {deposito:.2f}")
                print(Fore.GREEN + f"Depósito de R$ {deposito:.2f} realizado com sucesso!" + Style.RESET_ALL)
            else:
                print(Fore.LIGHTRED_EX + "Valor inválido! Deposite um valor acima de R$ 0." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Erro! Valor inválido!" + Style.RESET_ALL)

    def extrato(self):
        print(Fore.GREEN + f"Seu saldo atual é de R$ {self.saldo:.2f}" + Style.RESET_ALL)
        print(Fore.BLUE + "Operações realizadas:" + Style.RESET_ALL) 
        if not self.conta_operacao:
            print(Fore.LIGHTMAGENTA_EX +  "Nenhuma operação realizada." + Style.RESET_ALL)
        else:
            for operacao in self.conta_operacao:
                print(operacao)