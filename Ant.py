
import random as rnd

rnd.seed()


class Ant:

    def __init__(self):
        self.res = {}
        self.value = 0
        self.fit = 0

    @staticmethod
    def init_colony(count):
        colony = []
        for i in range(count):
            colony.append(Ant())
        return colony

    @staticmethod
    def clear_colony(colony):
        for ant in colony:
            ant.res = []
            ant.fit = 0

    @staticmethod
    def calc_prob(pheromone, a, c):
        return pow(c + pheromone, a)

    def copy(self):
        copy = Ant()
        copy.res = self.res.copy()
        copy.fit = self.fit
        return copy
