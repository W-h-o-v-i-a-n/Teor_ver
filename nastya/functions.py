import numpy as np


def random_a():
    """Random gener matrix a"""

    from random import random
    a = np.empty((4, 4))
    for i in range(4):
        for j in range(4):
            a[i][j] = round(random(), 3)

    for i in range(4):
        if a[i][0] + a[i][1] + a[i][2] + a[i][3] <= 1:
            a[i][3] = 1 - (a[i][0]+a[i][1]+a[i][2])
        elif a[i][0] + a[i][1] + a[i][2] + a[i][3] > 1:
            if a[i][0] + a[i][1] > 1:
                a[i][0] = round(random()/2, 3)
                a[i][1] = round(random()/6, 3)
                a[i][2] = round(random()/4, 3)
            a[i][3] = 1 - (a[i][0]+a[i][1]+a[i][2])
    return a


def coef_matrix(a):
    """Counts the coefficients of the system of equations"""

    kM = [[1, 1, 1, 1, 1],
          [-(a[0][1]+a[0][2]+a[0][3]), a[1][0], a[2][0], a[3][0], 0],
          [a[0][1], -(a[1][0]+a[1][2]+a[1][3]), a[2][1], a[3][1], 0],
          [a[0][2], a[1][2], -(a[2][0]+a[2][1]+a[2][3]), a[3][2], 0]]
    for i in range(len(kM)):
        for j in range(len(kM[i])):
            kM[i][j] = round(kM[i][j], 3)

    return kM


def count_probabilities(kM):
    """Counts probabilities P1, P2, P3, P4"""

    M = [[kM[0][0], kM[0][1], kM[0][2], kM[0][3]],
         [kM[1][0], kM[1][1], kM[1][2], kM[1][3]],
         [kM[2][0], kM[2][1], kM[2][2], kM[2][3]],
         [kM[3][0], kM[3][1], kM[3][2], kM[3][3]]]

    V = [kM[0][4], kM[1][4], kM[2][4], kM[3][4]]

    return np.linalg.solve(M, V)


def model_sys(a):
    """Matrix for experimental modeling of the system"""

    ms = [[a[0][0], a[0][0] + a[0][1], a[0][0] + a[0][1] + a[0][2], 1],
          [a[1][0], a[1][0] + a[1][1], a[1][0] + a[1][1] + a[1][2], 1],
          [a[2][0], a[2][0] + a[2][1], a[2][0] + a[2][1] + a[2][2], 1],
          [a[3][0], a[3][0] + a[3][1], a[3][0] + a[3][1] + a[3][2], 1]]
    return ms


def experiment(ms, n=10000):
    """Model of the system"""

    from random import random
    s1, s2, s3, s4 = 1, 0, 0, 0
    state = 0

    for i in range(n):
        r = random()
        for j in ms[state]:
            if j > r:
                if ms[state].index(j) == 0: s1 += 1
                elif ms[state].index(j) == 1: s2 += 1
                elif ms[state].index(j) == 2: s3 += 1
                elif ms[state].index(j) == 3: s4 += 1
                state = ms[state].index(j)
                break

    return s1/(s1+s2+s3+s4), s2/(s1+s2+s3+s4), s3/(s1+s2+s3+s4), s4/(s1+s2+s3+s4)

