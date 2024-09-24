import curses
from escolha import ESCOLHAS_POSSIVEIS, MENSAGENS_DE_VITORIA, Escolha
from game import Game, GameMode
from jogador import Jogador
from ui import UserInterface

def display_placar(ui: UserInterface, game: Game):
    pontuacao1, pontuacao2 = game.placar()
    ultimo_vencedor = game.ultimo_vencedor
    jogador1, jogador2 = game.jogadores

    ui.display('\n')

    if ultimo_vencedor:
        ui.colored_display(f'{jogador1.nome}', ui.GREEN_FOREGROUND if ultimo_vencedor is jogador1 else ui.RED_FOREGROUND)
        ui.display(f' - ({pontuacao1} x {pontuacao2}) - ')
        ui.colored_display(f'{jogador2.nome}', ui.GREEN_FOREGROUND if ultimo_vencedor is jogador2 else ui.RED_FOREGROUND)
    else:
        ui.colored_display(f'{jogador1.nome} - ({pontuacao1} x {pontuacao2}) - {jogador2.nome}', ui.YELLOW_FOREGROUND)

    ui.display('\n')

def display_jogadas(ui: UserInterface, game: Game):
    if game.rodadas == 0:
        ui.display('\n\n')
        return

    vencedor = game.get_ultimo_vencedor()
    perdedor = game.get_ultimo_perdedor()

    if vencedor:
        chave = (vencedor.escolha, perdedor.escolha)
        if chave in MENSAGENS_DE_VITORIA:
            ui.display(MENSAGENS_DE_VITORIA[chave])
    else:
        ui.display('Empate!')
    ui.display('\n\n')

def display_game_state(ui: UserInterface, game: Game, jogador: Jogador):
    tempo_restante = game.calcular_tempo_restante()
    color_pair = (
        ui.GREEN_PAIR if tempo_restante > (game.duracao / 2)
        else ui.YELLOW_PAIR if tempo_restante > (game.duracao / 5)
        else ui.RED_PAIR
    )

    ui.clear()
    ui.display(f'{jogador.nome} agora é sua vez !\n', ui.REVERSE_MODE)
    ui.display('\n')
    ui.colored_display(f'⏰ Tempo restante: {tempo_restante:.2f} segundos\n', color_pair)
    display_placar(ui, game)
    display_jogadas(ui, game)

    ui.display('Escolha uma opção: (basta digitar uma tecla, rápido!)\n')
    for idx, escolha in enumerate(ESCOLHAS_POSSIVEIS, 1):
        ui.display(f'{idx} - {escolha.name}\n')

    ui.refresh()

def display_vitoria(ui: UserInterface, game: Game):
    ui.clear()
    ui.display('Fim de jogo!\n')
    ui.display(f'{game.jogadores[0].nome} - {game.placar()[0]} x {game.placar()[1]} - {game.jogadores[1].nome}\n')

    vencedor = game.verificar_vencedor()

    if game.modo == GameMode.SINGLEPLAYER:
        result = 'You won!' if vencedor is game.jogadores[0] else 'You lose!' if vencedor is game.jogadores[1] else 'Empate!'
        color = ui.GREEN_FOREGROUND if result == 'You won!' else ui.RED_FOREGROUND if result == 'You lose!' else ui.YELLOW_FOREGROUND
    else:
        if game.jogadores[0].pontos > game.jogadores[1].pontos:
            result, color = f'{game.jogadores[0].nome} ganhou!', ui.GREEN_FOREGROUND
        elif game.jogadores[0].pontos < game.jogadores[1].pontos:
            result, color = f'{game.jogadores[1].nome} ganhou!', ui.RED_FOREGROUND
        else:
            result, color = 'Empate!', ui.YELLOW_FOREGROUND

    ui.colored_display(f'{result}\n', color)
    ui.display('Pressione qualquer tecla para sair\n')
    ui.refresh()
    ui.getkey()

def ler_escolha(ui: UserInterface, jogador: Jogador, game: Game):
    ui.set_nonblocking(True)
    while not game.tempo_expirado():
        display_game_state(ui, game, jogador)
        try:
            escolha = ui.getkey()
            ui.set_nonblocking(False)
            if escolha not in ['1', '2', '3', '4', '5']:
                ui.display('Tecla errada, o ponto vai para o seu adversário\n')
                ui.refresh()
                ui.sleep(1)
                game.incrementar_tempo(1)
                return None, True
            return ESCOLHAS_POSSIVEIS[int(escolha) - 1], False
        except:
            ui.sleep(0.1)
    return None, False

def main(stdscr):
    ui = UserInterface(stdscr)
    escolha = ui.menu("Escolha o modo de jogo", ["Player x Machine", "Player x Player", "Quit"])
    if escolha == 2:
        return

    modo = GameMode.SINGLEPLAYER if escolha == 0 else GameMode.MULTIPLAYER
    duracao = [8, 45, 60][ui.menu("Escolha a duração do jogo", ["30 segundos", "45 segundos", "60 segundos"])]

    jogadores = [Jogador('Jogador 1' if modo == GameMode.MULTIPLAYER else 'Jogador'),
                 Jogador('Máquina' if modo == GameMode.SINGLEPLAYER else 'Jogador 2')]

    game = Game(modo, duracao, jogadores)

    stdscr.clear()
    stdscr.refresh()

    while not game.tempo_expirado():
        for jogador in game.jogadores:
            if jogador.nome == 'Máquina':
                jogador.escolher(Escolha.aleatorio())
            else:
                escolha, erro = ler_escolha(ui, jogador, game)
                if erro:
                    game.jogadores[1 if jogador == game.jogadores[0] else 0].incrementar_pontos()
                    continue
                if escolha is None:
                    break
                jogador.escolher(Escolha(escolha))

        if escolha is None:
            break

        game.processar_rodada()

    ui.getch()
    ui.clear()

    ui.set_nonblocking(False)

    display_vitoria(ui, game)

if __name__ == "__main__":
    curses.wrapper(main)
