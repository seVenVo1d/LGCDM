# Finding cln(1+z_eff)/D_M(z_eff) from D_M/r_d
import numpy as np
from uncertainties import ufloat

from main_functions_lcdm import hubble_finder_LCDM, r_d_finder_LCDM

c = 299792.458  # speed of light in [km/s]
h0_lcdm = hubble_finder_LCDM()
r_d = r_d_finder_LCDM(h0_lcdm)

# beta = D_M/r_d
beta = ufloat(37.3, 1.7)
z_eff = 2.33
D_M = beta * r_d

D_M_plot_value = (c * np.log(1+z_eff)) / D_M
print('{:.4u}'.format(D_M_plot_value))
