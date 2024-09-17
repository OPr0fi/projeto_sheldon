
from escolha import Escolha


class Jogador:
    def __init__(self, nome: str):
        self.nome = nome
        self.pontos = 0
        self.escolha = None

    def escolher(self, escolha: Escolha):
        self.escolha = escolha

    def incrementar_pontos(self):
        self.pontos += 1
