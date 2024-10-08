# Sheldon - Pedra, papel, tesoura, lagarto, Spock

Pedra, papel e tesoura modificado, projeto desenvolvido para a disciplina de Linguagem de Programação I

## Como rodar

Clone o repositório e entre na pasta do projeto

```bash
git clone https://github.com/OPr0fi/projeto_sheldon.git
cd projeto_sheldon
```

Se estiver no windows, é necessário instalar a biblioteca curses

```bash
pip install windows-curses
python app.py
```

Porém eu recomendo fortemente o uso de Unix ou WSL, onde a biblioteca já vem instalada.

```bash
python3 app.py
```

## Como jogar

O jogo é uma variação do clássico pedra, papel e tesoura, com a adição de duas novas opções: lagarto e Spock.
Você vai decidir se quer jogar Singleplayer ou Multiplayer e a duração do jogo

## Organização do código

O código foi dividido em 5 arquivos:

- `app.py`: Arquivo principal, onde o jogo é executado

- `game.py`: Onde a lógica do jogo é implementada

- `jogador.py`: Onde a classe Player é definida

- `ui.py`: Onde todas as funções de interface com o usuário são definidas

- `escolha.py`: Onde as escolhas possíveis do jogo são definidas
