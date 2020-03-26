import MDAnalysis
from MDAnalysis.tests.datafiles import PDB,XTC
import numpy as np
import os
import sys

def verify_arg(sys_args):
    """
    La fonction vérifie que le bon nombre de fichiers a été pris en argument.
    Elle vérifie ensuite que les fichiers existent et peuvent être ouverts.
    """
    if len(sys_args) != 5:
        exit("ERROR: NEEDS 4 FILE AS ARGUMENT")
    if ((os.path.exists(sys_args[1]) == False) | (os.path.exists(sys_args[2]) == False) | 
        (os.path.exists(sys_args[3]) == False) | (os.path.exists(sys_args[4]) == False)):
        exit("ERROR: FILE DOES NOT EXIST")
    return sys_args[1:5]

def read_data(file_name_pdb, file_name_xtc):
    #Ouverture des données via MDAnalysis
    u_prot = MDAnalysis.Universe(file_name_pdb, file_name_xtc)
    #Récupération des données concernant les carbones alpha
    calphas = u_prot.select_atoms("name CA")

    #Compteur pour indiquer le pas de temps dans le dictionnaire
    range_time = 0
    #Compteur pour indiquer le numéro de coordonnée enregistrée dans le dictionnaire
    range_coor = 1

    #Définition des dictionnaires contenant les coordonnées x, y ou z de tous les carbones alpha à chaque pas de temps
    dictX = {}
    dictY = {}
    dictZ = {}

    for ts in u_prot.trajectory:
        #Dictionnaires temporaires pour enregistrer les coordonnées x, y ou z des carbones alpha à un pas de temps t
        listX = {}
        listY = {}
        listZ = {}
        for i in calphas.indices:
            listX[range_coor] = ts[i][0]
            listY[range_coor] = ts[i][1]
            listZ[range_coor] = ts[i][2]
            range_coor+=1
        dictX["t" + str(range_time)] = listX
        dictY["t" + str(range_time)] = listY
        dictZ["t" + str(range_time)] = listZ
        range_time += 1
        range_coor = 0

    return (dictX, dictY, dictZ)

def read_h2o(file_name_pdb, file_name_xtc):
    u_prot = MDAnalysis.Universe(file_name_pdb, file_name_xtc)
    #Récupération des atomes d'oxygène
    oxygene = u_prot.select_atoms("name OW")
    #Récupération de l'indice du premier atome d'oxygène
    oxygene = oxygene.indices[0]

    range_time = 0

    dict_eau = {}

    """
    On récupère les coordonnées du vecteur entre l'atome d'oxygène 
    et le premier atome d'hydrogène qui lui est lié.
    """
    for ts in u_prot.trajectory:
        x_eau = ts[oxygene+1][0] - ts[oxygene][0]
        y_eau = ts[oxygene+1][1] - ts[oxygene][1]
        z_eau = ts[oxygene+1][2] - ts[oxygene][2]
        dict_eau["t" + str(range_time)] = np.matrix([x_eau, y_eau, z_eau])
        range_time += 1

    return dict_eau
