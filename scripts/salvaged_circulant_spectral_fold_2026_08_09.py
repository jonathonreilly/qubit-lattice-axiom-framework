#!/usr/bin/env python3
"""Primary check: exact algebra of the three-dimensional Hermitian
circulant spectral fold, on definitions stipulated in this file, plus one
explicitly measured signed-root scan reported as observational support.

Scope of this runner.  Every object it computes with is stipulated in this
docstring and in the code below.  It derives nothing from the framework
axioms and identifies nothing with a physical readout: every line it prints
is a statement about the stipulated objects and about nothing else.
Sections 1-7 are exact rational/integer arithmetic; section 8 is a
floating-point measurement against imported charged-lepton masses and is
labelled as such at every surface it touches.

Read inventory (three kinds, kept separate).

  * Embedded observational comparator inputs: m_e = 0.51099895 MeV,
    m_mu = 105.6583755 MeV, and m_tau = 1776.86 MeV, used only in the
    measured section 8 with the provenance and non-derivational role stated
    there.
  * External runtime scientific file reads: NONE.  This runner reads no note,
    receipt, ledger, git object, or other runner.  It declares no
    ``AUDIT_INPUT_PATHS``.
  * Package-local integrity reads: exactly one -- this runner reads its own
    source file, both to bind its emitted payload and to scan that source
    text in section 9.

Stipulated objects.

  C            the 3-cycle permutation matrix with (C v)_0 = v_2,
               (C v)_1 = v_0, (C v)_2 = v_1
  H(a, b)      a*I + b*C + conj(b)*C^T, for real a and complex b = x + i y
  B, delta     the modulus and argument of b, so x = B cos delta and
               y = B sin delta
  e1, e2, e3   the coefficients of the characteristic polynomial of H:
               trace, sum of principal 2x2 minors, determinant
  Phi          (1/3) arccos(cos 3 delta), the folded argument recovered
               from an unordered spectrum with B > 0
  I_alpha      the equal-coefficient linear functional
               v -> alpha (v_0 + v_1 + v_2) on Q^3, for rational alpha

Sections.

  1. the family is self-adjoint and its characteristic coefficients are
     exact polynomials in (a, x, y); the eigenvectors are the three
     discrete-Fourier vectors, verified over the Eisenstein integers, with
     the argument orientation stated explicitly
  2. exact inversion of the unordered spectrum on B > 0, with the
     degenerate stratum B = 0 excluded by an exact witness and the fold
     range proved by an exact sum-of-two-squares identity
  3. the dihedral fold: the unordered spectrum is invariant under
     delta -> delta + 2 pi / 3 and delta -> -delta; the generated group is
     the order-six dihedral group whose composition law carries the outer
     reflection sign on the inner translation,
     (s2, k2) . (s1, k1) = (s2 s1, s2 k1 + k2 mod 3), and the preimage
     count is six generically and three at the six fold endpoints
     delta in (pi/3) Z
  4. Phi is a function of the characteristic coefficients alone, hence
     invariant under arbitrary similarity -- not only under transformations
     preserving the circulant form
  5. the 3-cycle permutation matrix fixes the all-ones line and restricts
     to the sum-zero plane as a rotation of angle 2 pi / 3
  6. the equal-coefficient functional: I_alpha(1,1,1) = 3 alpha, injective
     in alpha, with a unique member reaching the stipulated comparator 2/9
  7. a bounded exact separation: 2/9 differs from 2 pi q for every rational
     q in a declared finite family, verified against a rational enclosure of
     pi computed in-file with an alternating-series tail bound
  8. MEASURED SUPPORT ONLY: the eight signed-root assignments built from
     three imported charged-lepton masses, with the full table of distances
     to the stipulated comparator 2/9 published and no threshold applied

Fail-closed discipline.  Every check computes both sides; there are no
supplied verdict booleans anywhere in this file.  A check-count gate rejects
silently skipped sections.  Any failure prints FAIL and the process exits 1.
Exit 0 only on a full real PASS.  When ``--receipt-out`` is supplied, the
optional receipt is byte-deterministic and contains no timestamp.  A normal
run writes no repository output.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import math
import os
import sys
from fractions import Fraction

AUDIT_TIMEOUT_SEC = 120

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DATE = "2026-08-09"
EXPECTED_CHECK_COUNT = 45
PUBLISHED_SEPARATION_LOWER_BOUND = Fraction(3519, 2_000_000)
PUBLISHED_SEPARATION_LOWER_BOUND_TEXT = "1.7595e-03"

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok))
    print(f"{'PASS' if ok else 'FAIL'} {name}")
    return ok


# ---------------------------------------------------------------------------
# exact scalars: Gaussian rationals
# ---------------------------------------------------------------------------
class CQ:
    """An exact Gaussian rational re + im*i with re, im in Q."""

    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = Fraction(re)
        self.im = Fraction(im)

    def __add__(self, o):
        return CQ(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return CQ(self.re - o.re, self.im - o.im)

    def __neg__(self):
        return CQ(-self.re, -self.im)

    def __mul__(self, o):
        return CQ(self.re * o.re - self.im * o.im,
                  self.re * o.im + self.im * o.re)

    def conj(self):
        return CQ(self.re, -self.im)

    def inv(self):
        n = self.re * self.re + self.im * self.im
        if n == 0:
            raise ZeroDivisionError("zero Gaussian rational")
        return CQ(self.re / n, -self.im / n)

    def is_zero(self):
        return self.re == 0 and self.im == 0

    def __eq__(self, o):
        return isinstance(o, CQ) and self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def __repr__(self):
        return f"({self.re}{'+' if self.im >= 0 else '-'}{abs(self.im)}i)"


CQ0 = CQ(0, 0)
CQ1 = CQ(1, 0)


# ---------------------------------------------------------------------------
# exact polynomials in three real variables with Gaussian-rational
# coefficients.  Monomial key = (i, j, k) meaning v0^i v1^j v2^k.
# ---------------------------------------------------------------------------
class Poly:
    __slots__ = ("terms",)

    def __init__(self, terms=None):
        self.terms = {}
        if terms:
            for mono, coef in terms.items():
                if not coef.is_zero():
                    self.terms[mono] = coef

    @staticmethod
    def const(c: CQ):
        return Poly({(0, 0, 0): c})

    @staticmethod
    def var(index: int):
        mono = [0, 0, 0]
        mono[index] = 1
        return Poly({tuple(mono): CQ1})

    def __add__(self, o):
        out = dict(self.terms)
        for mono, coef in o.terms.items():
            merged = out.get(mono, CQ0) + coef
            if merged.is_zero():
                out.pop(mono, None)
            else:
                out[mono] = merged
        return Poly(out)

    def __neg__(self):
        return Poly({m: -c for m, c in self.terms.items()})

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, o):
        out: dict = {}
        for m1, c1 in self.terms.items():
            for m2, c2 in o.terms.items():
                mono = (m1[0] + m2[0], m1[1] + m2[1], m1[2] + m2[2])
                merged = out.get(mono, CQ0) + c1 * c2
                if merged.is_zero():
                    out.pop(mono, None)
                else:
                    out[mono] = merged
        return Poly(out)

    def conj(self):
        return Poly({m: c.conj() for m, c in self.terms.items()})

    def scaled(self, c: CQ):
        return self * Poly.const(c)

    def is_zero(self):
        return not self.terms

    def __eq__(self, o):
        return isinstance(o, Poly) and self.terms == o.terms

    def evaluate(self, v0: Fraction, v1: Fraction, v2: Fraction) -> CQ:
        total = CQ0
        for (i, j, k), coef in self.terms.items():
            weight = Fraction(v0 ** i) * Fraction(v1 ** j) * Fraction(v2 ** k)
            total = total + CQ(coef.re * weight, coef.im * weight)
        return total

    def __repr__(self):
        if not self.terms:
            return "0"
        return " + ".join(
            f"{c}*a^{m[0]}x^{m[1]}y^{m[2]}" for m, c in sorted(self.terms.items()))


ZERO = Poly()
ONE = Poly.const(CQ1)
PA = Poly.var(0)          # a
PX = Poly.var(1)          # x = Re b
PY = Poly.var(2)          # y = Im b


def int_poly(n: int) -> Poly:
    return Poly.const(CQ(n, 0))


# ---------------------------------------------------------------------------
# exact 3x3 matrices over Poly and over CQ
# ---------------------------------------------------------------------------
CYCLE = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]          # (C v)_0 = v_2, etc.


def mat_trace(M):
    total = M[0][0]
    for i in (1, 2):
        total = total + M[i][i]
    return total


def mat_second_invariant(M):
    total = None
    for i, j in itertools.combinations(range(3), 2):
        block = M[i][i] * M[j][j] - M[i][j] * M[j][i]
        total = block if total is None else total + block
    return total


def mat_det3(M):
    total = None
    for perm in itertools.permutations(range(3)):
        sign = 1
        for p, q in itertools.combinations(range(3), 2):
            if perm[p] > perm[q]:
                sign = -sign
        term = M[0][perm[0]] * M[1][perm[1]] * M[2][perm[2]]
        if sign < 0:
            term = -term
        total = term if total is None else total + term
    return total


def poly_H():
    """H(a, b) = a I + b C + conj(b) C^T with b = x + i y, entries in Poly."""
    b = PX + PY.scaled(CQ(0, 1))
    bbar = PX - PY.scaled(CQ(0, 1))
    rows = []
    for i in range(3):
        row = []
        for j in range(3):
            entry = ZERO
            if i == j:
                entry = entry + PA
            if CYCLE[i][j]:
                entry = entry + b
            if CYCLE[j][i]:
                entry = entry + bbar
            row.append(entry)
        rows.append(row)
    return rows


def cq_mat_mul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(3)), CQ0) for j in range(3)]
            for i in range(3)]


def cq_mat_inv(A):
    """Exact inverse of a 3x3 Gaussian-rational matrix by Gauss-Jordan."""
    aug = [[A[i][j] for j in range(3)] + [CQ1 if i == j else CQ0 for j in range(3)]
           for i in range(3)]
    for col in range(3):
        pivot = next((r for r in range(col, 3) if not aug[r][col].is_zero()), None)
        if pivot is None:
            raise ZeroDivisionError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col].inv()
        aug[col] = [scale * v for v in aug[col]]
        for r in range(3):
            if r != col and not aug[r][col].is_zero():
                factor = aug[r][col]
                aug[r] = [v - factor * w for v, w in zip(aug[r], aug[col])]
    return [row[3:] for row in aug]


def cq_H(a: Fraction, x: Fraction, y: Fraction):
    b = CQ(x, y)
    rows = []
    for i in range(3):
        row = []
        for j in range(3):
            entry = CQ0
            if i == j:
                entry = entry + CQ(a, 0)
            if CYCLE[i][j]:
                entry = entry + b
            if CYCLE[j][i]:
                entry = entry + b.conj()
            row.append(entry)
        rows.append(row)
    return rows


# ---------------------------------------------------------------------------
# SECTION 1 -- the self-adjoint circulant family and its characteristic
# coefficients, as exact polynomial identities
# ---------------------------------------------------------------------------
def section_family() -> dict:
    out: dict = {}
    H = poly_H()

    dagger = [[H[j][i].conj() for j in range(3)] for i in range(3)]
    self_adjoint = all(H[i][j] == dagger[i][j] for i in range(3) for j in range(3))
    check("SELF_ADJOINT_AS_A_POLYNOMIAL_IDENTITY_IN_A_X_Y", self_adjoint)

    e1 = mat_trace(H)
    e2 = mat_second_invariant(H)
    e3 = mat_det3(H)
    bnorm = PX * PX + PY * PY
    want_e1 = PA.scaled(CQ(3, 0))
    want_e2 = (PA * PA).scaled(CQ(3, 0)) - bnorm.scaled(CQ(3, 0))
    want_e3 = (PA * PA * PA) - (PA * bnorm).scaled(CQ(3, 0)) \
        + (PX * PX * PX).scaled(CQ(2, 0)) - (PX * PY * PY).scaled(CQ(6, 0))
    check("TRACE_EQUALS_THREE_A_IDENTICALLY", (e1 - want_e1).is_zero())
    check("SECOND_INVARIANT_EQUALS_THREE_A_SQUARED_MINUS_THREE_B_SQUARED",
          (e2 - want_e2).is_zero())
    check("DETERMINANT_EQUALS_THE_STATED_CUBIC_IDENTICALLY",
          (e3 - want_e3).is_zero())
    out["characteristic_coefficients"] = {
        "e1": "3*a",
        "e2": "3*a^2 - 3*(x^2 + y^2)",
        "e3": "a^3 - 3*a*(x^2 + y^2) + 2*(x^3 - 3*x*y^2)",
        "verified_as": "exact polynomial identity over Q(i)[a, x, y]",
    }

    # the triple-angle reduction that turns 2*(x^3 - 3xy^2) into 2 B^3 cos 3 delta:
    # with c = cos delta and s = sin delta, (c^3 - 3 c s^2) - (4 c^3 - 3 c)
    # equals -3 c (c^2 + s^2 - 1), which vanishes on the unit circle.
    pc, ps = PX, PY
    lhs = (pc * pc * pc) - (pc * ps * ps).scaled(CQ(3, 0))
    cheb = (pc * pc * pc).scaled(CQ(4, 0)) - pc.scaled(CQ(3, 0))
    circle = (pc * pc) + (ps * ps) - ONE
    residue = lhs - cheb + (pc * circle).scaled(CQ(3, 0))
    check("TRIPLE_ANGLE_REDUCTION_HOLDS_MODULO_THE_UNIT_CIRCLE",
          residue.is_zero() and not (lhs - cheb).is_zero())
    out["triple_angle"] = {
        "identity": "(c^3 - 3*c*s^2) - (4*c^3 - 3*c) = -3*c*(c^2 + s^2 - 1)",
        "consequence": "x^3 - 3*x*y^2 = B^3 cos(3 delta) when (x, y) = "
                       "(B cos delta, B sin delta)",
    }

    # Eisenstein-integer verification of the discrete-Fourier eigenvectors.
    # An element p + q w of Z[w], w^2 = -1 - w.
    def emul(u, v):
        (p1, q1), (p2, q2) = u, v
        return (p1 * p2 - q1 * q2, p1 * q2 + p2 * q1 - q1 * q2)

    def epow(u, n):
        acc = (1, 0)
        for _ in range(n):
            acc = emul(acc, u)
        return acc

    def eapply(M, v):
        """Act with an integer matrix on a vector of Eisenstein integers."""
        out_vec = []
        for i in range(3):
            acc = (0, 0)
            for j in range(3):
                if M[i][j]:
                    acc = (acc[0] + M[i][j] * v[j][0], acc[1] + M[i][j] * v[j][1])
            out_vec.append(acc)
        return out_vec

    w = (0, 1)
    cube_root = epow(w, 3) == (1, 0) and epow(w, 1) != (1, 0)
    transpose = [[CYCLE[j][i] for j in range(3)] for i in range(3)]
    eig_ok = True
    opposite_orientation_fails = False
    orientation = {}
    for k in range(3):
        v = [epow(w, (k * t) % 3) for t in range(3)]
        # both actions are computed FROM the stipulated matrix, not written
        # out by hand, so the orientation cannot drift from the definition
        cv = eapply(CYCLE, v)
        ctv = eapply(transpose, v)
        lam_c = epow(w, (-k) % 3)
        lam_ct = epow(w, k % 3)
        if any(cv[t] != emul(lam_c, v[t]) for t in range(3)):
            eig_ok = False
        if any(ctv[t] != emul(lam_ct, v[t]) for t in range(3)):
            eig_ok = False
        # non-vacuity: for k = 1, 2 the OPPOSITE assignment is per-index
        # wrong, so the stated orientation is a real fact and not a label
        if any(cv[t] != emul(lam_ct, v[t]) for t in range(3)):
            opposite_orientation_fails = True
        orientation[k] = {"C_eigenvalue": "w^{-%d}" % k, "CT_eigenvalue": "w^{%d}" % k}
    check("DISCRETE_FOURIER_VECTORS_DIAGONALISE_THE_CYCLE_OVER_EISENSTEIN_INTEGERS",
          cube_root and eig_ok)
    check("THE_CYCLE_MATRIX_DIFFERS_FROM_ITS_TRANSPOSE_SO_THE_TWO_ACTIONS_DIFFER",
          transpose != CYCLE)
    check("THE_OPPOSITE_PER_INDEX_ORIENTATION_FAILS_THE_EIGENVECTOR_EQUATION",
          opposite_orientation_fails)
    out["eigenvectors"] = {
        "vector": "v_k = (1, w^k, w^{2k}) with w a primitive cube root of unity",
        "per_index_eigenvalue_of_H": "a + 2 B cos(delta - 2 pi k / 3)",
        "orientation": orientation,
        "note": "the per-index argument carries a MINUS sign with these "
                "eigenvectors; the two three-element argument multisets "
                "coincide because k -> -k is a bijection of Z/3",
    }

    # the orientation multiset coincidence, exact in Q/Z (turns, not radians)
    turns = [Fraction(j, q) for q in (1, 2, 3, 4, 5, 7, 8, 11, 13, 17)
             for j in range(q)]
    coincide = all(
        sorted(((u - Fraction(k, 3)) % 1) for k in range(3))
        == sorted(((u + Fraction(k, 3)) % 1) for k in range(3)) for u in turns)
    check("PLUS_AND_MINUS_INDEX_ARGUMENT_MULTISETS_COINCIDE",
          coincide and len(turns) == 71)
    out["argument_multiset_orientation"] = {
        "turn_samples": len(turns),
        "statement": "{u - k/3} = {u + k/3} as multisets in Q/Z",
    }
    return out


# ---------------------------------------------------------------------------
# SECTION 2 -- exact inversion on B > 0
# ---------------------------------------------------------------------------
def section_inversion() -> dict:
    out: dict = {}
    H = poly_H()
    e1, e2, e3 = mat_trace(H), mat_second_invariant(H), mat_det3(H)
    bnorm = PX * PX + PY * PY

    disc = e1 * e1 - e2.scaled(CQ(3, 0))
    check("DISCRIMINANT_IDENTITY_GIVES_NINE_B_SQUARED",
          (disc - bnorm.scaled(CQ(9, 0))).is_zero())

    numerator = e3 - (PA * PA * PA) + (PA * bnorm).scaled(CQ(3, 0))
    twice_re_bcube = (PX * PX * PX).scaled(CQ(2, 0)) - (PX * PY * PY).scaled(CQ(6, 0))
    check("COSINE_NUMERATOR_IDENTITY_GIVES_TWICE_B_CUBED_COS_THREE_DELTA",
          (numerator - twice_re_bcube).is_zero())

    # |b^3|^2 = (Re b^3)^2 + (Im b^3)^2 bounds the fold argument exactly.
    re_bcube = (PX * PX * PX) - (PX * PY * PY).scaled(CQ(3, 0))
    im_bcube = (PX * PX * PY).scaled(CQ(3, 0)) - (PY * PY * PY)
    check("SUM_OF_TWO_SQUARES_IDENTITY_BOUNDS_THE_FOLD_ARGUMENT",
          ((bnorm * bnorm * bnorm) - (re_bcube * re_bcube)
           - (im_bcube * im_bcube)).is_zero())

    # The identity above uses only the SQUARES of the two parts, so it is
    # blind to a sign flip in either of them.  Pin both signs directly by
    # expanding b^3 = (x + i y)^3 and separating it into real and imaginary
    # parts as an exact polynomial identity.
    b_poly = PX + PY.scaled(CQ(0, 1))
    b_cubed = b_poly * b_poly * b_poly
    residual = b_cubed - re_bcube - im_bcube.scaled(CQ(0, 1))
    check("THE_CUBE_OF_B_HAS_EXACTLY_THE_STATED_REAL_AND_IMAGINARY_PARTS",
          residual.is_zero() and not im_bcube.is_zero())
    out["fold_range"] = {
        "identity": "(x^2 + y^2)^3 = (x^3 - 3*x*y^2)^2 + (3*x^2*y - y^3)^2",
        "consequence": "|cos 3 delta| <= 1, so Phi = arccos(cos 3 delta)/3 "
                       "lies in [0, pi/3]",
    }

    # exact round trip on rational samples: (a, x, y) -> (e1, e2, e3) -> back
    samples = [(Fraction(1, 2), Fraction(3, 5), Fraction(-2, 7)),
               (Fraction(-4), Fraction(1), Fraction(1)),
               (Fraction(0), Fraction(2, 3), Fraction(0)),
               (Fraction(7, 3), Fraction(-5, 4), Fraction(9, 8))]
    round_trip = []
    trip_ok = True
    for a, x, y in samples:
        v1 = e1.evaluate(a, x, y)
        v2 = e2.evaluate(a, x, y)
        v3 = e3.evaluate(a, x, y)
        if v1.im or v2.im or v3.im:
            trip_ok = False
        rec_a = v1.re / 3
        rec_bsq = (v1.re * v1.re - 3 * v2.re) / 9
        rec_num = v3.re - rec_a ** 3 + 3 * rec_a * rec_bsq
        want_num = 2 * (x ** 3 - 3 * x * y ** 2)
        if not (rec_a == a and rec_bsq == x * x + y * y and rec_num == want_num):
            trip_ok = False
        round_trip.append({"a": str(a), "x": str(x), "y": str(y),
                           "recovered_a": str(rec_a),
                           "recovered_B_squared": str(rec_bsq),
                           "recovered_2_B_cubed_cos3delta": str(rec_num)})
    check("EXACT_ROUND_TRIP_FROM_CHARACTERISTIC_COEFFICIENTS", trip_ok)
    out["round_trip"] = round_trip

    # the degenerate stratum: B = 0 is a single point of the (x, y) plane, so
    # the argument is not a coordinate there at all
    degenerate = []
    deg_ok = True
    for a_val in (Fraction(3), Fraction(-1, 2), Fraction(0)):
        v1 = e1.evaluate(a_val, Fraction(0), Fraction(0))
        v2 = e2.evaluate(a_val, Fraction(0), Fraction(0))
        v3 = e3.evaluate(a_val, Fraction(0), Fraction(0))
        degenerate.append({"a": str(a_val), "e1": str(v1.re), "e2": str(v2.re),
                           "e3": str(v3.re)})
        triple_root = (v1.re == 3 * a_val and v2.re == 3 * a_val ** 2
                       and v3.re == a_val ** 3)
        if not (v1.re * v1.re - 3 * v2.re == 0 and triple_root):
            deg_ok = False
    check("DEGENERATE_STRATUM_IS_EXCLUDED_BY_AN_EXACT_WITNESS", deg_ok)
    out["degenerate_stratum"] = {
        "witness": degenerate,
        "statement": "B = 0 forces x = y = 0, the spectrum is the triple root "
                     "{a, a, a}, the discriminant vanishes, and the inversion's "
                     "denominator 2 B^3 is zero, so Phi is undefined there and "
                     "the argument is not a coordinate on that stratum",
    }
    return out


# ---------------------------------------------------------------------------
# SECTION 3 -- the dihedral fold and the preimage count
# ---------------------------------------------------------------------------
def dihedral_orbit(u: Fraction) -> set:
    return {((sign * u + Fraction(k, 3)) % 1) for sign in (1, -1) for k in range(3)}


def section_fold() -> dict:
    out: dict = {}

    def arg_set(u: Fraction):
        return sorted(((u + Fraction(k, 3)) % 1) for k in range(3))

    turns = [Fraction(j, q) for q in range(1, 25) for j in range(q)]

    rot_ok = all(arg_set(u + Fraction(1, 3)) == arg_set(u) for u in turns)
    check("ROTATION_GENERATOR_FIXES_THE_ARGUMENT_MULTISET", rot_ok)

    refl_ok = all(sorted((-t) % 1 for t in arg_set(u)) == arg_set(-u)
                  for u in turns)
    check("REFLECTION_GENERATOR_MAPS_THE_ARGUMENT_MULTISET_TO_ITS_NEGATIVE",
          refl_ok)

    # the generated group has order six on a generic point
    probe = Fraction(1, 7)
    images = [((sign * probe + Fraction(k, 3)) % 1)
              for sign in (1, -1) for k in range(3)]
    check("THE_SIX_IMAGES_OF_A_GENERIC_ARGUMENT_ARE_DISTINCT",
          len(set(images)) == 6)

    # The composition law, verified as a law and not merely as membership in
    # an already-enumerated orbit.  Membership cannot see a dropped sign:
    # the orbit is stable under BOTH generators, so every mangled composite
    # still lands inside it.  What follows instead identifies the composite
    # map by its own action and requires it to be the predicted element.
    elements = [(s, k) for s in (1, -1) for k in range(3)]
    law_probes = [Fraction(1, 7), Fraction(2, 11), Fraction(5, 13),
                  Fraction(3, 17), Fraction(7, 19)]

    def act(element, u):
        s, k = element
        return (s * u + Fraction(k, 3)) % 1

    def identify(values):
        """The unique stipulated element whose action matches `values`."""
        found = [e for e in elements
                 if [act(e, u) for u in law_probes] == values]
        return found[0] if len(found) == 1 else None

    law_ok = True
    table: dict[tuple, dict[tuple, tuple]] = {}
    for outer in elements:                      # outer = (s2, k2), applied second
        table[outer] = {}
        for inner in elements:                  # inner = (s1, k1), applied first
            composite = [act(outer, act(inner, u)) for u in law_probes]
            identified = identify(composite)
            predicted = (outer[0] * inner[0],
                         (outer[0] * inner[1] + outer[1]) % 3)
            # (0, 0) is not a stipulated element, so an unidentifiable
            # composite fails the Latin-square test below rather than
            # raising during the sort
            table[outer][inner] = identified if identified is not None else (0, 0)
            if identified is None or identified != predicted:
                law_ok = False
    check("THE_COMPOSITION_LAW_CARRIES_THE_OUTER_SIGN_ON_THE_INNER_TRANSLATION",
          law_ok and len(law_probes) == 5)

    # A Latin square is exactly what a group table is, and it is what a
    # dropped outer sign destroys: the composite would stop depending on the
    # outer reflection, so a column would repeat.
    rows_ok = all(sorted(table[outer].values()) == sorted(elements)
                  for outer in elements)
    cols_ok = all(sorted(table[outer][inner] for outer in elements)
                  == sorted(elements) for inner in elements)
    check("THE_SIX_BY_SIX_COMPOSITION_TABLE_IS_A_LATIN_SQUARE",
          rows_ok and cols_ok and len(table) == 6)

    # Order of composition is load-bearing: this group is not abelian.
    rot, refl = (1, 1), (-1, 0)
    rot_then_refl = identify([act(refl, act(rot, u)) for u in law_probes])
    refl_then_rot = identify([act(rot, act(refl, u)) for u in law_probes])
    check("COMPOSITION_ORDER_CHANGES_THE_RESULT_ON_A_NAMED_PAIR",
          rot_then_refl is not None and refl_then_rot is not None
          and rot_then_refl != refl_then_rot)

    out["group"] = {
        "elements": "u -> s*u + k/3 for s in {+1, -1} and k in {0, 1, 2}",
        "composition_law": "(s2, k2) . (s1, k1) = (s2*s1, (s2*k1 + k2) mod 3), "
                           "where the right factor acts first; the outer "
                           "reflection sign multiplies the inner translation",
        # the table as computed, so the emitted value moves with the code
        "composition_table": {
            f"{outer[0]},{outer[1]}|{inner[0]},{inner[1]}":
                f"{table[outer][inner][0]},{table[outer][inner][1]}"
            for outer in elements for inner in elements},
        "verified_by": "each composite is identified by its own action on five "
                       "generic arguments and compared with the predicted "
                       "element; the resulting 6 x 6 table is a Latin square; "
                       "the group is non-abelian, so composition order is "
                       "load-bearing",
        "order": 6,
        "abelian": False,
    }

    sizes = {}
    dichotomy_ok = True
    endpoint_ok = True
    for u in turns:
        size = len(dihedral_orbit(u))
        sizes[size] = sizes.get(size, 0) + 1
        if size not in (3, 6):
            dichotomy_ok = False
        is_endpoint = (6 * u).denominator == 1
        if (size == 3) != is_endpoint:
            endpoint_ok = False
    check("ORBIT_SIZE_IS_SIX_GENERICALLY_AND_THREE_AT_THE_FOLD_ENDPOINTS",
          dichotomy_ok and endpoint_ok and sorted(sizes) == [3, 6])
    out["orbit_census"] = {"turn_samples": len(turns),
                           "size_histogram": {str(k): v for k, v in sorted(sizes.items())}}

    # the six endpoints in one turn, and the fold values they carry
    endpoints = sorted(u for u in {Fraction(m, 6) for m in range(6)})
    endpoint_sizes = {str(u): len(dihedral_orbit(u)) for u in endpoints}
    check("THE_SIX_ENDPOINTS_ARE_EXACTLY_THE_MULTIPLES_OF_ONE_SIXTH_TURN",
          len(endpoints) == 6 and set(endpoint_sizes.values()) == {3})
    out["fold_endpoints"] = {
        "turns": [str(u) for u in endpoints],
        "radians": "delta in {0, pi/3, 2 pi/3, pi, 4 pi/3, 5 pi/3}",
        "orbit_sizes": endpoint_sizes,
        "fold_values": "cos 3 delta = +-1 there, so Phi is 0 or pi/3",
    }

    out["preimage_statement"] = (
        "for an unordered spectrum with B > 0 the set of delta in [0, 2 pi) "
        "carrying it is exactly the dihedral orbit: six arguments generically, "
        "three at the six fold endpoints")
    return out


# ---------------------------------------------------------------------------
# SECTION 4 -- Phi is a similarity invariant
# ---------------------------------------------------------------------------
def section_invariance() -> dict:
    out: dict = {}
    a, x, y = Fraction(1, 3), Fraction(5, 4), Fraction(-2, 3)
    H = cq_H(a, x, y)
    base = (mat_trace(H), mat_second_invariant(H), mat_det3(H))

    transforms = [
        [[CQ(1), CQ(0, 1), CQ(0)], [CQ(0), CQ(2), CQ(1)], [CQ(1), CQ(0), CQ(3)]],
        [[CQ(2), CQ(1), CQ(0)], [CQ(0), CQ(1, 1), CQ(5)], [CQ(1), CQ(0), CQ(1)]],
        [[CQ(0), CQ(1), CQ(0)], [CQ(0), CQ(0), CQ(1)], [CQ(1), CQ(0), CQ(0)]],
    ]
    cyc = [[CQ(v) for v in row] for row in CYCLE]
    invariance_ok = True
    left_the_form_class = 0
    for S in transforms:
        Sinv = cq_mat_inv(S)
        conj = cq_mat_mul(cq_mat_mul(S, H), Sinv)
        got = (mat_trace(conj), mat_second_invariant(conj), mat_det3(conj))
        if got != base:
            invariance_ok = False
        left, right = cq_mat_mul(conj, cyc), cq_mat_mul(cyc, conj)
        if any(not (left[i][j] - right[i][j]).is_zero()
               for i in range(3) for j in range(3)):
            left_the_form_class += 1
    check("CHARACTERISTIC_COEFFICIENTS_SURVIVE_EXACT_SIMILARITY", invariance_ok)
    check("AT_LEAST_ONE_SIMILARITY_LEAVES_THE_CIRCULANT_FORM_CLASS",
          left_the_form_class >= 1)

    # an exact witness that the coefficients are not constant on the
    # self-adjoint cone: adding a real diagonal moves the trace
    moved = [[H[i][j] + (CQ(1) if (i, j) == (0, 0) else CQ0) for j in range(3)]
             for i in range(3)]
    moved_inv = (mat_trace(moved), mat_second_invariant(moved), mat_det3(moved))
    check("A_SELF_ADJOINT_PERTURBATION_MOVES_THE_COEFFICIENTS",
          moved_inv != base and moved_inv[0] == base[0] + CQ(1))

    out["similarity"] = {
        "base_coefficients": [str(v) for v in base],
        "transforms_tested": len(transforms),
        "transforms_leaving_the_circulant_form_class": left_the_form_class,
        "statement": "Phi depends on H only through (e1, e2, e3), which are "
                     "similarity invariants, so Phi is invariant under "
                     "arbitrary similarity and in particular under arbitrary "
                     "unitary conjugation",
    }
    return out


# ---------------------------------------------------------------------------
# SECTION 5 -- the 3-cycle permutation matrix
# ---------------------------------------------------------------------------
def section_permutation_geometry() -> dict:
    out: dict = {}
    C = [[Fraction(v) for v in row] for row in CYCLE]

    def apply(M, v):
        return [sum(M[i][j] * v[j] for j in range(3)) for i in range(3)]

    ones = [Fraction(1)] * 3
    fixes_line = apply(C, ones) == ones

    # orthogonality, exactly
    orth = all(
        sum(C[k][i] * C[k][j] for k in range(3)) == (1 if i == j else 0)
        for i in range(3) for j in range(3))
    check("THE_CYCLE_MATRIX_IS_ORTHOGONAL_AND_FIXES_THE_ALL_ONES_LINE",
          orth and fixes_line)

    # the fixed subspace is exactly one-dimensional: rank(C - I) = 2
    rows = [[C[i][j] - (Fraction(1) if i == j else Fraction(0)) for j in range(3)]
            for i in range(3)]
    rank = 0
    work = [row[:] for row in rows]
    for col in range(3):
        pivot = next((r for r in range(rank, 3) if work[r][col] != 0), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inv = Fraction(1) / work[rank][col]
        work[rank] = [inv * v for v in work[rank]]
        for r in range(3):
            if r != rank and work[r][col] != 0:
                f = work[r][col]
                work[r] = [v - f * u for v, u in zip(work[r], work[rank])]
        rank += 1
    check("THE_FIXED_SUBSPACE_IS_EXACTLY_THE_ALL_ONES_LINE", rank == 2)

    # the sum-zero plane is invariant; the restriction has trace -1 and det 1
    u1 = [Fraction(1), Fraction(-1), Fraction(0)]
    u2 = [Fraction(0), Fraction(1), Fraction(-1)]
    cu1, cu2 = apply(C, u1), apply(C, u2)

    def coords(v):
        # solve alpha*u1 + beta*u2 = v on the sum-zero plane
        alpha = v[0]
        beta = -v[2]
        rebuilt = [alpha * u1[i] + beta * u2[i] for i in range(3)]
        return (alpha, beta) if rebuilt == v else None

    c1, c2 = coords(cu1), coords(cu2)
    invariant = c1 is not None and c2 is not None and sum(cu1) == 0 and sum(cu2) == 0
    restriction_trace = (c1[0] + c2[1]) if invariant else None
    restriction_det = (c1[0] * c2[1] - c2[0] * c1[1]) if invariant else None
    check("THE_SUM_ZERO_PLANE_IS_INVARIANT_WITH_TRACE_MINUS_ONE_AND_DET_ONE",
          invariant and restriction_trace == -1 and restriction_det == 1)

    # Trace and determinant are blind to a transposed or sign-flipped
    # restriction (the transpose has the same trace and determinant), so pin
    # the matrix entry by entry.  Columns are the coordinates of the images.
    restriction = [[c1[0], c2[0]], [c1[1], c2[1]]] if invariant else None
    check("THE_PLANE_RESTRICTION_MATRIX_IS_EXACTLY_THE_STATED_ONE",
          restriction == [[Fraction(0), Fraction(-1)],
                          [Fraction(1), Fraction(-1)]])

    # an orthogonal plane map of determinant 1 is a rotation; its trace is
    # 2 cos theta, so cos theta = -1/2 and theta = 2 pi / 3 exactly
    cos_theta = (restriction_trace / 2) if invariant else None
    check("THE_NORMAL_PLANE_ROTATION_ANGLE_IS_TWO_PI_OVER_THREE",
          cos_theta == Fraction(-1, 2))
    out["cycle_geometry"] = {
        "fixed_line": "span (1, 1, 1)",
        "restriction_matrix_in_the_basis_u1_u2":
            [[str(v) for v in row] for row in restriction] if restriction else None,
        "restriction_trace": str(restriction_trace),
        "restriction_determinant": str(restriction_det),
        "cos_theta": str(cos_theta),
        "theta": "2*pi/3",
        "characteristic_polynomial_of_the_restriction": "t^2 + t + 1",
    }
    return out


# ---------------------------------------------------------------------------
# SECTION 6 -- the equal-coefficient functional
# ---------------------------------------------------------------------------
def section_linear_functional() -> dict:
    out: dict = {}
    alphas = [Fraction(0), Fraction(1, 9), Fraction(1, 3), Fraction(1),
              Fraction(2, 27), Fraction(-5, 4)]
    values = {str(al): str(al * 3) for al in alphas}
    computed_ok = all(
        Fraction(values[str(al)]) == al * (Fraction(1) + Fraction(1) + Fraction(1))
        for al in alphas)
    check("EQUAL_COEFFICIENT_FUNCTIONAL_AT_THE_ALL_ONES_VECTOR_IS_THREE_ALPHA",
          computed_ok)
    check("THE_FUNCTIONAL_VALUE_IS_INJECTIVE_IN_ALPHA",
          len(set(values.values())) == len(alphas))
    reaching = [str(al) for al in alphas if al * 3 == Fraction(2, 9)]
    check("EXACTLY_ONE_MEMBER_REACHES_THE_STIPULATED_COMPARATOR_TWO_NINTHS",
          reaching == ["2/27"] and Fraction(2, 27) * 3 == Fraction(2, 9))
    out["linear_functional"] = {"alphas": [str(a) for a in alphas],
                                "values_at_all_ones": values,
                                "member_reaching_2/9": reaching}
    return out


# ---------------------------------------------------------------------------
# SECTION 7 -- a bounded exact separation against multiples of 2 pi
# ---------------------------------------------------------------------------
def arctan_enclosure(inv_n: int, terms: int) -> tuple[Fraction, Fraction]:
    """Enclose arctan(1/n) by an alternating series with its tail bound."""
    total = Fraction(0)
    for k in range(terms):
        term = Fraction(1, (2 * k + 1) * inv_n ** (2 * k + 1))
        total += term if k % 2 == 0 else -term
    tail = Fraction(1, (2 * terms + 1) * inv_n ** (2 * terms + 1))
    return total - tail, total + tail


def pi_enclosure() -> tuple[Fraction, Fraction]:
    """Machin: pi = 16 arctan(1/5) - 4 arctan(1/239)."""
    lo5, hi5 = arctan_enclosure(5, 30)
    lo239, hi239 = arctan_enclosure(239, 10)
    return 16 * lo5 - 4 * hi239, 16 * hi5 - 4 * lo239


def section_separation() -> dict:
    out: dict = {}
    lo, hi = pi_enclosure()
    width = hi - lo
    # the enclosure is exact and far narrower than double precision, so the
    # float value of pi is only a coarse sanity comparison, not a bound
    check("THE_IN_FILE_PI_ENCLOSURE_IS_VALID_AND_NARROW",
          lo < hi and width < Fraction(1, 10 ** 30)
          and abs(float(lo) - math.pi) < 1e-12)

    target = Fraction(2, 9)
    denom_cap, numer_cap = 60, 60
    worst = None
    separated = 0
    total = 0
    all_separated = True
    for d in range(1, denom_cap + 1):
        for m in range(-numer_cap, numer_cap + 1):
            q = Fraction(m, d)
            total += 1
            low, high = (2 * lo * q, 2 * hi * q) if q >= 0 else (2 * hi * q, 2 * lo * q)
            if target < low:
                gap = low - target
            elif target > high:
                gap = target - high
            else:
                all_separated = False
                continue
            separated += 1
            if worst is None or gap < worst:
                worst = gap
    check("EVERY_RATIONAL_IN_THE_DECLARED_FAMILY_MEETS_THE_PUBLISHED_SEPARATION_BOUND",
          all_separated and separated == total and worst is not None
          and worst >= PUBLISHED_SEPARATION_LOWER_BOUND)
    out["separation"] = {
        "pi_enclosure_width_upper_bound": "1e-30",
        "declared_family": f"q = m/d with 1 <= d <= {denom_cap} and "
                           f"|m| <= {numer_cap}",
        "pairs_tested": total,
        "least_separation_lower_bound": PUBLISHED_SEPARATION_LOWER_BOUND_TEXT,
        "general_fact": "for every rational q, 2/9 differs from 2*pi*q, because "
                        "pi is irrational (Lambert 1761) and 2/9 is nonzero; the "
                        "runner verifies only the declared finite family",
    }
    return out


# ---------------------------------------------------------------------------
# SECTION 8 -- MEASURED SUPPORT ONLY: the signed-root scan
# ---------------------------------------------------------------------------
CHARGED_LEPTON_MASSES_MEV = {"e": 0.51099895, "mu": 105.6583755, "tau": 1776.86}
OBSERVATIONAL_INPUT_INVENTORY = {
    "charged_lepton_masses_MeV": CHARGED_LEPTON_MASSES_MEV,
    "role": "observational comparator inputs used only in measured section 8",
    "in_repo_provenance":
        "docs/CLOSURE_T2_DF_PHYSICAL_CONSEQUENCES_NOTE_2026-05-10_t2df.md",
}


def phi_from_spectrum(lams) -> float | None:
    """Float inversion of an unordered real triple; None on B = 0."""
    l0, l1, l2 = lams
    e1 = l0 + l1 + l2
    e2 = l0 * l1 + l0 * l2 + l1 * l2
    e3 = l0 * l1 * l2
    a = e1 / 3.0
    disc = e1 * e1 - 3.0 * e2
    if disc <= 0.0:
        return None
    B = math.sqrt(disc) / 3.0
    c3 = (e3 - a ** 3 + 3.0 * a * B * B) / (2.0 * B ** 3)
    return math.acos(max(-1.0, min(1.0, c3))) / 3.0


def section_measured_support() -> dict:
    out: dict = {}

    # Before any measured value is quoted: the float inversion above carries
    # the same signs as the exact recovery of section 2, and every one of
    # them is load-bearing.  Build a spectrum from a STIPULATED (a, B, delta)
    # through the section-1 eigenvalue formula, invert it, and require the
    # folded argument back.  A flipped sign on any term moves the result.
    inversion_probes = []
    inversion_ok = True
    for a_v, b_v, d_v in ((0.37, 1.9, 0.81), (-2.5, 0.75, 0.13),
                          (1.0, 3.25, 0.9), (0.0, 1.0, math.pi / 3 - 0.02)):
        lams = [a_v + 2.0 * b_v * math.cos(d_v - 2.0 * math.pi * k / 3.0)
                for k in range(3)]
        got = phi_from_spectrum(lams)
        want = math.acos(max(-1.0, min(1.0, math.cos(3.0 * d_v)))) / 3.0
        inversion_probes.append({"a": a_v, "B": b_v, "delta": d_v,
                                 "recovered_Phi": got, "stipulated_fold": want})
        if got is None or abs(got - want) > 1e-12:
            inversion_ok = False
    check("THE_FLOAT_INVERSION_REPRODUCES_A_STIPULATED_FOLDED_ARGUMENT",
          inversion_ok and len(inversion_probes) == 4)
    out["inversion_probes"] = inversion_probes

    roots = [math.sqrt(CHARGED_LEPTON_MASSES_MEV[k]) for k in ("e", "mu", "tau")]
    comparator = 2.0 / 9.0
    table = []
    for signs in itertools.product((1, -1), repeat=3):
        phi = phi_from_spectrum([s * r for s, r in zip(signs, roots)])
        table.append({
            "signs": list(signs),
            "Phi": phi,
            "distance_to_comparator": (None if phi is None else abs(phi - comparator)),
        })
    evaluated = [row for row in table if row["Phi"] is not None]
    check("ALL_EIGHT_SIGNED_ROOT_ASSIGNMENTS_WERE_EVALUATED",
          len(table) == 8 and len(evaluated) == 8)

    ordered = sorted(evaluated, key=lambda row: row["distance_to_comparator"])
    smallest = ordered[0]["distance_to_comparator"]
    runner_up = ordered[1]["distance_to_comparator"]
    check("THE_PUBLISHED_TABLE_IS_THE_FULL_ORDERED_DISTANCE_LIST",
          len(ordered) == 8 and smallest <= runner_up
          and all(ordered[i]["distance_to_comparator"]
                  <= ordered[i + 1]["distance_to_comparator"] for i in range(7)))
    check("THE_SMALLEST_DISTANCE_BELONGS_TO_THE_ALL_POSITIVE_ASSIGNMENT",
          ordered[0]["signs"] == [1, 1, 1])
    distinct = {round(row["Phi"], 12) for row in evaluated}
    check("THE_SIGN_ASSIGNMENT_CHANGES_THE_MEASURED_VALUE",
          len(distinct) > 1)

    out["measured_support"] = {
        "role": "MEASURED SUPPORT ONLY -- no derivation consumes this section",
        "imported_masses_MeV": CHARGED_LEPTON_MASSES_MEV,
        "import_provenance": "the repository's charged-lepton comparator "
                             "baseline; the values are measured inputs, not "
                             "derived here",
        "stipulated_convention": "lambda_k = s_k sqrt(m_k) with s_k in {+1, -1}; "
                                 "the masses alone do not fix the signs, and the "
                                 "positive-root choice is a stipulated condition",
        "comparator": "the rational number 2/9, stipulated here as a comparator "
                      "with no identification claimed",
        "arithmetic": "double precision; the quoted digits are float "
                      "measurements, not exact values",
        "table": table,
        "ordered_distances": [f"{row['distance_to_comparator']:.6e}"
                              for row in ordered],
        "smallest_distance": f"{smallest:.6e}",
        "next_smallest_distance": f"{runner_up:.6e}",
        "ratio_next_over_smallest": f"{runner_up / smallest:.6e}",
        "no_threshold_applied": "the full ordered list is published instead of a "
                                "cutoff; no uniqueness label is attached",
    }
    return out


# ---------------------------------------------------------------------------
# SECTION 9 -- scope discipline on this runner's own emitted claims
# ---------------------------------------------------------------------------
NOT_ESTABLISHED = {
    "family": "no physical carrier, state, or readout is constructed; "
              "self-adjointness and the coefficient identities are statements "
              "about the stipulated matrix family only",
    "inversion": "the inversion recovers stipulated parameters from stipulated "
                 "coefficients; it identifies nothing with a measured or "
                 "physical quantity",
    "fold": "the orbit and preimage counts are statements about the stipulated "
            "argument circle; nothing is claimed about any physical "
            "multiplicity or about any registration of one",
    "invariance": "similarity invariance is spectrum invariance; no "
                  "conservation law and no dynamics are claimed or used, and "
                  "no preservation property is attached to it",
    "permutation_geometry": "the fixed line, the plane, and the angle are "
                            "properties of a 3-by-3 permutation matrix; no "
                            "identification with any physical space, direction, "
                            "or angle is made",
    "linear_functional": "reaching a value exhibits an expression; the "
                         "functional is not identified with any readout and no "
                         "member is selected by anything here",
    "separation": "the separation is arithmetic between a rational number and "
                  "rational multiples of 2 pi; nothing is claimed about what "
                  "any convention, readout, or registration does",
    "measured_support": "the scan is a measurement against imported masses "
                        "under a stipulated sign condition; it derives nothing "
                        "and selects nothing",
}

# The demotion-target vocabulary of the review-loop conformance spec,
# section 3: words that claim more than a computation on stipulated objects
# can deliver.  The table is the one span this runner exempts from its own
# source scan, and the exemption is itself checked below.
# scope-scan-exempt-begin
OVERCLAIM_TOKENS = (
    "certified", "certifies", "certification", "globally", "maximal",
    "universally", "the law of", "proves the framework",
)
# scope-scan-exempt-end


def _split_scan_exemption(source: str) -> tuple[str, str]:
    """Return (exempt span, text actually scanned).

    The markers are assembled at run time so each appears exactly once in
    the source: on its own comment line around the token table.
    """
    begin = "# scope-scan-" + "exempt-begin"
    end = "# scope-scan-" + "exempt-end"
    i, j = source.find(begin), source.find(end)
    if i < 0 or j < 0 or j < i:
        return "", source
    j += len(end)
    return source[i:j], source[:i] + source[j:]


def section_scope_discipline(payload: dict, source_text: str) -> dict:
    exempt, scanned_source = _split_scan_exemption(source_text)
    body = "\n".join(line for line in exempt.splitlines()
                     if not line.strip().startswith("#"))
    try:
        tree = ast.parse(body)
    except SyntaxError:
        tree = None
    exemption_is_only_the_table = (
        tree is not None and len(tree.body) == 1
        and isinstance(tree.body[0], ast.Assign)
        and len(tree.body[0].targets) == 1
        and getattr(tree.body[0].targets[0], "id", None) == "OVERCLAIM_TOKENS"
        and ast.literal_eval(tree.body[0].value) == OVERCLAIM_TOKENS
        and source_text.count("# scope-scan-" + "exempt-begin") == 1
        and source_text.count("# scope-scan-" + "exempt-end") == 1)
    check("THE_SOURCE_SCAN_EXEMPTION_IS_EXACTLY_THE_TOKEN_TABLE",
          exemption_is_only_the_table and 0 < len(exempt.splitlines()) <= 12)

    surfaces = {
        "runner_source": scanned_source.casefold(),
        "emitted_payload": json.dumps(payload, sort_keys=True).casefold(),
    }
    hits = sorted({f"{name}:{token}" for name, blob in surfaces.items()
                   for token in OVERCLAIM_TOKENS if token in blob})
    check("NO_OVERCLAIM_VOCABULARY_ON_THE_SCANNED_PACKAGE_SURFACES", not hits)
    thin = sorted(key for key, text in NOT_ESTABLISHED.items() if len(text) < 40)
    check("EVERY_SECTION_DECLARES_WHAT_IT_DOES_NOT_ESTABLISH",
          not thin and len(NOT_ESTABLISHED) == 8)
    return {
        "overclaim_token_hits": hits,
        "scanned_surfaces": sorted(surfaces),
        "scan_coverage": "this runner's own source text (minus the token "
                         "table, which is exempt and validated to contain "
                         "nothing else) and its emitted payload; the "
                         "independent check scans the remaining executable "
                         "surfaces and a freshly emitted primary payload",
        "sections_declaring_limits": sorted(NOT_ESTABLISHED),
    }


# ---------------------------------------------------------------------------
def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--receipt-out", default=None,
        help="optional path for a deterministic JSON receipt; omitted by "
             "default so a normal verification run leaves no generated file")
    args = parser.parse_args()

    print("=" * 78)
    print("EXACT ALGEBRA OF THE THREE-DIMENSIONAL HERMITIAN CIRCULANT "
          "SPECTRAL FOLD")
    print("support-only; every object is stipulated in this file; section 8 is "
          "measured support")
    print("=" * 78)

    payload: dict = {"date": DATE}
    print("\n-- 1. the self-adjoint circulant family --")
    payload["family"] = section_family()
    print("\n-- 2. exact inversion on B > 0 --")
    payload["inversion"] = section_inversion()
    print("\n-- 3. the dihedral fold and the preimage count --")
    payload["fold"] = section_fold()
    print("\n-- 4. similarity invariance --")
    payload["invariance"] = section_invariance()
    print("\n-- 5. the 3-cycle permutation matrix --")
    payload["permutation_geometry"] = section_permutation_geometry()
    print("\n-- 6. the equal-coefficient functional --")
    payload["linear_functional"] = section_linear_functional()
    print("\n-- 7. bounded exact separation from multiples of 2 pi --")
    payload["separation"] = section_separation()
    print("\n-- 8. MEASURED SUPPORT ONLY: the signed-root scan --")
    payload["measured_support"] = section_measured_support()
    with open(os.path.abspath(__file__), "rb") as handle:
        self_bytes = handle.read()
    self_sha = hashlib.sha256(self_bytes).hexdigest()

    print("\n-- 9. scope discipline --")
    payload["not_established"] = NOT_ESTABLISHED
    payload["scope_discipline"] = section_scope_discipline(
        payload, self_bytes.decode("utf-8"))

    check("CHECK_COUNT_MATCHES_THE_DECLARED_TOTAL",
          len(CHECKS) + 1 == EXPECTED_CHECK_COUNT)
    passed = sum(1 for _, ok in CHECKS if ok)
    failed = len(CHECKS) - passed

    payload["checks"] = [{"name": name, "pass": ok} for name, ok in CHECKS]
    payload["totals"] = {"pass": passed, "fail": failed,
                         "declared_total": EXPECTED_CHECK_COUNT}
    payload["runner"] = "scripts/salvaged_circulant_spectral_fold_2026_08_09.py"
    payload["runner_sha256"] = self_sha
    payload["inputs"] = []
    payload["read_inventory"] = {
        "embedded_observational_comparator_inputs": OBSERVATIONAL_INPUT_INVENTORY,
        "external_runtime_scientific_file_reads": [],
        "package_local_integrity_reads": [
            "scripts/salvaged_circulant_spectral_fold_2026_08_09.py "
            "(this runner's own source, for the self-hash above and for the "
            "section-9 source scan)"],
    }
    blob = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["payload_sha256"] = hashlib.sha256(blob).hexdigest()

    if args.receipt_out:
        os.makedirs(os.path.dirname(os.path.abspath(args.receipt_out)), exist_ok=True)
        with open(args.receipt_out, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")

    print(f"\nTOTAL: PASS={passed} FAIL={failed}")
    print(f"VERDICT: {'PASS' if failed == 0 else 'FAIL'}")
    if args.receipt_out:
        print(f"receipt: {os.path.relpath(args.receipt_out, REPO)}")
    else:
        print(f"payload_sha256: {payload['payload_sha256']}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
