from enum import Enum
import time

from escolha import COMBINACOES_DE_VITORIA
from jogador import Jogador

class TempoSeveridade(Enum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3

class GameMode(Enum):
    SINGLEPLAYER = 1
    MULTIPLAYER = 2

class Game:
    def __init__(self, mode: GameMode, duracao: int, ):
        self.modo = mode
        self.duracao = duracao
        self.start_time = time.time()
        self.jogadores = [Jogador("Jogador 1"), Jogador("Jogador 2")]
        self.ultimo_vencedor = None
        pass

    def start(self):
        self.start_time = time.time()

    def tempo_expirado(self):
        return time.time() - self.start_time >= self.duracao

    def calcular_tempo_restante(self):
        return float(self.duracao) - (time.time() - self.start_time)

    def processar_rodada(self):
        escolha_primeiro_jogador, escolha_segundo_jogador = self.jogadores[0].escolha, self.jogadores[1].escolha

        if escolha_primeiro_jogador == escolha_segundo_jogador:
            self.ultimo_vencedor = None
            return None # Empate
        elif (escolha_primeiro_jogador, escolha_segundo_jogador) in COMBINACOES_DE_VITORIA:
            self.jogadores[0].incrementar_pontos()
            self.ultimo_vencedor = self.jogadores[0]
            return self.jogadores[0]
        else:
            self.jogadores[1].incrementar_pontos()
            self.ultimo_vencedor = self.jogadores[1]
            return self.jogadores[1]

    def placar(self):
        return self.jogadores[0].pontos, self.jogadores[1].pontos

    def verificar_vencedor(self):
        if self.jogadores[0].pontos > self.jogadores[1].pontos:
            return self.jogadores[0]
        elif self.jogadores[0].pontos < self.jogadores[1].pontos:
            return self.jogadores[1]
        else:
            return None # Empate
