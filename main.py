import sys

import autocorr_rot as arot
import barycenter as bc
import center as ct
import covar as cv
import eigen_val as ev
import graphique as graph
import mat_covar as mcv
import read_data_MDA as rdMDA

pdb_file = rdMDA.verify_arg(sys.argv)
#print(pdb_file[1])
interest = rdMDA.read_data(pdb_file[0], pdb_file[1])
#print(interest[0])
bary_coord = bc.barycenter(interest[0], interest[1], interest[2])
#print(bary_coord)
center_coord = ct.center(interest[0], interest[1], interest[2], bary_coord)
#print(center_coord)
matrice_covar = mcv.mat_cov(center_coord[0], center_coord[1], center_coord[2])
#print(matrice_covar)
matrice_eigval = ev.eig_val(matrice_covar)
#print(matrice_eigval)
matrice_tau = arot.autocorr_rot(matrice_eigval)
#print(matrice_tau)
graph.graphique(matrice_tau, "courbe_autocorr.png", "blue")

matrice_eau = rdMDA.read_h2o(pdb_file[0], pdb_file[1])
#print(matrice_eau)
matrice_tau_eau = arot.autocorr_rot(matrice_eau)
#print(matrice_tau_eau)
graph.graphique(matrice_tau_eau, "courbe_eau.png", "red")



