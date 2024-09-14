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
escolha = ('pedra', 'papel', 'tesoura', 'lagarto', 'spock')
escolha_computaor = random.choice(escolha)

print('Digite um número abaixo:')
print(' 0 -> pedra\n 1 -> papel\n 2 -> tesoura\n 3 -> lagarto\n 4 -> spock')

jogador = int(input('Sua escolha: '))
escolha_jogador = escolha[jogador]

if escolha_computaor == escolha_jogador:
    resultado = 'Draw!'
elif (escolha_jogador, escolha_computaor) in win_lose_escolhas:
    resultado = 'You Won!'
else:
    resultado = 'You Lost!'

print('Sua escolha foi: ', escolha_jogador )
print('O computador escolheu: ', escolha_computaor)
print(resultado)
