#!/usr/bin/env python3
"""Uniform ice: test defects interact through the lattice Green's function with the flux-cost stiffness.

Uniform ice puts three of the six links at every vertex occupied, so the
staggered link field E = (-1)^(x+y+z) (2v - 1) is divergence-free. A test
defect is one vertex where four (delta = +1) or two (delta = -1) links are
occupied instead. It carries charge 2 delta (-1)^(x+y+z) of that field. Two
opposite test defects are a probe of the layer measure: nothing is admitted
into the rule. Their free energy in the infinite prism A x Z is
V = -ln(Z_pair / Z_0), computed by layer transfer. Here T is the layer
transfer of the landed layer-unit note (PR 8740) and the row transfer of
open PR 8859, and a layer holding a defect uses the changed vertex count.

A Gaussian divergence-free field with stiffness K predicts
V(r) - V(r') = K Q^2 (G_A(r') - G_A(r)) for charges +-Q, where G_A is the
Green's function of the Z^3 graph Laplacian on the prism:
G_A(r, z) - G_A(0, 0) = (1/A) [ -|z|/2 + sum_{q != 0} (cos(q.r) e^(-D|z|) - 1) / (2 sinh D) ],
with cosh D = 1 + sum_i (1 - cos q_i). The runner takes Q = 2 and
K = 2 c(2) from the flux cost c(2) = (A/4) ln(lam_0 / lam_2), so nothing is
fitted.

Checks:

A. Symmetry. On the square 4 x 4 the pair free energy depends only on the
   graph distance of the cross-section, which is the four-cube: (1,0) and
   (0,1) agree, as do (1,1), (2,0) and (0,2), and (1,2) and (2,1). Swapping
   the defect types, the complement, leaves V unchanged on both shapes.
B. The string. At z = 8 the step V(z+1) - V(z) agrees with the Gaussian's
   within 0.1% on 4 x 4 and 2 x 8, and with the flux cost ln(lam_0 / lam_2)
   within 1%.
C. The square. In the layer, V rises with distance (the pair attracts), and
   V(r) - V(0,1) agrees with K Q^2 (G_A(0,1) - G_A(r)) within 4% at every
   separation; relative to distance 2, distances 3 and 4 agree within 1%.
   Along the prism, z = 1 to 9, the agreement is within 4%.
D. The strip 2 x 8. Along its length, and along the prism, the agreement is
   within 3%. Across the width of 2 it is within 8%.

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
check("on 4 x 4 the pair free energy depends only on the four-cube distance",
      spread < 1e-9, f"distance 1..4: {Vs[(0, 1, 0)]:.5f}, {Vs[(1, 1, 0)]:.5f}, {Vs[(1, 2, 0)]:.5f}, {Vs[(2, 2, 0)]:.5f}")
cspread = max(abs(d["Vc"][k] - d["V"][k]) for d in data.values() for k in d["Vc"])
check("swapping the defect types leaves V unchanged on both shapes", cspread < 1e-9, f"largest change {cspread:.1e}")
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
check("at z = 8 the step agrees with the Gaussian's within 0.1% and with the flux cost within 1%", okB, "; ".join(lines))
print()

print("== C. The square 4 x 4 ==")
rs = sq["ratio"]
inlayer = [(1, 1, 0), (1, 2, 0), (2, 2, 0)]
mono = Vs[(0, 1, 0)] < Vs[(1, 1, 0)] < Vs[(1, 2, 0)] < Vs[(2, 2, 0)]
rel = [(Vs[k] - Vs[(1, 1, 0)]) / (sq["K"] * Q * Q * (sq["G"][(1, 1, 0)] - sq["G"][k])) for k in ((1, 2, 0), (2, 2, 0))]
check("in the layer the pair attracts and V agrees with K Q^2 (G(0,1) - G(r)) within 4%; beyond distance 2 within 1%",
      mono and all(abs(rs[k] - 1) < 0.04 for k in inlayer) and all(abs(x - 1) < 0.01 for x in rel),
      "ratios " + ", ".join(f"{rs[k]:.4f}" for k in inlayer) + "; from distance 2: " + ", ".join(f"{x:.4f}" for x in rel))
zk = [(0, 0, z) for z in range(1, 10)]
check("along the prism, z = 1 to 9, the agreement is within 4%",
      all(abs(rs[k] - 1) < 0.04 for k in zk), "ratios " + ", ".join(f"{rs[k]:.3f}" for k in zk))
print()

print("== D. The strip 2 x 8 ==")
rt = st["ratio"]
length = [(0, y, 0) for y in (2, 3, 4)] + [(1, y, 0) for y in (2, 3, 4)]
width = [(1, 0, 0), (1, 1, 0)]
check("along the strip's length and along the prism the agreement is within 3%",
      all(abs(rt[k] - 1) < 0.03 for k in length + zk),
      "length " + ", ".join(f"{rt[k]:.3f}" for k in length) + "; prism " + ", ".join(f"{rt[k]:.3f}" for k in zk))
check("across the width of 2 the agreement is within 8%",
      all(abs(rt[k] - 1) < 0.08 for k in width), ", ".join(f"{k[:2]}: {rt[k]:.4f}" for k in width))
print()
print(f"K = 2 c(2): 4x4 {sq['K']:.5f}, 2x8 {st['K']:.5f}")
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
