#!/usr/bin/env python3
"""Lane T check A: 1D Dirac-type step (two counter-moving content-set conveyors + mixing angle m).

U(k) = C(m) S(k),  S(k) = diag(e^{-ik}, e^{+ik}),  C(m) = cos m I - i sin m sigma_x.
Checks (numerical eigenphases vs closed forms):
  (1) cos w = cos m cos k
  (2) sin^2 w = sin^2 m + cos^2 m sin^2 k            (exact Lorentz-form shell in deformed variables)
  (3) v = dw/dk = cos m sin k / sin w ; 1 - v^2 = sin^2 m / sin^2 w
  (4) clock rate dw/dm|_k = sin m cos k / sin w = sign(cos k) sqrt(1 - v^2/cos^2 m)
  (5) low-k series of w^2 (sympy, exact)
  (6) single-track brickwork realization (full swaps on even bonds, partial swaps on odd bonds,
      single-excitation sector) reproduces the same spectrum.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np


def U_batch(k, m):
    k = np.atleast_1d(k)
    c, s = np.cos(m), np.sin(m)
    U = np.zeros((k.size, 2, 2), dtype=complex)
    eR, eL = np.exp(-1j * k), np.exp(1j * k)
    U[:, 0, 0] = c * eR
    U[:, 0, 1] = -1j * s * eL
    U[:, 1, 0] = -1j * s * eR
    U[:, 1, 1] = c * eL
    return U


def w_num(k, m):
    """positive quasi-energy w in [0, pi] from numerical eigenvalues (both eigenvalues are e^{-+iw})."""
    lam = np.linalg.eigvals(U_batch(k, m))
    a = np.abs(np.angle(lam))
    return a.max(axis=1), a.min(axis=1)


ks = np.linspace(-np.pi, np.pi, 4001)[1:]
print("== (1)-(4) closed forms vs numerical eigenphases, 4000 k-points per m")
for m in (0.0, 0.05, 0.3, 0.7, 1.2):
    wmax, wmin = w_num(ks, m)
    target = np.arccos(np.clip(np.cos(m) * np.cos(ks), -1, 1))
    e1 = max(np.max(np.abs(wmax - target)), np.max(np.abs(wmin - target)))
    e2 = np.max(np.abs(np.sin(wmax) ** 2 - (np.sin(m) ** 2 + np.cos(m) ** 2 * np.sin(ks) ** 2)))
    # group velocity by central differences of numerical eigenphases
    h = 1e-6
    wp, _ = w_num(ks + h, m)
    wm, _ = w_num(ks - h, m)
    vnum = (wp - wm) / (2 * h)
    ok = np.sin(wmax) > 1e-2
    vform = np.cos(m) * np.sin(ks) / np.sin(wmax)
    e3 = np.max(np.abs(vnum[ok] - vform[ok]))
    e3b = np.max(np.abs((1 - vform[ok] ** 2) - np.sin(m) ** 2 / np.sin(wmax[ok]) ** 2))
    line = "m=%.2f  |w-arccos(cos m cos k)|max=%.1e  |shell|max=%.1e  |v_num-v_formula|max=%.1e  |1-v^2 - sin^2m/sin^2w|max=%.1e" % (m, e1, e2, e3, e3b)
    if m > 0:
        hm = 1e-6
        wpm, _ = w_num(ks, m + hm)
        wmm, _ = w_num(ks, m - hm)
        rnum = (wpm - wmm) / (2 * hm)
        rform = np.sin(m) * np.cos(ks) / np.sin(wmax)
        rv = np.sign(np.cos(ks)) * np.sqrt(np.clip(1 - vform ** 2 / np.cos(m) ** 2, 0, None))
        e4 = np.max(np.abs(rnum[ok] - rform[ok]))
        e5 = np.max(np.abs(rform[ok] - rv[ok]))
        vmax = np.max(np.abs(vform[ok]))
        line += "\n        |dw/dm num - formula|max=%.1e  |formula - sign(cos k)sqrt(1-v^2/cos^2 m)|max=%.1e  max|v|=%.6f (cos m=%.6f)" % (e4, e5, vmax, np.cos(m))
    print(line)

print("\n== (5) exact low-k series of w^2 from cos w = cos m cos k (sympy)")
try:
    import sympy as sp
    k_, m_, e_ = sp.symbols('k m e', positive=True)
    # w^2 as a series: w = arccos(cos m cos k); expand with k->e k, m->e m to order e^8
    expr = sp.acos(sp.cos(e_ * m_) * sp.cos(e_ * k_)) ** 2
    ser = sp.series(expr, e_, 0, 8).removeO()
    ser = sp.expand(sp.simplify(ser))
    print("   w^2 =", sp.collect(ser, e_))
except Exception as exc:  # pragma: no cover
    print("   sympy unavailable or failed:", exc)
    # numeric fallback: residual scaling
    for scale in (1e-1, 5e-2, 2.5e-2):
        k = 0.7 * scale
        m = 0.4 * scale
        w = np.arccos(np.cos(m) * np.cos(k))
        r = w ** 2 - (k ** 2 + m ** 2 - k ** 2 * m ** 2 / 3)
        print("   scale %.3g residual/(k^2+m^2)^3 = %.4f" % (scale, r / (k ** 2 + m ** 2) ** 3))

print("\n== (6) single-track brickwork (qubit chain, single-excitation sector)")
for m in (0.3, 0.9):
    Ncell = 64
    L = 2 * Ncell
    th_e, th_o = np.pi / 2, np.pi / 2 - m

    def layer(theta, start):
        M = np.eye(L, dtype=complex)
        c, s = np.cos(theta), np.sin(theta)
        for j in range(start, L, 2):
            a, b = j, (j + 1) % L
            M[np.ix_([a, b], [a, b])] = np.array([[c, -1j * s], [-1j * s, c]])
        return M
    Ubw = layer(th_o, 1) @ layer(th_e, 0)
    lam = np.linalg.eigvals(Ubw)
    wb = np.sort(np.abs(np.angle(lam)))
    q = 2 * np.pi * np.arange(Ncell) / Ncell
    k = q + np.pi
    wt = np.arccos(np.clip(np.cos(m) * np.cos(k), -1, 1))
    wt = np.sort(np.concatenate([wt, wt]))
    print("   m=%.2f  brickwork |w| multiset vs arccos(cos m cos k), k=q+pi:  max diff = %.1e  (unitarity err %.1e)" % (
        m, np.max(np.abs(wb - wt)), np.max(np.abs(Ubw.conj().T @ Ubw - np.eye(L)))))
