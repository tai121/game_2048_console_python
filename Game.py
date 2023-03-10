import constant
from collections import deque
import random
import copy


class Game:

    def __init__(self):
        self.__board = list(list(0 for _ in range(constant.LENGTH_OF_SQUARE)) for _ in range(constant.LENGTH_OF_SQUARE))
        self.__max_value = 0
        self.__score = 0
        self.__blank_space = constant.LENGTH_OF_SQUARE ** 2
        self.__generate_new_square()

    def move(self, moving):
        check_board = copy.deepcopy(self.__board)
        edge_longer = range(constant.LENGTH_OF_SQUARE)
        is_vertical = True if moving == constant.DOWN or moving == constant.UP else False
        is_revere = True if moving == constant.RIGHT or moving == constant.DOWN else False
        edge_shorter = range(constant.LENGTH_OF_SQUARE - 2, -1, -1) if is_revere else range(1,
                                                                                            constant.LENGTH_OF_SQUARE,
                                                                                            1)
        self.__blank_space = 0
        for i in edge_longer:
            x, y = i, constant.LENGTH_OF_SQUARE - 1 if is_revere else 0
            x, y = (y, x) if is_vertical else (x, y)
            for j in edge_shorter:
                u, v = (j, i) if is_vertical else (i, j)
                if self.__board[u][v] == 0:
                    continue
                if self.__board[x][y] == self.__board[u][v]:
                    self.__board[x][y] *= 2
                    self.__score += self.__board[x][y]
                    self.__board[u][v] = 0
                    self.__max_value = max(self.__max_value, self.__board[x][y])
                x, y = u, v

        edge_shorter = range(constant.LENGTH_OF_SQUARE - 1, -1, -1) if is_revere else range(constant.LENGTH_OF_SQUARE)
        for i in edge_longer:
            list_blank_squares = deque()
            for j in edge_shorter:
                u, v = (j, i) if is_vertical else (i, j)
                if self.__board[u][v] == 0:
                    list_blank_squares.append((u, v))
                    continue
                if len(list_blank_squares) != 0:
                    x, y = list_blank_squares.popleft()
                    self.__board[x][y] = self.__board[u][v]
                    self.__board[u][v] = 0
                    list_blank_squares.append((u, v))
            self.__blank_space += len(list_blank_squares)
        return check_board

    def is_change(self, check_board):
        for row in range(constant.LENGTH_OF_SQUARE):
            for column in range(constant.LENGTH_OF_SQUARE):
                if self.__board[row][column] != check_board[row][column]:
                    self.__generate_new_square()
                    return True
        return False

    def __generate_new_square(self):
        position = random.randint(1, self.__blank_space)
        two_or_four = (random.randint(1, 10) % 8 != 0)
        count = 0
        for row in range(constant.LENGTH_OF_SQUARE):
            for column in range(constant.LENGTH_OF_SQUARE):
                if self.__board[row][column] == 0:
                    count += 1
                    if count == position:
                        self.__board[row][column] = 4 - two_or_four * 2
                        self.__max_value = max(self.__max_value, self.__board[row][column])
                        self.__blank_space -= 1

    def get_board(self):
        return self.__board

    def get_score(self):
        return self.__score

    def is_end(self):
        if self.__blank_space > 0:
            return False
        for row in range(constant.LENGTH_OF_SQUARE - 1):
            for column in range(constant.LENGTH_OF_SQUARE - 1):
                if self.__board[row][column] == self.__board[row + 1][column] or self.__board[row][column] == \
                        self.__board[row][column + 1]:
                    return False
        return True

    def is_win(self):
        if self.__max_value == 2048:
            return True
        return False

    def get_max_value(self):
        return self.__max_value
