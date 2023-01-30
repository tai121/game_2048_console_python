# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.

from Game import *

if __name__ == '__main__':
    game = Game()
    while not game.is_end():
        print(f'Score: {game.get_score()}')
        board = game.get_board()
        for row in range(constant.LENGTH_OF_SQUARE):
            for column in range(constant.LENGTH_OF_SQUARE):
                print(board[row][column], end=" ")
            print()
        moving = input('your move: ')
        game.move(moving)
    print('end game')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
