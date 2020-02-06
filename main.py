
import ACO
import meta
import pprint as pp
import math as m
from matplotlib import pyplot as plt


# functions to test

def ft_sphere(params):
    return pow(params[0], 2) + pow(params[1], 2)


def ft_cosines(params):
    return m.fabs(m.cos(params[0]))


def ft_rastrigin(params):
    return 20 + pow(params[0], 2) - 10 * m.cos(2 * m.pi * params[0])\
              + pow(params[1], 2) - 10 * m.cos(2 * m.pi * params[1])


def ft_levi_13(params):
    return pow(m.sin(3 * m.pi * params[0]), 2) + pow(params[0] - 1, 2) * (1 + pow(m.sin(3 * m.pi * params[1]), 2))\
                                               + pow(params[1] - 1, 2) * (1 + pow(m.sin(2 * m.pi * params[1]), 2))


def ft_easom(params):
    return -m.cos(params[1]) * m.cos(params[0]) * m.exp(-(pow(params[0] - m.pi, 2) + pow(params[1] - m.pi, 2)))

# fitness stuff

def fitness(value):
    return 0.75 * (1 / (1 + m.fabs(value[0]) / stop_prec)) + 0.25 * (1 - (value[1] / timeout))


def fit_min_value(value):
    return 1 / (1 + (m.fabs(-1 - value)))


def fit_min_time(time):
    return 1 - time / timeout


# dim_prec, a, c, w, ant_count
# d = 3  # a, dim_prec, ant_count
# bounds = [[0, 2], [1, 201], [100, 1100]]
# dim_prec = 10
# m_stop_count = 100
# stop_prec = 10e-3
# timeout = 5

# ft, dimensions, bounds, dim_prec, m_stop_count, stop_prec, m_fitness, timeout
# pp.pprint(meta.meta_aco(ACO.main_ACO, d, bounds, dim_prec, m_stop_count, stop_prec, fitness, timeout))
# meta.meta_pso(ACO.main_ACO, ft_levi_13, d, bounds, m_stop_count, stop_prec, [fit_min_value, fit_min_time], timeout)

# res_count = 10
# avar_fit = 0
# avar_time = 0
# for i in range(res_count):
#     temp_res = ACO.main_ACO(ft_easom, 2, [[-100, 100], [-100, 100]], 201, 10e-3, 0.5, 0.3, 0.25, 500, fit_min_value, 5)
#     avar_fit += temp_res["value"]
#     avar_time += temp_res["time"]
# avar_fit /= res_count
# avar_time /= res_count
# print("Function: easom\nIterations: {}\nAverage fitness: {}\nAverage time: {}".format(res_count, avar_fit, avar_time))


# pp.pprint(ACO.main_ACO(ft_rastrigin, 2, [[-10, 10], [-10, 10]], 803, 0, 1, 0.1, 0.75, 200, fit_min_value, 500))


# ft, dimensions, bounds, dim_prec, stop_prec, a, c, w, ant_count, fitness, timeout
# ares = {"param": 0, "atime": 0, "avalue": 0}
# param_ax = []
# time_ax = []
# ftvalue_ax = []
# for ares["param"] in range(1, 11, 1):
#     ares["atime"] = 0
#     ares["avalue"] = 0
#     for i in range(10):
#         res = ACO.main_ACO(ft_rastrigin, 2, [[-10, 10], [-10, 10]], 41, 1e-3, 1 + ares["param"] / 2, 0.1, 0.75, 100, meta.fitness, 10)
#         ares["atime"] += res["time"]
#         ares["avalue"] += res["value"]
#     ares["param"] = 1 + ares["param"] / 2
#     ares["atime"] /= 10
#     ares["avalue"] /= 10
#     param_ax.append(ares["param"])
#     time_ax.append(ares["atime"])
#     ftvalue_ax.append(ares["avalue"])
#     pp.pprint(ares)
#     # fig = plt.figure()
#     # fig_time = fig.add_subplot(211)
#     # fig_time.plot(param_ax, time_ax, c="r")
#     # fig_time.set_ylabel("time")
#     # fig_value = fig.add_subplot(212)
#     # fig_value.plot(param_ax, ftvalue_ax, c="g")
#     # fig_value.set_xlabel("param value")
#     # fig_value.set_ylabel("ft value")
#     # plt.show()
#     ares["param"] = (ares["param"] - 1) * 2
#
# fig = plt.figure()
# fig_time = fig.add_subplot(211)
# fig_time.plot(param_ax, time_ax, c="r")
# fig_time.set_ylabel("time")
# fig_value = fig.add_subplot(212)
# fig_value.plot(param_ax, ftvalue_ax, c="g")
# fig_value.set_xlabel("param value")
# fig_value.set_ylabel("ft value")
# plt.show()



# compare

# amyres = {"atime": 0, "avalue": 0}
# acalres = {"atime": 0, "avalue": 0}
# count = 1000
# for i in range(count):
#     res = ACO.main_ACO(ft_levi_13, 2, [[-10, 10], [-10, 10]], 21, 10e-3, 1, 0.1, 0.75, 200, fit_min_value, 5)
#     amyres["atime"] += res["time"]
#     amyres["avalue"] += res["value"]
#     res = ACO.main_ACO(ft_levi_13, 2, [[-10, 10], [-10, 10]], 12, 10e-3, 1.885, 0.1, 0.75, 384, fit_min_value, 5)
#     acalres["atime"] += res["time"]
#     acalres["avalue"] += res["value"]
# amyres["atime"] /= count
# amyres["avalue"] /= count
# acalres["atime"] /= count
# acalres["avalue"] /= count
#
# print("my params:")
# pp.pprint(amyres)
# print("calibrated:")
# pp.pprint(acalres)
# print("\ncalibration result:")
# print("time: {} %, value: {} %".format(
#     round(amyres["atime"] / acalres["atime"] * 100, 2),
#     round(acalres["avalue"] / amyres["avalue"] * 100, 2)
# ))



d_precs = [1, 2, 3, 5, 10, 20, 30, 50, 100, 200, 300]
for d_prec in d_precs:
    log = open("easom_analysis.txt", mode="a+")
    log.write("\n" + "d_prec: {}, ants: {} >".format(d_prec, pow(d_prec, 2)) + "\n")
    log.close()
    res = ACO.main_ACO(ft_easom, 2, [[-100, 100], [-100, 100]], d_prec, 0, 0.2, 0.1, 0.25, pow(d_prec, 2), fit_min_value, 1000 if d_prec > 5 else 5000)
    log = open("easom_analysis.txt", mode="a+")
    log.write(str(res) + "\n")
    log.close()
