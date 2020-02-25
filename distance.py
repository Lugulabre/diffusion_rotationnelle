""" script that will take a pdb file containing multiple models of a same 
    molecule and then determine the distance between specific residues"""

__author__ = ["Apollinaire Roubert", "Maxime Kermarrec"]
__date__ = "2019-12-18"

import sys
import os

def verify_arg(sys_args):
    if len(sys_args) != 2:
        exit("ERROR: NEEDS 1 FILE AS ARGUMENT")
    if os.path.exists(sys_args[1]) == False:
        exit("ERROR: FILE DOES NOT EXIST")
    return sys_args[1]
        
def get_residues(file_name):
    """
    function that gets the lines containing the residues of interest in
    each model from the pdb file

    returns a list of lines
    """
    line_list = []
    with open(file_name, "r") as f_in:
        for l in f_in:
            if (l[0:6].strip()) == "ATOM":
                if l[17:20].strip() == "GLU" and l[22:26].strip() == "160" and (l[12:16].strip() == "OE1" or l[12:16].strip() == "OE2"):
                    line_list.append(l)
                elif l[17:20].strip() == "GLU" and l[22:26].strip() == "168" and (l[12:16].strip() == "OE1" or l[12:16].strip() == "OE2"):
                    line_list.append(l)
                elif l[17:20].strip() == "GLN" and l[22:26].strip() == "247" and (l[12:16].strip() == "OE1" or l[12:16].strip() == "NE2"):
                    line_list.append(l)
                elif l[17:20].strip() == "LYS" and l[22:26].strip() == "272" and l[12:16].strip() == "NZ":
                    line_list.append(l)
                elif l[17:20].strip() == "PHE" and l[22:26].strip() == "318" and (l[12:16].strip() == "CG" or l[12:16].strip() == "CD1" or l[12:16].strip() == "CD2" or l[12:16].strip() == "CE1" or l[12:16].strip() == "CE2" or l[12:16].strip() == "CZ"):
                    line_list.append(l)
                elif l[17:20].strip() == "ARG" and l[22:26].strip() == "321" and (l[12:16].strip() == "NH1" or l[12:16].strip() == "NH2" or l[12:16].strip() == "NE"):
                    line_list.append(l)
                elif l[17:20].strip() == "TYR" and l[22:26].strip() == "322"  and l[12:16].strip() == "OH":
                    line_list.append(l)
    return line_list

def write_dataset(atom_list, file_name):
    """
    """
    model = 1
    res_name = ""
    with open(file_name, "w") as filout:
        filout.write('"Model";"Residue";"Res_num";"X";"Y";"Z";"Prot"\n')
        for atom in atom_list:
            if res_name == "TYR" and atom[17:20].strip() != "TYR":
                model += 1
            res_name = atom[17:20].strip()
            res_num = atom[22:26].strip()
            x = atom[30:38].strip()
            y = atom[38:46].strip()
            z = atom[46:54].strip()
            if (res_name == "GLU") or (res_name == "GLN") or (res_name == "LYS"):
                prot = "GPR54"
            elif (res_name == "PHE") or (res_name == "ARG") or (res_name == "TYR"):
                prot = "KP10"
            filout.write("{};".format(model))
            filout.write("{};".format(res_name))
            filout.write("{};".format(res_num))
            filout.write("{};".format(x))
            filout.write("{};".format(y))
            filout.write("{};".format(z))
            filout.write("{}\n".format(prot))


if __name__ == "__main__":
    pdb_file = verify_arg(sys.argv)
    interest = get_residues(pdb_file)
    print(len(interest))
    write_dataset(interest, "dataset.csv")
