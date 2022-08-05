# LSCDM - Model Calculations
# Plotting the Hubble Data Obtained from Table 2 in 
# https://arxiv.org/pdf/1802.01505.pdf

import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np

from main_functions_gde import E_function_gDE, hubble_finder_gDE
from main_functions_lcdm import E_function_LCDM, hubble_finder_LCDM

# Adjusting size of the figure
params = {'legend.fontsize': '14',
          'figure.figsize': (19.20, 10.80),
          'axes.labelsize': '20',
          'xtick.labelsize':'20',
          'ytick.labelsize':'20'}
pylab.rcParams.update(params)

# z values that will be used for the x axis. Runs from z=0 to z=1 with step size 0.001
z_values = np.arange(0, 1, 0.001)

# Adjusting the z_dagger parameter
gamma_test = -0.017

# Hubble Constants
h0_lcdm = hubble_finder_LCDM()
h0_8 = hubble_finder_gDE(gamma_test, -8)
h0_12 = hubble_finder_gDE(gamma_test, -12)
h0_16 = hubble_finder_gDE(gamma_test, -16)
h0_20 = hubble_finder_gDE(gamma_test, -20)

# ---------- E(z) ----------
Ez_LCDM = [E_function_LCDM(z, h0_lcdm) for z in z_values]
Ez_8 = [E_function_gDE(z, h0_8, gamma_test, -8) for z in z_values]
Ez_12 = [E_function_gDE(z, h0_12 , gamma_test, -12) for z in z_values]
Ez_16 = [E_function_gDE(z, h0_16 , gamma_test, -16) for z in z_values]
Ez_20 = [E_function_gDE(z, h0_20 , gamma_test, -20) for z in z_values]


# ---------- PLOTTING ----------

# latex rendering text fonts
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Function (1+x)**(1/2)
def forward(x):
	return (1+x)**(1/2)

def inverse(x):
    return x**2-1


fig, ax0 = plt.subplots(figsize=(19.20, 10.80))

# ---------- AX0 ----------

ax0.plot(z_values, Ez_LCDM, linestyle='-',
        color='black', label='$\Lambda$CDM')

ax0.plot(z_values, Ez_8, linestyle=(0, (1, 1)),
        color='#CC6677', label='$\lambda = -8$')

ax0.plot(z_values, Ez_12, linestyle=(0, (5, 10)),
        color='#DDCC77', label='$\lambda = -12$')

ax0.plot(z_values, Ez_16, linestyle=(0, (5, 1)),
        color='#999933', label='$\lambda = -16$')

ax0.plot(z_values, Ez_20, linestyle=(0, (3, 1, 1, 1, 1, 1)),
        color='#44AA99', label='$\lambda = -20$')


# ---------- GRAPH OPTIONS ----------

# Setting Limits
ax0.set_xlim(1, 0)
# Setting Labels
ax0.set_ylabel('$E(z)$')
ax0.set_xlabel('$z$')
# Minor Ticks
ax0.yaxis.set_ticks_position('both')
ax0.xaxis.set_ticks_position('both')
ax0.yaxis.set_minor_locator(tck.AutoMinorLocator())
# Tick Options
ax0.tick_params(which='major', width=1, size=7, direction='in')
ax0.tick_params(which='minor', width=0.6, size=4, direction='in')
# Other Options
ax0.set_xscale('function', functions=(forward, inverse))
ax0.legend()

# Mean values and Errors for E(z) data obtained from Table 2 in given article
ax0.errorbar(0.07, 0.997, yerr=0.023, fmt='o', ecolor='blue')
ax0.errorbar(0.20, 1.111, yerr=0.020, fmt='o', ecolor='blue')
ax0.errorbar(0.35, 1.128 , yerr=0.037, fmt='o', ecolor='blue')
ax0.errorbar(0.55, 1.364, yerr=0.063, fmt='o', ecolor='blue')
ax0.errorbar(0.90, 1.52, yerr=0.12, fmt='o', ecolor='blue')

plt.show()
fig.savefig('plots/E_function_17.eps',rasterized=True,dpi=600)
