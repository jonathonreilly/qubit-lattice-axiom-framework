# O3 part 1b: how exact must cell-scale pairing be for Lambda (vacuum energy), given a Planck cell?
# Vacuum energy per site of one real KG component: e(M) = 1/2 <omega>, omega^2 = M^2 + sum(2-2cos k).
# A pair (boson, fermion) with identical lattice dispersion and masses split by d(M^2) leaves
# rho_res = (de/dM^2) * d(M^2) per cell to leading order (quadratic sensitivity), de/dM^2|_0 = 1/4 <1/omega_0>.
import numpy as np
from numpy.polynomial.legendre import leggauss
n = 64
x, w = leggauss(n); k = 0.5*np.pi*(x+1); wk = 0.5*w
C = np.cos(k)
CX, CY, CZ = np.meshgrid(C, C, C, indexing='ij')
W3 = wk[:,None,None]*wk[None,:,None]*wk[None,None,:]
S = 6-2*(CX+CY+CZ)
inv = np.sum(W3/np.sqrt(S+1e-300))
# correct the integrable 1/k singularity crudely by comparing two resolutions
print("<1/omega_0> (n=64 GL) = %.5f" % inv)
d_e_dM2 = 0.25*inv
print("de/dM^2 at M=0: %.5f per real component (lattice units)" % d_e_dM2)
rhoL = 2.519e-47; MPl = 1.220890e19; MPlr = 2.435323e18
for name, Mc in [("a^-1 = M_Pl", MPl), ("a^-1 = Mbar_Pl", MPlr)]:
    # rho_res [GeV^4] = d_e_dM2 * dM2 [GeV^2] * Mc^2
    dM2 = rhoL/(d_e_dM2*Mc**2)
    print("%s: |sum_pairs d(M^2)| <= %.2e GeV^2  -> splitting sqrt = %.2e eV" % (name, dM2, np.sqrt(dM2)*1e9))
    print("    observed partner splittings >= (100 GeV)^2 = 1e4 GeV^2 -> excess %.1e" % (1e4/dM2))
# if the quadratic rule holds by structure (Str M^2 = 0 analogue), the quartic-log term ~ Delta^4/(64 pi^2) ln:
for D in [1e-12, 1e2, 1e3]:
    print("quartic residual ~ D^4/(64 pi^2) for D=%.0e GeV: %.2e GeV^4 = %.1e rho_Lambda" % (D, D**4/(64*np.pi**2), D**4/(64*np.pi**2)/rhoL))
# Sorkin-type count fluctuation comparator: rho ~ H0^2 Mbar^2 (order of magnitude)
H0 = 67.4*1e3/3.0856775814913673e22 * 6.582119569e-25  # GeV
print("H0 = %.3e GeV;  H0^2 Mbar_Pl^2 = %.2e GeV^4 (= %.2f rho_Lambda)" % (H0, H0**2*MPlr**2, H0**2*MPlr**2/rhoL))
