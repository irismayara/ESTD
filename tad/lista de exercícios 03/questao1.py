#Crie um tipo de dados Conta quearmazena 'numero_conta', 'nome_correntista', 'saldo'
#Pergunte ao usuário vários números de contas e os armazene em uma lista
#Após armazenar,escreva todas as contas na tela
#Escreva a conta com o maior saldo

class Conta:

    def __init__(self, numero_conta, nome_correntista, saldo):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
    
    def __str__(self):
        return f"Número da conta: {self.numero_conta}, Nome do Correntista: {self.nome_correntista}, Saldo: R$ S{self.saldo}"


contas = []

comand = input('Digite F se desejar sair, ENTER para continuar: ').upper()
i = 1

while comand != "F":
    numero_conta = input(f'Digite o número da conta {i}: ')
    nome_correntista = input(f'Digite o nome do correntista da conta {i}: ')
    saldo = float(input(f'Digite o saldo da conta {i}: '))

    conta = Conta(numero_conta, nome_correntista, saldo)

    contas.append(conta)

    comand = input('Digite F se desejar sair, ENTER para continuar: ').upper()
    i += 1

print()
for conta in contas:
    print(conta)

max_saldo = 0
conta_max_saldo = Conta('','',0)

for conta in contas:
    if conta.saldo > max_saldo:
        max_saldo = conta.saldo
        conta_max_saldo = conta

print()
print(conta_max_saldo)


