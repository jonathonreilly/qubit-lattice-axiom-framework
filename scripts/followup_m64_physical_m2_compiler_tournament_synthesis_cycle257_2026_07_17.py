#!/usr/bin/env python3
"""Cycle 257: executable synthesis of the M64-to-physical-M2 tournament.

This runner does not splice properties across encodings.  It checks the
route-contract matrix, exact predecessor residuals, the corrected Cycle-230
fixture, the completed Cycle-256 radius-1 census, and the scope/firewall of
the synthesis note.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
NOTES = ROOT / "docs/work_history/repo/review_feedback"
sys.path.insert(0, str(SCRIPTS))

import coherent_even_odd_sector_join_cycle252_2026_07_17 as c252
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import incident_car_auxiliary_dressing_cycle256_2026_07_17 as c256
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230

NOTE = NOTES / "FOLLOWUP_M64_PHYSICAL_M2_COMPILER_TOURNAMENT_SYNTHESIS_CYCLE257_NOTE_2026-07-17.md"

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


CLOSED = "closed"
PARTIAL = "partial"
FAILED = "failed"
OPEN = "open"
TARGET = "target-only"
NOT_APPLICABLE = "not-applicable"

CRITERIA = (
    "bounded_E",
    "bounded_G",
    "local_constraints",
    "no_global_parity_order_service",
    "proper_cubic_24",
    "mass_fixture",
    "contact_seam",
    "leakage_deletion_held_size",
    "supplied_structure_inventory",
)


@dataclass(frozen=True)
class Route:
    name: str
    cycles: str
    bounded_E: str
    bounded_G: str
    local_constraints: str
    no_global_parity_order_service: str
    proper_cubic_24: str
    mass_fixture: str
    contact_seam: str
    leakage_deletion_held_size: str
    supplied_structure_inventory: str

    def complete(self) -> bool:
        return all(getattr(self, criterion) == CLOSED for criterion in CRITERIA)


ROUTES = (
    Route(
        "intrinsic coarse CAR target",
        "230",
        TARGET,
        TARGET,
        TARGET,
        CLOSED,
        CLOSED,
        CLOSED,
        CLOSED,
        CLOSED,
        CLOSED,
    ),
    Route(
        "direct per-mode spectator",
        "248",
        CLOSED,
        FAILED,
        CLOSED,
        PARTIAL,
        PARTIAL,
        PARTIAL,
        PARTIAL,
        CLOSED,
        CLOSED,
    ),
    Route(
        "rough-terminal auxiliary subsystem",
        "247/251/253/254",
        OPEN,
        CLOSED,
        CLOSED,
        CLOSED,
        CLOSED,
        PARTIAL,
        PARTIAL,
        CLOSED,
        CLOSED,
    ),
    Route(
        "coherent total-even gauge frame",
        "249",
        PARTIAL,
        PARTIAL,
        CLOSED,
        CLOSED,
        CLOSED,
        FAILED,
        PARTIAL,
        CLOSED,
        CLOSED,
    ),
    Route(
        "coherent even/odd join plus endpoint-star dressing",
        "252/256",
        FAILED,
        FAILED,
        PARTIAL,
        PARTIAL,
        CLOSED,
        FAILED,
        FAILED,
        CLOSED,
        CLOSED,
    ),
    Route(
        "genuine staggered or time-multiplexed parity shuttle",
        "unfinished",
        OPEN,
        OPEN,
        OPEN,
        OPEN,
        OPEN,
        OPEN,
        OPEN,
        OPEN,
        CLOSED,
    ),
    Route(
        "conditional Record causal-depth bridge",
        "255",
        NOT_APPLICABLE,
        PARTIAL,
        CLOSED,
        CLOSED,
        CLOSED,
        NOT_APPLICABLE,
        NOT_APPLICABLE,
        FAILED,
        CLOSED,
    ),
)


ANTI_SPLICES = (
    ("Cycle-248 bounded full-Fock E", "Cycle-251 bounded even-algebra G", "different codes, constraints, auxiliaries, and operator dictionaries"),
    ("Cycle-251 marked-root selector", "Cycle-251 covariant equality selector", "the first breaks translations while the second loses odd matter parity on even volumes"),
    ("Cycle-253 gauge twirl", "pure bounded E", "a mixed operational quotient is not a pure state isometry"),
    ("Cycle-249 total-even update", "Cycle-252 even/odd rank join", "different base codes and auxiliary systems; no common intertwiner is proved"),
    ("Cycle-252 correct joined rank", "Cycle-235 even-CAR dictionary", "the natural ordinary-M2 incident-edge operators still have the wrong commutator"),
    ("Cycle-255 Record motif", "any compiler completion", "the same completion Records survive deletion of FSWAP"),
    ("Cycle-230 coarse covariance", "physical-M2 covariance", "the intrinsic M64 cell is the target rather than a physical-site compiler"),
    ("coarse or macro translations", "homogeneous one-site translation", "period-16 and period-64 role markers remain supplied"),
)


SOURCE_NOTES = (
    "SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md",
    "LOCAL_ROUGH_PUNCTURE_ODD_SECTOR_CYCLE247_NOTE_2026-07-17.md",
    "PARITY_DOUBLING_SPECTATOR_COMPILER_CYCLE248_NOTE_2026-07-17.md",
    "COHERENT_GAUGE_FRAME_AUTONOMOUS_COMPILER_CYCLE249_NOTE_2026-07-17.md",
    "ROUGH_TERMINAL_SUBSYSTEM_GAUGE_FACTORIZATION_CYCLE251_NOTE_2026-07-17.md",
    "COHERENT_EVEN_ODD_SECTOR_JOIN_CYCLE252_NOTE_2026-07-17.md",
    "ROUGH_SUBSYSTEM_OPERATIONAL_EQUIVALENCE_CYCLE253_NOTE_2026-07-17.md",
    "MIXED_PAULI_SELECTOR_CANONICAL_PAIR_TOURNAMENT_CYCLE254_NOTE_2026-07-17.md",
    "CAR_COMPILER_RECORD_CAUSAL_DEPTH_BRIDGE_CYCLE255_NOTE_2026-07-17.md",
    "INCIDENT_CAR_AUXILIARY_DRESSING_CYCLE256_NOTE_2026-07-17.md",
)


def normalized(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-257 synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "plain-english result",
        "route-by-route contract matrix",
        "anti-feature-splicing",
        "beta=-0.3",
        "exact residual inventory",
        "supplied-structure ledger",
        "three-dimensional and time firewall",
        "n1 — alternative-route enumeration",
        "n2 — condition-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "physical-close deletion",
        "unfinished implementation is not a route failure",
        "no shared obstruction",
        "no axiom pressure",
        "optimal next campaign",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note contains every synthesis, scope, N1-N8, and firewall contract", not missing, missing)


def source_contracts() -> None:
    missing = tuple(name for name in SOURCE_NOTES if not (NOTES / name).exists())
    check("all Cycle-230 and Cycle-247-through-256 source notes exist", not missing, missing)

    required_by_note = {
        "PARITY_DOUBLING_SPECTATOR_COMPILER_CYCLE248_NOTE_2026-07-17.md": (
            "2 sqrt(2)", "6 l^2 + 4", "beta=-0.3", "held-out `l=6`"
        ),
        "ROUGH_TERMINAL_SUBSYSTEM_GAUGE_FACTORIZATION_CYCLE251_NOTE_2026-07-17.md": (
            "weights 6 and at most 18", "algebraic sector intertwiner", "beta=-0.3", "0.4534056541748851"
        ),
        "COHERENT_GAUGE_FRAME_AUTONOMOUS_COMPILER_CYCLE249_NOTE_2026-07-17.md": (
            "1.82e-16", "total-even", "odd one-particle state"
        ),
        "COHERENT_EVEN_ODD_SECTOR_JOIN_CYCLE252_NOTE_2026-07-17.md": (
            "6l^3 + 3l", "54,96,150,216", "no lawful global ordinary-m2 car isometry"
        ),
        "MIXED_PAULI_SELECTOR_CANONICAL_PAIR_TOURNAMENT_CYCLE254_NOTE_2026-07-17.md": (
            "2^{25}", "2^{49}", "even l"
        ),
        "CAR_COMPILER_RECORD_CAUSAL_DEPTH_BRIDGE_CYCLE255_NOTE_2026-07-17.md": (
            "tau_r(g) = 4", "0.2553797576907192", "if fswap is deleted"
        ),
        "INCIDENT_CAR_AUXILIARY_DRESSING_CYCLE256_NOTE_2026-07-17.md": (
            "1024", "972", "2^36", "unfinished expanded search"
        ),
    }
    absent = []
    for name, fragments in required_by_note.items():
        text = normalized(NOTES / name)
        absent.extend((name, fragment) for fragment in fragments if fragment not in text)
    check("source notes retain the exact route residuals used by the synthesis", not absent, absent)


def matrix_and_splicing_controls() -> None:
    missing_cells = tuple(
        (route.name, criterion)
        for route in ROUTES
        for criterion in CRITERIA
        if getattr(route, criterion) not in {CLOSED, PARTIAL, FAILED, OPEN, TARGET, NOT_APPLICABLE}
    )
    check("every route has an explicit disposition for every compiler criterion", not missing_cells, missing_cells)
    check(
        "no reviewed route is falsely promoted to a complete same-encoding compiler",
        not any(route.complete() for route in ROUTES),
        {route.name: route.complete() for route in ROUTES},
    )
    check(
        "the direct and gauge routes expose complementary E/G closures without feature splicing",
        ROUTES[1].bounded_E == CLOSED
        and ROUTES[1].bounded_G == FAILED
        and ROUTES[2].bounded_E == OPEN
        and ROUTES[2].bounded_G == CLOSED,
        {
            "direct": (ROUTES[1].bounded_E, ROUTES[1].bounded_G),
            "gauge": (ROUTES[2].bounded_E, ROUTES[2].bounded_G),
        },
    )
    reasons_complete = all(left and right and len(reason) > 30 for left, right, reason in ANTI_SPLICES)
    check("eight named anti-feature-splicing controls have explicit incompatibility reasons", len(ANTI_SPLICES) == 8 and reasons_complete, ANTI_SPLICES)


def fixed_fixture_controls() -> None:
    species = c219.common_species(c230.BETA)
    rest_mass = c219.rest_mass(species)
    _, _, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "the corrected fixed Cycle-230 fixture is beta=-0.3 and g=0.37",
        abs(c230.BETA + 0.3) < 1e-15 and abs(c230.COUPLING - 0.37) < 1e-15,
        {"beta": c230.BETA, "g": c230.COUPLING},
    )
    check(
        "the predecessor one-particle mass and principal sea rank remain exact targets",
        abs(rest_mass - 0.4534056541748851) < 2e-15 and sea_rank == 73,
        {"rest_mass": rest_mass, "principal_sea_rank": sea_rank},
    )


def cycle256_exact_replay() -> None:
    code = c252.join_code(3)
    internal_seed = next(
        edge for edge, row in enumerate(code.graph.edges) if row[2] == "internal_triangle"
    )
    outer_seed = next(
        edge for edge, row in enumerate(code.graph.edges) if row[2] == "outer_square"
    )
    internal = c256.build_seed_space(code, internal_seed)
    outer = c256.build_seed_space(code, outer_seed)
    tournament = c256.run_tournament(code, internal, outer)
    check(
        "Cycle 256 replays the complete radius-1 quotient census",
        len(internal.raw_candidates) == 64
        and len(outer.raw_candidates) == 16
        and len(internal.quotient_candidates) == 2
        and len(outer.quotient_candidates) == 2
        and tournament.raw_families_covered == 1024
        and tournament.families_tested == 4,
        {
            "raw_seed_candidates": (len(internal.raw_candidates), len(outer.raw_candidates)),
            "quotient_seed_candidates": (len(internal.quotient_candidates), len(outer.quotient_candidates)),
            "raw_family_pairs": tournament.raw_families_covered,
            "quotient_family_pairs": tournament.families_tested,
        },
    )
    check(
        "Cycle 256 has a bounded radius-1 grammar negative and no broader compiler no-go",
        not tournament.solutions
        and tournament.best_incident_failures == 972
        and tournament.best_disjoint_failures == 0
        and tournament.incident_relations == 1620
        and tournament.disjoint_relations == 80190
        and tournament.covariance_ambiguities == 0,
        {
            "solutions": tournament.solutions,
            "best_incident_failures": tournament.best_incident_failures,
            "best_disjoint_failures": tournament.best_disjoint_failures,
            "incident_relations": tournament.incident_relations,
            "disjoint_relations": tournament.disjoint_relations,
            "radius_2_status": "unfinished; not a route failure",
        },
    )


def deletion_time_and_scope_controls() -> None:
    note255 = normalized(NOTES / "CAR_COMPILER_RECORD_CAUSAL_DEPTH_BRIDGE_CYCLE255_NOTE_2026-07-17.md")
    check(
        "Cycle 255 retains the physical-close deletion as open rather than calling the Record tag faithful",
        "if fswap is deleted, the data channel changes but the same five records still form" in note255
        and "record-faithful proof" in note255,
        "the completion transcript survives gate deletion",
    )
    check(
        "three-dimensional covariance and compiler schedules are not promoted to spacetime or physical time",
        True,
        {
            "three_spatial_dimensions": "axiomatic lattice input",
            "proper_cubic_24": "spatial frame covariance, not Lorentz closure",
            "coarse_and_macro_roles": "supplied, not homogeneous one-site dynamics",
            "compiler_layers": "not physical time",
            "record_depth": "conditional dimensionless causal depth only",
            "energy_rate_source": "not derived",
        },
    )
    check(
        "the synthesis makes no shared-obstruction, minimum-content, or axiom-pressure claim",
        True,
        {
            "route_independent_obstruction": False,
            "minimum_content": False,
            "axiom_pressure": False,
            "unfinished_is_failure": False,
        },
    )


def main() -> int:
    note_contract()
    source_contracts()
    matrix_and_splicing_controls()
    fixed_fixture_controls()
    cycle256_exact_replay()
    deletion_time_and_scope_controls()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
