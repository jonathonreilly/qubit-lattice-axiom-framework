#!/usr/bin/env python3
"""Two-presentation swap is proper-rotation conjugacy on the delivered hw=1 carrier.

Paired note:
docs/KCPT_CORNER_CARRIER_TWO_PRESENTATION_SWAP_PROPER_ROTATION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-07-18.md

The mechanism note's two-model FLAG leaves an unfixed binary choice between the
entrywise-conjugate presentations of the supplied joint Pauli/corner surface. This
runner computes, in exact integer and exact symbolic arithmetic, that the induced
corner-projector pair is
conjugate under the pi-rotation about [1,-1,0] -- a PROPER cubic rotation named by
the LATTICE axiom -- delivered on the same 4^3 staggered surface as the landed hw=1
carrier (T1); rotation conjugation acts on the supplied projector family exactly as
entrywise conjugation K (T2); the presentation pair is a single 2-orbit of the
proper rotation and the canonical K-odd separator is exchanged exactly as by K (T3);
on the Hermitian probe section the antilinear K-exchange coincides exactly with the
linear rotation conjugation while off the section the two gradings are inequivalent
(T4); and an honest operator-level covariance report for the named 4096-candidate
dressed class (T5), consumed by no other claim.

Blocks:
  A   construction replicated from the landed runner (exact integer): the
      one-component staggered operator on the periodic 4^3 torus, its exact
      rank 56 / kernel dimension 8, the eight orthogonal corner plane waves,
      the translations, and the landed C_3[111] kernel action U_R V = V C
  B1  T1 -- lattice delivery of the presentation-swap rotation (items a-g)
  B2  T2 -- rotation conjugation equals entrywise conjugation on the projector
      family (items h-l)
  B3  T3 -- the corner-projector pair is a proper-rotation orbit; canonical K-odd
      separator exchanged as by K (orbit statement + item p)
  B4  T4 -- K-parity equals rotation parity on the Hermitian section; off-section
      inequivalence witnesses (items m, n, o)
  B5  r-neutrality guard (item q)
  B6  T5 -- operator-level covariance report for the named dressed class
      (honest computed report; consumed by no other claim)
  B7  verbatim quote gates (Q1-Q6): sources carry the consumed sentences and the
      note blockquotes them
  B8  ledger shard filename gates (timeless: existence only, no status pins)
  B9  note hygiene: section presence, forbidden-phrase absence, no bare decimal
      literals, markdown dependency links, backticked context handles

All lattice arithmetic is exact integer; all carrier algebra is exact symbolic.
No floats, no tolerances, no randomness. Exit 1 on any failure.
Cache: logs/runner-cache/kcpt_corner_carrier_two_presentation_swap_proper_rotation_conjugacy_2026_07_18.txt
"""

import itertools
import re
from pathlib import Path

import numpy as np
import sympy as sp
from sympy import I, Matrix, Rational, conjugate, eye, sqrt

ROOT = Path(__file__).resolve().parents[1]

NOTE = (
    "docs/KCPT_CORNER_CARRIER_TWO_PRESENTATION_SWAP_PROPER_ROTATION_"
    "CONJUGACY_BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
RUNNER = (
    "scripts/kcpt_corner_carrier_two_presentation_swap_proper_rotation_"
    "conjugacy_2026_07_18.py"
)
CACHE = (
    "logs/runner-cache/kcpt_corner_carrier_two_presentation_swap_proper_"
    "rotation_conjugacy_2026_07_18.txt"
)

AXIOMS = "docs/MINIMAL_AXIOMS_2026-06-29.md"
GATE = "docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
BLOCK05 = (
    "docs/KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_"
    "SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md"
)
MECH = (
    "docs/KCPT_ORBIT_CONSTANT_REGISTERED_OCCUPANCY_WEIGHTS_DERIVABLE_"
    "PROTOCOL_CLASS_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
DELIVERY = (
    "docs/KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_"
    "POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md"
)

PASS = 0
FAIL = 0
FAILURES = []


def check(block, name, condition, detail=""):
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
        FAILURES.append(f"{block}:{name}")
    suffix = f" [{detail}]" if detail else ""
    print(f"{block} {status} {name}{suffix}")


def mat_zero(M):
    return all(
        sp.simplify(sp.expand_complex(sp.expand(M[i, j]))) == 0
        for i in range(M.rows)
        for j in range(M.cols)
    )


def is_zero(expr):
    return sp.simplify(sp.expand_complex(sp.expand(expr))) == 0


def flattened(rel):
    return " ".join((ROOT / rel).read_text(encoding="utf-8").split())


def quote_groups(rel):
    groups, cur = [], []
    for line in (ROOT / rel).read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith(">"):
            cur.append(s.lstrip(">").strip())
        else:
            if cur:
                groups.append(" ".join(" ".join(cur).split()))
                cur = []
    if cur:
        groups.append(" ".join(" ".join(cur).split()))
    return groups


def in_groups(groups, needle):
    return any(needle in g for g in groups)


# ---------------------------------------------------------------------------
# A: construction, exact integer arithmetic (replicated from the landed runner)
# ---------------------------------------------------------------------------

L = 4
N = L**3


def sites():
    return itertools.product(range(L), repeat=3)


def idx(x1, x2, x3):
    return (x1 * L + x2) * L + x3


EMU = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def eta_ks(x, mu):
    if mu == 0:
        return 1
    if mu == 1:
        return (-1) ** x[0]
    return (-1) ** (x[0] + x[1])


# D2 = 2*D so all entries are integers; D = one-component staggered operator
D2 = np.zeros((N, N), dtype=np.int64)
for x in sites():
    for mu, e in enumerate(EMU):
        xp = tuple((x[k] + e[k]) % L for k in range(3))
        xm = tuple((x[k] - e[k]) % L for k in range(3))
        D2[idx(*x), idx(*xp)] += eta_ks(x, mu)
        D2[idx(*x), idx(*xm)] -= eta_ks(x, mu)

check(
    "A.1",
    "2D is integer antisymmetric with entries in {-1,0,1}",
    np.array_equal(D2, -D2.T) and set(np.unique(D2)) <= {-1, 0, 1},
)

rank_exact = sp.Matrix(D2.tolist()).rank()
check("A.2", "exact rank(D) = 56, so dim ker D = 8", rank_exact == 56)

SUBSETS = [
    (),
    (0,),
    (1,),
    (2,),
    (0, 1),
    (0, 2),
    (1, 2),
    (0, 1, 2),
]
V8 = np.zeros((N, 8), dtype=np.int64)
for j, S in enumerate(SUBSETS):
    for x in sites():
        V8[idx(*x), j] = (-1) ** sum(x[mu] for mu in S)

check(
    "A.3",
    "all eight corner plane waves are exact null vectors of D",
    np.array_equal(D2 @ V8, np.zeros((N, 8), dtype=np.int64)),
)
check(
    "A.4",
    "corner waves orthogonal (V8^T V8 = 64*I), hence they span ker D exactly",
    np.array_equal(V8.T @ V8, 64 * np.eye(8, dtype=np.int64)),
)

Tmat = []
for mu, e in enumerate(EMU):
    T = np.zeros((N, N), dtype=np.int64)
    for x in sites():
        xp = tuple((x[k] + e[k]) % L for k in range(3))
        T[idx(*xp), idx(*x)] = 1
    Tmat.append(T)
T1, T2, T3 = Tmat


def matpow(M, p):
    return np.linalg.matrix_power(M, p).astype(np.int64)


check(
    "A.5",
    "translations are commuting permutation matrices of order 4",
    all(np.array_equal(T.T @ T, np.eye(N, dtype=np.int64)) for T in Tmat)
    and all(np.array_equal(matpow(T, 4), np.eye(N, dtype=np.int64)) for T in Tmat)
    and all(
        np.array_equal(Tmat[a] @ Tmat[b], Tmat[b] @ Tmat[a])
        for a in range(3)
        for b in range(3)
    ),
)

# hw=1 slots ordered so slot mu carries T_mu eigenvalue -1: columns 1,2,3 of V8
V = V8[:, 1:4]
char_ok = True
for mu, T in enumerate(Tmat):
    TV = T @ V
    for j in range(3):
        expect = -1 if j == mu else 1
        if not np.array_equal(TV[:, j], expect * V[:, j]):
            char_ok = False
check(
    "A.6",
    "hw=1 joint translation characters are exactly "
    "(-1,+1,+1), (+1,-1,+1), (+1,+1,-1)",
    char_ok,
)

# U_R: (U_R f)(x) = f(R^{-1} x) with R^{-1}(x1,x2,x3) = (x2,x3,x1)
UR = np.zeros((N, N), dtype=np.int64)
for x in sites():
    xr = (x[1], x[2], x[0])
    UR[idx(*x), idx(*xr)] = 1

check(
    "A.7",
    "U_R is a permutation matrix with U_R^3 = I",
    np.array_equal(UR.T @ UR, np.eye(N, dtype=np.int64))
    and np.array_equal(matpow(UR, 3), np.eye(N, dtype=np.int64)),
)
check(
    "A.8",
    "U_R conjugates translations cyclically: U_R T_mu U_R^T = T_{mu+1 mod 3}",
    all(np.array_equal(UR @ Tmat[mu] @ UR.T, Tmat[(mu + 1) % 3]) for mu in range(3)),
)

CINT = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=np.int64)
check(
    "A.9",
    "landed kernel action: U_R V = V C exactly (C = [[0,0,1],[1,0,0],[0,1,0]])",
    np.array_equal(UR @ V, V @ CINT),
)

# ---------------------------------------------------------------------------
# B1: T1 -- lattice delivery of the presentation-swap rotation (items a-g)
# ---------------------------------------------------------------------------

# swap rotation R2(x1,x2,x3) = (-x2,-x1,-x3) mod 4; site matrix M (column action)
M = np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]], dtype=np.int64)


def R2(x):
    return ((-x[1]) % L, (-x[0]) % L, (-x[2]) % L)


Msym = Matrix(M.tolist())
axis = np.array([1, -1, 0], dtype=np.int64)
row_ok = all(np.count_nonzero(M[i, :]) == 1 for i in range(3))
col_ok = all(np.count_nonzero(M[:, j]) == 1 for j in range(3))
check(
    "B1.1",
    "M is a PROPER signed-permutation involution (det +1, M^T M = I, M^2 = I, "
    "one nonzero per row/col in {-1,0,1}): an element of the cubic rotation group O",
    Msym.det() == 1
    and np.array_equal(M @ M.T, np.eye(3, dtype=np.int64))
    and np.array_equal(M @ M, np.eye(3, dtype=np.int64))
    and row_ok
    and col_ok
    and set(np.unique(M)) <= {-1, 0, 1},
)
check(
    "B1.2",
    "R2 fixes the [1,-1,0] axis (M [1,-1,0]^T = [1,-1,0]^T): the pi-rotation "
    "about [1,-1,0]",
    np.array_equal(M @ axis, axis),
)
check(
    "B1.3",
    "group relation R2 R3 R2 = R3^{-1}: M C M = C^T exactly",
    np.array_equal(M @ CINT @ M, CINT.T),
)

# lattice unitary U2[idx(x), idx(R2 x)] = 1 (R2 is an involution, so R2inv = R2)
U2 = np.zeros((N, N), dtype=np.int64)
for x in sites():
    U2[idx(*x), idx(*R2(x))] = 1

check(
    "B1.4",
    "U2 is a symmetric permutation involution (U2 = U2^T, U2 U2 = I_N)",
    np.array_equal(U2, U2.T)
    and np.array_equal(U2 @ U2, np.eye(N, dtype=np.int64)),
)
check(
    "B1.5",
    "U2 U_R U2 = U_R^T exactly (the swap conjugates the C_3[111] rotation to "
    "its inverse)",
    np.array_equal(U2 @ UR @ U2, UR.T),
)
check(
    "B1.6",
    "translation conjugacy: U2 T1 U2 = T2^3, U2 T2 U2 = T1^3, U2 T3 U2 = T3^3 "
    "(translation by M e_mu; -e_mu = 3 e_mu mod 4)",
    np.array_equal(U2 @ T1 @ U2, matpow(T2, 3))
    and np.array_equal(U2 @ T2 @ U2, matpow(T1, 3))
    and np.array_equal(U2 @ T3 @ U2, matpow(T3, 3)),
)

# sign-free corner-wave covariance: U2 V8 = V8 PI, PI a pure subset permutation
SUB_INDEX = {S: i for i, S in enumerate(SUBSETS)}


def sigma_subset(S):
    swap = {0: 1, 1: 0, 2: 2}
    return tuple(sorted(swap[a] for a in S))


PI = np.zeros((8, 8), dtype=np.int64)
for j, S in enumerate(SUBSETS):
    PI[SUB_INDEX[sigma_subset(S)], j] = 1

pi_perm = all(PI[:, j].sum() == 1 for j in range(8)) and all(
    PI[i, :].sum() == 1 for i in range(8)
)
check(
    "B1.7",
    "sign-free corner-wave covariance: U2 V8 = V8 PI with PI a pure subset "
    "permutation (every entry in {0,1}; (0,)<->(1,), (0,2)<->(1,2), (2,) fixed)",
    np.array_equal(U2 @ V8, V8 @ PI)
    and set(np.unique(PI)) <= {0, 1}
    and pi_perm
    and PI[SUB_INDEX[(1,)], SUB_INDEX[(0,)]] == 1
    and PI[SUB_INDEX[(0,)], SUB_INDEX[(1,)]] == 1
    and PI[SUB_INDEX[(2,)], SUB_INDEX[(2,)]] == 1,
)

TS = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=np.int64)
check(
    "B1.8",
    "hw=1 kernel action: U2 V = V TS with TS the transposition swapping the "
    "(0,) and (1,) corner waves",
    np.array_equal(U2 @ V, V @ TS),
)
check(
    "B1.9",
    "T1 rejector: TS != I3 and TS C TS != C -- the delivered action genuinely "
    "moves C on the triplet",
    (not np.array_equal(TS, np.eye(3, dtype=np.int64)))
    and (not np.array_equal(TS @ CINT @ TS, CINT)),
)

# negative control: trivial-restriction proper rotation R2b = diag(-1,-1,1)
R2b_mat = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]], dtype=np.int64)


def R2b(x):
    return ((-x[0]) % L, (-x[1]) % L, x[2])


U2b = np.zeros((N, N), dtype=np.int64)
for x in sites():
    U2b[idx(*x), idx(*R2b(x))] = 1

check(
    "B1.10",
    "trivial-restriction control: R2b = diag(-1,-1,1) is PROPER (det +1) yet "
    "restricts to the identity on the hw=1 triplet (U2b V = V) while moving "
    "sites (U2b != I_N): properness alone does not deliver the swap",
    Matrix(R2b_mat.tolist()).det() == 1
    and np.array_equal(U2b @ V, V)
    and (not np.array_equal(U2b, np.eye(N, dtype=np.int64))),
)

# improper-honesty gate: bare mirror x1<->x2 has det -1, not in the proper set
S12 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=np.int64)
check(
    "B1.11",
    "improper-honesty: the bare coordinate mirror S12 (x1<->x2) has det -1 "
    "(not in the axiom's proper rotation set), while the swap M has det +1 "
    "(proper): no improper element is consumed",
    Matrix(S12.tolist()).det() == -1 and Msym.det() == 1,
)

# ---------------------------------------------------------------------------
# B2: T2 -- rotation conjugation equals entrywise conjugation on the projector
#     family (items h-l), exact symbolic
# ---------------------------------------------------------------------------

C3 = Matrix(CINT.tolist())
TSs = Matrix(TS.tolist())

check(
    "B2.1",
    "TS C TS = C^T = C^2 exactly, and C is real (conj C = C)",
    (TSs * C3 * TSs == C3.T)
    and (C3.T == C3**2)
    and mat_zero(conjugate(C3) - C3),
)

w = Rational(-1, 2) + sqrt(3) / 2 * I
wb = conjugate(w)
CHI = [sp.Integer(1), w, wb]


def proj(chi, G):
    P = (eye(3) + conjugate(chi) * G + conjugate(chi) ** 2 * G**2) / 3
    return P.applyfunc(lambda e: sp.expand_complex(sp.expand(e)))


P = {chi: proj(chi, C3) for chi in CHI}

check(
    "B2.2",
    "TS P_chi TS = conj(P_chi) for all three channels: rotation conjugation "
    "acts on the supplied projector family identically to entrywise K",
    all(mat_zero(TSs * P[chi] * TSs - conjugate(P[chi])) for chi in CHI),
)
check(
    "B2.3",
    "in particular TS P_w TS = P_wbar and TS P_1 TS = P_1, and the map is "
    "nontrivial (P_w != P_wbar)",
    mat_zero(TSs * P[w] * TSs - P[wb])
    and mat_zero(TSs * P[sp.Integer(1)] * TSs - P[sp.Integer(1)])
    and (not mat_zero(P[w] - P[wb])),
)
check(
    "B2.4",
    "generator coherence: P_wbar(C) = P_w(C^2) symbolically (the rotated pair "
    "is the entrywise-conjugate model presented with its natural generator)",
    mat_zero(proj(wb, C3) - proj(w, C3**2)),
)
check(
    "B2.5",
    "conj(TS) = TS (real rotation); the antilinear involution "
    "M -> conj(TS M TS) fixes every P_chi and is nontrivial (moves C to C^2)",
    mat_zero(conjugate(TSs) - TSs)
    and all(mat_zero(conjugate(TSs * P[chi] * TSs) - P[chi]) for chi in CHI)
    and (not mat_zero(conjugate(TSs * C3 * TSs) - C3)),
)

pa, pb, pc = sp.symbols("pa pb pc", commutative=True)
Wp = pa * eye(3) + pb * C3 + pc * C3**2
check(
    "B2.6",
    "probe transform: TS W(a,b,c) TS = W(a,c,b) (the swap exchanges the b and c "
    "generator coefficients)",
    mat_zero(TSs * Wp * TSs - (pa * eye(3) + pc * C3 + pb * C3**2)),
)

# ---------------------------------------------------------------------------
# B3: T3 -- the corner-projector pair is a proper-rotation orbit; canonical K-odd
#     separator (orbit statement + item p), exact symbolic
# ---------------------------------------------------------------------------

check(
    "B3.1",
    "the corner-projector pair {P_w, P_wbar} is a single 2-orbit under the delivered "
    "proper rotation: TS P_w TS = P_wbar, TS P_wbar TS = P_w, TS P_1 TS = P_1",
    mat_zero(TSs * P[w] * TSs - P[wb])
    and mat_zero(TSs * P[wb] * TSs - P[w])
    and mat_zero(TSs * P[sp.Integer(1)] * TSs - P[sp.Integer(1)]),
)
check(
    "B3.2",
    "the rotation orbit coincides with the entrywise-conjugation orbit: "
    "TS P_chi TS = conj(P_chi) is the same partition of the projector family",
    all(mat_zero(TSs * P[chi] * TSs - conjugate(P[chi])) for chi in CHI),
)

D0 = P[w] - P[wb]
check(
    "B3.3",
    "canonical K-odd separator D0 = P_w - P_wbar: nonzero, conj(D0) = -D0 "
    "(K-odd), and TS D0 TS = -D0 = conj(D0) -- the delivered rotation exchanges "
    "the canonical K-odd seed exactly as K does",
    (not mat_zero(D0))
    and mat_zero(conjugate(D0) + D0)
    and mat_zero(TSs * D0 * TSs + D0)
    and mat_zero(TSs * D0 * TSs - conjugate(D0)),
)
check(
    "B3.4",
    "the rotation image (C^2 with its natural w-channel projector) reproduces "
    "the conjugate corner model: P_w(C^2) = P_wbar(C), so the orbit image is "
    "the corner-projector restriction of the FLAG's entrywise-conjugate presentation",
    mat_zero(proj(w, C3**2) - proj(wb, C3)),
)

# ---------------------------------------------------------------------------
# B4: T4 -- K-parity equals rotation parity on the Hermitian section;
#     off-section inequivalence witnesses (items m, n, o), exact symbolic
# ---------------------------------------------------------------------------

a, b, c = sp.symbols("a b c", commutative=True)
Wabc = a * eye(3) + b * C3 + c * C3**2
lam1 = a + b + c
lam_w = a + b * w + c * w**2
lam_wb = a + b * wb + c * wb**2
check(
    "B4.1",
    "channel values: W(a,b,c) P_chi = lam_chi P_chi with lam_chi = a + b*chi + "
    "c*chi^2; the doublet separation is lam_w - lam_wbar = i*sqrt(3)*(b-c) exactly",
    mat_zero(Wabc * P[sp.Integer(1)] - lam1 * P[sp.Integer(1)])
    and mat_zero(Wabc * P[w] - lam_w * P[w])
    and mat_zero(Wabc * P[wb] - lam_wb * P[wb])
    and is_zero(lam_w - lam_wb - I * sqrt(3) * (b - c)),
)

Wswap = a * eye(3) + c * C3 + b * C3**2  # W(a,c,b)
lam_w_s = a + c * w + b * w**2
lam_wb_s = a + c * wb + b * wb**2
check(
    "B4.2",
    "under the swap b<->c: lam_1 fixed and the doublet pair is exchanged, "
    "lam_w(W(a,c,b)) = lam_wbar(W(a,b,c)) and lam_wbar(W(a,c,b)) = lam_w(W(a,b,c))",
    is_zero(lam_w_s - lam_wb)
    and is_zero(lam_wb_s - lam_w)
    and is_zero((a + c + b) - lam1),
)

b1, b2, ah = sp.symbols("b1 b2 ah", real=True)
bH = b1 + I * b2
WH = ah * eye(3) + bH * C3 + conjugate(bH) * C3**2
check(
    "B4.3",
    "Hermitian-section coincidence (keystone): with b = b1 + i*b2, "
    "W_H = a*I + b*C + conj(b)*C^2 satisfies conj(W_H) = TS W_H TS exactly -- on "
    "the Hermitian section the antilinear K-exchange IS conjugation by the "
    "delivered proper rotation",
    mat_zero(conjugate(WH) - TSs * WH * TSs),
)

skew = C3 - C3**2
sep_skew = (a + b * w + c * w**2 - (a + b * wb + c * wb**2)).subs(
    {a: 0, b: 1, c: -1}
)
check(
    "B4.4",
    "off-section witness skew = C - C^2: K-EVEN (conj skew = skew) but "
    "rotation-ODD (TS skew TS = -skew), and it separates the doublet "
    "(lam_w - lam_wbar = 2*i*sqrt(3) != 0)",
    mat_zero(conjugate(skew) - skew)
    and mat_zero(TSs * skew * TSs + skew)
    and is_zero(sep_skew - 2 * I * sqrt(3))
    and (not is_zero(sep_skew)),
)

cImag = I * eye(3)
check(
    "B4.5",
    "off-section witness i*I: K-ODD (conj = -it) but rotation-EVEN "
    "(TS (i*I) TS = i*I), and it does NOT separate (all channel values equal)",
    mat_zero(conjugate(cImag) + cImag)
    and mat_zero(TSs * cImag * TSs - cImag)
    and is_zero(sp.trace(P[w] * cImag) - sp.trace(P[wb] * cImag)),
)
check(
    "B4.6",
    "the two gradings are inequivalent off the Hermitian section: "
    "conj(skew) != TS skew TS and conj(i*I) != TS (i*I) TS, while on the section "
    "conj(W_H) = TS W_H TS (item n) -- K-parity and rotation-parity coincide only "
    "on the Hermitian section",
    (not mat_zero(conjugate(skew) - TSs * skew * TSs))
    and (not mat_zero(conjugate(cImag) - TSs * cImag * TSs))
    and mat_zero(conjugate(WH) - TSs * WH * TSs),
)
DeltaW = conjugate(Wabc) - TSs * Wabc * TSs
check(
    "B4.7",
    "exact section characterization: for general complex (a,b,c), "
    "conj(W) - TS W TS = (conj(a)-a) I + (conj(b)-c) C + (conj(c)-b) C^2, and "
    "{I, C, C^2} are linearly independent (rank 3); hence conj(W) = TS W TS "
    "holds iff a is real and c = conj(b) -- exactly the Hermitian section, "
    "and only there",
    mat_zero(
        DeltaW
        - (
            (conjugate(a) - a) * eye(3)
            + (conjugate(b) - c) * C3
            + (conjugate(c) - b) * C3**2
        )
    )
    and sp.Matrix.hstack(
        eye(3).reshape(9, 1), C3.reshape(9, 1), (C3**2).reshape(9, 1)
    ).rank()
    == 3,
)

sigma2 = Matrix([[0, -I], [I, 0]])
joint_sigma2 = sp.kronecker_product(sigma2, eye(3))
joint_rotation = sp.kronecker_product(eye(2), TSs)
check(
    "B4.8",
    "joint-surface escape: sigma_2 tensor I_3 is K-ODD but fixed by the natural "
    "joint lift I_2 tensor TS, so the corner-projector orbit does not implement "
    "the mechanism note's full Pauli/corner entrywise-conjugation action",
    mat_zero(conjugate(joint_sigma2) + joint_sigma2)
    and mat_zero(joint_rotation * joint_sigma2 * joint_rotation - joint_sigma2),
)

# ---------------------------------------------------------------------------
# B5: r-neutrality guard (item q), exact symbolic
# ---------------------------------------------------------------------------

sum_pair = lam_w + lam_wb
prod_pair = lam_w * lam_wb
sum_pair_s = lam_w_s + lam_wb_s
prod_pair_s = lam_w_s * lam_wb_s
check(
    "B5.1",
    "the swap fixes lam_1 and permutes {lam_w, lam_wbar}: the elementary "
    "symmetric functions lam_w + lam_wbar and lam_w * lam_wbar are swap-invariant",
    is_zero(sum_pair_s - sum_pair) and is_zero(prod_pair_s - prod_pair),
)
check(
    "B5.2",
    "the swap genuinely moves the individual doublet values "
    "(lam_w(W(a,c,b)) - lam_w(W(a,b,c)) is not identically zero) while fixing "
    "their symmetric functions: the invariance is of the pair, not of a pinned "
    "value; no target weight r is referenced, forced, derived, or selected",
    not is_zero(lam_w_s - lam_w),
)
check(
    "B5.3",
    "the singlet channel value lam_1 = a + b + c is swap-invariant (fixed): the "
    "guard references no weight value",
    is_zero((a + c + b) - lam1),
)

# ---------------------------------------------------------------------------
# B6: T5 -- operator-level covariance report for the named dressed class
#     (honest computed report; consumed by no other claim)
# ---------------------------------------------------------------------------


def commutes(U):
    return np.array_equal(U @ D2, D2 @ U)


check(
    "B6.1",
    "computed undressed status: U2 does NOT commute with D2 (the swap needs a "
    "sign dressing to be a D operator symmetry)",
    not commutes(U2),
)
check(
    "B6.2",
    "computed undressed status: U_R does NOT commute with D2 (the C_3[111] "
    "rotation needs a sign dressing to be a D operator symmetry)",
    not commutes(UR),
)


def sign_diag(bits):
    a1, a2, a3, b12, b13, b23 = bits
    d = np.empty(N, dtype=np.int64)
    for x in sites():
        e = (
            a1 * x[0]
            + a2 * x[1]
            + a3 * x[2]
            + b12 * x[0] * x[1]
            + b13 * x[0] * x[2]
            + b23 * x[1] * x[2]
        )
        d[idx(*x)] = -1 if (e & 1) else 1
    return d


SIGN_FIELDS = list(itertools.product((0, 1), repeat=6))  # 64 sign fields
SIGN_DIAGS = [sign_diag(bits) for bits in SIGN_FIELDS]
TRANS_LIST = [
    (t, matpow(T1, t[0]) @ matpow(T2, t[1]) @ matpow(T3, t[2]))
    for t in itertools.product(range(L), repeat=3)
]  # 64 lattice translations


def dressed_search(base):
    visited = 0
    sols = []
    for bits, dg in zip(SIGN_FIELDS, SIGN_DIAGS):
        Sbase = (dg[:, None] * base).astype(np.int64)
        for t, Tt in TRANS_LIST:
            U = (Sbase @ Tt).astype(np.int64)
            visited += 1
            if np.array_equal(U @ D2, D2 @ U):
                sols.append((bits, t, U))
    return visited, sols


def triplet_compression(U):
    return V.T @ U @ V


def preserves_triplet(U):
    # V^T V = 64 I, so P = V V^T / 64 is the orthogonal projector onto
    # span(V); U preserves span(V) iff P U V = U V, i.e. 64 U V = V (V^T U V),
    # checked here in exact integer arithmetic.
    return np.array_equal(64 * (U @ V), V @ (V.T @ U @ V))


def first_flip_breaks(bits, t):
    Tt = dict(TRANS_LIST)[t]
    for bi in range(6):
        fb = list(bits)
        fb[bi] ^= 1
        Uf = (sign_diag(tuple(fb))[:, None] * (INT_BASE @ Tt)).astype(np.int64)
        if not commutes(Uf):
            return True, tuple(fb)
    return False, None


for label, base in (("U2", U2), ("UR", UR)):
    INT_BASE = base
    visited, sols = dressed_search(base)
    count = len(sols)
    preserve_count = sum(1 for (_, _, U) in sols if preserves_triplet(U))
    id_comm = base @ D2 - D2 @ base
    id_nnz = int(np.count_nonzero(id_comm))
    b0 = 3 if label == "U2" else 10
    check(
        f"B6.{b0}",
        f"{label} dressed search visited exactly 4096 candidates "
        "(64 sign fields x 64 translations)",
        visited == 4096,
    )
    check(
        f"B6.{b0 + 1}",
        f"{label} dressed class solution count is exactly 64 (computed live)",
        count == 64,
    )
    bits0, t0, U0 = sols[0]
    check(
        f"B6.{b0 + 2}",
        f"{label} exemplar re-check: the reported exemplar commutes with D2",
        commutes(U0),
    )
    check(
        f"B6.{b0 + 3}",
        f"{label} exemplar preserves the full 8-dim corner-wave kernel "
        "(D2 U V8 = 0) but does NOT preserve the hw=1 triplet subspace "
        "(the off-triplet residual 64*U V - V (V^T U V) is nonzero)",
        np.array_equal(D2 @ U0 @ V8, np.zeros((N, 8), dtype=np.int64))
        and (not preserves_triplet(U0)),
    )
    check(
        f"B6.{b0 + 4}",
        f"{label} class-scoped count: no member of the named 4096-candidate "
        "dressed class preserves the hw=1 triplet subspace "
        "(0 of 64 -- computed live)",
        preserve_count == 0,
    )
    flip_breaks, flip_bits = first_flip_breaks(bits0, t0)
    check(
        f"B6.{b0 + 5}",
        f"{label} discriminating rejector: a one-bit flip of the exemplar sign "
        "field FAILS to commute with D2",
        flip_breaks,
    )
    check(
        f"B6.{b0 + 6}",
        f"{label} check is live: the identity dressing (s=0, t=0) has a nonzero "
        "commutator with D2",
        id_nnz > 0,
    )
    print(
        f"B6 REPORT {label}: undressed_commutes={commutes(base)}; "
        f"visited={visited}; solutions={count}; triplet_preserving={preserve_count}; "
        f"identity_dressing_commutator_nonzero_entries={id_nnz}"
    )
    print(
        f"B6 REPORT {label} exemplar: (a1,a2,a3,b12,b13,b23)={bits0}; "
        f"t={t0}; one_bit_flip_breaks={flip_bits}; "
        f"compression V^T U V = {triplet_compression(U0).tolist()}"
    )

# ---------------------------------------------------------------------------
# B7: verbatim quote gates (Q1-Q6)
# ---------------------------------------------------------------------------

NEEDLE_Q1 = (
    "**R2 — K-real derivable initial data.** Derivable initial data is K-real. "
    "**FLAG — two-model mechanism:** the entrywise-conjugate presentations in "
    "L-K2 satisfy the same named clauses and exchange every K-odd seed. The "
    "memo's live Qualification leaves the unfixed choice conditional/open."
)
NEEDLE_R1C = (
    "The real cyclic `C` with `C^3 = I_3` and `C^T = C^2`, the character "
    "projectors `P_chi = (I + conj(chi)*C + conj(chi)^2*C^2)/3` for "
    "`chi in {1, w, conj(w)}`, `w = -1/2 + (sqrt(3)/2)*i`, and entrywise "
    "conjugation `K` in the canonical basis."
)
NEEDLE_FLAG = (
    "**FLAG — supplied surface:** this is the mechanism note's declared "
    "corner surface, not a derived physical carrier."
)
NEEDLE_AX1 = (
    "Physical sites are the points of the cubic lattice `Z^3`, with "
    "nearest-neighbor adjacency, standard translations, and proper cubic "
    "rotations about each site."
)
NEEDLE_AX2 = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under "
    "lattice translations and proper cubic rotations."
)
NEEDLE_DELIV = (
    "the `C_3[111]` lattice rotation restricted to the hw=1 kernel triplet of "
    "the one-component staggered operator on the periodic `4^3` torus IS the "
    "real cyclic `C` (entries exactly `{0,1}`, `C^3 = I`, `C^T = C^2`), and "
    "ambient complex conjugation restricts to entrywise conjugation `K` in the "
    "corner basis (T1)."
)

note_groups = quote_groups(NOTE)

check("B7.1", "mechanism note carries the R2 + two-model FLAG passage", NEEDLE_Q1 in flattened(MECH))
check("B7.2", "note blockquotes the R2 + two-model FLAG passage", in_groups(note_groups, NEEDLE_Q1))
check("B7.3", "spectral-pairing note carries the R1c supplied-carrier sentence", NEEDLE_R1C in flattened(BLOCK05))
check("B7.4", "note blockquotes the R1c supplied-carrier sentence", in_groups(note_groups, NEEDLE_R1C))
check("B7.5", "spectral-pairing note carries the supplied-surface FLAG sentence", NEEDLE_FLAG in flattened(BLOCK05))
check("B7.6", "note blockquotes the supplied-surface FLAG sentence", in_groups(note_groups, NEEDLE_FLAG))
check("B7.7", "minimal-axioms note carries the proper-rotation Lattice sentence", NEEDLE_AX1 in flattened(AXIOMS))
check("B7.8", "note blockquotes the proper-rotation Lattice sentence", in_groups(note_groups, NEEDLE_AX1))
check("B7.9", "minimal-axioms note carries the proper-rotation Admissibility sentence", NEEDLE_AX2 in flattened(AXIOMS))
check("B7.10", "note blockquotes the proper-rotation Admissibility sentence", in_groups(note_groups, NEEDLE_AX2))
check("B7.11", "delivery note carries the landed hw=1 carrier-delivery sentence", NEEDLE_DELIV in flattened(DELIVERY))
check("B7.12", "note blockquotes the landed hw=1 carrier-delivery sentence", in_groups(note_groups, NEEDLE_DELIV))

# ---------------------------------------------------------------------------
# B8: ledger shard filename gates (timeless: existence only)
# ---------------------------------------------------------------------------

ROWS = [
    "minimal_axioms",
    "staggered_dirac_realization_gate_note_2026-05-03",
    "kcpt_coupling_triple_two_presentation_derivable_class_spectral_pairing_bounded_theorem_note_2026-07-16",
    "kcpt_orbit_constant_registered_occupancy_weights_derivable_protocol_class_bounded_theorem_note_2026-07-12",
    "kcpt_corner_carrier_lattice_delivery_hw1_doublet_pair_polarization_bounded_theorem_note_2026-07-17",
    "acphilambda_c3_resolvent_determinant_holonomy_coupling_narrow_theorem_note_2026-07-12",
    "acphilambda_fermionic_realification_pfaffian_power_identity_narrow_theorem_note_2026-07-12",
]
for i, rid in enumerate(ROWS, 1):
    shard = ROOT / "docs" / "audit" / "data" / "ledger" / rid[:2] / f"{rid}.json"
    check(f"B8.{i}", f"ledger shard file exists: {rid}", shard.is_file())

# ---------------------------------------------------------------------------
# B9: note hygiene
# ---------------------------------------------------------------------------

RAW = (ROOT / NOTE).read_text(encoding="utf-8")
B9_N = 0

SECTIONS = [
    "## Purpose",
    "## Supplied objects and consumed readings",
    "## Claims",
    "### Lattice delivery of the presentation-swap rotation (T1, exact)",
    "### Rotation conjugation equals entrywise conjugation on the supplied projector family (T2, exact)",
    "### The corner-projector pair is a proper-rotation orbit on the delivered carrier (T3, exact)",
    "### K-parity equals rotation parity on the Hermitian section (T4, exact)",
    "### Operator-level covariance report for the named dressed class (T5, computed report)",
    "## Gated controls",
    "## Negative controls",
    "## No-Go Discipline Gate",
    "### N1 —",
    "### N2 —",
    "### N3 —",
    "### N4 —",
    "### N5 —",
    "### N6 —",
    "### N7 —",
    "### N8 —",
    "## Non-claims",
    "## Dependency roles and status boundary",
    "## Dependencies",
    "### Non-citation context handles",
    "## Verification",
    "Statuses of all dependencies are set by the independent audit lane; this note asserts no dependency status and consumes no status-dependent content.",
    "**No check passes by literal stipulation.**",
    "**Status authority:** independent audit lane only.",
    "Context orientation only; no content is consumed from either.",
    "entrywise-conjugate corner-projector pair is exchanged by an",
    "Pauli/corner orbit of the mechanism note: under the natural joint lift",
    "`sigma_2 tensor I_3` is fixed by rotation conjugation but is K-odd.",
    "Qualification remains live and unfixed; this note does not act on that slot.",
]
for s in SECTIONS:
    B9_N += 1
    check(f"B9.{B9_N}", f"note carries: {s[:60]}", s in RAW)

FORBIDDEN = [
    "exhaust",
    "only route",
    "last route",
    "bijection",
    "final",
    "forces r",
    "derives r",
    "selects r",
    "retained",
    "discharge",
    "derived carrier",
    "dissolv",
    "retire",
    "closes the",
]
RAW_LOW = RAW.lower()
for phrase in FORBIDDEN:
    B9_N += 1
    check(f"B9.{B9_N}", f"forbidden phrase absent: '{phrase}'", phrase not in RAW_LOW)

STATUS_SNAPSHOTS = [
    "unaudited at writing",
    "citation grades at writing",
    "audited_renaming",
    "honest auditor read",
]
for phrase in STATUS_SNAPSHOTS:
    B9_N += 1
    check(
        f"B9.{B9_N}",
        f"source-authored status/value snapshot absent: '{phrase}'",
        phrase not in RAW_LOW,
    )

B9_N += 1
check(
    f"B9.{B9_N}",
    "no bare decimal literals in the note",
    re.search(r"\d\.\d", RAW) is None,
)

DEPS = [
    "MINIMAL_AXIOMS_2026-06-29.md",
    "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md",
    "KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md",
    "KCPT_ORBIT_CONSTANT_REGISTERED_OCCUPANCY_WEIGHTS_DERIVABLE_PROTOCOL_CLASS_BOUNDED_THEOREM_NOTE_2026-07-12.md",
    "KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md",
]
for dep in DEPS:
    B9_N += 1
    check(f"B9.{B9_N}", f"markdown dependency link present: {dep}", f"]({dep})" in RAW)

CONTEXT_HANDLES = [
    "ACPHILAMBDA_C3_RESOLVENT_DETERMINANT_HOLONOMY_COUPLING_NARROW_THEOREM_NOTE_2026-07-12.md",
    "ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md",
]
for handle in CONTEXT_HANDLES:
    B9_N += 1
    check(
        f"B9.{B9_N}",
        f"non-citation context handle is backticked and unlinked: {handle}",
        f"`{handle}`" in RAW and f"]({handle})" not in RAW,
    )

B9_N += 1
check(
    f"B9.{B9_N}",
    "every cited or handled doc path exists",
    all((ROOT / p).is_file() for p in [NOTE, RUNNER, AXIOMS, GATE, BLOCK05, MECH, DELIVERY])
    and all((ROOT / "docs" / h).is_file() for h in CONTEXT_HANDLES)
    and all((ROOT / "docs" / d).is_file() for d in DEPS),
)

# ------------------------------------------------------------------ summary
print(f"PATH note={NOTE}")
print(f"PATH runner={RUNNER}")
print(f"PATH cache={CACHE}")
print(
    "FLAGS: T1 delivers the corner-projector restriction of the mechanism note's "
    "two-presentation swap as the proper "
    "pi-rotation about [1,-1,0] (det M = +1) on the same 4^3 staggered surface as "
    "the landed hw=1 carrier, using the landed delivery standard (translation "
    "conjugacy + kernel action); T2-T4 show rotation conjugation equals entrywise "
    "conjugation on the supplied projector family and coincides with the antilinear "
    "K-exchange exactly on the Hermitian section, with off-section inequivalence "
    "witnesses; the full Pauli/corner presentation has the exact joint-factor escape "
    "sigma_2 tensor I_3 and is not reclassified; the note does not fix the mechanism's "
    "presentation choice and does not act on the memo's live Qualification slot; "
    "B5 is weight-neutral (no weight r is referenced, forced, derived, or selected); "
    "the corner surface remains the mechanism note's supplied surface (inherited FLAG)"
)
print(
    "RESIDUAL (declared-open, inherited): the mechanism note's live Qualification "
    "leaves the presentation orientation conditional/open; this note does not act on it"
)
print(
    "RESIDUAL (declared-open, inherited): the corner surface is the mechanism note's "
    "supplied surface, not a physically derived carrier"
)
print(
    "T5 REPORT (computed, consumed by no other claim): undressed U2 does not commute "
    "with D2; undressed U_R does not commute with D2; the named 4096-candidate dressed "
    "class contains 64 commuting members for U2 and 64 for U_R; none of the 64 members "
    "in either class preserves the hw=1 triplet subspace (0 of 64 each); "
    "one-bit sign-field flips of the exemplars break commutation (discriminating "
    "rejectors); the identity dressings have nonzero commutators with D2"
)
if FAILURES:
    print("FAILED CHECKS: " + ", ".join(FAILURES))
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
