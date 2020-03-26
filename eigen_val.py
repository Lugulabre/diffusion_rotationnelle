import math
import numpy as np
import numpy.linalg as alg

def scalaire(vecA, vecB):
    """
    Calcule le produit scalaire de deux vecteurs
    """
    vec_scal = 0
    for coor in range(0,len(vecA.A)):
        vec_scal += vecA.A[0][coor] * vecB.A[0][coor]
    return vec_scal

def eig_val(matrix_cov):
    #Récupère le premier vecteur propre de la matrice au temps t0
    vec_ini = alg.eig(matrix_cov['t0'])[1][0]
    #Création du dictionnaire de valeurs propres
    dico_eigval = {}
    dico_eigval["t0"] = vec_ini
    for i in range(1, len(matrix_cov)):
        temp = 't' + str(i)
        """
        Vérification de la colinéarité entre les temps t et t+1
        Si le produit scalaire est négatif, on enregistre l'inverse du vecteur propre calculé
        """
        if scalaire(vec_ini,alg.eig(matrix_cov[temp])[1][0]) > 0:
            dico_eigval[temp] = alg.eig(matrix_cov[temp])[1][0]
        else:
            dico_eigval[temp] = -alg.eig(matrix_cov[temp])[1][0]
        vec_ini = alg.eig(matrix_cov[temp])[1][0]
    return dico_eigval