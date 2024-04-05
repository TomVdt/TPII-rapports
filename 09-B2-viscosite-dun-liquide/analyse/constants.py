from uncertainties import ufloat
from numpy import pi, mean

# Erreurs
delta_T = 0.5
delta_t = 0.2

# Notice me senpai
g = 9.81  # m/s²
k_boltzmann = 1.38 * 1e-23  # J/K

bille_rayon = ufloat(1, 0.005) * 0.001  # m
bille_masse = ufloat(0.00443, 3e-5) * 1e-3  # kg
distance_top_bottom = ufloat(0.1, 0)  # m
densite_1 = 819  # kg/m³
densite_2 = 837  # kg/m³

# Trucs
