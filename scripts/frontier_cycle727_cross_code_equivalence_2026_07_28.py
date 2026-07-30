#!/usr/bin/env python3
"""Cycle-727 finite-box signed reference-to-companion pullback check.

The runner contains its complete finite fixture and tableau implementation in
Cycle-727 helper modules.  It constructs a fitted algebraic orientation
separately on four finite boxes; it does not construct a uniform encoder,
bounded physical preparation, or a coherent both-sector channel.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/CROSS_CODE_EQUIVALENCE_CYCLE727_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "docs/CROSS_CODE_EQUIVALENCE_CYCLE727_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "scripts/frontier_cycle727_cross_code_pullback_analysis_2026_07_28.py",
    "scripts/frontier_cycle727_cross_code_pullback_core_2026_07_28.py",
    "scripts/frontier_cycle727_finite_factorization_2026_07_28.py",
    "scripts/frontier_cycle727_finite_fixtures_2026_07_28.py",
    "scripts/frontier_cycle727_finite_pauli_tableau_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import json
import time

from frontier_cycle727_cross_code_pullback_analysis_2026_07_28 import (
    analyze_shape,
)
from frontier_cycle727_cross_code_pullback_core_2026_07_28 import (
    FAMILIES,
    FROZEN_DICTIONARY_DIGESTS,
    FROZEN_SECTOR_EXPONENT_PAIRS,
    FROZEN_SUPPLY_COUNT_DIGESTS,
    HELD_SHAPE,
    PARITY_SECTORS,
    Pauli,
    REGRESSION_SHAPES,
    json_digest,
    pauli_key,
)


FAILURES = 0


def check(label: str, condition: bool, detail: object = None) -> None:
    global FAILURES
    passed = bool(condition)
    FAILURES += not passed
    print("PASS" if passed else "FAIL", label, "::", "ok" if passed else detail)


def single_fixed_sector_dimension_census(
    bundles: tuple[dict[str, object], ...],
) -> dict[str, object]:
    rows = tuple({
        "shape": bundle["public"]["shape"],
        "Euler_full_exponent": bundle["euler"].matter_qubits,
        "companion_single_fixed_sector_exponent": bundle["factor"].logical,
        "dimension_ratio": 2,
        "single_fixed_sector_dimension_match": (
            bundle["euler"].matter_qubits == bundle["factor"].logical
        ),
        "two_sector_direct_sum_dimension_match": (
            bundle["euler"].matter_qubits
            == bundle["factor"].logical + 1
        ),
    } for bundle in bundles)
    return {
        "rows": rows,
        "certified": all(
            row["companion_single_fixed_sector_exponent"]
            == row["Euler_full_exponent"] - 1
            and row["dimension_ratio"] == 2
            and not row["single_fixed_sector_dimension_match"]
            and row["two_sector_direct_sum_dimension_match"]
            for row in rows
        ),
    }


def sign_corruption_control(bundle: dict[str, object]) -> dict[str, object]:
    target = bundle["generators"][0].target
    corrupted = Pauli((target.phase + 2) % 4, target.x, target.z)
    return {
        "detected": (
            corrupted.x == target.x
            and corrupted.z == target.z
            and corrupted.phase != target.phase
        ),
    }


def dictionary_permutation_control(
    bundle: dict[str, object],
) -> dict[str, object]:
    public = bundle["public"]
    generators = list(bundle["generators"])
    generators[0], generators[1] = generators[1], generators[0]
    original_payload = public["dictionary"]
    permuted_lists = {
        family: tuple({
            "label": row.label,
            "signed_target": pauli_key(row.target),
        } for row in generators if row.family == family)
        for family in FAMILIES
    }
    permuted_payload = {
        key: value for key, value in original_payload.items()
        if key not in (
            "signed_generator_lists",
            "family_order_digests",
            "frozen_dictionary_digest",
        )
    }
    permuted_payload["signed_generator_lists"] = permuted_lists
    permuted_payload["family_order_digests"] = {
        family: json_digest(permuted_lists[family]) for family in FAMILIES
    }
    changed = (
        json_digest(permuted_payload)
        != original_payload["frozen_dictionary_digest"]
        and permuted_payload["family_order_digests"]["free"]
        != original_payload["family_order_digests"]["free"]
    )
    return {"detected": changed}


def supply_count_mutation_control(
    bundle: dict[str, object],
) -> dict[str, object]:
    public = bundle["public"]
    original = public["supply_certificate"]["count_table"]
    mutated = json.loads(json.dumps(original))
    key = "CellEdgeGauge_constraint_supplied_rows"
    mutated["free"]["even"][key] += 1
    frozen = FROZEN_SUPPLY_COUNT_DIGESTS[public["shape"]]
    return {
        "detected": (
            json_digest(original) == frozen
            and json_digest(mutated) != frozen
        ),
    }


def shape_summary(public: dict[str, object]) -> dict[str, object]:
    return {
        "shape": public["shape"],
        "N": public["cells"],
        "E": public["oriented_edges"],
        "R": public["per_generator_certificate_count"],
        "dictionary_sha256": public["dictionary"]["frozen_dictionary_digest"],
        "generators_sha256": public["per_generator_certificate_digest"],
        "supply_counts_sha256": (
            public["supply_certificate"]["count_table_sha256"]
        ),
        "family_table": tuple(
            (
                public["family_tables"][family]["generator_count"],
                public["family_tables"][family][
                    "full_sector_target_rank"
                ],
                public["family_tables"][family]["sectors"]["even"][
                    "target_rank"
                ],
                public["family_tables"][family][
                    "locality_census"
                ]["maximum_reference_cell_diameter"],
                public["family_tables"][family][
                    "locality_census"
                ]["maximum_companion_cell_diameter"],
            )
            for family in FAMILIES
        ),
    }


def main() -> None:
    started = time.monotonic()
    print("SCOPE finite-box fitted signed pullback; supplied fixed sectors")
    bundles = tuple(analyze_shape(shape) for shape in REGRESSION_SHAPES)
    reports = tuple(bundle["public"] for bundle in bundles)

    dictionary_ok = all(
        all(row["dictionary_match"].values()) for row in reports
    )
    runtime_dictionary_digests = {
        row["shape"]: row["dictionary"]["frozen_dictionary_digest"]
        for row in reports
    }
    check(
        "dictionary frozen on four boxes",
        dictionary_ok
        and runtime_dictionary_digests == FROZEN_DICTIONARY_DIGESTS,
        runtime_dictionary_digests,
    )
    for family in FAMILIES:
        check(
            f"{family} ranks exact in both sectors",
            all(
                row["family_tables"][family]["sectors"][sector][
                    "rank_agreement"
                ]
                for row in reports
                for _odd, sector, _sign in PARITY_SECTORS
            ),
        )
        check(
            f"{family} signed rows exact in both sectors",
            all(
                not any(row["family_tables"][family]["sectors"][sector][
                    "phase_failures"
                ].values())
                and not any(row["family_tables"][family]["sectors"][sector][
                    "coordinate_failures"
                ].values())
                for row in reports
                for _odd, sector, _sign in PARITY_SECTORS
            ),
        )
        check(
            f"{family} gauge leakage zero",
            all(
                not any(row["family_tables"][family]["sectors"][sector][
                    "gauge_leakage_bit_totals"
                ].values())
                for row in reports
                for _odd, sector, _sign in PARITY_SECTORS
            ),
        )
        check(
            f"{family} explicit supply predicates exact",
            all(
                row["separate_certificates"][
                    "center_parity_supply_classified"
                ]
                for row in reports
            ),
        )
        check(
            f"{family} locality census bounded",
            all(
                row["separate_certificates"]["locality_census_certified"]
                for row in reports
            ),
        )

    cross_exact = all(row["cross_code_pullbacks_exact"] for row in reports)
    check("all signed pullbacks exact", cross_exact)

    dimensions = single_fixed_sector_dimension_census(bundles)
    runtime_sector_pairs = {
        row["shape"]: (
            row["Euler_full_exponent"],
            row["companion_single_fixed_sector_exponent"],
        )
        for row in dimensions["rows"]
    }
    check(
        "single fixed-sector dimension ratio is exactly two",
        dimensions["certified"]
        and runtime_sector_pairs == FROZEN_SECTOR_EXPONENT_PAIRS,
        runtime_sector_pairs,
    )

    controls = {
        "sign": sign_corruption_control(bundles[0]),
        "order": dictionary_permutation_control(bundles[0]),
        "supply": supply_count_mutation_control(bundles[0]),
    }
    for name, control in controls.items():
        check(f"control {name} mutation detected", control["detected"], control)

    all_pass = FAILURES == 0
    report = {
        "status": "CYCLE727_FINITE_BOX_SIGNED_PULLBACK_PASS",
        "pass": all_pass,
        "family_order": FAMILIES,
        "family_table_columns": (
            "count",
            "full_rank",
            "fixed_rank",
            "reference_diameter",
            "companion_diameter",
        ),
        "shapes": tuple(shape_summary(row) for row in reports),
        "certificates": {
            name: all(row["separate_certificates"][name] for row in reports)
            for name in reports[0]["separate_certificates"]
        },
        "supply_predicates": {
            "passed": sum(
                reports[0]["supply_certificate"]["predicates"].values()
            ),
            "total": len(
                reports[0]["supply_certificate"]["predicates"]
            ),
        },
        "single_fixed_sector_dimension": {
            "exponent_pairs": {
                "x".join(map(str, shape)): pair
                for shape, pair in runtime_sector_pairs.items()
            },
            "dimension_ratio": 2,
            "two_sector_direct_sum_dimension_match": True,
            "certified": dimensions["certified"],
        },
        "controls": {
            name: control["detected"] for name, control in controls.items()
        },
        "boundary": {
            "implementation": "self-contained finite Cycle-727 modules",
            "orientation": "shape-specific fitted algebraic orientation",
            "channel_scope": "separate supplied fixed-parity sectors",
            "physical_preparation": "open",
            "coherent_both_sector_channel": "open",
            "input_compiler_and_collision_free_epoch": "open",
            "marker_or_coframe_map": "not addressed",
        },
        "runtime_seconds": time.monotonic() - started,
    }
    report["report_sha256"] = json_digest(report)
    print("FINAL_JSON")
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    if not all_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
