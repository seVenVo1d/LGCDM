# LSCDM - Model Calculations
# Plotting Q vs z by varying lambda and gamma

import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np

from main_functions_gde import Q

# Adjusting size of the figure
params = {'legend.fontsize': '14',
          'figure.figsize': (19.20, 10.80),
          'axes.labelsize': '20',
          'xtick.labelsize':'20',
          'ytick.labelsize':'20'}
pylab.rcParams.update(params)


# Z values ranging from 0 to 10
z_values = np.arange(0, 10.0001, 0.0001)


Q_values_12 = [Q(z, -0.011, -14) for z in z_values]
Q_values_16 = [Q(z, -0.012, -16) for z in z_values]
Q_values_20 = [Q(z, -0.013, -18) for z in z_values]
Q_values_24 = [Q(z, -0.014, -20) for z in z_values]


# ---------- PLOTTING ----------

# latex rendering text fonts
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig, ax0 = plt.subplots(figsize=(19.20, 10.80))

# ---------- AX0 ----------

ax0.plot(z_values, Q_values_12, linestyle=(0, (1, 1)), color='#661100', label='$(\gamma, \lambda) = (-0.011, -14)$')
ax0.plot(z_values, Q_values_16, linestyle=(0, (5, 10)), color='#DDCC77', label='$(\gamma, \lambda) = (-0.012, -16)$')
ax0.plot(z_values, Q_values_20, linestyle=(0, (5, 1)), color='#999933', label='$(\gamma, \lambda) = (-0.013, -18)$')
ax0.plot(z_values, Q_values_24, linestyle=(0, (3, 1, 1, 1, 1, 1)), color='#CC6677', label='$(\gamma, \lambda) = (-0.014, -20)$')
ax0.axhline(y=1, color='black', linestyle='-', label='$\Lambda$CDM')
ax0.axhline(y=-1, color='red', linestyle='-', label=r'$\rho_{\rm g} = -\rho_{\rm g,0}$')

# ---------- GRAPH OPTIONS ----------

# Setting Limits
ax0.set_xlim(0, 10)
ax0.set_ylim(-1.1, 1.1)
# Setting Labels
ax0.set_xlabel('$z$')
ax0.set_ylabel(r'$\rho_{\rm g} / \rho_{\rm g,0}$')
# Minor Ticks
ax0.yaxis.set_ticks_position('both')
ax0.xaxis.set_ticks_position('both')
ax0.yaxis.set_minor_locator(tck.AutoMinorLocator())
# Tick Options
ax0.tick_params(which='major', width=1, size=7, direction='in')
ax0.tick_params(which='minor', width=0.6, size=4, direction='in')
# Other Options
ax0.invert_xaxis()
ax0.legend()

plt.show()
fig.savefig('plots/q_vs_z_varying_lambda.eps', format='eps', dpi=600)
