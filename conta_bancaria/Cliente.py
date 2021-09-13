from Contas.Conta import Conta
from Pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, conta: Conta) -> None:
        super().__init__(nome, idade)
        self.conta = conta
