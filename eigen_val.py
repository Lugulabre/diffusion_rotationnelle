import math
import numpy as np
import numpy.linalg as alg

def scalaire(vecA, vecB):
	vec_scal = 0
	for coor in range(0,len(vecA.A)):
		vec_scal += vecA.A[0][coor] * vecB.A[0][coor]
	return vec_scal

def eig_val(matrix_cov):
	vec_ini = alg.eig(matrix_cov['t0'])[1][0]
	dico_eigval = {}
	dico_eigval["t0"] = vec_ini
	for i in range(1, len(matrix_cov)):
		temp = 't' + str(i)
		#print(scalaire(vec_ini,alg.eig(matrix_cov[temp])[1][0]))
		if scalaire(vec_ini,alg.eig(matrix_cov[temp])[1][0]) > 0:
			dico_eigval[temp] = alg.eig(matrix_cov[temp])[1][0]
		else:
			dico_eigval[temp] = -alg.eig(matrix_cov[temp])[1][0]
		vec_ini = alg.eig(matrix_cov[temp])[1][0]
	return dico_eigval

if __name__ == "__main__":

	matrix_cov = {'t0' : np.matrix([[3,3,8,22],
						[77,82,12,9],
						[12,37,0.13,34],
						[92,32,39,0.23]]),
				't1' : np.matrix([[3,3,8,22],
						[77,82,12,9],
						[12,37,0.13,34],
						[92,30,39,0.23]]),
				't2' : np.matrix([[3,3,8,22],
						[77,82,12,9],
						[12,37,0.13,34],
						[92,30,39,0.23]])}
	eig_val(matrix_cov)
	print("Ok")