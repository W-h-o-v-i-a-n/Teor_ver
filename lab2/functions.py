from random import random
from math import sqrt


def gen_y():
    y = -6
    for i in range(12):
        y += random()
    return y


def gen_random_number(m: int, sigma: int):
    r = sigma*gen_y() + m
    return r


def count_m(row: list):
    M = 0
    for i in row:
        M += i
    return M / len(row)


def count_sigma(row: list, m: int):
    SIGMA = 0
    for i in row:
        SIGMA += (i - m)**2
    return sqrt(SIGMA/len(row))

