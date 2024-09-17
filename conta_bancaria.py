
class Conta_Bancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.saques = 0
        self.conta_operacao = []
    

    def sacar(self,saques_diarios): 
        if self.saques >= saques_diarios:
            print('Quantidade de saques excedeu o limite diário!')
            return
        
        try:
            valor = float(input("Digite o valor a ser sacado: "))
            if valor <= self.saldo and valor <= 500:
                self.saldo -= valor
                self.saques += 1
                self.conta_operacao.append(f"Saque: R$ {valor:.2f}")
                print(f"O saque no valor de R$ {valor:.2f} foi realizado com sucesso!")
            elif valor > 500:
                print("O valor do saque é maior que o permitido, que é R$ 500 por saque.")
            else:
                print(f"Saldo insuficiente, seu saldo é de R$ {self.saldo:.2f}")
        except ValueError:
            print("Erro! Valor inválido!")

    def depositar(self):
        try:
            valor_deposito = float(input("Digite o valor do depósito: "))
            if valor_deposito > 0:
                self.saldo += valor_deposito
                self.conta_operacao.append(f"Depósito: R$ {valor_deposito:.2f}")
                print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
            else:
                print("Valor inválido! Deposite um valor acima de R$ 0.")
        except ValueError:
            print("Erro! Valor inválido!")

    def extrato(self):
        print(f"Seu saldo atual é de R$ {self.saldo:.2f}")
        print("Operações realizadas:")
        if not self.conta_operacao:
            print("Nenhuma operação realizada.")
        else:
            for operacao in self.conta_operacao:
                print(operacao)