import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from numpy import arange

from main_functions import Q

z_values = arange(0, 10.0001, 0.0001)

Q_values_15 = [Q(z, -0.015, -15) for z in z_values]
Q_values_17 = [Q(z, -0.017, -15) for z in z_values]
Q_values_20 = [Q(z, -0.020, -15) for z in z_values]

# ---------- PLOTTING ----------

# latex rendering text fonts
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig, ax0 = plt.subplots(figsize=(19.20, 10.80))

# ---------- AX0 ----------

ax0.plot(z_values, Q_values_15, linestyle=(0, (1, 10)), color='#661100', label='$\gamma = -0.015 (z_{\dagger} = 3.01)$')
ax0.plot(z_values, Q_values_17, linestyle=(0, (5, 10)), color='#DDCC77', label='$\gamma = -0.017 (z_{\dagger} = 2.40)$')
ax0.plot(z_values, Q_values_20, linestyle=(0, (5, 1)), color='#999933', label='$\gamma = -0.020 (z_{\dagger} = 1.83)$')
ax0.axhline(y=1, color='black', linestyle='-', label='$\Lambda$CDM')
ax0.axhline(y=-1, color='red', linestyle='-', label=r'$\rho_{\rm g} = -\rho_{\rm g,0}$')

# ---------- GRAPH OPTIONS ----------

# Setting Limits
ax0.set_xlim(0, 10)
ax0.set_ylim(-1.1, 1.1)
# Setting Labels
ax0.set_xlabel('$z$')
ax0.set_ylabel('$\mathcal{Q}(z, z_{\dagger}, \lambda)$')
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
fig.savefig('plots/q_vs_z_varying_gamma.eps', format='eps', dpi=600)