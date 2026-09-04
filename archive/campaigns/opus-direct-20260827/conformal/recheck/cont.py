"""cont.py -- continuum references for g = diag(f_mu(t)), f_mu = 1 + eps P_mu cos(kk t),
t = x^0.  Christoffels and their derivative are analytic here:

  Gamma^0_{00} = f0'/(2 f0),  Gamma^0_{ii} = -fi'/(2 f0),  Gamma^i_{0i} = fi'/(2 fi)
  (i = 1,2,3; everything else zero).

Gives exact Vol = Int sqrt(g), S_cont = (1/2) Int R sqrt(g)  [the continuum value the
simplicial S_Regge must converge to], and Int a_2 with Gilkey's
a_2 = (1/360)(12 Box R + 5 R^2 - 2 Ric^2 + 2 Riem^2), E = 0; Box R integrates to zero.
"""
import numpy as np


def _f(t, eps, P, kk):
    P = np.asarray(P, dtype=float)
    c, s = np.cos(kk * t), np.sin(kk * t)
    f = 1.0 + eps * P * c
    fp = -eps * P * kk * s
    fpp = -eps * P * kk * kk * c
    return f, fp, fpp


def christoffel(f, fp):
    G = np.zeros((4, 4, 4))
    G[0][0, 0] = 0.5 * fp[0] / f[0]
    for i in range(1, 4):
        G[0][i, i] = -0.5 * fp[i] / f[0]
        G[i][0, i] = G[i][i, 0] = 0.5 * fp[i] / f[i]
    return G


def dchristoffel(f, fp, fpp):
    G = np.zeros((4, 4, 4))
    G[0][0, 0] = 0.5 * (fpp[0] * f[0] - fp[0] ** 2) / f[0] ** 2
    for i in range(1, 4):
        G[0][i, i] = -0.5 * (fpp[i] * f[0] - fp[i] * fp[0]) / f[0] ** 2
        G[i][0, i] = G[i][i, 0] = 0.5 * (fpp[i] * f[i] - fp[i] ** 2) / f[i] ** 2
    return G


def curv(t, eps, P, kk):
    f, fp, fpp = _f(t, eps, P, kk)
    G = christoffel(f, fp)
    dG = np.zeros((4, 4, 4, 4))
    dG[0] = dchristoffel(f, fp, fpp)                   # dG[c][a,b,cc] = d_c Gamma^a_{b cc}
    g = np.diag(f)
    gi = np.diag(1.0 / f)
    Rud = np.einsum('cabd->abcd', dG) - np.einsum('dabc->abcd', dG)
    Rud = Rud + np.einsum('ace,edb->abcd', G, G) - np.einsum('ade,ecb->abcd', G, G)
    Rdd = np.einsum('ae,ebcd->abcd', g, Rud)
    Ric = np.einsum('abad->bd', Rud)
    R = float(np.einsum('bd,bd->', gi, Ric))
    Ric2 = float(np.einsum('ab,cd,ac,bd->', Ric, Ric, gi, gi))
    Riem2 = float(np.einsum('abcd,efgh,ae,bf,cg,dh->', Rdd, Rdd, gi, gi, gi, gi))
    return R, Ric2, Riem2, float(np.sqrt(np.prod(f)))


def integrals(L, eps, P, kk, N=2048):
    """(Vol, S_cont, Int a_2) -- midpoint rule on a periodic integrand: spectrally exact."""
    ts = (np.arange(N) + 0.5) * L / N
    dt = L / N
    vol = IR = I2 = 0.0
    for t in ts:
        R, Ric2, Riem2, sg = curv(float(t), eps, P, kk)
        vol += sg
        IR += 0.5 * R * sg
        I2 += ((5 * R * R - 2 * Ric2 + 2 * Riem2) / 360.0) * sg
    return vol * dt * L ** 3, IR * dt * L ** 3, I2 * dt * L ** 3
