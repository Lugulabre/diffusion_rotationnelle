import MDAnalysis
from MDAnalysis.tests.datafiles import PDB,XTC
import os
import sys

def verify_arg(sys_args):
    if len(sys_args) != 3:
        exit("ERROR: NEEDS 2 FILE AS ARGUMENT")
    if (os.path.exists(sys_args[1]) == False) | (os.path.exists(sys_args[2]) == False):
        exit("ERROR: FILE DOES NOT EXIST")
    return sys_args[1:3]

def read_data(file_name_pdb, file_name_xtc):
	u_prot = MDAnalysis.Universe(file_name_pdb, file_name_xtc)
	calphas = u_prot.select_atoms("name CA")

	range_time = 0
	range_coor = 1

	dictX = {}
	dictY = {}
	dictZ = {}

	for ts in u_prot.trajectory:
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


