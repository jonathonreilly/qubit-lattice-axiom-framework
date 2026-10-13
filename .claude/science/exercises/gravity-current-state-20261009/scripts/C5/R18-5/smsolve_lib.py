"""R17-9 (c): SM-count solve. Content: 4 real scalars on ONE edge G_w(b_s, w_s) [U vertex, SF], 22.5 Dirac on D1(b_f, r) [V0, SF],
12 massless vectors on one photon edge gammaGw(b_g, w_g) [vertex VM or VU; SF shear = 2 x scalar formula].  Common m = 0.01 (matter).
Rows: Xi_T2g, Xi_Eg, mu_E (FIXED) ; mu_T2 reported.  Knobs: (b_g, fw_g, b_f, r, b_s, fr_s), w = frac * (pi - b)."""
import numpy as np, sys, time
from photon import photonGw, photon_xi, photon_xi_VM
from content3 import ferm
from content4 import scalw
from zz import mu_E
from scipy.optimize import least_squares
vert = "VM"; Ng = 48
nfev = int(sys.argv[4]) if len(sys.argv) > 4 else 40
NS, ND, NV = 4.0, 22.5, 12.0
def phot(bg, fwg, N=Ng):
    law = photonGw(bg, fwg*(np.pi - bg))
    fx = photon_xi_VM if vert == 'VM' else photon_xi
    T = fx(law, N, 'T2g')[0]; E = fx(law, N, 'Eg')[0]
    g, f = law.samples(1 << 14)
    return np.array([T, E, 2*mu_E(g, f, 1e-3), 0.0]), law
def parts(z, N=Ng, m=0.01):
    bg, fwg, bf, r, bs, frs = z
    return NS*scalw(bs, frs, m, vert='U')[0], ND*ferm(bf, r, m)[0], NV*phot(bg, fwg, N)[0]
def tot(z, N=Ng, m=0.01):
    a, b, c = parts(z, N, m); return a + b + c
lo = [0.15, 0.05, 0.15, 0.02, 0.3, 0.02]; hi = [1.5, 1.0, 1.55, 0.5773, 3.0, 1.0]
