import time
import os
import random

win_lose_escolhas = [('tesoura', 'papel'),
                     ('papel', 'pedra'),
                     ('pedra', 'tesoura'),
                     ('pedra', 'lagarto'),
                     ('lagarto', 'spock'),
                     ('spock', 'tesoura'),
                     ('tesoura', 'lagarto'),
                     ('lagarto', 'papel'),
                     ('papel', 'spock'),
                     ('spock', 'pedra'),]

def main():
    modo = input('Escolha o modo de jogo: \n 1 -> Player x Machine\n 2 -> Player x Player\n')
    tempo_duracao = 10

    # Estado do jogo
    pontos = [0, 0]
    tempo_inicial = time.time()

    escolhas = ('pedra', 'papel', 'tesoura', 'lagarto', 'spock')

    while True:
        os.system('clear')
        tempo_atual = time.time()
        if (tempo_atual - tempo_inicial) > tempo_duracao:
            break

        escolha_computador = random.choice(escolhas)

        print(f"Tempo restante: {tempo_duracao - int(tempo_atual - tempo_inicial)} segundos")

        print('Digite um número abaixo: ')
        print(' 0 -> pedra\n 1 -> papel\n 2 -> tesoura\n 3 -> lagarto\n 4 -> spock')

        jogador = int(input('Sua escolha: '))

        escolha_jogador = escolhas[jogador]


        print('Sua escolha foi: ', escolha_jogador )
        print('O computador escolheu: ', escolha_computador)

        if escolha_computador == escolha_jogador:
            print("It's a tie!")
        elif (escolha_jogador, escolha_computador) in win_lose_escolhas:
            print('You won!')
            pontos[0] += 1
        else:
            pontos[1] += 1
        time.sleep(1)

    resultado = 'You won!' if pontos[0] > pontos[1] else 'You lose!' if pontos[0] < pontos[1] else "It's a tie!"

    print(f"Placar final: {pontos[0]} x {pontos[1]}")

    print(resultado)


if __name__ == '__main__':
    main()
