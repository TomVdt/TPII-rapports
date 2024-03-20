from uncertainties import ufloat
from numpy import pi, mean

# Erreurs
delta_largeur_epaisseur = 0.02  # mm
delta_longueur = 0.03  # mm
delta_masse = 0.0005  # g

# Notice me senpai
Delta_lambda = 0.62  # sans unités
k_boltzmann = 1.38 * 1e-23  # J/K
v_0 = 3.05 * 1e-30  # m³

# Trucs
titane_epaisseur = ufloat(2.10, delta_largeur_epaisseur)  # mm
titane_largeur = ufloat(5.03, delta_largeur_epaisseur)  # mm
titane_longueur = ufloat(59.38, delta_longueur)  # mm
titane_masse = ufloat(2.6556, delta_masse)
titane_densite = titane_masse / (titane_longueur * titane_largeur * titane_epaisseur * 0.001)  # g / cm³

laiton_epaisseur = ufloat(2.01, delta_largeur_epaisseur)  # mm
laiton_largeur = ufloat(5.95, delta_largeur_epaisseur)  # mm
laiton_longueur = ufloat(60.00, delta_longueur)  # mm
laiton_masse = ufloat(5.9803, delta_masse)
laiton_densite = laiton_masse / (laiton_longueur * laiton_largeur * laiton_epaisseur * 0.001)  # g / cm³

acier_doux_epaisseur = ufloat(1.53, delta_largeur_epaisseur)  # mm
acier_doux_largeur = ufloat(4.09, delta_largeur_epaisseur)  # mm
acier_doux_longueur = ufloat(58.84, delta_longueur)  # mm
acier_doux_masse = ufloat(2.7658, delta_masse)
acier_doux_densite = acier_doux_masse / (acier_doux_longueur * acier_doux_largeur * acier_doux_epaisseur * 0.001)  # g / cm³
