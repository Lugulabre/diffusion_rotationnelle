import matplotlib.pyplot as plt
from math import exp
import numpy as np

def graphique(corr_dict, file_name, colgraph):

    list_keys = []
    list_values = []
    for cle, valeur in corr_dict.items():
        list_keys.append(cle)
        list_values.append(valeur)
    plt.plot(list_keys[0:100], list_values[0:100], color = colgraph)
    plt.xlabel("pas de temps")
    plt.ylabel("autocorrélation")
    plt.title("Autocorrélation en fonction du temps")
    plt.savefig(file_name)
    #plt.close()