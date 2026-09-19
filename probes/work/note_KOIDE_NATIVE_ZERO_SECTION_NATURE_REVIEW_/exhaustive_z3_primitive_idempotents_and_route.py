#!/usr/bin/env python3
"""Probe: KOIDE_NATIVE_ZERO_SECTION_NATURE_REVIEW_NOTE_2026-04-24 (route algebra of
KOIDE_NATIVE_ZERO_SECTION_CLOSURE_ROUTE_NOTE_2026-04-24, (D1)-(D5)).

The review's second falsifier is "a retained equivariant spectator projector on
the real primitive".  Implemented literally, with machinery disjoint from the
runners (sympy solve): self-written exact arithmetic in Q(sqrt3) and
Q(sqrt(-3)) as integer pairs, and EXHAUSTIVE enumeration.

 A  (D1) on the rational grid z = k/60, k = -59..600 (z != 1): Q(w_plus(z)) = 2/3
    and K_TL(w_plus(z)) = 0 exactly at z = 0 only; z = -1/3 gives w = 1/3, Q = 1.
 B  (D2)/(D3): every 2x2 matrix with entries in {(p + q sqrt3)/2 : |p|,|q| <= 2}
    (25^4 = 390625 matrices) tested for X R = R X and X^2 = X exactly: the
    commutant in the grid is exactly {aI + bJ} (625 matrices), its idempotents
    are 0 and I only; no rank-one idempotent of the grid, and no rational-slope
    line projector (t = tan(alpha/2) = k/12, |k| <= 240, plus the vertical
    line), commutes with R.  The real idempotent equation on aI + bJ has no root
    with b != 0 (a = 1/2 forces b^2 = -1/4).
 C  (D5) eta_Z3 = (1/3) sum_{k=1,2} 1/((w^k - 1)(w^{2k} - 1)) = 2/9 in Q(sqrt(-3));
    (D4) F(0) = 0 forces c = 0; delta_open = 2/9, and c = 1/9 gives 1/3.
 D  beyond the primitive (numbers only): rotations by 2 pi/n, n = 3..12, have a
    two-dimensional commutant with idempotents 0, I; the multiplicity-two
    doublet R + R on R^4 and the permutation representation on R^3 DO carry
    nontrivial equivariant idempotents (spectator projectors), so the absence
    is specific to the single real primitive; weights-(1,2) eta for odd n and
    weights-(1,-1) eta = (n^2 - 1)/(12 n).

Prints SUMMARY: lines; HIT: only when a stated route fact fails.
"""
import itertools
import math
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import mpmath as mp

HITS = []


def hit(msg):
    HITS.append(msg)
    print("HIT: " + msg)


def summary(msg):
    print("SUMMARY: " + msg)


# ---------------------------------------------------------------------------- A
def run_A():
    print("=" * 78)
    print("A  (D1) the source-label section")

    def wplus(z):
        return (1 + z) / 2

    def Q(w):
        return (1 + (1 - w) / w) / 3

    def KTL(w):
        r = (1 - w) / w
        return (r * r - 1) / (4 * r)
    zs = [Fr(k, 60) for k in range(-59, 601) if Fr(k, 60) != 1]
    q23 = [z for z in zs if Q(wplus(z)) == Fr(2, 3)]
    k0 = [z for z in zs if KTL(wplus(z)) == 0]
    w13 = wplus(Fr(-1, 3))
    print(f"  {len(zs)} rational labels: Q = 2/3 exactly at {[str(z) for z in q23]}; K_TL = 0 exactly at {[str(z) for z in k0]}; "
          f"z = -1/3: w = {w13}, Q = {Q(w13)}")
    ok = q23 == [0] and k0 == [0] and w13 == Fr(1, 3) and Q(w13) == 1 and wplus(0) == Fr(1, 2)
    if not ok:
        hit("the zero-section algebra (D1) differs")
    return len(zs), q23, k0, ok


# ---------------------------------------------------------------------------- B
# entries (p + q sqrt3)/2 stored as integer pairs (p, q); products carry denominator 4
def run_B():
    print("=" * 78)
    print("B  (D2)/(D3) exhaustive equivariant idempotents on the real Z3 primitive")
    vals = [(p, q) for p in range(-2, 3) for q in range(-2, 3)]
    V = np.array(vals, dtype=np.int64)                 # 25 x 2
    idx = np.array(list(itertools.product(range(25), repeat=4)), dtype=np.int64)   # 390625 x 4
    X = V[idx]                                         # N x 4 x 2 : entries x00, x01, x10, x11 as (p, q)
    # R = [[-1/2, -sqrt3/2], [sqrt3/2, -1/2]] -> pairs (-1, 0), (0, -1), (0, 1), (-1, 0)
    R = np.array([[-1, 0], [0, -1], [0, 1], [-1, 0]], dtype=np.int64)

    def mul(a, b):
        """(a0 + a1 s)(b0 + b1 s) with s = sqrt3, both over 2: numerator pair over 4"""
        return np.stack([a[..., 0] * b[..., 0] + 3 * a[..., 1] * b[..., 1], a[..., 0] * b[..., 1] + a[..., 1] * b[..., 0]], -1)

    def matmul(A, B):
        # A, B: (..., 4, 2) row-major 2x2; returns (..., 4, 2) numerators over 4
        c00 = mul(A[..., 0, :], B[..., 0, :]) + mul(A[..., 1, :], B[..., 2, :])
        c01 = mul(A[..., 0, :], B[..., 1, :]) + mul(A[..., 1, :], B[..., 3, :])
        c10 = mul(A[..., 2, :], B[..., 0, :]) + mul(A[..., 3, :], B[..., 2, :])
        c11 = mul(A[..., 2, :], B[..., 1, :]) + mul(A[..., 3, :], B[..., 3, :])
        return np.stack([c00, c01, c10, c11], -2)
    Rb = np.broadcast_to(R, X.shape)
    XR = matmul(X, Rb)
    RX = matmul(Rb, X)
    comm = np.all(XR == RX, axis=(-1, -2))
    XX = matmul(X, X)                                  # over 4; X over 2 -> X^2 = X  <=>  XX == 2 X
    idem = np.all(XX == 2 * X, axis=(-1, -2))
    n_comm = int(comm.sum())
    # commutant elements have the form [[a, -b], [b, a]]
    Xc = X[comm]
    form_ok = bool(np.all(Xc[:, 0] == Xc[:, 3]) and np.all(Xc[:, 1] == -Xc[:, 2]))
    eq_idem = X[comm & idem]
    eq_list = sorted(tuple(map(tuple, m.tolist())) for m in eq_idem)
    zero = ((0, 0), (0, 0), (0, 0), (0, 0))
    ident = ((2, 0), (0, 0), (0, 0), (2, 0))
    n_idem_all = int(idem.sum())
    # rank-one idempotents in the grid (trace 1) and whether any commutes with R
    tr = X[:, 0, :] + X[:, 3, :]
    rank1 = idem & np.all(tr == np.array([2, 0]), axis=-1)
    n_rank1 = int(rank1.sum())
    n_rank1_comm = int((rank1 & comm).sum())
    print(f"  390625 grid matrices: commutant members {n_comm} (all of the form aI + bJ: {form_ok}); equivariant idempotents "
          f"{len(eq_list)} = {{0, I}}: {eq_list == sorted([zero, ident])}; idempotents in the grid overall {n_idem_all}, rank-one "
          f"{n_rank1}, rank-one commuting with R {n_rank1_comm}")
    # real idempotent equation on aI + bJ: a^2 - b^2 = a, 2ab = b  ->  b = 0 or a = 1/2 with b^2 = a^2 - a = -1/4
    a = Fr(1, 2)
    no_b = (a * a - a) < 0
    # rational-slope line projectors (tan(alpha/2) = t) commute with R?
    comm_lines = 0
    tested = 0
    for k in list(range(-240, 241)) + [None]:
        if k is None:
            v = (Fr(-1), Fr(0))                           # t = infinity: alpha = pi
        else:
            t = Fr(k, 12)
            v = ((1 - t * t) / (1 + t * t), 2 * t / (1 + t * t))
        P = [[v[0] * v[0], v[0] * v[1]], [v[1] * v[0], v[1] * v[1]]]
        # [R, P] with R = [[-1/2, -s/2],[s/2, -1/2]], s = sqrt3: entries (rational part, sqrt3 part)
        # (RP - PR)_{ij} rational parts cancel (the -1/2 I part commutes); sqrt3 parts: (1/2)(K P - P K), K = [[0,-1],[1,0]]
        K = [[0, -1], [1, 0]]
        KP = [[sum(K[i][m] * P[m][j] for m in range(2)) for j in range(2)] for i in range(2)]
        PK = [[sum(P[i][m] * K[m][j] for m in range(2)) for j in range(2)] for i in range(2)]
        tested += 1
        if all(KP[i][j] == PK[i][j] for i in range(2) for j in range(2)):
            comm_lines += 1
    print(f"  idempotent equation on aI + bJ: a = 1/2 forces b^2 = {a * a - a} < 0 (no real root with b != 0): {no_b}; "
          f"{tested} rational line projectors, commuting with R: {comm_lines}")
    ok = form_ok and n_comm == 625 and eq_list == sorted([zero, ident]) and n_rank1_comm == 0 and no_b and comm_lines == 0
    if not ok:
        hit("a Z3-equivariant spectator projector exists on the real primitive, or the commutant differs from {aI + bJ}")
    return n_comm, len(eq_list), n_idem_all, n_rank1, tested, ok


# ---------------------------------------------------------------------------- C
class Eis:
    """a + b sqrt(-3) with Fractions"""
    def __init__(s, a, b=0):
        s.a, s.b = Fr(a), Fr(b)

    def __add__(s, o):
        o = o if isinstance(o, Eis) else Eis(o)
        return Eis(s.a + o.a, s.b + o.b)

    def __sub__(s, o):
        o = o if isinstance(o, Eis) else Eis(o)
        return Eis(s.a - o.a, s.b - o.b)

    def __mul__(s, o):
        o = o if isinstance(o, Eis) else Eis(o)
        return Eis(s.a * o.a - 3 * s.b * o.b, s.a * o.b + s.b * o.a)

    def inv(s):
        d = s.a * s.a + 3 * s.b * s.b
        return Eis(s.a / d, -s.b / d)

    def __eq__(s, o):
        o = o if isinstance(o, Eis) else Eis(o)
        return s.a == o.a and s.b == o.b


def run_C():
    print("=" * 78)
    print("C  (D4)/(D5) the finite Z3 scalar and the endpoint law")
    w = Eis(Fr(-1, 2), Fr(1, 2))                 # omega = (-1 + sqrt(-3))/2
    ok_w = (w * w * w) == 1 and not (w == 1)

    def pw(x, n):
        out = Eis(1)
        for _ in range(n):
            out = out * x
        return out
    terms = [((pw(w, k) - 1) * (pw(w, 2 * k) - 1)) for k in (1, 2)]
    eta = (terms[0].inv() + terms[1].inv()) * Eis(Fr(1, 3))
    c = Fr(0)                                    # F(phi) = phi + c with F(0) = 0
    delta = eta.a + c
    delta_torsor = eta.a + Fr(1, 9)
    print(f"  omega^3 = 1: {ok_w}; (w^k - 1)(w^2k - 1) = {terms[0].a}+{terms[0].b}sqrt(-3), {terms[1].a}+{terms[1].b}sqrt(-3); "
          f"eta_Z3 = {eta.a} + {eta.b} sqrt(-3); delta_open = {delta}; unbased c = 1/9 gives {delta_torsor}")
    ok = ok_w and eta == Eis(Fr(2, 9)) and delta == Fr(2, 9) and delta_torsor == Fr(1, 3)
    if not ok:
        hit("eta_Z3 or the endpoint law differs from 2/9")
    return eta.a, delta, delta_torsor, ok


# ---------------------------------------------------------------------------- D
def run_D():
    print("=" * 78)
    print("D  beyond the single primitive (numbers only)")
    rows = []
    for n in range(3, 13):
        th = 2 * math.pi / n
        R = np.array([[math.cos(th), -math.sin(th)], [math.sin(th), math.cos(th)]])
        # commutant: solve X R - R X = 0 as a 4x4 linear system
        M = np.kron(np.eye(2), R.T) - np.kron(R, np.eye(2))   # vec(X R) - vec(R X) for row-major vec
        dimc = 4 - np.linalg.matrix_rank(M, tol=1e-10)
        rows.append((n, int(dimc)))
    print("  rotations by 2pi/n: commutant dimension " + ", ".join(f"n={n}: {d}" for n, d in rows))
    # multiplicity two: R (+) R on R^4, and the permutation representation on R^3
    th = 2 * math.pi / 3
    R = np.array([[math.cos(th), -math.sin(th)], [math.sin(th), math.cos(th)]])
    R4 = np.block([[R, np.zeros((2, 2))], [np.zeros((2, 2)), R]])
    P4 = np.diag([1.0, 1.0, 0.0, 0.0])
    spect4 = np.allclose(P4 @ R4, R4 @ P4) and np.allclose(P4 @ P4, P4)
    M4 = np.kron(np.eye(4), R4.T) - np.kron(R4, np.eye(4))
    dim4 = int(16 - np.linalg.matrix_rank(M4, tol=1e-10))
    C3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=float)
    Pt = np.full((3, 3), 1 / 3)
    spect3 = np.allclose(Pt @ C3, C3 @ Pt) and np.allclose(Pt @ Pt, Pt)
    print(f"  R+R on R^4: commutant dimension {dim4} (M_2(C)); diag(I, 0) is an equivariant idempotent: {spect4}; "
          f"permutation rep on R^3: the trivial-line projector J/3 is equivariant: {spect3}")
    # eta with weights (1, 2) for odd n, and weights (1, -1)
    mp.mp.dps = 40
    e12 = {}
    e11 = {}
    for n in range(3, 26, 2):
        om = mp.e ** (2j * mp.pi / n)
        s = sum(1 / ((om ** k - 1) * (om ** (2 * k) - 1)) for k in range(1, n)) / n
        fr = Fr(mp.nstr(mp.re(s), 35)).limit_denominator(10 ** 6)
        e12[n] = str(fr) if abs(mp.im(s)) < mp.mpf(10) ** -30 and abs(mp.re(s) - mp.mpf(fr.numerator) / fr.denominator) < mp.mpf(10) ** -30 else "irrational?"
    for n in range(2, 31):
        om = mp.e ** (2j * mp.pi / n)
        s = sum(1 / ((om ** k - 1) * (om ** (-k) - 1)) for k in range(1, n)) / n
        e11[n] = abs(mp.re(s) - mp.mpf(n * n - 1) / (12 * n)) < mp.mpf(10) ** -30
    print(f"  eta with weights (1,2), odd n: {', '.join(f'n={n}: {v}' for n, v in e12.items())}")
    print(f"  eta with weights (1,-1) equals (n^2-1)/(12n) for n = 2..30: {all(e11.values())} (n = 3: 8/36 = 2/9)")
    return rows, dim4, spect4, spect3, e12, all(e11.values())


def main():
    t0 = time.time()
    nz, q23, k0, okA = run_A()
    summary(f"A (D1): on {nz} rational labels Q = 2/3 and K_TL = 0 hold exactly at z = 0 only ({[str(z) for z in q23]}, "
            f"{[str(z) for z in k0]}); z = -1/3 gives "
            f"w = 1/3, Q = 1")
    nc, ne, nia, nr1, tested, okB = run_B()
    summary(f"B (D2)/(D3) exhaustive over 390625 exact Q(sqrt3) matrices: commutant {nc} = {{aI + bJ}} on the grid, "
            f"equivariant idempotents {ne} = {{0, I}}, of {nia} grid idempotents ({nr1} rank-one) none rank-one commutes with R; "
            f"{tested} rational line projectors: none commutes; no spectator projector on the real primitive: {okB}")
    eta, delta, dt, okC = run_C()
    summary(f"C (D4)/(D5): eta_Z3 = {eta} exactly in Q(sqrt(-3)); F(0) = 0 gives c = 0 and delta_open = {delta}; unbased c = 1/9 "
            f"gives {dt}")
    rows, dim4, s4, s3, e12, e11 = run_D()
    summary(f"D beyond: 2 pi/n rotations n = 3..12 commutant dims {[d for _, d in rows]}; multiplicity-two doublet commutant dim "
            f"{dim4} with spectator diag(I,0): {s4}; R^3 permutation rep trivial-line projector equivariant: {s3}; weights-(1,2) "
            f"eta at odd n: {', '.join(f'{n}: {v}' for n, v in list(e12.items())[:6])}; weights-(1,-1) = (n^2-1)/(12n): {e11}")
    print("=" * 78)
    summary(f"hits={len(HITS)}; runtime {time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
