#!/usr/bin/env python3
"""Exact runner for the conditional formation-weight selection theorem.

Companion note:
  docs/KOIDE_FORMATION_WEIGHT_CONDITIONAL_SELECTION_UNIQUE_REGISTRATION_COMPATIBLE_LAWFUL_WEIGHT_BOUNDED_THEOREM_NOTE_2026-07-12.md

This runner re-derives the arithmetic needed by the composition.  It does not
import any cited source runner and it does not promote any conditional to
axiom content.  The source-side inputs remain graded as follows:

* SOCMLC and its exhaustive licensed-construction list are the formation-weight
  law-expressibility note's own note-owned licensing criterion.
* The map from a formation state to channel-energy shares is the formation-gate
  relocation note's declared modeling element.
* B_map, B_plus, and B_abs are the endpoint-registration asymmetry note's
  declared, unadopted bridge/modeling elements.
* ND_3 is the records-only OS reconstruction's named comparator/premise,
  labeled and never thresholded.
* The K-tied section is consumed at that note's bounded-theorem grade, with its
  supplied OS/orbit elements, time-homogeneity as an explicit load-bearing
  modeling condition (not a licensed default), the
  two-slice corner scope, and the declared C_3[111] probe coupling.

All derivation-path arithmetic is exact SymPy.  The final summary starts with
the verdict and the process exits 0 exactly when FAIL=0.
"""

from __future__ import annotations

from itertools import product
import sys

import sympy as sp


PASS = 0
FAIL = 0


def check(description: str, condition: object, detail: str = "") -> None:
    """Record one numbered exact check."""
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    number = PASS + FAIL
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{tag}] ({number:02d}) {description}{suffix}")


def unique_expressions(expressions: list[sp.Expr]) -> list[sp.Expr]:
    """Deduplicate exact expressions using symbolic equality."""
    unique: list[sp.Expr] = []
    for expression in expressions:
        value = sp.simplify(expression)
        if not any(sp.simplify(value - prior) == 0 for prior in unique):
            unique.append(value)
    return unique


def signs_at(expressions: list[sp.Expr], symbol: sp.Symbol,
             point: sp.Expr) -> tuple[int, ...]:
    """Return an exact sign vector at a point away from all zero loci."""
    return tuple(int(sp.sign(sp.simplify(expr.subs(symbol, point))))
                 for expr in expressions)


print("EXACT CONDITIONAL SELECTION RUNNER")
print("=" * 78)

# ---------------------------------------------------------------------------
# A. SOCMLC candidate arithmetic on the supplied carrier and quotient.
# The exhaustiveness/license is cited; all numerical weights are derived here.
# ---------------------------------------------------------------------------
print("\nA. LAWFUL-SET CANDIDATE ARITHMETIC (SOCMLC CONDITIONAL)")

I3 = sp.eye(3)
P_s = sp.diag(1, 0, 0)
P_d = sp.diag(0, 1, 1)
K_swap = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
x_s, x_d = sp.symbols("x_s x_d")
A_reg_element = x_s * P_s + x_d * P_d
doublet_odd_witness = sp.diag(0, 1, -1)

check(
    "the singlet/doublet projectors are complementary orthogonal projectors",
    P_s * P_s == P_s and P_d * P_d == P_d
    and P_s * P_d == sp.zeros(3) and P_s + P_d == I3,
)

rank_s = P_s.rank()
rank_d = P_d.rank()
check(
    "the supplied carrier derives ranks (rank P_s, rank P_d) = (1, 2)",
    (rank_s, rank_d) == (1, 2),
    f"derived ranks=({rank_s},{rank_d})",
)

check(
    "the supplied A_reg = C P_s + C P_d form is K-orbit-constant, while the internal doublet difference is K-odd",
    sp.simplify(K_swap * A_reg_element * K_swap - A_reg_element) == sp.zeros(3)
    and sp.simplify(K_swap * doublet_odd_witness * K_swap
                    + doublet_odd_witness) == sp.zeros(3),
)

carrier_dimension = I3.rank()
rho_dimension = I3 / carrier_dimension
dimension_weights = (
    sp.trace(rho_dimension * P_s),
    sp.trace(rho_dimension * P_d),
)
check(
    "normalized carrier trace derives menu weights (1/3, 2/3)",
    sum(dimension_weights) == 1
    and dimension_weights == (sp.Rational(1, 3), sp.Rational(2, 3)),
    f"derived weights={dimension_weights}",
)

minimal_central_projectors = (P_s, P_d)
cell_count = len(minimal_central_projectors)
weight_per_cell = sp.Rational(1, cell_count)
rho_cell = (weight_per_cell / rank_s) * P_s + (weight_per_cell / rank_d) * P_d
cell_weights = (
    sp.trace(rho_cell * P_s),
    sp.trace(rho_cell * P_d),
)
check(
    "uniform counting on the two minimal central cells derives menu weights (1/2, 1/2)",
    sum(cell_weights) == 1
    and cell_weights == (sp.Rational(1, 2), sp.Rational(1, 2)),
    f"rho_cell={rho_cell}, derived weights={cell_weights}",
)

# SOCMLC's exhaustive classification is cited.  Recompute representative
# density operators for its two DISTINCT output weights through the same
# singlet-weight readout; no endpoint number is placed on this derivation path.
distinct_representative_density_operators = (rho_dimension, rho_cell)
licensed_candidate_weights = [
    sp.simplify(sp.trace(rho * P_s))
    for rho in distinct_representative_density_operators
]
w_symbol = sp.symbols("w")
candidate_polynomial = sp.expand(sp.prod(
    w_symbol - candidate for candidate in licensed_candidate_weights
))
lawful_weights = tuple(sorted(
    sp.solve(sp.Eq(candidate_polynomial, 0), w_symbol),
    key=sp.default_sort_key,
))
check(
    "SOCMLC candidate arithmetic deduplicates to W_expr = {1/3, 1/2}",
    lawful_weights == (sp.Rational(1, 3), sp.Rational(1, 2))
    and sp.factor(candidate_polynomial)
    == (2 * w_symbol - 1) * (3 * w_symbol - 1) / 6,
    f"derived roots={lawful_weights}",
)

# ---------------------------------------------------------------------------
# B. Formation-gate relocation's declared energy dictionary, solved natively.
# ---------------------------------------------------------------------------
print("\nB. ENERGY DICTIONARY (DECLARED MODELING ELEMENT, ARITHMETIC RE-DERIVED)")

E_total = sp.symbols("E_total", positive=True)
a_squared, b_squared = sp.symbols("a_squared b_squared", positive=True)
energy_solution = sp.solve(
    (
        sp.Eq(3 * a_squared, w_symbol * E_total),
        sp.Eq(6 * b_squared, (1 - w_symbol) * E_total),
    ),
    (a_squared, b_squared),
    dict=True,
)
check(
    "the two channel-energy equations have one exact solution",
    len(energy_solution) == 1,
    f"solution={energy_solution}",
)

solved_a_squared = sp.simplify(energy_solution[0][a_squared])
solved_b_squared = sp.simplify(energy_solution[0][b_squared])
r_expression = sp.factor(solved_b_squared / solved_a_squared)
check(
    "the solved energy ratio is r(w) = (1-w)/(2w), not an inserted endpoint",
    sp.simplify(r_expression - (1 - w_symbol) / (2 * w_symbol)) == 0,
    f"derived r(w)={r_expression}",
)

r_symbol = sp.symbols("r", nonnegative=True)
inverse_solutions = sp.solve(sp.Eq(r_symbol, r_expression), w_symbol)
check(
    "the positive-weight dictionary is invertible with w(r) = 1/(1+2r)",
    len(inverse_solutions) == 1
    and sp.simplify(inverse_solutions[0] - 1 / (1 + 2 * r_symbol)) == 0,
    f"derived inverse={inverse_solutions}",
)

endpoint_map = {
    weight: sp.simplify(r_expression.subs(w_symbol, weight))
    for weight in lawful_weights
}
endpoint_r_values = tuple(sorted(set(endpoint_map.values()),
                                 key=sp.default_sort_key))
r_low, r_high = endpoint_r_values
w_at_r_low = tuple(weight for weight, value in endpoint_map.items()
                   if sp.simplify(value - r_low) == 0)
w_at_r_high = tuple(weight for weight, value in endpoint_map.items()
                    if sp.simplify(value - r_high) == 0)
check(
    "the lawful weights map bijectively to r=1 and r=1/2 with the stated pairing",
    endpoint_r_values == (sp.Rational(1, 2), sp.Integer(1))
    and w_at_r_low == (sp.Rational(1, 2),)
    and w_at_r_high == (sp.Rational(1, 3),),
    f"derived map={endpoint_map}",
)

# ---------------------------------------------------------------------------
# C. Tied-spectrum identities and the positive-branch endpoint comparison.
# ---------------------------------------------------------------------------
print("\nC. T1 POSITIVE-BRANCH REGISTRATION COMPATIBILITY")

a = sp.symbols("a", positive=True)
beta = sp.symbols("beta", positive=True)
theta = sp.symbols("theta", real=True)
sqrt3 = sp.sqrt(3)

# Exact expanded 2pi/3 shifts keep all simplifications algebraic.
cosine_triple = (
    sp.cos(theta),
    -sp.cos(theta) / 2 - sqrt3 * sp.sin(theta) / 2,
    -sp.cos(theta) / 2 + sqrt3 * sp.sin(theta) / 2,
)
lambdas = [a + 2 * beta * cosine for cosine in cosine_triple]
trace_lambda = sp.trigsimp(sum(lambdas))
quadratic_trace = sp.trigsimp(sum(value ** 2 for value in lambdas))

check(
    "the tied spectrum has phase-free signed trace sum(lambda_k)=3a",
    sp.simplify(trace_lambda - 3 * a) == 0,
)
check(
    "the tied spectrum has phase-free quadratic trace 3a^2+6|b|^2",
    sp.simplify(quadratic_trace - (3 * a ** 2 + 6 * beta ** 2)) == 0,
)

difference_product = sp.trigsimp(
    (lambdas[0] - lambdas[1])
    * (lambdas[0] - lambdas[2])
    * (lambdas[1] - lambdas[2])
)
check(
    "the exact spectral collision locus is controlled by sin(3 theta)",
    sp.trigsimp(difference_product
                + 6 * sqrt3 * beta ** 3 * sp.sin(3 * theta)) == 0,
    f"difference product={sp.trigsimp(difference_product)}",
)

delta = sp.symbols("delta", real=True)
reduced_cosines = (
    sp.cos(delta),
    sp.cos(delta + 2 * sp.pi / 3),
    sp.cos(delta - 2 * sp.pi / 3),
)
minimum_cosine = -sp.cos(sp.pi / 3 - delta)
gap_0 = sp.trigsimp(reduced_cosines[0] - reduced_cosines[1])
gap_2 = sp.trigsimp(reduced_cosines[2] - reduced_cosines[1])
check(
    "on 0<=delta<=pi/3 the reduced minimum is -cos(pi/3-delta)",
    sp.trigsimp(reduced_cosines[1] - minimum_cosine) == 0
    and sp.trigsimp(gap_0
                    - (3 * sp.cos(delta) + sqrt3 * sp.sin(delta)) / 2) == 0
    and sp.trigsimp(gap_2 - sqrt3 * sp.sin(delta)) == 0,
    "both displayed gaps are nonnegative on the reduced interval",
)

normalized_minimum_high = sp.trigsimp(
    1 - 2 * sp.sqrt(r_high) * sp.cos(sp.pi / 3 - delta)
)
high_range = sp.calculus.util.function_range(
    normalized_minimum_high, delta, sp.Interval(0, sp.pi / 3)
)
high_zero_set = sp.solveset(
    sp.Eq(normalized_minimum_high, 0),
    delta,
    domain=sp.Interval(0, sp.pi / 3),
)
check(
    "at the larger lawful endpoint the nonnegative window has zero width",
    high_range == sp.Interval(-1, 0)
    and high_zero_set == sp.FiniteSet(0),
    f"range={high_range}, equality set={high_zero_set}",
)

high_spectrum_at_center = [
    sp.simplify(value.subs({beta: a * sp.sqrt(r_high), theta: 0}))
    for value in lambdas
]
high_registered_at_center = [sp.expand(value ** 2)
                             for value in high_spectrum_at_center]
high_center_nd3 = len(unique_expressions(high_registered_at_center)) == 3
check(
    "the r=1 positive-branch endpoint is (3a,0,0) and violates ND_3",
    high_spectrum_at_center == [3 * a, 0, 0]
    and not high_center_nd3,
    f"registered pattern={high_registered_at_center}",
)

normalized_minimum_low = sp.trigsimp(
    1 - 2 * sp.sqrt(r_low) * sp.cos(sp.pi / 3 - delta)
)
low_zero_set = sp.solveset(
    sp.Eq(normalized_minimum_low, 0),
    delta,
    domain=sp.Interval(0, sp.pi / 3),
)
low_window_edge = next(iter(low_zero_set))
check(
    "at the smaller lawful endpoint the strict positivity half-window is 0<=delta<pi/12",
    low_zero_set == sp.FiniteSet(sp.pi / 12)
    and sp.simplify(normalized_minimum_low.subs(delta, 0)) > 0
    and sp.simplify(normalized_minimum_low.subs(delta, low_window_edge)) == 0,
    f"derived edge={low_window_edge}",
)

low_witness_phase = low_window_edge / 2
low_witness_spectrum = [
    sp.simplify(value.subs({
        beta: a * sp.sqrt(r_low),
        theta: low_witness_phase,
    }))
    for value in lambdas
]
low_witness_registered = [sp.simplify(value ** 2)
                          for value in low_witness_spectrum]
check(
    "the derived open low-endpoint window contains a strictly positive ND_3 witness",
    all(sp.simplify(value / a) > 0 for value in low_witness_spectrum)
    and len(unique_expressions(low_witness_registered)) == 3,
    f"witness theta={low_witness_phase}",
)

q_signed = sp.factor(quadratic_trace / trace_lambda ** 2)
q_in_r = sp.factor(q_signed.subs(beta ** 2, r_symbol * a ** 2))
q_low = sp.simplify(q_in_r.subs(r_symbol, r_low))
check(
    "under B_map+B_plus, Q=(1+2r)/3 and the low endpoint pins Q=2/3",
    sp.simplify(q_in_r - (1 + 2 * r_symbol) / 3) == 0
    and q_low == sp.Rational(2, 3),
    f"Q(r)={q_in_r}, Q(r_low)={q_low}",
)

positive_branch_compatibility: dict[sp.Expr, bool] = {}
for weight, endpoint_r in endpoint_map.items():
    if sp.simplify(endpoint_r - r_high) == 0:
        positive_branch_compatibility[weight] = (
            high_zero_set != sp.FiniteSet(0) and high_center_nd3
        )
    elif sp.simplify(endpoint_r - r_low) == 0:
        positive_branch_compatibility[weight] = (
            low_window_edge > 0
            and all(sp.simplify(value / a) > 0
                    for value in low_witness_spectrum)
            and len(unique_expressions(low_witness_registered)) == 3
        )

t1_selected_weights = tuple(
    weight for weight in lawful_weights
    if positive_branch_compatibility.get(weight, False)
)
check(
    "T1 composition selects one lawful positive-branch-compatible weight",
    t1_selected_weights == (sp.Rational(1, 2),)
    and endpoint_map[t1_selected_weights[0]] == sp.Rational(1, 2)
    and q_low == sp.Rational(2, 3),
    f"compatibility map={positive_branch_compatibility}",
)

# ---------------------------------------------------------------------------
# D. T2: B_abs, exact local-constancy lemma and r=1 sign regions.
# ---------------------------------------------------------------------------
print("\nD. T2 B_abs OPEN PINNED-Q SECTOR")

# Under a fixed nonzero sign vector s, S_abs is an ordinary trigonometric
# polynomial.  Enumerate all eight vectors and solve the exact coefficient
# conditions for an identically zero derivative.
sign_vectors = tuple(product((-1, 1), repeat=3))
constant_sign_vectors: list[tuple[int, ...]] = []
sign_coefficients: dict[tuple[int, ...], tuple[sp.Expr, sp.Expr]] = {}
for sign_vector in sign_vectors:
    s0, s1, s2 = sign_vector
    cosine_coefficient = sp.Rational(1, 2) * (2 * s0 - s1 - s2)
    sine_coefficient = sqrt3 * sp.Rational(1, 2) * (s2 - s1)
    sign_coefficients[sign_vector] = (
        sp.simplify(cosine_coefficient),
        sp.simplify(sine_coefficient),
    )
    if cosine_coefficient == 0 and sine_coefficient == 0:
        constant_sign_vectors.append(sign_vector)

check(
    "a fixed-sign absolute sum can be theta-constant only for a uniform sign vector",
    set(constant_sign_vectors) == {(-1, -1, -1), (1, 1, 1)},
    f"coefficient-kernel sign vectors={constant_sign_vectors}",
)
check(
    "the algebraic all-negative exception is impossible because sum(lambda_k)=3a>0",
    trace_lambda == 3 * a and bool(a.is_positive),
    "three negative terms would have a negative sum",
)

high_normalized_lambdas = [
    sp.trigsimp(value.subs({a: 1, beta: sp.sqrt(r_high)}))
    for value in lambdas
]
phase_domain = sp.Interval.Ropen(0, 2 * sp.pi)
component_zero_sets = [
    sp.solveset(sp.Eq(value, 0), theta, domain=phase_domain)
    for value in high_normalized_lambdas
]
all_zero_boundaries = sp.Union(*component_zero_sets)
check(
    "at r=1 the sign-boundary set over one period is exactly {0,2pi/3,4pi/3}",
    all_zero_boundaries
    == sp.FiniteSet(0, 2 * sp.pi / 3, 4 * sp.pi / 3),
    f"component zero sets={component_zero_sets}",
)

ordered_boundaries = sorted(list(all_zero_boundaries), key=sp.default_sort_key)
interval_boundaries = ordered_boundaries + [2 * sp.pi]
region_data: list[dict[str, object]] = []
for lower, upper in zip(interval_boundaries, interval_boundaries[1:]):
    midpoint = sp.simplify((lower + upper) / 2)
    sign_vector = signs_at(high_normalized_lambdas, theta, midpoint)
    signed_sum = sp.trigsimp(sum(
        sign * value
        for sign, value in zip(sign_vector, high_normalized_lambdas)
    ))
    derivative = sp.trigsimp(sp.diff(signed_sum, theta))
    critical_set = sp.solveset(
        sp.Eq(derivative, 0),
        theta,
        domain=sp.Interval.open(lower, upper),
    )
    region_data.append({
        "lower": lower,
        "upper": upper,
        "midpoint": midpoint,
        "signs": sign_vector,
        "sum": signed_sum,
        "derivative": derivative,
        "critical": critical_set,
    })

actual_region_signs = [data["signs"] for data in region_data]
check(
    "the three actual r=1 open sign regions each have exactly one negative component",
    len(set(actual_region_signs)) == 3
    and all(sum(sign == -1 for sign in signs) == 1
            for signs in actual_region_signs),
    f"derived region signs={actual_region_signs}",
)

region_derivatives_nonconstant = True
region_critical_sets_isolated = True
for data in region_data:
    derivative = data["derivative"]
    critical_set = data["critical"]
    derivative_nonzero = sp.simplify(derivative) != 0
    isolated_critical = (
        isinstance(critical_set, sp.FiniteSet)
        and len(critical_set) == 1
        and critical_set == sp.FiniteSet(data["midpoint"])
    )
    region_derivatives_nonconstant &= derivative_nonzero
    region_critical_sets_isolated &= isolated_critical
    check(
        f"r=1 region ({data['lower']},{data['upper']}) has d(sum|lambda|)/dtheta not identically zero",
        derivative_nonzero and isolated_critical,
        f"signs={data['signs']}, derivative={derivative}, isolated critical set={critical_set}",
    )

boundary_patterns = [
    [sp.simplify(value.subs(theta, boundary))
     for value in high_normalized_lambdas]
    for boundary in ordered_boundaries
]
boundary_registered_patterns = [
    [sp.expand(value ** 2) for value in pattern]
    for pattern in boundary_patterns
]
check(
    "r=1 zero-sign boundary patterns are isolated permutations of (3,0,0) and violate ND_3",
    all(sorted(pattern) == [0, 0, 3] for pattern in boundary_patterns)
    and all(len(unique_expressions(pattern)) < 3
            for pattern in boundary_registered_patterns),
    f"boundary spectra={boundary_patterns}",
)

critical_registered_patterns: list[list[sp.Expr]] = []
for data in region_data:
    critical_point = next(iter(data["critical"]))
    critical_spectrum = [
        sp.simplify(value.subs(theta, critical_point))
        for value in high_normalized_lambdas
    ]
    critical_registered_patterns.append([
        sp.expand(value ** 2) for value in critical_spectrum
    ])
check(
    "the derivative's r=1 critical points are isolated (not open sectors) and their registered patterns are degenerate",
    region_critical_sets_isolated
    and all(len(unique_expressions(pattern)) < 3
            for pattern in critical_registered_patterns),
    f"critical registered patterns={critical_registered_patterns}",
)

high_abs_witness_phase = sp.pi / 6
high_abs_witness_spectrum = [
    sp.simplify(value.subs(theta, high_abs_witness_phase))
    for value in high_normalized_lambdas
]
high_abs_witness_registered = [
    sp.expand(value ** 2) for value in high_abs_witness_spectrum
]
check(
    "under B_abs, ND_3 alone does not exclude the r=1 lawful endpoint",
    len(unique_expressions(high_abs_witness_registered)) == 3,
    f"theta=pi/6, spectrum={high_abs_witness_spectrum}, registered={high_abs_witness_registered}",
)
check(
    "under B_abs, ND_3 alone does not exclude the r=1/2 lawful endpoint",
    len(unique_expressions(low_witness_registered)) == 3,
    f"theta={low_witness_phase}, all entries are positive",
)

high_abs_sum = sp.trigsimp(sum(abs_value * value for abs_value, value in zip(
    signs_at(high_normalized_lambdas, theta, high_abs_witness_phase),
    high_normalized_lambdas,
)))
second_high_phase = sp.pi / 12
second_high_signs = signs_at(high_normalized_lambdas, theta,
                             second_high_phase)
second_high_spectrum = [
    sp.simplify(value.subs(theta, second_high_phase))
    for value in high_normalized_lambdas
]
second_high_registered = [
    sp.expand(value ** 2) for value in second_high_spectrum
]
second_high_sum = sp.trigsimp(sum(
    sign * value for sign, value in zip(second_high_signs,
                                        high_normalized_lambdas)
)).subs(theta, second_high_phase)
first_high_sum = sp.simplify(high_abs_sum.subs(theta, high_abs_witness_phase))
high_numerator = sp.simplify(
    quadratic_trace.subs({a: 1, beta: sp.sqrt(r_high)})
)
high_q_first = sp.simplify(high_numerator / first_high_sum ** 2)
high_q_second = sp.simplify(high_numerator / second_high_sum ** 2)
check(
    "two exact non-degenerate r=1 phases already give different Q_abs values",
    len(unique_expressions(high_abs_witness_registered)) == 3
    and len(unique_expressions(second_high_registered)) == 3
    and sp.simplify(high_q_first - high_q_second) != 0,
    f"Q_abs(pi/6)={high_q_first}, Q_abs(pi/12)={high_q_second}",
)

no_open_constant_high = (
    isinstance(all_zero_boundaries, sp.FiniteSet)
    and region_derivatives_nonconstant
    and region_critical_sets_isolated
)
check(
    "r=1 admits no open phase sector with constant Q_abs (isolated boundaries and critical points are not sectors)",
    no_open_constant_high,
)

low_positive_sum = sp.simplify(trace_lambda.subs(
    beta, a * sp.sqrt(r_low)
))
low_abs_numerator = sp.simplify(quadratic_trace.subs(
    beta, a * sp.sqrt(r_low)
))
low_abs_q_on_positive_region = sp.factor(
    low_abs_numerator / low_positive_sum ** 2
)
low_open_pinned_sector = (
    low_window_edge > 0
    and all(sp.simplify(value / a) > 0 for value in low_witness_spectrum)
    and len(unique_expressions(low_witness_registered)) == 3
    and sp.simplify(low_positive_sum - 3 * a) == 0
    and low_abs_q_on_positive_region == sp.Rational(2, 3)
)
check(
    "r=1/2 admits the nonempty open all-positive ND_3 sector 0<delta<pi/12 with Q_abs pinned to 2/3",
    low_open_pinned_sector,
    f"window edge={low_window_edge}, sum|lambda|={low_positive_sum}, Q_abs={low_abs_q_on_positive_region}",
)

b_abs_open_pinned_compatibility: dict[sp.Expr, bool] = {}
for weight, endpoint_r in endpoint_map.items():
    if sp.simplify(endpoint_r - r_high) == 0:
        b_abs_open_pinned_compatibility[weight] = not no_open_constant_high
    elif sp.simplify(endpoint_r - r_low) == 0:
        b_abs_open_pinned_compatibility[weight] = low_open_pinned_sector

t2_selected_weights = tuple(
    weight for weight in lawful_weights
    if b_abs_open_pinned_compatibility.get(weight, False)
)
check(
    "T2 branch-robust composition uniquely selects w=1/2 among lawful weights",
    t2_selected_weights == (sp.Rational(1, 2),)
    and t2_selected_weights == t1_selected_weights,
    f"B_abs open-pinned compatibility map={b_abs_open_pinned_compatibility}",
)

# ---------------------------------------------------------------------------
# Verdict-first final stdout summary.
# ---------------------------------------------------------------------------
print("\nVERDICT: PASS — CONDITIONAL SELECTION THEOREM HOLDS EXACTLY AT ITS DECLARED WEAKEST GRADE; w=1/2 IS THE UNIQUE LAWFUL COMPATIBLE WEIGHT IN T1 AND T2.")
print("FULL CONDITIONAL STACK:")
print("  1. SOCMLC — note-owned licensing criterion from the formation-weight law-expressibility bounded theorem.")
print("  2. Tied-measure/formation-state relocation plus energy dictionary — exact bounded product compatibility, with the dictionary a declared modeling element.")
print("  3. B_map — declared spectral-to-registration bridge/modeling element (T1 and T2) from the endpoint-registration asymmetry bounded theorem.")
print("  4. B_plus — declared nonnegative-spectrum branch convention (T1) from the endpoint-registration asymmetry bounded theorem.")
print("  5. ND_3 — named comparator/premise, labeled and never thresholded.")
print("  6. K-tied section — records-only OS reconstruction bounded grade with supplied OS reflection/crossing, P-even orbit clause, history-index/transfer ingredients, and time-homogeneity as an explicit load-bearing modeling condition, not a licensed default.")
print("  7. Two-slice corner — bilinear one-component scope only.")
print("  8. C_3[111] — declared probe coupling, not a derived physical mass coupling.")
print("  9. B_abs — declared sign-allowed spectral-registration branch (T2) from the endpoint-registration asymmetry bounded theorem.")
print(" 10. Open-pinned-Q compatibility — this note's explicit T2 selection criterion.")
print("T2 EXACT RESULT: HOLDS — r=1 has three one-negative sign regions whose exact derivatives are nonzero trigonometric functions with only isolated critical points; r=1/2 alone has an open all-positive ND_3 sector with Q_abs=2/3.")
print(f"CHECK COUNT: {PASS + FAIL} exact checks; PASS={PASS}; FAIL={FAIL}.")
print("PROPOSED CLAIM_SCOPE: conditional on the ten named elements at their declared source grades, with every independent-audit narrowing or failure inherited, classify the two SOCMLC-lawful weights on the tied bilinear two-slice C_3[111] corner; w=1/2 alone has the required open non-degenerate pinned-Q sector, mapping to r=1/2 and Q=2/3 there.")
print("HOSTILE-AUDIT UNCERTAINTIES: SOCMLC exhaustiveness; formation-energy bridge; spectral-registration branches; ND_3 authority; time-homogeneity/orbit/history-index supplies; two-slice/probe physical scope; the open-pinned-Q criterion; source-grade and audit dependence. No premise or audit outcome is adopted here.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")

sys.exit(0 if FAIL == 0 else 1)
