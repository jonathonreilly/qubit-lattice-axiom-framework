# GUIDE only. SU(2) Wilson twist ratio r = Z_tw/Z on L^4 by thermodynamic integration in the sheet coupling s (Lemma T4).
# -log r = beta*|S| * int_{-1}^{1} u(s) ds,  u(s) = mean of (1/2) tr U_p over the sheet at sheet coupling s*beta.
import sys, time, numpy as np
L = int(sys.argv[1]); beta = float(sys.argv[2]); nq = int(sys.argv[3]); ntherm = int(sys.argv[4]); nmeas = int(sys.argv[5]); seed = int(sys.argv[6])
rng = np.random.default_rng(seed)
V = L**4
coords = np.array(np.unravel_index(np.arange(V), (L,)*4)).T          # (V,4)
def idx(c): return np.ravel_multi_index(tuple(c.T % L), (L,)*4)
fwd = np.stack([idx(coords + np.eye(4, dtype=int)[m]) for m in range(4)])   # fwd[m][x]
bwd = np.stack([idx(coords - np.eye(4, dtype=int)[m]) for m in range(4)])
parity = coords.sum(1) % 2
def qmul(a, b):
    a0,a1,a2,a3 = a[...,0],a[...,1],a[...,2],a[...,3]; b0,b1,b2,b3 = b[...,0],b[...,1],b[...,2],b[...,3]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0], -1)
def qconj(a):
    c = a.copy(); c[...,1:] *= -1; return c
sheet = (coords[:,0] == 0) & (coords[:,1] == 0)        # base points of the (0,1) plaquettes on the sheet
nS = int(sheet.sum())
def coupling(s):
    c = np.full((4,4,V), beta)
    c[0,1,sheet] = s*beta; c[1,0,sheet] = s*beta
    return c
def staple_sum(U, c, m, sites):
    W = np.zeros((len(sites),4))
    xm = fwd[m][sites]
    for n in range(4):
        if n == m: continue
        xn = fwd[n][sites]
        up = qmul(qmul(U[n][xm], qconj(U[m][xn])), qconj(U[n][sites]))
        W += c[m,n,sites][:,None]*up
        xd = bwd[n][sites]; xmd = bwd[n][xm]
        dn = qmul(qmul(qconj(U[n][xmd]), qconj(U[m][xd])), U[n][xd])
        W += c[m,n,xd][:,None]*dn
    return W
def heatbath(U, c):
    for m in range(4):
        for p in (0,1):
            sites = np.nonzero(parity == p)[0]
            W = staple_sum(U, c, m, sites)
            k = np.sqrt((W*W).sum(1)); k = np.maximum(k, 1e-12)
            Vb = W / k[:,None]
            x0 = np.empty(len(sites)); todo = np.arange(len(sites))
            while len(todo):
                kk = k[todo]; u = rng.random(len(todo))
                t = 1.0 + np.log(np.exp(-2*kk) + u*(1.0-np.exp(-2*kk)))/kk
                acc = rng.random(len(todo))**2 <= 1.0 - t*t
                x0[todo[acc]] = t[acc]; todo = todo[~acc]
            r = np.sqrt(np.maximum(0.0, 1.0 - x0*x0))
            ct = 2*rng.random(len(sites)) - 1; st = np.sqrt(1-ct*ct); ph = 2*np.pi*rng.random(len(sites))
            X = np.stack([x0, r*st*np.cos(ph), r*st*np.sin(ph), r*ct], -1)
            U[m][sites] = qmul(X, qconj(Vb))
def sheet_plaq(U):
    x = np.nonzero(sheet)[0]
    P = qmul(qmul(U[0][x], U[1][fwd[0][x]]), qmul(qconj(U[0][fwd[1][x]]), qconj(U[1][x])))
    return P[:,0].mean()
def all_plaq(U):
    tot = 0.0; cnt = 0
    for m in range(4):
        for n in range(m+1,4):
            P = qmul(qmul(U[m], U[n][fwd[m]]), qmul(qconj(U[m][fwd[n]]), qconj(U[n])))
            tot += P[:,0].sum(); cnt += V
    return tot/cnt
nodes, weights = np.polynomial.legendre.leggauss(nq)
t0 = time.time(); res = []
U = np.zeros((4,V,4)); U[...,0] = 1.0
for s in nodes[::-1]:                     # start at s near +1, walk down to -1, reusing the configuration
    c = coupling(s)
    for _ in range(ntherm): heatbath(U, c)
    us = np.empty(nmeas); pl = 0.0
    for i in range(nmeas):
        heatbath(U, c); us[i] = sheet_plaq(U)
        if i % 50 == 0: pl += all_plaq(U)
    nb = 20; b = us[:nmeas//nb*nb].reshape(nb,-1).mean(1)
    res.append((s, us.mean(), b.std(ddof=1)/np.sqrt(nb), pl/len(range(0,nmeas,50))))
    print("s=%+.5f u=%+.5f +- %.5f  plaq=%.4f  t=%.0fs" % (res[-1] + (time.time()-t0,)), flush=True)
res = res[::-1]
u = np.array([x[1] for x in res]); e = np.array([x[2] for x in res])
I = (weights*u).sum(); dI = np.sqrt(((weights*e)**2).sum())
Fv = beta*nS*I; dFv = beta*nS*dI
print("L=%d beta=%.3f |S|=%d  F_v=%.4f +- %.4f   r=exp(-F_v)=%.4f  (range %.4f .. %.4f)" % (L, beta, nS, Fv, dFv, np.exp(-Fv), np.exp(-Fv-dFv), np.exp(-Fv+dFv)))
