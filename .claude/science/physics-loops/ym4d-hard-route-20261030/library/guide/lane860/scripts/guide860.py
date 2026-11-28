#!/usr/bin/env python3
"""GUIDE run for FINISH row 860 (decides nothing; no proof step rests on it).
4D SU(2) Wilson heat bath, L^4 periodic, untwisted.
Measures the one-edge one-slice spin law rho_j = d_j r_j(beta) z(beta) E[chi_j(U_p) e^{-beta x_p}]
with the one-link-integrated estimator
  E[chi_j(U Sig) e^{-beta x(U Sig)} | rest] = z(b')r_j(b') chi_j(c) / z(b),  b = beta|A|, b' = beta|A - Sig|,
  c = (A - Sig).Sig/|A - Sig|,   z(b) r_j(b) = (2/b) I_{2j+1}(b).
Usage: guide860.py beta L ntherm nmeas nskip seed
"""
import sys, time
import numpy as np
from scipy.special import iv

beta = float(sys.argv[1]); L = int(sys.argv[2]); ntherm = int(sys.argv[3])
nmeas = int(sys.argv[4]); nskip = int(sys.argv[5]); seed = int(sys.argv[6])
rng = np.random.default_rng(seed)
D = 4
JMAX2 = 8  # twice the top spin: j = 0, 1/2, ..., 4

def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([a0*b0 - a1*b1 - a2*b2 - a3*b3,
                     a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1,
                     a0*b3 + a1*b2 - a2*b1 + a3*b0], axis=-1)

def qconj(a):
    c = a.copy(); c[..., 1:] *= -1; return c

def sh(a, nu, s):  # field at x + s*nu
    return np.roll(a, -s, axis=nu)

U = np.zeros((D, L, L, L, L, 4)); U[..., 0] = 1.0  # cold start
idx = np.indices((L, L, L, L)).sum(axis=0) % 2

def staples(mu):
    out = []
    for nu in range(D):
        if nu == mu: continue
        f = qmul(qmul(sh(U[nu], mu, 1), qconj(sh(U[mu], nu, 1))), qconj(U[nu]))
        Unu_m = sh(U[nu], nu, -1)
        b = qmul(qmul(qconj(sh(Unu_m, mu, 1)), qconj(sh(U[mu], nu, -1))), Unu_m)
        out.append(f); out.append(b)
    return out

def heatbath(mu, par):
    A = sum(staples(mu))
    mask = (idx == par)
    Am = A[mask]
    k = np.sqrt((Am**2).sum(axis=-1))
    a = beta * k
    n = a.shape[0]
    x0 = np.empty(n); todo = np.arange(n)
    while todo.size:
        u = rng.random(todo.size)
        at = a[todo]
        cand = 1.0 + np.log(np.exp(-2*at) + u*(1 - np.exp(-2*at)))/at
        acc = rng.random(todo.size) < np.sqrt(np.clip(1 - cand**2, 0, 1))
        x0[todo[acc]] = cand[acc]
        todo = todo[~acc]
    v = rng.normal(size=(n, 3)); v /= np.sqrt((v**2).sum(axis=1))[:, None]
    r = np.sqrt(np.clip(1 - x0**2, 0, 1))
    X = np.concatenate([x0[:, None], r[:, None]*v], axis=1)
    V = Am / k[:, None]
    Um = U[mu]; Um[mask] = qmul(X, qconj(V))

def sweep():
    for mu in range(D):
        for par in (0, 1):
            heatbath(mu, par)

def cheb(c, nmax):  # U_n(c), n = 0..nmax ; chi_j = U_{2j}
    out = [np.ones_like(c), 2*c]
    for n in range(2, nmax+1):
        out.append(2*c*out[-1] - out[-2])
    return out

def measure():
    plaq = 0.0; npl = 0
    f = np.zeros(JMAX2+1); half = 0.0; direct = np.zeros(4); cnt = 0
    for mu in range(D):
        st = staples(mu)
        A = sum(st)
        kA = np.sqrt((A**2).sum(axis=-1)); b = beta*kA
        zb = 2*iv(1, b)/b
        for S in st:
            xp = (qmul(U[mu], S))[..., 0]
            plaq += xp.sum(); npl += xp.size
            Ap = A - S
            rp = np.sqrt((Ap**2).sum(axis=-1)); bp = beta*rp
            c = (Ap*S).sum(axis=-1)/rp
            ch = cheb(c, JMAX2)
            for n in range(JMAX2+1):
                f[n] += ((2/bp)*iv(n+1, bp)*ch[n]/zb).sum()
            A2 = A - 2*S
            b2 = beta*np.sqrt((A2**2).sum(axis=-1))
            half += ((2*iv(1, b2)/b2)/zb).sum()
            chd = cheb(xp, 3); w = np.exp(-beta*xp)
            for n in range(4):
                direct[n] += (chd[n]*w).sum()
            cnt += xp.size
    return plaq/npl, f/cnt, half/cnt, direct/cnt

t0 = time.time()
for i in range(ntherm): sweep()
P = []; F = []; Hh = []; Dd = []
for i in range(nmeas):
    for s in range(nskip): sweep()
    p, f, h, d = measure()
    P.append(p); F.append(f); Hh.append(h); Dd.append(d)
P = np.array(P); F = np.array(F); Hh = np.array(Hh); Dd = np.array(Dd)
def err(a):
    nb = 10; m = (len(a)//nb)*nb
    bl = a[:m].reshape(nb, -1, *a.shape[1:]).mean(axis=1)
    return bl.std(axis=0, ddof=1)/np.sqrt(nb)
z = 2*iv(1, beta)/beta
print(f"beta={beta} L={L} ntherm={ntherm} nmeas={nmeas} nskip={nskip} seed={seed} time={time.time()-t0:.0f}s")
print(f"<x_p> = {P.mean():.5f} +- {err(P):.5f}")
rho = np.zeros(JMAX2+1); rerr = np.zeros(JMAX2+1)
Fm = F.mean(axis=0); Fe = err(F)
for n in range(JMAX2+1):
    c = (n+1)*(2/beta)*iv(n+1, beta)   # d_j r_j z
    rho[n] = c*Fm[n]; rerr[n] = c*Fe[n]
print("j      rho_j (improved)      w_j (plaquette law)   env coeff e_j = rho_j/(rho_0 d_j^2 r_j)   r_j(beta)")
for n in range(JMAX2+1):
    rj = iv(n+1, beta)/iv(1, beta)
    wj = (2/beta)*(n+1)**2*iv(n+1, beta)*np.exp(-beta)
    ej = rho[n]/(rho[0]*(n+1)**2*rj)
    print(f"{n/2:<4} {rho[n]: .6e} +- {rerr[n]:.1e}   {wj:.6e}   {ej:.5f}   {rj:.6e}")
print(f"sum rho_j (j<=4) = {rho.sum():.6f}")
hm = Hh.mean(); he = err(Hh)
print(f"half-integer density (1 - E e^(-2 beta x))/2 = {(1-hm)/2:.5f} +- {he/2:.5f}")
print(f"sum of half-integer rho_j = {rho[1::2].sum():.5f}; spin>=2: {rho[4:].sum():.3e}; half-int >=3/2: {rho[3::2].sum():.3e}; half-int >=5/2: {rho[5::2].sum():.3e}")
dm = Dd.mean(axis=0)
print("direct estimator check (j=0,1/2,1,3/2):", " ".join(f"{(n+1)*(2/beta)*iv(n+1,beta)*dm[n]:.5f}" for n in range(4)))
