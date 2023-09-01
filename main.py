import bank
import person
import account

if __name__== '__name__':
    c1 = person.Account('Luiz', '000.000.000-00')
    cc1 = account.CheckingAccount(111, 222, 100)
    c1.conta = cc1
    banco_instancia = Bank()
    banco_instancia.clientes.extend([c1])
    banco_instancia.contas.extend([cc1])
    banco_instancia.agencias.extend([111, 222])

    if banco_instancia.autenticar(c1, cc1):
        cc1.deposit(10)
        c1.conta.deposit(100)
        print(c1.conta)