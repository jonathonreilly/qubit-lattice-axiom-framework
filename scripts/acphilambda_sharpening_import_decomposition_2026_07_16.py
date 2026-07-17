#!/usr/bin/env python3
"""Exact verification for the occupancy-grain sharpening-import decomposition note.

Claim id:
  acphilambda_occupancy_grain_sharpening_import_decomposition_reflection_asymmetry_orientation_dichotomy_bounded_theorem_note_2026-07-16

Paired note:
  docs/ACPHILAMBDA_OCCUPANCY_GRAIN_SHARPENING_IMPORT_DECOMPOSITION_REFLECTION_
  ASYMMETRY_ORIENTATION_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-16.md

Every check is exact (sympy Rationals / symbolic identities / exact radicals via
sp.sqrt + sp.radsimp). No float ever enters a pass condition. Each gate computes
its claim: solved fixed points are found by solving, then gated, then substituted
back. Blocks:

  TEXT_INTEGRITY   note exists, claim id present, dependency filenames cited
  T1_FIXED_POINT   fixed-point identity; interior fixed set; A-membership <=>
  T2_SIGN_BRIDGE   sign bridge sign(T_f(q)-q)=sign(h(q)); exchange; slope
  T3_HORN          off-center amplification T_f(q)>q for q>1/2
  ORBITS           A+ orbit rises toward 1; A- orbit falls toward 1/2 (exact)
  WITNESS_A        A+ witness: reflection asymmetry, non-monotone per-weight profile
  WITNESS_B        sign-mixed boundary witness B, fixed-point pair 5/22, 17/22
  IDENTITY         N2 identity member f = x: T_f = q, h identically zero
  LADDER           strict ladder M ( A+ ( A ( F
  SOURCE_GATES     verbatim source and boundary quote gates
  NOTE_HYGIENE     no prose decimals, pinned phrases absent, headers present
"""

import re
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / (
    "docs/ACPHILAMBDA_OCCUPANCY_GRAIN_SHARPENING_IMPORT_DECOMPOSITION_REFLECTION_"
    "ASYMMETRY_ORIENTATION_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-16.md"
)
W1B_PATH = ROOT / (
    "docs/ACPHILAMBDA_OCCUPANCY_GRAIN_RULE_CLASS_UNIVERSALITY_BOUNDED_THEOREM_"
    "NOTE_2026-07-11.md"
)
AXIOMS_PATH = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
OBLIG_PATH = ROOT / "docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md"

PASS_COUNT = 0
FAIL_COUNT = 0
BLOCK_COUNTS = {}


def flat(text):
    # Markdown block-quote markers are layout, not part of the quoted prose.
    return " ".join(re.sub(r"(?m)^\s*>\s?", "", text).split())


def check(block, label, condition):
    global PASS_COUNT, FAIL_COUNT
    BLOCK_COUNTS[block] = BLOCK_COUNTS.get(block, 0) + 1
    number = BLOCK_COUNTS[block]
    passed = bool(condition)
    if passed:
        PASS_COUNT += 1
        result = "PASS"
    else:
        FAIL_COUNT += 1
        result = "FAIL"
    print(f"{block}.{number} {result}: {label}")


def positive(expr):
    """Exact strict-positivity decision. No float ever enters the decision."""
    val = sp.simplify(expr)
    if val.is_positive is True:
        return True
    if val.is_positive is False:
        return False
    return bool(val > 0)


note_text = NOTE_PATH.read_text(encoding="utf-8")
w1b_text = W1B_PATH.read_text(encoding="utf-8")
axioms_text = AXIOMS_PATH.read_text(encoding="utf-8")
oblig_text = OBLIG_PATH.read_text(encoding="utf-8")
flat_note = flat(note_text)

q, x = sp.symbols("q x", real=True)
half = sp.Rational(1, 2)


# ---------------------------------------------------------------------------
print("[TEXT_INTEGRITY] Note exists, claim id present, dependency filenames cited")
CLAIM_ID = ("acphilambda_occupancy_grain_sharpening_import_decomposition_reflection_"
            "asymmetry_orientation_dichotomy_bounded_theorem_note_2026-07-16")
check("TEXT_INTEGRITY", "paired note file exists on disk", NOTE_PATH.is_file())
check("TEXT_INTEGRITY", "note states its claim id verbatim", CLAIM_ID in note_text)

DEP_FILENAMES = [
    "ACPHILAMBDA_OCCUPANCY_GRAIN_RULE_CLASS_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "MINIMAL_AXIOMS_2026-06-29.md",
    "AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md",
]
for dep_name in DEP_FILENAMES:
    check("TEXT_INTEGRITY", f"note cites dependency filename {dep_name}",
          dep_name in note_text)

# ---------------------------------------------------------------------------
print("[T1_FIXED_POINT] Fixed-point identity, interior fixed set, A-membership equivalence")
fsym = sp.Function("f")


def g_sym(fcall, t):
    return fcall(t) / t


def h_sym(fcall, t):
    return g_sym(fcall, t) - g_sym(fcall, 1 - t)


def T_sym(fcall, t):
    return fcall(t) / (fcall(t) + fcall(1 - t))


# T1 core identity: the fixed-condition numerator equals q(1-q) h(q).
h_general = fsym(q) / q - fsym(1 - q) / (1 - q)
identity_lhs = fsym(q) * (1 - q) - q * fsym(1 - q)
identity_rhs = q * (1 - q) * h_general
check("T1_FIXED_POINT", "f(q)(1-q) - q f(1-q) = q(1-q)[g(q) - g(1-q)] exactly",
      sp.simplify(identity_lhs - identity_rhs) == 0)

num_T_minus_q = sp.together(T_sym(fsym, q) - q).as_numer_denom()[0]
check("T1_FIXED_POINT", "numerator of T_f(q) - q equals f(q)(1-q) - q f(1-q) exactly",
      sp.simplify(sp.expand(num_T_minus_q) - sp.expand(identity_lhs)) == 0)

# Power members f = q^k: interior fixed set solved, not asserted.
for exponent in (sp.Integer(2), sp.Integer(3)):
    fixed_eq = sp.Eq(q ** exponent * (1 - q), q * (1 - q) ** exponent)
    fixed_sols = sp.solve(fixed_eq, q)
    check("T1_FIXED_POINT",
          f"f = q^{exponent}: exact solve of the fixed condition yields only {{0, 1/2, 1}}",
          set(fixed_sols) == {sp.Integer(0), half, sp.Integer(1)})

# Endpoint extension limits (computed, not stipulated).
T_pow = q ** 2 / (q ** 2 + (1 - q) ** 2)
check("T1_FIXED_POINT", "T_f extends by limit to T_f(0) = 0 (exemplar k=2)",
      sp.limit(T_pow, q, 0, "+") == 0)
check("T1_FIXED_POINT", "T_f extends by limit to T_f(1) = 1 (exemplar k=2)",
      sp.limit(T_pow, q, 1, "-") == 1)

# Reflection-oddness: h(1-q) = -h(q) for generic f, so interior zeros off the
# center pair up across q <-> 1-q; both directions of the A-membership
# equivalence are gated on concrete members and witnesses below.
check("T1_FIXED_POINT", "h is reflection-odd for generic f: h(1-q) = -h(q) exactly",
      sp.simplify(h_general.subs(q, 1 - q) + h_general) == 0)

# ---------------------------------------------------------------------------
print("[T2_SIGN_BRIDGE] Sign bridge, orientation dichotomy support, exchange, central slope")
bridge = T_sym(fsym, q) - q - q * (1 - q) * h_general / (fsym(q) + fsym(1 - q))
check("T2_SIGN_BRIDGE",
      "T_f(q) - q = q(1-q) h(q) / (f(q)+f(1-q)) exactly (full quotient)",
      sp.simplify(bridge) == 0)
check("T2_SIGN_BRIDGE",
      "sign-bridge numerator q(1-q) h(q) equals f(q)(1-q) - q f(1-q)",
      sp.simplify(q * (1 - q) * h_general - identity_lhs) == 0)

# Denominator positivity: f(q)+f(1-q) > 0 on (0,1) for concrete members.
DENOM_MEMBERS = [("q^2", lambda t: t ** 2), ("sqrt(q)", lambda t: sp.sqrt(t))]
for name, fcall in DENOM_MEMBERS:
    val = (fcall(q) + fcall(1 - q)).subs(q, sp.Rational(3, 5))
    check("T2_SIGN_BRIDGE", f"denominator f(q)+f(1-q) > 0 at q=3/5 for f={name}",
          positive(val))

# Exchange symmetry T_f(1-q) = 1 - T_f(q).
check("T2_SIGN_BRIDGE", "exchange symmetry: T_f(1-q) = 1 - T_f(q) exactly",
      sp.simplify(T_sym(fsym, q).subs(q, 1 - q) - (1 - T_sym(fsym, q))) == 0)

# If f is differentiable at 1/2, then
# T_f'(1/2) = f'(1/2)/(2 f(1/2)).
T_slope = sp.diff(T_sym(fsym, q), q).subs(q, half)
target_slope = sp.diff(fsym(q), q).subs(q, half) / (2 * fsym(half))
check("T2_SIGN_BRIDGE", "under differentiability at 1/2: central slope T_f'(1/2) = f'(1/2)/(2 f(1/2)) exactly",
      sp.simplify(T_slope - target_slope) == 0)

for exponent in (sp.Rational(1, 2), sp.Integer(2)):
    Tk = q ** exponent / (q ** exponent + (1 - q) ** exponent)
    check("T2_SIGN_BRIDGE", f"power member f = q^{exponent}: central slope is exactly {exponent}",
          sp.simplify(sp.diff(Tk, q).subs(q, half) - exponent) == 0)

kk = sp.Symbol("k", positive=True)
Tk_sym = q ** kk / (q ** kk + (1 - q) ** kk)
check("T2_SIGN_BRIDGE", "power member f = q^k, symbolic k > 0: central slope is exactly k",
      sp.simplify(sp.diff(Tk_sym, q).subs(q, half) - kk) == 0)

# ---------------------------------------------------------------------------
print("[T3_HORN] Off-center amplification: T_f(q) > q for q > 1/2 across members")
HORN_MEMBERS = [
    ("q^2", lambda t: t ** 2),
    ("q^3", lambda t: t ** 3),
    ("q^4", lambda t: t ** 4),
    ("(q + q^2)/2", lambda t: (t + t ** 2) / 2),
]
horn_poly = (q + q ** 2) / 2
horn_poly_prime = sp.diff(horn_poly, q)
check("T3_HORN",
      "normalized polynomial member is in F: f(0)=0, f(1)=1, and f' >= f'(0)=1/2 > 0",
      horn_poly.subs(q, 0) == 0
      and horn_poly.subs(q, 1) == 1
      and horn_poly_prime == q + half
      and positive(horn_poly_prime.subs(q, 0))
      and positive(sp.diff(horn_poly_prime, q)))
for name, fcall in HORN_MEMBERS:
    val = T_sym(fcall, sp.Rational(3, 5)) - sp.Rational(3, 5)
    check("T3_HORN", f"f = {name}: T_f(3/5) > 3/5 (off-center amplification, q > 1/2)",
          positive(val))
check("T3_HORN", "mirror: f = q^2 attenuates the minority side, T_f(2/5) < 2/5",
      positive(sp.Rational(2, 5) - T_sym(lambda t: t ** 2, sp.Rational(2, 5))))

# ---------------------------------------------------------------------------
print("[ORBITS] Exemplar orbits: A+ rises toward 1; A- falls toward 1/2 (exact)")


def orbit(fcall, q0, steps):
    pts = [sp.Rational(q0) if not isinstance(q0, sp.Expr) else q0]
    for _ in range(steps):
        cur = pts[-1]
        nxt = sp.radsimp(fcall(cur) / (fcall(cur) + fcall(1 - cur)))
        pts.append(nxt)
    return pts

# A+ exemplar f = q^2 (majority-amplifying), start 3/5, six exact-rational steps.
orb_up = orbit(lambda t: t ** 2, sp.Rational(3, 5), 6)
check("ORBITS", "A+ orbit f=q^2 from 3/5: strictly increasing over six steps",
      all(positive(orb_up[i + 1] - orb_up[i]) for i in range(6)))
check("ORBITS", "A+ orbit f=q^2 from 3/5: every iterate stays in (1/2, 1)",
      all(positive(p - half) and positive(1 - p) for p in orb_up))
check("ORBITS", "A+ orbit f=q^2 from 3/5: closing gap to 1 is below 1/1000 after six steps",
      positive(sp.Rational(1, 1000) - (1 - orb_up[-1])))

# A- exemplar f = sqrt(q) (majority-attenuating), start 3/4, six exact-radical steps.
orb_dn = orbit(lambda t: sp.sqrt(t), sp.Rational(3, 4), 6)
check("ORBITS", "A- orbit f=sqrt(q) from 3/4: strictly decreasing over six steps",
      all(positive(orb_dn[i] - orb_dn[i + 1]) for i in range(6)))
check("ORBITS", "A- orbit f=sqrt(q) from 3/4: every iterate stays above 1/2",
      all(positive(p - half) for p in orb_dn))
check("ORBITS", "A- orbit f=sqrt(q) from 3/4: closing gap to 1/2 is below 1/100 after six steps",
      positive(sp.Rational(1, 100) - (orb_dn[-1] - half)))

# A- exemplar interior fixed set solved exactly (T1: the limit point 1/2 is the
# unique interior fixed point of f = sqrt(q)).
sqrt_fixed = sp.solveset(sp.Eq(sp.sqrt(q) * (1 - q), q * sp.sqrt(1 - q)), q,
                         sp.Interval.open(0, 1))
check("ORBITS", "A- exemplar f = sqrt(q): interior fixed set solved exactly = {1/2}",
      sqrt_fixed == sp.FiniteSet(half))

# ---------------------------------------------------------------------------
print("[WITNESS_A] A+ witness: reflection asymmetry, non-monotone per-weight influence profile")
# g piecewise linear (a + b x) on [0,1/4],[1/4,1/2],[1/2,3/4],[3/4,1].
PIECES_A = [
    (sp.Integer(0), sp.Rational(1, 4), half, sp.Rational(2, 5)),
    (sp.Rational(1, 4), half, sp.Rational(13, 20), -sp.Rational(1, 5)),
    (half, sp.Rational(3, 4), sp.Rational(1, 20), sp.Integer(1)),
    (sp.Rational(3, 4), sp.Integer(1), half, sp.Rational(2, 5)),
]


def g_pw(pieces, t):
    for lo, hi, aa, bb in pieces:
        if bool(lo <= t) and bool(t <= hi):
            return aa + bb * t
    raise ValueError(f"g evaluated outside [0,1]: {t}")


def f_pw(pieces, t):
    return t * g_pw(pieces, t)


def h_pw(pieces, t):
    return g_pw(pieces, t) - g_pw(pieces, 1 - t)


def T_pw(pieces, t):
    fa, fb = f_pw(pieces, t), f_pw(pieces, 1 - t)
    return fa / (fa + fb)


NODES_A = {
    sp.Integer(0): half,
    sp.Rational(1, 4): sp.Rational(3, 5),
    half: sp.Rational(11, 20),
    sp.Rational(3, 4): sp.Rational(4, 5),
    sp.Integer(1): sp.Rational(9, 10),
}
NODES_A_TEXT = "g(0) = 1/2,  g(1/4) = 3/5,  g(1/2) = 11/20,  g(3/4) = 4/5,  g(1) = 9/10,"
check("WITNESS_A", "witness A node table gated in note text and matched by g exactly",
      flat(NODES_A_TEXT) in flat_note
      and all(g_pw(PIECES_A, node) == value for node, value in NODES_A.items()))
check("WITNESS_A", "witness A g continuous at internal breakpoints 1/4, 1/2, 3/4",
      all(sp.simplify((PIECES_A[i][2] + PIECES_A[i][3] * PIECES_A[i][1])
                      - (PIECES_A[i + 1][2] + PIECES_A[i + 1][3] * PIECES_A[i + 1][0])) == 0
          for i in range(3)))
check("WITNESS_A", "witness A f(0) = 0 and f(1) = 9/10 <= 1",
      f_pw(PIECES_A, sp.Integer(0)) == 0
      and f_pw(PIECES_A, sp.Integer(1)) == sp.Rational(9, 10)
      and f_pw(PIECES_A, sp.Integer(1)) <= 1)
fprime_A = []
for lo, hi, aa, bb in PIECES_A:
    fprime_A.extend([aa + 2 * bb * lo, aa + 2 * bb * hi])
check("WITNESS_A", "witness A f' > 0 at every piece endpoint (strictly increasing on [0,1])",
      all(positive(v) for v in fprime_A))

# h derived from g at the reflection nodes.
check("WITNESS_A", "witness A h(1/2) = 0 (reflection fixed at center)",
      h_pw(PIECES_A, half) == 0)
check("WITNESS_A", "witness A h(3/4) = 1/5 derived from g",
      h_pw(PIECES_A, sp.Rational(3, 4)) == sp.Rational(1, 5))
check("WITNESS_A", "witness A h(7/8) = 3/10 derived from g (interior sample)",
      h_pw(PIECES_A, sp.Rational(7, 8)) == sp.Rational(3, 10))

# Symbolic reflection asymmetry on each side of (1/2,1): h(q) = 4q/5 - 2/5.
h_upper_lo = sp.expand((PIECES_A[2][2] + PIECES_A[2][3] * q)
                       - (PIECES_A[1][2] + PIECES_A[1][3] * (1 - q)))
h_upper_hi = sp.expand((PIECES_A[3][2] + PIECES_A[3][3] * q)
                       - (PIECES_A[0][2] + PIECES_A[0][3] * (1 - q)))
h_formula = sp.Rational(4, 5) * q - sp.Rational(2, 5)
check("WITNESS_A", "witness A h(q) = 4q/5 - 2/5 on (1/2, 3/4)",
      sp.expand(h_upper_lo - h_formula) == 0)
check("WITNESS_A", "witness A h(q) = 4q/5 - 2/5 on (3/4, 1)",
      sp.expand(h_upper_hi - h_formula) == 0)
check("WITNESS_A",
      "witness A affine certificate: side formulas agree, h(1/2) = 0, slope dh/dq = 4/5 > 0",
      sp.expand(h_upper_lo - h_upper_hi) == 0
      and h_formula.subs(q, half) == 0
      and sp.diff(h_formula, q) == sp.Rational(4, 5)
      and positive(sp.diff(h_formula, q)))

# Collinearity certificates (one interior triple per subinterval).
COLLINEAR_A = [
    (sp.Rational(9, 16), sp.Rational(5, 8), sp.Rational(11, 16)),   # inside (1/2, 3/4)
    (sp.Rational(13, 16), sp.Rational(7, 8), sp.Rational(15, 16)),  # inside (3/4, 1)
]
check("WITNESS_A", "witness A h collinear on each subinterval: midpoint equals endpoint average",
      all(h_pw(PIECES_A, mid) == (h_pw(PIECES_A, lo) + h_pw(PIECES_A, hi)) / 2
          for lo, mid, hi in COLLINEAR_A))
check("WITNESS_A", "witness A per-weight influence profile g non-monotone: g(1/2) = 11/20 < g(1/4) = 3/5",
      positive(g_pw(PIECES_A, sp.Rational(1, 4)) - g_pw(PIECES_A, half)))
check("WITNESS_A", "witness A one-step amplification T_A(q) > q at q in {5/8, 3/4, 7/8}",
      all(positive(T_pw(PIECES_A, s) - s)
          for s in (sp.Rational(5, 8), sp.Rational(3, 4), sp.Rational(7, 8))))

# ---------------------------------------------------------------------------
print("[WITNESS_B] Sign-mixed boundary witness B, off-center fixed-point pair {5/22, 17/22}")
PIECES_B = [
    (sp.Integer(0), sp.Rational(1, 4), half, sp.Rational(4, 5)),
    (sp.Rational(1, 4), half, sp.Rational(4, 5), -sp.Rational(2, 5)),
    (half, sp.Rational(3, 4), half, sp.Rational(1, 5)),
    (sp.Rational(3, 4), sp.Integer(1), -sp.Rational(2, 5), sp.Rational(7, 5)),
]
NODES_B = {
    sp.Integer(0): half,
    sp.Rational(1, 4): sp.Rational(7, 10),
    half: sp.Rational(3, 5),
    sp.Rational(3, 4): sp.Rational(13, 20),
    sp.Integer(1): sp.Integer(1),
}
NODES_B_TEXT = "g(0) = 1/2,  g(1/4) = 7/10,  g(1/2) = 3/5,  g(3/4) = 13/20,  g(1) = 1,"
check("WITNESS_B", "witness B node table gated in note text and matched by g exactly",
      flat(NODES_B_TEXT) in flat_note
      and all(g_pw(PIECES_B, node) == value for node, value in NODES_B.items()))
check("WITNESS_B", "witness B g continuous at internal breakpoints 1/4, 1/2, 3/4",
      all(sp.simplify((PIECES_B[i][2] + PIECES_B[i][3] * PIECES_B[i][1])
                      - (PIECES_B[i + 1][2] + PIECES_B[i + 1][3] * PIECES_B[i + 1][0])) == 0
          for i in range(3)))
check("WITNESS_B", "witness B f(0) = 0 and f(1) = 1",
      f_pw(PIECES_B, sp.Integer(0)) == 0 and f_pw(PIECES_B, sp.Integer(1)) == 1)
fprime_B = []
for lo, hi, aa, bb in PIECES_B:
    fprime_B.extend([aa + 2 * bb * lo, aa + 2 * bb * hi])
check("WITNESS_B", "witness B f' > 0 at every piece endpoint (strictly increasing on [0,1])",
      all(positive(v) for v in fprime_B))

check("WITNESS_B", "witness B h(3/4) = -1/20 (negative just above center)",
      h_pw(PIECES_B, sp.Rational(3, 4)) == -sp.Rational(1, 20))
check("WITNESS_B", "witness B h(21/22) = 2/5 > 0 while h(3/4) < 0: sign-mixed on (1/2, 1)",
      h_pw(PIECES_B, sp.Rational(21, 22)) == sp.Rational(2, 5)
      and positive(h_pw(PIECES_B, sp.Rational(21, 22)))
      and not positive(h_pw(PIECES_B, sp.Rational(3, 4))))

# Symbolic h on each side; the upper side carries the off-center zero.
h_B_lo = sp.expand((PIECES_B[2][2] + PIECES_B[2][3] * q)
                   - (PIECES_B[1][2] + PIECES_B[1][3] * (1 - q)))
h_B_hi = sp.expand((PIECES_B[3][2] + PIECES_B[3][3] * q)
                   - (PIECES_B[0][2] + PIECES_B[0][3] * (1 - q)))
check("WITNESS_B", "witness B h(q) = 1/10 - q/5 on (1/2, 3/4)",
      sp.expand(h_B_lo - (sp.Rational(1, 10) - q / 5)) == 0)
check("WITNESS_B", "witness B h(q) = 11q/5 - 17/10 on (3/4, 1)",
      sp.expand(h_B_hi - (sp.Rational(11, 5) * q - sp.Rational(17, 10))) == 0)

# Derive the upper root by solving h = 0 on (3/4, 1), then obtain the lower
# root by the already-proved reflection oddness; do not assert either constant.
qstar_set = sp.solveset(sp.Eq(h_B_hi, 0), q, sp.Interval.open(sp.Rational(3, 4), 1))
check("WITNESS_B", "witness B: solving h(q) = 0 on (3/4, 1) yields exactly {17/22}",
      qstar_set == sp.FiniteSet(sp.Rational(17, 22)))
qstar = list(qstar_set)[0]
qstar_reflected = 1 - qstar
qstar_pair = {qstar_reflected, qstar}
check("WITNESS_B", "reflection gives the off-center pair {5/22, 17/22}",
      qstar_pair == {sp.Rational(5, 22), sp.Rational(17, 22)})
check("WITNESS_B", "both off-center points satisfy T_B(q*) = q* by back-substitution",
      all(T_pw(PIECES_B, root) == root for root in qstar_pair))
upper_low_roots = sp.solveset(
    sp.Eq(h_B_lo, 0), q, sp.Interval.open(half, sp.Rational(3, 4)))
upper_roots = set(upper_low_roots) | set(qstar_set)
closed_fixed_set = (
    {sp.Integer(0), half, sp.Integer(1)}
    | upper_roots
    | {1 - root for root in upper_roots}
)
check("WITNESS_B", "piecewise solve plus reflection gives closed fixed set {0,5/22,1/2,17/22,1}",
      closed_fixed_set
      == {sp.Integer(0), sp.Rational(5, 22), half, sp.Rational(17, 22), sp.Integer(1)})
check("WITNESS_B", "witness B below q*: T_B(7/10) < 7/10 (attenuation region)",
      positive(sp.Rational(7, 10) - T_pw(PIECES_B, sp.Rational(7, 10))))
check("WITNESS_B", "witness B above q*: T_B(9/10) > 9/10 (amplification region)",
      positive(T_pw(PIECES_B, sp.Rational(9, 10)) - sp.Rational(9, 10)))

# ---------------------------------------------------------------------------
print("[IDENTITY] N2 identity member f = x: T_f = q identically, h identically zero")
T_id = q / (q + (1 - q))
check("IDENTITY", "identity member f = x: T_f(q) = q identically",
      sp.simplify(T_id - q) == 0)
check("IDENTITY", "identity member: every rational sample is fixed (T_f(q) = q)",
      all(T_id.subs(q, s) == s
          for s in (sp.Rational(1, 5), sp.Rational(2, 5), half,
                    sp.Rational(3, 5), sp.Rational(4, 5))))
check("IDENTITY", "identity member: per-weight influence profile g = 1, h identically zero",
      sp.simplify(h_sym(lambda t: t, q)) == 0)

# ---------------------------------------------------------------------------
print("[LADDER] Strict ladder M ( A+ ( A ( F on named members")
# Affine subfamily mechanism: for g = c0 + c1 x the asymmetry is h = c1 (2q - 1),
# so strict increase of the profile (c1 > 0) forces h > 0 on (1/2, 1): M => A+.
c0, c1 = sp.symbols("c0 c1", real=True)
h_aff = (c0 + c1 * q) - (c0 + c1 * (1 - q))
check("LADDER", "affine mechanism: profile g = c0 + c1 x gives h(q) = c1 (2q - 1) exactly",
      sp.expand(h_aff - c1 * (2 * q - 1)) == 0)
# Witness A (N0): in A+ (h > 0 on (1/2,1)) but not in M (profile non-monotone).
check("LADDER", "N0 witness in A+ but not M: g(1/2) < g(1/4) and h > 0 at interior samples",
      positive(g_pw(PIECES_A, sp.Rational(1, 4)) - g_pw(PIECES_A, half))
      and all(positive(h_pw(PIECES_A, s))
              for s in (sp.Rational(5, 8), sp.Rational(3, 4), sp.Rational(7, 8))))
# sqrt member: in A- (h < 0 on (1/2,1)), hence in A, not A+, not M.
g_sqrt = 1 / sp.sqrt(x)
check("LADDER", "sqrt member f = sqrt(x): g' = -x^(-3/2)/2 exactly (profile strictly decreasing)",
      sp.simplify(sp.diff(g_sqrt, x) + x ** sp.Rational(-3, 2) / 2) == 0)
check("LADDER", "sqrt member: g'(x) < 0 at x in {1/4, 1/2} (not in M)",
      all(not positive(sp.diff(g_sqrt, x).subs(x, s))
          for s in (sp.Rational(1, 4), half)))
# Conjugate certificate: h(q) sqrt(q) sqrt(1-q) = sqrt(1-q) - sqrt(q), and
# (sqrt(1-q) - sqrt(q))(sqrt(1-q) + sqrt(q)) = 1 - 2q < 0 on (1/2,1), so h < 0
# on all of (1/2,1) (conjugate factor and sqrt(q)sqrt(1-q) are positive there).
h_sqrt = 1 / sp.sqrt(q) - 1 / sp.sqrt(1 - q)
num_sqrt = sp.sqrt(1 - q) - sp.sqrt(q)
conj_sqrt = sp.sqrt(1 - q) + sp.sqrt(q)
check("LADDER", "sqrt member in A-: exact conjugate certificate gives h < 0 on (1/2, 1)",
      sp.simplify(h_sqrt * sp.sqrt(q) * sp.sqrt(1 - q) - num_sqrt) == 0
      and sp.expand(num_sqrt * conj_sqrt - (1 - 2 * q)) == 0
      and sp.simplify_logic(sp.Equivalent(
          sp.reduce_inequalities([q > half, q < 1, h_sqrt < 0], q),
          sp.And(q > half, q < 1))) is sp.true)
check("LADDER", "identity member in F but not A: h identically 0 (no reflection asymmetry)",
      sp.simplify(h_sym(lambda t: t, q)) == 0)
check("LADDER", "witness B in F but not A: reflected off-center zeros h(5/22)=h(17/22)=0",
      all(h_pw(PIECES_B, root) == 0 for root in qstar_pair)
      and half not in qstar_pair)

# ---------------------------------------------------------------------------
print("[SOURCE_GATES] Verbatim quote gates (flattened substring in source AND this note)")
QUOTES = [
    ("Q1 family prose (W1b L2)",
     "the normalized record influence of a continued-registration rule in "
     "that class has the form",
     w1b_text),
    ("Q2 family form (W1b L2)",
     "T_f(q) = f(q) / (f(q)+f(1-q)), f : [0,1] -> [0,1], "
     "f continuous and strictly increasing,  f(0)=0.",
     w1b_text),
    ("Q3 strict-sharpening framing (W1b L3)",
     "For this lemma, **strict sharpening** has its majority-amplification meaning:",
     w1b_text),
    ("Q4 strict-sharpening inequalities (W1b L3)",
     "T_f(q) < q  for 0<q<1/2, T_f(q) > q  for 1/2<q<1.",
     w1b_text),
    ("Q5 scope boundary (W1b)",
     "L3 uses off-center majority amplification as strict sharpening. Bare "
     "monotonicity of the influence odds is insufficient, as N2 shows.",
     w1b_text),
    ("Q10 parent influence-odds definition (W1b)",
     "with input odds `O(q)=q/(1-q)` and influence odds `F(q)=f(q)/f(1-q)`",
     w1b_text),
    ("Q6 Record locking clause (axioms)",
     "When present, a record locks exactly one admissible local possibility. A "
     "site never carries more than one record; records are permanent.",
     axioms_text),
    ("Q7 Record readability clause (axioms)",
     "Only records are readable. A readout value is determined by record "
     "content alone.",
     axioms_text),
    ("Q8 Qualification clause (axioms)",
     "A choice not fixed by the supplied structure remains a named conditional "
     "or open dependency.",
     axioms_text),
    ("Q9 obligation closure criterion",
     "A closing theorem must derive the physical matter action and its "
     "measure, then distinguish the count-once `det_C`/holomorphic "
     "realization from the count-twice `|det_C|^2`/realified realization "
     "without inserting the desired charged-lepton value or readout "
     "dictionary.",
     oblig_text),
]
for name, quote, source in QUOTES:
    fq = flat(quote)
    check("SOURCE_GATES", f"{name}: present verbatim in source and in this note",
          fq in flat(source) and fq in flat_note)

# ---------------------------------------------------------------------------
print("[NOTE_HYGIENE] Note hygiene gates")
outside_fences = []
in_fence = False
for line in note_text.splitlines():
    if line.strip().startswith("```"):
        in_fence = not in_fence
        continue
    if not in_fence:
        outside_fences.append(line)
prose = "\n".join(outside_fences)
decimal_hits = [m.group(0) for m in re.finditer(r"[0-9]\.[0-9]", prose)]
check("NOTE_HYGIENE", "no decimal literals outside code fences in the note",
      decimal_hits == [])
FORBIDDEN = ["closes the route", "only route", "last route", "exhaust",
             "bijection", "final"]
check("NOTE_HYGIENE", "pinned closing / enumeration phrases are absent from the note",
      all(phrase not in note_text.lower() for phrase in FORBIDDEN))
check("NOTE_HYGIENE", "claim-type line is present exactly",
      "**Claim type:** bounded_theorem" in note_text)
check("NOTE_HYGIENE", "required sections and status-authority line are present",
      "## Honest auditor read / Boundary" in note_text
      and "## Non-claims" in note_text
      and "**Status authority:** independent audit lane only." in note_text)
check("NOTE_HYGIENE", "the T5 exact-characterization phrase appears exactly once in the flattened note",
      flat_note.lower().count("necessary and sufficient") == 1)

# ---------------------------------------------------------------------------
print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
sys.exit(1 if FAIL_COUNT else 0)
