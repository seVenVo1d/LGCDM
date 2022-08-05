# LSCDM - Model Calculations
# Plotting z_dagger as a function of gamma and lambda - Contour Plot

import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from matplotlib import cm
import numpy as np

from main_functions_gde import z_dagger_finder

# Adjusting size of the figure
params = {'legend.fontsize': '14',
          'figure.figsize': (19.20, 10.80),
          'axes.labelsize': '20',
          'xtick.labelsize':'20',
          'ytick.labelsize':'20'}
pylab.rcParams.update(params)


# gamma values starting from gamma = -0.01 up to gamma =-0.018, with step size -0.0005
gamma_values = np.arange(-0.01, -0.01805, -0.0005)

# lambda values starting from lambda = -13 to lambda = -24 with step size -0.01
lamda_values = np.arange(-13, -24.01, -0.01)

X, Y = np.meshgrid(gamma_values, lamda_values)

variable_grid_data = list((x, y) for x in gamma_values for y in lamda_values)
data_points = [z_dagger_finder(x, y) for (x, y) in variable_grid_data]
new_points = np.reshape(data_points, (len(gamma_values), len(lamda_values)))
Z = np.transpose(new_points)

# ---------- PLOTTING ----------

# latex rendering text fonts
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


fig, ax0 = plt.subplots(figsize=(19.20, 10.80))  # adjusting the size of the figure
plt.contourf(X, Y, Z, cmap=cm.plasma, antialiased=True)

# ---------- GRAPH OPTIONS ----------

# Setting Limits
ax0.set_xlim(-0.01, -0.018)
# Setting Labels
ax0.set_xlabel('$\gamma$')
ax0.set_ylabel('$\lambda$')
# Minor Ticks
ax0.get_yaxis().set_major_formatter(tck.ScalarFormatter())
# Tick Options
ax0.tick_params(which='major', width=1, size=7, direction='in')
# Other Options
cbar = plt.colorbar()
cbar.set_label('$z_{\dagger}$')
plt.imshow(Z, vmin=0., vmax=3., cmap=cm.plasma, origin='lower', extent=[X.min(), X.max(), Y.min(), Y.max()], aspect=8)
plt.axis('tight')
plt.show()

ax0.set_rasterized(True)
fig.savefig('plots/z_dagger_contour.eps',rasterized=True,dpi=600)



