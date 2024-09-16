import time
import os
import random
import curses

from errors import OpcaoInvalidaError

CONDICAO_VITORIA_TUPLAS = [
    ("tesoura", "papel"),
    ("papel", "pedra"),
    ("pedra", "tesoura"),
    ("pedra", "lagarto"),
    ("lagarto", "spock"),
    ("spock", "tesoura"),
    ("tesoura", "lagarto"),
    ("lagarto", "papel"),
    ("papel", "spock"),
    ("spock", "pedra"),
]

MODO_SINGLEPLAYER = "1"
MODO_MULTIPLAYER = "2"

JOGADOR_1 = 0
JOGADOR_2 = 1

ESCOLHAS_POSSIVEIS = ("pedra", "papel", "tesoura", "lagarto", "spock")


def ler_escolha(stdscr, jogador):
    mostrar_titulo(stdscr)
    stdscr.addstr(f'{jogador}, escolha a sua jogada:\n')
    stdscr.addstr('1 - pedra\n2 - papel\n3 - tesoura\n4 - lagarto\n5 - spock\n')
    stdscr.refresh()
    input = None

    try:
        input = int(stdscr.getch())
    except:
        return None

    if input not in range(49, 54):
        raise OpcaoInvalidaError()

    stdscr.addstr(f'Você escolheu: {input}\n')
    time.sleep(2)
    return ESCOLHAS_POSSIVEIS[input - 1]

def calcular_tempo_restante(tempo_inicial, tempo_duracao):
    return tempo_duracao - int(time.time() - tempo_inicial)

def mostrar_titulo(stdscr):
    stdscr.addstr('Sheldon Cooper - Pedra, papel, tesoura, lagarto, spock\n')

def mostrar_pontos(stdscr, pontos_ordenados):
    stdscr.addstr(f"Placar: {pontos_ordenados[0]} x {pontos_ordenados[1]}\n")

def mostrar_opcoes(stdscr, opcoes):
    for index, opcao in enumerate(opcoes):
        stdscr.addstr(f'{index + 1} - {opcao}\n')

def tempo_expirado(tempo_duracao, tempo_inicial):
    return (time.time() - tempo_inicial) > tempo_duracao


def main(stdscr=None):
    stdscr = curses.initscr()

    highlight = 0
    opcoes = ['Player x Machine', 'Player x Player', 'Sair']

    while True:
        stdscr.clear()
        mostrar_titulo(stdscr)
        stdscr.addstr('Escolha o modo de jogo:\n')
        # A variável ´highlight´ é usada para indicar qual opção está selecionada
        for index, opcao in enumerate(opcoes):
            if index == highlight:
                mode = curses.A_REVERSE
            else:
                mode = curses.A_NORMAL
            mensagem = f'{opcao}\n'
            stdscr.addstr(mensagem, mode)

        stdscr.refresh()
        tecla_pressionada = stdscr.getch()

        if tecla_pressionada == curses.KEY_UP:
            highlight = (highlight - 1) % 3
        elif tecla_pressionada == curses.KEY_DOWN:
            highlight = (highlight + 1) % 3
        elif tecla_pressionada == curses.KEY_ENTER or tecla_pressionada in [10, 13]:
            break

    # Sair do jogo
    if highlight == 2:
        return

    # Modo de jogo escolhido
    modo = MODO_SINGLEPLAYER if highlight == 0 else MODO_MULTIPLAYER

    # Iniciar o jogo
    pontos_ordenados = [0, 0]
    tempo_inicial = time.time()
    tempo_duracao = 20
    refresh_time = 0.1

    # Precisamos que os inputs não bloqueiem a execução do programa
    stdscr.nodelay(True)

    # Precisamos controlar qual jogador está jogando
    jogador_atual = JOGADOR_1
    escolhas_ordenadas = ["", ""]
    while True:
        stdscr.clear()
        if tempo_expirado(tempo_duracao, tempo_inicial):
            break

        if jogador_atual == JOGADOR_1:
            tempo_restante = calcular_tempo_restante(tempo_inicial, tempo_duracao)
            stdscr.addstr(f'Tempo restante: {tempo_restante}\n')
            mostrar_pontos(stdscr, pontos_ordenados)

            primeira_escolha = None

            stdscr.addstr(f'Jogador 1, escolha a sua jogada:\n')
            mostrar_opcoes(stdscr, ESCOLHAS_POSSIVEIS)
            stdscr.refresh()
            input = None

            time.sleep(refresh_time)

            # Esse trycatch é necessário por que o getkey pode lançar
            # uma exceção caso não tenha nenhuma tecla pressionada
            # já que ligamos o `nodelay`
            try:
                input = stdscr.getkey()
            except:
                continue

            stdscr.addstr(f'Você escolheu: {input}\n')

            if not input in ["1", "2", "3", "4", "5"]:
                stdscr.addstr("Tecla errada, o ponto vai para o seu adversário\n")
                stdscr.refresh()
                pontos_ordenados[1] += 1
                time.sleep(1.5)
                continue

            if input != None:
                primeira_escolha = ESCOLHAS_POSSIVEIS[int(input) - 1]
                escolhas_ordenadas[0] = primeira_escolha
                jogador_atual = JOGADOR_2


        if modo == MODO_MULTIPLAYER and jogador_atual == JOGADOR_2:
            stdscr.clear()

            input = None
            segunda_escolha = None

            tempo_restante = calcular_tempo_restante(tempo_inicial, tempo_duracao)
            stdscr.addstr(f'Tempo restante: {tempo_restante}\n')
            mostrar_pontos(stdscr, pontos_ordenados)

            stdscr.addstr(f'Jogador 2, escolha a sua jogada:\n')
            mostrar_opcoes(stdscr, ESCOLHAS_POSSIVEIS)
            stdscr.refresh()

            time.sleep(refresh_time)

            try:
                input = stdscr.getkey()
            except:
                continue

            stdscr.addstr(f'Você escolheu: {input}\n')

            if not input in ["1", "2", "3", "4", "5"]:
                stdscr.addstr("Tecla errada, o ponto vai para o seu adversário\n")
                stdscr.refresh()
                pontos_ordenados[0] += 1
                time.sleep(1.5)
                continue

            if input != None:
                segunda_escolha = ESCOLHAS_POSSIVEIS[int(input) - 1]
                escolhas_ordenadas[1] = segunda_escolha
                jogador_atual = JOGADOR_1

            stdscr.refresh()

        elif modo == MODO_SINGLEPLAYER and jogador_atual == JOGADOR_2  :
            segunda_escolha = random.choice(ESCOLHAS_POSSIVEIS)
            escolhas_ordenadas[1] = segunda_escolha
            jogador_atual = JOGADOR_1

        stdscr.refresh()
        if modo == MODO_SINGLEPLAYER:
            stdscr.addstr(f'Jogador 1 > {escolhas_ordenadas[0]} x {escolhas_ordenadas[1]} < Computador\n')
        else:
            stdscr.addstr(f'Jogador 1 > {escolhas_ordenadas[0]} x {escolhas_ordenadas[1]} Jogador 2\n')

        if escolhas_ordenadas[0] == escolhas_ordenadas[1]:
            stdscr.addstr("Empate!\n")
        elif (escolhas_ordenadas[0], escolhas_ordenadas[1]) in CONDICAO_VITORIA_TUPLAS:
            pontos_ordenados[0] += 1
            stdscr.addstr("Jogador 1 venceu essa rodada\n")
        else:
            pontos_ordenados[1] += 1

            if modo == MODO_SINGLEPLAYER:
                stdscr.addstr("Jogador 2 venceu essa rodada\n")
            else:
                stdscr.addstr("Computador venceu essa rodada\n")
        stdscr.refresh()
        time.sleep(1)

    # Não precisamos mais que os inputs não bloqueiem a execução do programa
    stdscr.nodelay(False)

    stdscr.addstr("Fim de jogo!\n")
    mostrar_pontos(stdscr, pontos_ordenados)

    empate = pontos_ordenados[0] == pontos_ordenados[1]

    if empate:
        stdscr.addstr("O jogo terminou em empate!\n")

    if modo == MODO_SINGLEPLAYER:
        if pontos_ordenados[0] > pontos_ordenados[1]:
            stdscr.addstr("You won!\n")
        else:
            stdscr.addstr("You lost!\n")
    else:
        if pontos_ordenados[0] > pontos_ordenados[1]:
            stdscr.addstr("Jogador 1, You won!\n")
            stdscr.addstr("Jogador 2, You lose!\n")
        else:
            stdscr.addstr("Jogador 2, You won!\n")
            stdscr.addstr("Jogador 1, You lose!\n")

    stdscr.refresh()
    stdscr.addstr("Pressione qualquer tecla\n")
    stdscr.getkey()


if __name__ == "__main__":
    curses.wrapper(main)
