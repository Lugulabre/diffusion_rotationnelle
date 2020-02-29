import numpy as np

import covar as cv

def mat_cov(x, y, z):
    """
    Cette fonction necessite Numpy importe comme np
    Prend comme argument les dictionnaires de coordonnees avec tous les temps
    """
    mat_dict = {}
    for i in range(0, len(x)):
        temp = 't' + str(i)
        mat_topline = np.array([cv.covar(x[temp], x[temp]), cv.covar(x[temp], y[temp]), cv.covar(x[temp], z[temp])])
        mat_midline = np.array([cv.covar(y[temp], x[temp]), cv.covar(y[temp], y[temp]), cv.covar(y[temp], z[temp])])
        mat_botline = np.array([cv.covar(z[temp], x[temp]), cv.covar(z[temp], y[temp]), cv.covar(z[temp], z[temp])])
        mat_dict[temp] = np.matrix([mat_topline, mat_midline, mat_botline])
    return mat_dict