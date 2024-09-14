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


def ler_escolha():
    print("Digite um número abaixo: ")
    print(" 0 -> pedra\n 1 -> papel\n 2 -> tesoura\n 3 -> lagarto\n 4 -> spock")

    escolha = int(input("Sua escolha: "))

    return escolhas_validas[escolha]


def main():
    modo = input(
        "Escolha o modo de jogo: \n 1 -> Player x Machine\n 2 -> Player x Player\n"
    )
    tempo_duracao = input(
        "Escolha a duração do jogo em segundos: \n 1 -> 30\n 2 -> 45\n 3 -> 60\n"
    )

    tempo_duracao = [30, 45, 60][int(tempo_duracao) - 1]

    # Estado do jogo
    pontos = [0, 0]
    tempo_inicial = time.time()

    while True:
        os.system("clear")
        tempo_atual = time.time()
        if (tempo_atual - tempo_inicial) > tempo_duracao:
            break

        escolhas = ["", ""]

        print(
            f"Tempo restante: {tempo_duracao - int(tempo_atual - tempo_inicial)} segundos"
        )

        print("Vez do jogador 1")
        escolhas[0] = ler_escolha()
        if modo == "2":
            print("Vez do jogador 2")
            escolhas[1] = ler_escolha()
        else:
            escolhas[1] = random.choice(escolhas_validas)

        print("Sua escolha foi: ", escolhas[0])
        print("O computador escolheu: ", escolhas[1])

        if escolhas[0] == escolhas[1]:
            print("It's a tie!")
        elif (escolhas[0], escolhas[1]) in win_lose_escolhas:
            print("Jogador 1 - You won!")
            pontos[0] += 1
        else:
            if modo == "2":
                print("Jogador 2 - You won!")
            else:
                print("Computador ganhou")
            pontos[1] += 1
        time.sleep(3)

    resultado = (
        "You won!"
        if pontos[0] > pontos[1]
        else "You lose!" if pontos[0] < pontos[1] else "It's a tie!"
    )

    print(f"Placar final: {pontos[0]} x {pontos[1]}")

    print(resultado)


if __name__ == "__main__":
    main()
