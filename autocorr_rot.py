import numpy as np

def cos_tau(vect_eig1, vect_eig2):
    """
    Fonction prend en argument 2 vecteurs propres de dim 3
    Elle renvoit le cosinus de leur angle
    Necessite: import numpy as np
    """
    vect_eig1 = np.array(vect_eig1)[0]
    vect_eig2 = np.array(vect_eig2)[0]
    return np.dot(vect_eig1, vect_eig2) / (np.linalg.norm(vect_eig1) * np.linalg.norm(vect_eig2))

def single_autocorr(eig_dict, tau):
    """
    Fonction qui prend en argument un dictionnaire de vect propres et un tau
    Tau correspond au decalage pour le calcul de l'autocorrelation
    La fonction retourne la moyenne des cosinus formes par les vecteurs aux temps
    t et t+tau
    """
    if tau >= len(eig_dict):
        return
    curr_val = 0
    for i in range(0, len(eig_dict)-tau):
        temp = 't' + str(i)
        curr_val += cos_tau(eig_dict[temp], eig_dict['t' + str(i+tau)])
    curr_val = curr_val / (len(eig_dict)-tau)
    return curr_val

def autocorr_rot(eig_dict):
    """
    Fonction prend en argument un dictionnaire de vect propres
    Retourne dictionnaire avec moyennes des cos pour chaque Tau
    Tau va de 0 jusqu'a longueur du dictionnaire-1
    """
    tau_dict = {}
    print(len(eig_dict))
    for tau in range(0, len(eig_dict)):
        tau_dict[tau] = single_autocorr(eig_dict, tau)
        print(tau)
    return tau_dict