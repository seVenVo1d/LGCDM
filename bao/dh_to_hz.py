# Finding D_H(z) H(z_eff)/1+z_eff from D_H/r_d

from uncertainties import ufloat

c = 299792.458  # speed of light in [km/s]
r_d = 147.09

# beta = D_H/r_d
beta = ufloat(8.93, 0.28)
z_eff = 2.33
D_H = beta * r_d

D_H_plot_value = (c / D_H) / (1+z_eff)
print('{:.4u}'.format(D_H_plot_value))
