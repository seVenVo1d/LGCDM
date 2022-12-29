# Finding D_H(z) H(z_eff)/1+z_eff from D_H/r_d

from uncertainties import ufloat
from main.lcdm import r_d_finder_LCDM, hubble_finder_LCDM

c = 299792.458  # speed of light in [km/s]
h0_lcdm = hubble_finder_LCDM()
r_d = r_d_finder_LCDM(h0_lcdm)

# beta = D_H/r_d
beta = ufloat(9.08, 0.34)
z_eff = 2.33
D_H = beta * r_d

D_H_plot_value = (c / D_H) / (1+z_eff)
print('{:.4u}'.format(D_H_plot_value))
