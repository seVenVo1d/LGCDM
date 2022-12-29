import numpy as np
from scipy.integrate import quad

# --------- PARAMETERS ---------
# These Parameters are taken from https://arxiv.org/pdf/1807.06209.pdf
# Table I. Upper Panel Plik Best Fit Values

# Prior Ranges
# gamma = (-0.001, -0.018)
# lambda = (-4, -24)


c = 299792.458   # speed of light in [km/s]
N_eff = 3.046   # effective neutrino number

w_b = 0.022383   # physical baryon density parameter
w_c = 0.12011   # physical cold dark matter density parameter
w_m = w_b + w_c   # physical matter density parameter

w_p = 2.469 * 10**(-5)   # physical photon density parameter
w_n = 2.469 * 10**(-5)*(7/8)*(4/11)**(4/3)*N_eff   # physical neutrino density parameter
w_r = w_p + w_n  # physical radiation density parameter

theta_true = 0.01040909   # approximation to the acoustic scale angle

hubble_error = 10**(-8) # the error while calculating the hubble constant


#--------- CALCULATING REDSHIFTS TO LSS and BDE ---------#
# See https://arxiv.org/pdf/astro-ph/9510117.pdf for further information


def z_star_finder(w_b, w_m):
    """Calculating the redshift to the Last Scattering Surface (LSS)"""
    g1 = 0.0783*w_b**(-0.238)*(1+39.5*w_b**(0.763))**(-1)
    g2 = 0.56*(1+21.1*w_b**(1.81))**(-1)
    z_star = 1048*(1+0.00124*w_b**(-0.738))*(1+g1*w_m**g2)
    return z_star


def z_d_finder(w_b, w_m):
    """Calculating the redshift to the Baryon Drag Epoch (BDE)"""
    b1 = 0.313*w_m**(-0.419)*(1+0.607*w_m**(0.674))
    b2 = 0.238*w_m**(0.223)
    b3 = w_m**(0.251) / (1+0.659*w_m**(0.828))
    z_d = 1345*b3*(1+b1*w_b**b2)
    return z_d


# Redshift parameters for a given w_b and w_m
z_star = z_star_finder(w_b, w_m)
z_d = z_d_finder(w_b, w_m)


#--------- CALCULATING THE COMOVING SOUND HORIZON AT THE LSS and BDE ---------#


def r_s_finder_gDE(h0, gamma, lamda):
    """Calculating the comoving sound horizon at the LSS (r_s)"""
    y = 1 / (1 - lamda)
    def integrand(z):
        x = 1 - 3*gamma*(lamda-1)*np.log(1+z)
        Q = np.copysign(1, x)*abs(x)**y
        R = (3*w_b) / (4*w_p*(1+z))
        c_s = c / np.sqrt(3*(1+R))
        return c_s / (100 * np.sqrt(w_m*(1+z)**3 + w_r*(1+z)**4 + (h0**2-w_m-w_r)*Q))
    r_s = quad(integrand, z_star, np.inf)[0]
    return r_s


def r_d_finder_gDE(h0, gamma, lamda):
    """Calculating the comoving sound horizon at the BDE (r_d)"""
    y = 1 / (1 - lamda)
    def integrand(z):
        x = 1 - 3*gamma*(lamda-1)*np.log(1+z)
        Q = np.copysign(1, x)*abs(x)**y
        R = (3*w_b) / (4*w_p*(1+z))
        c_s = c / np.sqrt(3*(1+R))
        return c_s / (100 * np.sqrt(w_m*(1+z)**3 + w_r*(1+z)**4 + (h0**2-w_m-w_r)*Q))
    r_d = quad(integrand, z_d, np.inf)[0]
    return r_d


#--------- CALCULATING COMOVING ANGULAR DIAMETER DISTANCE AT THE LSS ---------#

def d_A_finder_gDE(h0, gamma, lamda):
    """Calculating the comoving angular diameter distance to the LSS (d_A(z_*))"""
    y = 1 / (1 - lamda)
    def integrand(z):
        x = 1 - 3*gamma*(lamda-1)*np.log(1+z)
        Q = np.copysign(1, x)*abs(x)**y
        return c / (100 * np.sqrt(w_m*(1+z)**3 + w_r*(1+z)**4 + (h0**2-w_m-w_r)*Q))
    r_s = quad(integrand, 0, z_star)[0]
    return r_s


def hubble_finder_gDE(gamma, lamda):
    """Finding the Hubble constant"""
    h_min, h_max = 0.4, 1   # h_0 prior range
    for i in range(100):
        h0_test = (h_min + h_max) / 2
        r_s_test = r_s_finder_gDE(h0_test, gamma, lamda)
        d_A_test = d_A_finder_gDE(h0_test, gamma, lamda)
        theta_test = r_s_test / d_A_test
        if abs(theta_true - theta_test) > hubble_error: # adjusting the error
            if theta_true - theta_test > 0:
                h_min = h0_test
            else:
                h_max = h0_test
        else:
            break
    return h0_test


#--------- EVALUATING HUBBLE FUNCTION ---------#

def hubble_function_gDE(z, h0, gamma, lamda):
    """Hubble function """
    y = 1 / (1 - lamda)
    x = 1 - 3*gamma*(lamda-1)*np.log(1+z)
    Q = np.copysign(1, x)*abs(x)**y
    return 100 * np.sqrt(w_m*(1+z)**3 + w_r*(1+z)**4 + (h0**2-w_m-w_r) * Q)


#--------- CALCULATING Q ---------#

def Q(z, gamma, lamda):
    y = 1 / (1 - lamda)
    x = 1 - 3*gamma*(lamda-1)*np.log(1+z)
    return np.copysign(1, x) * abs(x)**y


#--------- CALCULATING E(z) ---------#
def E_function_gDE(z, h0, gamma, lamda):
    """E(z) function"""
    Omega_m = w_m / h0**2
    Omega_r = w_r / h0**2
    y = 1 / (1 - lamda)
    x = 1 - 3*gamma*(lamda-1)*np.log(1+z)
    Q = np.copysign(1, x) * abs(x)**y
    return np.sqrt(Omega_m*(1+z)**3 + Omega_r*(1+z)**4 + (1-Omega_m-Omega_r)*Q)


#--------- EVALUATING D_M ---------#
def d_M_function_gDE(z, h0, gamma, lamda):
    """Finding the d_M(z) for the given variables, gamma and lambda"""
    y = 1 / (1 - lamda)
    def integrand(z):
        x = 1 - 3*gamma*(lamda-1)*np.log(1+z)
        Q = np.copysign(1, x) * abs(x)**y
        return c / (100 * np.sqrt(w_m*(1+z)**3 + w_r*(1+z)**4 + (h0**2-w_m-w_r)*Q))
    d_M = quad(integrand, 0, z)[0]
    return d_M


#--------- CALCULATING EoS PARAMETER ---------#

def w_g(z, gamma, lamda):
    """Equation of State (EoS) parameter for gDE model"""
    x = 1 - 3*gamma*(lamda-1)*np.log(1+z)
    return -1 + (gamma/x)


#--------- CALCULATING THE MATTER DENSITY PARAMETER ---------#
def Omega_m0(gamma, lamda):
    """Matter Density Parameter"""
    h0 = hubble_finder_gDE(gamma, lamda)
    return w_m/h0**2


#--------- CALCULATING TRANSITION REDSHIFT ---------#
def z_dagger_finder(gamma, lamda):
    """Calculating the transition redshift for gDE"""
    psi = 3*gamma*(lamda-1)
    return np.exp(1/psi) - 1
