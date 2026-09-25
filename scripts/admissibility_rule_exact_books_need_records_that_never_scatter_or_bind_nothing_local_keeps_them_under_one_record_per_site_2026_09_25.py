#!/usr/bin/env python3
"""Exact checks for the conditional source note.
Exact two-walker shell kinematics, band-diagonal placement identity, fixed-channel line shells, removed coin dimensions and rational-interval nondegeneracy certificates at the stated total momenta. Conditional scattering implications require the explicitly stated absolutely-continuous wave-operator, local-current, shell-kernel and complex threshold hypotheses. The determinant conclusion excludes off-continuum eigenvalues only in the specified momentum neighbourhood; embedded states and a global no-binding theorem are not established. The unrestricted local-interaction no-go remains deferred pending the analytic bridge.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = ['docs/ADMISSIBILITY_RULE_EXACT_BOOKS_NEED_RECORDS_THAT_NEVER_SCATTER_OR_BIND_NOTHING_LOCAL_KEEPS_THEM_UNDER_ONE_RECORD_PER_SITE_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_KEEPS_THE_BOOKS_ONLY_AT_LEADING_ORDER_TWO_EXCLUDED_RECORDS_LOSE_THEIR_ENERGY_CURRENT_IN_TWO_AND_THREE_DIMENSIONS_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_NO_POSSIBILITY_SHIFT_AMONG_NEIGHBOURS_RESTORES_THE_BOOKS_NO_NEIGHBOUR_COIN_TERM_KEEPS_TWO_EXCLUDED_RECORDS_ENERGY_CURRENT_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/ADMISSIBILITY_RULE_THE_WALK_CARRIES_AN_EXACT_BOOST_CHARGE_ITS_BRACKETS_GIVE_THE_FALL_WEIGHT_AND_AN_EXACTLY_KEPT_ANGULAR_MOMENTUM_WITH_THE_FACE_SPIN_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/ADMISSIBILITY_RULE_TWO_STEP_CONTENT_KEEPS_SYMMETRIC_BOOKS_WHERE_THE_MEMBER_KEEPS_ITS_FIELDS_AND_A_BOND_SHIFT_KEEPS_EVERY_CONSTRAINT_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md']
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_exact_books_need_records_that_never_scatter_or_bind_nothing_local_keeps_them_under_one_record_per_site_bounded_theorem_note_2026-09-25"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "shell_point_forged": "B",
    "placement_band_diagonal_forged": "C",
    "line_shell_forged": "D",
    "removed_count_forged": "E",
    "determinant_zero_forged": "E",
    "morse_factor_dropped": "E",
    "cone_tilt_forged": "E",
    "claim_transition_injected": "F",
    "claim_classical_name_in_theorem": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failed_families: set[str] = set()

    def check(self, tag: str, ok: bool, msg: str) -> None:
        if ok:
            self.passed += 1
            print(f"PASS: {tag} {msg}")
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


Fr = Fraction


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[:2]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, one record per site, the interaction and the placements are supplied; the memo does not define a time metric)")
# ============================================================================================ two records at total wave vector K: kinematics of the collision shells
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
PAULI = (SX, SY, SZ)
# Pythagorean angles: (sin, cos) rational
PYTH = ((Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(12, 13)), (Fr(20, 29), Fr(21, 29)), (Fr(8, 17), Fr(15, 17)), (Fr(7, 25), Fr(24, 25)), (Fr(9, 41), Fr(40, 41)))


def s_add(a, b):
    return a[0] * b[1] + a[1] * b[0]


def s_sub(a, b):
    return a[0] * b[1] - a[1] * b[0]


def minor_is_nonzero(dim, rec1, rec2):
    """dg_1 ^ dE on the (q_1, q_2) plane at k1 = K/2 + q = rec1, k2 = K/2 - q = rec2 (angles given by rational (sin, cos)):
    g_1 = sin K_1 cos 2q_1 gives dg_1/dq_1 = -2 sin(K_1) sin(2 q_1) = -2 sin(a_1 + b_1) sin(a_1 - b_1); dE/dq_2 =
    s1 sin(2 a_2)/(2 eps(k1)) - s2 sin(2 b_2)/(2 eps(k2)), nonzero for every band pair when the squares of its two terms differ."""
    a, b = rec1[:dim], rec2[:dim]
    dg = -2 * s_add(a[0], b[0]) * s_sub(a[0], b[0])
    e1 = sum(x[0] ** 2 for x in a)
    e2 = sum(x[0] ** 2 for x in b)
    s2a = 2 * a[1][0] * a[1][1]
    s2b = 2 * b[1][0] * b[1][1]
    squares_differ = s2a ** 2 * e2 != s2b ** 2 * e1
    return dg != 0 and e1 != 0 and e2 != 0 and squares_differ, dg, (s2a ** 2 * e2, s2b ** 2 * e1)


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the total two-step momentum varies along the collision shells in the plane and in space."""
    ok_form = True
    for dim in (2, 3):
        K = sp.symbols("K1:%d" % (dim + 1), real=True)
        q = sp.symbols("q1:%d" % (dim + 1), real=True)
        for a in range(dim):
            ga = (sp.sin(2 * (K[a] / 2 + q[a])) + sp.sin(2 * (K[a] / 2 - q[a]))) / 2
            ok_form = ok_form and sp.simplify(sp.expand_trig(ga - sp.sin(K[a]) * sp.cos(2 * q[a]))) == 0
    rec1 = (PYTH[0], PYTH[1], PYTH[2])
    rec2 = (PYTH[3], PYTH[4], PYTH[5])
    if mut("shell_point_forged"):
        rec2 = rec1
    res = [minor_is_nonzero(dim, rec1, rec2) for dim in (2, 3)]
    ok_pts = all(r[0] for r in res)
    checks.check("B1", ok_form and ok_pts,
                 "T1: the total two-step momentum of two records at total wave vector K and relative q is g_a = sin K_a cos 2q_a in every band (symbolic, Z^2 and Z^3); at the point k1 = K/2 + q, k2 = K/2 - q with Pythagorean angles the shell derivative dg_1 ^ dE on (q_1, q_2) is nonzero for all four band pairs in both dimensions (dg_1/dq_1 = %s, squares %s vs %s and %s vs %s differ), so g is not constant on the shell there; being analytic, it is non-constant on every shell component for almost every K and E" % (res[0][1], res[0][2][0], res[0][2][1], res[1][2][0], res[1][2][1]))


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: a one-body placement adds nothing to the current within a band; the free current is coin-scalar."""
    k = sp.symbols("k1:4", real=True)
    f0, f1, f2, f3 = sp.symbols("f0:4", real=True)
    h = sum((sp.sin(k[a]) * PAULI[a] for a in range(3)), sp.zeros(2, 2))
    eps = sp.sqrt(sum(sp.sin(x) ** 2 for x in k))
    f = f0 * sp.eye(2) + f1 * SX + f2 * SY + f3 * SZ
    comm = sp.I * (h * f - f * h)
    if mut("placement_band_diagonal_forged"):
        comm = comm + f1 * sp.eye(2)
    ok = True
    for s in (1, -1):
        proj = (sp.eye(2) + s * h / eps) / 2
        ok = ok and sp.simplify((proj * comm).trace()) == 0
    # the free record's current is its two-step momentum, sin(k)cos(k) per axis, a multiple of the identity on the coins
    P = [sp.sin(k[a]) * sp.cos(k[a]) * sp.eye(2) for a in range(3)]
    ok = ok and all((h * Pa - Pa * h).applyfunc(sp.simplify) == sp.zeros(2, 2) for Pa in P)
    checks.check("C1", ok,
                 "T2: for any translation-invariant one-body placement f(k) = f0 + f.sigma, the change i[h(k), f(k)] of one record's current has zero trace against each band projector (1 +- h/eps)/2 (symbolic on Z^3): within a band a placement adds nothing to the current; the free record's current is its two-step momentum sin k cos k, a multiple of the identity on the coins that commutes with h(k)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T4 (the line): every collision shell on the line is a pair of points on which g is constant."""
    K, q, q0 = sp.symbols("K q q0", real=True)
    g = sp.sin(K) * sp.cos(2 * q)
    ok = True
    # equal coins: E = sin(K/2 + q) + sin(K/2 - q) = 2 sin(K/2) cos q; shell {q0, -q0}
    E_eq = sp.sin(K / 2 + q) + sp.sin(K / 2 - q)
    ok = ok and sp.simplify(sp.expand_trig(E_eq - 2 * sp.sin(K / 2) * sp.cos(q))) == 0
    ok = ok and sp.simplify(E_eq.subs(q, q0) - E_eq.subs(q, -q0)) == 0 and sp.simplify(g.subs(q, q0) - g.subs(q, -q0)) == 0
    # opposite coins: E = sin(K/2 + q) - sin(K/2 - q) = 2 cos(K/2) sin q; shell {q0, pi - q0}
    E_op = sp.sin(K / 2 + q) - sp.sin(K / 2 - q)
    ok = ok and sp.simplify(sp.expand_trig(E_op - 2 * sp.cos(K / 2) * sp.sin(q))) == 0
    other = sp.pi - q0
    if mut("line_shell_forged"):
        other = sp.pi / 2 - q0
    ok = ok and sp.simplify(E_op.subs(q, q0) - E_op.subs(q, other)) == 0 and sp.simplify(g.subs(q, q0) - g.subs(q, other)) == 0
    checks.check("D1", ok,
                 "T4: on the line (walkers sigma_z D) the collision shells are pairs of points: equal coins have E = 2 sin(K/2) cos q, shell {q0, -q0}; opposite coins have E = 2 cos(K/2) sin q, shell {q0, pi - q0}; on both g = sin K cos 2q takes one value, this identity is within a fixed coin channel, not a statement about arbitrary coin-changing collisions")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Controls: the coincident states one record per site removes, per total wave vector and exchange sign."""
    up = sp.Matrix([1, 0])
    dn = sp.Matrix([0, 1])
    basis = [sp.kronecker_product(x, y) for x in (up, dn) for y in (up, dn)]
    swap = sp.Matrix(4, 4, lambda i, j: 1 if (i // 2 == j % 2 and i % 2 == j // 2) else 0)
    # at coincidence exchange acts on the coins alone: antisymmetric pairs keep the coin-antisymmetric states there
    anti = (sp.eye(4) - swap) / 2
    sym = (sp.eye(4) + swap) / 2
    r_f, r_b = anti.rank(), sym.rank()
    if mut("removed_count_forged"):
        r_f = 2
    # the singlet's overlap with a band pair (s1, s2) at directions n1, n2: (1 - s1 s2 n1.n2)/4
    n1 = sp.Matrix([Fr(3, 5), Fr(4, 5), 0])
    n2 = sp.Matrix([0, Fr(5, 13), Fr(12, 13)])
    S = (basis[1] - basis[2]) / sp.sqrt(2)
    ok_ov = True
    for s1 in (1, -1):
        for s2 in (1, -1):
            p1 = (sp.eye(2) + s1 * sum((n1[a] * PAULI[a] for a in range(3)), sp.zeros(2, 2))) / 2
            p2 = (sp.eye(2) + s2 * sum((n2[a] * PAULI[a] for a in range(3)), sp.zeros(2, 2))) / 2
            ov = sp.simplify((S.T * sp.kronecker_product(p1, p2) * S)[0])
            ok_ov = ok_ov and ov == (1 - s1 * s2 * (n1.T * n2)[0]) / 4 and ov != 0
    checks.check("E1", r_f == 1 and r_b == 3 and ok_ov,
                 "controls: one record per site removes, at every total wave vector, the coincident coin states - one (the singlet) for antisymmetric pairs, three for symmetric pairs; the singlet overlaps every band pair, (1 - s1 s2 n1.n2)/4 != 0 at the test directions, this is an overlap identity only, not by itself a scattering proof")
    family_e2(checks)
    family_e3(checks)


def family_e2(checks: Checks) -> None:
    """T5, step 1 illustrated: the perturbation determinant vanishes at the removed state's energy."""
    z, lam = sp.symbols("z lambda")
    b = sp.Rational(1, 3)
    R = 3
    n = 2 * R + 1
    h0 = sp.zeros(n, n)
    for i in range(n - 1):
        h0[i, i + 1] = b
        h0[i + 1, i] = b
    c = R                      # the coincident relative position r = 0
    P = sp.eye(n)
    P[c, c] = 0
    Q = sp.eye(n) - P
    h2 = P * h0 * P + lam * Q
    A = h2 - h0
    delta = sp.simplify((sp.eye(n) + A * (h0 - z * sp.eye(n)).inv()).det())
    ratio = sp.simplify((h2 - z * sp.eye(n)).det() / (h0 - z * sp.eye(n)).det())
    at = lam if not mut("determinant_zero_forged") else lam + 1
    ok = sp.simplify(delta - ratio) == 0 and sp.simplify(ratio.subs(z, at)) == 0
    checks.check("E2", ok,
                 "T5 (step 1 illustrated): on the line's relative problem truncated to %d positions with the coincident state removed and placed at lambda, the perturbation determinant det(1 + (h'' - h0)(h0 - z)^-1) equals det(h'' - z)/det(h0 - z) symbolically in z and vanishes at z = lambda: a removed state is a zero of the determinant, which transparency forces to one only under the additional infinite-volume analytic hypotheses, not tested by this finite example" % n)


# ============================================================================================ T6: exact nondegeneracy at one wave vector
from math import isqrt
# ---------------------------------------------------------------- rational interval arithmetic
class Iv:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        lo = Fr(lo)
        hi = lo if hi is None else Fr(hi)
        assert lo <= hi
        self.lo, self.hi = lo, hi

    def __add__(self, o):
        o = o if isinstance(o, Iv) else Iv(o)
        return Iv(self.lo + o.lo, self.hi + o.hi)
    __radd__ = __add__

    def __neg__(self):
        return Iv(-self.hi, -self.lo)

    def __sub__(self, o):
        o = o if isinstance(o, Iv) else Iv(o)
        return Iv(self.lo - o.hi, self.hi - o.lo)

    def __rsub__(self, o):
        return Iv(o) - self

    def __mul__(self, o):
        o = o if isinstance(o, Iv) else Iv(o)
        c = [self.lo * o.lo, self.lo * o.hi, self.hi * o.lo, self.hi * o.hi]
        return Iv(min(c), max(c))
    __rmul__ = __mul__

    def inv(self):
        assert self.lo > 0 or self.hi < 0, "division by an interval containing zero"
        return Iv(1 / self.hi, 1 / self.lo)

    def __truediv__(self, o):
        o = o if isinstance(o, Iv) else Iv(o)
        return self * o.inv()

    def __rtruediv__(self, o):
        return Iv(o) * self.inv()

    def sq(self):
        if self.lo >= 0:
            return Iv(self.lo ** 2, self.hi ** 2)
        if self.hi <= 0:
            return Iv(self.hi ** 2, self.lo ** 2)
        return Iv(0, max(self.lo ** 2, self.hi ** 2))

    def sqrt(self, bits=200):
        assert self.lo >= 0
        s = 2 ** bits

        def lower(x):
            n = x.numerator * s * s // x.denominator
            return Fr(isqrt(n), s)

        def upper(x):
            n = -((-x.numerator * s * s) // x.denominator)
            r = isqrt(n)
            if r * r < n:
                r += 1
            return Fr(r, s)
        return Iv(lower(self.lo), upper(self.hi))

    def excludes_zero(self):
        return self.lo > 0 or self.hi < 0

    def width(self):
        return self.hi - self.lo


# ---------------------------------------------------------------- the pair's functions in half-angle-free coordinates t_a = tan k1_a
def model(tau):
    """tau = rational tan K0_a; returns sympy expressions for g1, g2, X, Y and the Hessian pieces, in symbols t."""
    d = len(tau)
    t = sp.symbols("t1:%d" % (d + 1), real=True)
    S = [2 * x / (1 + x ** 2) for x in tau]
    C = [(1 - x ** 2) / (1 + x ** 2) for x in tau]
    c2k1 = [(1 - ti ** 2) / (1 + ti ** 2) for ti in t]
    s2k1 = [2 * ti / (1 + ti ** 2) for ti in t]
    g1 = [ti / (1 + ti ** 2) for ti in t]
    X = [ti ** 2 / (1 + ti ** 2) for ti in t]
    g2 = [(S[a] * c2k1[a] - C[a] * s2k1[a]) / 2 for a in range(d)]
    Y = [(1 - (C[a] * c2k1[a] + S[a] * s2k1[a])) / 2 for a in range(d)]
    c2k2 = [C[a] * c2k1[a] + S[a] * s2k1[a] for a in range(d)]
    return t, g1, g2, X, Y, c2k1, c2k2




def horner_iv(coeffs, x):
    """coeffs highest first (Fractions or Iv); x an Iv."""
    acc = Iv(0)
    for c in coeffs:
        acc = acc * x + (c if isinstance(c, Iv) else Iv(c))
    return acc


def poly_iv(poly, var_ivs, gens):
    """evaluate a sympy Poly in gens at interval arguments (monomial sum)."""
    acc = Iv(0)
    for monom, coeff in poly.terms():
        term = Iv(Fr(int(coeff.p), int(coeff.q)))
        for g, e in zip(gens, monom):
            if e:
                x = var_ivs[g]
                p = Iv(1)
                for _ in range(e):
                    p = p * x
                term = term * p
        acc = acc + term
    return acc


def comp_fns(tau_a):
    """per-component rational functions of t = tan k1_a, evaluated on an interval."""
    S = Fr(2) * tau_a / (1 + tau_a ** 2)
    C = (1 - tau_a ** 2) / (1 + tau_a ** 2)

    def f(ti):
        den = (Iv(1) + ti.sq()).inv()
        c2k1 = (Iv(1) - ti.sq()) * den
        s2k1 = Iv(2) * ti * den
        g1 = ti * den
        X = ti.sq() * den
        g2 = (Iv(S) * c2k1 - Iv(C) * s2k1) * Fr(1, 2)
        Y = (Iv(1) - (Iv(C) * c2k1 + Iv(S) * s2k1)) * Fr(1, 2)
        c2k2 = Iv(C) * c2k1 + Iv(S) * s2k1
        return c2k1, g1, X, c2k2, g2, Y
    return f


def det_iv(M):
    n = len(M)
    if n == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    if n == 3:
        return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
                - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    raise ValueError


def hess_dets(tau, box):
    """interval determinants of s1 H(k1) + s2 H(k2) for (s1, s2) = (+,+) and (+,-) at a box of t = tan k1."""
    d = len(tau)
    comps = [comp_fns(Fr(tau[a]))(box[a]) for a in range(d)]
    X = sum((c[2] for c in comps), Iv(0))
    Y = sum((c[5] for c in comps), Iv(0))
    if not (X.lo > 0 and Y.lo > 0):
        return None
    e1 = X.sqrt()
    e2 = Y.sqrt()
    e1i, e2i = e1.inv(), e2.inv()
    e1i3, e2i3 = e1i * e1i * e1i, e2i * e2i * e2i
    H1 = [[(comps[a][0] * e1i if a == b else Iv(0)) - comps[a][1] * comps[b][1] * e1i3 for b in range(d)] for a in range(d)]
    H2 = [[(comps[a][3] * e2i if a == b else Iv(0)) - comps[a][4] * comps[b][4] * e2i3 for b in range(d)] for a in range(d)]
    out = {}
    for s2 in (1, -1):
        M = [[H1[a][b] + H2[a][b] * s2 for b in range(d)] for a in range(d)]
        grad = [comps[a][1] * e1i - comps[a][4] * e2i * s2 for a in range(d)]
        out[(1, s2)] = (det_iv(M), any(g.excludes_zero() for g in grad))
    return out


def cone_tilts(tau):
    """squared gradient of the smooth record's energy at every cone point (k1 = corner or k2 = corner): must be < 1."""
    d = len(tau)
    sinsq = [Fr(x) ** 2 / (1 + Fr(x) ** 2) for x in tau]
    sincos = [Fr(x) / (1 + Fr(x) ** 2) for x in tau]
    tilt2 = sum(v ** 2 for v in sincos) / sum(sinsq)
    return tilt2


def system_2d(tau):
    t, g1, g2, X, Y, c2k1, c2k2 = model(tau)
    t1, t2 = t
    P = sp.Poly(sp.numer(sp.together(g1[0] * g2[1] - g1[1] * g2[0])), t1, t2)
    Q = sp.Poly(sp.numer(sp.together(g1[0] ** 2 * (Y[0] + Y[1]) - g2[0] ** 2 * (X[0] + X[1]))), t1, t2)
    return t, P, Q


def certify_2d(tau, prec_exp=60):
    t, P, Q = system_2d(tau)
    t1, t2 = t
    R = sp.Poly(sp.resultant(P.as_expr(), Q.as_expr(), t2), t1)
    assert not R.is_zero
    eps = sp.Rational(1, 10 ** prec_exp)
    # coefficients of P in t2, as polys in t1
    Pt2 = sp.Poly(P.as_expr(), t2)
    coeffs = [sp.Poly(c, t1) for c in Pt2.all_coeffs()]
    assert not all(c.is_zero for c in coeffs)
    cones = {(Fr(0), Fr(0)), (Fr(tau[0]), Fr(tau[1]))}
    report = []
    for f, mult in sp.factor_list(R.as_expr())[1]:
        fp = sp.Poly(f, t1)
        for (a, b), m in fp.intervals(eps=eps):
            a, b = Fr(int(sp.Rational(a).p), int(sp.Rational(a).q)), Fr(int(sp.Rational(b).p), int(sp.Rational(b).q))
            if a == b:   # exact rational root
                cs = [Fr(int(sp.Rational(c.eval(a)).p), int(sp.Rational(c.eval(a)).q)) if not c.is_zero else Fr(0) for c in coeffs]
                qpoly = sp.Poly(sum(sp.Rational(cs[i].numerator, cs[i].denominator) * t2 ** (len(cs) - 1 - i) for i in range(len(cs))), t2)
                roots2 = []
                for (c0, c1), m2 in qpoly.intervals(eps=eps):
                    roots2.append(Iv(Fr(int(sp.Rational(c0).p), int(sp.Rational(c0).q)), Fr(int(sp.Rational(c1).p), int(sp.Rational(c1).q))))
                I1 = Iv(a)
            else:
                I1 = Iv(a, b)
                A, B, C = [horner_iv([Fr(int(x.p), int(x.q)) for x in c.all_coeffs()], I1) if not c.is_zero else Iv(0) for c in coeffs]
                assert A.excludes_zero(), "leading coefficient not separated"
                disc = B * B - Iv(4) * A * C
                if disc.hi < 0:
                    report.append(("no real t2", a))
                    continue
                assert disc.lo > 0, "discriminant not separated"
                sq = disc.sqrt()
                roots2 = [(-B + sq) / (Iv(2) * A), (-B - sq) / (Iv(2) * A)]
            for I2 in roots2:
                if I1.width() == 0 and I2.width() == 0 and (I1.lo, I2.lo) in cones:
                    report.append(("cone", (I1.lo, I2.lo)))
                    continue
                # a candidate: Q must vanish there for a genuine stationary point; record Q's enclosure
                Qv = poly_iv(Q, {t1: I1, t2: I2}, (t1, t2))
                dets = hess_dets(tau, [I1, I2])
                if dets is None:
                    report.append(("eps interval touches zero", (I1.lo, I2.lo)))
                    continue
                verdict = {}
                for k, (dv, gnz) in dets.items():
                    verdict[k] = "not stationary" if gnz else ("nondegenerate" if dv.excludes_zero() else "UNDECIDED")
                report.append(("candidate", I1.lo, I2.lo, "Q excludes 0" if Qv.excludes_zero() else "Q may vanish", verdict))
    return R, report


def iv_of(r):
    r = sp.Rational(r)
    return Fr(int(r.p), int(r.q))


def quad_roots_iv(coeff_polys, x_iv, var):
    """real roots (intervals) of sum c_i(x) y^i where coefficient polys are in `var`, evaluated at the interval x_iv."""
    cs = [horner_iv([iv_of(z) for z in c.all_coeffs()], x_iv) if not c.is_zero else Iv(0) for c in coeff_polys]
    if len(cs) == 3:
        A, B, C = cs
        assert A.excludes_zero(), "leading coefficient not separated"
        disc = B * B - Iv(4) * A * C
        if disc.hi < 0:
            return []
        assert disc.lo > 0, "discriminant not separated"
        sq = disc.sqrt()
        return [(-B + sq) / (Iv(2) * A), (-B - sq) / (Iv(2) * A)]
    if len(cs) == 2:
        A, B = cs
        assert A.excludes_zero()
        return [-B / A]
    raise ValueError


def certify_3d(tau, prec_exp=80):
    t, g1, g2, X, Y, c2k1, c2k2 = model(tau)
    t1, t2, t3 = t
    P12 = sp.Poly(sp.numer(sp.together(g1[0] * g2[1] - g1[1] * g2[0])), t1, t2)
    P13 = sp.Poly(sp.numer(sp.together(g1[0] * g2[2] - g1[2] * g2[0])), t1, t3)
    Q = sp.Poly(sp.numer(sp.together(g1[0] ** 2 * (Y[0] + Y[1] + Y[2]) - g2[0] ** 2 * (X[0] + X[1] + X[2]))), t1, t2, t3)
    R1 = sp.Poly(sp.resultant(P13.as_expr(), Q.as_expr(), t3), t1, t2)
    assert not R1.is_zero
    R = sp.Poly(sp.resultant(P12.as_expr(), R1.as_expr(), t2), t1)
    assert not R.is_zero
    eps = sp.Rational(1, 10 ** prec_exp)
    c12 = [sp.Poly(c, t1) for c in sp.Poly(P12.as_expr(), t2).all_coeffs()]
    c13 = [sp.Poly(c, t1) for c in sp.Poly(P13.as_expr(), t3).all_coeffs()]
    report = []
    ncand = 0
    for f, mult in sp.factor_list(R.as_expr())[1]:
        fp = sp.Poly(f, t1)
        for (a, b), m in fp.intervals(eps=eps):
            a, b = iv_of(a), iv_of(b)
            I1 = Iv(a, b)
            if a == b and a == 0:
                report.append(("t1 = 0 (a corner coordinate; no stationary point has sin k cos k = 0)",))
                continue
            if a == b and a == Fr(tau[0]):
                report.append(("t1 = tan K0_1 (k2_1 at a corner coordinate; excluded likewise)",))
                continue
            for I2 in quad_roots_iv(c12, I1, t1):
                for I3 in quad_roots_iv(c13, I1, t1):
                    ncand += 1
                    dets = hess_dets(tau, [I1, I2, I3])
                    if dets is None:
                        report.append(("eps touches zero", a))
                        continue
                    verdict = {}
                    for k, (dv, gnz) in dets.items():
                        verdict[k] = "not stationary" if gnz else ("nondegenerate" if dv.excludes_zero() else "UNDECIDED")
                    report.append(("candidate", a, I2.lo, I3.lo, verdict))
    return R, report, ncand



def family_e3(checks: Checks) -> None:
    """T6: an exact proof that at one total wave vector in each dimension every stationary point of the pair's band functions is nondegenerate."""
    drop = mut("morse_factor_dropped")
    out = {}
    for name, tau in (("plane", (Fr(5, 6), Fr(18, 5))), ("space", (Fr(5, 6), Fr(18, 5), Fr(1, 2)))):
        if len(tau) == 2:
            R, rep = certify_2d(tau)
        else:
            R, rep, _ = certify_3d(tau)
        assert all(r[0] != "eps interval touches zero" for r in rep), "unresolved cone enclosure"
        if drop:
            rep = [r for r in rep if not (r[0] == "candidate" and "nondegenerate" in r[-1].values() and r[-1].get((1, 1)) == "nondegenerate")]
        undecided = sum(1 for r in rep if r[0] == "candidate" and "UNDECIDED" in r[-1].values())
        n_pp = sum(1 for r in rep if r[0] == "candidate" and r[-1].get((1, 1)) == "nondegenerate")
        n_pm = sum(1 for r in rep if r[0] == "candidate" and r[-1].get((1, -1)) == "nondegenerate")
        tilt = cone_tilts(tau)
        if mut("cone_tilt_forged"):
            tilt = tilt + 1
        out[name] = (undecided, n_pp, n_pm, tilt)
    ok = (out["plane"][0] == 0 and out["plane"][1:3] == (4, 2) and out["space"][0] == 0 and out["space"][1:3] == (8, 6)
          and all(v[3] < 1 for v in out.values()))
    checks.check("E3", ok,
                 "T6: at tan K0 = (5/6, 18/5) on Z^2 and (5/6, 18/5, 1/2) on Z^3, the stationary points of the pair's band functions lie on the real roots of an exact resultant (degree 16 and 40), isolated exactly; at every candidate, for each band pair, rational interval arithmetic shows either a nonvanishing gradient or a nonvanishing Hessian determinant: %d and %d nondegenerate candidate enclosures per half-period cell (existence in every box not asserted) for the ++ and +- band pairs in the plane, %d and %d in space, none undecided; at the cone points the other record's energy has squared gradient %s and %s, below one" % (out["plane"][1], out["plane"][2], out["space"][1], out["space"][2], out["plane"][3], out["space"][3]))


# ============================================================================================ family F
FENCES = (
    "This note retains exact two-walker algebra and interval enclosures, with scattering conclusions conditional on an unresolved analytic bridge; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "DeWitt", "Hojman", "Kuchar", "Kuchař", "Teitelboim", "Dirac", "Bergmann", "Lorentz", "Kato", "Rosenblum", "Ruelle", "Amrein", "Georgescu", "Enss", "Lebesgue", "Levinson", "Birman", "Krein", "Schwarz", "Liouville", "Morse", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Bloch", "Berry", "Schrodinger", "Lorentz", "Hartree", "Mach", "Eddington", "Soldner", "Dicke", "Riemann", "Regge", "Lame", "Hooke", "Abraham", "Arnowitt", "Deser", "Misner", "Brill", "Lindquist", "Isenberg", "Wilson", "Mathews", "Lichnerowicz", "York", "Hilbert", "Tolman", "Komar", "Friedmann", "Ricci",
                   "Christoffel", "Baierlein", "Wheeler", "Lagrange", "Jacobi", "Brans", "Nordtvedt")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record", "Analytic bridge", "No-Go Discipline Gate")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Einstein)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + nm + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + nm + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - the closed form g_a = sin K_a cos 2q_a of the total two-step momentum, symbolically on Z^2 and Z^3",
    "per_site: executed - the shell derivative dg_1 ^ dE at a Pythagorean point for all four band pairs, by rational comparison",
    "per_mode: executed - the placement lemma for any one-body term f0 + f.sigma, symbolically on Z^3",
    "per_block: executed - the line's two-point shells with one value of g; the coincident states removed and their overlap with every band pair; the perturbation determinant on a truncation vanishing at the removed state; exact nondegeneracy of every stationary point of the pair bands at one wave vector in each dimension",
    "lattice_wide: exact finite algebra and interval certificate only; infinite-volume scattering and threshold application remain conditional",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


def main(argv) -> int:
    global ACTIVE_MUTATION
    if "--list-mutations" in argv:
        for name, fam in MUTATION_GATE.items():
            print(f"{name} {fam}")
        return 0
    if "--mutation" in argv:
        ACTIVE_MUTATION = argv[argv.index("--mutation") + 1]
        if ACTIVE_MUTATION not in MUTATION_GATE:
            print(f"unknown mutation {ACTIVE_MUTATION}")
            return 2
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    texts = [Path(ROOT, p).read_text(encoding="utf-8") if Path(ROOT, p).exists() else "" for p in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print('scope: Exact two-walker shell kinematics, band-diagonal placement identity, fixed-channel line shells, removed coin dimensions and rational-interval nondegeneracy certificates at the stated total momenta. Conditional scattering implications require the explicitly stated absolutely-continuous wave-operator, local-current, shell-kernel and complex threshold hypotheses. The determinant conclusion excludes off-continuum eigenvalues only in the specified momentum neighbourhood; embedded states and a global no-binding theorem are not established. The unrestricted local-interaction no-go remains deferred pending the analytic bridge.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
