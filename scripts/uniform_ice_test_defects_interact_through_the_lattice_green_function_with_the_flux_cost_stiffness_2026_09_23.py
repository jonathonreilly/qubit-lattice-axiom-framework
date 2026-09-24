#!/usr/bin/env python3
'Finite computations supporting: Charge normalization and a conditional Gaussian prism potential, with finite transfer calculations for neutral test-defect pairs. Numerical diagnostics are not limit or particle theorems.'
AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = ('docs/UNIFORM_ICE_TEST_DEFECTS_INTERACT_THROUGH_THE_LATTICE_GREEN_FUNCTION_WITH_THE_FLUX_COST_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/UNIFORM_ICE_BY_LAYER_UNITS_ON_INFINITE_PRISMS_IS_EXACT_IN_THE_ZERO_FLUX_SECTOR_THAT_LONG_PRISMS_SELECT_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/UNIFORM_ICE_FLUX_STIFFNESS_ON_A_SQUARE_CROSS_SECTION_BY_ROW_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/UNIFORM_ICE_UNIT_LINK_FIELD_FIXES_ONE_STIFFNESS_FOR_THE_FLUX_COST_AND_THE_FIELD_CORRELATIONS_BOUNDED_THEOREM_NOTE_2026-09-23.md')

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


def row_tensor(a, deltas):
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
                    need = [3 + deltas[x] - hdeg[x] - ib[x] - ob[x] - wb[x] for x in range(a)]
                    if all(t in (0, 1) for t in need):
                        R[sum(t << x for x, t in enumerate(need)), o, w, i] += 1
    return R


class Prism:
    def __init__(self, a, b):
        self.a, self.b, self.n, self.A = a, b, 1 << a, a * b
        self.N = 1 << (a * b)
        self.R0 = row_tensor(a, [0] * a)
        self.rows = {}
        idx = np.arange(self.N)
        S = np.zeros(self.N, dtype=np.int64)
        for y in range(b):
            for x in range(a):
                S += (-1) ** (x + y) * (2 * ((idx >> ((b - 1 - y) * a + x)) & 1) - 1)
        self.S = S

    def T(self, phi, defects=()):
        # defects: (x, y, delta) in this layer
        n, b = self.n, self.b
        tensors = [self.R0] * b
        for y in sorted(set(d[1] for d in defects)):
            dl = [0] * self.a
            for (x, yy, de) in defects:
                if yy == y:
                    dl[x] += de
            key = tuple(dl)
            if key not in self.rows:
                self.rows[key] = row_tensor(self.a, dl)
            tensors[y] = self.rows[key]
        A = phi.reshape((n,) * b)
        A = np.einsum("...,ij->...ij", A, np.eye(n))
        for r in range(b):
            A = np.tensordot(A, tensors[r], axes=([r, b], [2, 3]))
            A = np.moveaxis(A, [b, b + 1], [r, b])
        return np.einsum("...ii->...", A).reshape(-1)

    def top(self, s):
        # T maps the flux S of one layer to -S, so a flux sector is |S| = s
        m = (np.abs(self.S) == s).astype(float)
        op = LinearOperator((self.N, self.N), matvec=lambda u: m * self.T(m * u), dtype=float)
        w, V = eigsh(op, k=1, which="LA", tol=1e-12, maxiter=50000)
        v = V[:, 0]
        return float(w[0]), v / np.linalg.norm(v) * np.sign(v.sum())

    def pair(self, psi, lam0, r, z, d1=1):
        # defect 1 at (0, 0) in layer 0 with delta d1; defect 2 at r in layer z with the opposite charge
        d2 = -d1 * (-1) ** ((r[0] + r[1] + z) % 2)
        if z == 0:
            w = self.T(psi, defects=[(0, 0, d1), (r[0], r[1], d2)])
            return -np.log(float(psi @ w) / lam0)
        u = self.T(psi, defects=[(0, 0, d1)])
        for _ in range(z - 1):
            u = self.T(u)
        w = self.T(u, defects=[(r[0], r[1], d2)])
        return -np.log(float(psi @ w) / lam0 ** (z + 1))


def green(a, b, r, z):
    tot = -abs(z) / 2.0
    for mx in range(a):
        for my in range(b):
            if mx == 0 and my == 0:
                continue
            qx, qy = 2 * np.pi * mx / a, 2 * np.pi * my / b
            D = np.arccosh(1 + (1 - np.cos(qx)) + (1 - np.cos(qy)))
            tot += (np.cos(qx * r[0] + qy * r[1]) * np.exp(-D * abs(z)) - 1) / (2 * np.sinh(D))
    return tot / (a * b)


Q = 2
data = {}
for (a, b) in ((4, 4), (2, 8)):
    P = Prism(a, b)
    lam0, psi = P.top(0)
    lam2, _ = P.top(2)
    c2 = (P.A / 4) * np.log(lam0 / lam2)
    K = 2 * c2
    keys = [(x, y, 0) for x in range(a // 2 + 1) for y in range(b // 2 + 1) if (x, y) != (0, 0)] + [(0, 0, z) for z in range(1, 10)]
    V = {k: P.pair(psi, lam0, k[:2], k[2]) for k in keys}
    Vc = {k: P.pair(psi, lam0, k[:2], k[2], d1=-1) for k in ((0, 1, 0), (0, 0, 2))}
    G = {k: green(a, b, k[:2], k[2]) for k in keys}
    # pairs equivalent to the reference (the four-cube's (1,0) on 4 x 4) have no difference to compare
    ratio = {k: (V[k] - V[(0, 1, 0)]) / (K * Q * Q * (G[(0, 1, 0)] - G[k])) for k in keys if abs(G[(0, 1, 0)] - G[k]) > 1e-12}
    data[(a, b)] = dict(lam0=lam0, lam2=lam2, c2=c2, K=K, V=V, Vc=Vc, G=G, ratio=ratio)
    del P, psi

sq, st = data[(4, 4)], data[(2, 8)]
print("== A. Symmetry ==")
Vs = sq["V"]
groups = [[(1, 0, 0), (0, 1, 0)], [(1, 1, 0), (2, 0, 0), (0, 2, 0)], [(1, 2, 0), (2, 1, 0)]]
spread = max(max(Vs[k] for k in g) - min(Vs[k] for k in g) for g in groups)
check('Finite diagnostic 1; scope and exceptions are in the companion note',
      spread < 1e-9, f"distance 1..4: {Vs[(0, 1, 0)]:.5f}, {Vs[(1, 1, 0)]:.5f}, {Vs[(1, 2, 0)]:.5f}, {Vs[(2, 2, 0)]:.5f}")
cspread = max(abs(d["Vc"][k] - d["V"][k]) for d in data.values() for k in d["Vc"])
check('Finite diagnostic 2; scope and exceptions are in the companion note', cspread < 1e-9, f"largest change {cspread:.1e}")
print()

print("== B. The string ==")
lines = []
okB = True
for s, d in data.items():
    step = d["V"][(0, 0, 9)] - d["V"][(0, 0, 8)]
    gstep = d["K"] * Q * Q * (d["G"][(0, 0, 8)] - d["G"][(0, 0, 9)])
    cost = np.log(d["lam0"] / d["lam2"])
    okB &= abs(step / gstep - 1) < 1e-3 and abs(step / cost - 1) < 1e-2
    lines.append(f"{s[0]}x{s[1]}: step {step:.5f}, Gaussian {gstep:.5f}, ln(lam0/lam2) {cost:.5f}")
check('Finite diagnostic 3; scope and exceptions are in the companion note', okB, "; ".join(lines))
print()

print("== C. The square 4 x 4 ==")
rs = sq["ratio"]
inlayer = [(1, 1, 0), (1, 2, 0), (2, 2, 0)]
mono = Vs[(0, 1, 0)] < Vs[(1, 1, 0)] < Vs[(1, 2, 0)] < Vs[(2, 2, 0)]
rel = [(Vs[k] - Vs[(1, 1, 0)]) / (sq["K"] * Q * Q * (sq["G"][(1, 1, 0)] - sq["G"][k])) for k in ((1, 2, 0), (2, 2, 0))]
check('Finite diagnostic 4; scope and exceptions are in the companion note',
      mono and all(abs(rs[k] - 1) < 0.04 for k in inlayer) and all(abs(x - 1) < 0.01 for x in rel),
      "ratios " + ", ".join(f"{rs[k]:.4f}" for k in inlayer) + "; from distance 2: " + ", ".join(f"{x:.4f}" for x in rel))
zk = [(0, 0, z) for z in range(1, 10)]
check('Finite diagnostic 5; scope and exceptions are in the companion note',
      all(abs(rs[k] - 1) < 0.04 for k in zk), "ratios " + ", ".join(f"{rs[k]:.3f}" for k in zk))
print()

print("== D. The strip 2 x 8 ==")
rt = st["ratio"]
length = [(0, y, 0) for y in (2, 3, 4)] + [(1, y, 0) for y in (2, 3, 4)]
width = [(1, 0, 0), (1, 1, 0)]
check('Finite diagnostic 6; scope and exceptions are in the companion note',
      all(abs(rt[k] - 1) < 0.03 for k in length + zk),
      "length " + ", ".join(f"{rt[k]:.3f}" for k in length) + "; prism " + ", ".join(f"{rt[k]:.3f}" for k in zk))
check('Finite diagnostic 7; scope and exceptions are in the companion note',
      all(abs(rt[k] - 1) < 0.08 for k in width), ", ".join(f"{k[:2]}: {rt[k]:.4f}" for k in width))
print()
print(f"K = 2 c(2): 4x4 {sq['K']:.5f}, 2x8 {st['K']:.5f}")
print("maximum checked relative eigenpair residual:", max(EIGENPAIR_RESIDUALS, default=0.0))
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
