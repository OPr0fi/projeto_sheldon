from enum import Enum
import time
from typing import List
from escolha import COMBINACOES_DE_VITORIA
from jogador import Jogador

class GameMode(Enum):
    SINGLEPLAYER = 1
    MULTIPLAYER = 2

class Game:
    def __init__(self, mode: GameMode, duracao: int, jogadores: List[Jogador]):
        self.modo = mode
        self.duracao = duracao
        self.start_time = time.time()
        self.jogadores = jogadores
        self.ultimo_vencedor = None
        self.rodadas = 0

    def tempo_expirado(self) -> bool:
        return time.time() - self.start_time >= self.duracao

    def calcular_tempo_restante(self) -> float:
        return max(0, self.duracao - (time.time() - self.start_time))

    def processar_rodada(self) -> Jogador | None:
        escolha1, escolha2 = self.jogadores[0].escolha, self.jogadores[1].escolha
        self.rodadas += 1

        if escolha1 == escolha2:
            self.ultimo_vencedor = None
        elif (escolha1, escolha2) in COMBINACOES_DE_VITORIA:
            self.ultimo_vencedor = self.jogadores[0]
            self.jogadores[0].incrementar_pontos()
        else:
            self.ultimo_vencedor = self.jogadores[1]
            self.jogadores[1].incrementar_pontos()

        return self.ultimo_vencedor

    def get_ultimo_vencedor(self) -> Jogador | None:
        return self.ultimo_vencedor

    def get_ultimo_perdedor(self) -> Jogador | None:
        return self.jogadores[1] if self.ultimo_vencedor == self.jogadores[0] else self.jogadores[0] if self.ultimo_vencedor else None

    def placar(self) -> tuple[int, int]:
        return self.jogadores[0].pontos, self.jogadores[1].pontos

    def verificar_vencedor(self) -> Jogador | None:
        if self.jogadores[0].pontos > self.jogadores[1].pontos:
            return self.jogadores[0]
        elif self.jogadores[0].pontos < self.jogadores[1].pontos:
            return self.jogadores[1]
        return None

    def incrementar_tempo(self, intervalo: int) -> None:
        self.duracao += intervalo
