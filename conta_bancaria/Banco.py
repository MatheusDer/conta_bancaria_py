from Cliente import Cliente
from Contas.Conta import Conta


class Banco:
    def __init__(self):
        self.agencias = [1234, 1111, 22233]
        self.contas = [Conta]
        self.clientes = [Cliente]

    def inserir_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta: Conta):
        self.contas.append(conta)

    def validacao_sacar(self, cliente: Cliente) -> bool:
        if cliente not in self.clientes:
            return False
        
        if cliente.conta not in self.contas:
            return False
        
        if cliente.conta.agencia not in self.agencias:
            return False

        return True

