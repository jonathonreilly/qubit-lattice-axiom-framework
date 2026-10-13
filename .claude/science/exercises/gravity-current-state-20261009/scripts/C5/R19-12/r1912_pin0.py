"""R19-12: the Dirac-only pin at m -> 0+ : {mu_T2(b_f, r; m_f = 0) = 0 (R18-9 lib9, GL(4,10)), Sigma = 8 G_1/2(b_f, r) = 0}.
mu_T2 and Sigma are both Dirac-only rows, so this fixes the Dirac edge of a Sigma = 0 one-law root, whatever the photon and scalars do.
Also at m = 0.01 for comparison."""
import os, sys, time, numpy as np
from scipy.optimize import brentq
from r1912_lib import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'arch', 'R18-9'))
import lib9 as L9
t0 = time.time()
def G0p(bf, r):
    g1, g2 = G_dirac(bf, r, 0.0025, 192), G_dirac(bf, r, 0.005, 192); return 2*g1 - g2
for mf in (0.0, 0.01):
    rs = lambda bf: L9.rstar(bf, m=mf, q=(4, 10))
    for bf in (0.82, 0.84, 0.86, 0.9154):
        r = rs(bf); print('m_f=%g b_f %.4f r*(b_f) %.6f G12(0+) %+.6f' % (mf, bf, r, G0p(bf, r)), flush=True)
    bfs = brentq(lambda bf: G0p(bf, rs(bf)), 0.80, 0.88, xtol=1e-9); rr = rs(bfs)
    print('PIN m_f=%g: b_f = %.8f r = %.8f  (G12 there %+.2e; mu_T2 per field %+.2e) (%.0fs)' % (mf, bfs, rr, G0p(bfs, rr), L9.muT2(bfs, rr, m=mf, q=(4, 10)), time.time()-t0), flush=True)
