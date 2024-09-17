
import curses
from enum import Enum
import time
from typing import List


REFRESH_TIME = 0.01


# Wrapper da nossa aplicação para o módulo curses
class UserInterface:
    def __init__(self, stdscr):
        self.stdscr = stdscr

        self.GREEN_PAIR = 1
        self.YELLOW_PAIR = 2
        self.RED_PAIR = 3

        self.GREEN_FOREGROUND = 4
        self.YELLOW_FOREGROUND = 5
        self.RED_FOREGROUND = 6

        self.REVERSE_MODE = curses.A_REVERSE
        self.NORMAL_MODE = curses.A_NORMAL

        curses.init_pair(self.GREEN_PAIR,  curses.COLOR_WHITE, curses.COLOR_GREEN,)
        curses.init_pair(self.YELLOW_PAIR, curses.COLOR_BLACK,  curses.COLOR_YELLOW)
        curses.init_pair(self.RED_PAIR, curses.COLOR_WHITE, curses.COLOR_RED)
        curses.init_pair(self.GREEN_FOREGROUND, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(self.YELLOW_FOREGROUND, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(self.RED_FOREGROUND, curses.COLOR_RED, curses.COLOR_BLACK)

    def set_nonblocking(self, nonblocking: bool):
        self.stdscr.nodelay(nonblocking)

    def clear(self):
        self.stdscr.clear()

    def sleep(self, timeout = REFRESH_TIME):
        time.sleep(timeout)

    def refresh(self):
        self.stdscr.refresh()

    def display(self, text, mode = curses.A_NORMAL):
        self.stdscr.addstr(text, mode)

    def colored_display(self, text, color_pair):
        self.stdscr.addstr(text, curses.color_pair(color_pair))

    def menu(self, title, opcoes: List[str]):
        highlight = 0

        while True:
            self.display(title + "\n\n")
            for idx, opcao in enumerate(opcoes):
                mode = curses.A_REVERSE if idx == highlight else curses.A_NORMAL
                self.display(f"{opcao}\n", mode)

            tecla = self.getch()

            self.sleep()

            if tecla == curses.KEY_UP:
                # Usamos esse operador de resto da divisão pra garantir
                # que o highlight não ultrapasse os limites da lista
                highlight = (highlight - 1) % len(opcoes)
            elif tecla == curses.KEY_DOWN:
                highlight = (highlight + 1) % len(opcoes)
            elif tecla in [10, 13]: # Enter do curses não funciona aqui
                self.clear()
                self.refresh()
                return highlight
            self.clear()
            self.refresh()

    def getch(self):
        return self.stdscr.getch()

    def getkey(self):
        return self.stdscr.getkey()
