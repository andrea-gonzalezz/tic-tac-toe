import sys
import copy
import random
import pygame
import numpy as np

from constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)


class Board:

    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_sqrs = self.squares
        self.marked_sqrs = 0

    def final_state(self):
        #Vertical
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] and self.squares[0][col] != 0:
                return self.squares[0][col]
        #Horizontal
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] and self.squares[row][0] != 0:
                return self.squares[row][0]

        #Diagonals
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] and self.squares[0][0] != 0:
            return self.squares[0][0]
        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] and self.squares[0][2] != 0:
            return self.squares[0][2]

        #no win
        return 0


    def mark_square(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1


    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0

    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append((row, col))
        return empty_sqrs


    def isfull(self):
        return self.marked_sqrs == 9

    def isempty(self):
        return self.marked_sqrs == 0



class AI:

    def __init__(self, level = 1, player = 2):
        self.level = level
        self.player = player

    def rnd(self, board):
        empty_sqrs = board.get_empty_sqrs()
        idx = random.randrange(0, len(empty_sqrs))
        return empty_sqrs[idx]

    def minimax(self, board, maximizing):
        case= board.final_state()

        #player 1 wins
        if case == 1:
            return 1, None

        #player 2 wins
        elif case == 2:
            return -1, None

        #draw
        elif board.isfull():
            return 0, None

        if maximizing:
            max_eval = -100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, 1)
                eval = self.minimax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)

            return max_eval, best_move



        elif not maximizing:
            min_eval = 100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row,col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, self.player)
                eval = self.minimax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)

            return min_eval, best_move



    def eval(self, main_board):
        if self.level == 0:
            eval = 'random'
            move = self.rnd(main_board)
        else:
           eval, move = self.minimax(main_board, False)
        print(f'AI has chosen {move} with eval {eval}')

        return move


class Game:

    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1
        self.gamemode = "ai" #pvp or ai
        self.running = True
        self.show_lines()

    def make_move(self, row, col):
        self.board.mark_square(row, col, self.player)
        self.board.draw_fig(row, col)
        self.next_turn()

    def show_lines(self):
        #vertical lines
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (2 * SQSIZE, 0), (2 * SQSIZE, HEIGHT), LINE_WIDTH)

        #horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQSIZE), (WIDTH, 2 * SQSIZE), LINE_WIDTH)

    def draw_fig(self, row, col):
        if self.player == 1:
            pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE),(col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
            pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE),(col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)


        elif self.player == 2:
            center = (col * SQSIZE + SQSIZE//2, row * SQSIZE + SQSIZE//2)
            pygame.draw.circle(screen, CIRCLE_COLOR, center, CIRCLE_RADIUS, CIRCLE_WIDTH)


    def next_turn(self):
        self.player = self.player % 2 + 1

    def change_gamemode(self):
        if self.gamemode == 'ai':
            self.gamemode = 'pvp'
        else:
            self.gamemode = 'pvp'

    def reset(self):
        self.__init__()


def main():
    #Objets
    game = Game()
    board = game.board
    ai = game.ai
    #mainloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE
                print(row,col)

                if board.empty_sqr(row, col):
                    board.mark_square(row, col, game.player)
                    game.draw_fig(row,col)
                    game.next_turn()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.change_gamemode()
                    print(game.gamemode)
                if event.key == pygame.K_0:
                    ai.level = 0

                if event.key == pygame.K_1:
                    ai.level = 1

                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai


        if game.gamemode == 'ai' and game.player == ai.player:
            pygame.display.update()
            row, col = ai.eval(board)
            board.mark_square(row, col, ai.player)
            game.draw_fig(row, col)
            game.next_turn()


        pygame.display.update()



main()