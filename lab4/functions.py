from termcolor import colored


def dispersion(X):
    """Count dispersion"""
    if 4 <= len(X) <= 10:
        an = [2.059, 2.32, 2.55, 2.7, 2.8, 2.95, 3.1]
        return ((max(X)-min(X))/an[len(X)-4])**2
    elif len(X) > 10:
        average_x = sum(X)/len(X)
        return sum(map(lambda x: (x-average_x)**2, X))/(len(X)-1)
    else:
        print(colored('InputError: plural length should be >= 4', 'red'))


def covariance(X: list, Y: list):
    """Count cov"""
    average_x = sum(X)/len(X)
    average_y = sum(Y)/len(Y)
    return sum(map(lambda x, y: (x - average_x)*(y - average_y), X, Y))/len(X)


def create_L(a: list, b: list, y: list):
    """Create cov matrix"""
    L = [[covariance(a, a), covariance(a, b)],
         [covariance(b, a), covariance(b, b)]]

    L1 = [[covariance(a, y), covariance(a, b)],
          [covariance(b, y), covariance(b, b)]]

    L2 = [[covariance(a, a), covariance(a, y)],
          [covariance(b, a), covariance(b, y)]]
    return L, L1, L2


def det_matrix_2x2(m: list):
    """Count determinant of 2x2 matrix"""
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]


def count_coefs(L: list, L1: list, L2: list, X1:list, X2:list, Y:list):
    """Count function`s coefs"""
    b1 = det_matrix_2x2(L1) / det_matrix_2x2(L)
    b2 = det_matrix_2x2(L2) / det_matrix_2x2(L)
    a = sum(Y)/len(Y) - b1*sum(X1)/len(X1) - b2*sum(X2)/len(X2)
    return a, b1, b2
