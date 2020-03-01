import matplotlib.pyplot as plt
import numpy as np

def graphique(corr_dict):
	#print(corr_dict.keys()[0])
	#print(np.array(corr_dict.values()))
	list_keys = []
	list_values = []
	for cle, valeur in corr_dict.items():
		list_keys.append(cle)
		list_values.append(valeur)
	#print(list_keys, list_values)
	plt.plot(list_keys, list_values)
	plt.savefig("courbe_autocorr.png")
	#plt.show()