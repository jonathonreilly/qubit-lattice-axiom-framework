"""R17-7 (b): does one edge tuning plus one enthalpy tuning remove the grid vacuum's enthalpy along a history
with changing masses (bridge d-ii)?  Uses R11-3's profiles (copied unchanged into ../recheck/R11-3, rerun byte-identical).
By Identity W (R11-3, refereed), E(m^2) := rho + p_U = -<eps trA>/6 with trA = 0 on the box; on the edge eps is bounded
away from 0, so E is analytic in m^2 at m = 0:  E = E0 + c2 m^2 + c4 m^4 + ...,
  c2 = -<trA/(12 eps)>,   c4 = (1/2) d^2E/d(m^2)^2 = <trA/(48 eps^3)>   (eps at m -> 0; per real scalar, lattice units).
Checked: c2 at the R11-3 edge root t* = 0.00117 (should be ~0), and c4 there (is it also ~0?).  Also a direct
finite-difference check of E(m^2) at t*.  Subtraction: none (absolute E; differences in m^2 only).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'recheck', 'R11-3'))
import numpy as np
from r113_profiles import profile
from scipy.optimize import brentq

def moments(name, m=1e-6, N=160):
    k = 2*np.pi*(np.arange(N) + 0.5)/N - np.pi
    u, up, upp = profile(name, k)
    Ux, Uy = np.meshgrid(u, u, indexing='ij'); Ax, Ay = np.meshgrid(upp/2 - 1, upp/2 - 1, indexing='ij')
    E = c2 = c4 = 0.0
    for iz in range(N):
        e = np.sqrt(m*m + Ux + Uy + u[iz]); trA = Ax + Ay + upp[iz]/2 - 1
        E += (-e*trA/6).sum(); c2 += (-trA/(12*e)).sum(); c4 += (trA/(48*e**3)).sum()
    n = float(N)**3
    return E/n, c2/n, c4/n

ts = brentq(lambda t: moments('T%.7f' % t)[1], 0.0, 0.2, xtol=1e-7)
print("edge root of c2 (U coupling, m -> 0): t* = %.6f (R11-3 reported 0.00117)" % ts)
for name in ['L', 'T%.7f' % ts, 'T0.1000000', 'G', 'NN']:
    E, c2, c4 = moments(name)
    print("  %-11s: E0 = %.6f ; c2 = %+.6f ; c4 = %+.6f" % (name, E, c2, c4))
# direct check of the expansion at t* with finite m
name = 'T%.7f' % ts
E0 = moments(name, m=1e-6)[0]
for m in [0.05, 0.1, 0.2]:
    E = moments(name, m=m)[0]
    print("  t*: m = %.2f: E(m) - E0 = %+.3e ; c4 m^4 = %+.3e" % (m, E - E0, moments(name)[2]*m**4))
MP, rhoL = 1.22089e19, 2.520e-47
c4s = moments(name)[2]
print("size at t* (a = l_P, RECALLED inputs): c4 (100 GeV)^4 = %.2e GeV^4 = %.1e rho_Lambda per real scalar" % (c4s*1e8, c4s*1e8/rhoL))
