# This is a sample Python script.

import os
import time

import constant
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.

from Game import *
from GreedyBot import GreedyBot

if __name__ == '__main__':
    score = []
    max_value = {2: 0, 4: 0, 8: 0, 16: 0, 32: 0, 64: 0, 128: 0, 256: 0, 512: 0, 1024: 0, 2048: 0}
    for _ in range(1):
        game = Game()
        bot = GreedyBot()
        while True:
            os.system('cls')
            print(f'Score: {game.get_score()}')
            board = game.get_board()
            for row in range(constant.LENGTH_OF_SQUARE):
                for column in range(constant.LENGTH_OF_SQUARE):
                    print(board[row][column], end=" ")
                print()
            if game.is_win():
                print("You win!!!")
                break
            # while True:
            #     moving = constant.DOWN
            #     status1 = game.is_change(game.move(moving))
            #     moving = constant.LEFT
            #     status2 = game.is_change(game.move(moving))
            #     if not status1 and not status2:
            #         break
            moving, val = bot.predict(game, 3)
            status = game.is_change(game.move(moving))
            if not status:
                break
            # time.sleep(0.75)
        score.append(game.get_score())
        max_value[game.get_max_value()] = max_value[game.get_max_value()] + 1

    print(sum(score)/len(score))
    print(max_value)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
