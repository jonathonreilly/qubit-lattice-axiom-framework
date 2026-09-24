#!/usr/bin/env python3
"""The unit-field sum rule is ten times closer for three-dimensional ice than for square ice.

Open PRs 8871 and 8881 found that for uniform ice in three dimensions the
flux cost is fixed, to half a percent, by the sum rule of a Gaussian
divergence-free field whose unit link field has <E^2> = 1. Open PR 8928 found
that at full polarization each layer of three-dimensional ice becomes square
ice: two of four links occupied at every vertex of the plane. This runner
applies the same sum rule to square ice itself and compares.

On a strip of width a, periodic across and infinite along, the Gaussian field
with stiffness K costs K S^2 / (2a) per row for a flux S, so c = K/2. Its
equal-row correlation is sqrt(Q/(Q+4)) / K with Q = 2 - 2 cos q, and the sum
rule fixes K_a = (1/a) sum_q sqrt(Q/(Q+4)). In the plane the transverse
projector has trace 1, shared by two directions, so the zone average of
sqrt(Q/(Q+4)) is 1/2: K = 1/2 and c = 1/4 for wide strips.

Checks:

A. The square-ice row transfer, applied site by site, reproduces the torus
   counts of an independent dense row transfer: tr T^b on 4 x 4, 4 x 6,
   6 x 4 and 6 x 6 (2970 on 4 x 4, as in open PR 8928).
B. The one-dimensional zone average of sqrt(Q/(Q+4)) is 1/2 within 1e-9.
C. Square ice: the flux cost c(2) = (a/4) ln(lam_0/lam_2) rises with the
   width for a = 4 to 20 and exceeds the sum-rule value K_a/2 by 4.1% to
   4.7% at every width, the excess growing from a = 6 on.
D. Three-dimensional ice, by the row transfer of the landed note of PR 8859:
   on the prisms 2 x 8 and 4 x 4 the flux cost lies within 0.5% of its
   sum-rule value (open PR 8871), at least ten times closer than square ice
   at every width.

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


# ---------------------------------------------------------------- square ice, site by site
R2 = np.zeros((2, 2, 2, 2))
for vo in (0, 1):
    for co in (0, 1):
        for vi in (0, 1):
            for ci in (0, 1):
                if vo + co + vi + ci == 2:
                    R2[vo, co, vi, ci] = 1


def make_T2(a):
    def T(phi):
        A = phi.reshape((2,) * a)
        A = np.einsum("...,ij->...ij", A, np.eye(2))
        for x in range(a):
            A = np.tensordot(A, R2, axes=([x, a], [2, 3]))
            A = np.moveaxis(A, [a, a + 1], [x, a])
        return np.einsum("...ii->...", A).reshape(-1)
    return T


def dense_square_ice(a, b):
    n = 1 << a
    Tm = np.zeros((n, n))
    for vin in range(n):
        for vout in range(n):
            for h in range(n):
                if all(((h >> ((x - 1) % a)) & 1) + ((h >> x) & 1) + ((vin >> x) & 1) + ((vout >> x) & 1) == 2 for x in range(a)):
                    Tm[vout, vin] += 1
    return int(round(np.trace(np.linalg.matrix_power(Tm, b))))


def unit(N, i):
    e = np.zeros(N)
    e[i] = 1.0
    return e


print("== A. The square-ice transfer ==")
counts = {}
for a, b in ((4, 4), (4, 6), (6, 4), (6, 6)):
    T = make_T2(a)
    M = np.column_stack([T(unit(1 << a, i)) for i in range(1 << a)])
    counts[(a, b)] = (int(round(np.trace(np.linalg.matrix_power(M, b)))), dense_square_ice(a, b))
check("tr T^b from the site-by-site transfer equals the dense row-transfer count on 4x4, 4x6, 6x4, 6x6",
      all(x == y for x, y in counts.values()) and counts[(4, 4)][0] == 2970,
      ", ".join(f"{a}x{b}: {x}" for (a, b), (x, y) in counts.items()))
print()

print("== B. The planar sum rule ==")
qq = 2 * np.pi * np.arange(1 << 20) / (1 << 20)
QQ = 2 - 2 * np.cos(qq)
avg = float(np.mean(np.sqrt(QQ / (QQ + 4))))
check("the one-dimensional zone average of sqrt(Q/(Q+4)) is 1/2 within 1e-9, so K = 1/2 and c = 1/4 on wide strips",
      abs(avg - 0.5) < 1e-9, f"average {avg:.12f}")
print()


def cost_2d(a):
    N = 1 << a
    idx = np.arange(N)
    S = np.zeros(N, dtype=np.int64)
    for x in range(a):
        S += (-1) ** x * (2 * ((idx >> (a - 1 - x)) & 1) - 1)
    T = make_T2(a)

    def top(s):
        # the staggered flux of a row flips sign from row to row, so a sector is |S| = s
        m = (np.abs(S) == s).astype(float)
        if N <= 256:
            sel = np.where(m > 0)[0]
            M = np.column_stack([T(unit(N, i))[sel] for i in sel])
            return float(np.max(np.abs(np.linalg.eigvals(M))))
        op = LinearOperator((N, N), matvec=lambda u: m * T(m * u), dtype=float)
        return float(abs(eigsh(op, k=1, which="LM", tol=1e-12, maxiter=50000)[0][0]))
    c = (a / 4) * np.log(top(0) / top(2))
    q = 2 * np.pi * np.arange(a) / a
    Q = 2 - 2 * np.cos(q)
    return c, float(np.mean(np.sqrt(Q / (Q + 4)))) / 2


print("== C. Square ice ==")
sq = {a: cost_2d(a) for a in range(4, 21, 2)}
dev2 = {a: c / k - 1 for a, (c, k) in sq.items()}
widths = sorted(sq)
check("c(2) rises with the width for a = 4 to 20 and exceeds K_a/2 by 4.1% to 4.7% at every width, the excess growing from a = 6 on",
      all(sq[x][0] < sq[y][0] for x, y in zip(widths, widths[1:])) and all(0.041 <= d <= 0.047 for d in dev2.values())
      and all(dev2[x] < dev2[y] for x, y in zip(widths[1:], widths[2:]))
      and dev2[20] > dev2[16] > dev2[12],
      ", ".join(f"{a}: {sq[a][0]:.5f} ({dev2[a] * 100:+.2f}%)" for a in widths))
print()


# ---------------------------------------------------------------- three-dimensional ice
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


def cost_3d(a, b):
    n, N, A = 1 << a, 1 << (a * b), a * b
    R = row_tensor(a)

    def T(phi):
        X = phi.reshape((n,) * b)
        X = np.einsum("...,ij->...ij", X, np.eye(n))
        for r in range(b):
            X = np.tensordot(X, R, axes=([r, b], [2, 3]))
            X = np.moveaxis(X, [b, b + 1], [r, b])
        return np.einsum("...ii->...", X).reshape(-1)
    idx = np.arange(N)
    S = np.zeros(N, dtype=np.int64)
    for y in range(b):
        for x in range(a):
            S += (-1) ** (x + y) * (2 * ((idx >> ((b - 1 - y) * a + x)) & 1) - 1)

    def top(s):
        m = (np.abs(S) == s).astype(float)
        op = LinearOperator((N, N), matvec=lambda u: m * T(m * u), dtype=float)
        return float(abs(eigsh(op, k=1, which="LM", tol=1e-12, maxiter=50000)[0][0]))
    c = (A / 4) * np.log(top(0) / top(2))
    qx = 2 * np.pi * np.arange(a) / a
    qy = 2 * np.pi * np.arange(b) / b
    Q = (2 - 2 * np.cos(qx))[:, None] + (2 - 2 * np.cos(qy))[None, :]
    return c, float(np.mean(np.sqrt(Q / (Q + 4)))) / 2


print("== D. Three-dimensional ice ==")
th = {s: cost_3d(*s) for s in ((2, 8), (4, 4))}
dev3 = {s: c / k - 1 for s, (c, k) in th.items()}
check("on the prisms 2x8 and 4x4 the flux cost lies within 0.5% of its sum-rule value, at least ten times closer than square ice at every width",
      all(abs(d) < 0.005 for d in dev3.values()) and max(abs(d) for d in dev3.values()) * 10 < min(dev2.values()),
      ", ".join(f"{a}x{b}: {th[(a, b)][0]:.5f} ({dev3[(a, b)] * 100:+.2f}%)" for (a, b) in th))
print()
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
