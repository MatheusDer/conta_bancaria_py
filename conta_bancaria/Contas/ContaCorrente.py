from Contas.Conta import Conta
from typing import Union


class ContaCorrente(Conta):
    def __init__(self, agencia: int, numero_conta: int) -> None:
        super().__init__(agencia, numero_conta)
        self.limite = 200

    def sacar(self, valor: Union[float, int]) -> None:
        self.limite = 200

        if not isinstance(valor, (float, int)):
            raise ValueError("Valor tem que ser um inteiro ou um float")

        if not (self._saldo + self.limite) >= valor:
            print("Saldo insuficiente")
            return
            
        self._saldo -= valor
        
        self.detalhes()
