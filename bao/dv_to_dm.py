# Finding cln(1+z_eff)/D_M(z_eff) from D_V(z_eff)

from negative_lambda.main_functions import hubble_finder_LCDM, hubble_function_LCDM
from numpy import log as ln
from uncertainties import ufloat, umath

#important parameters
c = 299792.458  # speed of light in [km/s]
z_eff = 0.85
h0_lcdm = hubble_finder_LCDM() / 100
r_d = 147.09

h_zeff = hubble_function_LCDM(z_eff, h0_lcdm)

# beta = D_V/r_d

beta = ufloat(18.33, 0.60)
D_V = beta * r_d
D_M = umath.sqrt((D_V**3 * h_zeff) / (c * z_eff))

D_M_plot_value = (c * ln(1+z_eff)) / D_M
print('{:.4u}'.format(D_M_plot_value))
