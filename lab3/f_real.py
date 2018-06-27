import random, math

# сторона куба: a = 1
# висота куба:  h = 1/math.pow(a, 2)


def gen_xy(n):
    """Генеруємо пари (х,у)"""
    X = [random.random() for i in range(n)]
    Y = [random.random() for j in range(n)]
    return X, Y


def mean(N):
    """Математичне очікування"""
    s = 0
    for i in N:
        s += i
    m = s/len(N)
    return m


def cov(X, Y):
    """Коваріація"""
    n = 0
    for i in range(len(X)):
        n += ((X[i] - mean(X)) * (Y[i] - mean(Y)))
    n = n/len(X)
    return n


def deviation(N):
    """Середньоквадратичне відхлення"""
    v = 0
    m = mean(N)
    for i in range(len(N)):
        v += math.pow((N[i] - m), 2)
    v = v/len(N)
    return math.sqrt(v)


def corel(X,Y):
    """Коефіцієнт кореляції"""
    return cov(X, Y) / (deviation(X) * deviation(Y))

