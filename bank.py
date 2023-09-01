import account
import person

class Bank:
    def __init__(self, agencias: list[int] | None = None, 
                 clientes: list[person.Person] | None = None, 
                 contas: list[account.Account] | None = None ) -> None:
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []



        

    def _check_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('checkagencia', True)
            return True
        print ('Check agencia', False)
        return False
    def _check_cliente(self, cliente):
        if cliente in self.clientes:
            print("Checa clientes", True)
            return True
        print("Checa Clientes", False)
        return False
    
    def _check_conta (self, contas):
        if conta in self.contas:
            print("Checka conta", True)
            return True
        print("check_conta0", False)
        return False
    
    def _check_conta_pertence_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('Check conta pertence cliente', True)
            return True
        print ('check conta pertence', False)
        return False


        def autenticar (self, cliente: pessoa.pessoa, conta: contas.Account):
            return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)
        
        def __repr__(self):
            class_name =  type(self).__name__
            attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
            return f'{class_name}{attrs}'
        


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
