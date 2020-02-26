def covar(a, b):
    """
    prend en argument 2 dictionnaires de coordonnees pour 1 temps
    et renvoit la covariance (variance si la meme est fournit 2 fois)
    Exemple: covar(x['t0'], y['t0'])
    Cette fonction recalcule les moyennes obtenues apres centrage
    A revoir: si on divise par n ou n-1
    """
    var_mat = {}
    curr_var = 0
    a_mean = (sum(a.values())/len(a))
    b_mean = (sum(b.values())/len(b))
    for j in range(1, len(a)):
        curr_var += (a[j] - a_mean)*(b[j] - b_mean)
    curr_var = curr_var/len(a)
    return curr_var