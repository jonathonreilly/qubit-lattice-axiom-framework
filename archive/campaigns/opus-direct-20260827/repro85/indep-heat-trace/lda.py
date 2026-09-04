"""Local-density (zero-gradient) lattice-artifact subtraction.
For a UNIFORM diagonal metric f_mu the Kuhn operator symbol is exactly
D_f(k) = sum_mu 2(1-cos k_mu)/f_mu  (verified numerically), and the improved
symbol is D_f + c_f D_f^2 with c_f = sum_mu f_mu / 96.  Its heat trace per site
differs from the continuum sqrt(det f)/(4 pi s)^2 by a pure lattice artifact
delta(s;f) that involves NO curvature (a constant metric is flat).  Subtracting
sum_{x0}[delta(s;f(x0)) - delta(s;1)] therefore removes the zero-gradient part of
the discretisation error and cannot touch the O(s) Regge term."""
import numpy as np, math

def delta(L, f, svals):
    n = np.arange(L); c1 = 2*(1-np.cos(2*np.pi*n/L))
    D = (c1[:,None,None,None]/f[0] + c1[None,:,None,None]/f[1]
       + c1[None,None,:,None]/f[2] + c1[None,None,None,:]/f[3])
    cf = float(np.sum(f))/96.0
    X = D + cf*D*D
    out = []
    for s in svals:
        out.append((4*math.pi*s)**2*np.exp(-s*X).sum()/L**4 - math.sqrt(np.prod(f)))
    return np.array(out)

def correction(L, eps, P, k, svals):
    from geom import gdiag
    svals = np.asarray(svals,float)
    tot = np.zeros(len(svals))
    d0 = delta(L, np.ones(4), svals)
    cache = {}
    for x0 in range(L):
        f = np.array([0.5*(gdiag(x0-0.5,eps,P,k)[0]+gdiag(x0+0.5,eps,P,k)[0])]
                     + [gdiag(x0,eps,P,k)[mu] for mu in (1,2,3)])
        key = tuple(np.round(f,12))
        if key not in cache: cache[key] = delta(L, f, svals)
        tot += cache[key] - d0
    return tot*L**3
