from numpy import copysign, sqrt, exp
from numpy import log as ln
from scipy.integrate import quad


# Important Parameters
c = 299792.458  # speed of light in [km/s]
N_eff = 3.046  # effective neutrino number
w_r = 2.469 * 10**(-5) * (1 + (7/8)*(4/11)**(4/3)*N_eff)  # radiation density parameter
w_m = 0.1430  # matter density parameter
z_rec = 1089.92  # redshift to the recombination
theta_star = 0.0104110
r_star = 144.43


# angular diameter distance to the recombination in [Mpc]
C_true = (100 * r_star) / (c * theta_star)


#--------- FINDING d_A(z_rec) ---------#


def C_finder(z, h0, gamma, lamda):
    """
    Finding the C for LSCDM model

    Args:
        z : the redshift
        h : the hubble parameter h = H / 100
        gamma : gamma parameter for the LSCDM model
        lamda : lambda parameter for the LSCDM model
    """
    y = 1 / (1 - lamda)
    x = 1 - 3*gamma*(lamda-1)*ln(1+z)
    Q = copysign(1, x) * abs(x)**y
    return 1 / sqrt(w_m*(1+z)**3 + w_r*(1+z)**4 + (h0**2-w_m-w_r)*Q)


def C_finder_LCDM(z, h0):
    """
    Finding the C for LCDM model

    Args:
        z : the redshift
        h : the hubble parameter h = H / 100
    """
    return 1 / sqrt(w_m*(1+z)**3 + w_r*(1+z)**4 + (h0**2-w_m-w_r))


#--------- FINDING HUBBLE CONSTANT ---------#


def hubble_finder(gamma, lamda):
    """
    Finding the hubble constant for LSCDM Model - 10**(-6) precision

    Args:
        gamma : gamma parameter for the LSCDM model
        lamda : lambda parameter for the LSCDM model
    """
    h_min, h_max = 0.4, 0.9
    for i in range(100):
        h0_test = (h_min + h_max) / 2
        C_test = quad(C_finder, 0, z_rec, args=(h0_test, gamma, lamda))[0]
        if abs(C_true - C_test) > 10**(-6):
            if C_true - C_test > 0:
                h_max = h0_test
            else:
                h_min = h0_test
        else:
            break
    return h0_test * 100



def hubble_finder_LCDM():
    """
    Finding the hubble constant for LCDM Model - 10**(-6) precision
    """
    h_min, h_max = 0.4, 0.9
    for i in range(100):
        h0_test = (h_min + h_max) / 2
        C_test = quad(C_finder_LCDM, 0, z_rec, args=(h0_test))[0]
        if abs(C_true - C_test) > 10**(-6):
            if C_true - C_test > 0:
                h_max = h0_test
            else:
                h_min = h0_test
        else:
            break
    return h0_test * 100


#--------- HUBBLE FUNCTIONS FOR MODELS ---------#


def hubble_function(z, h0, gamma, lamda):
    """
    Hubble function for LSCDM

    Args:
        z : the redshift
        h0 : reduced hubble parameter
        gamma : gamma parameter for the LSCDM model
        lamda : lambda parameter for the LSCDM model
    """
    y = 1 / (1 - lamda)
    x = 1 - 3*gamma*(lamda-1)*ln(1+z)
    Q = copysign(1, x) * abs(x)**y
    return 100 * sqrt(w_m*(1+z)**3 + w_r*(1+z)**4 + (h0**2-w_m-w_r) * Q)


def hubble_function_LCDM(z, h0):
    """
    Hubble function for LCDM

    Args:
        z : the redshift
        h0 : reduced hubble parameter
    """
    return 100 * sqrt(w_m*(1+z)**3 + w_r*(1+z)**4 + (h0**2-w_m-w_r))


#--------- CALCULATING Q AND C ---------#


def Q(z, gamma, lamda):
    y = 1 / (1 - lamda)
    x = 1 - 3*gamma*(lamda-1)*ln(1+z)
    return copysign(1, x) * abs(x)**y


#--------- CALCULATING D_M ---------#

def dm(z, h0, gamma, lamda):
    '''Finds the D_M(z) for the given variables, z_* and lambda'''
    def E(z):
        ''' dz/E(z) function for gDE'''
        y = 1 / (1 - lamda)
        x = 1 - 3*gamma*(lamda-1)*ln(1+z)
        Q = copysign(1, x) * abs(x)**y
        return 1 / (100 * sqrt(w_m*(1+z)**3 + w_r*(1+z)**4 + (h0**2-w_m-w_r) * Q))
    # from now on calculating D_M for different z values
    S = quad(E, 0, z)[0]  # integrating dz/E(z)
    return c*S


def dm_LCDM(z, h0):
    '''Finds the D_M(z) for the LCDM'''
    def E_LCDM(z):
        '''dz/E(z) function for LCDM model'''
        return 1 / (100 * sqrt(w_m*(1+z)**3 + w_r*(1+z)**4 + (h0**2-w_m-w_r)))
    S = quad(E_LCDM, 0, z)[0]
    return c*S


#--------- CALCULATING EoS PARAMETER ---------#

def w_g(z, gamma, lamda):
    x = 1 - 3*gamma*(lamda-1)*ln(1+z)
    return -1 + (gamma/x)


#--------- CALCULATING MATTER DENSITY PARAMETER ---------#
def Omega_m0(gamma, lamda):
    h0 = hubble_finder(gamma, lamda) / 100
    return w_m/h0**2


#--------- CALCULATING E(z) FUNCTION (E(z) = H(z)/H0) ---------#
def E_function(z, h0, gamma, lamda):
    """
    E(z) for LSCDM model

    Args:
        z : the redshift
        h0 : reduced hubble parameter
        gamma : gamma parameter for the LSCDM model
        lamda : lambda parameter for the LSCDM model
    """
    Omega_m = w_m / h0**2
    Omega_r = w_r / h0**2
    y = 1 / (1 - lamda)
    x = 1 - 3*gamma*(lamda-1)*ln(1+z)
    Q = copysign(1, x) * abs(x)**y
    return sqrt(Omega_m*(1+z)**3 + Omega_r*(1+z)**4 + (1-Omega_m-Omega_r)*Q)


def E_function_LCDM(z, h0):
    """
    E(z) for LCDM model

    Args:
        z : the redshift
        h0 : reduced hubble parameter
    """
    Omega_m = w_m / h0**2
    Omega_r = w_r / h0**2
    return sqrt(Omega_m*(1+z)**3 + Omega_r*(1+z)**4 + (1-Omega_m-Omega_r))

#--------- CALCULATING TRANSITION REDSHIFT ---------#

def z_dagger_finder(gamma, lamda):
    psi = 3*gamma*(lamda-1)
    return exp(1/psi) - 1

