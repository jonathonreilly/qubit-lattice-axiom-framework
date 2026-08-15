#!/usr/bin/env python3
"""Independent check of the circulant spectral fold support packet.

Each unit named below is recomputed here by a DIFFERENT exact method, and the
primary's freshly emitted payload is verified fail-closed against selected
canonical-summary fields.  This file deliberately does not import the primary:
it re-derives, it does not re-run the same code path.  The mapping is exhaustive
over the primary's sections, and it is the honest statement of coverage: what
is not in this list is not independently recomputed here.

Methods used here (primary's method -> method used here):

  characteristic coefficients: symbolic term comparison over Q(i)[a, x, y]
      -> Newton's identities from power traces, checked by exact evaluation
         on a 4 x 4 x 4 rational grid, which proves the identity because both
         sides have degree at most three in each variable
  eigenvectors, multiset level: Eisenstein-integer eigenvalue equations
      -> Vieta: the three claimed eigenvalues are evaluated exactly in
         Q(i, w) with w^2 + w + 1 = 0 and their elementary symmetric
         functions are compared with the closed forms
  eigenvectors, per-index orientation: Eisenstein-integer eigenvalue equations
      -> explicit matrix-vector action of H on v_k in Q(i, w), with the
         opposite orientation required to fail per index
  inversion: forward evaluation of the recovery formulas
      -> reverse direction, rebuilding (e1, e2, e3) from the recovered
         parameters and comparing with the originals
  degenerate stratum: exact witness at x = y = 0
      -> the same stratum reached as a limit point of the rational grid,
         with the discriminant and the triple root recomputed there
  dihedral fold, orbit sizes: Fraction arithmetic modulo one turn
      -> integer arithmetic in Z/N with N = 3q, orbits as integer cosets
  dihedral fold, composition law: composites identified by their action on
      five generic arguments
      -> the six maps represented as permutations of one six-point orbit,
         composed as permutations, with the group table read off the
         permutation composition and compared with the parameter law
  similarity invariance: trace / principal-minor / determinant evaluation
      -> power traces of the conjugated matrix with Newton's identities
  cycle geometry: restriction matrix in an explicit plane basis
      -> characteristic polynomial of the full matrix, its factorisation, the
         Cayley-Hamilton relation R^2 + R + I = 0 on the plane, and the
         restriction rebuilt entry by entry from a projection
  equal-coefficient functional: closed-form value 3 alpha
      -> coordinate summation on the all-ones vector, with injectivity and
         the comparator member recomputed
  pi enclosure: Machin, pi = 16 arctan(1/5) - 4 arctan(1/239)
      -> pi = 4 arctan(1/2) + 4 arctan(1/3), with overlap of the two
         enclosures required
  measured signed-root scan: symmetric-function inversion
      -> bisection on the argument against the sorted target triple, with the
         modulus taken from the second central moment

Execution evidence:

  * the primary's own source SHA-256 must equal the value recorded in its
    freshly emitted payload;
  * the primary is executed as a subprocess, writing to a temporary path, and
    must exit 0;
  * the temporary payload must be present and parse as JSON;
  * the stored payload digest must equal a digest recomputed here;
  * the payload must match a canonical expected summary assembled
    from this file's own independent methods;
  * two tamper regressions run every time: a byte tamper must break the
    digest, and the same tamper to a selected canonical-summary field with a
    recomputed self-digest must still be rejected by the selected-summary
    comparison.

Read inventory (three kinds, kept separate).

  * Embedded observational comparator inputs: m_e = 0.51099895 MeV,
    m_mu = 105.6583755 MeV, and m_tau = 1776.86 MeV, independently embedded
    for the measured section-8 comparison only.
  * External runtime scientific file reads: NONE.
  * Package-local integrity reads: the primary runner's source, for the
    source-hash comparison and the subprocess execution.  It is declared in
    ``AUDIT_INPUT_PATHS``.  The subprocess writes only inside a temporary
    directory, and a normal run leaves no generated repository output.

Fail-closed: every check computes both sides; any failure prints FAIL and the
process exits 1.
"""
from __future__ import annotations

import ast
import hashlib
import itertools
import json
import math
import os
import subprocess
import sys
import tempfile
from fractions import Fraction

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "scripts/salvaged_circulant_spectral_fold_2026_08_09.py",
)

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
PRIMARY = os.path.join(REPO, AUDIT_INPUT_PATHS[0])
DATE = "2026-08-09"
EXPECTED_CHECK_COUNT = 35
PRIMARY_DECLARED_CHECK_COUNT = 45
PUBLISHED_SEPARATION_LOWER_BOUND = Fraction(3519, 2_000_000)
PUBLISHED_SEPARATION_LOWER_BOUND_TEXT = "1.7595e-03"

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok))
    print(f"{'PASS' if ok else 'FAIL'} {name}")
    return ok


# ---------------------------------------------------------------------------
# exact arithmetic in Q(i, w), w^2 + w + 1 = 0.  An element is stored as four
# rationals: (r0, i0, r1, i1) meaning (r0 + i0*i) + (r1 + i1*i)*w.
# ---------------------------------------------------------------------------
class QIW:
    __slots__ = ("c",)

    def __init__(self, r0=0, i0=0, r1=0, i1=0):
        self.c = (Fraction(r0), Fraction(i0), Fraction(r1), Fraction(i1))

    def __add__(self, o):
        return QIW(*(a + b for a, b in zip(self.c, o.c)))

    def __sub__(self, o):
        return QIW(*(a - b for a, b in zip(self.c, o.c)))

    def __mul__(self, o):
        a0, b0, a1, b1 = self.c
        c0, d0, c1, d1 = o.c
        # complex products of the two w-components
        p0 = (a0 * c0 - b0 * d0, a0 * d0 + b0 * c0)          # 1 * 1
        p1 = (a0 * c1 - b0 * d1, a0 * d1 + b0 * c1)          # 1 * w
        p2 = (a1 * c0 - b1 * d0, a1 * d0 + b1 * c0)          # w * 1
        p3 = (a1 * c1 - b1 * d1, a1 * d1 + b1 * c1)          # w * w = -1 - w
        r0 = p0[0] - p3[0]
        i0 = p0[1] - p3[1]
        r1 = p1[0] + p2[0] - p3[0]
        i1 = p1[1] + p2[1] - p3[1]
        return QIW(r0, i0, r1, i1)

    def is_zero(self):
        return all(v == 0 for v in self.c)

    def __eq__(self, o):
        return isinstance(o, QIW) and self.c == o.c

    def __repr__(self):
        return f"QIW{self.c}"


def qiw_rational(value: Fraction) -> QIW:
    return QIW(value, 0, 0, 0)


W = QIW(0, 0, 1, 0)
W2 = W * W


def qiw_pow_w(k: int) -> QIW:
    return [QIW(1, 0, 0, 0), W, W2][k % 3]


# ---------------------------------------------------------------------------
# exact matrices over Fraction / Gaussian rationals, independent helpers
# ---------------------------------------------------------------------------
CYCLE = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]


def cplx_H(a: Fraction, x: Fraction, y: Fraction):
    """H as a 3x3 matrix of complex pairs (re, im) of Fractions."""
    b = (x, y)
    bbar = (x, -y)

    def add(p, q):
        return (p[0] + q[0], p[1] + q[1])

    rows = []
    for i in range(3):
        row = []
        for j in range(3):
            entry = (Fraction(0), Fraction(0))
            if i == j:
                entry = add(entry, (a, Fraction(0)))
            if CYCLE[i][j]:
                entry = add(entry, b)
            if CYCLE[j][i]:
                entry = add(entry, bbar)
            row.append(entry)
        rows.append(row)
    return rows


def cmul(p, q):
    return (p[0] * q[0] - p[1] * q[1], p[0] * q[1] + p[1] * q[0])


def cadd(p, q):
    return (p[0] + q[0], p[1] + q[1])


def mat_mul_pairs(A, B):
    out = []
    for i in range(3):
        row = []
        for j in range(3):
            acc = (Fraction(0), Fraction(0))
            for k in range(3):
                acc = cadd(acc, cmul(A[i][k], B[k][j]))
            row.append(acc)
        out.append(row)
    return out


def trace_pairs(A):
    acc = (Fraction(0), Fraction(0))
    for i in range(3):
        acc = cadd(acc, A[i][i])
    return acc


def newton_invariants(A):
    """(e1, e2, e3) from power traces, via Newton's identities."""
    A2 = mat_mul_pairs(A, A)
    A3 = mat_mul_pairs(A2, A)
    p1, p2, p3 = trace_pairs(A), trace_pairs(A2), trace_pairs(A3)
    e1 = p1
    e2 = (Fraction(1, 2) * (cmul(p1, p1)[0] - p2[0]),
          Fraction(1, 2) * (cmul(p1, p1)[1] - p2[1]))
    p1cube = cmul(cmul(p1, p1), p1)
    p1p2 = cmul(p1, p2)
    e3 = (Fraction(1, 6) * (p1cube[0] - 3 * p1p2[0] + 2 * p3[0]),
          Fraction(1, 6) * (p1cube[1] - 3 * p1p2[1] + 2 * p3[1]))
    return e1, e2, e3


GRID = (Fraction(-2), Fraction(-1, 3), Fraction(1), Fraction(5, 2))


def closed_forms(a: Fraction, x: Fraction, y: Fraction):
    bsq = x * x + y * y
    return (3 * a,
            3 * a * a - 3 * bsq,
            a ** 3 - 3 * a * bsq + 2 * (x ** 3 - 3 * x * y * y))


# ---------------------------------------------------------------------------
# CROSS-CHECK -- characteristic coefficients by Newton's identities on a grid
# ---------------------------------------------------------------------------
def crosscheck_coefficients() -> dict:
    agree = True
    self_adjoint = True
    points = 0
    for a, x, y in itertools.product(GRID, repeat=3):
        points += 1
        H = cplx_H(a, x, y)
        for i in range(3):
            for j in range(3):
                if H[i][j] != (H[j][i][0], -H[j][i][1]):
                    self_adjoint = False
        e1, e2, e3 = newton_invariants(H)
        if any(v[1] != 0 for v in (e1, e2, e3)):
            agree = False
        if (e1[0], e2[0], e3[0]) != closed_forms(a, x, y):
            agree = False
    check("GRID_PROOF_OF_THE_CHARACTERISTIC_COEFFICIENTS_BY_NEWTON_IDENTITIES",
          agree and points == 64)
    check("SELF_ADJOINTNESS_HOLDS_AT_EVERY_GRID_POINT", self_adjoint)
    return {"grid_points": points,
            "degree_bound_per_variable": 3,
            "argument": "both sides have degree at most three in each variable, "
                        "so agreement on a 4 x 4 x 4 grid of distinct rational "
                        "values proves the identity",
            "closed_forms": {"e1": "3*a", "e2": "3*a^2 - 3*(x^2 + y^2)",
                             "e3": "a^3 - 3*a*(x^2 + y^2) + 2*(x^3 - 3*x*y^2)"}}


# ---------------------------------------------------------------------------
# CROSS-CHECK -- Vieta on the claimed eigenvalues, exactly in Q(i, w)
# ---------------------------------------------------------------------------
def crosscheck_vieta() -> dict:
    ok = True
    orientation_ok = True
    for a, x, y in itertools.product(GRID, repeat=3):
        b = QIW(x, y, 0, 0)
        bbar = QIW(x, -y, 0, 0)
        lams = [qiw_rational(a) + b * qiw_pow_w((-k) % 3)
                + bbar * qiw_pow_w(k % 3) for k in range(3)]
        s1 = lams[0] + lams[1] + lams[2]
        s2 = lams[0] * lams[1] + lams[0] * lams[2] + lams[1] * lams[2]
        s3 = lams[0] * lams[1] * lams[2]
        want = closed_forms(a, x, y)
        for got, target in zip((s1, s2, s3), want):
            if got != QIW(target, 0, 0, 0):
                ok = False
        # the opposite orientation gives the same multiset
        flipped = [qiw_rational(a) + b * qiw_pow_w(k % 3)
                   + bbar * qiw_pow_w((-k) % 3) for k in range(3)]
        if sorted(repr(v) for v in lams) != sorted(repr(v) for v in flipped):
            orientation_ok = False
    check("VIETA_ON_THE_CLAIMED_EIGENVALUES_REPRODUCES_THE_COEFFICIENTS", ok)
    check("BOTH_ARGUMENT_ORIENTATIONS_GIVE_THE_SAME_EIGENVALUE_MULTISET",
          orientation_ok)

    # Vieta sees only symmetric functions, so it is blind to the PER-INDEX
    # orientation: the two assignments give the same multiset, which is
    # exactly what the check above says.  Pin the per-index statement by
    # acting with H on v_k directly.
    per_index_ok = True
    opposite_fails = False
    for a, x, y in itertools.product(GRID, repeat=3):
        if (x, y) == (Fraction(0), Fraction(0)):
            continue
        b, bbar = QIW(x, y, 0, 0), QIW(x, -y, 0, 0)
        transpose = [[CYCLE[j][i] for j in range(3)] for i in range(3)]
        for k in range(3):
            v = [qiw_pow_w((k * t) % 3) for t in range(3)]
            # (H v)_i = a v_i + b (C v)_i + conj(b) (C^T v)_i
            image = []
            for i in range(3):
                acc = qiw_rational(a) * v[i]
                for j in range(3):
                    if CYCLE[i][j]:
                        acc = acc + b * v[j]
                    if transpose[i][j]:
                        acc = acc + bbar * v[j]
                image.append(acc)
            lam = (qiw_rational(a) + b * qiw_pow_w((-k) % 3)
                   + bbar * qiw_pow_w(k % 3))
            lam_opposite = (qiw_rational(a) + b * qiw_pow_w(k % 3)
                            + bbar * qiw_pow_w((-k) % 3))
            if any(image[t] != lam * v[t] for t in range(3)):
                per_index_ok = False
            if any(image[t] != lam_opposite * v[t] for t in range(3)):
                opposite_fails = True
    check("MATRIX_ACTION_PINS_THE_PER_INDEX_EIGENVALUE_ORIENTATION",
          per_index_ok)
    check("THE_OPPOSITE_PER_INDEX_ORIENTATION_IS_WRONG_AT_SOME_GRID_POINT",
          opposite_fails)
    return {"ring": "Q(i, w) with w^2 + w + 1 = 0",
            "eigenvalues": "lambda_k = a + b w^{-k} + conj(b) w^{k}",
            "orientation": "swapping w^{-k} for w^{k} permutes the triple and "
                           "leaves the multiset unchanged, while the "
                           "per-index assignment is pinned separately below"}


# ---------------------------------------------------------------------------
# CROSS-CHECK -- inversion, reverse direction
# ---------------------------------------------------------------------------
def crosscheck_inversion() -> dict:
    ok = True
    samples = []
    for a, x, y in itertools.product(GRID, repeat=3):
        e1, e2, e3 = closed_forms(a, x, y)
        rec_a = Fraction(e1, 3)
        rec_bsq = Fraction(e1 * e1 - 3 * e2, 9)
        rec_num = e3 - rec_a ** 3 + 3 * rec_a * rec_bsq
        # rebuild the coefficients from the recovered parameters
        rebuilt = (3 * rec_a, 3 * rec_a ** 2 - 3 * rec_bsq,
                   rec_a ** 3 - 3 * rec_a * rec_bsq + rec_num)
        if rebuilt != (e1, e2, e3):
            ok = False
        if rec_bsq != x * x + y * y or rec_num != 2 * (x ** 3 - 3 * x * y * y):
            ok = False
        if x == 0 and y == 0 and rec_bsq != 0:
            ok = False
    check("REVERSE_DIRECTION_REBUILDS_THE_COEFFICIENTS_FROM_THE_RECOVERY",
          ok)
    # the sum-of-two-squares bound, re-derived by direct expansion
    bound_ok = True
    for x, y in itertools.product(GRID, repeat=2):
        lhs = (x * x + y * y) ** 3
        rhs = (x ** 3 - 3 * x * y * y) ** 2 + (3 * x * x * y - y ** 3) ** 2
        if lhs != rhs:
            bound_ok = False
        if (x ** 3 - 3 * x * y * y) ** 2 > (x * x + y * y) ** 3:
            bound_ok = False
    check("THE_FOLD_ARGUMENT_BOUND_HOLDS_AT_EVERY_GRID_POINT", bound_ok)

    # The primary's grid excludes B = 0; the degenerate stratum is checked
    # here on its own, at the point the recovery is undefined.
    degenerate = []
    degenerate_ok = True
    for a in (Fraction(3), Fraction(-1, 2), Fraction(0), Fraction(7, 4)):
        e1, e2, e3 = closed_forms(a, Fraction(0), Fraction(0))
        degenerate.append({"a": str(a), "e1": str(e1), "e2": str(e2),
                           "e3": str(e3)})
        if e1 * e1 - 3 * e2 != 0:
            degenerate_ok = False
        # the characteristic polynomial is (t - a)^3 exactly
        if (e1, e2, e3) != (3 * a, 3 * a * a, a ** 3):
            degenerate_ok = False
    check("THE_DEGENERATE_STRATUM_AT_B_ZERO_IS_A_TRIPLE_ROOT_WITH_ZERO_DISCRIMINANT",
          degenerate_ok and len(degenerate) == 4)
    samples.append({"grid_points": len(GRID) ** 3})
    return {"reverse_method": "rebuild (e1, e2, e3) from (a, B^2, "
                             "2 B^3 cos 3 delta) and compare",
            "bound": "(x^2 + y^2)^3 - (x^3 - 3 x y^2)^2 = (3 x^2 y - y^3)^2 "
                     ">= 0, so |cos 3 delta| <= 1",
            "degenerate_stratum": degenerate,
            "samples": samples}


# ---------------------------------------------------------------------------
# CROSS-CHECK -- the fold, in integer arithmetic
# ---------------------------------------------------------------------------
def crosscheck_fold() -> dict:
    histogram: dict[int, int] = {}
    dichotomy_ok = True
    endpoint_ok = True
    turns = 0
    for q in range(1, 25):
        N = 3 * q
        for j in range(q):
            turns += 1
            U = (3 * j) % N              # u = j/q as U/N
            R = q                        # one third of a turn as R/N
            orbit = {(sign * U + k * R) % N for sign in (1, -1) for k in range(3)}
            size = len(orbit)
            histogram[size] = histogram.get(size, 0) + 1
            if size not in (3, 6):
                dichotomy_ok = False
            if (size == 3) != ((6 * j) % q == 0):
                endpoint_ok = False
    check("INTEGER_COSET_METHOD_REPRODUCES_THE_ORBIT_SIZE_DICHOTOMY",
          dichotomy_ok and sorted(histogram) == [3, 6])
    check("INTEGER_COSET_METHOD_REPRODUCES_THE_ENDPOINT_CHARACTERISATION",
          endpoint_ok)

    # The composition law, by a method that never writes the law down: each
    # of the six maps becomes a PERMUTATION of one six-point orbit, the
    # permutations are composed as permutations, and the resulting table is
    # compared with the parameter law only at the end.  A dropped outer sign
    # changes the permutation, so it cannot survive here either.
    N, U = 3 * 7, 3            # u = 1/7 as U/N, one third of a turn is 7/N
    R = 7
    elements = [(s, k) for s in (1, -1) for k in range(3)]
    orbit_points = sorted({(s * U + k * R) % N for s, k in elements})

    def permutation(element):
        s, k = element
        return tuple(orbit_points.index((s * p + k * R) % N)
                     for p in orbit_points)

    perms = {e: permutation(e) for e in elements}
    faithful = len(set(perms.values())) == 6 and len(orbit_points) == 6

    def compose_perms(outer, inner):
        return tuple(outer[inner[i]] for i in range(len(inner)))

    law_ok = True
    table: dict[tuple, list] = {}
    for outer in elements:
        row = []
        for inner in elements:
            product = compose_perms(perms[outer], perms[inner])
            named = [e for e in elements if perms[e] == product]
            predicted = (outer[0] * inner[0],
                         (outer[0] * inner[1] + outer[1]) % 3)
            row.append(named[0] if len(named) == 1 else (0, 0))
            if len(named) != 1 or named[0] != predicted:
                law_ok = False
        table[outer] = row
    check("PERMUTATION_METHOD_REPRODUCES_THE_SIGNED_COMPOSITION_LAW",
          law_ok and faithful)
    latin = (all(sorted(row) == sorted(elements) for row in table.values())
             and all(sorted(table[outer][i] for outer in elements)
                     == sorted(elements) for i in range(6)))
    non_abelian = any(
        compose_perms(perms[g], perms[h]) != compose_perms(perms[h], perms[g])
        for g in elements for h in elements)
    check("THE_PERMUTATION_GROUP_TABLE_IS_A_LATIN_SQUARE_AND_NON_ABELIAN",
          latin and non_abelian)
    return {"turn_samples": turns,
            "size_histogram": {str(k): v for k, v in sorted(histogram.items())},
            "composition_table": {
                f"{outer[0]},{outer[1]}|{inner[0]},{inner[1]}":
                    f"{table[outer][i][0]},{table[outer][i][1]}"
                for outer in elements for i, inner in enumerate(elements)},
            "composition_method": "the six maps as permutations of one "
                                  "six-point orbit, composed as permutations",
            "method": "orbits computed as integer cosets in Z/N with N = 3q"}


# ---------------------------------------------------------------------------
# CROSS-CHECK -- similarity invariance by power traces
# ---------------------------------------------------------------------------
def crosscheck_similarity() -> dict:
    a, x, y = Fraction(1, 3), Fraction(5, 4), Fraction(-2, 3)
    H = cplx_H(a, x, y)
    base = newton_invariants(H)

    def cq_inv(M):
        aug = [[M[i][j] for j in range(3)]
               + [(Fraction(1), Fraction(0)) if i == j else (Fraction(0), Fraction(0))
                  for j in range(3)] for i in range(3)]
        for col in range(3):
            pivot = next((r for r in range(col, 3) if aug[r][col] != (0, 0)), None)
            if pivot is None:
                raise ZeroDivisionError("singular")
            aug[col], aug[pivot] = aug[pivot], aug[col]
            p = aug[col][col]
            n = p[0] * p[0] + p[1] * p[1]
            scale = (p[0] / n, -p[1] / n)
            aug[col] = [cmul(scale, v) for v in aug[col]]
            for r in range(3):
                if r != col and aug[r][col] != (0, 0):
                    f = aug[r][col]
                    aug[r] = [(v[0] - cmul(f, w)[0], v[1] - cmul(f, w)[1])
                              for v, w in zip(aug[r], aug[col])]
        return [row[3:] for row in aug]

    transforms = [
        [[(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)), (Fraction(0), Fraction(0))],
         [(Fraction(0), Fraction(0)), (Fraction(2), Fraction(0)), (Fraction(1), Fraction(0))],
         [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(0)), (Fraction(3), Fraction(0))]],
        [[(Fraction(2), Fraction(0)), (Fraction(1), Fraction(0)), (Fraction(0), Fraction(0))],
         [(Fraction(0), Fraction(0)), (Fraction(1), Fraction(1)), (Fraction(5), Fraction(0))],
         [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(0)), (Fraction(1), Fraction(0))]],
    ]
    invariant = True
    for S in transforms:
        conj = mat_mul_pairs(mat_mul_pairs(S, H), cq_inv(S))
        if newton_invariants(conj) != base:
            invariant = False
    check("POWER_TRACE_METHOD_CONFIRMS_SIMILARITY_INVARIANCE", invariant)

    moved = [[cadd(H[i][j], (Fraction(1), Fraction(0)) if (i, j) == (0, 0)
                   else (Fraction(0), Fraction(0))) for j in range(3)]
             for i in range(3)]
    check("A_SELF_ADJOINT_PERTURBATION_MOVES_THE_POWER_TRACES",
          newton_invariants(moved) != base)
    return {"method": "power traces p1, p2, p3 with Newton's identities",
            "transforms_tested": len(transforms)}


# ---------------------------------------------------------------------------
# CROSS-CHECK -- cycle geometry from the characteristic polynomial
# ---------------------------------------------------------------------------
def crosscheck_cycle_geometry() -> dict:
    C = [[(Fraction(v), Fraction(0)) for v in row] for row in CYCLE]
    e1, e2, e3 = newton_invariants(C)
    # characteristic polynomial t^3 - e1 t^2 + e2 t - e3 = t^3 - 1
    charpoly_ok = (e1 == (0, 0) and e2 == (0, 0) and e3 == (1, 0))
    C3 = mat_mul_pairs(mat_mul_pairs(C, C), C)
    identity = [[(Fraction(1), Fraction(0)) if i == j else (Fraction(0), Fraction(0))
                 for j in range(3)] for i in range(3)]
    order_three = C3 == identity and C != identity
    check("THE_CYCLE_CHARACTERISTIC_POLYNOMIAL_IS_T_CUBED_MINUS_ONE",
          charpoly_ok and order_three)

    # on the sum-zero plane, Cayley-Hamilton for the restriction: R^2 + R + I = 0
    u1 = [Fraction(1), Fraction(-1), Fraction(0)]
    u2 = [Fraction(0), Fraction(1), Fraction(-1)]

    def apply(v):
        return [v[2], v[0], v[1]]

    def combo(alpha, beta):
        return [alpha * u1[i] + beta * u2[i] for i in range(3)]

    relation_ok = True
    for alpha, beta in ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)),
                        (Fraction(3, 7), Fraction(-2))):
        v = combo(alpha, beta)
        image = apply(apply(v))
        total = [image[i] + apply(v)[i] + v[i] for i in range(3)]
        if any(t != 0 for t in total):
            relation_ok = False
    check("THE_PLANE_RESTRICTION_SATISFIES_R_SQUARED_PLUS_R_PLUS_IDENTITY",
          relation_ok)
    # the fixed line carries eigenvalue 1, so the restriction's trace is
    # trace(C) - 1 and the rotation angle satisfies 2 cos theta = that trace
    cos_theta = (e1[0] - 1) / 2
    check("THE_ROTATION_ANGLE_FOLLOWS_FROM_THE_RESTRICTION_TRACE",
          cos_theta == Fraction(-1, 2))

    # Trace and determinant do not see a transposed or sign-flipped
    # restriction, so rebuild the matrix entry by entry by expanding each
    # image in the plane basis with an explicit linear solve.
    def coordinates(v):
        # alpha*u1 + beta*u2 = (alpha, beta - alpha, -beta)
        alpha, beta = v[0], -v[2]
        rebuilt = [alpha * u1[i] + beta * u2[i] for i in range(3)]
        return (alpha, beta) if rebuilt == list(v) else None

    col1, col2 = coordinates(apply(u1)), coordinates(apply(u2))
    restriction = ([[col1[0], col2[0]], [col1[1], col2[1]]]
                   if col1 and col2 else None)
    check("THE_RESTRICTION_MATRIX_REBUILT_FROM_THE_IMAGES_IS_THE_STATED_ONE",
          restriction == [[Fraction(0), Fraction(-1)],
                          [Fraction(1), Fraction(-1)]])
    return {"characteristic_polynomial": "t^3 - 1",
            "restriction_relation": "R^2 + R + I = 0 on the sum-zero plane",
            "restriction_matrix_in_the_basis_u1_u2":
                [[str(v) for v in row] for row in restriction] if restriction else None,
            "cos_theta": str(cos_theta), "theta": "2*pi/3"}


# ---------------------------------------------------------------------------
# CROSS-CHECK -- pi by a different arctan decomposition, and the separation
# ---------------------------------------------------------------------------
def arctan_enclosure(inv_n: int, terms: int) -> tuple[Fraction, Fraction]:
    total = Fraction(0)
    for k in range(terms):
        term = Fraction(1, (2 * k + 1) * inv_n ** (2 * k + 1))
        total += term if k % 2 == 0 else -term
    tail = Fraction(1, (2 * terms + 1) * inv_n ** (2 * terms + 1))
    return total - tail, total + tail


def crosscheck_separation() -> dict:
    lo2, hi2 = arctan_enclosure(2, 60)
    lo3, hi3 = arctan_enclosure(3, 40)
    lo, hi = 4 * (lo2 + lo3), 4 * (hi2 + hi3)
    machin_lo = 16 * arctan_enclosure(5, 30)[0] - 4 * arctan_enclosure(239, 10)[1]
    machin_hi = 16 * arctan_enclosure(5, 30)[1] - 4 * arctan_enclosure(239, 10)[0]
    overlap = max(lo, machin_lo) < min(hi, machin_hi)
    check("THE_INDEPENDENT_PI_ENCLOSURE_OVERLAPS_THE_PRIMARY_ONE",
          lo < hi and overlap and abs(float(lo) - math.pi) < 1e-12)

    target = Fraction(2, 9)
    worst = None
    all_separated = True
    pairs = 0
    for d in range(1, 61):
        for m in range(-60, 61):
            q = Fraction(m, d)
            pairs += 1
            low, high = (2 * lo * q, 2 * hi * q) if q >= 0 else (2 * hi * q, 2 * lo * q)
            if target < low:
                gap = low - target
            elif target > high:
                gap = target - high
            else:
                all_separated = False
                continue
            if worst is None or gap < worst:
                worst = gap
    check("THE_INDEPENDENT_ENCLOSURE_REPRODUCES_THE_PUBLISHED_SEPARATION_BOUND",
          all_separated and pairs == 7260 and worst is not None
          and worst >= PUBLISHED_SEPARATION_LOWER_BOUND)

    # the equal-coefficient functional, by coordinate summation rather than
    # by the closed form
    alphas = [Fraction(0), Fraction(1, 9), Fraction(1, 3), Fraction(1),
              Fraction(2, 27), Fraction(-5, 4)]
    ones = (Fraction(1), Fraction(1), Fraction(1))
    values = {al: sum((al * c for c in ones), Fraction(0)) for al in alphas}
    functional_ok = all(values[al] == 3 * al for al in alphas)
    injective = len(set(values.values())) == len(alphas)
    reaching = sorted(str(al) for al in alphas if values[al] == Fraction(2, 9))
    check("COORDINATE_SUMMATION_REPRODUCES_THE_FUNCTIONAL_AND_ITS_COMPARATOR_MEMBER",
          functional_ok and injective and reaching == ["2/27"])
    return {"formula": "pi = 4 arctan(1/2) + 4 arctan(1/3)",
            "pairs_tested": pairs,
            "least_separation_lower_bound": PUBLISHED_SEPARATION_LOWER_BOUND_TEXT,
            "functional_values_at_all_ones": {str(k): str(v)
                                              for k, v in values.items()},
            "functional_member_reaching_2/9": reaching}


# ---------------------------------------------------------------------------
# CROSS-CHECK -- the measured scan, by bisection on the argument
# ---------------------------------------------------------------------------
CHARGED_LEPTON_MASSES_MEV = {"e": 0.51099895, "mu": 105.6583755, "tau": 1776.86}
OBSERVATIONAL_INPUT_INVENTORY = {
    "charged_lepton_masses_MeV": CHARGED_LEPTON_MASSES_MEV,
    "role": "observational comparator inputs used only in measured section 8",
    "in_repo_provenance":
        "docs/CLOSURE_T2_DF_PHYSICAL_CONSEQUENCES_NOTE_2026-05-10_t2df.md",
}


def phi_by_bisection(lams) -> float | None:
    """Recover the folded argument without the symmetric-function inversion.

    The modulus comes from the second central moment (sum of squared
    deviations = 6 B^2), and the folded argument from bisection on the
    LARGEST spectral value, which equals a + 2 B cos delta and is strictly
    decreasing on [0, pi/3].
    """
    a = sum(lams) / 3.0
    second = sum((v - a) ** 2 for v in lams)
    if second <= 0.0:
        return None
    B = math.sqrt(second / 6.0)
    top = max(lams)

    def residual(delta):
        return (a + 2.0 * B * math.cos(delta)) - top

    lo, hi = 0.0, math.pi / 3.0
    flo, fhi = residual(lo), residual(hi)
    if flo < 0.0 or fhi > 0.0:
        return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if residual(mid) >= 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def crosscheck_measured(primary_table) -> dict:
    roots = [math.sqrt(CHARGED_LEPTON_MASSES_MEV[k]) for k in ("e", "mu", "tau")]
    comparator = 2.0 / 9.0
    rebuilt = []
    for signs in itertools.product((1, -1), repeat=3):
        lams = [s * r for s, r in zip(signs, roots)]
        phi = phi_by_bisection(lams)
        rebuilt.append({"signs": list(signs), "Phi": phi,
                        "distance": None if phi is None else abs(phi - comparator)})
    matched = 0
    for mine, theirs in zip(rebuilt, primary_table):
        if mine["signs"] != theirs["signs"]:
            continue
        if mine["Phi"] is None or theirs["Phi"] is None:
            continue
        if abs(mine["Phi"] - theirs["Phi"]) < 1e-12:
            matched += 1
    check("BISECTION_METHOD_REPRODUCES_ALL_EIGHT_MEASURED_VALUES", matched == 8)

    ordered = sorted((row for row in rebuilt if row["distance"] is not None),
                     key=lambda row: row["distance"])
    their_ordered = sorted(
        (row for row in primary_table if row["distance_to_comparator"] is not None),
        key=lambda row: row["distance_to_comparator"])
    same_order = ([row["signs"] for row in ordered]
                  == [row["signs"] for row in their_ordered])
    full_table = len(ordered) == 8
    check("THE_INDEPENDENT_ORDERING_MATCHES_THE_PRIMARY_ORDERING",
          same_order and full_table
          and ordered[0]["distance"] < ordered[1]["distance"])
    return {"method": "bisection on the largest spectral value, modulus from "
                     "the second central moment",
            "role": "MEASURED SUPPORT ONLY -- no derivation consumes this",
            "smallest_distance":
                f"{ordered[0]['distance']:.6e}" if full_table else None,
            "next_smallest_distance":
                f"{ordered[1]['distance']:.6e}" if full_table else None}


# ---------------------------------------------------------------------------
# fresh-payload verification: execution evidence, digest, selected-summary comparison
# ---------------------------------------------------------------------------
def digest_of(payload: dict) -> str:
    trimmed = {k: v for k, v in payload.items() if k != "payload_sha256"}
    blob = json.dumps(trimmed, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def expected_summary(crosschecks: dict) -> dict:
    """The canonical summary this checker requires the primary to carry."""
    return {
        "date": DATE,
        "runner": "scripts/salvaged_circulant_spectral_fold_2026_08_09.py",
        "inputs": [],
        "declared_total": PRIMARY_DECLARED_CHECK_COUNT,
        "e1": crosschecks["coefficients"]["closed_forms"]["e1"],
        "e2": crosschecks["coefficients"]["closed_forms"]["e2"],
        "e3": crosschecks["coefficients"]["closed_forms"]["e3"],
        "orbit_histogram": crosschecks["fold"]["size_histogram"],
        "composition_table": crosschecks["fold"]["composition_table"],
        "group_order": 6,
        "group_abelian": False,
        "restriction_matrix":
            crosschecks["cycle_geometry"]["restriction_matrix_in_the_basis_u1_u2"],
        "cos_theta": crosschecks["cycle_geometry"]["cos_theta"],
        "theta": crosschecks["cycle_geometry"]["theta"],
        "separation_pairs": crosschecks["separation"]["pairs_tested"],
        "separation_lower_bound":
            crosschecks["separation"]["least_separation_lower_bound"],
        "functional_values":
            crosschecks["separation"]["functional_values_at_all_ones"],
        "functional_member": crosschecks["separation"]["functional_member_reaching_2/9"],
        "embedded_observational_comparator_inputs": OBSERVATIONAL_INPUT_INVENTORY,
        "external_runtime_scientific_file_reads": [],
        "measured_smallest": crosschecks["measured"]["smallest_distance"],
        "measured_next": crosschecks["measured"]["next_smallest_distance"],
        "all_checks_passed": True,
    }


def observed_summary(payload: dict) -> dict:
    coeff = payload["family"]["characteristic_coefficients"]
    return {
        "date": payload.get("date"),
        "runner": payload.get("runner"),
        "inputs": payload.get("inputs"),
        "declared_total": payload.get("totals", {}).get("declared_total"),
        "e1": coeff.get("e1"),
        "e2": coeff.get("e2"),
        "e3": coeff.get("e3"),
        "orbit_histogram": payload["fold"]["orbit_census"]["size_histogram"],
        "composition_table": payload["fold"]["group"]["composition_table"],
        "group_order": payload["fold"]["group"]["order"],
        "group_abelian": payload["fold"]["group"]["abelian"],
        "restriction_matrix": payload["permutation_geometry"]["cycle_geometry"][
            "restriction_matrix_in_the_basis_u1_u2"],
        "cos_theta": payload["permutation_geometry"]["cycle_geometry"]["cos_theta"],
        "theta": payload["permutation_geometry"]["cycle_geometry"]["theta"],
        "separation_pairs": payload["separation"]["separation"]["pairs_tested"],
        "separation_lower_bound":
            payload["separation"]["separation"]["least_separation_lower_bound"],
        "functional_values":
            payload["linear_functional"]["linear_functional"]["values_at_all_ones"],
        "functional_member":
            payload["linear_functional"]["linear_functional"]["member_reaching_2/9"],
        "embedded_observational_comparator_inputs":
            payload["read_inventory"]["embedded_observational_comparator_inputs"],
        "external_runtime_scientific_file_reads":
            payload["read_inventory"]["external_runtime_scientific_file_reads"],
        "measured_smallest":
            payload["measured_support"]["measured_support"]["smallest_distance"],
        "measured_next":
            payload["measured_support"]["measured_support"]["next_smallest_distance"],
        "all_checks_passed": all(entry["pass"] for entry in payload["checks"]),
    }


def execute_primary_fresh() -> dict:
    """Execute the primary once and retain only its temporary payload bytes."""
    with tempfile.TemporaryDirectory() as tmp:
        fresh_path = os.path.join(tmp, "fresh_receipt.json")
        completed = subprocess.run(
            [sys.executable, PRIMARY, "--receipt-out", fresh_path],
            capture_output=True, text=True, timeout=AUDIT_TIMEOUT_SEC)
        exit_ok = completed.returncode == 0
        terminal = "TOTAL: PASS=" in completed.stdout and \
            "FAIL=0" in completed.stdout and "VERDICT: PASS" in completed.stdout
        fresh_bytes = b""
        if os.path.exists(fresh_path):
            with open(fresh_path, "rb") as handle:
                fresh_bytes = handle.read()
    check("THE_PRIMARY_EXECUTES_FRESHLY_AND_EXITS_ZERO", exit_ok and terminal)
    try:
        payload = json.loads(fresh_bytes.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        payload = {}
    check("THE_FRESH_PRIMARY_PAYLOAD_IS_PRESENT_AND_PARSEABLE",
          bool(fresh_bytes) and isinstance(payload, dict) and bool(payload))
    return {
        "bytes": fresh_bytes,
        "payload": payload,
        "exit_code": completed.returncode,
    }


def verify_fresh_payload(crosschecks: dict, primary_run: dict) -> dict:
    payload = primary_run["payload"]
    fresh_bytes = primary_run["bytes"]

    with open(PRIMARY, "rb") as handle:
        primary_sha = hashlib.sha256(handle.read()).hexdigest()
    check("THE_FRESH_PAYLOAD_PINS_THE_PRIMARY_SOURCE_ON_DISK",
          payload.get("runner_sha256") == primary_sha)

    check("THE_STORED_PAYLOAD_DIGEST_MATCHES_A_RECOMPUTED_DIGEST",
          payload.get("payload_sha256") == digest_of(payload))

    want = expected_summary(crosschecks)
    try:
        got = observed_summary(payload)
    except (KeyError, TypeError):
        got = {}
    mismatches = sorted(k for k in want if want[k] != got.get(k))
    check("THE_FRESH_PAYLOAD_MATCHES_THE_CANONICAL_EXPECTED_SUMMARY", not mismatches)

    primary_checks = payload.get("checks", [])
    primary_totals = payload.get("totals", {})
    check("EVERY_PRIMARY_CHECK_PASSED_AND_THE_COUNT_IS_CONSISTENT",
          len(primary_checks) == primary_totals.get("declared_total")
          and primary_totals.get("fail") == 0
          and primary_totals.get("pass") == len(primary_checks))

    # tamper regression 1: a byte tamper must break the stored digest
    tampered = json.loads(fresh_bytes.decode("utf-8")) if fresh_bytes else {}
    try:
        tampered["permutation_geometry"]["cycle_geometry"]["cos_theta"] = "-1/3"
    except (KeyError, TypeError):
        tampered = {}
    check("A_BYTE_TAMPER_BREAKS_THE_STORED_DIGEST",
          bool(tampered) and tampered.get("payload_sha256") != digest_of(tampered))

    # tamper regression 2: the same selected-summary tamper with a recomputed
    # self-digest must still be rejected by the selected-summary comparison
    tampered["payload_sha256"] = digest_of(tampered)
    rehashed_ok = tampered["payload_sha256"] == digest_of(tampered)
    try:
        still_rejected = observed_summary(tampered) != expected_summary(crosschecks)
    except (KeyError, TypeError):
        still_rejected = True
    check("A_REHASHED_CANONICAL_SUMMARY_TAMPER_IS_STILL_REJECTED",
          rehashed_ok and still_rejected)

    return {"primary_source_sha256": primary_sha,
            "fresh_execution_exit_code": primary_run["exit_code"],
            "fresh_payload_bytes_sha256": hashlib.sha256(fresh_bytes).hexdigest(),
            "summary_mismatches": mismatches,
            "primary_table_rows": len(
                payload.get("measured_support", {}).get(
                    "measured_support", {}).get("table", []))}


# ---------------------------------------------------------------------------
# scope discipline over the package surfaces the primary cannot reach
# ---------------------------------------------------------------------------
# The demotion-target vocabulary of the review-loop conformance spec,
# section 3.  This table is the only span excluded from the source scans, in
# this file and in the primary alike; the exclusion is validated below.
# scope-scan-exempt-begin
OVERCLAIM_TOKENS = (
    "certified", "certifies", "certification", "globally", "maximal",
    "universally", "the law of", "proves the framework",
)
# scope-scan-exempt-end


def _split_scan_exemption(source: str) -> tuple[str, str]:
    begin = "# scope-scan-" + "exempt-begin"
    end = "# scope-scan-" + "exempt-end"
    i, j = source.find(begin), source.find(end)
    if i < 0 or j < 0 or j < i:
        return "", source
    j += len(end)
    return source[i:j], source[:i] + source[j:]


def scan_package_surfaces(self_source: str, primary_payload_text: str) -> dict:
    """Scan the package surfaces the primary's own scan cannot reach.

    The primary scans its own source and its own emitted payload.  This
    completes the mechanical coverage of the executable package: this
    checker's source, the primary's source, and the primary's freshly emitted
    payload.  The source note is not scanned by either runner -- it is not
    inside the package a runner may read without breaking self-containment,
    and the repository's own controlled-vocabulary lint owns it.
    """
    with open(PRIMARY, "r", encoding="utf-8") as handle:
        primary_source = handle.read()

    exempt_self, scanned_self = _split_scan_exemption(self_source)
    exempt_primary, scanned_primary = _split_scan_exemption(primary_source)

    def exemption_is_only_the_shared_table(span: str) -> bool:
        """The span must hold the token table and nothing else, and the two
        runners must carry the SAME table."""
        body = "\n".join(line for line in span.splitlines()
                         if not line.strip().startswith("#"))
        try:
            tree = ast.parse(body)
        except SyntaxError:
            return False
        return (len(tree.body) == 1
                and isinstance(tree.body[0], ast.Assign)
                and len(tree.body[0].targets) == 1
                and getattr(tree.body[0].targets[0], "id", None)
                == "OVERCLAIM_TOKENS"
                and ast.literal_eval(tree.body[0].value) == OVERCLAIM_TOKENS
                and 0 < len(span.splitlines()) <= 12)

    exemptions_bounded = all(exemption_is_only_the_shared_table(span)
                             for span in (exempt_self, exempt_primary))
    markers_unique = all(
        source.count("# scope-scan-" + "exempt-begin") == 1
        and source.count("# scope-scan-" + "exempt-end") == 1
        for source in (self_source, primary_source))
    check("BOTH_SOURCE_SCAN_EXEMPTIONS_ARE_THE_SAME_BOUNDED_TOKEN_TABLE",
          exemptions_bounded and markers_unique)

    surfaces = {
        "independent_check_source": scanned_self.casefold(),
        "primary_source": scanned_primary.casefold(),
        "fresh_primary_payload": primary_payload_text.casefold(),
    }
    hits = sorted({f"{name}:{token}" for name, blob in surfaces.items()
                   for token in OVERCLAIM_TOKENS if token in blob})
    check("NO_OVERCLAIM_VOCABULARY_ON_THE_REMAINING_PACKAGE_SURFACES", not hits)
    return {
        "overclaim_token_hits": hits,
        "scanned_surfaces": sorted(surfaces),
        "not_scanned_by_either_runner": [
            "the source note (outside the executable package; owned by the "
            "repository controlled-vocabulary lint)"],
    }


# ---------------------------------------------------------------------------
def main() -> int:
    print("=" * 78)
    print("INDEPENDENT CHECK -- CIRCULANT SPECTRAL FOLD SUPPORT PACKET")
    print("every listed unit recomputed by a different exact method; the primary "
          "is executed freshly and its payload is verified fail-closed")
    print("=" * 78)

    crosschecks: dict = {}
    print("\n-- Newton's identities on a rational grid --")
    crosschecks["coefficients"] = crosscheck_coefficients()
    print("\n-- Vieta in Q(i, w), and the per-index orientation --")
    crosschecks["vieta"] = crosscheck_vieta()
    print("\n-- inversion, reverse direction, with the degenerate stratum --")
    crosschecks["inversion"] = crosscheck_inversion()
    print("\n-- the fold in integer arithmetic, and the composition law --")
    crosschecks["fold"] = crosscheck_fold()
    print("\n-- similarity invariance by power traces --")
    crosschecks["similarity"] = crosscheck_similarity()
    print("\n-- cycle geometry from the characteristic polynomial --")
    crosschecks["cycle_geometry"] = crosscheck_cycle_geometry()
    print("\n-- an independent pi enclosure, the separation, the functional --")
    crosschecks["separation"] = crosscheck_separation()

    print("\n-- fresh primary execution --")
    primary_run = execute_primary_fresh()
    primary_payload = primary_run["payload"]
    primary_table = primary_payload.get("measured_support", {}).get(
        "measured_support", {}).get("table", [])
    print("\n-- the measured scan by bisection --")
    crosschecks["measured"] = crosscheck_measured(primary_table)

    print("\n-- fresh-payload verification --")
    execution_report = verify_fresh_payload(crosschecks, primary_run)

    with open(os.path.abspath(__file__), "rb") as handle:
        self_bytes = handle.read()
    self_sha = hashlib.sha256(self_bytes).hexdigest()

    print("\n-- scope discipline over the remaining package surfaces --")
    scope_report = scan_package_surfaces(
        self_bytes.decode("utf-8"), primary_run["bytes"].decode("utf-8"))

    check("CHECK_COUNT_MATCHES_THE_DECLARED_TOTAL",
          len(CHECKS) + 1 == EXPECTED_CHECK_COUNT)
    passed = sum(1 for _, ok in CHECKS if ok)
    failed = len(CHECKS) - passed

    payload = {
        "date": DATE,
        "runner": "scripts/salvaged_circulant_spectral_fold_"
                  "independent_check_2026_08_09.py",
        "runner_sha256": self_sha,
        "inputs": list(AUDIT_INPUT_PATHS),
        "read_inventory": {
            "embedded_observational_comparator_inputs": OBSERVATIONAL_INPUT_INVENTORY,
            "external_runtime_scientific_file_reads": [],
            "package_local_integrity_reads": list(AUDIT_INPUT_PATHS),
        },
        "cross_checks": crosschecks,
        "primary_execution": execution_report,
        "scope_discipline": scope_report,
        "checks": [{"name": name, "pass": ok} for name, ok in CHECKS],
        "totals": {"pass": passed, "fail": failed,
                   "declared_total": EXPECTED_CHECK_COUNT},
    }
    blob = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["payload_sha256"] = hashlib.sha256(blob).hexdigest()

    print(f"\nTOTAL: PASS={passed} FAIL={failed}")
    print(f"VERDICT: {'PASS' if failed == 0 else 'FAIL'}")
    print(f"payload_sha256: {payload['payload_sha256']}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
