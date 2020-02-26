def mat_cov(x, y, z):
    """
    Cette fonction necessite Numpy importe comme np
    Prend comme argument les dictionnaires de coordonnees avec tous les temps
    """
    mat_dict = {}
    for i in range(0, len(x)):
        temp = 't' + str(i)
        mat_topline = np.array([covar(x[temp], x[temp]), covar(x[temp], y[temp]), covar(x[temp], z[temp])])
        mat_midline = np.array([covar(y[temp], x[temp]), covar(y[temp], y[temp]), covar(y[temp], z[temp])])
        mat_botline = np.array([covar(z[temp], x[temp]), covar(z[temp], y[temp]), covar(z[temp], z[temp])])
        mat_dict[temp] = np.array([mat_topline, mat_midline, mat_botline])
    return mat_dict
