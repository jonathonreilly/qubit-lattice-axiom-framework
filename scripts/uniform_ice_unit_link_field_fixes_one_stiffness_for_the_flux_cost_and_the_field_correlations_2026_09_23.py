#!/usr/bin/env python3
"""Uniform ice: the unit field on every link fixes one stiffness for the flux cost and the field's correlations.

Open PRs 8746 and 8859 measured the cost of a flux sector per layer of
uniform ice, c(S) = (A / S^2) ln(lam_0 / lam_S), and found it nearly
independent of S (Gaussian). Open PR 8864 found the zero-flux layer chain
gapless, and the companion block found its branch to be that of the
massless nearest-neighbour lattice field on Z^3.

A Gaussian divergence-free field with weight exp(-(K/2) sum E^2) on the
links of the prism A x Z has two consequences. The flux S through every
layer costs K S^2 / (2A) per layer, so c = K / 2. The equal-layer
correlation of the vertical field at transverse wavenumber q is
S_zz(q) = sqrt(Q / (Q + 4)) / K, with Q = sum_i 2 (1 - cos q_i). Every link
carries E = (-1)^(x+y) (2v - 1) = +-1, so <E_z^2> = 1.
That fixes K to K_A = (1/A) sum_q sqrt(Q / (Q + 4)), with no free constant.

Checks:

A. On 2 x 2, 2 x 4, 2 x 6, 2 x 8, 2 x 10 and 4 x 4, the measured c(2)
   reproduces open PR 8859 (0.2808, 0.3073, 0.3121, 0.3137, 0.3145,
   0.3270). In the zero-flux vacuum S_zz(0) = 0 and (1/A) sum_q S_zz(q) = 1.
B. The flux cost c(2) is within 1% of K_A / 2 on every shape.
C. With K = 2 c(2) from the flux cost, K S_zz(q) is within 1% of
   sqrt(Q / (Q + 4)) at every nonzero wavenumber on the square 4 x 4. On the
   strips 2 x 4 to 2 x 10 it is within 5%, with the largest deviation at
   q = (pi, 0), the wavenumber that alternates across the width of 2. On
   2 x 2 it is within 10%.
D. The large-section value: the transverse projector of a divergence-free
   field has trace 2 at every nonzero wavevector of Z^3, so by cubic symmetry
   the Brillouin-zone average of sqrt(Q / (Q + 4)) is 2/3. The sum rule then
   gives K = 2/3 and c = 1/3. The measured costs lie below 1/3; the square's
   is within 2% of it.

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
            w, V = np.linalg.eigh((M + M.T) / 2)
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
check("c(2) reproduces open PR #8859 on 2 x 2 ... 2 x 10 and 4 x 4",
      all(abs(rows[s]["c2"] - G6[s]) < 5e-5 for s in G6),
      ", ".join(f"{a}x{b}: {rows[(a, b)]['c2']:.5f}" for a, b in G6))
check("in the zero-flux vacuum S_zz(0) = 0 and (1/A) sum_q S_zz(q) = 1 on every shape",
      all(abs(r["sz"][(0, 0)][0]) < 1e-9 and abs(np.mean([v for v, _ in r["sz"].values()]) - 1) < 1e-9 for r in rows.values()))
print()

print("== B. The flux cost is the stiffness fixed by the sum rule ==")
devB = {s: rows[s]["c2"] / (rows[s]["KA"] / 2) - 1 for s in G6}
check("c(2) is within 1% of K_A / 2 on every shape",
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
check("on the square 4 x 4, with K = 2 c(2), K S_zz(q) is within 1% of sqrt(Q/(Q+4)) at every nonzero wavenumber",
      devC[(4, 4)] < 0.01, f"largest deviation {devC[(4, 4)] * 100:.2f}%")
strips = [(2, 4), (2, 6), (2, 8), (2, 10)]
check("on the strips 2 x 4 to 2 x 10 it is within 5%, largest at q = (pi, 0) across the width; on 2 x 2 within 10%",
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
check("the transverse projector has trace 2, the k_z integral gives sqrt(Q/(Q+4)), and its zone average is 2/3",
      np.abs(trace - 2).max() < 1e-12 and np.abs(integ - np.sqrt(Qs / (Qs + 4))).max() < 1e-12 and abs(avg - 2 / 3) < 1e-8,
      f"average {avg:.10f}")
check("every measured cost lies below c = 1/3, and the square's is within 2% of it",
      all(r["c2"] < 1 / 3 for r in rows.values()) and abs(rows[(4, 4)]["c2"] * 3 - 1) < 0.02,
      f"square {rows[(4, 4)]['c2']:.5f} vs 1/3")
print()
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
