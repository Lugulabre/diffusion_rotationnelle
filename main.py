import sys

import autocorr_rot as arot
import barycenter as bc
import center as ct
import covar as cv
import eigen_val as ev
import fitting as fit
import graphique as graph
import mat_covar as mcv
#import read_data_MDA as rdMDA
import save_file as svfile

if __name__ == "__main__":
    """
    #Vérifie que les noms de fichiers suffisants ont été passés en ligne de commande
    pdb_file = rdMDA.verify_arg(sys.argv)

    #PARTIE PROTEINE

    #Récupération des coordonnées x y z des carbones alpha à chaque pas de temps
    interest = rdMDA.read_data(pdb_file[0], pdb_file[1])
    #Calcul du barycentre
    bary_coord = bc.barycenter(interest[0], interest[1], interest[2])
    #Centrage des coordonnées
    center_coord = ct.center(interest[0], interest[1], interest[2], bary_coord)
    #Calcul de la matrice de covariance
    matrice_covar = mcv.mat_cov(center_coord[0], center_coord[1], center_coord[2])
    #Calcul des vecteurs propres
    matrice_eigval = ev.eig_val(matrice_covar)
    #Calcul de l'autocorrélation
    matrice_tau = arot.autocorr_rot(matrice_eigval)
    #Ecriture des résultats dans un fichier output
    svfile.save_dict(matrice_tau, "protein_result.txt")

    #PARTIE MOLECULE D'EAU

    #Récupération des coordonnées x, y, z du vecteur entre O et H d'une molécule
    matrice_eau = rdMDA.read_h2o(pdb_file[2], pdb_file[3])
    #Calcul de l'autocorrélation
    matrice_tau_eau = arot.autocorr_rot(matrice_eau)
    #Ecriture des résultats dans un fichier output
    svfile.save_dict(matrice_tau_eau, "h2o_result.txt")

    #On représente les résultats sur un graphique avec un script R
    """

    print(fit.calc_param("protein_result.txt",100))
    print(fit.calc_param("h2o_result.txt", 10))


