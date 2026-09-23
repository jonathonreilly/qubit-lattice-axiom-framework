#!/usr/bin/env python3
"""Uniform ice: the zero-flux layer chain's gap closes as the smallest transverse wavenumber.

Open PR #8740 formed uniform ice by layer units on infinite prisms: in the
zero-flux sector the law of a layer depends only on the layer below, a
Markov chain whose transfer matrix T is the layer transfer. How fast the
chain forgets is set by its gap, the log of the ratio between the top
eigenvalue and the next largest in modulus within the sector. This runner
computes that gap on cross-sections 2 x b (b = 2 to 10) and on the square
4 x 4. It applies T row by row (open PR #8859), so the matrix is never
formed.

Checks:

A. The values of open PR #8740: on 2 x 2 the zero-flux top eigenvalue is
   32 + 2 sqrt(209) and the next modulus is 14; on 2 x 4 the next modulus is
   668.3638.
B. On every cross-section the next level is negative and degenerate: twice
   on the strips, four times on the square. The negative sign is the
   staggered sign of the occupation form, so correlations of the
   occupations alternate from layer to layer.
C. On the strips the gap D times b rises and stays below 2 pi: 2.94, 5.12,
   5.71, 5.94, 6.06. So on the computed strips the gap closes like 1/b, and
   the chain's memory grows with the cross-section.
D. The square 4 x 4 has the gap of the strip 2 x 4 within 2%: the gap
   follows the smallest transverse wavenumber 2 pi / 4, not the area.

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


def make_matvec(a, b):
    R = row_tensor(a)
    n = 1 << a

    def matvec(phi):
        A = phi.reshape((n,) * b)
        A = np.einsum("...,ij->...ij", A, np.eye(n))
        for r in range(b):
            A = np.tensordot(A, R, axes=([r, b], [2, 3]))
            A = np.moveaxis(A, [b, b + 1], [r, b])
        return np.einsum("...ii->...", A).reshape(-1)
    return matvec


def zero_flux(a, b):
    idx = np.arange(1 << (a * b))
    S = np.zeros(len(idx), dtype=np.int64)
    for y in range(b):
        for x in range(a):
            S += (-1) ** (x + y) * (2 * ((idx >> ((b - 1 - y) * a + x)) & 1) - 1)
    return np.where(S == 0)[0], len(idx)


def top_levels(a, b, k=5):
    mv = make_matvec(a, b)
    sel, N = zero_flux(a, b)

    def f(u):
        full = np.zeros(N)
        full[sel] = u
        return mv(full)[sel]
    if len(sel) <= 400:
        Mx = np.column_stack([f(e) for e in np.eye(len(sel))])
        ev = np.linalg.eigvalsh((Mx + Mx.T) / 2)
    else:
        op = LinearOperator((len(sel), len(sel)), matvec=f, dtype=np.float64)
        ev = eigsh(op, k=k, which="LM", tol=1e-11, maxiter=50000)[0]
    return sorted(ev, key=lambda x: -abs(x))


LV = {}
for a, b in ((2, 2), (2, 4), (2, 6), (2, 8), (2, 10), (4, 4)):
    LV[(a, b)] = top_levels(a, b)
gap = {ab: float(np.log(abs(LV[ab][0]) / abs(LV[ab][1]))) for ab in LV}

print("== A. The values of open PR #8740 ==")
check("2 x 2: top 32 + 2 sqrt(209), next modulus 14; 2 x 4: next modulus 668.3638",
      abs(LV[(2, 2)][0] - (32 + 2 * 209 ** 0.5)) < 1e-9 and abs(abs(LV[(2, 2)][1]) - 14) < 1e-9
      and abs(abs(LV[(2, 4)][1]) - 668.3638) < 1e-4,
      f"{LV[(2, 2)][0]:.4f}, {abs(LV[(2, 2)][1]):.4f}; {abs(LV[(2, 4)][1]):.4f}")
print()

print("== B. The next level ==")
deg = {}
for ab, ev in LV.items():
    nxt = ev[1]
    deg[ab] = sum(1 for x in ev[1:] if abs(x - nxt) < 1e-6 * abs(nxt))
strips_ok = all(LV[(2, b)][1] < 0 and deg[(2, b)] == 2 for b in (2, 4, 6, 8, 10))
check("the next level is negative on every cross-section, twice degenerate on the strips and four times on the square",
      strips_ok and LV[(4, 4)][1] < 0 and deg[(4, 4)] == 4,
      "degeneracies " + ", ".join(f"{a}x{b}: {deg[(a, b)]}" for a, b in LV))
print()

print("== C. Strips: the gap closes like 1/b ==")
seq = [gap[(2, b)] * b for b in (2, 4, 6, 8, 10)]
check("gap times b rises and stays below 2 pi, so the gap closes like 1/b",
      all(seq[i] < seq[i + 1] for i in range(4)) and seq[-1] < 2 * np.pi and seq[-1] > 0.96 * 2 * np.pi,
      "gap x b = " + ", ".join(f"{x:.4f}" for x in seq) + f"; 2 pi = {2 * np.pi:.4f}")
print()

print("== D. The square follows the smallest wavenumber ==")
check("the square 4 x 4 has the gap of the strip 2 x 4 within 2%",
      abs(gap[(4, 4)] / gap[(2, 4)] - 1) < 0.02, f"{gap[(4, 4)]:.5f} vs {gap[(2, 4)]:.5f}")
print()
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
