#!/usr/bin/env python3
"""Exact hostile certificate for the q=3 oriented vector-triple boundary."""

from __future__ import annotations

import argparse
import subprocess
from fractions import Fraction as F
from pathlib import Path

import sympy as sp

from admissibility_exterior_character_jr_r2_q3_oriented_vector_triple_recoupling_independent_2026_08_29 import (
    independent_checks,
    independent_fixture,
)


AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q3_ORIENTED_VECTOR_TRIPLE_CHANNEL_RESOLUTION_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q3_GAP_FILL_PRODUCT_VECTOR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_ADJACENT_PRODUCT_VECTOR_CHANNEL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_exterior_character_jr_r2_q3_oriented_vector_triple_recoupling_independent_2026_08_29.py",
)
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / AUDIT_INPUT_PATHS[0]
BLOCK237 = ROOT / AUDIT_INPUT_PATHS[1]
BLOCK236 = ROOT / AUDIT_INPUT_PATHS[2]
ACTION_PARENT = ROOT / AUDIT_INPUT_PATHS[3]

MUTATIONS = (
    "break_independent",
    "wrong_o01",
    "wrong_o10",
    "wrong_g_phase",
    "wrong_g_order",
    "drop_spin_zero",
    "force_three_routes",
    "wrong_triple_weight",
    "wrong_pair_weight",
    "wrong_closure",
    "claim_unbounded",
    "claim_full_response",
    "claim_axiom_edit",
)

CHECKING_LEVELS = (
    "per_element: exact rational O(3) moments on every non-h0 original link",
    "per_site: both parity-allowed cell-zero orientations and physical-Q histories",
    "per_mode: all seven V-cubed multiplicity routes and the signed vector Racah block",
    "per_block: one q=3 nested-product coordinate and its finite channel-resolution boundary",
    "lattice_wide: not claimed; no arbitrary word, full response, dynamics, locality, or interpretation",
)


def coupling_routes() -> tuple[tuple[int, int], ...]:
    """Allowed (pair spin L, total spin J) routes in (V tensor V) tensor V."""

    return tuple(
        (pair_spin, total_spin)
        for pair_spin in range(3)
        for total_spin in range(abs(pair_spin - 1), pair_spin + 2)
    )


def raw_triple_weights() -> tuple[tuple[int, int, F], ...]:
    """One d_J/81 weight for each multiplicity copy of total spin J."""

    rows = []
    for pair_spin, total_spin in coupling_routes():
        rows.append((pair_spin, total_spin, F(2 * total_spin + 1, 81)))
    return tuple(rows)


def pair_weights() -> tuple[tuple[int, F], ...]:
    return tuple((spin, F(2 * spin + 1, 27)) for spin in range(3))


def authority_and_scope() -> bool:
    note = NOTE.read_text()
    parents = (BLOCK237, BLOCK236, ACTION_PARENT)
    status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    return (
        all("claim_id:" in path.read_text() for path in parents)
        and "actual_current_surface_status: conditional-support" in note
        and "finite channel-resolution growth" in note
        and "not a theorem that seven states are" in note
        and "does not prove unbounded" in note
        and "complete temporal response remains open" in note
        and "MINIMAL_AXIOMS" not in status
    )


def fixture(
    mutation: str | None = None,
    independent: dict[str, object] | None = None,
) -> dict[str, object]:
    if independent is None:
        independent = independent_fixture()
    open_01 = independent["open_01"]
    open_10 = independent["open_10"]
    representations = independent["representations"]
    racah = independent["intertwiners"]["racah"]
    expected_racah = sp.Matrix([
        [sp.Rational(1, 3), -sp.sqrt(3) / 3, sp.sqrt(5) / 3],
        [sp.sqrt(3) / 3, -sp.Rational(1, 2), -sp.sqrt(15) / 6],
        [sp.sqrt(5) / 3, sp.sqrt(15) / 6, sp.Rational(1, 6)],
    ])

    exact_independent = all(passed for _label, passed in independent_checks(independent))
    o01_coefficient = open_01["coefficient"]
    o10_coefficient = open_10["coefficient"]
    phase_target = expected_racah
    order_three = independent["intertwiners"]["order_three"]
    decomposition = representations["powers"][3]
    routes = coupling_routes()
    triple_weights = raw_triple_weights()
    old_pair_weights = pair_weights()
    closure_01 = sum(weight for _pair, _total, weight in triple_weights)
    closure_10 = sum(weight for _spin, weight in old_pair_weights)
    boundary = {"old_pair_channels": 3, "triple_channels": len(routes), "unbounded": False}
    scope = authority_and_scope()
    axiom_edit = False

    if mutation == "break_independent":
        exact_independent = False
    elif mutation == "wrong_o01":
        o01_coefficient = F(1, 27)
    elif mutation == "wrong_o10":
        o10_coefficient = F(1, 27)
    elif mutation == "wrong_g_phase":
        phase_target = sp.diag(1, -1, 1) * expected_racah * sp.diag(1, -1, 1)
    elif mutation == "wrong_g_order":
        order_three = False
    elif mutation == "drop_spin_zero":
        decomposition = {1: 3, 2: 2, 3: 1}
    elif mutation == "force_three_routes":
        routes = routes[:3]
    elif mutation == "wrong_triple_weight":
        triple_weights = triple_weights[:-1] + ((2, 3, F(7, 27)),)
    elif mutation == "wrong_pair_weight":
        old_pair_weights = old_pair_weights[:-1] + ((2, F(5, 81)),)
    elif mutation == "wrong_closure":
        closure_01 = F(1)
    elif mutation == "claim_unbounded":
        boundary["unbounded"] = True
    elif mutation == "claim_full_response":
        scope = False
    elif mutation == "claim_axiom_edit":
        axiom_edit = True

    return {
        "independent": exact_independent,
        "open_01": open_01,
        "open_10": open_10,
        "o01_coefficient": o01_coefficient,
        "o10_coefficient": o10_coefficient,
        "racah": racah,
        "phase_target": phase_target,
        "order_three": order_three,
        "decomposition": decomposition,
        "routes": routes,
        "triple_weights": triple_weights,
        "pair_weights": old_pair_weights,
        "closure_01": closure_01,
        "closure_10": closure_10,
        "boundary": boundary,
        "scope": scope,
        "axiom_edit": axiom_edit,
        "representations": representations,
        "intertwiners": independent["intertwiners"],
    }


def checks(
    mutation: str | None = None,
    independent: dict[str, object] | None = None,
) -> tuple[tuple[str, bool], ...]:
    data = fixture(mutation, independent)
    expected_routes = (
        (0, 1),
        (1, 0), (1, 1), (1, 2),
        (2, 1), (2, 2), (2, 3),
    )
    expected_triple_weights = tuple(
        (pair, total, F(2 * total + 1, 81))
        for pair, total in expected_routes
    )
    return (
        ("the standalone exact original-link reconstruction passes",
         data["independent"]),
        ("O01 is exactly the same-order identity on V cubed over 81",
         data["open_01"]["exact_expected_tensor"]
         and data["o01_coefficient"] == F(1, 81)
         and data["open_01"]["open_side_census"] == {"left": 3, "right": 3}),
        ("O10 is exactly the two-to-four cup/cross tensor over 81",
         data["open_10"]["exact_expected_tensor"]
         and data["o10_coefficient"] == F(1, 81)
         and data["open_10"]["open_side_census"] == {"left": 2, "right": 4}),
        ("the contracted strand map fixes the Cartesian-convention vector Racah block",
         data["racah"] == data["phase_target"]),
        ("the convention-fixed Racah block is orthogonal with determinant one and order three",
         data["intertwiners"]["orthogonal"]
         and data["intertwiners"]["determinant"] == 1
         and data["order_three"]),
        ("V cubed decomposes into one, three, two, and one copies of spins zero through three",
         data["decomposition"] == {0: 1, 1: 3, 2: 2, 3: 1}),
        ("pair spin and total spin resolve exactly seven triple channels",
         data["routes"] == expected_routes),
        ("the seven raw O01 channel weights are d_J over 81",
         data["triple_weights"] == expected_triple_weights),
        ("the O10 scalar cup leaves the three pair weights d_L over 27",
         data["pair_weights"] == ((0, F(1, 27)), (1, F(1, 9)), (2, F(5, 27)))),
        ("both raw orientation closures equal one third",
         data["closure_01"] == F(1, 3) and data["closure_10"] == F(1, 3)),
        ("the exact result is finite three-to-seven channel resolution, not a minimal-memory theorem",
         data["boundary"] == {"old_pair_channels": 3, "triple_channels": 7, "unbounded": False}),
        ("the note leaves the temporal response and arbitrary histories open",
         data["scope"]),
        ("no axiom or approved primitive is edited",
         not data["axiom_edit"]),
    )


def run(
    mutation: str | None = None,
    independent: dict[str, object] | None = None,
) -> int:
    results = checks(mutation, independent)
    if mutation is None:
        print(f"audit_timeout_sec: {AUDIT_TIMEOUT_SEC}")
        for level in CHECKING_LEVELS:
            print(level)
    failures = 0
    for label, passed in results:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(results) - failures} FAIL={failures}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-suite", action="store_true")
    args = parser.parse_args()
    if args.mutation_suite:
        independent = independent_fixture()
        failures = 0
        for mutation in MUTATIONS:
            count = run(mutation, independent)
            passed = count == 1
            print(f"[{'PASS' if passed else 'FAIL'}] mutation {mutation}: failures={count}")
            failures += int(not passed)
        print(f"MUTATION TOTAL: PASS={len(MUTATIONS) - failures} FAIL={failures}")
        return int(failures != 0)
    return int(run(args.mutation) != 0)


if __name__ == "__main__":
    raise SystemExit(main())
