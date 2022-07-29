# gDE-Hubble Constant Calculation
# Plotting H_0 vs z_dagger for different lambda values
# All parameters are taken from Planck 2018 (TT,TE,EE+lowE+lensing)

import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from numpy import arange

from main_functions import hubble_finder

# gamma values starting from g=-0.025 up to g=-0.06, with step size -0.001
gamma_values = arange(-0.015, -0.0205, -0.0005)


# H_0 values for lambda = 0 at different z_dagger values
gamma_values_12 = [hubble_finder(gamma, -12) for gamma in gamma_values]

# H_0 values for lambda = 0 at different z_dagger values
gamma_values_14 = [hubble_finder(gamma, -14) for gamma in gamma_values]

# H_0 values for lambda = 0 at different z_dagger values
gamma_values_16 = [hubble_finder(gamma, -16) for gamma in gamma_values]

# H_0 values for lambda = 0 at different z_dagger values
gamma_values_18 = [hubble_finder(gamma, -18) for gamma in gamma_values]

# H_0 values for lambda = 0 at different z_dagger values
gamma_values_20 = [hubble_finder(gamma, -20) for gamma in gamma_values]


# ---------- PLOTTING ----------

# latex rendering text fonts
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


fig, ax0 = plt.subplots(figsize=(19.20, 10.80))

# ---------- AX0 ----------

ax0.plot(gamma_values, gamma_values_12, linestyle=(0, (1, 10)),
        color='#661100', label='$\lambda = -12$')

ax0.plot(gamma_values, gamma_values_14, linestyle=(0, (1, 1)),
        color='#CC6677', label='$\lambda = -14$')

ax0.plot(gamma_values, gamma_values_16, linestyle=(0, (5, 10)),
        color='#DDCC77', label='$\lambda = -16$')

ax0.plot(gamma_values, gamma_values_18, linestyle=(0, (5, 1)),
        color='#999933', label='$\lambda = -16$')

ax0.plot(gamma_values, gamma_values_20, linestyle=(0, (3, 1, 1, 1, 1, 1)),
        color='#44AA99', label='$\lambda = -20$')


# ---------- GRAPH OPTIONS ----------

# Setting Limits
ax0.set_xlim(-0.015, -0.020)
# ax0.set_ylim(65, 75)
# Setting Labels
ax0.set_ylabel('$H_0$')
ax0.set_xlabel('$\gamma$')
# Minor Ticks
ax0.yaxis.set_ticks_position('both')
ax0.xaxis.set_ticks_position('both')
ax0.yaxis.set_minor_locator(tck.AutoMinorLocator())
# Tick Options
ax0.tick_params(which='major', width=1, size=7, direction='in')
ax0.tick_params(which='minor', width=0.6, size=4, direction='in')
# Other Options
ax0.legend()

plt.fill_between(gamma_values, 67.36-0.54, 67.36+0.54, color='red', alpha=0.4)
plt.fill_between(gamma_values, 69.6-0.8, 69.6+0.8, color='green', alpha=0.4)
plt.fill_between(gamma_values, 73.04-1.04, 73.04+1.04, color='blue', alpha=0.4)


plt.text(1.55, 67.36, 'PL18', verticalalignment='top')
plt.text(1.55, 69.60, 'TRGB', verticalalignment='top')
plt.text(1.55, 73.04, 'R21', verticalalignment='top')

plt.show()
ax0.set_rasterized(True)
fig.savefig('plots/gamma_vs_h0.eps',rasterized=True,dpi=600)
