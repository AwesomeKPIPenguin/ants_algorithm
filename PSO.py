
from Particle import Particle
import datetime
import math as m

from matplotlib import pyplot as plt


m_parts = 10000
m_cp = 0.1
m_cs = 0.1
m_cg = 0.25


def ft_rastrigin(params):
    return 20 + pow(params[0], 2) - 10 * m.cos(2 * m.pi * params[0])\
              + pow(params[1], 2) - 10 * m.cos(2 * m.pi * params[1])


def fitness(value):
    return 1 / (1 + value)


def main_pso(ft, dimensions, bounds, stop_prec, count):
    swarm = []
    for i in range(m_parts):
        swarm.append(Particle(bounds))
    gbest = [0] * dimensions
    gbest_fit = 0
    time_start = datetime.datetime.now()
    curr_time = time_start
    # while (curr_time - time_start).seconds < timeout or 1 - gbest_fit < stop_prec:
    for i in range(count):
        # plt.xlim(bounds[0][0], bounds[0][1])
        # plt.ylim(bounds[1][0], bounds[1][1])

        for particle in swarm:
            fit = 0
            particle.update_v(gbest, m_cp, m_cs, m_cg)
            particle.update_pos(bounds)

            # plt.scatter(particle.pos[0], particle.pos[1], marker="o", c="red", s=50)

            ftres = ft(particle.pos)
            fit = fitness(ftres)
            if fit > particle.best_fit:
                particle.best = particle.pos
                particle.best_fit = fit
        for particle in swarm:
            if particle.best_fit > gbest_fit:
                gbest = particle.pos
                gbest_fit = particle.best_fit

        # plt.scatter(gbest[0], gbest[1], marker="o", c="green", s=100)
        # plt.show()

        curr_time = datetime.datetime.now()
        if 1 - gbest_fit < stop_prec:
            break
    return [gbest_fit, gbest, i]


for i in range(10):
    print(main_pso(ft_rastrigin, 2, [[-10, 10], [-10, 10]], 1e-5, 100))
