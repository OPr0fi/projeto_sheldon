import time
import os
import random

win_lose_escolhas = [
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

escolhas_validas = ("pedra", "papel", "tesoura", "lagarto", "spock")


def ler_escolha(mensagem, pontos, jogador_atual, adversario, modo):
    print(mensagem)
    print(" 0 -> pedra\n 1 -> papel\n 2 -> tesoura\n 3 -> lagarto\n 4 -> spock")

    try:
        escolha = int(input("Sua escolha: "))
        if escolha not in range(5):
            raise ValueError
        return escolhas_validas[escolha]
    except (ValueError, IndexError):
        if modo == "1":
            print(f"Tecla errada! O ponto vai para o computador.")
            pontos[1] += 1
        else:
            print(f"Tecla errada! O ponto vai para o Jogador {adversario + 1}.")
            pontos[adversario] += 1
        return None


def mostrar_tempo_restante(tempo_duracao, tempo_inicial):
    tempo_atual = time.time()
    tempo_restante = tempo_duracao - int(tempo_atual - tempo_inicial)
    print(f"Tempo restante: {tempo_restante} segundos")


def mostrar_pontos(pontos):
    print(f"Placar: {pontos[0]} x {pontos[1]}")


def tempo_expirado(tempo_duracao, tempo_inicial):
    return (time.time() - tempo_inicial) > tempo_duracao


def main():
    modo = input(
        "Escolha o modo de jogo: \n 1 -> Player x Machine\n 2 -> Player x Player\n"
    )
    tempo_duracao = input(
        "Escolha a duração do jogo em segundos: \n 1 -> 30\n 2 -> 45\n 3 -> 60\n"
    )

    tempo_duracao = [30, 45, 60][int(tempo_duracao) - 1]

    pontos = [0, 0]
    tempo_inicial = time.time()

    while True:
        os.system('cls||clear')
        if tempo_expirado(tempo_duracao, tempo_inicial):
            break

        mostrar_tempo_restante(tempo_duracao, tempo_inicial)
        mostrar_pontos(pontos)

        escolhas = ["", ""]

        escolhas[0] = ler_escolha("Jogador 1, sua jogada:", pontos, 0, 1, modo)
        if escolhas[0] is None:
            time.sleep(2)
            continue

        if modo == "2":
            escolhas[1] = ler_escolha("Jogador 2, sua jogada:", pontos, 1, 0, modo)
            if escolhas[1] is None:
                time.sleep(2)
                continue
            print(f"Jogador 2 escolheu: {escolhas[1]}")
        else:
            escolhas[1] = random.choice(escolhas_validas)
            print(f"O computador escolheu: {escolhas[1]}")

        print("Jogador 1 escolheu: ", escolhas[0])

        if escolhas[0] == escolhas[1]:
            print("Empate!")
        elif (escolhas[0], escolhas[1]) in win_lose_escolhas:
            print("Jogador 1 - Você venceu!")
            pontos[0] += 1
        else:
            if modo == "2":
                print("Jogador 2 venceu!")
            else:
                print("Computador venceu!")
            pontos[1] += 1

        time.sleep(3)

    print("Fim de jogo!")
    mostrar_pontos(pontos)

    if pontos[0] == pontos[1]:
        print("O jogo terminou em empate!")
    else:
        vencedor = 1 if pontos[0] > pontos[1] else 2
        if modo == "1":
            print("Você ganhou!" if vencedor == 1 else "Você perdeu!")
        else:
            print(f"Jogador {vencedor} venceu!")


if __name__ == "__main__":
    main()
