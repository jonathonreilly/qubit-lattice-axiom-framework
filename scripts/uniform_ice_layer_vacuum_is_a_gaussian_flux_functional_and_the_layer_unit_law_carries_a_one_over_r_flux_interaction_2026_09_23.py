#!/usr/bin/env python3
'Finite computations supporting: An exact positive-eigenvector Markov transform, finite fits to a Gaussian layer functional and finite FFT comparisons for the supplied kernel. Numerical diagnostics are not limit or particle theorems.'
AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = ('docs/UNIFORM_ICE_LAYER_VACUUM_IS_A_GAUSSIAN_FLUX_FUNCTIONAL_AND_THE_LAYER_UNIT_LAW_CARRIES_A_ONE_OVER_R_FLUX_INTERACTION_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/UNIFORM_ICE_BY_LAYER_UNITS_ON_INFINITE_PRISMS_IS_EXACT_IN_THE_ZERO_FLUX_SECTOR_THAT_LONG_PRISMS_SELECT_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/UNIFORM_ICE_FLUX_STIFFNESS_ON_A_SQUARE_CROSS_SECTION_BY_ROW_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/UNIFORM_ICE_UNIT_LINK_FIELD_FIXES_ONE_STIFFNESS_FOR_THE_FLUX_COST_AND_THE_FIELD_CORRELATIONS_BOUNDED_THEOREM_NOTE_2026-09-23.md')

import sys
import time

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh as _eigsh
EIGENPAIR_RESIDUALS = []
def eigsh(op, *args, **kwargs):
    rng = np.random.default_rng(20260924)
    if "v0" not in kwargs:
        v0 = rng.standard_normal(op.shape[0])
        if np.issubdtype(op.dtype, np.complexfloating):
            v0 = v0 + 1j*rng.standard_normal(op.shape[0])
        kwargs["v0"] = v0
    values, vectors = _eigsh(op, *args, **kwargs)
    for j, value in enumerate(values):
        v = vectors[:, j]; applied = op @ v
        residual = np.linalg.norm(applied-value*v)/max(1.0, abs(value)*np.linalg.norm(v), np.linalg.norm(applied))
        assert np.isfinite(residual) and residual < 1e-8, residual
        EIGENPAIR_RESIDUALS.append(float(residual))
    return values, vectors


PASS = FAIL = 0
T0 = time.time()
print("Evidence boundary: finite computations and bin diagnostics; no certified spectral enclosure, confidence coverage, particle claim or limit theorem.")


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
check('Finite diagnostic 1; scope and exceptions are in the companion note', dev < 1e-9, f"largest deviation {dev:.1e}")
print()

print("== B. The layer vacuum is Gaussian (measured kernel) ==")
check('Finite diagnostic 2; scope and exceptions are in the companion note',
      all(v["r2m"] >= 0.996 and abs(v["sm"] * 4 + 1) < 0.08 for v in res.values()) and abs(res[(4, 4)]["sm"] * 4 + 1) < 0.02,
      ", ".join(f"{a}x{b}: slope {v['sm']:.4f}, R2 {v['r2m']:.4f}" for (a, b), v in res.items()))
print()

print("== C. The predicted kernel, from K = 2 c(2) alone ==")
check('Finite diagnostic 3; scope and exceptions are in the companion note',
      all(v["r2p"] >= 0.979 and abs(v["sp"] * 4 + 1) < 0.03 for v in res.values()) and res[(4, 4)]["r2p"] >= 0.998,
      ", ".join(f"{a}x{b}: slope {v['sp']:.4f}, R2 {v['r2p']:.4f}" for (a, b), v in res.items()))
print()

print("== D. The formation law ==")
check('Finite diagnostic 4; scope and exceptions are in the companion note',
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
check('Finite diagnostic 5; scope and exceptions are in the companion note',
      all(abs(x - 1) < 1e-3 for x in ax) and all(abs(x - 1) < 5e-3 for x in dg),
      "axis " + ", ".join(f"{x:.5f}" for x in ax) + "; diagonal " + ", ".join(f"{x:.5f}" for x in dg))
print()
print("maximum checked relative eigenpair residual:", max(EIGENPAIR_RESIDUALS, default=0.0))
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
