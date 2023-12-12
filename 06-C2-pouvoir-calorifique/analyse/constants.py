from uncertainties import ufloat
from numpy import pi

# Erreurs

delta_M = 5e-3  # kg
delta_m = 0.02e-3  # kg
delta_Mc = 0.1e-3  # kg
delta_T = 0.1  # K

# Thermo shit

l_vap_eau = ufloat(2_257_000, 100)  # J / kg
C_m_eau = ufloat(4179.6, 0.1) # J / K / kg

# Constantes pour les valeurs théoriques
# Chaleurs latentes tout ca tout ca

H_CO2 = ...
H_BiTe = ...


# Masses molaires
m_mol_ethanol = ufloat(46.07, 0.01) # g / mol   https://pubchem.ncbi.nlm.nih.gov/compound/ethanol
m_mol_propane = ufloat(44.10, 0.01) # g / mol   https://pubchem.ncbi.nlm.nih.gov/compound/6334
m_mol_butane = ufloat(58.12, 0.01) # g / mol   https://pubchem.ncbi.nlm.nih.gov/compound/7843
m_mol_co2 = ufloat(44.009, 0.01) # g / mol   https://pubchem.ncbi.nlm.nih.gov/compound/280