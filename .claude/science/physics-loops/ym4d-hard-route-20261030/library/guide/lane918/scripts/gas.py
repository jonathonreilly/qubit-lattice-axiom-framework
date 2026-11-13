#!/usr/bin/env python3
"""GUIDE dilute-gas model (row 918) of the thermal sums of the periodic box b^3 at time t.
Assumption (stated, not proved): the low spectrum is a dilute Boltzmann gas of free glueballs (even) and of one Z_2
electric flux per direction (odd under that direction's centre flip), E(p)^2 = E^2 + phat^2, phat_i = 2 sin(p_i/2).
Then G_glue = sum_species mult sum_p e^(-t E(p)), z_i = sum_(p_perp) e^(-t E_f(p_perp)), and
  1 + S = e^(G_glue) prod_i e^(z_i),  1 + S_ev = e^(G_glue) prod_i cosh(z_i),  rho_(100) = e^(-2 z_1),  Q_0 = (1 - rho)/2.
Usage: gas.py beta  (parameter sets below; masses in lattice units)
"""
import sys
import numpy as np

PARS = {
    # m_0: this campaign's spectroscopy (Step 3b) and the RECALLED large-volume value; sigma RECALLED (a^2 sigma)
    '2.3': dict(m0=[1.30, 1.40], sigma=0.136),
    '2.5': dict(m0=[0.90, 0.70], sigma=0.0336),
}
# RECALLED glueball ratios m/m_0 and multiplicities (0++ 1; 2++ 5; 0-+ 1; 2-+ 5; 1+- 3); used for a rough upper count
SPECIES = [(1.0, 1), (1.45, 5), (1.55, 1), (1.75, 5), (1.8, 3)]


def phat2(b, dims):
    n = np.arange(b); p = 2*np.sin(np.pi*n/b)
    grids = np.meshgrid(*([p**2]*dims), indexing='ij')
    return sum(grids).ravel()


def sums(t, b, m0, sigma):
    P3 = phat2(b, 3); P2 = phat2(b, 2)
    G = sum(mult*np.exp(-t*np.sqrt((r*m0)**2 + P3)).sum() for r, mult in SPECIES)
    Ef = sigma*b - np.pi/(3*b)
    z = np.exp(-t*np.sqrt(max(Ef, 1e-9)**2 + P2)).sum() if Ef > 0 else np.inf
    S = np.expm1(G + 3*z); Sev = np.exp(G)*np.cosh(z)**3 - 1
    rho = np.exp(-2*z)
    return S, Sev, (1 - rho)/2, G, z


beta = sys.argv[1]; pr = PARS[beta]
for m0 in pr['m0']:
    print(f"beta {beta}, m_0 = {m0}, a^2 sigma = {pr['sigma']}")
    print("  cube (N; (2N)^3):  N  S  S_ev  Q_0  [glue part, one-direction flux z]")
    first = None
    for N in range(2, 41):
        S, Sev, Q, G, z = sums(N, 2*N, m0, pr['sigma'])
        if N <= 6 or N % 2 == 0:
            print(f"   {N:3d}  {S:.3e}  {Sev:.3e}  {Q:.2e}  [{G:.2e}, {z:.2e}]")
        if first is None and S < 1/5041: first = N
        if N > 6 and S < 1e-5: break
    print(f"  first cube with S < 1/5041: N = {first}, side {2*first if first else None}, m_0 N = {m0*first if first else None}")
    print("  SH shape (a; (24a)^3): a  S  S_ev  Q_0")
    for a in range(2, 25):
        S, Sev, Q, G, z = sums(a, 24*a, m0, pr['sigma'])
        print(f"   {a:3d}  {S:.3e}  {Sev:.3e}  {Q:.2e}")
        if S < 0.01: break
