from enum import Enum


class Escolha(Enum):
    PEDRA = 1
    PAPEL = 2
    TESOURA = 3
    LAGARTO = 4
    SPOCK = 5

    @classmethod
    def from_int(cls, value: int):
        return cls(value)

    def __str__(self):
        return self.name.lower()

    @staticmethod
    def aleatorio():
        from random import choice
        return choice(list(Escolha))

COMBINACOES_DE_VITORIA = [
    (Escolha.TESOURA, Escolha.PAPEL),
    (Escolha.PAPEL, Escolha.PEDRA),
    (Escolha.PEDRA, Escolha.LAGARTO),
    (Escolha.LAGARTO, Escolha.SPOCK),
    (Escolha.SPOCK, Escolha.TESOURA),
    (Escolha.TESOURA, Escolha.LAGARTO),
    (Escolha.LAGARTO, Escolha.PAPEL),
    (Escolha.PAPEL, Escolha.SPOCK),
    (Escolha.SPOCK, Escolha.PEDRA),
    (Escolha.PEDRA, Escolha.TESOURA),
]


ESCOLHAS_POSSIVEIS = (Escolha.PEDRA, Escolha.PAPEL, Escolha.TESOURA, Escolha.LAGARTO, Escolha.SPOCK)
