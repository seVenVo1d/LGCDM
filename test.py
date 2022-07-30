from numpy import arange, linspace
from main_functions import z_dagger_finder, hubble_finder

# gamma_values = arange(-0.001, -0.019, -0.001)
# lamda_values = arange(-4, -25, -1)

# for gamma in gamma_values:
#     print('----------')
#     for lamda in lamda_values:
#         if z_dagger_finder(gamma, lamda) < 10:
#             print(gamma, lamda)

print(round(z_dagger_finder(-0.013, -24), 2))
print(round(z_dagger_finder(-0.015, -24), 2))
print(round(z_dagger_finder(-0.017, -24), 2))
