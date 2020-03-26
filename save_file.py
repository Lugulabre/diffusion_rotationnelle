
def save_dict(dico, file_name):
    """
    Ecrit un dictionnaire en input dans un fichier
    """
    with open(file_name, "w") as output:
        for cle, valeur in dico.items():
            output.write(str(cle) + " " + str(valeur) + "\n")
