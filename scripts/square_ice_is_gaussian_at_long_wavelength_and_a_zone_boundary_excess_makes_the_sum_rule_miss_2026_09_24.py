#!/usr/bin/env python3
"""Square ice is Gaussian at long wavelength; a zone-boundary excess makes the unit-field sum rule miss.

Open PR 8930 found that square ice (two of four links occupied at every
vertex of the plane) has a flux cost 4.1% to 4.7% above the value the
unit-field sum rule gives a Gaussian divergence-free field, while
three-dimensional uniform ice sits ten times closer. This runner asks which
part of the Gaussian picture fails in the plane.

On a strip of width a, with the row law psi^2 of the zero-flux top vector psi,
the equal-row correlation of the staggered field is S(q) = (1/a) <|E_q|^2>.
A Gaussian field with stiffness K has S(q) = g(q) / K with
g(q) = sqrt(Q / (Q + 4)), Q = 2 - 2 cos q. Take K = 2 c(2) from the measured
flux cost and define R(q) = K S(q) / g(q). Because E^2 = 1 exactly,
sum_q S(q) = a, so K / K_a = sum_q R(q) g(q) / sum_q g(q): the flux cost
exceeds the sum rule by the g-weighted mean of R - 1.

Checks:

A. The site-by-site square-ice transfer gives the 4 x 4 torus count 2970
   (open PR 8928) and the flux costs of open PR 8930 on widths 8 to 20.
B. At long wavelength the Gaussian holds with one stiffness: R at the
   smallest wavenumber 2 pi / a is 0.9901, 0.9949, 0.9970 and 0.9981 for
   a = 8, 12, 16 and 20, rising toward 1.
C. At the zone boundary it fails: R(pi) lies between 1.09 and 1.11 on every
   width, and R rises monotonically from the smallest wavenumber to pi.
D. The g-weighted mean of R equals K / K_a within 1e-9 on every width,
   between 1.041 and 1.047: the zone-boundary excess is the sum rule's miss.

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


def unit(N, i):
    e = np.zeros(N)
    e[i] = 1.0
    return e


def strip(a):
    N = 1 << a
    idx = np.arange(N)
    E = [((-1) ** x * (2 * ((idx >> (a - 1 - x)) & 1) - 1)).astype(np.int8) for x in range(a)]
    S = np.sum(E, axis=0, dtype=np.int64)
    T = make_T2(a)

    def top(s, vec=False):
        # the staggered flux of a row flips sign from row to row, so a sector is |S| = s
        m = (np.abs(S) == s).astype(float)
        op = LinearOperator((N, N), matvec=lambda u: m * T(m * u), dtype=float)
        w, V = eigsh(op, k=1, which="LA", tol=1e-12, maxiter=50000)
        return (float(w[0]), np.abs(V[:, 0])) if vec else float(w[0])
    l0, psi = top(0, True)
    c = (a / 4) * np.log(l0 / top(2))
    P = psi ** 2 / (psi ** 2).sum()
    q = 2 * np.pi * np.arange(a) / a
    Sq = np.zeros(a)
    for m in range(a):
        Eq = np.zeros(N, dtype=complex)
        for x in range(a):
            Eq += np.exp(-1j * q[m] * x) * E[x]
        Sq[m] = float(np.sum(P * np.abs(Eq) ** 2)) / a
    Q = 2 - 2 * np.cos(q)
    g = np.sqrt(Q / (Q + 4))
    K = 2 * c
    R = np.ones(a)
    R[1:] = K * Sq[1:] / g[1:]
    return dict(c=c, K=K, Ka=float(g.mean()), R=R, g=g, Szero=float(Sq[0]))


print("== A. The transfer ==")
T4 = make_T2(4)
M = np.column_stack([T4(unit(16, i)) for i in range(16)])
tor = int(round(np.trace(np.linalg.matrix_power(M, 4))))
res = {a: strip(a) for a in (8, 12, 16, 20)}
ref = {8: 0.25641, 12: 0.25933, 16: 0.26040, 20: 0.26090}
check("the 4 x 4 torus count is 2970, and the flux costs on widths 8 to 20 reproduce open PR 8930",
      tor == 2970 and all(abs(res[a]["c"] - ref[a]) < 5e-6 for a in ref),
      f"count {tor}; " + ", ".join(f"{a}: {res[a]['c']:.5f}" for a in res))
print()

print("== B. Long wavelength ==")
first = {a: res[a]["R"][1] for a in res}
check("R at the smallest wavenumber is 0.9901, 0.9949, 0.9970, 0.9981 for a = 8 to 20, rising toward 1",
      all(abs(first[a] - v) < 5e-5 for a, v in zip((8, 12, 16, 20), (0.9901, 0.9949, 0.9970, 0.9981)))
      and first[8] < first[12] < first[16] < first[20] < 1, ", ".join(f"{a}: {v:.4f}" for a, v in first.items()))
print()

print("== C. The zone boundary ==")
edge = {a: res[a]["R"][a // 2] for a in res}
mono = all(np.all(np.diff(res[a]["R"][1:a // 2 + 1]) > 0) for a in res)
check("R(pi) lies between 1.09 and 1.11 on every width, and R rises monotonically from the smallest wavenumber to pi",
      all(1.09 <= v <= 1.11 for v in edge.values()) and mono, ", ".join(f"{a}: {v:.4f}" for a, v in edge.items()))
print()

print("== D. The excess is the sum rule's miss ==")
wm = {a: float((res[a]["R"][1:] * res[a]["g"][1:]).sum() / res[a]["g"][1:].sum()) for a in res}
ratio = {a: res[a]["K"] / res[a]["Ka"] for a in res}
# the zero mode: S(0) = 0 in the zero-flux sector, so only q != 0 carries weight
check("the g-weighted mean of R equals K / K_a within 1e-9 on every width, between 1.041 and 1.047",
      all(abs(wm[a] - ratio[a]) < 1e-9 and 1.041 <= wm[a] <= 1.047 for a in res) and all(abs(res[a]["Szero"]) < 1e-12 for a in res),
      ", ".join(f"{a}: {wm[a]:.5f} vs {ratio[a]:.5f}" for a in res))
print()
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
