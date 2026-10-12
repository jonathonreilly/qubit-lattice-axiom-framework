"""C1 readout Q1, accurate version (c1_approx.py's LP has a ~1e-7 tolerance floor; its whole-zone part (i) is kept).
 (ii')  window |k|<=kap: Chebyshev interpolant in x=cos k on [cos kap, 1] (near-best within a log factor).
        Local rate ln(E_n/E_{n+4})/4 vs Bernstein-Walsh rho(kap) = arccosh((3+cos kap)/(1-cos kap)).
        Closure residual delta = sup|E dE/dk - k| = sup|p'(k)/2 - k| on window; size of p on the rest of the zone.
 (iii') window + stability/boundedness 0 <= p <= pi^2 on the whole zone: LP with iterative refinement (scaled corrections).
 (v')   1-band direct approximation of E = sqrt(m^2+k^2) on the window: rate vs branch point k = i m.
 (vi)   smooth-filtered Fourier series of k^2 (bounded, local, whole zone): sup error on zone (O(1/n) at the face),
        and closure residual on windows.
Units: c = 1, lattice spacing 1, per axis (the d-dim SLAC E^2 is separable).
"""
import numpy as np
from numpy.polynomial import chebyshev as C
from scipy.optimize import linprog
out = []
P = lambda *s: (print(*s), out.append(' '.join(str(t) for t in s)))

def cheb_interp(fun, n, a, b):
    j = np.arange(n+1); u = np.cos(np.pi*(j+0.5)/(n+1)); x = 0.5*(a+b) + 0.5*(b-a)*u
    return C.chebfit(u, fun(x), n)

def ev(c, x, a, b): return C.chebval((2*x-(a+b))/(b-a), c)
def dk(c, k, a, b):
    dc = C.chebder(c)*2/(b-a); return -np.sin(k)*C.chebval((2*np.cos(k)-(a+b))/(b-a), dc)

F = lambda x: np.arccos(np.clip(x, -1, 1))**2
P("(ii') window, Chebyshev interpolant of k^2 in x = cos k")
for kap in [np.pi/4, np.pi/2, 3*np.pi/4]:
    a = np.cos(kap); rho = np.arccosh((3+a)/(1-a))
    kw = np.linspace(0, kap, 6001); k08 = np.linspace(0, 0.8*kap, 6001); kz = np.linspace(0, np.pi, 6001)
    P(f" kap={kap/np.pi:.2f}pi  rho_BW={rho:.4f}")
    P("  n   E_n(win)    delta(win)  delta(0.8win)  max|p| on zone")
    res = []
    nl = range(4, 41, 4) if kap > 2 else (range(2, 23, 2) if kap > 1 else range(1, 13, 1))
    for n in nl:
        c = cheb_interp(F, n, a, 1)
        e = np.abs(ev(c, np.cos(kw), a, 1) - kw**2).max()
        d1 = np.abs(dk(c, kw, a, 1)/2 - kw).max(); d2 = np.abs(dk(c, k08, a, 1)/2 - k08).max()
        pz = np.abs(ev(c, np.cos(kz), a, 1)).max()
        res.append((n, e, d1, d2, pz)); P(f"  {n:2d}  {e:.3e}  {d1:.3e}  {d2:.3e}  {pz:.3e}")
    ns = np.array([r[0] for r in res]); E = np.array([r[1] for r in res]); D = np.array([r[2] for r in res]); Z = np.array([r[4] for r in res])
    ok = E > 1e-13
    i1, i2 = np.where(ok)[0][-3], np.where(ok)[0][-1]
    P(f"  local rate of E_n (last points above 1e-13, n={ns[i1]}..{ns[i2]}): {np.log(E[i1]/E[i2])/(ns[i2]-ns[i1]):.4f};  "
      f"fit E_n ~ A n^-1.5 e^(-rho n): rho_fit = {-np.polyfit(ns[ok], np.log(E[ok]*ns[ok]**1.5), 1)[0]:.4f}")
    okd = D > 1e-12
    P(f"  closure residual delta(win) fit ~ e^(-r n) n^0.5... r_fit (with n^-0.5 prefactor) = {-np.polyfit(ns[okd], np.log(D[okd]*ns[okd]**0.5), 1)[0]:.4f}")
    P(f"  growth of max|p| on zone per degree: {np.polyfit(ns[-4:], np.log(Z[-4:]), 1)[0]:.4f}  (unconstrained approximant is wild off-window)")

# (iii') bounded/stable band, LP with refinement
def lp_ref(kap, n, Pmax=np.pi**2, rounds=4):
    kw = np.linspace(0, kap, 2001); xw = np.cos(kw); fw = kw**2
    kc = np.linspace(0, np.pi, 3001); xc = np.cos(kc)
    Vw = C.chebvander(xw, n); Vc = C.chebvander(xc, n)
    c = np.zeros(n+1); hist = []
    for r in range(rounds):
        res_w = fw - Vw@c; s = max(np.abs(res_w).max(), 1e-15)
        pc = Vc@c
        m = len(xw)
        A = np.vstack([np.hstack([Vw, -np.ones((m,1))]), np.hstack([-Vw, -np.ones((m,1))]),
                       np.hstack([Vc, np.zeros((len(xc),1))]), np.hstack([-Vc, np.zeros((len(xc),1))])])
        bb = np.concatenate([res_w/s, -res_w/s, (Pmax - pc)/s, (pc - 0.0)/s])
        cost = np.zeros(n+2); cost[-1] = 1
        sol = linprog(cost, A_ub=A, b_ub=bb, bounds=[(None,None)]*(n+1)+[(0,None)], method='highs')
        if sol.status != 0: break
        c = c + s*sol.x[:-1]
        hist.append(np.abs(fw - Vw@c).max())
    pz = Vc@c
    d = np.abs(-np.sin(kw)*C.chebval(xw, C.chebder(c))/2 - kw).max()
    return hist[-1], d, pz.min(), pz.max()

P("\n(iii') window + 0 <= p <= pi^2 on whole zone (stable, bounded band); LP with refinement")
for kap in [np.pi/2, 3*np.pi/4]:
    P(f" kap={kap/np.pi:.2f}pi:  n  E_n(win)  delta(win)  min p  max p")
    res = []
    for n in [4, 8, 12, 16, 20, 24, 32, 40]:
        e, d, lo, hi = lp_ref(kap, n)
        res.append((n, e, d)); P(f"   {n:2d}  {e:.3e}  {d:.3e}  {lo:.2e}  {hi:.3f}")
    ns = np.array([r[0] for r in res]); E = np.array([r[1] for r in res]); ok = E > 1e-12
    P(f"   fitted rate (E_n ~ e^(-r n)) over E>1e-12: r = {-np.polyfit(ns[ok], np.log(E[ok]), 1)[0]:.4f}")

# (v') E directly
P("\n(v') direct approximation of E = sqrt(m^2+k^2) on |k|<=pi/2 (1-band), Chebyshev interpolant; asymptotic local rate")
kap = np.pi/2; a = np.cos(kap); kw = np.linspace(0, kap, 6001)
for mm in [0.1, 0.3, 1.0]:
    G = lambda x, mm=mm: np.sqrt(mm**2 + np.arccos(np.clip(x, -1, 1))**2)
    Es = []
    for n in [20, 30, 40, 50, 60, 80]:
        c = cheb_interp(G, n, a, 1); Es.append((n, np.abs(ev(c, np.cos(kw), a, 1) - np.sqrt(mm**2+kw**2)).max()))
    rho_m = np.arccosh((2*np.cosh(mm) - (a+1))/(1-a)); rho_f = np.arccosh((3+a)/(1-a))
    ok = [e for e in Es if e[1] > 1e-13]
    r = np.log(ok[-2][1]/ok[-1][1])/(ok[-1][0]-ok[-2][0]) if len(ok) > 1 else np.nan
    P(f"  m={mm}: E_n = " + ', '.join(f"{n}:{e:.2e}" for n, e in Es) + f";  local rate {r:.4f};  predicted min(branch {rho_m:.4f}, face {rho_f:.4f})")

# (vi) filtered Fourier series: k^2 = pi^2/3 + 4 sum (-1)^j cos(jk)/j^2
P("\n(vi) smooth-filtered Fourier series of k^2, sigma(eta)=exp(-36 eta^8), degree n (bounded, local, whole zone)")
kz = np.linspace(0, np.pi, 40001)
P("  n    sup err zone   n*err    err |k|<=pi/2   delta zone   delta |k|<=pi/2   delta |k|<=3pi/4   min p")
for n in [8, 16, 32, 64, 128, 256, 512]:
    j = np.arange(1, n+1); sig = np.exp(-36*(j/n)**8)
    coef = 4*(-1.0)**j/j**2*sig
    p = np.pi**2/3 + np.cos(np.outer(kz, j))@coef
    dp = -np.sin(np.outer(kz, j))@(coef*j)
    e = np.abs(p - kz**2); dd = np.abs(dp/2 - kz)
    P(f"  {n:3d}  {e.max():.3e}  {n*e.max():.3f}  {e[kz<=np.pi/2].max():.3e}  {dd.max():.3f}  {dd[kz<=np.pi/2].max():.3e}  {dd[kz<=3*np.pi/4].max():.3e}  {p.min():.2e}")
open('c1_approx2.out', 'w').write('\n'.join(out) + '\n')
