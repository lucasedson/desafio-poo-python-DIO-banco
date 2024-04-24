from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, endereco:str, contas:list):
        self.endereco = endereco
        self.contas = contas

    def realizar_transacao(self, conta, transacao):
        ...

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf:str, nome:str, data_nascimento):
        super().__init__(contas=contas)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        ...

class Deposito(Transacao):
    def registrar(self, conta):
        ...

class Saque(Transacao):
    def registrar(self, conta):
        ...

class Historico:
    def adicionar_transacao(self, transacao):
        ...

class Conta:
    def __init__(self, saldo:float, numero:int, agencia:str, cliente:Cliente, historico:Historico):
        self._saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico

    @property
    def saldo(self):
        return self._saldo

    @classmethod
    def nova_conta(cls, saldo:float, numero:int, agencia:str, cliente:Cliente, historico:Historico)->Conta:
        return cls(saldo, numero, agencia, cliente, historico)

    def sacar(self, valor:float)->bool:
        ...

    def depositar(self, valor:float)->bool:
        ...


class ContaCorrente(Conta):
    def __init__(self, limite:float, limite_saques: int):
        super().__init__()
        self.limite = limite
        self.limite_saques = limite_saques
    