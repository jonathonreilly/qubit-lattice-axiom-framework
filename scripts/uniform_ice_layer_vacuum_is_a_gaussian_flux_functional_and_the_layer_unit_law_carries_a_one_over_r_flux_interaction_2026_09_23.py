#!/usr/bin/env python3
"""Uniform ice: the layer vacuum is a Gaussian flux functional, so the layer-unit law carries a 1/r flux interaction.

The landed layer-unit note (PR 8740) forms uniform ice on infinite prisms,
layer by layer, in the zero-flux sector. With T the symmetric layer transfer
and psi its top vector (eigenvalue lam_0), the exact law of a new layer v'
given the layer v below is

    P(v' | v) = T(v', v) psi(v') / (lam_0 psi(v)),

and the law of one layer is psi^2. T is local; all the non-locality sits in
psi. The open edge asks what this law becomes on an infinite cross-section.

A Gaussian divergence-free field gives the layer the weight
exp(-(1/2) sum_q |E_q|^2 / (A S_q)), with E_q the transform of the staggered
field E = (-1)^(x+y) (2v - 1) over the layer and S_q = sqrt(Q/(Q+4)) / K,
Q = sum_i 2 (1 - cos q_i) (open PR 8871). Then ln psi = const - (1/4) G(v)
with G(v) = sum_q |E_q|^2 / (A S_q). The kernel 1/S_q tends to 2K/|q| at
small q, whose transform in the plane falls as K/(pi r).

Checks:

A. The layer-unit law is exact: at 200 sampled layers v on each shape,
   sum_{v'} P(v' | v) = 1.
B. The layer vacuum is Gaussian. On 2 x 4, 2 x 6, 2 x 8 and 4 x 4, with S_q
   measured from psi^2, ln psi is linear in G with weighted R^2 >= 0.996, and
   the slope is within 8% of -1/4 (within 2% on the square).
C. With the predicted kernel, from K = 2 c(2) alone, R^2 >= 0.979 on every
   shape and 0.9989 on the square, and the slope is within 3% of -1/4.
D. The formation law. The Gaussian law P_G(v' | v), proportional to
   T(v', v) exp(-G(v')/4) with the predicted kernel, is within 1.3% of the
   exact law in total variation at every sampled layer, and within 0.25% on
   the square.
E. The kernel's tail. On a 2048 x 2048 layer, (U(r) - U(2r)) 2 pi r / K
   equals 1 within 1e-3 along an axis and within 5e-3 along the diagonal
   for r = 8, 16, 32, where U is the transform of K sqrt((Q+4)/Q): a 1/r
   flux interaction.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
import time

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

PASS = FAIL = 0
T0 = time.time()


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))


def row_tensor(a):
    n = 1 << a
    R = np.zeros((n, n, n, n))
    bits = lambda z: [(z >> i) & 1 for i in range(a)]
    for h in range(n):
        hb = bits(h)
        hdeg = [hb[(x - 1) % a] + hb[x] for x in range(a)]
        for w in range(n):
            wb = bits(w)
            for i in range(n):
                ib = bits(i)
                for o in range(n):
                    ob = bits(o)
                    need = [3 - hdeg[x] - ib[x] - ob[x] - wb[x] for x in range(a)]
                    if all(t in (0, 1) for t in need):
                        R[sum(t << x for x, t in enumerate(need)), o, w, i] += 1
    return R


def make_T(a, b):
    R = row_tensor(a)
    n = 1 << a

    def T(phi):
        A = phi.reshape((n,) * b)
        A = np.einsum("...,ij->...ij", A, np.eye(n))
        for r in range(b):
            A = np.tensordot(A, R, axes=([r, b], [2, 3]))
            A = np.moveaxis(A, [b, b + 1], [r, b])
        return np.einsum("...ii->...", A).reshape(-1)
    return T


def flux(a, b):
    idx = np.arange(1 << (a * b))
    S = np.zeros(len(idx), dtype=np.int64)
    for y in range(b):
        for x in range(a):
            S += (-1) ** (x + y) * (2 * ((idx >> ((b - 1 - y) * a + x)) & 1) - 1)
    return S


rng = np.random.default_rng(20260923)
res = {}
for (a, b) in ((2, 4), (2, 6), (2, 8), (4, 4)):
    N, A = 1 << (a * b), a * b
    S = flux(a, b)
    T = make_T(a, b)

    def top(s):
        # T maps the flux S of one layer to -S, so a flux sector is |S| = s
        m = (np.abs(S) == s).astype(float)
        op = LinearOperator((N, N), matvec=lambda u: m * T(m * u), dtype=float)
        w, V = eigsh(op, k=1, which="LA", tol=1e-12, maxiter=50000)
        return float(w[0]), np.abs(V[:, 0])
    lam0, psi_full = top(0)
    lam2, _ = top(2)
    K = 2 * (A / 4) * np.log(lam0 / lam2)
    sel = np.where(S == 0)[0]
    psi = psi_full[sel]
    P = psi ** 2 / (psi ** 2).sum()
    E = np.zeros((len(sel), a, b))
    for y in range(b):
        for x in range(a):
            E[:, x, y] = (-1) ** (x + y) * (2 * ((sel >> ((b - 1 - y) * a + x)) & 1) - 1)
    F2 = np.abs(np.fft.fft2(E, axes=(1, 2))) ** 2
    Qq = (2 - 2 * np.cos(2 * np.pi * np.arange(a) / a))[:, None] + (2 - 2 * np.cos(2 * np.pi * np.arange(b) / b))[None, :]
    nz = Qq > 0
    Smeas = (P[:, None, None] * F2).sum(0) / A
    inv_meas = np.zeros_like(Qq)
    inv_meas[nz] = 1 / Smeas[nz]
    inv_pred = np.zeros_like(Qq)
    inv_pred[nz] = K * np.sqrt((Qq[nz] + 4) / Qq[nz])
    y_ = np.log(psi)

    def fit(inv):
        G = (F2 * inv[None]).sum((1, 2)) / A
        X = np.stack([np.ones_like(G), G], 1)
        beta = np.linalg.solve(X.T @ (P[:, None] * X), X.T @ (P * y_))
        r = y_ - X @ beta
        r2 = 1 - (P * r ** 2).sum() / (P * (y_ - (P * y_).sum()) ** 2).sum()
        return float(beta[1]), float(r2), G
    sm, r2m, _ = fit(inv_meas)
    sp, r2p, Gp = fit(inv_pred)
    gw = np.exp(-(Gp - Gp.min()) / 4)
    sums, tvs = [], []
    for i in rng.choice(len(sel), size=min(200, len(sel)), replace=False, p=P):
        e = np.zeros(N)
        e[sel[i]] = 1.0
        col = T(e)[sel]
        pe = col * psi / (lam0 * psi[i])
        pg = col * gw
        pg /= pg.sum()
        sums.append(pe.sum())
        tvs.append(0.5 * np.abs(pe - pg).sum())
    res[(a, b)] = dict(sm=sm, r2m=r2m, sp=sp, r2p=r2p, tv=max(tvs), tvmean=float(np.mean(tvs)), sums=sums, K=K)

print("== A. The layer-unit law ==")
dev = max(abs(s - 1) for v in res.values() for s in v["sums"])
check("sum_{v'} P(v' | v) = 1 at 200 sampled layers on each shape", dev < 1e-9, f"largest deviation {dev:.1e}")
print()

print("== B. The layer vacuum is Gaussian (measured kernel) ==")
check("ln psi is linear in G: R^2 >= 0.996 on every shape, slope within 8% of -1/4, within 2% on the square",
      all(v["r2m"] >= 0.996 and abs(v["sm"] * 4 + 1) < 0.08 for v in res.values()) and abs(res[(4, 4)]["sm"] * 4 + 1) < 0.02,
      ", ".join(f"{a}x{b}: slope {v['sm']:.4f}, R2 {v['r2m']:.4f}" for (a, b), v in res.items()))
print()

print("== C. The predicted kernel, from K = 2 c(2) alone ==")
check("R^2 >= 0.979 on every shape and >= 0.998 on the square; slope within 3% of -1/4",
      all(v["r2p"] >= 0.979 and abs(v["sp"] * 4 + 1) < 0.03 for v in res.values()) and res[(4, 4)]["r2p"] >= 0.998,
      ", ".join(f"{a}x{b}: slope {v['sp']:.4f}, R2 {v['r2p']:.4f}" for (a, b), v in res.items()))
print()

print("== D. The formation law ==")
check("the Gaussian law is within 1.3% of the exact law in total variation at every sampled layer, within 0.25% on the square",
      all(v["tv"] < 0.013 for v in res.values()) and res[(4, 4)]["tv"] < 0.0025,
      ", ".join(f"{a}x{b}: mean {v['tvmean']:.4f}, max {v['tv']:.4f}" for (a, b), v in res.items()))
print()

print("== E. The kernel's tail ==")
n, Kt = 2048, 2.0 / 3.0
q = 2 * np.pi * np.arange(n) / n
Qg = (2 - 2 * np.cos(q))[:, None] + (2 - 2 * np.cos(q))[None, :]
ker = np.zeros_like(Qg)
ker[Qg > 0] = Kt * np.sqrt((Qg[Qg > 0] + 4) / Qg[Qg > 0])
U = np.real(np.fft.ifft2(ker))
ax = [(U[r, 0] - U[2 * r, 0]) * 2 * np.pi * r / Kt for r in (8, 16, 32)]
dg = [(U[r, r] - U[2 * r, 2 * r]) * 2 * np.pi * r * np.sqrt(2) / Kt for r in (8, 16, 32)]
check("(U(r) - U(2r)) 2 pi r / K = 1 within 1e-3 on an axis and 5e-3 on the diagonal at r = 8, 16, 32: a 1/r flux interaction",
      all(abs(x - 1) < 1e-3 for x in ax) and all(abs(x - 1) < 5e-3 for x in dg),
      "axis " + ", ".join(f"{x:.5f}" for x in ax) + "; diagonal " + ", ".join(f"{x:.5f}" for x in dg))
print()
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
