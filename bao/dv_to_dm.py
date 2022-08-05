# Finding cln(1+z_eff)/D_M(z_eff) from D_V(z_eff)

import numpy as np
from uncertainties import ufloat, umath

from main_functions_lcdm import hubble_finder_LCDM, hubble_function_LCDM, r_d_finder_LCDM

#important parameters
c = 299792.458  # speed of light in [km/s]

z_eff = 0.85

h0_lcdm = hubble_finder_LCDM()
h_zeff = hubble_function_LCDM(z_eff, h0_lcdm)
r_d = r_d_finder_LCDM(h0_lcdm)

# beta = D_V/r_d

beta = ufloat(18.33, 0.6)
D_V = beta * r_d
D_M = umath.sqrt((D_V**3 * h_zeff) / (c * z_eff))

D_M_plot_value = (c * np.log(1+z_eff)) / D_M
print('{:.4u}'.format(D_M_plot_value))
