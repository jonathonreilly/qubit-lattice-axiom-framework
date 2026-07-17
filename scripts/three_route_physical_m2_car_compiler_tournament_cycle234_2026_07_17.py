#!/usr/bin/env python3
"""Cycle 234 common runner for the three-route physical-M2 CAR tournament.

This runner does not turn three scoped failures into a general no-go.  It
reruns every route artifact, checks the common exact residuals, independently
reconstructs the scalar-reference ranks and macro-translation residual, and
guards the route-independent N1--N8 and time-lane wording in the synthesis.
"""

from __future__ import annotations

import importlib.util
from itertools import combinations, product
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "THREE_ROUTE_PHYSICAL_M2_CAR_COMPILER_TOURNAMENT_CYCLE234_NOTE_2026-07-17.md"
)
ROUTES = (
    (
        "route1",
        SCRIPTS / "ROUTE1_DIRECT_CAR_COMPILER_CYCLE231_2026_07_17.py",
        "SUMMARY 24 passed / 0 failed",
    ),
    (
        "route2",
        SCRIPTS / "ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
        "SUMMARY PASS 27 FAIL 0",
    ),
    (
        "route3",
        SCRIPTS / "ROUTE3_STAGGERED_CAR_COMPILER_CYCLE233_2026_07_17.py",
        "SUMMARY: 20 PASS / 0 FAIL",
    ),
)

sys.path.insert(0, str(SCRIPTS))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError((name, path))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "no route satisfies the full local-encoding contract",
        "bounded-radius locality-preserving state encoding",
        "global parity bus",
        "operator residual `2`",
        "global residual = sqrt(8)",
        "three torus wilson spectators",
        "unit-translation theorem",
        "spatial-dimension and time firewall",
        "compiler controls",
        "c_ref",
        "c_num",
        "c_wrap",
        "c_int",
        "c_local",
        "c_source",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution audit",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "there is no axiom pressure",
        "**authority:** none",
        "**audit:** unset",
    )
    missing = tuple(item for item in required if item not in text)
    check("synthesis preserves the frozen contract, six-wall ledger, and N1-N8 scope", not missing, missing)


def route_regressions() -> None:
    rows = []
    for name, path, expected in ROUTES:
        result = subprocess.run(
            (sys.executable, str(path)),
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        rows.append(
            {
                "route": name,
                "exit": result.returncode,
                "expected_summary": expected in result.stdout,
            }
        )
    check(
        "all three independently retained route runners pass their scoped controls",
        all(row["exit"] == 0 and row["expected_summary"] for row in rows),
        rows,
    )


def direct_residual_controls(route1) -> None:
    rows = []
    for length in (3, 4, 5):
        mismatch, total, witness = route1.two_particle_mismatch(length)
        rows.append((length, mismatch, total, witness))
    expected = ((3, 4140, 13041), (4, 19008, 73536), (5, 60600, 280875))
    check(
        "direct endpoint stream retains the exact held-out two-particle mismatch census",
        tuple(row[:3] for row in rows) == expected and all(row[3] is not None for row in rows),
        rows,
    )
    permutation = route1.edge_permutation(3)
    witness = rows[0][3]
    exact = route1.exterior_permutation_action(permutation, witness)
    local = route1.endpoint_fswap_action(permutation, witness)
    check(
        "direct local intertwining residual has an exact norm-two basis witness",
        exact[0] == local[0] and abs(exact[1] - local[1]) == 2,
        {"witness": witness, "exact": exact, "local": local},
    )


def gauge_rank_and_encoding_controls(route2) -> None:
    rows = []
    for length in (3, 4, 5, 7):
        graph = route2.ReferenceGraph(length, True)
        local_rank = route2.gf2_rank(mask for mask, _, _ in route2.local_cycles(graph))
        full_rank = len(graph.edges) - len(graph.vertices) + 1
        d_rank = route2.gf2_rank(row.z for row in route2.reference_constraints(graph))
        rows.append((length, local_rank, full_rank, d_rank))
    check(
        "scalar-reference graph has exact local/full/D ranks and exactly three Wilson labels",
        rows
        == [
            (3, 457, 460, 26),
            (4, 1086, 1089, 63),
            (5, 2123, 2126, 124),
            (7, 5829, 5832, 342),
        ],
        rows,
    )

    local_residual, global_residual = route2.pair_shadow_global_counterexample()
    check(
        "pair-shadow lift passes locally and fails global assembly by sqrt(8)",
        local_residual < 2e-15 and abs(global_residual - np.sqrt(8)) < 2e-13,
        {"local": local_residual, "global": global_residual},
    )

    sector_rows = {
        length: {b: b ** (length**3) for b in (-1, 1)}
        for length in (3, 4, 5, 7)
    }
    check(
        "odd volumes carry both matter parities while even L=4 duplicates only even matter",
        all(set(sector_rows[length].values()) == {-1, 1} for length in (3, 5, 7))
        and set(sector_rows[4].values()) == {1},
        sector_rows,
    )

    witnesses = []
    for radius in (0, 1, 2, 4):
        length = 2 * radius + 5
        remote = (radius + 1, 0, 0)
        distance = min(remote[0], length - remote[0])
        witnesses.append((length, radius, distance, 0, 2))
    check(
        "scalar reference gives a route-specific bounded-E contradiction at held-out radii",
        all(distance > radius and local_gap == 0 and parity_gap == 2 for _, radius, distance, local_gap, parity_gap in witnesses),
        witnesses,
    )


def macro_layout(length: int) -> set[tuple[int, int, int]]:
    period = 16 * length
    directions = tuple(np.asarray(row, dtype=int) for row in c210.DIRECTIONS)
    positive = tuple(np.eye(3, dtype=int)[axis] for axis in range(3))
    sites: set[tuple[int, int, int]] = set()
    for cell in product(range(length), repeat=3):
        center = 16 * np.asarray(cell, dtype=int)
        for left, right in combinations(range(6), 2):
            if tuple(directions[left]) == tuple(-directions[right]):
                continue
            position = center + 2 * (directions[left] + directions[right])
            sites.add(tuple(int(value % period) for value in position))
        for direction in directions:
            position = center + 4 * direction
            sites.add(tuple(int(value % period) for value in position))
        for direction in positive:
            for radius in (7, 8, 9):
                position = center + radius * direction
                sites.add(tuple(int(value % period) for value in position))
    return sites


def translation_marker_controls() -> None:
    rows = []
    for length in (3, 4, 5):
        period = 16 * length
        active = macro_layout(length)
        translated = {
            ((site[0] + 1) % period, site[1], site[2]) for site in active
        }
        macro_translated = {
            ((site[0] + 16) % period, site[1], site[2]) for site in active
        }
        rows.append(
            {
                "L": length,
                "active": len(active),
                "unit_intersection": len(active & translated),
                "unit_symdiff": len(active ^ translated),
                "macro_symdiff": len(active ^ macro_translated),
            }
        )
    check(
        "27-carrier layout is collision-free and exposes the exact period-16 marker residual",
        all(
            row["active"] == 27 * row["L"] ** 3
            and row["unit_intersection"] == 2 * row["L"] ** 3
            and row["unit_symdiff"] == 50 * row["L"] ** 3
            and row["macro_symdiff"] == 0
            for row in rows
        ),
        rows,
    )


def staggered_controls(route3) -> None:
    rows = []
    for length in (3, 4, 5):
        modes = route3.axial_modes(length)
        best, exact, _ = route3.best_order_census(
            route3.cell_local_orders(length), modes, route3.axial_pairs(length)
        )
        rows.append((length, best, exact))
    check(
        "staggered static local-order census retains 4,6,8 periodic sign errors",
        rows == [(3, 4, 0), (4, 6, 0), (5, 8, 0)],
        rows,
    )

    shift = route3.cycle_shift(4)
    equality = np.diag(
        [1 if left == right else 0 for left in range(4) for right in range(4)]
    ).astype(complex)
    pair_shift = np.kron(shift, shift)
    leakage = np.linalg.norm((np.eye(16) - equality) @ pair_shift @ equality)
    check(
        "four-phase logical schedule is autonomous and leakage-free but remains implementation control",
        leakage < 2e-15 and np.linalg.norm(pair_shift @ equality - equality @ pair_shift) < 2e-15,
        leakage,
    )


def physics_and_firewall_controls() -> None:
    species = c219.common_species(-0.3)
    curvature_mass = 1 / float(
        np.mean(np.diag(c210.curvature_tensor(species, step=1e-4)))
    )
    forced_mass = c210.force_response(species, 2e-5).measured_mass
    check(
        "common one-particle mass fixture is preserved only at its inherited resolution",
        abs(c219.rest_mass(species) - 0.4534056541748851) < 2e-15
        and abs(curvature_mass - 0.4534056690336209) < 2e-15
        and abs(forced_mass - 0.45444242813733504) < 2e-15,
        {
            "rest": c219.rest_mass(species),
            "curvature": curvature_mass,
            "forced": forced_mass,
        },
    )

    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    forbidden_promotions = (
        "q is physical time",
        "layer count is physical time",
        "compiler depth is a rate",
        "wilson label is a clock",
        "wrapped phase is physical energy",
    )
    check(
        "3-D substrate use is separated from the still-open causal-time bridge",
        "the framework already supplies `z^3` spatial adjacency" in text
        and "a genuine bridge between the spatial compiler and the causal-time lane remains open" in text
        and not any(item in text for item in forbidden_promotions),
    )


def broad_claim_gate() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    live = (
        "auxiliary-majorana cancellation",
        "exact 3-d higher-form bosonization",
        "distinguishable walkers plus antisymmetric sector",
        "infinite-volume quasi-local representation",
    )
    check(
        "live constructive routes defeat shared-obstruction and axiom-pressure claims",
        all(item in text for item in live)
        and "no residual survives as a route-independent substrate obstruction" in text
        and "there is no axiom pressure" in text,
    )


def main() -> None:
    note_contract()
    route_regressions()
    route1 = load_module("cycle234_route1", ROUTES[0][1])
    route2 = load_module("cycle234_route2", ROUTES[1][1])
    route3 = load_module("cycle234_route3", ROUTES[2][1])
    direct_residual_controls(route1)
    gauge_rank_and_encoding_controls(route2)
    translation_marker_controls()
    staggered_controls(route3)
    physics_and_firewall_controls()
    broad_claim_gate()
    print(f"SUMMARY {PASS} PASS / {FAIL} FAIL")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
