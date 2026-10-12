"""R16-9 explicit laws in S from slope plans: sigma' = 1 on [0,b], then segments (value in {1,-1,0}, length), then flat to pi.
C^inf steps of width wt (convex blends => |sigma'| <= 1 exactly). zigzag(level_top, amp, length) = alternating -1/+1 of length amp."""
import numpy as np, sys; sys.path.insert(0, '.')
from zz import *
NF = 1 << 16
def build(b, segs, wt, name='R', nf=NF):
    vals = [1.0]; bks = [b]; k = b
    for (v, Lg) in segs:
        vals.append(float(v)); k += Lg; bks.append(k)
    vals.append(0.0)
    if k > np.pi - wt: return None
    return ZLaw(vals, bks, wt, name, nf=nf)
def descend(dl): return [(-1.0, dl)]
def climb(dl): return [(1.0, dl)]
def zig(amp, length, start=-1):
    n = max(1, int(round(length/amp))); s = start; out = []
    for i in range(n): out.append((float(s), amp)); s = -s
    return out
def flat(Lg): return [(0.0, Lg)]
def ev(L, m, nn=1 << 13, nu=800):
    g, f = L.samples(nn); X = xi_all(g, f, m, nu=nu); mu = mu_E(g, f, m, nu=nu)
    return X, mu
def report(L, m, nn=1 << 15, nu=2000):
    X, mu = ev(L, m, nn, nu); b = L.b
    return ('%s m=%g: M Eg %+.3e T2g %+.3e | U Eg %+.3e T2g %+.3e | mu_E %+.3e | vmax %.6f max|sp| %.9f min edge g %.4f'
            % (L.name, m, X['M,Eg'], X['M,T2g'], X['U,Eg'], X['U,T2g'], mu, L.vmax(m), np.abs(L.sp).max(), (L.sig[L.k >= L.bks[0]]**2).min()))
