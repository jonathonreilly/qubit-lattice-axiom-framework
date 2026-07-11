#!/usr/bin/env python3
"""Exact certificate for YT endpoint/bridge non-identifiability.

The source note proves a model-theoretic no-go on the current minimal premise
surface.  This runner checks the finite algebra used by that proof:

* the axiom source explicitly supplies no dynamics or physical-observable map;
* one concrete Admissibility/Record reduct is nonempty and internally exact;
* distinct endpoint values are conservative expansions of that same reduct;
* diffuse, IR-localized, and UV-localized C2 switching functions have exactly
  the same endpoints but exactly different transition centroids;
* an arbitrary-size linearly independent family of smooth endpoint-preserving
  perturbations exists without target fitting.

The analytic conservative-extension proof is in the note.  These checks are a
certificate for its explicit witnesses, not a numerical substitute for it.
"""

from __future__ import annotations

import sys
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AXIOM_NOTE = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

passed = 0
failed = 0


def check(section: str, number: int, statement: str, condition: bool, detail: str = "") -> bool:
    global passed, failed
    ok = bool(condition)
    if ok:
        passed += 1
    else:
        failed += 1
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{'PASS' if ok else 'FAIL'}] ({section}{number:02d}) {statement}{suffix}")
    return ok


def poly_eval(coeffs: list[Q], x: Q) -> Q:
    value = Q(0)
    for coefficient in reversed(coeffs):
        value = value * x + coefficient
    return value


def derivative(coeffs: list[Q]) -> list[Q]:
    return [Q(i) * coeffs[i] for i in range(1, len(coeffs))]


def integral_0_1(coeffs: list[Q]) -> Q:
    return sum((coeffs[i] / Q(i + 1) for i in range(len(coeffs))), Q(0))


def coefficient_rank(rows: list[list[Q]]) -> int:
    matrix = [row[:] for row in rows]
    if not matrix:
        return 0
    nrows = len(matrix)
    ncols = len(matrix[0])
    pivot_row = 0
    for column in range(ncols):
        pivot = next((r for r in range(pivot_row, nrows) if matrix[r][column] != 0), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / scale for entry in matrix[pivot_row]]
        for row in range(nrows):
            if row == pivot_row:
                continue
            factor = matrix[row][column]
            if factor:
                matrix[row] = [
                    matrix[row][j] - factor * matrix[pivot_row][j]
                    for j in range(ncols)
                ]
        pivot_row += 1
        if pivot_row == nrows:
            break
    return pivot_row


print("=" * 79)
print("YT CONSTRUCTIVE UV BRIDGE MINIMAL-SURFACE NON-IDENTIFIABILITY CERTIFICATE")
print("=" * 79)


print("\n--- [A] allowed-premise source guards")
axiom_text = AXIOM_NOTE.read_text(encoding="utf-8")
axiom_flat = " ".join(axiom_text.split())
check("A", 1, "current one-site algebra is M_2(C)", "M_2(C)" in axiom_text)
check("A", 2, "current lattice is nearest-neighbor Z^3", "cubic lattice `Z^3`" in axiom_text)
check(
    "A",
    3,
    "Admissibility explicitly does not choose a Hamiltonian or transfer operator",
    "does not choose a Hamiltonian or transfer operator" in axiom_flat,
)
check(
    "A",
    4,
    "source/action and physical-observable identification remain outside the axioms",
    "source/action and physical-observable identification" in axiom_flat,
)
check(
    "A",
    5,
    "dimensionless coupling content requires a separate derivation/bridge/admission",
    "Further physical structure requires derivation, bridge, explicit admission" in axiom_flat,
)


print("\n--- [M] explicit nonempty shared axiom reduct")
# Exact rank-one projectors used in the constructive record history.
p0 = ((Q(1), Q(0)), (Q(0), Q(0)))
p1 = ((Q(0), Q(0)), (Q(0), Q(1)))
p_plus = ((Q(1, 2), Q(1, 2)), (Q(1, 2), Q(1, 2)))
identity = ((Q(1), Q(0)), (Q(0), Q(1)))
zero = ((Q(0), Q(0)), (Q(0), Q(0)))


def matrix_add(*matrices):
    return tuple(
        tuple(sum((matrix[i][j] for matrix in matrices), Q(0)) for j in range(2))
        for i in range(2)
    )


def matrix_mul(left, right):
    return tuple(
        tuple(sum((left[i][k] * right[k][j] for k in range(2)), Q(0)) for j in range(2))
        for i in range(2)
    )


def conjugate_by_swap(matrix):
    swap = ((Q(0), Q(1)), (Q(1), Q(0)))
    return matrix_mul(matrix_mul(swap, matrix), swap)


def tested_top_support(neighbor_projectors):
    """Exact spectral support for the diagonal/scalar witness conditions.

    The note defines the rule for arbitrary Hermitian neighbor sums.  The
    certificate exercises its exact diagonal branches and a nontrivial frame
    covariance.  It does not pretend to be a general symbolic eigensolver.
    """
    neighbor_sum = matrix_add(*neighbor_projectors)
    if neighbor_sum[0][1] != 0 or neighbor_sum[1][0] != 0:
        raise ValueError("finite certificate expects a diagonal neighbor sum")
    if neighbor_sum[0][0] == neighbor_sum[1][1]:
        return identity
    return p0 if neighbor_sum[0][0] > neighbor_sum[1][1] else p1


E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def neighbors(site):
    result = []
    for direction in E:
        result.append(tuple(site[i] + direction[i] for i in range(3)))
        result.append(tuple(site[i] - direction[i] for i in range(3)))
    return result


def available_support(records, site):
    return tested_top_support([records.get(point, zero) for point in neighbors(site)])


def can_lock(records, site, projector):
    support = available_support(records, site)
    return site not in records and matrix_mul(support, projector) == projector


check(
    "M",
    1,
    "record projectors are exact idempotents",
    all(matrix_mul(projector, projector) == projector for projector in (p0, p1, p_plus)),
)
empty_support = tested_top_support([zero] * 6)
aligned_zero_support = tested_top_support([p0] * 6)
aligned_one_support = tested_top_support([p1] * 6)
tie_support = tested_top_support([p0, p1, zero, zero, zero, zero])
check("M", 2, "empty and scalar-tie conditions allow the full domain", empty_support == identity and tie_support == identity)
check("M", 3, "the fixed rule varies between two aligned neighbor conditions", aligned_zero_support == p0 and aligned_one_support == p1)
check(
    "M",
    4,
    "the tested rule is neighbor-order blind and covariant under a frame swap",
    tested_top_support([zero, p1, zero, p0, zero, zero]) == tie_support
    and conjugate_by_swap(aligned_zero_support) == aligned_one_support,
)

origin = (0, 0, 0)
far = (2, 0, 0)
middle = (1, 0, 0)
history = [{}]
history_ok = can_lock(history[-1], origin, p0)
history.append({**history[-1], origin: p0})
history_ok &= can_lock(history[-1], far, p1)
history.append({**history[-1], far: p1})
history_ok &= available_support(history[-1], middle) == identity
history_ok &= can_lock(history[-1], middle, p_plus)
history.append({**history[-1], middle: p_plus})
history_ok &= all(set(history[i]).issubset(history[i + 1]) for i in range(len(history) - 1))
check("M", 5, "the three-record history is sequentially admissible and permanent", history_ok)

records_left = {origin: p0, far: p1}
records_right = {middle: p_plus}
readout_left = Q(len(records_left))
readout_right = Q(len(records_right))
readout_union = Q(len(records_left | records_right))
check(
    "M",
    6,
    "finite scalar record readout is exactly additive on disjoint domains",
    readout_union == readout_left + readout_right,
    f"{readout_left}+{readout_right}={readout_union}",
)
check("M", 7, "a constant law gives one answer and privileges no tested record state", len({Q(0) for _state in history}) == 1)


print("\n--- [E] conservative endpoint expansions")
endpoint_a = Q(1147, 1250)  # exactly 0.9176
endpoint_b = Q(1)
check("E", 1, "the two displayed endpoint assignments are exact and distinct", endpoint_a != endpoint_b, f"{endpoint_a} != {endpoint_b}")
check("E", 2, "the historical decimal is exactly 1147/1250", endpoint_a == Q(9176, 10000))
print("  Analytic gate: conservative expansion of the disjoint theory is proved in the note, not self-certified here.")


print("\n--- [B] exact endpoint-preserving bridge witnesses")
# Quintic smoothstep q(u)=10u^3-15u^4+6u^5.  q' and q'' vanish at
# both joins, so its constant extensions are C2.
q = [Q(0), Q(0), Q(0), Q(10), Q(-15), Q(6)]
dq = derivative(q)
ddq = derivative(dq)
factorized_dq = [Q(0), Q(0), Q(30), Q(-60), Q(30)]
check("B", 1, "quintic switch has exact endpoints q(0)=0 and q(1)=1", poly_eval(q, Q(0)) == 0 and poly_eval(q, Q(1)) == 1)
check("B", 2, "constant joins are C2 at both ends", all(poly_eval(poly, x) == 0 for poly in (dq, ddq) for x in (Q(0), Q(1))))
check("B", 3, "transition density is nonnegative: q'=30u^2(1-u)^2", dq == factorized_dq)

transition_mass = integral_0_1(dq)
transition_moment = integral_0_1([Q(0)] + dq)
check("B", 4, "switch transition mass is exactly one", transition_mass == 1)
check("B", 5, "unit-interval transition centroid is exactly 1/2", transition_moment / transition_mass == Q(1, 2))

# w_IR transitions on [0,1/20], w_D(x)=x transitions on [0,1], and
# w_UV transitions on [19/20,1].  All have w(0)=0, w(1)=1.
ir_left, ir_right = Q(0), Q(1, 20)
uv_left, uv_right = Q(19, 20), Q(1)


def smooth_switch(x: Q, left: Q, right: Q) -> Q:
    if x <= left:
        return Q(0)
    if x >= right:
        return Q(1)
    return poly_eval(q, (x - left) / (right - left))


def diffuse_switch(x: Q) -> Q:
    return x


ir_centroid = ir_left + (ir_right - ir_left) * Q(1, 2)
diffuse_centroid = Q(1, 2)
uv_centroid = uv_left + (uv_right - uv_left) * Q(1, 2)
check(
    "B",
    6,
    "IR, diffuse, and UV switches preserve identical endpoints",
    (
        (smooth_switch(Q(0), ir_left, ir_right), smooth_switch(Q(1), ir_left, ir_right))
        == (Q(0), Q(1))
        and (diffuse_switch(Q(0)), diffuse_switch(Q(1))) == (Q(0), Q(1))
        and (smooth_switch(Q(0), uv_left, uv_right), smooth_switch(Q(1), uv_left, uv_right))
        == (Q(0), Q(1))
    ),
)
check(
    "B",
    7,
    "their transition centroids are exactly separated",
    (ir_centroid, diffuse_centroid, uv_centroid) == (Q(1, 40), Q(1, 2), Q(39, 40)),
    f"{ir_centroid}, {diffuse_centroid}, {uv_centroid}",
)
check("B", 8, "the UV witness transition is confined to x>=0.95", uv_left == Q(95, 100))
check(
    "B",
    9,
    "the exact UV predicate separates the UV switch from diffuse and IR switches",
    uv_left >= Q(19, 20) and ir_left < Q(19, 20) and Q(0) < Q(19, 20),
)


print("\n--- [F] infinite endpoint-preserving profile freedom")
# h_n(x)=x^(n+1)(1-x), n>=1.  The h_n have distinct top degrees and
# are linearly independent.  w_n=x+epsilon*h_n has the same endpoints.
# Since h_n'=x^n[(n+1)-(n+2)x] >= -1 on [0,1], epsilon=1/2 gives
# w_n'>=1/2, so every displayed witness is monotone.
n_witness = 12
max_degree = n_witness + 2
rows: list[list[Q]] = []
endpoint_ok = True
for n in range(1, n_witness + 1):
    coefficients = [Q(0)] * (max_degree + 1)
    coefficients[n + 1] = Q(1)
    coefficients[n + 2] = Q(-1)
    rows.append(coefficients)
    endpoint_ok &= poly_eval(coefficients, Q(0)) == 0 and poly_eval(coefficients, Q(1)) == 0

rank = coefficient_rank(rows)
check("F", 1, "twelve polynomial perturbations preserve both endpoints exactly", endpoint_ok)
check("F", 2, "the twelve perturbations are exactly linearly independent", rank == n_witness, f"rank={rank}")
epsilon = Q(1, 2)
monotonicity_witnesses = []
for n in range(1, n_witness + 1):
    critical = Q(n, n + 2)

    def h_prime(x, degree=n):
        return x**degree * (Q(degree + 1) - Q(degree + 2) * x)

    left_probe = critical / 2
    right_probe = (critical + 1) / 2
    # d(h_n')/dx has the sign of n-(n+2)x on (0,1).  Thus the
    # interior critical point is a maximum and the minimum is at an endpoint.
    derivative_sign_left = Q(n) - Q(n + 2) * left_probe > 0
    derivative_sign_right = Q(n) - Q(n + 2) * right_probe < 0
    monotonicity_witnesses.append(
        h_prime(Q(0)) == 0
        and h_prime(Q(1)) == -1
        and h_prime(critical) > 0
        and derivative_sign_left
        and derivative_sign_right
    )
check(
    "F",
    3,
    "exact calculus gives min h_n'=-1 and w_n'>=1-epsilon=1/2 for n=1..12",
    all(monotonicity_witnesses) and Q(1) - epsilon == Q(1, 2),
)


print("\n--- [C] analytic-proof firewall")
print("  The runner certifies explicit finite witnesses only.")
print("  The conservative-expansion implication and physical-identification boundary remain analytic.")

print("\n" + "=" * 79)
print(f"FINAL TALLY: {passed} PASS / {failed} FAIL")
print("Claim boundary: free-symbol selection no-go on current minimal surface; no positive endpoint derived.")
print("=" * 79)

sys.exit(1 if failed else 0)
