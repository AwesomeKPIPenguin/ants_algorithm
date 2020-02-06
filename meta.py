
from Grid import Grid
from Ant import Ant
from Particle import Particle
from pareto import best_tournament
import math as m
import random as rnd
import pprint as pp
import datetime


rnd.seed()

# aco
m_ant_count = 20
m_a = 1
m_c = 0.1
m_w = 0.75

# pso
m_parts = 100
m_cp = 0.1
m_cs = 0.1
m_cg = 0.25


def meta_pso(algorithm, ft, dimensions, bounds, m_stop_count, stop_prec, m_fitness, timeout):
    swarm = []
    for i in range(m_parts):
        swarm.append(Particle(bounds))
    res = {"params": [0] * dimensions, "fit": 0, "value": 100, "time": 100}
    for i in range(m_stop_count):
        tournament = []
        for particle in swarm:
            particle.update_v(res["params"], m_cp, m_cs, m_cg)
            particle.update_pos(bounds)
            ftres = {
                "value": 0,
                "time": 0
            }

            # print("\na: {}, d_prec: {}".format(particle.pos[0], particle.pos[1]))

            lcount = 5
            for j in range(lcount):
                tmpres = algorithm(
                    ft,
                    2,
                    [[-10, 10], [-10, 10]],
                    round(particle.pos[1]),
                    stop_prec,
                    particle.pos[0],
                    0.1,
                    0.75,
                    round(particle.pos[2]),
                    m_fitness[0],
                    timeout
                )
                ftres["value"] += tmpres["fvalue"]
                ftres["time"] += tmpres["time"]
            ftres["value"] /= lcount
            ftres["time"] /= lcount

            tournament.append([particle.pos, [ftres["value"], ftres["time"]]])  # adding result to tournament

            # fit = m_fitness([ftres["value"], ftres["time"]])
            #
            # # print(ftres, fit)
            #
            # if fit > particle.best_fit:
            #     particle.best = particle.pos
            #     particle.best_fit = fit

        board, winner_i = best_tournament(tournament, m_fitness, 2)

        print(tournament[winner_i])

        for j in range(m_parts):
            if board[j] > swarm[j].best_fit:
                swarm[j].best_fit = board[j]
                swarm[j].best = tournament[j][0]
                if swarm[j].best_fit > res["fit"]:
                    res["params"] = swarm[j].best
                    res["fit"] = swarm[j].best_fit
                    res["value"] = tournament[j][1][0]
                    res["time"] = tournament[j][1][1]

        note = "[{}] {}".format(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), res)
        print(note)
        log = open("log.txt", mode="a+")
        log.write(str(note) + "\n")
        log.close()
    return res


def meta_aco(ft, dimensions, bounds, dim_prec, m_stop_count, stop_prec, m_fitness, timeout):
    ants = Ant.init_colony(m_ant_count)
    best_fit_per_gen = 0
    grid = Grid(dimensions, bounds, dim_prec)
    best_ants = []
    best_ant = object
    i = 0
    res = {}
    for ic in range(m_stop_count):
        i += 1
        for ant in ants:
            ant.res = {}
            j = 0
            for dim in grid.dimensions:
                j += 1
                probs = []
                total = 0
                for r in range(dim_prec):
                    prob = Ant.calc_prob(dim["pheromones"][r], m_a, m_c)
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
            ant.res["d2"] = round(ant.res["d2"])
            ft_res = ft(
                ft_rastrigin,
                2,
                [[-10, 10], [-10, 10]],
                ant.res["d2"],
                stop_prec,
                ant.res["d1"],
                0.1,
                0.75,
                50,
                fitness,
                timeout
            )
            ant.fit = m_fitness(list(ft_res.values()))
        best_ant = max(ants, key=lambda p: p.fit)
        pp.pprint(best_ant.res)
        log = open("log.txt", mode="a+")
        log.write(str(best_ant.res) + "\n")
        log.close()
        best_ants.append(best_ant.copy())
        best_fit_per_gen = best_ant.fit
        grid.weather_pheromone(m_w)
        grid.leave_pheromone(ants)
        Ant.clear_colony(ants)
    best_ant = max(best_ants, key=lambda p: p.fit)
    res = {
        "params": best_ant.res,
        "value": best_ant.fit
    }
    return res
