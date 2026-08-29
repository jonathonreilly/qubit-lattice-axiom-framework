#!/usr/bin/env python3
"""Exact hostile certificate for the Block239 seven-route temporal response."""

from __future__ import annotations

import argparse
from collections import Counter
from math import comb
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q3_SEVEN_CHANNEL_TEMPORAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q3_ORIENTED_VECTOR_TRIPLE_CHANNEL_RESOLUTION_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_CO_SCALED_TEMPORAL_TROTTER_AND_CYLINDRICAL_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_TIME_REFINEMENT_SEMIGROUP_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "scripts/admissibility_exterior_character_jr_r2_q3_seven_channel_temporal_response_independent_2026_08_29.py",
)

ROUTES = (
    (0, 1),
    (1, 0), (1, 1), (1, 2),
    (2, 1), (2, 2), (2, 3),
)
MUTATIONS = (
    "j0_trivial",
    "collapse_total_spin",
    "erase_pair_channel",
    "wrong_ty",
    "wrong_tz",
    "wrong_t01",
    "wrong_t10",
    "drop_reverse_orientation",
    "double_count_dimension",
    "wrong_half_action_normalization",
    "claim_seven_local_eigenvalues",
    "claim_minimal_memory",
    "claim_axiom_edit",
)


def fine_plaquette(index: int) -> frozenset[str]:
    return frozenset((f"u{index}", f"h{index + 1}", f"v{index}", f"h{index}"))


def merged_interval(first_cell: int, last_cell: int) -> frozenset[str]:
    first = 2 * first_cell
    last = 2 * last_cell + 1
    return frozenset(
        [f"u{index}" for index in range(first, last + 1)]
        + [f"h{last + 1}"]
        + [f"v{index}" for index in range(first, last + 1)]
        + [f"h{first}"]
    )


def multiplicity_census(factors: tuple[frozenset[str], ...]) -> dict[int, int]:
    links = frozenset().union(*factors)
    counts = Counter(sum(link in factor for factor in factors) for link in links)
    return dict(sorted(counts.items()))


def catalan(index: int) -> int:
    return comb(2 * index, index) // (index + 1)


def vector_action_coefficient(n: int) -> sp.Rational:
    return sp.Rational(3 * 2 ** max(0, 3 - 2 * n) * catalan(n), n + 2) if n <= 1 else (
        sp.Rational(3 * catalan(n), (n + 2) * 2 ** (2 * n - 3))
    )


def route_data(mutation: str | None = None) -> dict[str, object]:
    d, t, u, v = sp.symbols("d t u v")
    x = {0: sp.Integer(1), 1: t, 2: u}
    y = {0: d, 1: t, 2: u, 3: v}
    if mutation == "j0_trivial":
        y[0] = sp.Integer(1)
    if mutation == "collapse_total_spin":
        y = {spin: t for spin in range(4)}
    if mutation == "erase_pair_channel":
        x = {spin: sp.Integer(1) for spin in range(3)}

    rows = {}
    total_numerator = sp.Integer(0)
    for pair_spin, total_spin in ROUTES:
        pair_multiplier = x[pair_spin]
        total_multiplier = y[total_spin]
        ty = t**6 * pair_multiplier**9
        tz = t**7 * pair_multiplier**4 * total_multiplier**5
        t01 = t**7 * pair_multiplier**6 * total_multiplier**3
        t10 = t**8 * pair_multiplier**7 * total_multiplier**2
        if mutation == "wrong_ty":
            ty *= t
        if mutation == "wrong_tz":
            tz *= total_multiplier
        if mutation == "wrong_t01":
            t01 *= pair_multiplier
        if mutation == "wrong_t10":
            t10 *= t
        dimension = 2 * total_spin + 1
        if mutation == "double_count_dimension":
            dimension *= 2 * total_spin + 1
        first = (ty + t01) * (tz + t01)
        second = (ty + t10) * (tz + t10)
        if mutation == "drop_reverse_orientation":
            second = 0
        numerator = sp.expand(dimension * (first + second))
        rows[(pair_spin, total_spin)] = {
            "x_L": pair_multiplier,
            "y_J": total_multiplier,
            "T_Y": ty,
            "T_Z": tz,
            "T_01": t01,
            "T_10": t10,
            "d_J": 2 * total_spin + 1,
            "numerator": numerator,
        }
        total_numerator += numerator
    denominator = 324
    if mutation == "wrong_half_action_normalization":
        denominator = 81
    return {
        "symbols": (d, t, u, v),
        "x": x,
        "y": y,
        "rows": rows,
        "dimension_sum": sum(2 * total_spin + 1 for _pair_spin, total_spin in ROUTES),
        "normalized_response": sp.expand(total_numerator / denominator),
        "denominator": denominator,
    }


def note_scope_ok(root: Path, mutation: str | None) -> tuple[bool, bool, bool]:
    note_path = root / AUDIT_INPUT_PATHS[0]
    note = note_path.read_text() if note_path.exists() else ""
    note_lower = note.lower()
    route_scope = (
        "seven route contributions" in note_lower
        and "not seven intrinsic local eigenvalues" in note_lower
        and "minimal transfer memory remains open" in note_lower
    )
    axiom_scope = "No axiom or approved primitive changes" in note
    if mutation == "claim_seven_local_eigenvalues":
        route_scope = False
    if mutation == "claim_minimal_memory":
        route_scope = False
    if mutation == "claim_axiom_edit":
        axiom_scope = False
    return route_scope, axiom_scope, note_path.exists()


def checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    root = Path(__file__).resolve().parents[1]
    data = route_data(mutation)
    d, t, u, v = data["symbols"]
    rows = data["rows"]
    a0 = merged_interval(0, 0)
    d01 = merged_interval(0, 1)
    d012 = merged_interval(0, 2)
    p0, p1 = fine_plaquette(0), fine_plaquette(1)
    censuses = {
        "Y": multiplicity_census((d01, d012)),
        "Z": multiplicity_census((a0, d01, d012)),
        "Y0": multiplicity_census((p0, d01, d012)),
        "Y1": multiplicity_census((p1, d01, d012)),
        "Z0": multiplicity_census((p0, a0, d01, d012)),
        "Z1": multiplicity_census((p1, a0, d01, d012)),
    }
    identity_value = sp.simplify(data["normalized_response"].subs({d: 1, t: 1, u: 1, v: 1}))
    zero_vector_value = sp.simplify(data["normalized_response"].subs(t, 0))
    route_polynomials = tuple(row["numerator"] for row in rows.values())
    pairwise_distinct = all(
        sp.expand(route_polynomials[left] - route_polynomials[right]) != 0
        for left in range(len(route_polynomials))
        for right in range(left)
    )
    route_scope, axiom_scope, note_exists = note_scope_ok(root, mutation)
    return [
        ("the q=3 factor-set census is reconstructed from original links", censuses == {
            "Y": {1: 6, 2: 9},
            "Z": {1: 7, 2: 4, 3: 5},
            "Y0": {1: 7, 2: 6, 3: 3},
            "Y1": {1: 8, 2: 7, 3: 2},
            "Z0": {1: 8, 2: 4, 3: 2, 4: 3},
            "Z1": {1: 7, 2: 5, 3: 3, 4: 2},
        }),
        ("the seven pair-spin/total-spin routes have total dimension 27", data["dimension_sum"] == 27),
        ("the odd total-spin-zero route carries the determinant multiplier", rows[(1, 0)]["y_J"] == d),
        ("central crossing is multiplicity blind at fixed total spin", rows[(0, 1)]["y_J"] == rows[(1, 1)]["y_J"] == rows[(2, 1)]["y_J"] == t),
        ("double-occupied links retain the old pair-channel multiplier", data["x"] == {0: 1, 1: t, 2: u}),
        ("the coarse Y factor is t^6 x_L^9", all(row["T_Y"] == t**6 * row["x_L"]**9 for row in rows.values())),
        ("the coarse Z factor is t^7 x_L^4 y_J^5", all(row["T_Z"] == t**7 * row["x_L"]**4 * row["y_J"]**5 for row in rows.values())),
        ("the O01 residual factor is t^7 x_L^6 y_J^3", all(row["T_01"] == t**7 * row["x_L"]**6 * row["y_J"]**3 for row in rows.values())),
        ("the cup-resolved O10 factor is t^8 x_L^7 y_J^2", all(row["T_10"] == t**8 * row["x_L"]**7 * row["y_J"]**2 for row in rows.values())),
        ("both Gram orientations and the half-action normalization are present", data["denominator"] == 324 and all("T_01" in row and "T_10" in row for row in rows.values())),
        ("the identity crossing returns the raw two-orientation closure 2/3", identity_value == sp.Rational(2, 3)),
        ("zero defining-vector multiplier kills every exclusive-rail route", zero_vector_value == 0),
        ("the seven route polynomials are generically distinct without asserting pointwise separation", pairwise_distinct),
        ("the supplied n=1 vector action coefficient remains c_V=2", vector_action_coefficient(1) == 2),
        ("the theorem note keeps route, local-eigenvalue, memory, and axiom boundaries honest", note_exists and route_scope and axiom_scope),
    ]


def run(mutation: str | None = None) -> tuple[int, int]:
    results = checks(mutation)
    passed = sum(ok for _label, ok in results)
    failed = len(results) - passed
    for label, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return passed, failed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-suite", action="store_true")
    args = parser.parse_args()
    if args.mutation_suite:
        passed = 0
        for mutation in MUTATIONS:
            _checks, failures = run(mutation)
            detected = failures > 0
            print(f"[{'PASS' if detected else 'FAIL'}] mutation {mutation}: failures={failures}")
            passed += int(detected)
        failed = len(MUTATIONS) - passed
        print(f"MUTATION TOTAL: PASS={passed} FAIL={failed}")
        return int(failed != 0)
    _passed, failed = run(args.mutation)
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
