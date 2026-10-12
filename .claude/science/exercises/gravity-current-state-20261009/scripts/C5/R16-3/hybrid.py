"""Hybrid laws for the 3-condition problem (Eg = T2g = mu_E = 0, P62): box b=1.0, descent to V, n_z zigzags of amplitude amp,
then a rise of height R at slope 1, then flat to pi (terrace at high sigma: high-kurtosis f for mu_E < 0). wt = 0.03. m = 0.01, vertex M."""
import numpy as np, sys, itertools; sys.path.insert(0, '.')
from zz import *
NF = 1 << 16; out = []
for V, amp, nz, R in itertools.product([0.3, 0.4, 0.5], [0.08, 0.12, 0.2], [2, 4, 6], [0.5, 1.0, 1.5, 2.0]):
    vals = [1.0, -1.0]; bks = [1.0]; k = 1.0 + (1.0 - V); s = 1
    for i in range(nz):
        bks.append(k); vals.append(float(s)); k += amp; s = -s
    # end of zigzag: level is V (if nz even) or V+amp; then rise R
    bks.append(k); vals.append(1.0); k += R; bks.append(k); vals.append(0.0)
    if k > np.pi - 0.05: continue
    L = ZLaw(vals, bks, 0.03, 'H(V=%.2f,amp=%.2f,nz=%d,R=%.1f)' % (V, amp, nz, R), nf=NF)
    if np.abs(L.sp).max() > 1 + 1e-12: continue
    g, f = L.samples(1 << 13); X = xi_all(g, f, 0.01, nu=600); mu = mu_E(g, f, 0.01, nu=600)
    out.append((mu, X['M,Eg'], X['M,T2g'], X['U,Eg'], X['U,T2g'], L.name))
print('%d hybrids' % len(out))
ok = [o for o in out if o[1] > 0 and o[2] > 0]
print('with M Eg>0 and T2g>0: %d; min mu_E among them:' % len(ok))
for o in sorted(ok)[:6]: print('  mu_E %+.3e | M Eg %+.2e T2g %+.2e | U Eg %+.2e T2g %+.2e | %s' % o)
neg = [o for o in out if o[0] < 0]
print('with mu_E<0: %d; max min(M Eg, M T2g) among them:' % len(neg))
for o in sorted(neg, key=lambda o: -min(o[1], o[2]))[:6]: print('  mu_E %+.3e | M Eg %+.2e T2g %+.2e | U Eg %+.2e T2g %+.2e | %s' % o)
