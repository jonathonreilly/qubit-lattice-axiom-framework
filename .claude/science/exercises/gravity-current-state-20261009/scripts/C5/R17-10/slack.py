"""R17-10: how far is the node-placed relaxation from an outward-rounded superset?
For a stored relaxation point (bin totals at nodes, bins [h_j - DL/2, h_j + DL/2]), bound face1 over every placement of each
bin's mass inside its bin: every positive-coefficient term uses the per-bin max of its kernel, every negative one the min
(sampled on 41 points per bin: an ESTIMATE of the outward enclosure, not itself rigorous).  Also checks t-quadrature (NU 700 vs 2800).
Usage: python3 slack.py file.npy m smin b [L]"""
import numpy as np, sys
from math import gamma
fn = sys.argv[1]; m = float(sys.argv[2]); smin = float(sys.argv[3]); b = float(sys.argv[4]); L = int(sys.argv[5]) if len(sys.argv) > 5 else 50
x = np.load(fn); lev = np.linspace(smin, np.pi, L); DL = lev[1]-lev[0]
M, P, Q, R = x[:L], x[L:2*L], x[2*L:3*L], x[3*L:]
def rows(NU, mode):
    umax = np.log(80.0/min(m*m, 1.0)) + 2; u = np.linspace(-16.0, umax, NU); t = np.exp(u); du = u[1]-u[0]
    w7 = t*du*t**2.5*np.exp(-t*m*m)/gamma(3.5); w5 = t*du*t**1.5*np.exp(-t*m*m)/gamma(2.5)
    xg, wg = np.polynomial.legendre.leggauss(400); kb = 0.5*b*(xg+1); wb = 0.5*b*wg; Eb = np.exp(-np.outer(t, kb*kb))
    Bx = {p: Eb@(wb*kb**p)/np.pi for p in (0, 2, 4, 6)}
    off = np.linspace(-0.5, 0.5, 41)*DL
    H = np.clip(lev[:, None] + off[None, :], 0, None)          # samples inside each bin
    def mom(p, wts, ext):
        K = np.exp(-t[:, None, None]*H[None]**2)*H[None]**p   # (NU, L, 41)
        if ext == 'node': Kb = np.exp(-np.outer(t, lev**2))*lev**p
        elif ext == 'max': Kb = K.max(2)
        else: Kb = K.min(2)
        return Bx[p] + Kb@wts/np.pi
    def term(name, ext):
        E0, F2, F4, F6 = mom(0, M, ext), mom(2, P, ext), mom(4, Q, ext), mom(6, R, ext)
        return dict(a6=w7@(F6*E0*E0), a42=w7@(F4*F2*E0), a222=w7@F2**3, b4=w5@(F4*E0*E0), b22=w5@(F2*F2*E0))[name]
    cf = dict(a6=-1/128, a42=45/128, a222=-5/16, b4=-3/64, b22=1/64)
    if mode == 'node': return sum(c*term(k, 'node') for k, c in cf.items())
    return sum(c*term(k, 'max' if c > 0 else 'min') for k, c in cf.items())
f700 = rows(700, 'node'); f2800 = rows(2800, 'node'); fup = rows(700, 'up')
print('%s L=%d: face1(node, NU=700) %+.6e  (NU=2800) %+.6e  quad diff %.1e | outward-placement upper bound %+.6e  slack %+.3e  (margin %.3e)'
      % (fn, L, f700, f2800, abs(f700-f2800), fup, fup-f700, -f700))
