from Pessoa import Pessoa
from Contas.ContaPoupanca import ContaPoupanca
from Banco import Banco
from Contas.Conta import Conta
from Cliente import Cliente
from Contas.ContaCorrente import ContaCorrente

"""banco = Banco()

conta1 = ContaCorrente(1111, 23)
banco.inserir_conta(conta1)

conta2 = ContaPoupanca(2222, 3)

cliente1 = Cliente("Matheus", 19, conta1)
banco.inserir_cliente(cliente1)


if banco.validacao_sacar(cliente1):
    cliente1.conta.depositar(100)
    cliente1.conta.sacar(100)
else:
    print("Autenticação nao encontrada")"""

p1 = Pessoa("nome", 10)
print(p1.nome)
