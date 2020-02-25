# diffusion_rotationnelle
Projet de dynamique moléculaire

## Détermination de l'axe de la protéine

Stockage des coordonnées :
- dictionnaire pour chaque axe (x, y, z)
Norme : dicX = {t0 : {x1 : 0.23
                      x2 : 0.74
                      x3 : 0.1
                      ...},
                t1 : {x1 : 0.57
                      x2 : 0.91
                      x3 : 0.02
                      ...},
                ...}
                      
Lire les fichiers pdb et xtc et récupérer les coordonnées x, y et z des carbones alpha uniquement.
Centrer les données -> calcul de la moyenne selon chaque axe et recentrage des données selon la valeur.
A partir de ces nouvelles coordonnées, calculer la matrice de variance / covariance.
L'axe de la protéine sera le premier vecteur propre -> diagonaliser la matrice (package numpy) pour avoir les vecteurs propres.
Vérifier que l'axe est toujours orienté dans la même "direction" -> prendre 2 atomes après le premier calcul et faire le produit scalaire du vecteur entre ces 2 atomes avec l'axe principal (produit négatif si l'axe principal a été inversé).
Reproduire pour chaque temps et stocker les axes principaux dans un dico.
Norme : dicAxe = {t0 : {x : 0.23
                        y : 0.74
                        z : 0.1},
                  t1 : {x : 0.57
                        y : 0.91
                        z : 0.02},
                  ...}

## Autocorrélation rotationnelle

Pour chaque temps thô, calculer la moyenne du produit scalaire de l'axe au temps t avec l'axe au temps t+thô (ce qui revient à calculer le cosinus de l'angle alpha entre les deux axes).# diffusion_rotationnelle
Projet de dynamique moléculaire
