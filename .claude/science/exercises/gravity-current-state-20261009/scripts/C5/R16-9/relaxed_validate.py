"""Validate relaxed evaluator against zz.py: box [0,1] + flat at sigma=1 (mass pi-1), and box [0,1] + fast atom at level 0.5 realized
by a dense zigzag 0.45<->0.55 is approximated; here only the exact-representable flat case plus a two-level case via ZLaw with tiny wt."""
import numpy as np, sys; sys.path.insert(0, '.')
from zz import *
for VTX in ['M', 'U']:
    sys.argv = ['x', VTX, '0.1', '0.15', '0.3', '0', '0']
    src = open('relaxed.py').read().split('rng = np.random')[0]; ns = {}; exec(src, ns)
    L_, lev, NSG, SG = ns['L'], ns['lev'], ns['NSG'], ns['SGRID']
    # law 1: box [0,1], flat at level 1 -> represent: put mass at the level nearest 1.0 (use exact level by shifting grid point)
    for (bb, name) in [(1.0, 'box1+flat'), (0.7, 'box0.7+flat')]:
        i = np.argmin(np.abs(lev - bb)); ns['lev'][i] = bb
        A = np.zeros((NSG, L_)); A[0, i] = np.pi - bb
        x = np.concatenate([[bb], A.ravel() + 0.0]); x[1:][x[1:] == 0] = 0
        Eg, T2, mu, b, AA = ns['evalq'](np.concatenate([[bb], A.ravel()]))
        Z = ZLaw([1.0, 0.0], [bb], 0.002, name, nf=1 << 20); g, f = Z.samples(1 << 16); X = xi_all(g, f, 0.1, nu=2000); muz = mu_E(g, f, 0.1, nu=2000)
        print('%s %s relaxed: Eg %+.5e T2g %+.5e mu %+.5e | zz(wt=0.002): Eg %+.5e T2g %+.5e mu %+.5e' % (VTX, name, Eg, T2, mu, X[VTX+',Eg'], X[VTX+',T2g'], muz))
