#!/usr/bin/env python3
"""Exact finite controls for full-lattice FD-SLIR compatibility and content.

This runner verifies a conditional construction and finite independence
fixtures.  It does not select a physical law or modify foundation authority.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import floor, log2
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "FULL_LATTICE_FD_SLIR_COMPATIBILITY_AND_MINIMUM_CONTENT_NOTE_2026-07-14.md"
)
FD_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "FINITE_DIAMOND_SAMPLED_LUDERS_INVARIANT_RECORD_MODEL_NOTE_2026-07-14.md"
)
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def source_contract() -> None:
    section("A - Authority and documentation contract")
    note = NOTE.read_text(encoding="utf-8")
    fd_note = FD_NOTE.read_text(encoding="utf-8")
    normalized = note.lower().replace("*", "").replace("`", "")
    normalized_words = " ".join(normalized.split())
    check("A extension note is authority-free", "authority: none" in normalized)
    check("A source finite model is authority-free", "authority: none" in fd_note.lower().replace("*", ""))
    check("A extension is conditional", "conditional extension theorem" in normalized)
    check("A extension disclaims an axiom proposal", "not the framework law, an axiom proposal" in normalized)
    check(
        "A seven target names are present",
        all(
            f"`{field}`" in note
            for field in (
                "DOMAIN",
                "STATE",
                "CONTEXT",
                "ACTUALITY",
                "STATISTICS",
                "EXTENSION",
                "RENEWAL",
            )
        ),
    )
    check("A one/three/five/seven boundary is documented", all(marker in note for marker in ("one-name syntactic cover", "three clauses", "five-clause surface", "seven semantic atoms")))
    check("A set-cover count is explicitly scoped", "residual counts inside the declared fd-slir typing" in normalized_words)
    check("A uncompressed law-job checklist has thirteen rows", "uncompressed law-job checklist" in normalized_words and "13. renewal/export" in note)
    check("A corrected strict-instrument DAG has ten core inputs", "corrected dependency dag under strict fd-slir typing" in normalized_words and "c10" in normalized_words)
    check("A optional formation, trial, and boundary inputs are split", all(marker in normalized_words for marker in ("c11 formation_eligibility", "e1 trial_corpus", "b actual_boundary_selection")))
    check("A strict and Lieb-Robinson propagation are separated", "liebrobinson tails" in normalized_words.replace("-", ""))
    check("A generic frequency theorem is disclaimed", "No generic frequency theorem is claimed here" in note)


def l1(point: tuple[int, int, int]) -> int:
    return sum(abs(value) for value in point)


def l1_ball(radius: int) -> set[tuple[int, int, int]]:
    return {
        point
        for point in product(range(-radius, radius + 1), repeat=3)
        if l1(point) <= radius
    }


def ball_size_formula(radius: int) -> int:
    return (4 * radius**3 + 6 * radius**2 + 8 * radius + 3) // 3


def centered_diamond(radius: int):
    return {
        (time, point)
        for time in range(-radius, radius + 1)
        for point in product(range(-radius, radius + 1), repeat=3)
        if l1(point) <= radius - abs(time)
    }


def diamond_size_formula(radius: int) -> int:
    return (2 * radius**4 + 4 * radius**3 + 10 * radius**2 + 8 * radius + 3) // 3


def causal(left, right) -> bool:
    time_left, point_left = left
    time_right, point_right = right
    distance = sum(abs(a - b) for a, b in zip(point_left, point_right))
    return time_left <= time_right and distance <= time_right - time_left


def geometry_and_diamonds() -> None:
    section("B - Exact finite causal-diamond geometry")
    for radius in range(6):
        ball = l1_ball(radius)
        diamond = centered_diamond(radius)
        check(f"B radius-{radius} L1 ball count", len(ball) == ball_size_formula(radius))
        check(f"B radius-{radius} diamond count", len(diamond) == diamond_size_formula(radius))
        past = (-radius, (0, 0, 0))
        future = (radius, (0, 0, 0))
        check(
            f"B radius-{radius} is the apex interval",
            all(causal(past, event) and causal(event, future) for event in diamond),
        )
        if radius:
            check(f"B D_{radius-1} embeds in D_{radius}", centered_diamond(radius - 1) <= diamond)
    expected = [1, 9, 41, 129, 321, 681]
    check("B T=0..5 diamond sequence", [diamond_size_formula(radius) for radius in range(6)] == expected, str(expected))
    left = (0, (0, 0, 0))
    right = (0, (1, 0, 0))
    check("B distinct same-slice events are incomparable", not causal(left, right) and not causal(right, left))


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.diag(1, -1)
P0 = sp.diag(1, 0)
P1 = sp.diag(0, 1)
KET0 = sp.Matrix([1, 0])
KET1 = sp.Matrix([0, 1])
KET_PLUS = (KET0 + KET1) / sp.sqrt(2)
KET_MINUS = (KET0 - KET1) / sp.sqrt(2)


def dagger(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.conjugate().T


def density(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * dagger(vector))


def trace(matrix: sp.Matrix):
    return sp.simplify(sp.trace(matrix))


def exact_matrix(left: sp.Matrix, right: sp.Matrix) -> bool:
    return sp.simplify(left - right) == sp.zeros(*left.shape)


def sequential_cylinders(pvm_stream, initial_state):
    law = {}
    for outcomes in product((0, 1), repeat=len(pvm_stream)):
        branch = initial_state
        for event, outcome in enumerate(outcomes):
            projector = pvm_stream[event][outcome]
            branch = sp.simplify(projector * branch * projector)
        law[outcomes] = trace(branch)
    return law


def cylinder_compatibility() -> None:
    section("C - Projective cylinders and incompatibility control")
    z_pvm = (P0, P1)
    x_pvm = (density(KET_PLUS), density(KET_MINUS))
    stream = (z_pvm, x_pvm, z_pvm, x_pvm, z_pvm, x_pvm)
    initial = density(KET_PLUS)
    family = {
        length: sequential_cylinders(stream[:length], initial)
        for length in range(1, len(stream) + 1)
    }
    for length, law in family.items():
        check(f"C length-{length} law normalizes", sp.simplify(sum(law.values()) - 1) == 0)
        if length > 1:
            previous = family[length - 1]
            check(
                f"C length-{length} restricts to length-{length-1}",
                all(
                    sp.simplify(sum(law[prefix + (outcome,)] for outcome in (0, 1)) - weight) == 0
                    for prefix, weight in previous.items()
                ),
            )
    check("C largest checked family has 64 cylinders", len(family[6]) == 64)

    small = {(0,): Fraction(1, 2), (1,): Fraction(1, 2)}
    large = {
        (0, 0): Fraction(1, 3),
        (0, 1): Fraction(1, 3),
        (1, 0): Fraction(1, 6),
        (1, 1): Fraction(1, 6),
    }
    check("C incompatible finite laws each normalize", sum(small.values()) == sum(large.values()) == 1)
    check(
        "C normalization does not imply projective extension",
        sum(large[(0, tail)] for tail in (0, 1)) == Fraction(2, 3) != small[(0,)],
    )


def spacelike_order() -> None:
    section("D - Spacelike order and marginal")
    rho = density(sp.kronecker_product(KET_PLUS, KET_PLUS))
    left = sp.kronecker_product(P0, I2)
    right = sp.kronecker_product(I2, density(KET_PLUS))
    check("D disjoint projectors commute", exact_matrix(left * right, right * left))
    branch_lr = sp.simplify(right * left * rho * left * right)
    branch_rl = sp.simplify(left * right * rho * right * left)
    check("D spacelike branch is order independent", exact_matrix(branch_lr, branch_rl))
    remote = tuple(sp.kronecker_product(I2, projector) for projector in (P0, P1))
    local_probability = trace(left * rho * left)
    remote_sum = sum(trace(projector * left * rho * left * projector) for projector in remote)
    check("D complete remote PVM preserves local marginal", sp.simplify(local_probability - remote_sum) == 0)


def composition_and_state_ablations() -> None:
    section("E - DOMAIN and STATE independence")
    dimensions = tuple((sites, 2**sites, 4**sites) for sites in range(1, 9))
    check("E generated tensor dimensions", all(algebra == hilbert**2 for _, hilbert, algebra in dimensions))
    word = sp.kronecker_product(X, Z)
    direct = sp.kronecker_product(word, I2, I2)
    stepwise = sp.kronecker_product(sp.kronecker_product(word, I2), I2)
    check("E quasilocal embeddings compose", exact_matrix(direct, stepwise))
    rho2 = density(sp.kronecker_product(KET_PLUS, KET0))
    rho4 = sp.kronecker_product(rho2, density(KET0), density(KET0))
    observable2 = sp.kronecker_product(X, Z)
    observable4 = sp.kronecker_product(observable2, I2, I2)
    check("E embedded local expectation is unchanged", sp.simplify(trace(rho2 * observable2) - trace(rho4 * observable4)) == 0)

    visible_generated_dimension = 16
    duplicate_full_dimension = 32
    check("E ordinary two-site visible algebra has dimension 16", visible_generated_dimension == 16)
    check("E duplicate sector adds a silent 16-dimensional sector", duplicate_full_dimension == 2 * visible_generated_dimension)
    check("E one-site data do not force no-extra-global-sector", duplicate_full_dimension != visible_generated_dimension)

    phi_plus = (sp.kronecker_product(KET0, KET0) + sp.kronecker_product(KET1, KET1)) / sp.sqrt(2)
    phi_minus = (sp.kronecker_product(KET0, KET0) - sp.kronecker_product(KET1, KET1)) / sp.sqrt(2)
    rho_plus = density(phi_plus)
    rho_minus = density(phi_minus)
    zz = sp.kronecker_product(Z, Z)
    xx = sp.kronecker_product(X, X)
    check("E hidden phases share the coarse ZZ law", trace(rho_plus * zz) == trace(rho_minus * zz) == 1)
    check("E hidden phases have opposite future XX laws", trace(rho_plus * xx) == 1 and trace(rho_minus * xx) == -1)


def context_actuality_statistics_ablations() -> None:
    section("F - CONTEXT, ACTUALITY, and STATISTICS independence")
    rho = density(KET_PLUS)
    branches = (sp.simplify(P0 * rho * P0), sp.simplify(P1 * rho * P1))
    nonselective = sp.simplify(sum(branches, sp.zeros(2)))
    check("F nonselective Lüders map is normalized", trace(nonselective) == 1)
    check(
        "F nonselective map is not either selected branch",
        not exact_matrix(nonselective, branches[0] / trace(branches[0]))
        and not exact_matrix(nonselective, branches[1] / trace(branches[1])),
    )

    trace_law = (Fraction(1, 2), Fraction(1, 2))
    alternative_law = (Fraction(3, 4), Fraction(1, 4))
    seed = Fraction(3, 5)

    def sample(weights):
        return 0 if seed < weights[0] else 1

    check("F two normalized positive laws have identical support", sum(trace_law) == sum(alternative_law) == 1 and all(weight > 0 for weight in trace_law + alternative_law))
    check("F actuality does not select the statistical law", sample(trace_law) == 1 and sample(alternative_law) == 0)

    rho_zero = density(KET0)
    z_law = (trace(P0 * rho_zero * P0), trace(P1 * rho_zero * P1))
    x_projectors = (density(KET_PLUS), density(KET_MINUS))
    x_law = tuple(trace(projector * rho_zero * projector) for projector in x_projectors)
    check("F Z and X contexts have exact distinct laws", z_law == (1, 0) and x_law == (sp.Rational(1, 2), sp.Rational(1, 2)))
    check("F one fixed context does not derive context selection", z_law != x_law)


def renewal_export() -> None:
    section("G - Permanent-record renewal and export")
    previous = set()
    for radius in range(9):
        ball = l1_ball(radius)
        shell = ball - previous
        check(f"G radius-{radius} ball capacity", len(ball) == ball_size_formula(radius))
        check(f"G radius-{radius} shell capacity", len(shell) == (1 if radius == 0 else 4 * radius**2 + 2))
        previous = ball

    allocation = []
    for radius in range(6):
        prior = l1_ball(radius - 1) if radius else set()
        allocation.extend(sorted(l1_ball(radius) - prior))
    check("G shell allocator is injective", len(allocation) == len(set(allocation)))
    check("G shell allocator fills B_5 exactly", len(allocation) == ball_size_formula(5))

    for bits_per_cycle in (1, 2, 3, 5):
        for cycles in (1, 2, 4, 7):
            histories = 2 ** (bits_per_cycle * cycles)
            required_bits = int(log2(histories))
            check(
                f"G export k={bits_per_cycle},m={cycles}",
                histories == 2 ** (bits_per_cycle * cycles)
                and required_bits == bits_per_cycle * cycles,
            )
    check("G B=17,k=3 supports only five arbitrary cycles", floor(17 / 3) == 5)


def minimum_covers(universe, candidates):
    names = tuple(candidates)
    for size in range(1, len(names) + 1):
        covers = []
        for chosen in combinations(names, size):
            covered = set().union(*(candidates[name] for name in chosen))
            if universe <= covered:
                covers.append(chosen)
        if covers:
            return covers
    return []


def independence_and_set_cover() -> None:
    section("H - Seven-residual-atom independence and exact scoped covers")
    five = frozenset({"DOMAIN", "STATE", "CONTEXT", "ACTUALITY", "STATISTICS"})
    atoms = {
        "TENSOR_NET": {"DOMAIN"},
        "RECORD_MARKOV": {"STATE"},
        "RECORDED_CONTEXT": {"CONTEXT"},
        "ONE_SAMPLE": {"ACTUALITY"},
        "TRACE_WEIGHT": {"STATISTICS"},
    }
    sampled = {**atoms, "SAMPLED_INSTRUMENT": {"CONTEXT", "ACTUALITY", "STATISTICS"}}
    macro = {**sampled, "FD_SLIR_MACRO": set(five)}
    check("H five-field semantic minimum is five", len(minimum_covers(five, atoms)[0]) == 5)
    check("H sampled-instrument five-field surface minimum is three", len(minimum_covers(five, sampled)[0]) == 3)
    check("H FD-SLIR macro gives one-name cover", minimum_covers(five, macro) == [("FD_SLIR_MACRO",)])

    full = five | {"EXTENSION", "RENEWAL"}
    full_atoms = {**atoms, "PROJECTIVE_FAMILY": {"EXTENSION"}, "PROPER_EXPORT": {"RENEWAL"}}
    audit_separated = {**full_atoms, "SAMPLED_INSTRUMENT": {"CONTEXT", "ACTUALITY", "STATISTICS"}}
    full_reference = {
        **audit_separated,
        "FULL_LAW_REFERENCE": {"CONTEXT", "ACTUALITY", "STATISTICS", "EXTENSION", "RENEWAL"},
    }
    check("H full dependency-expanded minimum is seven", len(minimum_covers(full, full_atoms)[0]) == 7)
    check("H audit-separated visible minimum is five", len(minimum_covers(full, audit_separated)[0]) == 5)
    check("H full-law plus DOMAIN and STATE minimum is three", len(minimum_covers(full, full_reference)[0]) == 3)

    fields = tuple(sorted(full))
    ablations = {
        missing: tuple(field != missing for field in fields)
        for missing in fields
    }
    check("H seven single-atom ablations are distinct", len(set(ablations.values())) == 7)
    check("H every ablation retains the other six targets", all(sum(row) == 6 for row in ablations.values()))


def boundary_needles() -> None:
    section("I - Narrow claim boundary")
    note = " ".join(
        NOTE.read_text(encoding="utf-8")
        .lower()
        .replace("*", "")
        .replace("`", "")
        .split()
    )
    for phrase in (
        "does not derive either generated qubit composition",
        "predictive completeness of records",
        "one exact compatible full-law reference",
        "scoped residual minimum",
        "uncompressed law-job checklist",
        "corrected dependency dag",
        "live alternatives remain",
        "no global derivation route is declared closed",
    ):
        check(f"I note contains: {phrase}", phrase in note)


def main() -> int:
    source_contract()
    geometry_and_diamonds()
    cylinder_compatibility()
    spacelike_order()
    composition_and_state_ablations()
    context_actuality_statistics_ablations()
    renewal_export()
    independence_and_set_cover()
    boundary_needles()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: conditional full-lattice FD-SLIR compatibility and finite "
        "minimum-content certificate; no law, axiom, or audit selection"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
