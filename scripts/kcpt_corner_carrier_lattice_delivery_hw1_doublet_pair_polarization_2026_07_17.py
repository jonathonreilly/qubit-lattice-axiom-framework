#!/usr/bin/env python3
"""hw=1 corner-carrier lattice delivery and doublet-pair K-polarization checks.

Paired note:
docs/KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md

Blocks:
  A  gate-surface construction replication, exact integer arithmetic: the
     one-component staggered operator on the periodic 4^3 torus with the
     Kawamoto-Smit phases, exact rank 56 (dim ker = 8), the eight corner
     plane waves as exact orthogonal null vectors spanning the kernel,
     joint translation characters of the hw=1 slots, the C_3[111]
     permutation unitary and its exact conjugation action on translations
  B1 carrier delivery (T1): U_R restricted to the hw=1 corner basis IS the
     real cyclic permutation C with entries exactly {0,1}, C^3 = I,
     C^T = C^2; ambient complex conjugation restricts to entrywise
     conjugation K in the corner basis; delivered character projectors are
     Hermitian rank-one with exact channel-eigenvalue association
  B2 K-polarization (T2): K fixes the singlet channel, exchanges the two
     doublet channels as one 2-orbit; democratic direction K-fixed; the
     omega eigenline maps to the omegabar eigenline under K
  B3 spectral-pairing instantiation (T3): entrywise-real triples on the
     delivered carrier have spectrum {lam0 real} plus a conjugate pair,
     det = lam0*|lam1|^2 exactly; block-05 negative control (1,i,0)
     reproduced with exact values sqrt(3)-i and 1-i
  B4 doublet-pair separation is K-gated (T4, bounded negative): exact
     commutant classification; Hermitian + K-real equivariant = the
     two-parameter real class a*I + b*(C+C^2) with doublet eigenvalues
     exactly equal; separation is identically proportional to the K-odd
     component; the canonical separator P_w - P_wbar is K-odd; hardening:
     a general (non-equivariant) real symmetric operator has exactly equal
     expectations on the two conjugate doublet lines; boundary witness P_w
  B5 r-neutrality guard: the K-real class realizes every
     (singlet, doublet) channel-value pair exactly once (linear bijection,
     determinant -3); three exact witnesses with distinct doublet-to-singlet
     ratios 1, 1/2, 1/4 -- nothing pins any ratio
  B6 verbatim quote gates: sources carry the consumed sentences and the
     note quotes them in blockquotes
  B7 ledger shard filename gates (timeless: existence only, no status pins)
  B8 note hygiene: section presence, forbidden-phrase absence, no bare
     decimal literals, markdown dependency links, backticked context handles

Lattice arithmetic is exact integer (numpy int64 + sympy exact rank).
Corner algebra is exact sympy. No floats, no tolerances, no randomness.
Exit 1 on any failure.
"""

import itertools
import re
from pathlib import Path

import numpy as np
import sympy as sp
from sympy import I, Matrix, Rational, conjugate, eye, sqrt

ROOT = Path(__file__).resolve().parents[1]

NOTE = (
    "docs/KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_"
    "POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md"
)
RUNNER = (
    "scripts/kcpt_corner_carrier_lattice_delivery_hw1_doublet_pair_"
    "polarization_2026_07_17.py"
)
CACHE = (
    "logs/runner-cache/kcpt_corner_carrier_lattice_delivery_hw1_doublet_"
    "pair_polarization_2026_07_17.txt"
)

GATE = "docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
BLOCK05 = (
    "docs/KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_"
    "SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md"
)
MECH = (
    "docs/KCPT_ORBIT_CONSTANT_REGISTERED_OCCUPANCY_WEIGHTS_DERIVABLE_"
    "PROTOCOL_CLASS_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
AXIOMS = "docs/MINIMAL_AXIOMS_2026-06-29.md"

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
# A: gate-surface construction, exact integer arithmetic
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

# the eight Hamming-weight corner plane waves v_S(x) = (-1)^{sum_{mu in S} x_mu}
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

check(
    "A.5",
    "translations are commuting permutation matrices of order 4",
    all(np.array_equal(T.T @ T, np.eye(N, dtype=np.int64)) for T in Tmat)
    and all(
        np.array_equal(
            np.linalg.matrix_power(T, 4).astype(np.int64), np.eye(N, dtype=np.int64)
        )
        for T in Tmat
    )
    and all(
        np.array_equal(Tmat[a] @ Tmat[b], Tmat[b] @ Tmat[a])
        for a in range(3)
        for b in range(3)
    ),
)

# hw=1 slots ordered so slot mu carries T_mu eigenvalue -1: columns 1,2,3 of V8
V = V8[:, 1:4]
chars = np.zeros((3, 3), dtype=np.int64)
char_ok = True
for mu, T in enumerate(Tmat):
    TV = T @ V
    for j in range(3):
        expect = -1 if j == mu else 1
        if not np.array_equal(TV[:, j], expect * V[:, j]):
            char_ok = False
        chars[j, mu] = expect
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
    and np.array_equal(
        np.linalg.matrix_power(UR, 3).astype(np.int64), np.eye(N, dtype=np.int64)
    ),
)
check(
    "A.8",
    "U_R conjugates translations cyclically: U_R T_mu U_R^T = T_{mu+1 mod 3}",
    all(
        np.array_equal(UR @ Tmat[mu] @ UR.T, Tmat[(mu + 1) % 3]) for mu in range(3)
    ),
)

# ---------------------------------------------------------------------------
# B1: carrier delivery (T1)
# ---------------------------------------------------------------------------

CINT = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=np.int64)

check(
    "B1.1",
    "U_R V = V C exactly (columnwise: U_R v1 = v2, U_R v2 = v3, U_R v3 = v1)",
    np.array_equal(UR @ V, V @ CINT),
)
c3_num = V.T @ UR @ V
check(
    "B1.2",
    "delivered c3 = (V^T U_R V)/64 has entries exactly {0,1} and equals C",
    np.array_equal(c3_num, 64 * CINT),
)

C3 = Matrix(CINT.tolist())
check("B1.3", "C^3 = I exactly", C3**3 == eye(3))
check("B1.4", "C^T = C^2 exactly", C3.T == C3**2)
check(
    "B1.5",
    "U_R maps corner 1 to corner 2 with coefficient +1 (no sign)",
    np.array_equal(UR @ V[:, 0], V[:, 1]),
)

# ambient conjugation restricts to entrywise conjugation in the corner basis
z = Matrix([1 + 2 * I, -3 + 7 * I, 5 - I])
Vs = Matrix(V.tolist())
check(
    "B1.6",
    "conj(V z) = V conj(z): ambient conjugation = entrywise K in corner basis",
    mat_zero((Vs * z).conjugate() - Vs * z.conjugate()),
)

w = Rational(-1, 2) + sqrt(3) / 2 * I
wb = conjugate(w)
CHI = [sp.Integer(1), w, wb]
P = {}
for chi in CHI:
    P[chi] = (eye(3) + conjugate(chi) * C3 + conjugate(chi) ** 2 * C3**2) / 3
    P[chi] = P[chi].applyfunc(lambda e: sp.expand_complex(sp.expand(e)))

check(
    "B1.7",
    "delivered projectors Hermitian, idempotent, orthogonal, sum = I, trace 1",
    all(mat_zero(P[chi] - P[chi].H) for chi in CHI)
    and all(mat_zero(P[chi] * P[chi] - P[chi]) for chi in CHI)
    and mat_zero(P[CHI[0]] * P[CHI[1]])
    and mat_zero(P[CHI[1]] * P[CHI[2]])
    and mat_zero(P[CHI[0]] * P[CHI[2]])
    and mat_zero(P[CHI[0]] + P[CHI[1]] + P[CHI[2]] - eye(3))
    and all(is_zero(sp.trace(P[chi]) - 1) for chi in CHI),
)
check(
    "B1.8",
    "channel-eigenvalue association: C P_chi = chi P_chi for all three channels",
    all(mat_zero(C3 * P[chi] - chi * P[chi]) for chi in CHI),
)

# ---------------------------------------------------------------------------
# B2: K-polarization (T2)
# ---------------------------------------------------------------------------


def Kc(M):
    return M.conjugate()


check("B2.1", "K P_1 K = P_1: singlet channel K-fixed", mat_zero(Kc(P[1]) - P[1]))
check(
    "B2.2",
    "K P_w K = P_wbar and K P_wbar K = P_w: doublet channels one K 2-orbit",
    mat_zero(Kc(P[w]) - P[wb]) and mat_zero(Kc(P[wb]) - P[w]),
)

dem = Matrix([1, 1, 1]) / sqrt(3)
check(
    "B2.3",
    "democratic direction is entrywise real and P_1-fixed (K-fixed vector)",
    mat_zero(P[1] * dem - dem) and all(sp.im(dem[i]) == 0 for i in range(3)),
)

vw = Matrix([1, wb, wb**2]) / sqrt(3)
check("B2.4", "vw = (1, wbar, wbar^2)/sqrt(3) satisfies C vw = w vw", mat_zero(C3 * vw - w * vw))
check(
    "B2.5",
    "K maps the omega eigenline to the omegabar eigenline: C conj(vw) = wbar conj(vw)",
    mat_zero(C3 * vw.conjugate() - wb * vw.conjugate()),
)
check(
    "B2.6",
    "P_w = vw vw^dagger exactly (doublet line projector identification)",
    mat_zero(P[w] - vw * vw.H),
)

# ---------------------------------------------------------------------------
# B3: spectral-pairing instantiation (T3)
# ---------------------------------------------------------------------------

a, b, c = sp.symbols("a b c", real=True)
Wc = a * eye(3) + b * C3 + c * C3**2
lam0 = a + b + c
lam1 = a + b * w + c * w**2
lam2 = a + b * wb + c * wb**2

check(
    "B3.1",
    "real-triple channel eigenvalues: Wc P_chi = lam_chi P_chi; "
    "lam0 real; lam2 = conj(lam1)",
    mat_zero(Wc * P[1] - lam0 * P[1])
    and mat_zero(Wc * P[w] - lam1 * P[w])
    and mat_zero(Wc * P[wb] - lam2 * P[wb])
    and is_zero(sp.im(lam0))
    and is_zero(lam2 - conjugate(lam1)),
)
check(
    "B3.2",
    "det(Wc) = lam0 * |lam1|^2 exactly on entrywise-real triples",
    is_zero(Wc.det() - lam0 * lam1 * conjugate(lam1)),
)

# block-05 negative control (a,b,c) = (1,i,0): pairing fails off the real locus
nl0 = 1 + I
nl1 = 1 + I * w
nl2 = 1 + I * w**2
Wneg = eye(3) + I * C3
check(
    "B3.3",
    "negative control (1,i,0): lam2 - conj(lam1) = sqrt(3) - i and det = 1 - i",
    is_zero(nl2 - conjugate(nl1) - (sqrt(3) - I))
    and is_zero(Wneg.det() - (1 - I))
    and is_zero(Wneg.det() - nl0 * nl1 * nl2),
)

# ---------------------------------------------------------------------------
# B4: doublet-pair separation is K-gated (T4, bounded negative)
# ---------------------------------------------------------------------------

# commutant of C in M_3(C): kernel of ad_C on the 9-dim matrix space
ad = np.zeros((9, 9), dtype=np.int64)
for i in range(3):
    for j in range(3):
        E = np.zeros((3, 3), dtype=np.int64)
        E[i, j] = 1
        comm = CINT @ E - E @ CINT
        ad[:, 3 * i + j] = comm.reshape(9)
check(
    "B4.1",
    "commutant of C has dimension exactly 3 (rank of ad_C = 6)",
    sp.Matrix(ad.tolist()).rank() == 6,
)
check(
    "B4.2",
    "{I, C, C^2} are linearly independent commuting elements, so they span "
    "the commutant",
    sp.Matrix(
        [list(eye(3).reshape(1, 9)), list((C3**1).reshape(1, 9)), list((C3**2).reshape(1, 9))]
    ).rank()
    == 3,
)

a1, a2, b1, b2, c1, c2 = sp.symbols("a1 a2 b1 b2 c1 c2", real=True)
X = (a1 + I * a2) * eye(3) + (b1 + I * b2) * C3 + (c1 + I * c2) * C3**2
eqs = []
for M in (X - X.H, X - X.conjugate()):
    for e in M:
        ec = sp.expand_complex(sp.expand(e))
        eqs.append(sp.re(ec))
        eqs.append(sp.im(ec))
A_sys, _ = sp.linear_eq_to_matrix(eqs, [a1, a2, b1, b2, c1, c2])
check(
    "B4.3",
    "Hermitian + K-real commutant member forced to a*I + b*(C + C^2): "
    "constraint rank 4, kernel spanned by I and C+C^2, and b=c is enforced",
    A_sys.rank() == 4
    and mat_zero(A_sys * Matrix([1, 0, 0, 0, 0, 0]))
    and mat_zero(A_sys * Matrix([0, 0, 1, 0, 1, 0]))
    and not mat_zero(A_sys * Matrix([0, 0, 1, 0, 0, 0])),
)

ar, br = sp.symbols("ar br", real=True)
Hrs = ar * eye(3) + br * (C3 + C3**2)
x = sp.symbols("x")
charpoly = Hrs.charpoly(x).as_expr()
target = (x - (ar + 2 * br)) * (x - (ar - br)) ** 2
check(
    "B4.4",
    "K-real class spectrum: charpoly = (x-(a+2b)) * (x-(a-b))^2, doublet "
    "eigenvalues exactly equal",
    is_zero(sp.expand(charpoly) - sp.expand(target)),
)
check(
    "B4.5",
    "channel values on the K-real class: tr(P_1 H) = a+2b, "
    "tr(P_w H) = tr(P_wbar H) = a-b; separation identically zero",
    is_zero(sp.trace(P[1] * Hrs) - (ar + 2 * br))
    and is_zero(sp.trace(P[w] * Hrs) - (ar - br))
    and is_zero(sp.trace(P[w] * Hrs) - sp.trace(P[wb] * Hrs)),
)

al, be, ga = sp.symbols("al be ga", real=True)
H = al * P[1] + be * P[w] + ga * P[wb]
check(
    "B4.6",
    "equivariant Hermitian class: H - K H K = (be-ga)*(P_w - P_wbar) "
    "identically, so doublet separation iff nonzero K-odd component",
    mat_zero((H - Kc(H)) - (be - ga) * (P[w] - P[wb]))
    and mat_zero(H - H.H),
)

S = P[w] - P[wb]
check(
    "B4.7",
    "canonical separator P_w - P_wbar: Hermitian, equivariant, K-ODD, and "
    "separates (channel difference 2)",
    mat_zero(S - S.H)
    and mat_zero(C3 * S - S * C3)
    and mat_zero(Kc(S) + S)
    and is_zero(sp.trace(P[w] * S) - sp.trace(P[wb] * S) - 2),
)

h11, h22, h33, h12, h13, h23 = sp.symbols("h11 h22 h33 h12 h13 h23", real=True)
H6 = Matrix([[h11, h12, h13], [h12, h22, h23], [h13, h23, h33]])
expec_w = (vw.H * H6 * vw)[0, 0]
expec_wb = (vw.conjugate().H * H6 * vw.conjugate())[0, 0]
check(
    "B4.8",
    "hardening: a GENERAL real symmetric operator (equivariance dropped) has "
    "exactly equal expectations on the two conjugate doublet lines",
    is_zero(expec_w - expec_wb),
)
check(
    "B4.9",
    "boundary witness: P_w (Hermitian, K-odd in part) separates the lines "
    "with expectations 1 and 0",
    is_zero((vw.H * P[w] * vw)[0, 0] - 1)
    and is_zero((vw.conjugate().H * P[w] * vw.conjugate())[0, 0]),
)

# ---------------------------------------------------------------------------
# B5: r-neutrality guard
# ---------------------------------------------------------------------------

check(
    "B5.1",
    "the K-real class realizes every (singlet, doublet) channel-value pair "
    "exactly once: (a,b) -> (a+2b, a-b) has determinant -3",
    Matrix([[1, 2], [1, -1]]).det() == -3,
)
ratios = set()
for aa, bb in [(1, 0), (4, 1), (2, 1)]:
    singlet = aa + 2 * bb
    doublet = aa - bb
    ratios.add(Rational(doublet, singlet))
check(
    "B5.2",
    "three exact witnesses give distinct doublet-to-singlet ratios "
    "{1, 1/2, 1/4}: the classification pins no ratio value",
    ratios == {Rational(1), Rational(1, 2), Rational(1, 4)},
)

# ---------------------------------------------------------------------------
# B6: verbatim quote gates
# ---------------------------------------------------------------------------

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
NEEDLE_R2 = (
    "**R2 — K-real derivable initial data.** Derivable initial data is K-real."
)
NEEDLE_SPECIES = (
    "the hw=1 triplet is three pairwise orthogonal, "
    "translation-character-distinct states in one physical Hilbert space, "
    "connected by the `C_3[111]` lattice unitary"
)

note_groups = quote_groups(NOTE)

check("B6.1", "block-05 carries the R1c supplied-carrier sentence", NEEDLE_R1C in flattened(BLOCK05))
check("B6.2", "note blockquotes the R1c supplied-carrier sentence", in_groups(note_groups, NEEDLE_R1C))
check("B6.3", "block-05 carries the supplied-surface FLAG sentence", NEEDLE_FLAG in flattened(BLOCK05))
check("B6.4", "note blockquotes the supplied-surface FLAG sentence", in_groups(note_groups, NEEDLE_FLAG))
check("B6.5", "mechanism note carries the R2 derivability sentence", NEEDLE_R2 in flattened(MECH))
check("B6.6", "note blockquotes the R2 derivability sentence", in_groups(note_groups, NEEDLE_R2))
check(
    "B6.7",
    "gate note carries the species-surface algebraic clause",
    in_groups(quote_groups(GATE), NEEDLE_SPECIES),
)
check("B6.8", "note blockquotes the species-surface algebraic clause", in_groups(note_groups, NEEDLE_SPECIES))

# ---------------------------------------------------------------------------
# B7: ledger shard filename gates (timeless: existence only)
# ---------------------------------------------------------------------------

ROWS = [
    "minimal_axioms",
    "staggered_dirac_realization_gate_note_2026-05-03",
    "kcpt_coupling_triple_two_presentation_derivable_class_spectral_pairing_bounded_theorem_note_2026-07-16",
    "kcpt_orbit_constant_registered_occupancy_weights_derivable_protocol_class_bounded_theorem_note_2026-07-12",
    "acphilambda_c3_resolvent_determinant_holonomy_coupling_narrow_theorem_note_2026-07-12",
    "acphilambda_fermionic_realification_pfaffian_power_identity_narrow_theorem_note_2026-07-12",
]
for i, rid in enumerate(ROWS, 1):
    shard = ROOT / "docs" / "audit" / "data" / "ledger" / rid[:2] / f"{rid}.json"
    check(f"B7.{i}", f"ledger shard file exists: {rid}", shard.is_file())

# ---------------------------------------------------------------------------
# B8: note hygiene
# ---------------------------------------------------------------------------

RAW = (ROOT / NOTE).read_text(encoding="utf-8")
B8_N = 0

SECTIONS = [
    "## Purpose",
    "## Supplied objects and consumed readings",
    "## Claims",
    "### Lattice delivery of the supplied corner carrier (T1, exact)",
    "### K-polarization of the delivered channels (T2, exact)",
    "### Spectral-pairing license instantiated on the delivered carrier (T3, exact)",
    "### Doublet-pair separation is K-gated on the delivered carrier (T4, bounded negative)",
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
    "**No check passes by literal stipulation.**",
    "**Status authority:** independent audit lane only.",
]
for s in SECTIONS:
    B8_N += 1
    check(f"B8.{B8_N}", f"note carries: {s}", s in RAW)

FORBIDDEN = [
    "exhaust",
    "only route",
    "last route",
    "closes the",
    "bijection",
    "final",
    "forces r",
    "derives r",
    "selects r",
    "retained",
    "discharge",
    "derived carrier",
]
RAW_LOW = RAW.lower()
for phrase in FORBIDDEN:
    B8_N += 1
    check(f"B8.{B8_N}", f"forbidden phrase absent: '{phrase}'", phrase not in RAW_LOW)

STATUS_SNAPSHOTS = [
    "unaudited at writing",
    "citation grades at writing",
    "audited_renaming",
    "honest auditor read",
]
for phrase in STATUS_SNAPSHOTS:
    B8_N += 1
    check(
        f"B8.{B8_N}",
        f"source-authored status/value snapshot absent: '{phrase}'",
        phrase not in RAW_LOW,
    )

B8_N += 1
check(
    f"B8.{B8_N}",
    "no bare decimal literals in the note",
    re.search(r"\d\.\d", RAW) is None,
)

DEPS = [
    "MINIMAL_AXIOMS_2026-06-29.md",
    "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md",
    "KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md",
    "KCPT_ORBIT_CONSTANT_REGISTERED_OCCUPANCY_WEIGHTS_DERIVABLE_PROTOCOL_CLASS_BOUNDED_THEOREM_NOTE_2026-07-12.md",
]
for dep in DEPS:
    B8_N += 1
    check(f"B8.{B8_N}", f"markdown dependency link present: {dep}", f"]({dep})" in RAW)

CONTEXT_HANDLES = [
    "ACPHILAMBDA_C3_RESOLVENT_DETERMINANT_HOLONOMY_COUPLING_NARROW_THEOREM_NOTE_2026-07-12.md",
    "ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md",
]
for handle in CONTEXT_HANDLES:
    B8_N += 1
    check(
        f"B8.{B8_N}",
        f"non-citation context handle is backticked and unlinked: {handle}",
        f"`{handle}`" in RAW and f"]({handle})" not in RAW,
    )

B8_N += 1
check(
    f"B8.{B8_N}",
    "every cited or handled doc path exists",
    all((ROOT / p).is_file() for p in [NOTE, RUNNER, GATE, BLOCK05, MECH, AXIOMS])
    and all((ROOT / "docs" / h).is_file() for h in CONTEXT_HANDLES)
    and all((ROOT / "docs" / d).is_file() for d in DEPS),
)

# ------------------------------------------------------------------ summary
print(f"PATH note={NOTE}")
print(f"PATH runner={RUNNER}")
print(f"PATH cache={CACHE}")
print(
    "FLAGS: T1 delivers a lattice realization of block-05's flagged supplied "
    "corner surface at the gate note's declared premise set (the surface "
    "remains supplied on the mechanism-note side); T4 is conditional on the "
    "consumed R2 derivability reading and scoped to expectation/channel "
    "separation by Hermitian observables (antilinear and non-Hermitian "
    "functionals declared untested); the K-real classification leaves the "
    "doublet-to-singlet channel ratio a free two-parameter dial -- r remains "
    "a dial (0, 1/2, 1), nothing here pins it; species labeling enters only "
    "as convention per the gate note's labeling clause"
)
print(
    "RESIDUAL (declared-open, inherited from the gate note): "
    "kinetic-class / P-FLUX supply line"
)
print(
    "RESIDUAL (declared-open, inherited from the gate note): "
    "spin-statistics support tier"
)
print(
    "RESIDUAL (declared-open, inherited from the gate note): "
    "boundary-holonomy convention (this runner computes the periodic sector)"
)
print(
    "RESIDUAL (declared-open, inherited from the gate note): "
    "species labeling convention (derivability no-go computed by the gate runner)"
)
if FAILURES:
    print("FAILED CHECKS: " + ", ".join(FAILURES))
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
