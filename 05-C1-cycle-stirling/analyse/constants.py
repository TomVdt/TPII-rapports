from uncertainties import ufloat
from numpy import pi

# Taille du cylindre du moteur
r_cylindre = ufloat(4, 0.5) # cm
h_max = ufloat(7.4, 0.5) # cm
h_min = ufloat(2.04, 0.25) # cm
V_max = pi * (r_cylindre ** 2) * h_max # cm³
V_min = pi * (r_cylindre ** 2) * h_min # cm³

# Caractéristiques du cycle
# TODO: check values
P_max = ufloat(0.54, 0.1) # bar
P_min = ufloat(0.1, 0.1) # bar

# Rayon du disque de freinage
r_disque = ufloat(4, 0.001) # cm

# Puissance fil
U_fil = ufloat(13.41, 0.05) # V
I_fil = ufloat(12.82, 0.05) # A

# Temperatures
T_eau_in = ufloat(20, 0.1) + 273 # K
delta_T_eau = ufloat(3.9, 0.1) # K
T_eau_out = T_eau_in + delta_T_eau # K

T_fil = ufloat(1143, 70) # K

# Débit
debit_eau = ufloat(280, 5) # mL / min
# https://fr.wikipedia.org/wiki/Capacit%C3%A9_thermique_massique
C_m_eau = ufloat(4_185, 0.1) # J / K / kg
rho_eau = ufloat(1_000, 0.1) # kg / m^3
