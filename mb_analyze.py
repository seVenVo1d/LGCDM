# Binned Pantheon Data Obtained from
# https://archive.stsci.edu/hlsps/ps1cosmo/scolnic/binned_data/hlsp_ps1cosmo_panstarrs_gpc1_all_model_v1_lcparam.txt
# https://archive.stsci.edu/doi/resolve/resolve.html?doi=10.17909/T95Q4X

from operator import index
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np
import pandas as pd
from scipy.integrate import quad

from main_functions_gde import hubble_finder_gDE, z_d_finder
from main_functions_lcdm import hubble_finder_LCDM

# Adjusting size of the figure
params = {'legend.fontsize': '14',
          'figure.figsize': (19.20, 10.80),
          'axes.labelsize': '20',
          'xtick.labelsize':'20',
          'ytick.labelsize':'20'}
pylab.rcParams.update(params)

# Parameters
c = 299792.458   # speed of light in [km/s]
N_eff = 3.046   # effective neutrino number

w_b = 0.022383   # physical baryon density parameter
w_c = 0.12011   # physical cold dark matter density parameter
w_m = w_b + w_c   # physical matter density parameter

w_p = 2.469 * 10**(-5)   # physical photon density parameter
w_n = 2.469 * 10**(-5)*(7/8)*(4/11)**(4/3)*N_eff   # physical neutrino density parameter
w_r = w_p + w_n  # physical radiation density parameter


# Defining the distance modulus
def Mb_finder_LCDM(row):
    z_i, mb, mb_err = row[[1, 4, 5]]
    h0 = hubble_finder_LCDM()
    def integrand(z):
        return c / (100 * np.sqrt(w_m*(1+z)**3 + w_r*(1+z)**4 + (h0**2-w_m-w_r)))
    integral = quad(integrand, 0, z_i)[0]
    distance_mod = 5*np.log10((1+z_i)*10**5*integral)
    Mb = mb - distance_mod
    Mb_error = mb_err
    return (z_i, Mb, Mb_error)


def Mb_finder_gDE(row):
    gamma = -0.015
    lamda = -10
    z_i, mb, mb_err = row[[1, 4, 5]]
    h0 = hubble_finder_gDE(-0.015, -10)
    y = 1 / (1 - lamda)
    def integrand(z):
        x = 1 - 3*gamma*(lamda-1)*np.log(1+z)
        Q = np.copysign(1, x)*abs(x)**y
        return c / (100 * np.sqrt(w_m*(1+z)**3 + w_r*(1+z)**4 + (h0**2-w_m-w_r)*Q))
    integral = quad(integrand, 0, z_i)[0]
    distance_mod = 5*np.log10((1+z_i)*10**5*integral)
    Mb = mb - distance_mod
    Mb_error = mb_err
    return (z_i, Mb, Mb_error)

# Importing data
data = pd.read_csv('mb_data.txt', sep=' ')


# ------------ LCDM ---------------
Mb_LCDM = data.apply(Mb_finder_LCDM, axis=1)
z_values_lcdm, M_b_values_lcdm, M_b_err_values_lcdm = [], [], []

for z_i, M_b, M_b_err in  Mb_LCDM:
    z_values_lcdm.append(z_i)
    M_b_values_lcdm.append(M_b)
    M_b_err_values_lcdm.append(M_b_err)



# ------------ gDE ------------------
Mb_gDE = data.apply(Mb_finder_gDE, axis=1)
z_values_gde, M_b_values_gde, M_b_err_values_gde = [], [], []

for z_i, M_b, M_b_err in  Mb_gDE:
    z_values_gde.append(z_i)
    M_b_values_gde.append(M_b)
    M_b_err_values_gde.append(M_b_err)

#---------- PLOTTING ----------

# Function (1+x)**(1/2)
def forward(x):
	return x**(1/3)

def inverse(x):
    return x**3

# latex rendering text fonts
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig, ax0 = plt.subplots()  # adjusting the size of the figure
ax0.errorbar(z_values_lcdm, M_b_values_lcdm, yerr=M_b_err_values_lcdm, fmt='s', ecolor='black', label='$\Lambda$CDM' )
ax0.errorbar(z_values_gde, M_b_values_gde, yerr=M_b_err_values_gde, fmt='v', ecolor='red', label='$\gamma=-0.015, \lambda=-10$')

# ---------- GRAPH OPTIONS ----------

# Setting Limits
ax0.set_xlim(0, 2)
# Setting Label
ax0.set_ylabel('$M_B$ [mag]')
ax0.set_xlabel('$z$')
# Scaling
ax0.set_xscale('function', functions=(forward, inverse))
ax0.set_xticks([0.05, 0.1, 0.5, 1, 2])
# Minor Ticks
ax0.yaxis.set_ticks_position('both')
ax0.xaxis.set_ticks_position('both')
ax0.yaxis.set_minor_locator(tck.AutoMinorLocator())
# Tick Options
ax0.tick_params(which='major', width=1, size = 7, direction='in')
ax0.tick_params(which='minor', width=0.6, size = 4, direction='in')

plt.show()
ax0.set_rasterized(True)
fig.savefig('plots/h0_vs_lambda.eps',rasterized=True,dpi=600)
