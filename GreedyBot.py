import constant
from Game import *
import copy
import numpy as np


class GreedyBot:
    def __init__(self):
        self.__greedy_board = [[4**10, 4**5, 4**4, 4**3],
                               [4**13, 4**4, 4**3, 4**2],
                               [4**15, 4**3, 4**2, 4**1],
                               [4**20, 4**2, 4**1, 4**0]]

    def __calculate_greedy_score(self, moving, game):
        g = copy.deepcopy(game)
        t = g.move(moving)
        yield int(np.sum(np.array(g.get_board()) * np.array(self.__greedy_board)))
        yield g.is_change(t)
        yield g

    def predict(self, game, remaining_time):
        remaining_time -= 1
        mx = 0
        moving = constant.UP
        for the_move in constant.MOVE:
            (value, change, g) = self.__calculate_greedy_score(the_move, game)
            if change:
                if remaining_time > 0:
                    mov, value = self.predict(g, remaining_time)
                if value > mx:
                    mx = value
                    moving = the_move

        return moving, mx
