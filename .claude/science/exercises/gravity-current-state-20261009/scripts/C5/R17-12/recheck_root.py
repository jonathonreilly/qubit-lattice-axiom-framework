"""Recheck of R17-9's archived VM root (smroot_VM_N48.npy) with R17-9's own matter routines and my VMone vertex code."""
import numpy as np
from r1712_lib import xi, photonGw
from content3 import ferm
from content4 import scalw
from zz import mu_E
z = np.load('smroot_VM_N48.npy'); bg, fwg, bf, r, bs, frs = z; m = 0.01
law = photonGw(bg, fwg*(np.pi - bg)); g, f = law.samples(1 << 14)
S = 4*scalw(bs, frs, m, vert='U')[0]; F = 22.5*ferm(bf, r, m)[0]
for var in ('VMone', 'VMsym', 'VW0', 'VU'):
    V = 12*np.array([xi(law, 48, 'T2g', var)[0], xi(law, 48, 'Eg', var)[0], 2*mu_E(g, f, 1e-3), 0.0])
    t = S + F + V
    print('%-6s at R17-9 VM root (N=48): TOTAL Xi_T2g %+.4e Xi_Eg %+.4e mu_E %+.4e mu_T2 %+.4e | 12 vectors %s' % ((var,) + tuple(t) + (np.array2string(V, precision=4),)))
print('scalars', S, '\nDirac', F)
