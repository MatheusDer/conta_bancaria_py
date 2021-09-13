from Contas.Conta import Conta
from typing import Union

class ContaPoupanca(Conta):
    def sacar(self, valor: Union[float, int]) -> None:
        if not isinstance(valor, (float, int)):
            raise ValueError("Valor tem que ser um inteiro ou um float")
        
        if not self._saldo > 0:
            print("Saldo insuficiente")
            return
            
        self._saldo -= valor
        
        self.detalhes()
