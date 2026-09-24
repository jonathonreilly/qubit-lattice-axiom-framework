#!/usr/bin/env python3
'Finite computations supporting: Conditional Gaussian prism covariance and variance calibration, with finite numerical ice flux-cost and equal-layer correlation comparisons. Numerical diagnostics are not limit or particle theorems.'
AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = ('docs/UNIFORM_ICE_UNIT_LINK_FIELD_FIXES_ONE_STIFFNESS_FOR_THE_FLUX_COST_AND_THE_FIELD_CORRELATIONS_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/UNIFORM_ICE_BY_LAYER_UNITS_ON_INFINITE_PRISMS_IS_EXACT_IN_THE_ZERO_FLUX_SECTOR_THAT_LONG_PRISMS_SELECT_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/UNIFORM_ICE_FLUX_STIFFNESS_ON_A_SQUARE_CROSS_SECTION_BY_ROW_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-23.md')

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


class Prism:
    def __init__(self, a, b):
        self.a, self.b, self.n, self.A = a, b, 1 << a, a * b
        self.R = row_tensor(a)
        self.N = 1 << (a * b)
        idx = np.arange(self.N)
        self.E = []
        for y in range(b):
            for x in range(a):
                self.E.append(((-1) ** (x + y) * (2 * ((idx >> ((b - 1 - y) * a + x)) & 1) - 1)).astype(np.int8))
        self.S = np.sum(self.E, axis=0, dtype=np.int64)

    def T(self, phi):
        n, b = self.n, self.b
        A = phi.reshape((n,) * b)
        A = np.einsum("...,ij->...ij", A, np.eye(n))
        for r in range(b):
            A = np.tensordot(A, self.R, axes=([r, b], [2, 3]))
            A = np.moveaxis(A, [b, b + 1], [r, b])
        return np.einsum("...ii->...", A).reshape(-1)

    def top(self, s):
        # T maps flux S to -S between consecutive layers, so the sector is |S| = s
        m = (np.abs(self.S) == s).astype(float)
        if self.N <= 4096:
            sel = np.where(m > 0)[0]
            M = np.column_stack([self.T(np.eye(self.N)[k])[sel] for k in sel])
            assert np.array_equal(M, M.T), "raw transfer symmetry"
            w, V = np.linalg.eigh(M)
            vec = np.zeros(self.N)
            vec[sel] = V[:, -1]
            return float(w[-1]), vec
        op = LinearOperator((self.N, self.N), matvec=lambda u: m * self.T(m * u), dtype=float)
        w, V = eigsh(op, k=1, which="LA", tol=1e-11, maxiter=50000)
        return float(w[0]), V[:, 0]

    def szz(self, psi):
        P = psi ** 2 / np.sum(psi ** 2)
        out = {}
        for mx in range(self.a):
            for my in range(self.b):
                qx, qy = 2 * np.pi * mx / self.a, 2 * np.pi * my / self.b
                Eq = np.zeros(self.N, dtype=complex)
                k = 0
                for y in range(self.b):
                    for x in range(self.a):
                        Eq += np.exp(-1j * (qx * x + qy * y)) * self.E[k]
                        k += 1
                Q = 2 * (1 - np.cos(qx)) + 2 * (1 - np.cos(qy))
                out[(mx, my)] = (float(np.sum(P * np.abs(Eq) ** 2) / self.A), float(np.sqrt(Q / (Q + 4))))
        return out


G6 = {(2, 2): 0.2808, (2, 4): 0.3073, (2, 6): 0.3121, (2, 8): 0.3137, (2, 10): 0.3145, (4, 4): 0.3270}
rows = {}
for (a, b) in G6:
    P = Prism(a, b)
    lam0, psi = P.top(0)
    lam2, _ = P.top(2)
    c2 = (P.A / 4) * np.log(lam0 / lam2)
    sz = P.szz(psi)
    KA = float(np.mean([g for _, g in sz.values()]))
    rows[(a, b)] = dict(c2=c2, sz=sz, KA=KA)
    del P, psi

print("== A. The flux costs of open PR #8859 and the vacuum's sum rule ==")
check('Finite diagnostic 1; scope and exceptions are in the companion note',
      all(abs(rows[s]["c2"] - G6[s]) < 5e-5 for s in G6),
      ", ".join(f"{a}x{b}: {rows[(a, b)]['c2']:.5f}" for a, b in G6))
check('Finite diagnostic 2; scope and exceptions are in the companion note',
      all(abs(r["sz"][(0, 0)][0]) < 1e-9 and abs(np.mean([v for v, _ in r["sz"].values()]) - 1) < 1e-9 for r in rows.values()))
print()

print("== B. The flux cost is the stiffness fixed by the sum rule ==")
devB = {s: rows[s]["c2"] / (rows[s]["KA"] / 2) - 1 for s in G6}
check('Finite diagnostic 3; scope and exceptions are in the companion note',
      all(abs(d) < 0.01 for d in devB.values()),
      ", ".join(f"{a}x{b}: {rows[(a, b)]['KA'] / 2:.5f} ({devB[(a, b)] * 100:+.2f}%)" for a, b in G6))
print()

print("== C. The same stiffness sets the correlations ==")
devC, argC = {}, {}
for s, r in rows.items():
    K = 2 * r["c2"]
    dev = {key: abs(K * v / g - 1) for key, (v, g) in r["sz"].items() if key != (0, 0)}
    argC[s] = max(dev, key=dev.get)
    devC[s] = dev[argC[s]]
check('Finite diagnostic 4; scope and exceptions are in the companion note',
      devC[(4, 4)] < 0.01, f"largest deviation {devC[(4, 4)] * 100:.2f}%")
strips = [(2, 4), (2, 6), (2, 8), (2, 10)]
check('Finite diagnostic 5; scope and exceptions are in the companion note',
      all(devC[s] < 0.05 and argC[s] == (1, 0) for s in strips) and devC[(2, 2)] < 0.10,
      ", ".join(f"{a}x{b}: {devC[(a, b)] * 100:.1f}% at {argC[(a, b)]}" for a, b in [(2, 2)] + strips))
print()

print("== D. The large-section value ==")
rng = np.random.default_rng(3)
k = rng.uniform(-np.pi, np.pi, size=(1000, 3))
s2 = 2 * (1 - np.cos(k))
trace = np.sum(1 - s2 / s2.sum(axis=1, keepdims=True), axis=1)
nq = 1024
q = 2 * np.pi * np.arange(nq) / nq
Qg = (2 - 2 * np.cos(q))[:, None] + (2 - 2 * np.cos(q))[None, :]
avg = float(np.sqrt(Qg / (Qg + 4)).mean())
Qs = np.array([0.5, 2.0, 6.0])
kz = 2 * np.pi * (np.arange(4096) + 0.5) / 4096
integ = np.array([np.mean(Qv / (Qv + 2 - 2 * np.cos(kz))) for Qv in Qs])
check('Finite diagnostic 6; scope and exceptions are in the companion note',
      np.abs(trace - 2).max() < 1e-12 and np.abs(integ - np.sqrt(Qs / (Qs + 4))).max() < 1e-12 and abs(avg - 2 / 3) < 1e-8,
      f"average {avg:.10f}")
check('Finite diagnostic 7; scope and exceptions are in the companion note',
      all(r["c2"] < 1 / 3 for r in rows.values()) and abs(rows[(4, 4)]["c2"] * 3 - 1) < 0.02,
      f"square {rows[(4, 4)]['c2']:.5f} vs 1/3")
print()
print("maximum checked relative eigenpair residual:", max(EIGENPAIR_RESIDUALS, default=0.0))
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
