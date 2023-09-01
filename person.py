import account


class Person():
    def __init__(self, name:str, cpf:str):
        self.name = name
        self.cpf = cpf
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name:str):
        self._name = name

    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, cpf:str):
        self._cpf = cpf


    def __repr__(self):
        class_name = type(self).__name__
        attrs = (f'({self.name!r}, {self.cpf!r})')
        return f'{class_name}{attrs}'
        

class Client(Person):
    def __init__(self, name: str, cpf: str):
        super().__init__(name, cpf)
        self.account = account.Account | None 
    
    def __repr__(self):
        return super().__repr__()


if __name__ == "__main__":
    c1 = Client('Guilherme', '000.000.000-00')
    c1.account = account.CheckingAccount(111, 222, 0)
    print(c1)
    print(c1.account)



