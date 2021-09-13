from abc import ABC, abstractmethod
from typing import Union

class Conta(ABC):
    def __init__(self, agencia: int, numero_conta: int) -> None:
        self.agencia = agencia
        self.numero_conta = numero_conta
        self._saldo = 0
    
    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor: Union[float, int]) -> None:
        if not isinstance(valor, (float, int)):
            raise ValueError("Valor tem que ser um inteiro ou um float")
        
        self._saldo += valor

        self.detalhes()
    
    def detalhes(self) -> None:
        print(F"""Agencia: {self.agencia}
Numero da Conta: {self.numero_conta}
Saldo: {self._saldo}
""")

    @abstractmethod
    def sacar(self, valor) -> None: pass
