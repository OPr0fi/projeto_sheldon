from enum import Enum
from random import choice


class Escolha(Enum):
    PEDRA = 1
    PAPEL = 2
    TESOURA = 3
    LAGARTO = 4
    SPOCK = 5

    def __str__(self):
        return self.name.lower()

    @staticmethod
    def aleatorio():
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

MENSAGENS_DE_VITORIA = {
    (Escolha.TESOURA, Escolha.PAPEL): 'Tesoura corta papel',
    (Escolha.PAPEL, Escolha.PEDRA): 'Papel cobre pedra',
    (Escolha.PEDRA, Escolha.LAGARTO): 'Pedra esmaga lagarto',
    (Escolha.LAGARTO, Escolha.SPOCK): 'Lagarto envenena Spock',
    (Escolha.SPOCK, Escolha.TESOURA): 'Spock esmaga tesoura',
    (Escolha.TESOURA, Escolha.LAGARTO): 'Tesoura decapita lagarto',
    (Escolha.LAGARTO, Escolha.PAPEL): 'Lagarto come papel',
    (Escolha.PAPEL, Escolha.SPOCK): 'Papel refuta Spock',
    (Escolha.SPOCK, Escolha.PEDRA): 'Spock vaporiza pedra',
    (Escolha.PEDRA, Escolha.TESOURA): 'Pedra quebra tesoura',
}

ESCOLHAS_POSSIVEIS = (Escolha.PEDRA, Escolha.PAPEL, Escolha.TESOURA, Escolha.LAGARTO, Escolha.SPOCK)
