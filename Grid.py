
import random as rnd


class Grid:

    def __init__(self, dims, bounds, prec):
        self.prec = prec
        self.dimensions = []
        for d in range(dims):
            step = (bounds[d][1] - bounds[d][0]) / prec
            dimension = {
                "from_bound": bounds[d][0],
                "to_bound": bounds[d][1],
                "step": step,
                "pheromones": []
            }
            for p in range(prec):
                pheromone = rnd.random() / 100
                dimension["pheromones"].append(pheromone)
            self.dimensions.append(dimension)

    def weather_pheromone(self, coef):
        for dim in self.dimensions:
            for p in dim["pheromones"]:
                p *= coef

    def leave_pheromone(self, ants):
        i = 1
        for dim in self.dimensions:
            for p in range(self.prec):
                from_bound = dim["from_bound"] + p * dim["step"]
                to_bound = from_bound + dim["step"]
                for ant in ants:
                    if from_bound <= ant.res["d{}".format(i)] <= to_bound:
                        dim["pheromones"][p] += ant.fit
            i += 1
