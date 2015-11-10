__author__ = 'Crismaru Paula'

import operator
import sys
from random import randint

class Backgammon:
    def __init__(self):
        self.board = [24]
        for i in range(0, 24):
            self.board.append({'pieces': 0, 'color': '0'})
        self.board[0]={'pieces': 5, 'color': 'white'}
        self.board[4]={'pieces': 3, 'color': 'black'}
        self.board[6]={'pieces': 5, 'color': 'black'}
        self.board[11]={'pieces': 2, 'color': 'white'}
        self.board[12]={'pieces': 5, 'color': 'black'}
        self.board[16]={'pieces': 3, 'color': 'white'}
        self.board[18]={'pieces': 5, 'color': 'white'}
        self.board[23]={'pieces': 2, 'color': 'black'}

    def print_board(self):
        hi = 0
        for x in (item['pieces'] for item in self.board[11:]):
            hi = max(x,hi)
        for level in range(0, hi):
            for i in range(0,12):
                if level+1 <= self.board[i]['pieces']:
                    if self.board[i]['color'] == 'white':
                        print('o ', end="")
                    elif self.board[i]['color'] == 'black':
                        print('x ', end="")
                else:
                    if level == 0:
                        print("- ", end="")
                    else:
                        print("  ", end="")
                if i == 5:
                    print("| ", end="")
            print("")
        hi = 0
        for x in (item['pieces'] for item in self.board[:12]):
            hi = max(x,hi)
        for level in range(hi, -1, -1):
            for i in range(12,24):
                if level+1 <= self.board[i]['pieces']:
                    if self.board[i]['color'] == 'white':
                        print('o ', end="")
                    elif self.board[i]['color'] == 'black':
                        print('x ', end="")
                else:
                    if level == 0:
                        print("- ", end="")
                    else:
                        print("  ", end="")
                if i == 17:
                    print("| ", end="")
            print("")

    def roll_dice(self):
        self.dice1 = randint(1, 6)
        self.dice2 = randint(1, 6)
        print(self.dice1, " ", self.dice2)



game = Backgammon()
game.print_board()
game.roll_dice()