"""Same LDA (zero-gradient) artifact as lda.py, evaluated exactly but fast:
for a uniform diagonal metric the improved symbol depends on k only through
D = sum_mu d(k_mu)/f_mu, so collapse each axis to its (L/2+1) distinct d values
with multiplicities and take the weighted outer product."""
import numpy as np, math

def axis(L):
    n = np.arange(L); d = 2*(1-np.cos(2*np.pi*n/L))
    v, inv = np.unique(np.round(d,13), return_inverse=True)
    w = np.bincount(inv).astype(float)
    return v, w

def delta(L, f, svals, cache={}):
    if L not in cache: cache[L] = axis(L)
    v, w = cache[L]
    D = (v[:,None,None,None]/f[0] + v[None,:,None,None]/f[1]
       + v[None,None,:,None]/f[2] + v[None,None,None,:]/f[3]).ravel()
    Wt = (w[:,None,None,None]*w[None,:,None,None]*w[None,None,:,None]*w[None,None,None,:]).ravel()
    cf = float(np.sum(f))/96.0
    X = D + cf*D*D
    sd = math.sqrt(np.prod(f))
    return np.array([(4*math.pi*s)**2*float(Wt@np.exp(-s*X))/L**4 - sd for s in svals])

def correction(L, eps, P, k, svals):
    from geom import gdiag
    svals = np.asarray(svals,float); tot = np.zeros(len(svals))
    d0 = delta(L, np.ones(4), svals); cc = {}
    for x0 in range(L):
        f = np.array([0.5*(gdiag(x0-0.5,eps,P,k)[0]+gdiag(x0+0.5,eps,P,k)[0])]
                     + [gdiag(x0,eps,P,k)[mu] for mu in (1,2,3)])
        key = tuple(np.round(f,12))
        if key not in cc: cc[key] = delta(L, f, svals)
        tot += cc[key] - d0
    return tot*L**3
