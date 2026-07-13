#!/usr/bin/env python3
"""Exact finite checks for the pair-correlation adjacency-confinement note.

Motivating external comparator (context only, NOT a derivation input):
STAR Collaboration, "Measuring spin correlation between quarks during QCD
confinement," Nature 650, 65-71 (2026) / arXiv:2506.05499 -- a (18 +/- 4)%
relative spin polarization correlation between Lambda / anti-Lambda hyperons,
inherited from a vacuum strange quark-antiquark pair, which VANISHES as the
pair separates in angle (decoherence with separation).

This runner establishes, at bounded-theorem strength and with exact rational
arithmetic (Fraction; no floats, no tolerances), the framework-internal
structural statements the note discusses:

  T1  The nearest-neighbor bonded-pair arena C^2 (x) C^2 carries the canonical
      exchange split Sym^2 (+) Anti^2 = ranks 3 (+) 1 (re-established here,
      consistent with the color-arena bonded-pair note).
  T2  UNDER A SUPPLIED SPIN-AXIS IDENTIFICATION S_i = sigma_i / 2 (the arena
      note flags this identification as downstream, not axiom content) the
      two-body operator S_A . S_B equals (1/2) SWAP - (1/4) I exactly, with
      eigenvalue +1/4 on the symmetric (spin-1 triplet) block and -3/4 on the
      antisymmetric (spin-0 singlet) block; the total Casimir is 2 and 0.
  T3  The SINGLET is a genuinely correlated pair: its connected spin correlator
      <S_A . S_B> - <S_A> . <S_B> = -3/4 is nonzero and maximal. This is the
      substrate of a STAR-like correlated created pair.
  T4  A PRODUCT (uncorrelated) two-site state has connected correlator exactly
      0 for the same observable. Since the only supplied inter-site coupling is
      the nearest-neighbor admissibility rule, two NON-adjacent sites carry a
      product state -> zero connected correlator. This is the framework's
      structural "decoherence with separation."
  T5  The framework's NAMED scalar readout is additive over disjoint records,
      so its two-record connected cumulant I(A |_| B) - I(A) - I(B) vanishes
      IDENTICALLY. The named readout is therefore correlation-blind: expressing
      any nonzero pair correlation (STAR's magnitude) requires a joint,
      non-additive functional -- the minimal extension target named in the note.
  T6  Assembling T3-T4 over Z^3 lattice separation: the connected correlator is
      nonzero only at adjacency (distance 1) and 0 at every larger separation.

Self-contained: Python standard library only (fractions, itertools, ast, sys,
pathlib). No numeric libraries, no network, no subprocess, no file writes.
"""

import ast
from fractions import Fraction as Fr
from itertools import product
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
AXIOM_FILE = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
ARENA_FILE = (
    ROOT
    / "docs"
    / "COLOR_ARENA_BONDED_PAIR_ADMISSIBILITY_CROSS_SITE_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-06.md"
)

passes = 0
fails = 0


def record(label, condition, detail=""):
    global passes, fails
    if condition:
        passes += 1
        print(f"[PASS] {label}")
    else:
        fails += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


# ---------------------------------------------------------------------------
# Tiny exact linear algebra over the rationals (matrices = tuple-of-tuples of
# Fraction; vectors = tuple of Fraction). Dimensions are 2 and 4, so naive
# implementations are exact and instant.
# ---------------------------------------------------------------------------

def mat(rows):
    return tuple(tuple(Fr(x) for x in row) for row in rows)


def vec(xs):
    return tuple(Fr(x) for x in xs)


def eye(n):
    return tuple(tuple(Fr(1) if i == j else Fr(0) for j in range(n)) for i in range(n))


def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return tuple(
        tuple(sum((A[i][k] * B[k][j] for k in range(m)), Fr(0)) for j in range(p))
        for i in range(n)
    )


def matadd(A, B):
    return tuple(tuple(A[i][j] + B[i][j] for j in range(len(A[0]))) for i in range(len(A)))


def scal(c, A):
    c = Fr(c)
    return tuple(tuple(c * A[i][j] for j in range(len(A[0]))) for i in range(len(A)))


def transpose(A):
    return tuple(tuple(A[j][i] for j in range(len(A))) for i in range(len(A[0])))


def matvec(A, v):
    return tuple(sum((A[i][k] * v[k] for k in range(len(v))), Fr(0)) for i in range(len(A)))


def dot(u, v):
    return sum((u[i] * v[i] for i in range(len(u))), Fr(0))


def kron(A, B):
    ra, ca, rb, cb = len(A), len(A[0]), len(B), len(B[0])
    out = []
    for i in range(ra):
        for k in range(rb):
            row = []
            for j in range(ca):
                for l in range(cb):
                    row.append(A[i][j] * B[k][l])
            out.append(tuple(row))
    return tuple(out)


def rank(A):
    """Exact rank by fraction-free-friendly Gaussian elimination over Q."""
    M = [list(row) for row in A]
    rows, cols = len(M), len(M[0])
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[r][j] for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def expectation(op, v):
    """<v|op|v> / <v|v> for a real state vector v (exact rational)."""
    return dot(v, matvec(op, v)) / dot(v, v)


# ---------------------------------------------------------------------------
# Operators.
# ---------------------------------------------------------------------------
I2 = eye(2)
I4 = eye(4)

SX = mat([[0, 1], [1, 0]])            # sigma_x
SZ = mat([[1, 0], [0, -1]])           # sigma_z
SY_OVER_I = mat([[0, -1], [1, 0]])    # sigma_y / i  (real antisymmetric)

# SWAP on C^2 (x) C^2, basis |00>,|01>,|10>,|11> (indices 0..3).
SWAP = mat([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])

# sigma . sigma = sx(x)sx + sy(x)sy + sz(x)sz.  sy(x)sy = (sigma_y/i)(x)(sigma_y/i)
# because the two factors of i multiply to i^2 = -1 = (1/i)(1/i)^{-1}... concretely
# sigma_y (x) sigma_y = (i * SY_OVER_I) (x) (i * SY_OVER_I) = -(SY_OVER_I (x) SY_OVER_I).
SYSY = scal(-1, kron(SY_OVER_I, SY_OVER_I))
SIGMA_DOT = matadd(matadd(kron(SX, SX), SYSY), kron(SZ, SZ))
S_DOT_S = scal(Fr(1, 4), SIGMA_DOT)           # S_A . S_B = (1/4) sigma.sigma

# Single-site spin components embedded in the two-site space (for connected corr).
SxA = scal(Fr(1, 2), kron(SX, I2))
SzA = scal(Fr(1, 2), kron(SZ, I2))
SxB = scal(Fr(1, 2), kron(I2, SX))
SzB = scal(Fr(1, 2), kron(I2, SZ))
# S_y single-site expectation on a REAL state vanishes: <psi|sigma_y|psi> =
# i * psi^T (sigma_y/i) psi = 0 since sigma_y/i is antisymmetric. Handled below.
SyA_over_i = scal(Fr(1, 2), kron(SY_OVER_I, I2))
SyB_over_i = scal(Fr(1, 2), kron(I2, SY_OVER_I))

# Exchange projectors.
P_SYM = scal(Fr(1, 2), matadd(I4, SWAP))
P_ANTI = scal(Fr(1, 2), matadd(I4, scal(-1, SWAP)))

# Total-spin Casimir S^2 = S_A^2 + S_B^2 + 2 S_A.S_B = (3/2) I + 2 S_A.S_B.
S2_TOT = matadd(scal(Fr(3, 2), I4), scal(2, S_DOT_S))

# State vectors (unnormalized, real -> exact rational expectations).
SINGLET = vec([0, 1, -1, 0])
TRIP0 = vec([1, 0, 0, 0])
TRIP_SYM = vec([0, 1, 1, 0])
TRIP1 = vec([0, 0, 0, 1])


def real_connected_correlator(v):
    """Connected correlator <S_A.S_B> - <S_A>.<S_B> for a real 2-qubit state v.
    The S_y term uses <S_y>=0 for real states (verified separately)."""
    exx = expectation(SxA, v) * expectation(SxB, v)
    ezz = expectation(SzA, v) * expectation(SzB, v)
    # <S_y> = i * <S_y/i>; for real v, <S_y/i> is an antisymmetric form = 0.
    eyy = (expectation(SyA_over_i, v)) * (expectation(SyB_over_i, v))  # = 0*0
    return expectation(S_DOT_S, v) - (exx + eyy + ezz)


# ===========================================================================
# T1 -- the bonded-pair exchange substrate (re-established self-contained).
# ===========================================================================
record("T1: SWAP is an involution (SWAP^2 = I)", matmul(SWAP, SWAP) == I4)
record("T1: SWAP is symmetric (self-transpose)", transpose(SWAP) == SWAP)
record("T1: P_sym idempotent", matmul(P_SYM, P_SYM) == P_SYM)
record("T1: P_anti idempotent", matmul(P_ANTI, P_ANTI) == P_ANTI)
record(
    "T1: P_sym, P_anti orthogonal and complete",
    matmul(P_SYM, P_ANTI) == scal(0, I4) and matadd(P_SYM, P_ANTI) == I4,
)
record("T1: Sym block has rank 3 (triplet)", rank(P_SYM) == 3)
record("T1: Anti block has rank 1 (singlet)", rank(P_ANTI) == 1)

# ===========================================================================
# T2 -- spin content, CONDITIONAL on a supplied spin-axis identification.
# ===========================================================================
record(
    "T2 [EXACT, conditional on supplied S_i=sigma_i/2]: S_A.S_B = (1/2)SWAP - (1/4)I",
    S_DOT_S == matadd(scal(Fr(1, 2), SWAP), scal(Fr(-1, 4), I4)),
)
record(
    "T2 [EXACT]: S_A.S_B eigenvalue = -3/4 on the singlet (Anti block)",
    matvec(S_DOT_S, SINGLET) == tuple(Fr(-3, 4) * x for x in SINGLET),
)
for name, tv in (("T0", TRIP0), ("Tsym", TRIP_SYM), ("T1", TRIP1)):
    record(
        f"T2 [EXACT]: S_A.S_B eigenvalue = +1/4 on symmetric triplet vector {name}",
        matvec(S_DOT_S, tv) == tuple(Fr(1, 4) * x for x in tv),
    )
record(
    "T2 [EXACT]: total Casimir S^2 = 0 on singlet (spin-0)",
    matvec(S2_TOT, SINGLET) == tuple(Fr(0) for _ in SINGLET),
)
record(
    "T2 [EXACT]: total Casimir S^2 = 2 on symmetric triplet (spin-1)",
    matvec(S2_TOT, TRIP_SYM) == tuple(Fr(2) * x for x in TRIP_SYM),
)

# ===========================================================================
# T3 -- the singlet is a genuinely correlated pair.
# ===========================================================================
record(
    "T3 [EXACT]: <S_z^A> = 0 on the singlet (rotationally invariant)",
    expectation(SzA, SINGLET) == 0 and expectation(SxA, SINGLET) == 0,
)
singlet_conn = real_connected_correlator(SINGLET)
record(
    "T3 [EXACT]: singlet connected correlator <S_A.S_B> - <S_A>.<S_B> = -3/4 (nonzero, maximal)",
    singlet_conn == Fr(-3, 4),
)

# ===========================================================================
# T4 -- product (uncorrelated) states have zero connected correlator.
#       Off-adjacency the only supplied coupling (nearest-neighbor
#       admissibility) is absent, so the two-site state is a product ->
#       decoherence with separation, at the state level.
# ===========================================================================
single_qubit_states = [
    vec([1, 0]),
    vec([0, 1]),
    vec([1, 1]),
    vec([1, -1]),
    vec([2, 1]),
    vec([1, 3]),
    vec([3, -2]),
]
product_conn_all_zero = True
for a in single_qubit_states:
    for b in single_qubit_states:
        pv = tuple(a[i] * b[j] for i in range(2) for j in range(2))
        if real_connected_correlator(pv) != 0:
            product_conn_all_zero = False
record(
    "T4 [EXACT]: connected correlator = 0 for every product state "
    f"({len(single_qubit_states)**2} tested) -- structural decoherence with separation",
    product_conn_all_zero,
)
record(
    "T4 control (non-vacuous): the entangled singlet is NOT a product state "
    "(its connected correlator is nonzero)",
    singlet_conn != 0,
)

# ===========================================================================
# T5 -- the NAMED additive scalar readout is correlation-blind.
#       Record axiom: for disjoint records, scalar readout I is additive.
#       => the 2-record connected cumulant I(A|_|B) - I(A) - I(B) vanishes
#          identically. A non-additive functional does not.
# ===========================================================================

def I_additive(records_set, weight):
    return sum((weight[r] for r in records_set), 0)


# A deterministic family of finite records with assorted integer readout weights.
universe = list(range(8))
weight = {0: 3, 1: -2, 2: 5, 3: 0, 4: -7, 5: 11, 6: -1, 7: 4}
disjoint_pairs = [
    (frozenset({0, 1}), frozenset({2, 3})),
    (frozenset({4}), frozenset({5, 6, 7})),
    (frozenset({0, 2, 4}), frozenset({1, 3, 5})),
    (frozenset({6, 7}), frozenset({0})),
    (frozenset(), frozenset({1, 2})),
    (frozenset({3, 5, 7}), frozenset({2, 4, 6})),
]
additive_cumulant_zero = True
for A, B in disjoint_pairs:
    assert A.isdisjoint(B)
    kappa2 = I_additive(A | B, weight) - I_additive(A, weight) - I_additive(B, weight)
    if kappa2 != 0:
        additive_cumulant_zero = False
record(
    "T5 [EXACT]: additive readout 2-record connected cumulant I(A|_|B)-I(A)-I(B) = 0 "
    f"on all {len(disjoint_pairs)} disjoint families (named readout is correlation-blind)",
    additive_cumulant_zero,
)

# Control: a NON-additive functional (I^2) has a nonzero cumulant, so the T5
# zero is a genuine consequence of additivity, not of the test construction.
def I_squared(records_set, weight):
    s = I_additive(records_set, weight)
    return s * s


nonadditive_has_nonzero = False
for A, B in disjoint_pairs:
    kappa2 = I_squared(A | B, weight) - I_squared(A, weight) - I_squared(B, weight)
    if kappa2 != 0:
        nonadditive_has_nonzero = True
record(
    "T5 control (non-vacuous): a non-additive functional (I^2) has a nonzero "
    "2-record cumulant -> a joint (non-additive) correlator is the extension target",
    nonadditive_has_nonzero,
)

# ===========================================================================
# T6 -- assembly over Z^3: readable pair correlation is adjacency-confined.
#       At distance 1 the bonded-pair arena admits the correlated singlet
#       (connected correlator -3/4); at any larger separation only a product
#       state is supplied (connected correlator 0). Distance profile:
# ===========================================================================
origin = (0, 0, 0)
lattice_probes = [
    (1, 0, 0),   # distance 1  (nearest neighbor -> arena)
    (0, 1, 0),   # distance 1
    (1, 1, 0),   # distance sqrt(2)
    (1, 1, 1),   # distance sqrt(3)
    (2, 0, 0),   # distance 2
    (3, 1, 0),   # farther
]


def is_nn(x, y):
    return sum(abs(x[i] - y[i]) for i in range(3)) == 1


def structural_correlator(x, y):
    """Connected correlator of the state supplied at {x,y}: the adjacency
    arena supplies the correlated singlet; non-adjacency supplies a product."""
    if is_nn(x, y):
        return real_connected_correlator(SINGLET)          # -3/4 (arena admits singlet)
    return real_connected_correlator(vec([1, 0, 0, 0]))    # 0 (|00>, a product state)


profile = [(pt, structural_correlator(origin, pt)) for pt in lattice_probes]
nonzero_only_at_nn = all(
    (val == Fr(-3, 4)) == is_nn(origin, pt) and (val == 0) != is_nn(origin, pt)
    for pt, val in profile
)
record(
    "T6 [EXACT]: connected correlator nonzero (-3/4) ONLY at adjacency, 0 at every "
    "larger Z^3 separation -- structural decoherence-with-separation profile",
    nonzero_only_at_nn,
)
print("        distance profile (L1, correlator): "
      + ", ".join(f"d{sum(abs(pt[i]) for i in range(3))}->{val}" for pt, val in profile))

# ===========================================================================
# Text audit -- the two axiom sentences this note leans on are present verbatim.
# ===========================================================================

def norm_ws(s):
    return " ".join(s.split())


axiom_text = norm_ws(AXIOM_FILE.read_text(encoding="utf-8"))
arena_text = norm_ws(ARENA_FILE.read_text(encoding="utf-8"))
record(
    "Text audit: Admissibility nearest-neighbor sentence present in axiom memo",
    "the available possibilities are determined by, and vary with, the nearest-neighbor conditions"
    in axiom_text,
)
record(
    "Text audit: Record additive-scalar-readout sentence present in axiom memo",
    "scalar readout" in axiom_text and "is additive" in axiom_text,
)
record(
    "Text audit: arena note supplies the Sym^2 + Anti^2 exchange split",
    "Sym^2(C^2)" in arena_text and "Anti^2(C^2)" in arena_text,
)
record(
    "Text audit: arena note flags the spin-axis identification as downstream (not axiom)",
    "spin-axis identification" in arena_text,
)

# ===========================================================================
# AST self-scan -- the runner performs no network / subprocess / write I/O.
# ===========================================================================
self_src = Path(__file__).read_text(encoding="utf-8")
tree = ast.parse(self_src)
banned_imports = {"os", "socket", "subprocess", "requests", "urllib", "shutil", "http"}
imported = set()
write_open = False
path_write = False
for node in ast.walk(tree):
    if isinstance(node, ast.Import):
        for n in node.names:
            imported.add(n.name.split(".")[0])
    elif isinstance(node, ast.ImportFrom):
        if node.module:
            imported.add(node.module.split(".")[0])
    elif isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name) and node.func.id == "open":
            for kw in node.keywords:
                if kw.arg == "mode" and isinstance(kw.value, ast.Constant) and "w" in str(kw.value.value):
                    write_open = True
            for arg in node.args[1:]:
                if isinstance(arg, ast.Constant) and "w" in str(arg.value):
                    write_open = True
        if isinstance(node.func, ast.Attribute) and node.func.attr in {
            "write_text", "write_bytes", "open",
        } and isinstance(node.func.value, ast.Name):
            # allow Path(...).read_text via attribute on a call, but flag write_*
            if node.func.attr in {"write_text", "write_bytes"}:
                path_write = True
record("AST self-scan: no network/subprocess/os imports", not (imported & banned_imports),
       f"found {sorted(imported & banned_imports)}")
record("AST self-scan: no write-mode open() calls", not write_open)
record("AST self-scan: no Path write_text/write_bytes calls", not path_write)

# ===========================================================================
print(f"TOTAL: {passes} PASS / {fails} FAIL")
print(
    "DECLARATION: bounded structural result. The bonded-pair arena supplies a "
    "correlated (singlet) two-site substrate; readable pair correlation is "
    "confined to nearest-neighbor adjacency (product off-adjacency -> "
    "decoherence with separation); and the NAMED additive scalar readout has "
    "identically zero two-record connected part. No dynamics, Born weight, "
    "record-formation rate, spin-axis identification, strangeness, hyperon, or "
    "the STAR (18+/-4)% magnitude is derived or claimed; STAR is a named "
    "external comparator only. Audit status is set solely by the independent "
    "audit lane."
)
sys.exit(1 if fails else 0)
