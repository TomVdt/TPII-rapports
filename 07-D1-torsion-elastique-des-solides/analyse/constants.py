from uncertainties import ufloat
from numpy import pi, mean

# Erreurs
g = 9.81

# Statique
delta_regle_laser = 0.05  # cm
delta_regle_tige = 0.01  # cm
delta_masse = 1  # g

distance_regle = ufloat(67, 0.1)  # cm

taille_disque_magnesium = ufloat(9.94, 0.001)  # cm
epaisseur_tige_magnesium = mean([ufloat(i/10, 0.001) for i in (10.11, 10.02, 10.04, 10.08, 10.05, 10.02, 10.01, 10.02, 10.06)])  # cm

taille_disque_laiton = ufloat(9.951, 0.001)  # cm
epaisseur_tige_laiton = mean([ufloat(i/10, 0.001) for i in (5, 4.99, 5.11, 5, 5, 4.99, 4.99, 5.01, 5, 5)])  # cm

taille_disque_acier = ufloat(9.964, 0.001)  # cm
epaisseur_tige_acier = mean([ufloat(i/10, 0.001) for i in (5.12, 5.11, 5.19, 5.01, 5.11, 5.07, 5.01, 4.99, 5, 4.99)])  # cm

# Dynamique
masse_disque = ufloat(2991, 0.1)  # g
diametre_disque = ufloat(14.935, 0.0001)  # cm

epaisseur_fil_acier = mean([ufloat(i/10, 0.001) for i in (1.11, 1.04, 1.04, 1.06)])  # cm
longueur_fil_acier = ufloat(7.996, 0.001)  # cm

epaisseur_fil_laiton = mean([ufloat(i/10, 0.001) for i in (1.14, 1.12, 1.13, 1.12)])  # cm
longueur_fil_laiton = ufloat(8.036, 0.001)  # cm

epaisseur_fil_magnesium = mean([ufloat(i/10, 0.001) for i in (2.08, 2.02, 2.03, 2.01)])  # cm
longueur_fil_magnesium = ufloat(8, 0.001)  # cm
