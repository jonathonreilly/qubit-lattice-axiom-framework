#!/usr/bin/env python3
"""Finite local Z_3 normal-plane density and commutant certificate.

This runner proves only a two-real-dimensional representation-theory result:
the body-diagonal order-three rotation has a scalar symmetric commutant on one
real normal plane, its inverse-normal-determinant average is 2/9, and several
finite character identities agree with that value.

It does not identify the finite average with an operator eta invariant. It
does not prove an isolated-point theorem in four real dimensions, a global
metric theorem, a PL/smooth bridge, a spin-lift theorem, or a physical readout.
Those are separate open obligations.
"""

from __future__ import annotations

import math
import sys

import sympy as sp


PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> bool:
    """Print and count one exact certificate."""
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    message = f"  [{status}] {label}"
    if detail:
        message += f"  ({detail})"
    print(message)
    return condition


OMEGA = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
OMEGA2 = sp.Rational(-1, 2) - sp.I * sp.sqrt(3) / 2
ROOTS = [sp.Integer(1), OMEGA, OMEGA2]


def inverse_normal_determinant_average(a: int, b: int, p: int = 3):
    """Return the defined finite average for two nontrivial characters."""
    if p != 3:
        raise NotImplementedError("this finite certificate is specialized to p=3")
    total = sp.Rational(0)
    for k in range(1, p):
        z_a = ROOTS[(k * a) % p]
        z_b = ROOTS[(k * b) % p]
        total += 1 / ((z_a - 1) * (z_b - 1))
    return sp.simplify(sp.nsimplify(total / p))


def character_weighted_average(character: int):
    """Compute, rather than install, one character-weighted finite average."""
    total = sp.Rational(0)
    for k in (1, 2):
        numerator = ROOTS[(character * k) % 3]
        denominator = (ROOTS[k] - 1) * (ROOTS[(2 * k) % 3] - 1)
        total += numerator / denominator
    return sp.simplify(sp.nsimplify(total / 3))


print("=" * 72)
print("LOCAL Z_3 NORMAL-PLANE DENSITY CERTIFICATE")
print("=" * 72)
print(
    """
Scope under test
----------------
The representation is one real two-dimensional normal plane with the order-
three rotation R(2*pi/3). Its complex eigencharacters are the conjugate pair
(1,2). The finite functional checked here is defined by

  L(a,b) = (1/3) * sum_{k=1,2}
           1 / ((zeta^(k*a)-1) * (zeta^(k*b)-1)).

The executable conclusions are deliberately local:

  * det_R(I-R) is 3;
  * L(1,2) is 2/9;
  * the symmetric commutant of R on this one real plane is scalar;
  * finite character-weighted versions agree with direct evaluation.

The calculation is not an operator localization theorem. A pair of complex
tangent weights at an isolated point would be a four-real-dimensional
representation, whose symmetric commutant is not the one computed below.
Nothing here establishes a global manifold, smoothability, a spin lift,
operator metric invariance, a physical carrier, a unit, or a readout map.
"""
)


# ---------------------------------------------------------------------------
# T1. Direct evaluation of the defined finite average: 5 checks
# ---------------------------------------------------------------------------
print("=" * 72)
print("T1: DIRECT FINITE-AVERAGE EVALUATION")
print("=" * 72)
print(
    """
These checks use exact cube roots of unity. They establish values of the
declared finite rational function only. The symbol L is a local density label;
no operator invariant is inferred from its value.
"""
)

density_12 = inverse_normal_determinant_average(1, 2)
check(
    "(T1.1) L(1,2) = 2/9",
    sp.simplify(density_12 - sp.Rational(2, 9)) == 0,
    f"L(1,2) = {density_12}",
)

density_21 = inverse_normal_determinant_average(2, 1)
check(
    "(T1.2) L is symmetric under character permutation",
    sp.simplify(density_12 - density_21) == 0,
    f"L(2,1) = {density_21}",
)

density_11 = inverse_normal_determinant_average(1, 1)
check(
    "(T1.3) L(1,1) = 1/9",
    sp.simplify(density_11 - sp.Rational(1, 9)) == 0,
    f"L(1,1) = {density_11}",
)

density_14 = inverse_normal_determinant_average(1, 4)
check(
    "(T1.4) L(1,4) = L(1,1), so characters reduce modulo three",
    sp.simplify(density_14 - density_11) == 0,
    f"L(1,4) = {density_14}",
)

density_15 = inverse_normal_determinant_average(1, 5)
check(
    "(T1.5) L(1,5) = L(1,2), so characters reduce modulo three",
    sp.simplify(density_15 - density_12) == 0,
    f"L(1,5) = {density_15}",
)


# ---------------------------------------------------------------------------
# T2. Symmetric commutant on one real normal plane: 11 checks
# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("T2: ONE REAL NORMAL-PLANE COMMUTANT")
print("=" * 72)
print(
    """
Let G be a general symmetric 2x2 bilinear form on one real normal plane.
Solving R^T G R = G for the plane rotation is a complete calculation in this
two-real-dimensional domain. It does not describe a four-dimensional tangent
space or metrics away from the fixed normal fibre.
"""
)

rotation = sp.Matrix(
    [
        [sp.cos(2 * sp.pi / 3), -sp.sin(2 * sp.pi / 3)],
        [sp.sin(2 * sp.pi / 3), sp.cos(2 * sp.pi / 3)],
    ]
)
rotation = sp.simplify(rotation)

g11, g12, g22 = sp.symbols("g11 g12 g22", real=True)
metric = sp.Matrix([[g11, g12], [g12, g22]])
equivariance = sp.simplify(rotation.T * metric * rotation - metric)
solutions = sp.solve(
    [equivariance[0, 0], equivariance[0, 1], equivariance[1, 1]],
    [g12, g22],
    dict=True,
)

check(
    "(T2.1) the 2x2 symmetric commutant has g12=0 and g22=g11",
    len(solutions) == 1
    and sp.simplify(solutions[0][g12]) == 0
    and sp.simplify(solutions[0][g22] - g11) == 0,
    f"solutions = {solutions}",
)

scale = sp.symbols("scale", positive=True)
scaled_identity = scale * sp.eye(2)
check(
    "(T2.2) every positive scalar multiple of I is invariant on the plane",
    sp.simplify(rotation.T * scaled_identity * rotation - scaled_identity)
    == sp.zeros(2, 2),
    "R^T (scale I) R = scale I",
)

check(
    "(T2.3) the finite average itself contains no metric variable",
    {g11, g12, g22, scale}.isdisjoint(density_12.free_symbols),
    f"free symbols = {density_12.free_symbols}",
)

for m, n in [
    (0, 0),
    (1, 0),
    (0, 1),
    (1, 1),
    (2, 3),
    (-1, 2),
    (3, 3),
    (-2, -1),
]:
    a_raw = 1 + 3 * m
    b_raw = 2 + 3 * n
    lifted = inverse_normal_determinant_average(a_raw, b_raw)
    check(
        f"(T2.4-{m},{n}) the lift ({a_raw},{b_raw}) gives 2/9",
        sp.simplify(lifted - sp.Rational(2, 9)) == 0,
        f"L({a_raw},{b_raw}) = {lifted}",
    )


# ---------------------------------------------------------------------------
# T3. Real determinant identities: 5 checks
# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("T3: FINITE DETERMINANT IDENTITIES")
print("=" * 72)
print(
    """
The determinant factor is representation-theoretic. For the conjugate
characters it is the real determinant of I-R on the single normal plane.
For equal characters the script checks the exact squared magnitude instead.
"""
)

determinant_12 = sp.simplify((1 - OMEGA) * (1 - OMEGA2))
check(
    "(T3.1) (1-zeta)(1-zeta^2) = 3",
    sp.simplify(determinant_12 - 3) == 0,
    f"determinant factor = {determinant_12}",
)

for a, b in [(1, 1), (1, 2), (2, 1), (2, 2)]:
    factor = sp.simplify((1 - OMEGA**a) * (1 - OMEGA**b))
    if (a, b) in {(1, 2), (2, 1)}:
        condition = sp.simplify(factor - 3) == 0
        detail = f"factor = {factor}"
    else:
        magnitude_squared = sp.simplify(sp.Abs(factor) ** 2)
        condition = sp.simplify(magnitude_squared - 9) == 0
        detail = f"|factor|^2 = {magnitude_squared}"
    check(
        f"(T3.2-{a},{b}) exact determinant check for ({a},{b})",
        condition,
        detail,
    )


# ---------------------------------------------------------------------------
# T4. Character-weighted finite averages: 4 checks
# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("T4: CHARACTER-WEIGHTED FINITE AVERAGES")
print("=" * 72)
print(
    """
Each of the three character values is independently evaluated from the same
finite sum. Their linear combination is then checked symbolically. This is a
finite representation-ring identity, not a claim about a specified operator.
"""
)

weighted_0 = character_weighted_average(0)
weighted_1 = character_weighted_average(1)
weighted_2 = character_weighted_average(2)

check(
    "(T4.1) the trivial character gives 2/9",
    weighted_0 == sp.Rational(2, 9),
    f"value = {weighted_0}",
)
check(
    "(T4.2) the two nontrivial characters each give -1/9",
    weighted_1 == weighted_2 == sp.Rational(-1, 9),
    f"values = ({weighted_1}, {weighted_2})",
)
check(
    "(T4.3) the sum over all three characters vanishes",
    sp.simplify(weighted_0 + weighted_1 + weighted_2) == 0,
    f"sum = {sp.simplify(weighted_0 + weighted_1 + weighted_2)}",
)

m0, m1, m2 = sp.symbols("m0 m1 m2", integer=True)
weighted_linear = sp.expand(m0 * weighted_0 + m1 * weighted_1 + m2 * weighted_2)
check(
    "(T4.4) the weighted average is rational-linear in multiplicities",
    sp.simplify(weighted_linear - (2 * m0 - m1 - m2) / 9) == 0,
    f"value = {weighted_linear}",
)


# ---------------------------------------------------------------------------
# T5. Integer-shift arithmetic: 6 checks
# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("T5: ELEMENTARY INTEGER-SHIFT ARITHMETIC")
print("=" * 72)
print(
    """
This section checks only that adding an integer does not change the fractional
part of 2/9. It is not evidence for an operator variation theorem; any such
theorem needs its own operator, hypotheses, and direct authority.
"""
)

for integer_shift in [0, 1, -1, 5, -3, 100]:
    shifted = sp.Rational(2, 9) + integer_shift
    fractional_part = shifted - sp.floor(shifted)
    check(
        f"(T5.{integer_shift}) frac(2/9 + {integer_shift}) = 2/9",
        fractional_part == sp.Rational(2, 9),
        f"fractional part = {fractional_part}",
    )


# ---------------------------------------------------------------------------
# T6. Coprimality and odd-order parity arithmetic: 6 checks
# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("T6: COPRIMALITY AND ODD-ORDER PARITY")
print("=" * 72)
print(
    """
These checks are recorded as elementary number theory only. Coprimality of
the character labels and absence of order-two elements in an odd cyclic group
do not by themselves prove smoothability, an equivariant spin lift, existence
of an operator, or uniqueness of any global structure.
"""
)

gcd_value = math.gcd(math.gcd(1, 2), 3)
check(
    "(T6.1) gcd(1,2,3) = 1",
    gcd_value == 1,
    f"gcd = {gcd_value}",
)

for odd_order in [3, 5, 7, 9, 11]:
    check(
        f"(T6.2-{odd_order}) the odd order {odd_order} is not divisible by two",
        odd_order % 2 == 1 and math.gcd(2, odd_order) == 1,
        f"gcd(2,{odd_order}) = {math.gcd(2, odd_order)}",
    )


# ---------------------------------------------------------------------------
# T7. Cross-formula agreement: 2 checks
# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("T7: FINITE CROSS-FORMULA AGREEMENT")
print("=" * 72)
print(
    """
Agreement below is between two finite algebraic presentations: direct
inverse-determinant averaging and character-weighted averaging. It excludes
neither missing geometric hypotheses nor missing operator data.
"""
)

check(
    "(T7.1) direct L(1,2) equals the trivial-character weighted average",
    sp.simplify(density_12 - weighted_0) == 0,
    f"direct = {density_12}, weighted = {weighted_0}",
)
check(
    "(T7.2) exchanging the conjugate characters leaves L unchanged",
    sp.simplify(density_12 - density_21) == 0,
    f"L(1,2) = {density_12}, L(2,1) = {density_21}",
)


# ---------------------------------------------------------------------------
# T8. Representation sensitivity and core identity: 2 checks
# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("T8: REPRESENTATION SENSITIVITY")
print("=" * 72)
print(
    """
The values distinguish character pairs. This is evidence that the finite
functional depends on the declared local representation. It neither selects a
physical representation nor turns the number into a physical observable.
"""
)

density_22 = inverse_normal_determinant_average(2, 2)
check(
    "(T8.1) equal characters give 1/9 rather than 2/9",
    density_11 == density_22 == sp.Rational(1, 9)
    and density_11 != density_12,
    f"L(1,1) = {density_11}, L(2,2) = {density_22}, L(1,2) = {density_12}",
)

core_identity = sp.simplify((OMEGA - 1) * (OMEGA2 - 1))
check(
    "(T8.2) the conjugate-character denominator is exactly 3",
    core_identity == 3 and density_12 == sp.Rational(2, 9),
    f"denominator = {core_identity}, L(1,2) = {density_12}",
)


print("\n" + "=" * 72)
print(f"Summary: PASS={PASS}, FAIL={FAIL}")
print("=" * 72)

if FAIL == 0:
    print(
        f"""
All {PASS} finite checks passed.

Certified surface:
  - one real two-dimensional order-three normal-plane representation;
  - scalar symmetric commutant on that plane;
  - exact determinant factor 3;
  - defined inverse-normal-determinant average L(1,2) = 2/9;
  - exact finite character and integer arithmetic.

Not certified:
  - an operator eta or localization formula;
  - an isolated-point theorem in four real dimensions;
  - global metric independence;
  - PL/smooth or spin-lift statements;
  - physical representation selection, units, or readout.

The exclusions are proof boundaries, not impossibility results. A wider claim
requires new direct authority and a coherent fixed-set/operator geometry.
"""
    )
    sys.exit(0)

print(f"\n{FAIL} finite checks failed.")
sys.exit(1)
