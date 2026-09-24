#!/usr/bin/env python3
'Finite computations supporting: Charge normalization and finite neutral-pair transfer calculations on a 4 by 4 prism, compared with a conditional charge-squared Gaussian prediction. Numerical diagnostics are not limit or particle theorems.'
AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = ('docs/UNIFORM_ICE_TEST_DEFECT_PAIRS_FOLLOW_THE_CHARGE_SQUARED_LAW_WITH_A_CORE_CORRECTION_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/UNIFORM_ICE_TEST_DEFECTS_INTERACT_THROUGH_THE_LATTICE_GREEN_FUNCTION_WITH_THE_FLUX_COST_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/UNIFORM_ICE_STATIC_PHOTON_STIFFENS_IN_A_BACKGROUND_FLUX_AND_SATURATION_LEAVES_SQUARE_ICE_BOUNDED_THEOREM_NOTE_2026-09-23.md')

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
        # defect 1 at (0, 0) in layer 0 with delta d1 (charge 2 d1); defect 2 at r in layer z with the opposite charge
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




P = Prism(4, 4)
lam0, psi = P.top(0)
lam2, _ = P.top(2)
lam4, _ = P.top(4)
A = 16
c2 = (A / 4) * np.log(lam0 / lam2)
c4 = (A / 16) * np.log(lam0 / lam4)
K = 2 * c2
layer = [(0, 1), (1, 0), (1, 1), (2, 0), (0, 2), (1, 2), (2, 1), (2, 2)]
V = {D: {r: P.pair(psi, lam0, r, 0, d1=D) for r in layer} for D in (1, 2)}
Vc4 = {r: P.pair(psi, lam0, r, 0, d1=-2) for r in ((0, 1), (1, 1))}
zs = (1, 2, 4, 8, 9)
Vz = {D: {z: P.pair(psi, lam0, (0, 0), z, d1=D) for z in zs} for D in (1, 2)}

print("== A. Symmetry ==")
groups = [[(1, 0), (0, 1)], [(1, 1), (2, 0), (0, 2)], [(1, 2), (2, 1)]]
spread = max(max(V[2][k] for k in g) - min(V[2][k] for k in g) for g in groups)
cs = max(abs(Vc4[r] - V[2][r]) for r in Vc4)
check('Finite diagnostic 1; scope and exceptions are in the companion note',
      spread < 1e-9 and cs < 1e-9, f"spread {spread:.1e}, complement {cs:.1e}")
print()

print("== B. The charge-squared law in the layer ==")
dist = {2: (1, 1), 3: (1, 2), 4: (2, 2)}
rat = {d: (V[2][r] - V[2][(0, 1)]) / (V[1][r] - V[1][(0, 1)]) for d, r in dist.items()}
check('Finite diagnostic 2; scope and exceptions are in the companion note',
      all(3.4 <= v <= 3.7 for v in rat.values()) and rat[2] < rat[3] < rat[4],
      ", ".join(f"distance {d}: {v:.3f}" for d, v in rat.items()))
print()

print("== C. Along the prism ==")
zr = {z: (Vz[2][z] - Vz[2][2]) / (Vz[1][z] - Vz[1][2]) for z in (4, 8)}
step4 = Vz[2][9] - Vz[2][8]
step2 = Vz[1][9] - Vz[1][8]
cost4 = np.log(lam0 / lam4)
check('Finite diagnostic 3; scope and exceptions are in the companion note',
      all(3.9 <= v <= 4.05 for v in zr.values()) and abs(step4 / cost4 - 1) < 0.01 and abs((step4 / step2) / (4 * c4 / c2) - 1) < 0.01,
      ", ".join(f"z={z}: {v:.3f}" for z, v in zr.items()) + f"; step ratio {step4 / step2:.4f} vs 4 c(4)/c(2) = {4 * c4 / c2:.4f}")
print()

print("== D. The core correction grows with the charge ==")
g = {r: green(4, 4, r, 0) for r in layer}
gr = {D: {d: (V[D][r] - V[D][(0, 1)]) / (K * (2 * D) ** 2 * (g[(0, 1)] - g[r])) for d, r in dist.items()} for D in (1, 2)}
check('Finite diagnostic 4; scope and exceptions are in the companion note',
      all(0.96 <= v <= 0.98 for v in gr[1].values()) and all(0.82 <= v <= 0.90 for v in gr[2].values()),
      "charge 2: " + ", ".join(f"{v:.4f}" for v in gr[1].values()) + "; charge 4: " + ", ".join(f"{v:.4f}" for v in gr[2].values()))
print()
print("maximum checked relative eigenpair residual:", max(EIGENPAIR_RESIDUALS, default=0.0))
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
