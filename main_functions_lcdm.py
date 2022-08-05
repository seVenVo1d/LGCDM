import numpy as np
from scipy.integrate import quad


# --------- PARAMETERS ---------
# These Parameters are taken from https://arxiv.org/pdf/1807.06209.pdf
# Table I. Upper Panel Plik Best Fit Values


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


def r_s_finder_LCDM(h0):
    """Calculating the comoving sound horizon at the LSS (r_s)"""
    def integrand(z):
        R = (3*w_b) / (4*w_p*(1+z))
        c_s = c / np.sqrt(3*(1+R))
        return c_s / (100 * np.sqrt(w_m*(1+z)**3 + w_r*(1+z)**4 + (h0**2-w_m-w_r)))
    r_s = quad(integrand, z_star, np.inf)[0]
    return r_s


def r_d_finder_LCDM(h0):
    """Calculating the comoving sound horizon at the BDE (r_d)"""
    def integrand(z):
        R = (3*w_b) / (4*w_p*(1+z))
        c_s = c / np.sqrt(3*(1+R))
        return c_s / (100 * np.sqrt(w_m*(1+z)**3 + w_r*(1+z)**4 + (h0**2-w_m-w_r)))
    r_d = quad(integrand, z_d, np.inf)[0]
    return r_d


#--------- CALCULATING COMOVING ANGULAR DIAMETER DISTANCE AT THE LSS ---------#


def d_A_finder_LCDM(h0):
    """Calculating the comoving angular diameter distance to the LSS (d_A(z_*))"""
    def integrand(z):
        return c / (100 * np.sqrt(w_m*(1+z)**3 + w_r*(1+z)**4 + (h0**2-w_m-w_r)))
    r_s = quad(integrand, 0, z_star)[0]
    return r_s


#--------- FINDING HUBBLE CONSTANT ---------#

def hubble_finder_LCDM():
    """Finding the Hubble constant"""
    h_min, h_max = 0.4, 1   # h_0 prior range
    for i in range(100):
        h0_test = (h_min + h_max) / 2
        r_s_test = r_s_finder_LCDM(h0_test)
        d_A_test = d_A_finder_LCDM(h0_test)
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

def hubble_function_LCDM(z, h0):
    """Hubble function H(z)"""
    return 100 * np.sqrt(w_m*(1+z)**3 + w_r*(1+z)**4 + (h0**2-w_m-w_r))

#--------- EVALUATING E(z) ---------#

def E_function_LCDM(z, h0):
    """E(z) function"""
    Omega_m = w_m / h0**2
    Omega_r = w_r / h0**2
    return np.sqrt(Omega_m*(1+z)**3 + Omega_r*(1+z)**4 + (1-Omega_m-Omega_r))


#--------- EVALUATING D_M ---------#

def d_M_function_LCDM(z, h0):
    """Finding the D_M(z)"""
    def integrand(z):
        """1/H(z) for LCDM"""
        return c / (100 * np.sqrt(w_m*(1+z)**3 + w_r*(1+z)**4 + (h0**2-w_m-w_r)))
    d_M = quad(integrand, 0, z)[0]
    return d_M
