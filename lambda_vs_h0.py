#LSCDM - Model Calculations
# Plotting lambda vs H_0 for different gamma values

import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np

from main_functions_gde import hubble_finder_gDE
from main_functions_lcdm import hubble_finder_LCDM

# Adjusting size of the figure
params = {'legend.fontsize': '14',
          'figure.figsize': (19.20, 10.80),
          'axes.labelsize': '20',
          'xtick.labelsize':'20',
          'ytick.labelsize':'20'}
pylab.rcParams.update(params)


# lambda values starting from -4 up to -24, with step size 0.05
lamda_values = np.arange(-4, -24.05, -0.05)

# H_0 values for gamma = -0.001 for different lambda values
h0_values_1 = 100*np.array([hubble_finder_gDE(-0.001, lamda) for lamda in lamda_values])

# H_0 values for gamma = -0.004 for different lambda values
h0_values_4 = 100*np.array([hubble_finder_gDE(-0.004, lamda) for lamda in lamda_values])

# H_0 values for gamma = -0.007 for different lambda values
h0_values_7 = 100*np.array([hubble_finder_gDE(-0.007, lamda) for lamda in lamda_values])

# H_0 values for gamma = -0.010 for different lambda values
h0_values_10 = 100*np.array([hubble_finder_gDE(-0.010, lamda) for lamda in lamda_values])

# H_0 values for gamma = -0.013 for different lambda values
h0_values_13 = 100*np.array([hubble_finder_gDE(-0.013, lamda) for lamda in lamda_values])

# H_0 values for gamma = -0.017 for different lambda values
h0_values_17 = 100*np.array([hubble_finder_gDE(-0.017, lamda) for lamda in lamda_values])

h0_lcdm = hubble_finder_LCDM() * 100

# ---------- PLOTTING ----------

# latex rendering text fonts
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig, ax0 = plt.subplots()

# ---------- AX0 ----------

ax0.plot(lamda_values, h0_values_1, linestyle=(0, (1, 10)),
        color='#661100', label='$\gamma = -0.001$')

ax0.plot(lamda_values, h0_values_4, linestyle=(0, (1, 1)),
        color='#CC6677',  label='$\gamma = -0.004$')

ax0.plot(lamda_values, h0_values_7, linestyle=(0, (5, 10)),
        color='#DDCC77',  label='$\gamma = -0.007$')

ax0.plot(lamda_values, h0_values_10, linestyle=(0, (5, 1)),
        color='#999933',  label='$\gamma = -0.010$')

ax0.plot(lamda_values, h0_values_13, linestyle=(0, (3, 1, 1, 1, 1, 1)),
        color='#44AA99',  label='$\gamma = -0.013$')

ax0.plot(lamda_values, h0_values_17, linestyle=(0, (3, 1, 1, 1)),
        color='#AA4499',   label='$\gamma = -0.017$')

ax0.axhline(h0_lcdm, linestyle='-', color='black', label='$\Lambda$CDM')

# ---------- GRAPH OPTIONS ----------

# Setting Limits
ax0.set_xlim(-4, -24)
# Setting Labels
ax0.set_ylabel('$H_0$')
ax0.set_xlabel('$\lambda$')
# Minor Ticks
ax0.yaxis.set_ticks_position('both')
ax0.xaxis.set_ticks_position('both')
ax0.yaxis.set_minor_locator(tck.AutoMinorLocator())
# Tick Options
ax0.tick_params(which='major', width=1, size=7, direction='in')
ax0.tick_params(which='minor', width=0.6, size=4, direction='in')
# Other Options
ax0.legend()
plt.show()

ax0.set_rasterized(True)
fig.savefig('plots/lambda_vs_h0.eps',rasterized=True,dpi=600)
