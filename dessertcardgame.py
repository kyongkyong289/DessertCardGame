import os
import sys
import traceback
import curses
import random

class Unit:
    attack = 0
    hp = 0
    max_hp = 0
    pos = [0, 0]
    
    def __init__(self, init_attack, init_hp, init_pos):
        self.attack = init_attack
        self.hp = init_hp
        self.max_hp = init_hp
        self.pos = init_pos

class Card:
    cost = 0
    name = ''

    def __init__(self, init_cost, init_name):
        self.cost = init_cost
        self.name = init_name

class Hero:
    attack = 0
    hp = 0
    max_hp = 0
    pos = [0, 0]
    hand = []

    def __init__(self, init_attack, init_hp, init_pos):
        self.attack = init_attack
        self.hp = init_hp
        self.max_hp = init_hp
        self.pos = init_pos

def display_board(target_board):
    for i in range(len(target_board)):
        for j in range(len(target_board[0])):
            window.addstr(2 * i + 1, 2 * j + 1, target_board[i][j])
    
def display_hand(target_hand):
    for i in range(len(target_hand)):
        window.addstr(15, 10 * i + 1, str(target_hand[i].cost))
        window.addstr(16, 10 * i + 1, str(target_hand[i].name))

def display_status(target_unit):
    window.addstr(20, 1, "Hello")

try:
    window = curses.initscr()
    curses.echo()
    curses.nocbreak()
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    window.keypad(True)

    map_board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']] 

    map_board_unit = [[None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None]]

    player = Hero(2, 15, [2, 1])

    for i in range(2):
        card_temp = Card(2, 'fireball')
        player.hand += [card_temp]

    player.hand[0].cost = 4

    while 1:
        map_board[player.pos[0]][player.pos[1]] = 'H'

        window.erase()
        display_board(map_board)
        display_hand(player.hand)
        window.addstr(21, 0, str(player.hp))
        window.refresh()

        window.move(17, 0)

        a = window.getch()

        break

    curses.endwin()
    sys.exit()

except:
    curses.endwin()
    traceback.print_exc()
    sys.exit()