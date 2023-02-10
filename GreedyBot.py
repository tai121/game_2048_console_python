import constant
from Game import *
import copy
import numpy as np


class GreedyBot:
    def __init__(self):
        self.__greedy_board = [[4**6, 2**5, 2**4, 2**3],
                               [4**8, 2**4, 2**3, 2**2],
                               [4**10, 2**3, 2**2, 2**1],
                               [4**13, 4**2, 4**1, 2**0]]

    def __calculate_greedy_score(self, moving, game):
        g = copy.deepcopy(game)
        t = g.move(moving)
        yield int(np.sum(np.array(g.get_board()) * np.array(self.__greedy_board)))
        yield g.is_change(t)

    def predict(self, game):
        mx = 0
        moving = constant.UP
        (value, change) = self.__calculate_greedy_score(constant.UP, game)
        if change:
            mx = value
            moving = constant.UP

        (value, change) = self.__calculate_greedy_score(constant.DOWN, game)
        if mx < value and change:
            moving = constant.DOWN
            mx = value

        (value, change) = self.__calculate_greedy_score(constant.LEFT, game)
        if mx < value and change:
            moving = constant.LEFT
            mx = value

        (value, change) = self.__calculate_greedy_score(constant.RIGHT, game)
        if mx < value and change:
            moving = constant.RIGHT

        return moving
