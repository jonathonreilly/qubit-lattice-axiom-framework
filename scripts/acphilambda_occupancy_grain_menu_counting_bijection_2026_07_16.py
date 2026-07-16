#!/usr/bin/env python3
"""Exact verification for the occupancy grain-menu counting-measure bijection note.

Paired note:
  docs/ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_BIJECTION_BOUNDED_THEOREM_NOTE_2026-07-16.md

Every check is exact (sympy Rationals / symbolic identities). No floats enter
any pass condition. Blocks:

  R1  aggregation identity + odds form of the aggregated fixed condition
  R2  n=2 equivalence identity (D1 content = consumed L3 at complementary pairs)
  R3  power family k in {2, 3, 5/2, 4}: D1 membership + exact fixed sets at both grains
  R4  non-power members f = x*e^(x-1), f = (x^2+x^3)/2: codomain + D1 + fixed sets
  R5  T1 classification at n=3 (f = x^2, x^3): the 7 uniform-on-support points
  R6  weight-to-dial bijection arithmetic + menu set equalities + counterfactual
  R7  swap equivariance, surface invariance, aggregated shadow, asymmetry
  R8  exact instability multipliers (= 2) and separatrix match
  R9  T5 negative-control witness: full aggregated fixed set [1/3,2/3] union {8/9}
  R10 verbatim quote gates (flattened substring in source AND in this note)
  R11 note hygiene (no prose decimals, no pinned closing phrases, headers)
"""

import re
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / (
    "docs/ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_"
    "BIJECTION_BOUNDED_THEOREM_NOTE_2026-07-16.md"
)
W1B_PATH = ROOT / (
    "docs/ACPHILAMBDA_OCCUPANCY_GRAIN_RULE_CLASS_UNIVERSALITY_BOUNDED_THEOREM_"
    "NOTE_2026-07-11.md"
)
EXPR_PATH = ROOT / (
    "docs/KOIDE_FORMATION_WEIGHT_LAW_EXPRESSIBILITY_CLASSIFICATION_BOUNDED_"
    "THEOREM_NOTE_2026-07-12.md"
)
OBLIG_PATH = ROOT / "docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md"

PASS_COUNT = 0
FAIL_COUNT = 0
BLOCK_COUNTS = {}


def flat(text):
    return " ".join(text.split())


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


note_text = NOTE_PATH.read_text(encoding="utf-8")
w1b_text = W1B_PATH.read_text(encoding="utf-8")
expr_text = EXPR_PATH.read_text(encoding="utf-8")
oblig_text = OBLIG_PATH.read_text(encoding="utf-8")

q, x = sp.symbols("q x", real=True)
half = sp.Rational(1, 2)
third = sp.Rational(1, 3)
two_thirds = sp.Rational(2, 3)

# ---------------------------------------------------------------------------
print("[R1] Aggregation identity and aggregated fixed-point odds form (symbolic)")
g = sp.Function("g")


def f_of(t):
    return t * g(t)


lhs = 2 * f_of(q / 2) * (1 - q) - q * f_of(1 - q)
rhs = q * (1 - q) * (g(q / 2) - g(1 - q))
check("R1", "2 f(q/2)(1-q) - q f(1-q) = q(1-q)[g(q/2) - g(1-q)] exactly",
      sp.simplify(lhs - rhs) == 0)

F_d, F_s = sp.symbols("F_d F_s", positive=True)
agg_map = F_d / (F_d + F_s)
numer = sp.together(agg_map - q).as_numer_denom()[0]
check("R1", "interior fixed condition of q -> F_d/(F_d+F_s) is F_d(1-q) = q F_s (odds form)",
      sp.simplify(sp.expand(numer) - sp.expand(F_d * (1 - q) - q * F_s)) == 0)

fsym = sp.Function("f")
surface_total = fsym(1 - q) + 2 * fsym(q / 2)
q_prime = 2 * fsym(q / 2) / surface_total
delta = sp.together(q_prime - q)
delta_numer = delta.as_numer_denom()[0]
check("R1", "aggregated displacement numerator is exactly 2 f(q/2)(1-q) - q f(1-q)",
      sp.simplify(sp.expand(delta_numer)
                  - sp.expand(2 * fsym(q / 2) * (1 - q) - q * fsym(1 - q))) == 0)

# ---------------------------------------------------------------------------
print("[R2] n=2 equivalence identity: D1 content = L3 at complementary pairs")
lhs2 = f_of(q) * (1 - q) - q * f_of(1 - q)
rhs2 = q * (1 - q) * (g(q) - g(1 - q))
check("R2", "f(q)(1-q) - q f(1-q) = q(1-q)[g(q) - g(1-q)] exactly",
      sp.simplify(lhs2 - rhs2) == 0)

q0 = sp.Rational(1, 4)
f_sample = lambda t: t**2  # noqa: E731 - exemplar in the class, satisfies D1
g_sample = lambda t: t  # noqa: E731 - g(x) = f(x)/x for f = x^2
sample_l3 = f_sample(q0) * (1 - q0) < q0 * f_sample(1 - q0)
sample_g = g_sample(q0) < g_sample(1 - q0)
sample_identity = (f_sample(q0) * (1 - q0) - q0 * f_sample(1 - q0)
                   == q0 * (1 - q0) * (g_sample(q0) - g_sample(1 - q0)))
check("R2", "exact sample q=1/4, f=x^2: L3 odds inequality, g inequality, identity all hold",
      sample_l3 and sample_g and sample_identity)

# ---------------------------------------------------------------------------
print("[R3] Power family k in {2, 3, 5/2, 4}: exact fixed sets at both grains")
for exponent in (sp.Integer(2), sp.Integer(3), sp.Rational(5, 2), sp.Integer(4)):
    check("R3", f"D1 membership for k={exponent}: g' has empty non-positivity set on (0,1]",
          sp.solveset(sp.diff(x ** (exponent - 1), x) <= 0, x,
                      sp.Interval.Lopen(0, 1)) == sp.S.EmptySet)
    agg_eq = sp.Eq(2 * (q / 2) ** exponent * (1 - q), q * (1 - q) ** exponent)
    agg_sols = sp.solve(agg_eq, q)
    agg_interior = set()
    for s in agg_sols:
        if s.is_real and bool(s > 0) and bool(s < 1) and sp.checksol(agg_eq, q, s):
            agg_interior.add(sp.nsimplify(s))
    check("R3", f"aggregated interior fixed set for k={exponent} is exactly {{2/3}}",
          agg_interior == {two_thirds})

    orbit_eq = sp.Eq(q ** exponent * (1 - q), q * (1 - q) ** exponent)
    orbit_sols = sp.solve(orbit_eq, q)
    check("R3", f"orbit-grain exact solve for k={exponent} yields only {{0, 1/2, 1}}",
          set(orbit_sols) == {sp.Integer(0), half, sp.Integer(1)})

# ---------------------------------------------------------------------------
print("[R4] Non-power members: f = x*e^(x-1) and f = (x^2 + x^3)/2")
# f1 = x e^(x-1)  =>  g1 = e^(x-1)
f1 = lambda t: t * sp.exp(t - 1)  # noqa: E731
check("R4", "f = x e^(x-1): class codomain gates f(0) = 0 and f(1) = 1",
      f1(sp.Integer(0)) == 0 and sp.simplify(f1(sp.Integer(1)) - 1) == 0)
check("R4", "f = x e^(x-1): f' = (1+x) e^(x-1) > 0 on [0,1] (positive exp factor, positive linear factor)",
      sp.exp(x - 1).is_positive
      and sp.solveset(1 + x <= 0, x, sp.Interval(0, 1)) == sp.S.EmptySet)
check("R4", "f = x e^(x-1): D1 membership — g' = e^(x-1) has empty non-positivity set on the reals",
      sp.solveset(sp.exp(x - 1) <= 0, x, sp.S.Reals) == sp.S.EmptySet)
check("R4", "f = x e^(x-1): aggregated stationarity g(q/2) = g(1-q) solves to exactly {2/3}",
      sp.solveset(sp.exp(q / 2 - 1) - sp.exp(-q), q, sp.S.Reals) == sp.FiniteSet(two_thirds))
agg_exp = 2 * f1(q / 2) * (1 - q) - q * f1(1 - q)
check("R4", "f = x e^(x-1): aggregated fixed equation vanishes exactly at q = 2/3",
      sp.simplify(agg_exp.subs(q, two_thirds)) == 0)
check("R4", "f = x e^(x-1): orbit stationarity g(q) = g(1-q) solves to exactly {1/2}",
      sp.solveset(sp.exp(q - 1) - sp.exp(-q), q, sp.S.Reals) == sp.FiniteSet(half))
orb_exp = f1(q) * (1 - q) - q * f1(1 - q)
check("R4", "f = x e^(x-1): orbit fixed equation vanishes exactly at q = 1/2",
      sp.simplify(orb_exp.subs(q, half)) == 0)

# f2 = (x^2 + x^3)/2  =>  g2 = (x + x^2)/2
f2 = lambda t: (t**2 + t**3) / 2  # noqa: E731
check("R4", "f = (x^2 + x^3)/2: class codomain gates f(0) = 0 and f(1) = 1",
      f2(sp.Integer(0)) == 0 and f2(sp.Integer(1)) == 1)
check("R4", "f = (x^2 + x^3)/2: f' = x(2 + 3x)/2 has empty non-positivity set on (0,1]",
      sp.solveset(x * (2 + 3 * x) / 2 <= 0, x, sp.Interval.Lopen(0, 1)) == sp.S.EmptySet)
check("R4", "f = (x^2 + x^3)/2: D1 membership — g' = (1 + 2x)/2 has empty non-positivity set on (0,1]",
      sp.solveset((1 + 2 * x) / 2 <= 0, x, sp.Interval.Lopen(0, 1)) == sp.S.EmptySet)
agg_poly = sp.expand(2 * f2(q / 2) * (1 - q) - q * f2(1 - q))
check("R4", "f = (x^2 + x^3)/2: aggregated interior fixed set is exactly {2/3}",
      sp.solveset(sp.Eq(agg_poly, 0), q, sp.Interval.open(0, 1)) == sp.FiniteSet(two_thirds))
orb_poly = sp.expand(f2(q) * (1 - q) - q * f2(1 - q))
check("R4", "f = (x^2 + x^3)/2: orbit interior fixed set is exactly {1/2}",
      sp.solveset(sp.Eq(orb_poly, 0), q, sp.Interval.open(0, 1)) == sp.FiniteSet(half))

# ---------------------------------------------------------------------------
print("[R5] T1 at n=3: simplex fixed set = the 7 uniform-on-support points")
p1, p2, p3 = sp.symbols("p1 p2 p3", real=True)
EXPECTED_SEVEN = {
    (sp.Integer(1), sp.Integer(0), sp.Integer(0)),
    (sp.Integer(0), sp.Integer(1), sp.Integer(0)),
    (sp.Integer(0), sp.Integer(0), sp.Integer(1)),
    (half, half, sp.Integer(0)),
    (half, sp.Integer(0), half),
    (sp.Integer(0), half, half),
    (third, third, third),
}
for exponent in (2, 3):
    total = p1**exponent + p2**exponent + p3**exponent
    system = [
        p1**exponent - p1 * total,
        p2**exponent - p2 * total,
        p3**exponent - p3 * total,
        p1 + p2 + p3 - 1,
    ]
    raw = sp.solve(system, [p1, p2, p3], dict=True)
    simplex_fixed = set()
    for sol in raw:
        vals = tuple(sp.nsimplify(sol[v]) for v in (p1, p2, p3))
        if all(v.is_real and bool(v >= 0) and bool(v <= 1) for v in vals):
            simplex_fixed.add(vals)
    check("R5", f"f = x^{exponent}: n=3 simplex fixed set is exactly the 7 uniform-on-support points",
          simplex_fixed == EXPECTED_SEVEN)
check("R5", "uniform-on-support count at n=3 is 2^3 - 1 = 7",
      2**3 - 1 == 7 and len(EXPECTED_SEVEN) == 7)

# ---------------------------------------------------------------------------
print("[R6] Weight-to-dial bijection arithmetic and menu set equalities")


def dial(w):
    return (1 - w) / (2 * w)


check("R6", "orbit grain: w = 1/2 maps to dial r = 1/2", dial(half) == half)
check("R6", "sector grain: w = 1/3 maps to dial r = 1", dial(third) == sp.Integer(1))
w_orbit = 1 - half        # uniform on 2 cells: singlet weight 1/2
w_sector = 1 - two_thirds  # aggregated q = 2/3: singlet weight 1/3
check("R6", "dynamical durable weights {1/2, 1/3} equal the licensed static menu W_expr",
      {w_orbit, w_sector} == {half, third})
check("R6", "dial image of the menu is exactly {1/2, 1}",
      {dial(w_orbit), dial(w_sector)} == {half, sp.Integer(1)})
counterfactual = dial(sp.Rational(1, 4))
check("R6", "counterfactual 4-cell menu: w = 1/4 -> r = 3/2, outside both licensed sets",
      counterfactual == sp.Rational(3, 2)
      and counterfactual not in {half, sp.Integer(1)}
      and sp.Rational(1, 4) not in {half, third})

# ---------------------------------------------------------------------------
print("[R7] Swap equivariance, surface invariance, aggregated shadow, asymmetry")
a, b, c = sp.symbols("a b c", positive=True)
S3 = fsym(a) + fsym(b) + fsym(c)
T3map = (fsym(a) / S3, fsym(b) / S3, fsym(c) / S3)
S3_swapped = fsym(a) + fsym(c) + fsym(b)
T3_swapped = (fsym(a) / S3_swapped, fsym(c) / S3_swapped, fsym(b) / S3_swapped)
check("R7", "swap equivariance: T(p_s, p_wbar, p_w) = swap T(p_s, p_w, p_wbar) componentwise",
      all(sp.simplify(T3_swapped[i] - (T3map[0], T3map[2], T3map[1])[i]) == 0
          for i in range(3)))
check("R7", "surface invariance: T_w = T_wbar exactly when p_w = p_wbar",
      sp.simplify((T3map[1] - T3map[2]).subs(c, b)) == 0)
surf_S = fsym(1 - q) + 2 * fsym(q / 2)
shadow = sp.simplify(fsym(q / 2) / surf_S + fsym(q / 2) / surf_S
                     - 2 * fsym(q / 2) / (fsym(1 - q) + 2 * fsym(q / 2)))
check("R7", "aggregated shadow: q' = T_w + T_wbar = 2 f(q/2) / (f(1-q) + 2 f(q/2)) on the surface",
      shadow == 0)
check("R7", "exemplar f = x^2: f_d(q) = 2 f(q/2) = q^2/2 differs from f_s(q) = q^2",
      sp.simplify(2 * (q / 2) ** 2 - q**2) != 0)
check("R7", "identity profile f = x: f_d(q) = 2 f(q/2) = q coincides with f_s (contrast case)",
      sp.simplify(2 * (q / 2) - q) == 0)
check("R7", "strict asymmetry identity: 2 f(q/2) - f(q) = q [g(q/2) - g(q)] exactly",
      sp.simplify((2 * f_of(q / 2) - f_of(q)) - q * (g(q / 2) - g(q))) == 0)

# ---------------------------------------------------------------------------
print("[R8] Exact instability multipliers and separatrix match")
total_sq = p1**2 + p2**2 + p3**2
T_sq = sp.Matrix([p1**2 / total_sq, p2**2 / total_sq, p3**2 / total_sq])
jacobian = T_sq.jacobian([p1, p2, p3]).subs({p1: third, p2: third, p3: third})
v_odd = sp.Matrix([0, 1, -1])
check("R8", "f = x^2, n=3: transverse swap-odd mode (0,1,-1) has exact multiplier 2",
      sp.simplify(jacobian * v_odd - 2 * v_odd) == sp.zeros(3, 1))
T_orbit = q**2 / (q**2 + (1 - q) ** 2)
check("R8", "f = x^2, orbit grain: multiplier at q = 1/2 is exactly 2",
      sp.diff(T_orbit, q).subs(q, half) == 2)
T_agg = (q**2 / 2) / (q**2 / 2 + (1 - q) ** 2)
check("R8", "f = x^2, aggregated sector grain: q = 2/3 is a fixed point",
      sp.simplify(T_agg.subs(q, two_thirds) - two_thirds) == 0)
check("R8", "f = x^2, aggregated sector grain: multiplier at q = 2/3 is exactly 2",
      sp.simplify(sp.diff(T_agg, q).subs(q, two_thirds)) == 2)
r_sym = sp.symbols("r", real=True)
check("R8", "separatrix exemplar r -> 2 r^2: multiplier at r = 1/2 is exactly 2",
      sp.diff(2 * r_sym**2, r_sym).subs(r_sym, half) == 2)

# ---------------------------------------------------------------------------
print("[R9] T5 witness: piecewise-linear g separating D1 from 2-cell L3")
# g = a + b*x on each piece
PIECES = [
    (sp.Integer(0), sp.Rational(1, 6), sp.Rational(2, 5), sp.Rational(3, 5)),
    (sp.Rational(1, 6), third, sp.Rational(11, 20), -sp.Rational(3, 10)),
    (third, two_thirds, sp.Rational(2, 5), sp.Rational(3, 20)),
    (two_thirds, sp.Integer(1), sp.Rational(1, 10), sp.Rational(3, 5)),
]


def g_witness(t):
    for lo, hi, aa, bb in PIECES:
        if bool(lo <= t) and bool(t <= hi):
            return aa + bb * t
    raise ValueError(f"witness g evaluated outside [0,1]: {t}")


def f_witness(t):
    return t * g_witness(t)


NODES = {
    sp.Integer(0): sp.Rational(2, 5),
    sp.Rational(1, 6): half,
    third: sp.Rational(9, 20),
    two_thirds: half,
    sp.Rational(5, 6): sp.Rational(3, 5),
    sp.Integer(1): sp.Rational(7, 10),
}
check("R9", "witness node values match the declared table exactly",
      all(g_witness(node) == value for node, value in NODES.items()))
check("R9", "witness g is continuous at the internal breakpoints 1/6, 1/3, 2/3",
      all(sp.simplify((PIECES[i][2] + PIECES[i][3] * PIECES[i][1])
                      - (PIECES[i + 1][2] + PIECES[i + 1][3] * PIECES[i + 1][0])) == 0
          for i in range(3)))
check("R9", "witness f(0) = 0 and f(1) = 7/10 <= 1",
      f_witness(sp.Integer(0)) == 0 and f_witness(sp.Integer(1)) == sp.Rational(7, 10)
      and f_witness(sp.Integer(1)) <= 1)

fprime_endpoint_values = []
for lo, hi, aa, bb in PIECES:
    # f = a x + b x^2 on the piece, so f' = a + 2 b x is linear: piece minimum
    # of f' sits at an endpoint.
    fprime_endpoint_values.extend([aa + 2 * bb * lo, aa + 2 * bb * hi])
check("R9", "witness f' > 0 at every piece endpoint (strict increase on [0,1])",
      all(bool(v > 0) for v in fprime_endpoint_values))
check("R9", "named per-piece minima: f'(0) = 2/5 on piece 1, f'(1/3) = 7/20 on piece 2, f' >= 2/5 on piece 3",
      PIECES[0][2] + 2 * PIECES[0][3] * 0 == sp.Rational(2, 5)
      and PIECES[1][2] + 2 * PIECES[1][3] * third == sp.Rational(7, 20)
      and all(bool(PIECES[2][2] + 2 * PIECES[2][3] * t - sp.Rational(2, 5) >= 0)
              for t in (third, two_thirds)))


def h_witness(t):
    return g_witness(1 - t) - g_witness(t)


H_BREAK_VALUES = {
    sp.Integer(0): sp.Rational(3, 10),
    sp.Rational(1, 6): sp.Rational(1, 10),
    third: sp.Rational(1, 20),
    half: sp.Integer(0),
}
check("R9", "h breakpoint values on [0,1/2] are exactly (3/10, 1/10, 1/20, 0)",
      all(h_witness(node) == value for node, value in H_BREAK_VALUES.items()))
samples = (sp.Rational(1, 12), sp.Rational(1, 4), sp.Rational(5, 12))
check("R9", "h > 0 at interior samples of (0,1/2) and h(1-q) = -h(q) at those samples",
      all(bool(h_witness(s) > 0) and h_witness(1 - s) == -h_witness(s) for s in samples))
node_set = set(NODES.keys())
h_breaks = {n for n in node_set if bool(n > 0) and bool(n < half)}
h_breaks |= {1 - n for n in node_set if bool(1 - n > 0) and bool(1 - n < half)}
check("R9", "h breakpoint set on (0,1/2) is exactly {1/6, 1/3}",
      h_breaks == {sp.Rational(1, 6), third})

interior_zeros = set()
h_grid = sorted(set(list(H_BREAK_VALUES.keys())
                    + [1 - n for n in H_BREAK_VALUES.keys()]))
for lo, hi in zip(h_grid[:-1], h_grid[1:]):
    v_lo, v_hi = h_witness(lo), h_witness(hi)
    # h is linear on [lo, hi] (breakpoints exhaust the grid): interpolate exactly.
    line = v_lo + (v_hi - v_lo) * (q - lo) / (hi - lo)
    zeros = sp.solveset(sp.Eq(line, 0), q, sp.Interval(lo, hi))
    for z in zeros:
        if bool(z > 0) and bool(z < 1):
            interior_zeros.add(sp.nsimplify(z))
check("R9", "witness 2-cell interior fixed set (zeros of h on (0,1)) is exactly {1/2}",
      interior_zeros == {half})
check("R9", "linearity certificate: h at each sub-piece midpoint equals the endpoint average",
      all(h_witness((lo + hi) / 2) == (h_witness(lo) + h_witness(hi)) / 2
          for lo, hi in zip(h_grid[:-1], h_grid[1:])))

check("R9", "D1 fails: g(1/6) = g(2/3) = 1/2 while g(1/3) = 9/20 < 1/2 with 1/6 < 1/3",
      g_witness(sp.Rational(1, 6)) == half and g_witness(two_thirds) == half
      and g_witness(third) == sp.Rational(9, 20) and bool(g_witness(third) < half)
      and bool(sp.Rational(1, 6) < third))

p_bad = (two_thirds, sp.Rational(1, 6), sp.Rational(1, 6))
S_bad = sum(f_witness(t) for t in p_bad)
T_bad = tuple(f_witness(t) / S_bad for t in p_bad)
check("R9", "n=3 non-uniform fixed point: f(2/3) = 1/3, f(1/6) = 1/12, S = 1/2, T(p) = p",
      f_witness(two_thirds) == third and f_witness(sp.Rational(1, 6)) == sp.Rational(1, 12)
      and S_bad == half and T_bad == p_bad and p_bad[0] != p_bad[1])

def g_expr_on(t_expr, i):
    return PIECES[i][2] + PIECES[i][3] * t_expr


Q_PIECES = [
    (sp.Integer(0), third, 0, 3),
    (third, two_thirds, 1, 2),
    (two_thirds, sp.Rational(5, 6), 2, 1),
    (sp.Rational(5, 6), sp.Integer(1), 2, 0),
]
check("R9", "piece mapping: on each q-piece, q/2 and 1-q stay inside the named g-pieces",
      all(bool(PIECES[ih][0] <= lo / 2) and bool(hi / 2 <= PIECES[ih][1])
          and bool(PIECES[il][0] <= 1 - hi) and bool(1 - lo <= PIECES[il][1])
          for lo, hi, ih, il in Q_PIECES))

PHI_EXPECTED = [
    sp.Rational(9, 10) * q - sp.Rational(3, 10),
    sp.Integer(0),
    sp.Rational(3, 20) - sp.Rational(9, 40) * q,
    sp.Rational(27, 40) * q - sp.Rational(3, 5),
]
for (lo, hi, ih, il), expected in zip(Q_PIECES, PHI_EXPECTED):
    phi_piece = sp.expand(g_expr_on(q / 2, ih) - g_expr_on(1 - q, il))
    check("R9", f"phi(q) = g(q/2) - g(1-q) on q-piece [{lo}, {hi}] equals the declared formula",
          sp.expand(phi_piece - expected) == 0)

check("R9", "identically-zero segment: g(q/2) and g(1-q) are the SAME polynomial 11/20 - 3q/20 on [1/3, 2/3]",
      sp.expand(g_expr_on(q / 2, 1)) == sp.expand(g_expr_on(1 - q, 2))
      and sp.expand(g_expr_on(q / 2, 1))
      == sp.expand(sp.Rational(11, 20) - sp.Rational(3, 20) * q))

zero_sets = []
for (lo, hi, ih, il), expected in zip(Q_PIECES, PHI_EXPECTED):
    if expected == 0:
        continue
    zero_sets.append(sp.solveset(sp.Eq(expected, 0), q, sp.Interval(lo, hi)))
check("R9", "non-flat phi pieces have unique zeros exactly at q = 1/3, 2/3, 8/9",
      zero_sets == [sp.FiniteSet(third), sp.FiniteSet(two_thirds),
                    sp.FiniteSet(sp.Rational(8, 9))])

assembled = sp.Union(sp.Interval(third, two_thirds), *zero_sets)
check("R9", "assembled aggregated interior fixed set is exactly [1/3, 2/3] union {8/9}",
      assembled == sp.Union(sp.Interval(third, two_thirds),
                            sp.FiniteSet(sp.Rational(8, 9))))

SPOTS = {
    sp.Rational(2, 5): sp.Rational(147, 1250),
    half: sp.Rational(19, 160),
    sp.Rational(3, 5): sp.Rational(69, 625),
    sp.Rational(8, 9): sp.Rational(56, 1215),
}
check("R9", "spot identities 2 f(q/2)(1-q) = q f(1-q) at q = 2/5, 1/2, 3/5, 8/9 with declared exact values",
      all(2 * f_witness(s / 2) * (1 - s) == v and s * f_witness(1 - s) == v
          for s, v in SPOTS.items()))

p_mid = (half, sp.Rational(1, 4), sp.Rational(1, 4))
S_mid = sum(f_witness(t) for t in p_mid)
T_mid = tuple(f_witness(t) / S_mid for t in p_mid)
check("R9", "non-counting durable profile (1/2, 1/4, 1/4): g(1/4) = g(1/2) = 19/40, S = 19/40, T(p) = p",
      g_witness(sp.Rational(1, 4)) == sp.Rational(19, 40)
      and g_witness(half) == sp.Rational(19, 40)
      and f_witness(half) == sp.Rational(19, 80)
      and f_witness(sp.Rational(1, 4)) == sp.Rational(19, 160)
      and S_mid == sp.Rational(19, 40) and T_mid == p_mid and p_mid[0] != p_mid[1])
check("R9", "midpoint registers the LICENSED dial: q = 1/2 gives w = 1/2, r = 1/2 in the menu",
      dial(half) == half and dial(half) in {half, sp.Integer(1)})

c_common = sp.Rational(11, 20) - sp.Rational(3, 20) * q
f_s_seg = (1 - q) * g_expr_on(1 - q, 2)
f_w_seg = (q / 2) * g_expr_on(q / 2, 1)
S_seg = sp.expand(f_s_seg + 2 * f_w_seg)
check("R9", "fixed-segment mechanism on [1/3, 2/3]: S = c(q), ratios exactly 1-q and q/2 (T(p) = p identically)",
      sp.simplify(S_seg - c_common) == 0
      and sp.simplify(f_s_seg / c_common - (1 - q)) == 0
      and sp.simplify(f_w_seg / c_common - q / 2) == 0)

check("R9", "segment endpoint q = 1/3: 2 f(1/6)(2/3) = 1/9 = (1/3) f(2/3); dial r = 1/4 outside the menu",
      2 * f_witness(sp.Rational(1, 6)) * two_thirds == sp.Rational(1, 9)
      and third * f_witness(two_thirds) == sp.Rational(1, 9)
      and dial(two_thirds) == sp.Rational(1, 4)
      and dial(two_thirds) not in {half, sp.Integer(1)}
      and two_thirds not in {half, third})
check("R9", "segment endpoint q = 2/3 stays fixed: 2 f(1/3)(1/3) = (2/3) f(1/3) = 1/10",
      2 * f_witness(third) * third == sp.Rational(1, 10)
      and two_thirds * f_witness(third) == sp.Rational(1, 10))
check("R9", "isolated fixed point q = 8/9: g(4/9) = g(1/9) = 7/15; singlet weight w = 1/9, dial r = 4",
      g_witness(sp.Rational(4, 9)) == sp.Rational(7, 15)
      and g_witness(sp.Rational(1, 9)) == sp.Rational(7, 15)
      and dial(sp.Rational(1, 9)) == sp.Integer(4))
w_sym = sp.symbols("w", positive=True)
r_of_w = (1 - w_sym) / (2 * w_sym)
check("R9", "dial sweep: dr/dw = -1/(2 w^2) < 0; segment weights w in [1/3, 2/3] sweep r in [1/4, 1]",
      sp.simplify(sp.diff(r_of_w, w_sym) + 1 / (2 * w_sym**2)) == 0
      and r_of_w.subs(w_sym, two_thirds) == sp.Rational(1, 4)
      and r_of_w.subs(w_sym, third) == sp.Integer(1))

# ---------------------------------------------------------------------------
print("[R10] Verbatim quote gates (flattened substring in source AND this note)")
QUOTES = [
    ("Q1 class prose",
     "the normalized record influence of a continued-registration rule in "
     "that class has the form",
     w1b_text),
    ("Q2 class form",
     "T_f(q) = f(q) / (f(q)+f(1-q)), f : [0,1] -> [0,1], "
     "f continuous and strictly increasing, f(0)=0.",
     w1b_text),
    ("Q3 recording distinction",
     "an admissible **continued-registration** rule is a recording update: "
     "its off-center action strictly amplifies the majority sector in the "
     "sense stated in L3. The identity family in N2 is non-recording dynamics "
     "and is therefore a negative control outside that recording-update "
     "hypothesis",
     w1b_text),
    ("Q4 symmetric-family reading (L2)",
     "Under this declared reading, the same `f` acts on both sectors. An "
     "asymmetric pair `f_s != f_d` lies outside the declared symmetric "
     "family and is tested in N1 as a load-bearing negative control",
     w1b_text),
    ("Q5 strict-sharpening meaning (L3)",
     "T_f(q) < q for 0<q<1/2, T_f(q) > q for 1/2<q<1.",
     w1b_text),
    ("Q6 negative-control contrast",
     "N3 is an exact contrast, not a competing derivation.",
     w1b_text),
    ("Q7 licensed static menu",
     "W_expr = {1/3, 1/2}.",
     expr_text),
    ("Q8 weight-to-dial coordinates",
     "cell probabilities = (w, 1-w) = (singlet, doublet), r = (1-w)/(2w).",
     expr_text),
    ("Q9 unadopted-energy-dictionary hedge",
     "Using the relocation theorem's explicitly unadopted energy dictionary "
     "(Residual Atom 2), the coordinate map is",
     expr_text),
    ("Q10 obligation closure criterion (two-part)",
     "A closing theorem must derive the physical matter action and its "
     "measure, then distinguish the count-once `det_C`/holomorphic "
     "realization from the count-twice `|det_C|^2`/realified realization "
     "without inserting the desired charged-lepton value or readout "
     "dictionary.",
     oblig_text),
]
flat_note = flat(note_text)
for name, quote, source in QUOTES:
    fq = flat(quote)
    check("R10", f"{name}: present verbatim in source and in this note",
          fq in flat(source) and fq in flat_note)

# ---------------------------------------------------------------------------
print("[R11] Note hygiene gates")
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
check("R11", "no decimal literals outside code fences in the note",
      decimal_hits == [])
FORBIDDEN = ["closes the route", "only route", "last route", "exhaust"]
check("R11", "pinned closing phrases are absent from the note",
      all(phrase not in note_text.lower() for phrase in FORBIDDEN))
check("R11", "claim-type line is present exactly",
      "**Claim type:** bounded_theorem" in note_text)
check("R11", "required sections and status-authority line are present",
      "## Honest auditor read / Boundary" in note_text
      and "## Non-claims" in note_text
      and "**Status authority:** independent audit lane only." in note_text)

# ---------------------------------------------------------------------------
print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
sys.exit(1 if FAIL_COUNT else 0)
