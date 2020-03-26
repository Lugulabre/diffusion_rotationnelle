def covar(a, b):
    """
    Prend en argument 2 dictionnaires de coordonnees pour 1 temps
    et renvoie la covariance (variance si la meme est fourni 2 fois)
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