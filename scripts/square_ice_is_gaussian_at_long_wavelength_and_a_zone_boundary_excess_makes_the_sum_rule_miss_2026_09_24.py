#!/usr/bin/env python3
'Finite computations supporting: An exact Parseval-based weighted identity and finite square-ice row-correlation comparisons on four widths; no Gaussian probability-law or long-wavelength limit theorem. Numerical diagnostics are not limit or particle theorems.'
AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = ('docs/SQUARE_ICE_IS_GAUSSIAN_AT_LONG_WAVELENGTH_AND_A_ZONE_BOUNDARY_EXCESS_MAKES_THE_SUM_RULE_MISS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ICE_UNIT_FIELD_SUM_RULE_IS_TEN_TIMES_CLOSER_IN_THREE_DIMENSIONS_THAN_IN_SQUARE_ICE_BOUNDED_THEOREM_NOTE_2026-09-23.md')

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
assert np.array_equal(M,np.rint(M))
tor = int(np.trace(np.linalg.matrix_power(M.astype(np.int64).astype(object), 4)))
res = {a: strip(a) for a in (8, 12, 16, 20)}
ref = {8: 0.25641, 12: 0.25933, 16: 0.26040, 20: 0.26090}
check('Finite diagnostic 1; scope and exceptions are in the companion note',
      tor == 2970 and all(abs(res[a]["c"] - ref[a]) < 5e-6 for a in ref),
      f"count {tor}; " + ", ".join(f"{a}: {res[a]['c']:.5f}" for a in res))
print()

print("== B. Long wavelength ==")
first = {a: res[a]["R"][1] for a in res}
check('Finite diagnostic 2; scope and exceptions are in the companion note',
      all(abs(first[a] - v) < 5e-5 for a, v in zip((8, 12, 16, 20), (0.9901, 0.9949, 0.9970, 0.9981)))
      and first[8] < first[12] < first[16] < first[20] < 1, ", ".join(f"{a}: {v:.4f}" for a, v in first.items()))
print()

print("== C. The zone boundary ==")
edge = {a: res[a]["R"][a // 2] for a in res}
mono = all(np.all(np.diff(res[a]["R"][1:a // 2 + 1]) > 0) for a in res)
check('Finite diagnostic 3; scope and exceptions are in the companion note',
      all(1.09 <= v <= 1.11 for v in edge.values()) and mono, ", ".join(f"{a}: {v:.4f}" for a, v in edge.items()))
print()

print("== D. The excess is the sum rule's miss ==")
wm = {a: float((res[a]["R"][1:] * res[a]["g"][1:]).sum() / res[a]["g"][1:].sum()) for a in res}
ratio = {a: res[a]["K"] / res[a]["Ka"] for a in res}
# the zero mode: S(0) = 0 in the zero-flux sector, so only q != 0 carries weight
check('Finite diagnostic 4; scope and exceptions are in the companion note',
      all(abs(wm[a] - ratio[a]) < 1e-9 and 1.041 <= wm[a] <= 1.047 for a in res) and all(abs(res[a]["Szero"]) < 1e-12 for a in res),
      ", ".join(f"{a}: {wm[a]:.5f} vs {ratio[a]:.5f}" for a in res))
print()
print("maximum checked relative eigenpair residual:", max(EIGENPAIR_RESIDUALS, default=0.0))
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
