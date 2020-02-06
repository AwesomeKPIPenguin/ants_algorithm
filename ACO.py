
from Grid import Grid
from Ant import Ant
import random as rnd
import time
from matplotlib import pyplot as plt


def main_ACO(ft, dimensions, bounds, dim_prec, stop_prec, a, c, w, ant_count, fitness, timeout):
    ants = Ant.init_colony(ant_count)
    best_fit_per_gen = 0
    grid = Grid(dimensions, bounds, dim_prec)
    precs = [10e-2, 10e-3, 10e-4, 10e-5, 10e-6, 10e-7, 10e-8, 10e-9]
    precs_len = len(precs)
    curr_prec_i = 0
    iters = [0] * precs_len
    best_ants = []
    best_ant = Ant()
    best_ant.value = 100
    # time_start = time.process_time()
    duration = 1
    # res = {}
    # plt_value = [0] * (timeout + 1)
    # plt_iter = [i for i in range(timeout + 1)]
    best_fit = 0
    best_value = 0
    while (best_ant.value > -1 + precs[-1]) and (duration < timeout): #
        for ant in ants:
            ant.res = {}
            j = 0
            for dim in grid.dimensions:
                j += 1
                probs = []
                total = 0
                for r in range(dim_prec):
                    prob = Ant.calc_prob(dim["pheromones"][r], a, c)
                    probs.append(prob)
                    total += prob
                r = rnd.random()
                for rng in range(grid.prec):
                    prob = (probs[rng] / total if total != 0 else 0)
                    if r <= prob:
                        range_start = dim["from_bound"] + rng * dim["step"]
                        ant.res["d{}".format(j)] = range_start + rnd.random() * dim["step"]
                        break
                    else:
                        r -= prob
            ant.value = ft(list(ant.res.values()))
            ant.fit = fitness(ant.value)
        best_ant = max(ants, key=lambda p: p.fit)

        if best_ant.fit > best_fit:
            best_fit = best_ant.fit
            best_value = best_ant.value

        best_ants.append(best_ant.copy())
        best_fit_per_gen = best_ant.fit
        grid.weather_pheromone(w)
        grid.leave_pheromone(ants)
        Ant.clear_colony(ants)
        # duration = time.process_time() - time_start

        # plt_value[duration] = best_ant.value

        while curr_prec_i < precs_len and best_ant.value < -1 + precs[curr_prec_i]: #
            iters[curr_prec_i] = duration
            curr_prec_i += 1
        if curr_prec_i == precs_len:
            break
        duration += 1

    best_ant = max(best_ants, key=lambda p: p.fit)
    best_ant.value = ft(list(best_ant.res.values()))
    res = {
        "params": best_ant.res,
        "value": best_ant.fit,
        "fvalue": best_ant.value,
        "iters": iters
        # "time": time.process_time() - time_start
    }

    # plt_value[0] = plt_value[1]
    # # for value in plt_value:
    # #     value *= 1000
    # # plt.set_ylabel("value")
    # # plt.set_xlabel("iteration")
    # plt.plot(plt_iter, plt_value, c="blue")
    # plt.plot([0, timeout - 1], [0, 0], "--", c="red")
    # plt.show()

    return res
