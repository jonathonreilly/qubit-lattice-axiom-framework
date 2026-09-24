#!/usr/bin/env python3
'Finite computations supporting: Conditional Gaussian trace identities and finite transfer-count and flux-cost comparisons on specified planar strips and cubic prisms. Numerical diagnostics are not limit or particle theorems.'
AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = ('docs/ICE_UNIT_FIELD_SUM_RULE_IS_TEN_TIMES_CLOSER_IN_THREE_DIMENSIONS_THAN_IN_SQUARE_ICE_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/UNIFORM_ICE_FLUX_STIFFNESS_ON_A_SQUARE_CROSS_SECTION_BY_ROW_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/UNIFORM_ICE_UNIT_LINK_FIELD_FIXES_ONE_STIFFNESS_FOR_THE_FLUX_COST_AND_THE_FIELD_CORRELATIONS_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/UNIFORM_ICE_STATIC_PHOTON_STIFFENS_IN_A_BACKGROUND_FLUX_AND_SATURATION_LEAVES_SQUARE_ICE_BOUNDED_THEOREM_NOTE_2026-09-23.md')

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
    Tm = np.zeros((n, n), dtype=object)
    for vin in range(n):
        for vout in range(n):
            for h in range(n):
                if all(((h >> ((x - 1) % a)) & 1) + ((h >> x) & 1) + ((vin >> x) & 1) + ((vout >> x) & 1) == 2 for x in range(a)):
                    Tm[vout, vin] += 1
    return int(np.trace(np.linalg.matrix_power(Tm, b)))


def unit(N, i):
    e = np.zeros(N)
    e[i] = 1.0
    return e


print("== A. The square-ice transfer ==")
counts = {}
for a, b in ((4, 4), (4, 6), (6, 4), (6, 6)):
    T = make_T2(a)
    M = np.column_stack([T(unit(1 << a, i)) for i in range(1 << a)])
    assert np.array_equal(M,np.rint(M))
    counts[(a, b)] = (int(np.trace(np.linalg.matrix_power(M.astype(np.int64).astype(object), b))), dense_square_ice(a, b))
check('Finite diagnostic 1; scope and exceptions are in the companion note',
      all(x == y for x, y in counts.values()) and counts[(4, 4)][0] == 2970,
      ", ".join(f"{a}x{b}: {x}" for (a, b), (x, y) in counts.items()))
print()

print("== B. The planar sum rule ==")
qq = 2 * np.pi * np.arange(1 << 20) / (1 << 20)
QQ = 2 - 2 * np.cos(qq)
avg = float(np.mean(np.sqrt(QQ / (QQ + 4))))
check('Finite diagnostic 2; scope and exceptions are in the companion note',
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
check('Finite diagnostic 3; scope and exceptions are in the companion note',
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
check('Finite diagnostic 4; scope and exceptions are in the companion note',
      all(abs(d) < 0.005 for d in dev3.values()) and max(abs(d) for d in dev3.values()) * 10 < min(dev2.values()),
      ", ".join(f"{a}x{b}: {th[(a, b)][0]:.5f} ({dev3[(a, b)] * 100:+.2f}%)" for (a, b) in th))
print()
print("maximum checked relative eigenpair residual:", max(EIGENPAIR_RESIDUALS, default=0.0))
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
