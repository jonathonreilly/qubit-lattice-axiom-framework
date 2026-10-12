#!/usr/bin/env python3
"""T2g: family C' = perfect action whose blocking cell is a FIXED PHYSICAL hypercube (does not follow the lattice).

  S_G(q) = sum_l F(P k_l) + s^2,  F(p) = Pi(p)/p^2,  k_l = q + 2 pi l,  P = A^{-T} = diag(1, g^{-1/2}) (physical momentum).
Label-cell blocking (T2c) has Pi(k_l) instead of Pi(P k_l).  At g = 1 the two coincide (hypercubic; same RP data).
Time-RP for every g: the physical blocks are still unit time slabs (link-RP EXACT, as in T2c).
EXACT: <S_G>_BZ = int_{R^4} F(p) d^4p/(2pi)^4 (unfold the image sum, unit Jacobian) is shape-independent,
  so the sigma^-2 term of T2c, -<S''>/(2 s^2), vanishes identically. Prediction: kappa ~ s^-4 (image cross terms).
Evaluation: Schwinger t-integral; 1D tables U_{j,a}(q,t) = sum_l phi_t^(j)(k) k^a, phi_t(k) = sinc^2(k/2) e^{-t k^2}.
"""
import numpy as np
from t2_core import midgrid, fit_power
from T2c_perfect_action import B_tables

SQ2 = np.sqrt(2.0)


def Bfull(q, t):
    """B_j = sum_l k^j e^{-t k^2} for j = -4..2."""
    B = B_tables(q, t)
    lmax = 2000 if t < 0.05 else int(np.ceil(np.sqrt(45 / t) / (2 * np.pi))) + 2
    l = np.arange(-lmax, lmax + 1)[:, None]
    k = q[None, :] + 2 * np.pi * l
    e = np.exp(-t * k * k)
    B[-3] = (k ** -3.0 * e).sum(0)
    B[-4] = (k ** -4.0 * e).sum(0)
    return B


def U_tables(q, t):
    """U[(j, a)] = sum_l phi^(j)(k) k^a, j = 0,1,2 ; a = 0,1,2."""
    B = Bfull(q, t)
    sg, cs, s2 = np.sin(q), np.cos(q), np.sin(q / 2) ** 2
    # g = 4 s2 k^-2 ; g' = 2 sg k^-2 - 8 s2 k^-3 ; g'' = 2 cs k^-2 - 8 sg k^-3 + 24 s2 k^-4
    # phi = g E ; phi' = (g' - 2 t k g) E ; phi'' = (g'' - 4 t k g' - 2 t g + 4 t^2 k^2 g) E
    terms = {
        0: [(4 * s2, -2)],
        1: [(2 * sg, -2), (-8 * s2, -3), (-8 * t * s2, -1)],
        2: [(2 * cs, -2), (-8 * sg, -3), (24 * s2, -4),
            (-8 * t * sg, -1), (32 * t * s2, -2),
            (-8 * t * s2, -2), (16 * t * t * s2, 0)],
    }
    U = {}
    for j, lst in terms.items():
        for a in range(3):
            U[(j, a)] = sum(c * B[p + a] for c, p in lst)
    return U


def arrays(L, smin=-18.0, ds=0.04):
    q = midgrid(L)
    smax = np.log(45 * L * L / (4 * np.pi ** 2)) + 1.0
    sg = np.arange(smin, smax + ds / 2, ds)
    shp = (L,) * 4
    S0 = np.zeros(shp)
    d1 = {"E_g": np.zeros(shp), "T_2g": np.zeros(shp)}
    d2 = {"E_g": np.zeros(shp), "T_2g": np.zeros(shp)}
    for i, s in enumerate(sg):
        t = np.exp(s)
        w = ds * t * (0.5 if i in (0, len(sg) - 1) else 1.0)
        U = U_tables(q, t)
        o = np.multiply.outer
        A03 = o(U[(0, 0)], U[(0, 0)])
        def put(arr, plane, c):
            arr += c * A03[:, None, None, :] * plane[None, :, :, None]
        put(S0, o(U[(0, 0)], U[(0, 0)]), w)
        put(d1["E_g"], (-o(U[(1, 1)], U[(0, 0)]) + o(U[(0, 0)], U[(1, 1)])) / (2 * SQ2), w)
        put(d1["T_2g"], -(o(U[(1, 0)], U[(0, 1)]) + o(U[(0, 1)], U[(1, 0)])) / (2 * SQ2), w)
        common = o(U[(1, 1)], U[(0, 0)]) + o(U[(0, 0)], U[(1, 1)])
        put(d2["E_g"], (o(U[(2, 2)], U[(0, 0)]) - 2 * o(U[(1, 1)], U[(1, 1)]) + o(U[(0, 0)], U[(2, 2)]) + common) / 8, w)
        put(d2["T_2g"], (o(U[(2, 0)], U[(0, 2)]) + 2 * o(U[(1, 1)], U[(1, 1)]) + o(U[(0, 2)], U[(2, 0)]) + common) / 8, w)
    return S0, d1, d2


def brute_S(q, X, eps, physical=True, lr=10, l0r=40):
    from scipy.linalg import expm
    P = np.eye(4); P[1:, 1:] = expm(-eps * X / 2)
    r = np.arange(-lr, lr + 1)
    l = np.array(np.meshgrid(np.arange(-l0r, l0r + 1), r, r, r, indexing="ij")).reshape(4, -1).T
    k = q[None, :] + 2 * np.pi * l
    p = k @ P.T
    Pi = np.prod(np.sinc((p if physical else k) / (2 * np.pi)) ** 2, axis=1)
    return (Pi / (p ** 2).sum(1)).sum()


if __name__ == "__main__":
    from t2_core import CHANNELS
    print("== T2g: perfect action, blocking cell = fixed physical hypercube; m = 0 ==")
    # validation of S', S'' at one grid point against finite differences of a truncated brute image sum
    L = 16
    S0, d1, d2 = arrays(L)
    q = midgrid(L); i = (3, 9, 5, 12); qq = np.array([q[j] for j in i])
    for ch, X in CHANNELS.items():
        h = 1e-3
        b = [brute_S(qq, X, t * h) for t in (-1, 0, 1)]
        print(f" check {ch} at {i}: S0 {S0[i]:.6f} brute {b[1]:.6f} | S' {d1[ch][i]:+.6e} fd {(b[2]-b[0])/(2*h):+.6e} | S'' {d2[ch][i]:+.6e} fd {(b[2]-2*b[1]+b[0])/h**2:+.6e}")
    for L in (24, 32, 48):
        S0, d1, d2 = arrays(L)
        print(f"L={L}: <S''> E/T = {np.mean(d2['E_g']):+.2e} {np.mean(d2['T_2g']):+.2e}  (EXACT value 0; grid error)")
        print("   s^2     sigma_N   kappa_E        kappa_T        kappa*s^4 (E, T)")
        rows = []
        for s2 in (1 / 3, 0.5, 1.0, 2.0, 4.0, 9.0, 16.0, 25.0, 64.0):
            S = S0 + s2
            k = {ch: -0.5 * np.mean(d2[ch] / S - (d1[ch] / S) ** 2) for ch in d1}
            sN = np.sqrt(4 * s2 - 1 / 3)
            print(f"  {s2:6.3f}  {sN:6.3f}   {k['E_g']:+.4e}  {k['T_2g']:+.4e}   {k['E_g']*s2*s2:+.4e} {k['T_2g']*s2*s2:+.4e}")
            rows.append((sN, k["E_g"], k["T_2g"]))
        rows = np.array(rows); sel = rows[:, 0] >= 3
        for j, name in ((1, "E_g"), (2, "T_2g")):
            p, c = fit_power(rows[sel, 0], rows[sel, j])
            print(f"  fit sigma_N >= 3, {name}: |kappa| ~ {c:.4f} sigma_N^-{p:.3f}")
