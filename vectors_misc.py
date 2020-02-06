
import math as m


def vadd(v1, v2):
    return [v1[i] + v2[i] for i in range(len(v1))]


def vsub(v1, v2):
    return [v1[i] - v2[i] for i in range(len(v1))]


def vscale(v, k):
    sum = 0
    for i in range(len(v)):
        sum += v[i] * v[i]
    length = m.sqrt(sum)
    return [v[i] / length * k for i in range(len(v))] if length != 0 else [0] * len(v)
