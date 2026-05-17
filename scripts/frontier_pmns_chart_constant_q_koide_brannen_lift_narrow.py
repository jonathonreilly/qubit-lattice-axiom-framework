#!/usr/bin/env python3
"""Narrow algebraic theorem: PMNS chart constant Q_Koide = 2/3 Brannen lift.

Verifies the four algebraic-substitution identities of
PMNS_CHART_CONSTANT_Q_KOIDE_BRANNEN_LIFT_NARROW_THEOREM_NOTE_2026-05-17:

  (T1)  Q_Koide = Q = (Σ x_k^2) / (Σ x_k)^2 = 2/3  where
        x_k = v_0 (1 + sqrt(2) cos(delta + 2 pi k / 3)),  v_0 > 0
  (T2)  SELECTOR^2 = (sqrt(6) / 3)^2 = 2/3 = Q_Koide
  (T3)  2 SELECTOR / sqrt(3) = sqrt(8) / 3 = E2
  (T4)  SELECTOR^2 = Q = (Σ x_k^2) / (Σ x_k)^2

Negative control (Part 5) verifies delta * q_+ on the PMNS affine chart is
NOT identically 2/3 — the proposed selector law is a constraint, not an
algebraic identity. This narrow theorem does NOT close that proposed law.
"""
from __future__ import annotations

import math
import sys

import sympy as sp

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if cond else "FAIL"
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return cond


# --------- Brannen-side symbolic ingredients ---------
v0, delta = sp.symbols("v_0 delta", real=True)
k = sp.symbols("k", integer=True)
x_k_expr = v0 * (1 + sp.sqrt(2) * sp.cos(delta + 2 * sp.pi * k / 3))
x_0 = x_k_expr.subs(k, 0)
x_1 = x_k_expr.subs(k, 1)
x_2 = x_k_expr.subs(k, 2)
sum_x = sp.simplify(sp.trigsimp(sp.expand_trig(x_0 + x_1 + x_2)))
sum_x_sq = sp.simplify(sp.trigsimp(sp.expand_trig(x_0 ** 2 + x_1 ** 2 + x_2 ** 2)))
Q_brannen = sp.simplify(sum_x_sq / sum_x ** 2)

# --------- PMNS chart-side constants ---------
Q_KOIDE_CONST = sp.Rational(2, 3)
SELECTOR_CONST = sp.sqrt(6) / 3
E2_CONST = sp.sqrt(8) / 3


print("=" * 72)
print("Part 1: retained Brannen narrow-theorem core identities")
print("=" * 72)

check(
    "1.1 Σ_k x_k = 3 v_0  symbolically",
    sp.simplify(sum_x - 3 * v0) == 0,
    f"Σ x_k = {sum_x}",
)
check(
    "1.2 Σ_k x_k^2 = 6 v_0^2  symbolically",
    sp.simplify(sum_x_sq - 6 * v0 ** 2) == 0,
    f"Σ x_k^2 = {sum_x_sq}",
)
check(
    "1.3 Q := (Σ x_k^2) / (Σ x_k)^2 = 2/3  symbolically in (v_0, delta)",
    sp.simplify(Q_brannen - sp.Rational(2, 3)) == 0,
    f"Q = {Q_brannen}",
)

print("\n" + "=" * 72)
print("Part 2: PMNS chart constants — elementary closed-form arithmetic")
print("=" * 72)

check(
    "2.1 SELECTOR^2 = 6/9 = 2/3",
    sp.simplify(SELECTOR_CONST ** 2 - sp.Rational(2, 3)) == 0,
    f"SELECTOR^2 = {sp.simplify(SELECTOR_CONST ** 2)}",
)
check(
    "2.2 Q_Koide := 2/3 equals SELECTOR^2",
    sp.simplify(Q_KOIDE_CONST - SELECTOR_CONST ** 2) == 0,
    f"Q_Koide - SELECTOR^2 = {sp.simplify(Q_KOIDE_CONST - SELECTOR_CONST ** 2)}",
)
check(
    "2.3 E2 := sqrt(8)/3 equals 2 sqrt(2)/3",
    sp.simplify(E2_CONST - 2 * sp.sqrt(2) / 3) == 0,
    f"E2 = {sp.simplify(E2_CONST)}",
)
check(
    "2.4 2 SELECTOR / sqrt(3) = E2",
    sp.simplify(2 * SELECTOR_CONST / sp.sqrt(3) - E2_CONST) == 0,
    "elementary surd arithmetic",
)

print("\n" + "=" * 72)
print("Part 3: T1, T2, T3, T4 main identities")
print("=" * 72)

check(
    "3.1 (T1) Q_Koide = Q (Brannen narrow theorem value)",
    sp.simplify(Q_KOIDE_CONST - Q_brannen) == 0,
    f"Q_Koide - Q = {sp.simplify(Q_KOIDE_CONST - Q_brannen)}",
)
check(
    "3.2 (T1) Q = 2/3 symbolically",
    sp.simplify(Q_brannen - sp.Rational(2, 3)) == 0,
    f"Q - 2/3 = {sp.simplify(Q_brannen - sp.Rational(2, 3))}",
)
check(
    "3.3 (T2) SELECTOR^2 = Q_Koide = 2/3",
    sp.simplify(SELECTOR_CONST ** 2 - Q_KOIDE_CONST) == 0,
    f"SELECTOR^2 - Q_Koide = {sp.simplify(SELECTOR_CONST ** 2 - Q_KOIDE_CONST)}",
)
check(
    "3.4 (T3) 2 SELECTOR / sqrt(3) = E2 = sqrt(8)/3",
    sp.simplify(2 * SELECTOR_CONST / sp.sqrt(3) - E2_CONST) == 0,
    "elementary closed-form arithmetic",
)
check(
    "3.5 (T4) SELECTOR^2 = Q = (Σ x_k^2)/(Σ x_k)^2 symbolically",
    sp.simplify(SELECTOR_CONST ** 2 - sp.simplify(sum_x_sq / sum_x ** 2)) == 0,
    f"diff = {sp.simplify(SELECTOR_CONST ** 2 - sp.simplify(sum_x_sq / sum_x ** 2))}",
)

print("\n" + "=" * 72)
print("Part 4: numerical sanity at concrete (v_0, delta) grid points")
print("=" * 72)

deltas = [
    sp.Integer(0),
    sp.pi / 12,
    sp.Rational(2, 9),
    sp.pi / 3,
    sp.pi / 2,
    sp.pi,
    sp.Rational(-5, 7),
]
v0s = [sp.Integer(1), sp.pi, sp.E, sp.Rational(13, 5)]

all_ok = True
for d_val in deltas:
    for v_val in v0s:
        q_num = sp.simplify(Q_brannen.subs({delta: d_val, v0: v_val}))
        if sp.simplify(q_num - sp.Rational(2, 3)) != 0:
            all_ok = False
            print(f"  numerical FAIL at (delta, v_0) = ({d_val}, {v_val}): Q = {q_num}")

check(
    f"4.1 Brannen Q = 2/3 at all {len(deltas) * len(v0s)} sampled symbolic (v_0, delta) points",
    all_ok,
    f"{len(deltas)} deltas x {len(v0s)} v_0",
)

for d_f, v_f in [(0.0, 1.0), (math.pi / 7, 2.5), (0.222222222, 3.14)]:
    x = [v_f * (1 + math.sqrt(2) * math.cos(d_f + 2 * math.pi * kk / 3)) for kk in range(3)]
    sx = sum(x)
    sx2 = sum(xi ** 2 for xi in x)
    q_n = sx2 / (sx ** 2)
    check(
        f"4.2 numeric float Q = 2/3 at (delta, v_0) = ({d_f:.4f}, {v_f:.4f})",
        abs(q_n - 2.0 / 3.0) < 1e-14,
        f"|Q - 2/3| = {abs(q_n - 2.0 / 3.0):.2e}",
    )

print("\n" + "=" * 72)
print("Part 5: NEGATIVE CONTROL — delta * q_+ is NOT identically 2/3")
print("=" * 72)

# On the PMNS affine chart, (m, delta, q_+) are independent real coordinates.
# delta * q_+ = Q_Koide is a proposed SELECTOR EQUATION, not an algebraic
# identity. Verify by evaluating at generic chart points.

generic_pairs = [
    (sp.Rational(1, 2), sp.Rational(1, 3)),
    (sp.Integer(1), sp.Integer(1)),
    (sp.Rational(2, 3), sp.Rational(1, 2)),
    (sp.pi, sp.Rational(1, 4)),
]

all_distinct = True
for d_val, q_val in generic_pairs:
    prod = sp.simplify(d_val * q_val)
    diff = sp.simplify(prod - sp.Rational(2, 3))
    if diff == 0:
        all_distinct = False
        print(f"  NEGATIVE-CONTROL FAIL at ({d_val}, {q_val}): product = {prod}")
    else:
        print(f"  generic (delta, q_+) = ({d_val}, {q_val}) -> product = {prod} != 2/3")

check(
    "5.1 delta * q_+ != 2/3 at the sampled generic chart points",
    all_distinct,
    "chart product is a SELECTOR EQUATION, not an algebraic identity",
)

# Sanity: the parent's numerically-recovered point gives product approx 2/3.
prod_star = 0.93305106 * 0.71450181
check(
    "5.2 at recovered point (delta_*, q_+*), product approx 2/3 numerically",
    abs(prod_star - 2.0 / 3.0) < 1e-6,
    f"product = {prod_star:.10f}, 2/3 = {2.0/3.0:.10f}",
)

print()
print("  Honest scope: T1-T4 are algebraic identities on the retained Brannen")
print("  ansatz + PMNS chart constants. The proposed selector law")
print("  delta * q_+ = Q_Koide on the PMNS affine Hermitian chart is NOT")
print("  closed by this narrow theorem; it remains the Open missing_bridge")
print("  target on pmns_selector_three_identity_support_note_2026-04-21.")

print("\n" + "=" * 72)
print(f"Summary: PASS = {PASS}, FAIL = {FAIL}")
print("=" * 72)

if FAIL == 0:
    print("\n  PMNS_CHART_CONSTANT_Q_KOIDE_BRANNEN_LIFT_NARROW_THEOREM = TRUE")
    sys.exit(0)
else:
    print("\n  PMNS_CHART_CONSTANT_Q_KOIDE_BRANNEN_LIFT_NARROW_THEOREM = FALSE")
    sys.exit(1)
