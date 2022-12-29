# BAO plots

import matplotlib.gridspec as gridspec
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np

# Adjusting size of the figure
params = {'legend.fontsize': '14',
          'figure.figsize': (19.20, 10.80),
          'axes.labelsize': '20',
          'xtick.labelsize':'20',
          'ytick.labelsize':'20'}
pylab.rcParams.update(params)


from main.gde_cdm import (d_M_function_gDE, hubble_finder_gDE,
                                hubble_function_gDE)
from main.lcdm import (d_M_function_LCDM, hubble_finder_LCDM,
                                hubble_function_LCDM)

c = 299792.458  # speed of light in [km/s]

# z values that will be used for the x axis. Runs from z=0 to z=5 with step size 0.001
z_values = np.arange(0.001, 5.001, 0.001)

# Adjusting the Lambda parameter
lamda_test = -24

# Hubble Constants
h0_lcdm = hubble_finder_LCDM()
h0_13 = hubble_finder_gDE(-0.013, lamda_test)
h0_15 = hubble_finder_gDE(-0.015, lamda_test)
h0_17 = hubble_finder_gDE(-0.017, lamda_test)


# ---------- PART I H(z) / (1+z) ----------
LCDM_data_h = [hubble_function_LCDM(z, h0_lcdm) / (1 + z) for z in z_values]
z_dagger_13_h= [hubble_function_gDE(z, h0_13, -0.013, lamda_test) / (1 + z) for z in z_values]
z_dagger_15_h= [hubble_function_gDE(z, h0_15, -0.015, lamda_test) / (1 + z) for z in z_values]
z_dagger_17_h= [hubble_function_gDE(z, h0_17, -0.017, lamda_test) / (1 + z) for z in z_values]


# ---------- PART II cln(1+z) / D_M(z) ----------
LCDM_data_dm = [(c*np.log(1+z))/d_M_function_LCDM(z, h0_lcdm) for z in z_values]
z_dagger_13_dm = [(c*np.log(1+z))/d_M_function_gDE(z, h0_13, -0.013, lamda_test) for z in z_values]
z_dagger_15_dm = [(c*np.log(1+z))/d_M_function_gDE(z, h0_15, -0.015, lamda_test) for z in z_values]
z_dagger_17_dm = [(c*np.log(1+z))/d_M_function_gDE(z, h0_17, -0.017, lamda_test) for z in z_values]

# ---------- PLOTTING ----------------
# latex rendering text fonts
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Function (1+x)**(1/2)
def forward(x):
	return (1+x)**(1/2)

def inverse(x):
    return x**2-1


fig = plt.figure(constrained_layout=True)
spec = gridspec.GridSpec(ncols=1, nrows=2, figure=fig)

ax0 = fig.add_subplot(spec[0, 0])
ax1 = fig.add_subplot(spec[1, 0], sharex=ax0)

# --------- AX0 (PART I) -----------

ax0.plot(z_values, LCDM_data_h, color='black', linestyle='-', label='$\Lambda$CDM')

ax0.plot(z_values, z_dagger_13_h, linestyle=(0, (1, 10)),
        color='orange', label='$\gamma=-0.013$')

ax0.plot(z_values, z_dagger_15_h, linestyle=(0, (1, 1)),
        color='green', label='$\gamma=-0.015$')

ax0.plot(z_values, z_dagger_17_h, linestyle=(0, (5, 10)),
        color='red', label='$\gamma=-0.017$')

# Errors

# #Early Universe
# ax0.errorbar(0, 69.6, yerr=0.8, fmt='+', elinewidth=2,
#              ecolor='purple', capsize=2, capthick=1, label='TRGB')

# ax0.errorbar(0, 67.36, yerr=0.54, fmt='+', elinewidth=2,
#              ecolor='purple', capsize=2, capthick=1, label='CMB')

# ax0.errorbar(0, 73.04 , yerr=1.04, fmt='+', elinewidth=2,
#              ecolor='purple', capsize=2, capthick=1, label='SH0ES')

# BOSS Galaxy
ax0.errorbar(0.38, 59.200, yerr=1.800, fmt='o', ecolor='blue', label='BOSS Galaxy')
ax0.errorbar(0.51, 60.573, yerr=1.573, fmt='o', ecolor='blue')

# eBOSS
ax0.errorbar(0.70, 62.153, yerr=1.704, fmt='s', ecolor='yellow', label='eBOSS')
ax0.errorbar(1.48, 62.108, yerr=2.576, fmt='s', ecolor='yellow')

# Ly alpha
ax0.errorbar(2.33, 68.683, yerr=2.154, fmt='+', ecolor='magenta', label=r'Ly$\alpha$-Ly$\alpha$')
ax0.errorbar(2.33, 67.548, yerr=2.529, fmt='x', ecolor='magenta', label=r'Ly$\alpha$-Quasar')


# ---------- GRAPH OPTIONS ----------

# Setting Limits
ax0.set_xlim(0.001, 3)
ax0.set_ylim(55, 75)
# Setting Label
ax0.set_ylabel('$H(z)/1+z$'+ '\n' + '(km/s/Mpc)')
# Scaling
ax0.invert_xaxis()
ax0.set_xscale('function', functions=(forward, inverse))
ax0.set_yticks([55, 60, 65, 70, 75])
# Minor Ticks
ax0.yaxis.set_ticks_position('both')
ax0.xaxis.set_ticks_position('both')
ax0.yaxis.set_minor_locator(tck.AutoMinorLocator())
# Tick Options
ax0.tick_params(which='major', width=1, size = 7, direction='in')
ax0.tick_params(which='minor', width=0.6, size = 4, direction='in')


# --------- AX1 (PART II) -----------

ax1.plot(z_values, LCDM_data_dm, color='black', linestyle='-', label='$\Lambda$CDM')

ax1.plot(z_values, z_dagger_13_dm, linestyle=(0, (1, 10)),
        color='orange', label='$\gamma=-0.013$')

ax1.plot(z_values, z_dagger_15_dm, linestyle=(0, (1, 1)),
        color='green', label='$\gamma=-0.015$')

ax1.plot(z_values, z_dagger_17_dm, linestyle=(0, (5, 10)),
        color='red', label='$\gamma=-0.017$')

# Errors

# MGS
ax1.errorbar(0.15, 61.725, yerr=3.521, fmt='X', ecolor='purple', label='MGS')

# BOSS Galaxy
ax1.errorbar(0.38, 64.304, yerr=1.069, fmt='o', ecolor='blue', label='BOSS Galaxy')
ax1.errorbar(0.51, 63.0014, yerr=0.9903, fmt='o', ecolor='blue')

# eBOSS
ax1.errorbar(0.70, 60.681, yerr=1.121, fmt='s', ecolor='yellow', label='eBOSS')
ax1.errorbar(0.85, 63.442, yerr=3.114, fmt='s', ecolor='yellow')
ax1.errorbar(1.48, 60.445, yerr=1.576, fmt='s', ecolor='yellow')

# Ly alpha
ax1.errorbar(2.33, 65.345, yerr=3.302, fmt='+', ecolor='magenta', label=r'Ly$\alpha$-Ly$\alpha$')
ax1.errorbar(2.33, 65.871, yerr=3.002, fmt='x', ecolor='magenta', label=r'Ly$\alpha$-Quasar')


# ---------- GRAPH OPTIONS ----------
# Setting Limits
ax1.set_xlim(0.001, 3)
ax1.set_ylim(55, 75)
# Setting Label
ax1.set_ylabel('$c\ln(1+z)/d_M(z)$' + '\n' + '(km/s/Mpc)')
ax1.set_xlabel('$z$')
# Scaling and Tick Position
ax1.invert_xaxis()
ax1.set_xscale('function', functions=(forward, inverse))
ax1.set_yticks([55, 60, 65, 70, 75])
ax1.set_xticks([3, 2, 1, 0.5, 0])
# Minor Ticks
ax1.yaxis.set_ticks_position('both')
ax1.xaxis.set_ticks_position('both')
ax1.yaxis.set_minor_locator(tck.AutoMinorLocator())
# Tick Options
ax1.tick_params(which='major', width=1, size = 7, direction='in')
ax1.tick_params(which='minor', width=0.6, size = 4, direction='in')
ax1.legend(loc='lower left')

plt.setp(ax0.get_xticklabels(), visible=False)
plt.show()
fig.savefig('plots/bao_24.eps', format='eps', dpi=600)
