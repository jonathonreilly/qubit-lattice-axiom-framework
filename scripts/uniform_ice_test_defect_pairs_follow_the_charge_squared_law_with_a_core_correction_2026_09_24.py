#!/usr/bin/env python3
"""Uniform ice: test-defect pairs follow the charge-squared law, with a core correction that grows with the charge.

Open PR 8875 put two test defects, vertices with four or two of their six
links occupied (charge +-2 of the staggered field), into the layer measure of
uniform ice. Their pair free energy followed K Q^2 (G_A(r') - G_A(r)) with
Q = 2 and K = 2 c(2), within 4% on the square 4 x 4. A vertex with five or one
occupied links (delta = +-2) carries charge +-4. The Gaussian field predicts
four times the free-energy differences for a charge-4 pair. This runner
tests that on the square 4 x 4, with the layer transfer of the landed
layer-unit note (PR 8740) applied by the row transfer of the landed note of
PR 8859.

Checks:

A. Symmetry. The charge-4 pair free energy on 4 x 4 depends only on the
   four-cube distance of the cross-section, and swapping the defect types
   (the complement) leaves it unchanged.
B. The charge-squared law in the layer. Relative to the nearest pair, the
   charge-4 differences are 3.4 to 3.7 times the charge-2 differences at
   distances 2, 3 and 4, rising with distance toward 4.
C. Along the prism, beyond the contact pair z = 1 (whose charge-4 core is
   anomalous), the ratio of differences measured from z = 2 lies between
   3.9 and 4.05 at z = 4 and 8. At z = 8 the charge-4 step V(z+1) - V(z)
   equals the flux cost ln(lam_0 / lam_4) within 1%, and its ratio to the
   charge-2 step equals 4 c(4)/c(2) = 4.04 within 1%: the string ratio, not
   exactly 4.
D. The core correction grows with the charge. Against K Q^2 Delta G with
   K = 2 c(2), the in-layer ratios are 0.96 to 0.98 for charge 2 and 0.82 to
   0.90 for charge 4.

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
check("the charge-4 pair free energy depends only on the four-cube distance, and the complement leaves it unchanged",
      spread < 1e-9 and cs < 1e-9, f"spread {spread:.1e}, complement {cs:.1e}")
print()

print("== B. The charge-squared law in the layer ==")
dist = {2: (1, 1), 3: (1, 2), 4: (2, 2)}
rat = {d: (V[2][r] - V[2][(0, 1)]) / (V[1][r] - V[1][(0, 1)]) for d, r in dist.items()}
check("relative to the nearest pair, charge-4 differences are 3.4 to 3.7 times the charge-2 ones at distances 2, 3, 4, rising",
      all(3.4 <= v <= 3.7 for v in rat.values()) and rat[2] < rat[3] < rat[4],
      ", ".join(f"distance {d}: {v:.3f}" for d, v in rat.items()))
print()

print("== C. Along the prism ==")
zr = {z: (Vz[2][z] - Vz[2][2]) / (Vz[1][z] - Vz[1][2]) for z in (4, 8)}
step4 = Vz[2][9] - Vz[2][8]
step2 = Vz[1][9] - Vz[1][8]
cost4 = np.log(lam0 / lam4)
check("beyond the contact pair, relative to z = 2, the ratio at z = 4 and 8 lies in [3.9, 4.05]; at z = 8 the charge-4 step equals ln(lam_0/lam_4) and its ratio to the charge-2 step equals 4 c(4)/c(2), both within 1%",
      all(3.9 <= v <= 4.05 for v in zr.values()) and abs(step4 / cost4 - 1) < 0.01 and abs((step4 / step2) / (4 * c4 / c2) - 1) < 0.01,
      ", ".join(f"z={z}: {v:.3f}" for z, v in zr.items()) + f"; step ratio {step4 / step2:.4f} vs 4 c(4)/c(2) = {4 * c4 / c2:.4f}")
print()

print("== D. The core correction grows with the charge ==")
g = {r: green(4, 4, r, 0) for r in layer}
gr = {D: {d: (V[D][r] - V[D][(0, 1)]) / (K * (2 * D) ** 2 * (g[(0, 1)] - g[r])) for d, r in dist.items()} for D in (1, 2)}
check("against K Q^2 Delta G the in-layer ratios are 0.96 to 0.98 for charge 2 and 0.82 to 0.90 for charge 4",
      all(0.96 <= v <= 0.98 for v in gr[1].values()) and all(0.82 <= v <= 0.90 for v in gr[2].values()),
      "charge 2: " + ", ".join(f"{v:.4f}" for v in gr[1].values()) + "; charge 4: " + ", ".join(f"{v:.4f}" for v in gr[2].values()))
print()
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
