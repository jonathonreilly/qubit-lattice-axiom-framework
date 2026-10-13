"""F5 check (normalization of R19-35's Dirac Hess(nn) = +2.164325e-2 per field): rank-one form -(w/12)<u^4/E^3>, w = -2,
for n along z / [110] / [111], m = 0.01 and 0, R18-9 root, 80-node GL octant grid (integrand even in each k_j)."""
import numpy as np, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f5_lib import *
n_, hm, mph = 4, 0.35, 3
br = mkbreaks(ROOT[0], CPH, mph); x, w = panels(br, n_, hm)
X, Y, Z = x[:, None, None], x[None, :, None], x[None, None, :]
WW = w[:, None, None]*w[None, :, None]*w[None, None, :]
for m in (0.01, 0.0):
    F = Ferm(*ROOT, mflow=m)
    M = m + F.W(X) + F.W(Y) + F.W(Z); E = np.sqrt(F.s(X)**2 + F.s(Y)**2 + F.s(Z)**2 + M*M)
    p = [F.s(K)*F.ds(K) + M*F.dW(K) for K in (X, Y, Z)]
    for lab, nv in (('z', (0, 0, 1)), ('[110]', (1/np.sqrt(2), 1/np.sqrt(2), 0)), ('[111]', (1/np.sqrt(3),)*3)):
        u = nv[0]*p[0] + nv[1]*p[1] + nv[2]*p[2]
        # even-in-each-k_j quadrature is valid for u^4 only after symmetrizing signs: average over sign flips of p_x, p_y
        val = 0.0
        for sx in (1, -1):
            for sy in (1, -1):
                us = nv[0]*sx*p[0] + nv[1]*sy*p[1] + nv[2]*p[2]
                val += float((WW*us**4/E**3).sum())/4
        print('m=%.2f n=%-6s -(w/12)<u^4/E^3> = %+.7e' % (m, lab, (2/12)*val))
