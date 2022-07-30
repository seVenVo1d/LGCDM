# Finding cln(1+z_eff)/D_M(z_eff) from D_M/r_d

from numpy import log as ln
from uncertainties import ufloat

c = 299792.458  # speed of light in [km/s]
r_d = 147.09

# beta = D_M/r_d
beta = ufloat(37.6, 1.9)
z_eff = 2.33
D_M = beta * r_d

D_M_plot_value = (c * ln(1+z_eff)) / D_M
print('{:.4u}'.format(D_M_plot_value))
