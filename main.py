# This is a sample Python script.

import os
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.

from Game import *
from GreedyBot import GreedyBot

if __name__ == '__main__':
    score = []
    max_value = []
    for _ in range(100):
        game = Game()
        bot = GreedyBot()
        while True:
            os.system('cls')
            print(f'Score: {game.get_score()}')
            board = game.get_board()
            # for row in range(constant.LENGTH_OF_SQUARE):
            #     for column in range(constant.LENGTH_OF_SQUARE):
            #         print(board[row][column], end=" ")
            #     print()
            if game.is_win():
                print("You win!!!")
                break
            moving = bot.predict(game)
            status = game.is_change(game.move(moving))
            if not status:
                break
        score.append(game.get_score())
        max_value.append(game.get_max_value())
    print(score)
    print(max_value)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
