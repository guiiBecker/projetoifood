from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, agency, account, balance:float = 0):
        self.agency = agency
        self.account = account
        self.balance = balance


# classe abstrata para ser herdada na classe CheckingAccount
    @abstractmethod
    def withdraw (self, value:float):
        ...  
# funções para serem herdadas para a classe CheckingAccount
    def deposit(self, value:float):
        self.balance += value
        self.details (f'Depósito {value:.2f}')

        
# Essa função gerará uma espécie de log para o usuário informando o que causou a falha
    def details(self, msg=''):
        print (f'Seu saldo é {self.balance:.2f} {msg}')


    def __repr__(self):
        class_name = type(self).__name__
        attrs = (f'({self.agency!r}, {self.account!r}, {self.balance})')
        return f'{class_name}{attrs}'

class CheckingAccount(Account):
    def withdraw(self, value:float):
        balance_after_withdraw = self.balance - value

        if balance_after_withdraw >= 0:
            self.balance -= value
            self.details(f'Saque {value:.2f}')
            return self.balance
        
        print ('Não foi possível sacar o valor desejado')
        
    
#testes para essa classe
if __name__=='__main__':
    cc1 =  CheckingAccount (111, 222 )
    cc1.deposit(1)
    cc1.withdraw(1)