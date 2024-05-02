from uncertainties import ufloat
from numpy import pi, mean
from collections import namedtuple

# Erreurs
delta_dist = 0.01  # mm

dimensions = namedtuple('dim', ['longueur', 'largeur', 'epaisseur'])
froid1 = dimensions(ufloat(18.13, delta_dist), ufloat(4.21, delta_dist), ufloat(2.30, delta_dist))
froid2 = dimensions(ufloat(20.46, delta_dist), ufloat(4.19, delta_dist), ufloat(2.07, delta_dist))

chaud3 = dimensions(ufloat(17.42, delta_dist), ufloat(4.05, delta_dist), ufloat(2.01, delta_dist))
chaud4 = dimensions(ufloat(17.41, delta_dist), ufloat(4.09, delta_dist), ufloat(2.00, delta_dist))

tiede5 = dimensions(ufloat(18.04, delta_dist), ufloat(4.06, delta_dist), ufloat(2.03, delta_dist))
tiede6 = dimensions(ufloat(00, delta_dist), ufloat(00, delta_dist), ufloat(00, delta_dist))