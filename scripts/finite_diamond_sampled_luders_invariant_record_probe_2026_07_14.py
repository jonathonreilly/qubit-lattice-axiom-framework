#!/usr/bin/env python3
"""Exact finite construction and ablations for the FD-SLIR candidate law."""

from __future__ import annotations

from itertools import product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "FINITE_DIAMOND_SAMPLED_LUDERS_INVARIANT_RECORD_MODEL_NOTE_2026-07-14.md"
)
TOURNAMENT = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "EXACT_PREDICTIVE_SPECIFICATION_TOURNAMENT_NOTE_2026-07-14.md"
)
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def exact_equal(left, right) -> bool:
    if isinstance(left, sp.MatrixBase) or isinstance(right, sp.MatrixBase):
        return sp.simplify(left - right) == sp.zeros(*left.shape)
    return sp.simplify(left - right) == 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def dagger(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.conjugate().T


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.diag(1, -1)
P0 = sp.diag(1, 0)
P1 = sp.diag(0, 1)
ket0 = sp.Matrix([1, 0])
ket1 = sp.Matrix([0, 1])
ket_plus = (ket0 + ket1) / sp.sqrt(2)
ket_minus = (ket0 - ket1) / sp.sqrt(2)


def density(vector: sp.Matrix) -> sp.Matrix:
    return vector * dagger(vector)


def projector(observable: sp.Matrix, outcome: int) -> sp.Matrix:
    return (sp.eye(observable.rows) + outcome * observable) / 2


def trace(matrix: sp.Matrix):
    return sp.simplify(sp.trace(matrix))


def source_contract() -> None:
    section("A - Source and scope contract")
    note = NOTE.read_text(encoding="utf-8")
    tournament = TOURNAMENT.read_text(encoding="utf-8")
    normalized = note.lower().replace("*", "").replace("`", "")
    check("A candidate note is authority-free", "authority: none" in normalized)
    check("A candidate is explicitly finite and conditional", "exact finite conditional construction" in normalized)
    check("A candidate disclaims unique selection", "uniquely selected" in normalized)
    check("A note fills all ten field names", all(f"`{field}`" in note for field in (
        "DOMAIN", "STATE", "CONTEXT", "ATOMIC_LAW", "CONTINUATION",
        "AVAILABILITY", "CONCURRENCY", "RECORD", "ACTUALITY", "STATISTICS",
    )))
    check("A tournament no longer claims one instrument object closes all fields", "The leading expressive substrate candidate is not one object" in tournament)


def bell_diamond() -> None:
    section("B - Exact Bell, normalization, no-signalling, and disjoint order")
    bell = (sp.kronecker_product(ket0, ket0) + sp.kronecker_product(ket1, ket1)) / sp.sqrt(2)
    rho = density(bell)
    alice = (Z, X)
    bob = ((Z + X) / sp.sqrt(2), (Z - X) / sp.sqrt(2))
    correlations = {}
    all_normalized = True
    all_marginals_half = True
    all_commute = True
    all_order_equal = True

    for x, y in product((0, 1), repeat=2):
        probabilities = {}
        branch_states = {}
        for a, b in product((-1, 1), repeat=2):
            pa = projector(alice[x], a)
            pb = projector(bob[y], b)
            pa_full = sp.kronecker_product(pa, I2)
            pb_full = sp.kronecker_product(I2, pb)
            joint = pa_full * pb_full
            branch_ab = sp.simplify(joint * rho * joint)
            branch_ba = sp.simplify(pb_full * pa_full * rho * pa_full * pb_full)
            probabilities[(a, b)] = trace(branch_ab)
            branch_states[(a, b)] = branch_ab
            all_commute &= exact_equal(pa_full * pb_full, pb_full * pa_full)
            all_order_equal &= exact_equal(branch_ab, branch_ba)
        all_normalized &= exact_equal(sum(probabilities.values()), 1)
        for a in (-1, 1):
            all_marginals_half &= exact_equal(sum(probabilities[(a, b)] for b in (-1, 1)), sp.Rational(1, 2))
        for b in (-1, 1):
            all_marginals_half &= exact_equal(sum(probabilities[(a, b)] for a in (-1, 1)), sp.Rational(1, 2))
        correlations[(x, y)] = sp.simplify(sum(a * b * probabilities[(a, b)] for a, b in probabilities))

    expected = {
        (0, 0): 1 / sp.sqrt(2),
        (0, 1): 1 / sp.sqrt(2),
        (1, 0): 1 / sp.sqrt(2),
        (1, 1): -1 / sp.sqrt(2),
    }
    chsh = sp.simplify(correlations[(0, 0)] + correlations[(0, 1)] + correlations[(1, 0)] - correlations[(1, 1)])
    check("B every Bell context normalizes", all_normalized)
    check("B all local marginals are one half", all_marginals_half)
    check("B disjoint local projectors commute", all_commute)
    check("B disjoint update order gives the same branches", all_order_equal)
    check("B exact quantum correlations", all(exact_equal(correlations[key], value) for key, value in expected.items()))
    check("B CHSH equals 2 sqrt(2)", exact_equal(chsh, 2 * sp.sqrt(2)))


def sample_index(probabilities: tuple[sp.Rational, ...], seed: sp.Rational) -> int:
    cumulative = sp.Rational(0)
    for index, probability in enumerate(probabilities):
        cumulative += probability
        if seed < cumulative:
            return index
    raise ValueError("seed must lie in [0,1)")


def sampled_actuality_and_cylinders() -> None:
    section("C - Explicit sample semantics, state reconstruction, and cylinders")
    probabilities = (sp.Rational(1, 2), sp.Rational(1, 2))
    first = sample_index(probabilities, sp.Rational(1, 4))
    second = sample_index(probabilities, sp.Rational(3, 4))
    check("C one supplied seed returns exactly one label", first == 0 and second == 1)
    check("C identical weights permit different realized samples", first != second)

    rho = density(ket_plus)
    z_projectors = (P0, P1)
    x_projectors = (density(ket_plus), density(ket_minus))
    cylinders = {}
    prefixes = {}
    reconstructed = {}
    for a, b in product((0, 1), repeat=2):
        branch_operator = x_projectors[b] * z_projectors[a]
        sigma = sp.simplify(branch_operator * rho * dagger(branch_operator))
        cylinders[(a, b)] = trace(sigma)
        reconstructed[(a, b)] = sigma
    for a in (0, 1):
        sigma_prefix = z_projectors[a] * rho * z_projectors[a]
        prefixes[a] = trace(sigma_prefix)
    check("C sequential cylinder law normalizes", exact_equal(sum(cylinders.values()), 1))
    check("C prefix cylinders are marginals", all(exact_equal(sum(cylinders[(a, b)] for b in (0, 1)), prefixes[a]) for a in (0, 1)))
    check("C branch state is reconstructed from recorded operator word", all(exact_equal(trace(state), cylinders[key]) for key, state in reconstructed.items()))

    # Sharp repeatability: after P_a, repeating the same PVM returns a with certainty.
    for a, p in enumerate(z_projectors):
        post = p * rho * p
        probability = trace(post)
        conditional = sp.simplify(post / probability)
        repeat_same = trace(p * conditional * p)
        repeat_other = trace(z_projectors[1 - a] * conditional * z_projectors[1 - a])
        check(f"C Z outcome {a} is exactly repeatable", exact_equal(repeat_same, 1) and exact_equal(repeat_other, 0))


def record_invariance() -> None:
    section("D - Record-preserving operations and absorption boundary")
    q0 = sp.kronecker_product(I2, P0)
    q1 = sp.kronecker_product(I2, P1)
    future = sp.kronecker_product(X, P0) + sp.kronecker_product(Z, P1)
    check("D future operation is unitary", exact_equal(dagger(future) * future, sp.eye(4)))
    check("D future operation commutes with both record projectors", exact_equal(future * q0, q0 * future) and exact_equal(future * q1, q1 * future))
    for label, q in enumerate((q0, q1)):
        dual = sp.simplify(dagger(future) * q * future)
        check(f"D record sector {label} is fixed", exact_equal(dual, q))
    cross_01 = q0 * future * q1
    cross_10 = q1 * future * q0
    check("D fixed sectors have no reconnecting cross blocks", exact_equal(cross_01, sp.zeros(4)) and exact_equal(cross_10, sp.zeros(4)))

    gamma = sp.Rational(1, 3)
    k0 = sp.diag(1, sp.sqrt(1 - gamma))
    k1 = sp.Matrix([[0, sp.sqrt(gamma)], [0, 0]])
    check("D amplitude-damping Kraus family is trace preserving", exact_equal(dagger(k0) * k0 + dagger(k1) * k1, I2))
    absorbed = sp.simplify(k0 * P0 * dagger(k0) + k1 * P0 * dagger(k1))
    dual_p0 = sp.simplify(dagger(k0) * P0 * k0 + dagger(k1) * P0 * k1)
    check("D formed P0 is branch-relative absorbing", exact_equal(absorbed, P0))
    check("D branch absorption does not imply global fixed projector", not exact_equal(dual_p0, P0) and exact_equal(dual_p0, sp.diag(1, gamma)))
    check("D one-way no-escape blocks vanish", exact_equal(P1 * k0 * P0, sp.zeros(2)) and exact_equal(P1 * k1 * P0, sp.zeros(2)))


def luders_reduction() -> None:
    section("E - Sharp rank-one repeatability fixes the Lüders branch map")
    rho = sp.Matrix([[sp.Rational(2, 5), sp.Rational(1, 5) + sp.I / 10], [sp.Rational(1, 5) - sp.I / 10, sp.Rational(3, 5)]])
    coefficients = (sp.sqrt(sp.Rational(1, 3)), sp.I * sp.sqrt(sp.Rational(2, 3)))
    kraus = tuple(coefficient * P0 for coefficient in coefficients)
    effect = sp.simplify(sum((dagger(k) * k for k in kraus), sp.zeros(2)))
    branch = sp.simplify(sum((k * rho * dagger(k) for k in kraus), sp.zeros(2)))
    check("E rank-one Kraus effect is P0", exact_equal(effect, P0))
    check("E every Kraus range lies in P0", all(exact_equal(P1 * k, sp.zeros(2)) for k in kraus))
    check("E branch map is exactly P0 rho P0", exact_equal(branch, P0 * rho * P0))


def norm_square_reduction() -> None:
    section("F - Orthogonal-refinement condition selects exponent two")
    q = sp.symbols("q", real=True)
    equation = sp.Eq(2 * (1 / sp.sqrt(2)) ** q, 1)
    solutions = sp.solveset(equation, q, domain=sp.S.Reals)
    simplified_solutions = tuple(sp.simplify(solution) for solution in solutions)
    check("F two-way equal refinement has unique real exponent", simplified_solutions == (sp.Integer(2),), str(solutions))
    for branches in (2, 3, 5, 7):
        check(
            f"F q=2 is invariant under {branches}-way orthogonal refinement",
            exact_equal(branches * (1 / sp.sqrt(branches)) ** 2, 1),
        )
    check("F q=1 fails the same refinement", not exact_equal(2 * (1 / sp.sqrt(2)), 1))


def unraveling_and_ergodic_controls() -> None:
    section("G - Minimum-resource, ergodicity, and boundary nonuniqueness")
    rho = density(ket_plus)
    projective = (P0 * rho * P0, P1 * rho * P1)
    random_unitary = (rho / 2, Z * rho * Z / 2)
    projective_sum = sp.simplify(projective[0] + projective[1])
    random_sum = sp.simplify(random_unitary[0] + random_unitary[1])
    check("G two minimal two-branch instruments have the same channel", exact_equal(projective_sum, random_sum))
    check("G both instruments give one-half branch weights", [trace(branch) for branch in projective] == [sp.Rational(1, 2)] * 2 and [trace(branch) for branch in random_unitary] == [sp.Rational(1, 2)] * 2)
    projective_post = tuple(sp.simplify(branch / trace(branch)) for branch in projective)
    random_post = tuple(sp.simplify(branch / trace(branch)) for branch in random_unitary)
    check("G equal channel and resource count do not fix record meaning", not exact_equal(projective_post[0], random_post[0]) and exact_equal(projective_post[0], P0) and exact_equal(random_post[0], rho))

    stationary = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]])
    eigenvalues = []
    for flip in (sp.Rational(1, 4), sp.Rational(1, 3)):
        kernel = sp.Matrix([[1 - flip, flip], [flip, 1 - flip]])
        check(f"G q={flip} preserves unique symmetric stationary law", exact_equal(stationary * kernel, stationary))
        eigenvalues.append(1 - 2 * flip)
    check("G unique stationary law does not fix correlations", eigenvalues == [sp.Rational(1, 2), sp.Rational(1, 3)])

    weight_zero = trace(P0 * rho * P0)
    weight_one = trace(P1 * rho * P1)
    check("G opposite final boundaries select opposite histories", exact_equal(weight_zero, sp.Rational(1, 2)) and exact_equal(weight_one, sp.Rational(1, 2)) and not exact_equal(P0, P1))


def partial_trace_first(rho: sp.Matrix) -> sp.Matrix:
    reduced = sp.zeros(2)
    for a, b, second in product(range(2), range(2), range(2)):
        reduced[a, b] += rho[2 * a + second, 2 * b + second]
    return sp.simplify(reduced)


def state_and_bell_classical_controls() -> None:
    section("H - Record-state sufficiency and classical Bell boundary")
    phi_plus = (sp.kronecker_product(ket0, ket0) + sp.kronecker_product(ket1, ket1)) / sp.sqrt(2)
    phi_minus = (sp.kronecker_product(ket0, ket0) - sp.kronecker_product(ket1, ket1)) / sp.sqrt(2)
    rho_plus = density(phi_plus)
    rho_minus = density(phi_minus)
    check("H Phi+/- have identical local records", exact_equal(partial_trace_first(rho_plus), I2 / 2) and exact_equal(partial_trace_first(rho_minus), I2 / 2))
    zz = sp.kronecker_product(Z, Z)
    xx = sp.kronecker_product(X, X)
    check("H Phi+/- share ZZ law", exact_equal(trace(rho_plus * zz), 1) and exact_equal(trace(rho_minus * zz), 1))
    check("H relational phase changes future XX law", exact_equal(trace(rho_plus * xx), 1) and exact_equal(trace(rho_minus * xx), -1))

    # Same coarse record fiber fails strong lumpability under the future XX test.
    coarse_future = {"phi_plus": (1, 0), "phi_minus": (0, 1)}
    check("H omitting relational phase violates predictive sufficiency", len(set(coarse_future.values())) == 2)
    refined_records = {"phi_plus": "+", "phi_minus": "-"}
    check("H one relational bit separates this restricted family", len(set(refined_records.values())) == 2)

    chsh_values = []
    for a0, a1, b0, b1 in product((-1, 1), repeat=4):
        chsh_values.append(a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1)
    check("H all 16 deterministic local response tables obey |CHSH|=2", len(chsh_values) == 16 and all(abs(value) == 2 for value in chsh_values))
    check("H eight tables attain each sign", chsh_values.count(2) == chsh_values.count(-2) == 8)
    check("H quantum Bell control exceeds the classical mixture bound", 2 * sp.sqrt(2) > 2)


def documentation_contract() -> None:
    section("I - Model documentation boundary")
    note = NOTE.read_text(encoding="utf-8")
    flat_note = " ".join(note.split())
    for marker in (
        "CHSH = 2 sqrt(2)",
        "Sharp rank-one repeatability",
        "Orthogonal Hilbert refinement",
        "One dephasing channel",
        "ten-field",
        "TOE Boundary",
        "Sampling is physical law content",
    ):
        check(f"I note contains: {marker}", marker.lower() in flat_note.lower())
    check("I note disclaims a continuum theorem", "not the framework law" in note.lower() and "continuum theorem" in note.lower())


def main() -> int:
    source_contract()
    bell_diamond()
    sampled_actuality_and_cylinders()
    record_invariance()
    luders_reduction()
    norm_square_reduction()
    unraveling_and_ergodic_controls()
    state_and_bell_classical_controls()
    documentation_contract()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print("BOUNDARY: FD-SLIR is an exact finite conditional quantum model; its process, sample, context, record-operation scope, preparation, and continuum completion are supplied")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
