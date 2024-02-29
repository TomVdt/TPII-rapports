from uncertainties import ufloat
from numpy import pi, mean

# Erreurs

# Statique
delta_regle = 0.5  # mm
delta_masse = 1  # g

distance_regle = ufloat(670, 1)  # mm

taille_disque_magnesium = ufloat(99.4, 0.01)  # mm
epaisseur_tige_magnesium = mean([ufloat(i, 0.01) for i in (10.11, 10.02, 10.04, 10.08, 10.05, 10.02, 10.01, 10.02, 10.06)])  # mm

taille_disque_laiton = ufloat(99.51, 0.01)  # mm
epaisseur_tige_laiton = mean([ufloat(i, 0.01) for i in (5, 4.99, 5.11, 5, 5, 4.99, 4.99, 5.01, 5, 5)])  # mm

taille_disque_acier = ufloat(99.64, 0.01)  # mm
epaisseur_tige_acier = mean([ufloat(i, 0.01) for i in (5.12, 5.11, 5.19, 5.01, 5.11, 5.07, 5.01, 4.99, 5, 4.99)])  # mm

# Dynamique
masse_disque = ufloat(2991, 0.1)  # g
diametre_disque = ufloat(149.35, 0.001)  # mm

epaisseur_fil_acier = mean([ufloat(i, 0.01) for i in (1.11, 1.04, 1.04, 1.06)])  # mm
longueur_fil_acier = ufloat(79.96, 0.01)  # mm

epaisseur_fil_laiton = mean([ufloat(i, 0.01) for i in (1.14, 1.12, 1.13, 1.12)])  # mm
longueur_fil_laiton = ufloat(80.36, 0.01)  # mm

epaisseur_fil_magnesium = mean([ufloat(i, 0.01) for i in (2.08, 2.02, 2.03, 2.01)])  # mm
longueur_fil_magnesium = ufloat(80, 0.01)  # mm
