"""C6 (ARGUED arithmetic): a frozen pattern-free substrate has zero MEAN TT stiffness but a white-noise
local stiffness delta-mu(x) (variance per site sigma^2; CHECKED in C2b: per-realization sd ~ sigma/sqrt(N)).
Graviton wave equation (linearized GR, reduced Planck mass M): (M^2/8)(w^2 - q^2) h = delta-mu(x) h
 -> random 'mass' potential V = 8 delta-mu / M^2, white-noise strength W = <V^2> a^3.
Born (3D Helmholtz, point scatterers): 1/l = W/(4 pi), independent of frequency (mass-type disorder,
no Rayleigh w^4 suppression, unlike disorder that multiplies gradients)."""
import numpy as np
sd = {512: 0.00175, 1000: 0.00124, 1728: 0.00085}      # C2b per-realization sd of E''/N (scalar toy)
for N, s in sd.items(): print(f"N={N}: sd*sqrt(N) = {s*np.sqrt(N):.4f}  (white noise => constant)")
Mred_over_ainv = 2.435e18/1.221e19          # reduced Planck mass in units of a^-1 = M_Planck
for sigma in (0.04, 1e-2, 1e-3):
    W = (8*sigma/Mred_over_ainv**2)**2        # in units a^-1
    print(f"sigma={sigma:g} per cell, a = l_P: Born mean free path l = 4pi/W = {4*np.pi/W:.3g} Planck lengths")
# coarse cutoff Lambda = a^-1: W = (8 sigma Lambda^4/M^2)^2 Lambda^-3 ; require l > 1 Gpc
Gpc_inv_GeV = 1/(3.086e25/1.973e-16)        # 1/Gpc in GeV
M = 2.435e18
for sigma in (0.04, 1e-2):
    Lam = (4*np.pi*Gpc_inv_GeV*M**4/(64*sigma**2))**(1/5)
    print(f"sigma={sigma:g}: mean free path > 1 Gpc needs cutoff a^-1 < {Lam:.2g} GeV")
