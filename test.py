from main_functions import z_dagger_finder, Q
from numpy import log as ln

print(round(z_dagger_finder(-0.017, -12),  2))
print(round(z_dagger_finder(-0.017, -16), 2))
print(round(z_dagger_finder(-0.017, -20), 2))

print(Q(500, -0.017, -12))
print(Q(1000, -0.017, -12))
print(Q(100000000, -0.017, -12))
