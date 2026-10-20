import numpy as np
import pandas as pd

xl      = -30*(10**(-9))
lint    = 5.25*(10**(-9))
L1 = 65*(10**(-9))
L2 = 70*(10**(-9))
wint    = 5e-009 
W = 1e-6
toxe    = 1.85e-9 
e_ox = 1e-12


Leff_1 = L1 + xl - 2*lint
Leff_2 = L2 + xl - 2*lint
Weff = W - 2*wint
Cox = e_ox/toxe

print("\n       65_nm:","\nLeff is",Leff_1,"\nWeff is",Weff,"\nCox is",Cox)
print("\n       70_nm:","\nLeff is",Leff_2,"\nWeff is",Weff,"\nCox is",Cox)

