# gDE-Hubble Constant Calculation
# Plotting w_g,0 as a function of z_dagger and lambda - Contour Plot
# All parameters are taken from Planck 2018 (TT,TE,EE+lowE+lensing)

import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from matplotlib import cm
from numpy import arange, meshgrid, reshape, transpose

from main_functions import w_g

# gamma values starting from g=-0.025 up to g=-0.06, with step size -0.001
gamma_values = arange(-0.015, -0.0205, -0.0005)

# lambda values starting from lambda = -8 to lambda = -32 with step size -0.25
lamda_values = arange(-12, -20.1, -0.1)

X, Y = meshgrid(gamma_values, lamda_values)

variable_grid_data = list((x, y) for x in gamma_values for y in lamda_values)
data_points = [w_g(0, x, y) for (x, y) in variable_grid_data]
new_points = reshape(data_points, (len(gamma_values), len(lamda_values)))
Z = transpose(new_points)

# ---------- PLOTTING ----------

# latex rendering text fonts
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


fig, ax0 = plt.subplots(figsize=(19.20, 10.80))  # adjusting the size of the figure
plt.contourf(X, Y, Z, cmap=cm.plasma, antialiased=True)

# ---------- GRAPH OPTIONS ----------

# Setting Limits
ax0.set_xlim(-0.015, -0.020)
# Setting Labels
ax0.set_xlabel('$\gamma$')
ax0.set_ylabel('$\lambda$')
# Tick Options
ax0.tick_params(which='major', width=1, size=7, direction='in')
# Other Options
plt.colorbar()
plt.imshow(Z, vmin=0., vmax=3., cmap=cm.plasma, origin='lower', extent=[X.min(), X.max(), Y.min(), Y.max()], aspect=8)
plt.axis('tight')
plt.show()
fig.savefig('plots/eos_parameter.eps', format='eps', dpi=600)
