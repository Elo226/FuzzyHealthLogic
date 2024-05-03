from devoir import *

avant_repas = 120  # Valeur de la glycémie avant le repas (en mg/dL)
apres_repas = 180  # Valeur de la glycémie après le repas (en mg/dL)
choix = 'choix_glycemie'  # Choix du critère de sortie (ex. 'choix_glycemie')

# Appel de la fonction etatGlycemie avec les paramètres spécifiés
resultat = etatPression(avant_repas, apres_repas, choix)

# Affichage du résultat
print("État de la glycémie :", resultat)