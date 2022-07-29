# gDE-Hubble Constant Calculation
# Plotting lambda vs H0 for different gamma values
# All parameters are taken from Planck 2018 (TT,TE,EE+lowE+lensing)

import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from numpy import arange

from main_functions import hubble_finder

# gamma values starting from g=-0.025 up to g=-0.06, with step size -0.001
lamda_values = arange(-12, -20.1, -0.1)

# H_0 values for lambda = 0 at different z_dagger values
h0_values_1 = [hubble_finder(-0.015, lamda) for lamda in lamda_values]

# H_0 values for lambda = 0 at different z_dagger values
h0_values_2 = [hubble_finder(-0.016, lamda) for lamda in lamda_values]

# H_0 values for lambda = 0 at different z_dagger values
h0_values_3 = [hubble_finder(-0.017, lamda) for lamda in lamda_values]

# H_0 values for lambda = 0 at different z_dagger values
h0_values_4 = [hubble_finder(-0.018, lamda) for lamda in lamda_values]

# H_0 values for lambda = 0 at different z_dagger values
h0_values_5 = [hubble_finder(-0.019, lamda) for lamda in lamda_values]

# H_0 values for lambda = 0 at different z_dagger values
h0_values_6 = [hubble_finder(-0.020, lamda) for lamda in lamda_values]


# ---------- PLOTTING ----------

# latex rendering text fonts
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


fig, ax0 = plt.subplots(figsize=(19.20, 10.80))

# ---------- AX0 ----------

ax0.plot(lamda_values, h0_values_1, linestyle=(0, (1, 10)),
        color='#661100', label='$\gamma = -0.015$')

ax0.plot(lamda_values, h0_values_2, linestyle=(0, (1, 1)),
        color='#CC6677',  label='$\gamma = -0.016$')

ax0.plot(lamda_values, h0_values_3, linestyle=(0, (5, 10)),
        color='#DDCC77',  label='$\gamma = -0.017$')

ax0.plot(lamda_values, h0_values_4, linestyle=(0, (5, 1)),
        color='#999933',  label='$\gamma = -0.018$')

ax0.plot(lamda_values, h0_values_5, linestyle=(0, (3, 1, 1, 1, 1, 1)),
        color='#44AA99',  label='$\gamma = -0.019$')

ax0.plot(lamda_values, h0_values_6, linestyle=(0, (3, 1, 1, 1)),
        color='#AA4499',   label='$\gamma = -0.020$')


# ---------- GRAPH OPTIONS ----------

# Setting Limits
ax0.set_xlim(-12, -20)
# ax0.set_ylim(65, 75)
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

plt.fill_between(lamda_values, 67.36-0.54, 67.36+0.54, color='red', alpha=0.4)
plt.fill_between(lamda_values, 69.6-0.8, 69.6+0.8, color='green', alpha=0.4)
plt.fill_between(lamda_values, 73.04-1.04, 73.04+1.04, color='blue', alpha=0.4)

plt.text(1.55, 67.36, 'PL18', verticalalignment='top')
plt.text(1.55, 69.60, 'TRGB', verticalalignment='top')
plt.text(1.55, 73.04, 'R21', verticalalignment='top')

plt.show()
ax0.set_rasterized(True)
fig.savefig('plots/lambda_vs_h0.eps',rasterized=True,dpi=600)
