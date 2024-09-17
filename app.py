import curses
import time

from escolha import ESCOLHAS_POSSIVEIS, Escolha
from game import Game, GameMode
from jogador import Jogador
from ui import UserInterface

def display_placar(ui: UserInterface, game: Game):
    pontuacao1, pontuacao2 = game.placar()
    ultimo_vencedor = game.ultimo_vencedor
    primeiro_jogador = game.jogadores[0]
    segundo_jogador = game.jogadores[1]

    ui.display('\n')

    if ultimo_vencedor is not None:
        if ultimo_vencedor is primeiro_jogador:
            ui.colored_display(f'{primeiro_jogador.nome}', ui.GREEN_FOREGROUND)
        else:
            ui.display(f'{primeiro_jogador.nome}', ui.RED_FOREGROUND)

        ui.display(f' - ({pontuacao1} x {pontuacao2}) - ')

        if ultimo_vencedor is segundo_jogador:
            ui.colored_display(f'{segundo_jogador.nome}', ui.GREEN_FOREGROUND)
        else:
            ui.display(f'{segundo_jogador.nome}', ui.RED_FOREGROUND)

    else:
        ui.colored_display(f'{primeiro_jogador.nome} - ({pontuacao1} x {pontuacao2}) - {segundo_jogador.nome}', ui.YELLOW_FOREGROUND)

    ui.display('\n\n')


def display_game_state(ui: UserInterface, game: Game, jogador: Jogador):
    tempo_restante = game.calcular_tempo_restante()

    color_pair = None

    if tempo_restante > (game.duracao / 2):
        color_pair = ui.GREEN_PAIR
    elif tempo_restante > (game.duracao / 5):
        color_pair = ui.YELLOW_PAIR
    else:
        color_pair = ui.RED_PAIR


    ui.clear()

    ui.display(f'{jogador.nome} agora é sua vez !\n', ui.REVERSE_MODE)
    ui.display('\n')
    ui.colored_display(f'⏰ Tempo restante: {tempo_restante:.2f} segundos\n', color_pair)
    display_placar(ui, game)
    ui.display('Escolha uma opção: (basta digitar uma tecla, rápido!)\n')
    for idx, escolha in enumerate(ESCOLHAS_POSSIVEIS):
        ui.display(f'{idx+1} - {escolha.name}\n')

    ui.refresh()


def ler_escolha(ui: UserInterface, jogador: Jogador, game: Game):
    start_time = time.time()
    while not game.tempo_expirado():
        display_game_state(ui, game, jogador)

        # Check for input with a short timeout
        ui.set_nonblocking(True)
        try:
            escolha = ui.getkey()
            ui.set_nonblocking(False)

            if escolha not in ['1', '2', '3', '4', '5']:
                ui.display('Tecla errada, o ponto vai para o seu adversário')
                ui.display('\n')
                ui.refresh()
                time.sleep(1)
                return None, True

            return ESCOLHAS_POSSIVEIS[int(escolha) - 1], False
        except:
            # No input, continue updating display
            pass

        ui.sleep(0.1)  # Short sleep to prevent CPU overuse

    # Time expired without a choice
    return None, True


def main(stdscr):
    ui = UserInterface(stdscr)

    escolha = ui.menu("Escolha o modo de jogo", ["Player x Machine", "Player x Player", "Quit"])

    if escolha == 2:
        return

    modo = GameMode.SINGLEPLAYER if escolha == 0 else GameMode.MULTIPLAYER

    escolha = ui.menu("Escolha a duração do jogo", ["30 segundos", "45 segundos", "60 segundos"])

    duracao = 30 if escolha == 0 else 45 if escolha == 1 else 60
    game = Game(modo, duracao)

    stdscr.clear()
    stdscr.refresh()

    while not game.tempo_expirado():
        escolha, erro = ler_escolha(ui, game.jogadores[0], game)

        if erro:
            game.jogadores[1].incrementar_pontos()
            continue

        if escolha is None:  # Time expired
            break

        game.jogadores[0].escolher(Escolha(escolha))

        if game.modo == GameMode.MULTIPLAYER:
            escolha, erro = ler_escolha(ui, game.jogadores[1], game)

            if erro:
                game.jogadores[0].incrementar_pontos()
                continue

            if escolha is None:  # Time expired
                break

            game.jogadores[1].escolher(Escolha(escolha))

        else:
            game.jogadores[1].escolher(Escolha.aleatorio())

        game.processar_rodada()

    vencedor = game.verificar_vencedor()

    ui.set_nonblocking(False)

    ui.clear()

    ui.display('Tempo esgotado!\n\n')
    if vencedor is None:
        ui.colored_display('Empate!\n', ui.YELLOW_PAIR)
    else:
        ui.colored_display(f'{vencedor.nome} - You won!\n', ui.GREEN_PAIR)

    ui.display('Pressione qualquer tecla para sair...\n')
    ui.refresh()
    ui.getch()

if __name__ == "__main__":
    curses.wrapper(main)
