# LSCDM - Model Calculations
# Calculating the Omega_m,0 for a given gamma and lambda

import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import arange, meshgrid, reshape, transpose

from main_functions import Omega_m0

# gamma values starting from gamma = -0.001 to gamma = -0.018 with step size 0.001
gamma_values = arange(-0.001, -0.018, -0.001)

# lambda values starting from lambda = -4 to lambda = -24 with step size 0.5
lamda_values = arange(-4, -24.5, -0.5)


X, Y = meshgrid(gamma_values, lamda_values)

variable_grid_data = list((x, y) for x in gamma_values for y in lamda_values)
data_points = [Omega_m0(x, y) for (x, y) in variable_grid_data]
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
ax0.set_xlim(-0.001, -0.018)
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

fig.savefig('plots/omega_m0_parameter.eps', format='eps', dpi=600)
