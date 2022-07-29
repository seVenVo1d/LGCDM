# Plotting the Hubble Data Obtained from Table 2 in 
# https://arxiv.org/pdf/1802.01505.pdf

import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from numpy import arange

from main_functions import (E_function, E_function_LCDM, hubble_finder,
                            hubble_finder_LCDM)


# Important Parameters
N_eff = 3.046  # effective neutrino number
w_r = 2.469 * 10**(-5) * (1 + (7/8)*(4/11)**(4/3)*N_eff)  # radiation density parameter
w_m = 0.1430  # matter density parameter

# z values that will be used for the x axis. Runs from z=0 to z=1 with step size 0.001
z_values = arange(0, 1, 0.001)

# Adjusting the z_dagger parameter
gamma_test = -0.019

# Hubble Constants
h0_lcdm = hubble_finder_LCDM() / 100
h0_12 = hubble_finder(gamma_test, -12) / 100
h0_14 = hubble_finder(gamma_test, -14) / 100
h0_16 = hubble_finder(gamma_test, -16) / 100
h0_18 = hubble_finder(gamma_test, -18) / 100

# ---------- E(z) ----------
Ez_LCDM = [E_function_LCDM(z, h0_lcdm) for z in z_values]
Ez_12 = [E_function(z, h0_12, gamma_test, -12) for z in z_values]
Ez_14 = [E_function(z, h0_14 , gamma_test, -14) for z in z_values]
Ez_16 = [E_function(z, h0_16 , gamma_test, -16) for z in z_values]
Ez_18 = [E_function(z, h0_18 , gamma_test, -18) for z in z_values]


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

ax0.plot(z_values, Ez_12, linestyle=(0, (1, 1)),
        color='#CC6677', label='$\lambda = -12$')

ax0.plot(z_values, Ez_14, linestyle=(0, (5, 10)),
        color='#DDCC77', label='$\lambda = -14$')

ax0.plot(z_values, Ez_16, linestyle=(0, (5, 1)),
        color='#999933', label='$\lambda = -16$')

ax0.plot(z_values, Ez_18, linestyle=(0, (3, 1, 1, 1, 1, 1)),
        color='#44AA99', label='$\lambda = -32$')


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
fig.savefig('plots/E_function_19.eps',rasterized=True,dpi=600)
