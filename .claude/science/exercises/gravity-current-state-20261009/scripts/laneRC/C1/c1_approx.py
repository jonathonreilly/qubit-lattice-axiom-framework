"""C1 readout Q1: best approximation of the SLAC band by depth-n network bands.

Even trig polynomial of degree n in k  <->  algebraic polynomial of degree n in x = cos k.
Target for E^2 (units c = 1, 1D factor of the separable d-dim problem):  F(x) = (arccos x)^2 = k^2 on [-pi, pi].
Classes:
 (i)   whole zone, best uniform:                      min_p max_{|k|<=pi} |p - k^2|
 (ii)  window |k|<=kap, unconstrained:                 min_p max_{|k|<=kap} |p - k^2|
 (iii) window |k|<=kap, with 0 <= p <= Pmax on zone:   (a bounded, stable network band)
 (iv)  closure residual delta_n = sup_{|k|<=kap'} |E dE/dk - k| = sup |p'(k)/2 - k|
 (v)   1-band direct approximation of E = sqrt(m^2+k^2) on the window (rate limited by k = i m)
LP (HiGHS) on dense grids; Chebyshev bases for conditioning.
"""
import numpy as np
from numpy.polynomial import chebyshev as C
from scipy.optimize import linprog

def lp_best(xg, fg, n, dom, xc=None, lo=None, hi=None):
    """min t s.t. |p(xg)-fg|<=t, and lo<=p(xc)<=hi; p = sum c_j T_j(map(x)) on dom=[a,b]."""
    a, b = dom
    u = (2*xg - (a+b))/(b-a)
    V = C.chebvander(u, n)
    m = len(xg)
    A = [np.hstack([V, -np.ones((m,1))]), np.hstack([-V, -np.ones((m,1))])]
    bb = [fg, -fg]
    if xc is not None:
        uc = (2*xc - (a+b))/(b-a)
        Vc = C.chebvander(uc, n)
        A += [np.hstack([Vc, np.zeros((len(xc),1))]), np.hstack([-Vc, np.zeros((len(xc),1))])]
        bb += [hi*np.ones(len(xc)), -lo*np.ones(len(xc))]
    A = np.vstack(A); bb = np.concatenate(bb)
    cost = np.zeros(n+2); cost[-1] = 1
    res = linprog(cost, A_ub=A, b_ub=bb, bounds=[(None,None)]*(n+1)+[(0,None)], method='highs')
    return res.x[-1], res.x[:-1]

def peval(coef, x, dom):
    a, b = dom
    return C.chebval((2*x-(a+b))/(b-a), coef)

def pder_k(coef, k, dom):
    """d/dk p(cos k) = -sin k * p'(x)."""
    a, b = dom
    dc = C.chebder(coef) * 2/(b-a)
    return -np.sin(k) * C.chebval((2*np.cos(k)-(a+b))/(b-a), dc)

out = []
P = lambda *s: (print(*s), out.append(' '.join(str(t) for t in s)))

# (i) whole zone: grid in k uniform plus clustering near the face
kg = np.unique(np.concatenate([np.linspace(0, np.pi, 6001), np.pi - np.geomspace(1e-7, 0.3, 2000)]))
xg = np.cos(kg); fg = kg**2
P("(i) whole-zone best uniform approximation of k^2 (periodic, kink at face) by cos-poly degree n")
P("n  E_n  n*E_n  sup|p'/2-k| on zone  sup|p'/2-k| on |k|<=pi/2")
rows = []
for n in [4, 8, 16, 32, 64, 128, 192]:
    t, c = lp_best(xg, fg, n, (-1, 1))
    kk = np.linspace(0, np.pi, 20001)
    dres = np.abs(pder_k(c, kk, (-1,1))/2 - kk)
    rows.append((n, t))
    P(n, f"{t:.6e}", f"{n*t:.4f}", f"{dres.max():.4f}", f"{dres[kk<=np.pi/2].max():.4e}")
ns = np.array([r[0] for r in rows[2:]]); es = np.array([r[1] for r in rows[2:]])
sl, ic = np.polyfit(np.log(ns), np.log(es), 1)
P(f"fit E_n ~ A n^p over n>=16: p = {sl:.4f}, A = {np.exp(ic):.4f}")

# (ii) window, unconstrained, and (iii) bounded on the zone
def window_rates(kap, nlist, bounded, Pmax=None):
    a = np.cos(kap)
    kw = np.linspace(0, kap, 3001)
    xw = np.cos(kw); fw = kw**2
    if bounded:
        kc = np.linspace(0, np.pi, 4001); xc = np.cos(kc)
        dom = (-1, 1)
    else:
        xc = None; dom = (a, 1)
    res = []
    for n in nlist:
        if bounded:
            t, c = lp_best(xw, fw, n, dom, xc=xc, lo=0.0, hi=Pmax)
        else:
            t, c = lp_best(xw, fw, n, dom)
        # closure residual on a slightly smaller window and on the window
        k1 = np.linspace(0, kap, 4001)
        d1 = np.abs(pder_k(c, k1, dom)/2 - k1).max()
        k2 = np.linspace(0, 0.8*kap, 4001)
        d2 = np.abs(pder_k(c, k2, dom)/2 - k2).max()
        kz = np.linspace(0, np.pi, 8001)
        pz = peval(c, np.cos(kz), dom)
        res.append((n, t, d1, d2, pz.min(), pz.max(), np.abs(c).max()))
    return res

def fitrate(res, col, floor=3e-11):
    ns = np.array([r[0] for r in res]); es = np.array([r[col] for r in res])
    ok = es > floor
    if ok.sum() < 3: return np.nan
    sl, ic = np.polyfit(ns[ok], np.log(es[ok]), 1)
    return -sl

for kap in [np.pi/4, np.pi/2, 3*np.pi/4]:
    rho = np.arccosh((3+np.cos(kap))/(1-np.cos(kap)))
    P(f"\n(ii) window |k|<={kap/np.pi:.3f}pi, unconstrained; Bernstein-Walsh prediction rho = arccosh((3+cos)/(1-cos)) = {rho:.4f}")
    nl = list(range(2, 31, 2)) if kap > 1 else list(range(2, 17, 1))
    r = window_rates(kap, nl, False)
    P("n  E_n(window)  delta(window)  delta(0.8 window)  min p on zone  max p on zone  max|coef|")
    for row in r:
        P(row[0], *[f"{v:.3e}" for v in row[1:]])
    P(f"fitted rate -dlnE_n/dn = {fitrate(r,1):.4f};  delta rate = {fitrate(r,2):.4f}; delta(0.8) rate = {fitrate(r,3):.4f}")
    Pmax = 1.0*np.pi**2
    P(f"(iii) same window, with 0 <= p <= pi^2 on the whole zone (stable bounded band)")
    nl2 = list(range(4, 61, 4))
    r2 = window_rates(kap, nl2, True, Pmax)
    for row in r2:
        P(row[0], *[f"{v:.3e}" for v in row[1:]])
    P(f"fitted rate = {fitrate(r2,1):.4f};  delta rate = {fitrate(r2,2):.4f}; delta(0.8) rate = {fitrate(r2,3):.4f}")

# (v) one-band direct approximation of E = sqrt(m^2 + k^2) on window pi/2 (fermion-like single band)
P("\n(v) direct approximation of E = sqrt(m^2+k^2) (not E^2) on |k|<=pi/2, unconstrained")
kap = np.pi/2; a = np.cos(kap)
for mm in [0.1, 0.5, 1.0]:
    kw = np.linspace(0, kap, 3001); xw = np.cos(kw); fw = np.sqrt(mm**2 + kw**2)
    res = []
    for n in range(2, 31, 2):
        t, c = lp_best(xw, fw, n, (a, 1)); res.append((n, t))
    x0 = np.cosh(mm)  # k = i m  ->  x = cosh m
    u0 = (2*x0 - (a+1))/(1-a)
    rho_m = np.arccosh(u0)
    rho_f = np.arccosh((3+a)/(1-a))
    P(f"m={mm}: fitted rate {fitrate(res,1):.4f}; predicted min(branch-point {rho_m:.4f}, face {rho_f:.4f}) = {min(rho_m,rho_f):.4f}; E_30 = {res[-1][1]:.3e}")

open('c1_approx.out', 'w').write('\n'.join(out) + '\n')
