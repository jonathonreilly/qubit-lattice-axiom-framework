#!/usr/bin/env python3
"""Independent reconstruction of the finite packet-count vector comparison.

This checker parses the primary's literal projection tables but never imports
or calls the primary module.  It rebuilds the landed packet schedules and
recomputes both vectors and raw constraint residuals directly.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
PRIMARY_PATH = (
    "scripts/frontier_companion_bank_packet_count_tensor_projection_"
    "constraint_membership_2026_07_28.py"
)
NOTE_PATH = (
    "docs/COMPANION_BANK_PACKET_COUNT_TENSOR_PROJECTION_CONSTRAINT_"
    "MEMBERSHIP_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_companion_bank_packet_count_tensor_projection_"
    "constraint_membership_2026_07_28.py",
    "scripts/frontier_companion_bank_liveness_endpoint_interval_packet_projection_2026_07_28.py",
    "scripts/signed_gravity_oriented_tensor_source_lift.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
from time import perf_counter

import numpy as np

import frontier_companion_bank_liveness_endpoint_interval_packet_projection_2026_07_28 as PACKET
import signed_gravity_oriented_tensor_source_lift as S1


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_MODULE = (
    "frontier_companion_bank_packet_count_tensor_projection_"
    "constraint_membership_2026_07_28"
)
DEPENDENCY_PATHS = AUDIT_INPUT_PATHS[1:]
EXPECTED_STAGE_VECTOR = np.array(
    [225, 9, 112, 17304, 24, 225, 18, 0, 17304, 24],
    dtype=float,
)
EXPECTED_READ_COUNT = 24
TOL = 1.0e-9


def literal_assignment(tree: ast.Module, name: str) -> object:
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise AssertionError(f"missing literal assignment {name}")


def parse_primary_contract() -> dict[str, object]:
    source = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_PATH)
    imported_roots = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    imported_roots.update(
        node.module
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module
    )
    allowed_science_imports = {
        (
            "frontier_companion_bank_liveness_endpoint_interval_packet_"
            "projection_2026_07_28"
        ),
        "signed_gravity_oriented_tensor_source_lift",
    }
    repo_science_imports = {
        name
        for name in imported_roots
        if name.startswith(
            (
                "frontier_",
                "physical_",
                "signed_gravity_",
                "two_cell_",
                "unit_weight_",
            )
        )
    }
    return {
        "fixture_table": literal_assignment(
            tree, "FIXTURE_PROJECTION_TABLE"
        ),
        "stage_table": literal_assignment(
            tree, "STAGE_SLOT_PROJECTION_TABLE"
        ),
        "frozen_stage_vector": literal_assignment(
            tree, "FROZEN_STAGE_SLOT_VECTOR"
        ),
        "primary_imported": PRIMARY_MODULE in imported_roots,
        "unexpected_science_imports": sorted(
            repo_science_imports - allowed_science_imports
        ),
        "primary_sha256": sha256(source.encode()).hexdigest(),
    }


def landed_dependency_pins() -> dict[str, object]:
    rows = {}
    for relative in DEPENDENCY_PATHS:
        observed = (ROOT / relative).read_bytes()
        landed = subprocess.run(
            ["git", "-C", str(ROOT), "show", f"HEAD:{relative}"],
            capture_output=True,
            check=False,
        )
        rows[relative] = {
            "observed_sha256": sha256(observed).hexdigest(),
            "HEAD_sha256": (
                sha256(landed.stdout).hexdigest()
                if landed.returncode == 0
                else None
            ),
            "pass": (
                landed.returncode == 0
                and sha256(observed).hexdigest()
                == sha256(landed.stdout).hexdigest()
            ),
        }
    rows["pass"] = all(
        bool(row["pass"])
        for row in rows.values()
        if isinstance(row, dict)
    )
    return rows


def build_independent_counts() -> dict[str, object]:
    atlas = PACKET.EPOCH.P.build_private_atlases()
    primary = PACKET.EPOCH.build_epoch((2, 2, 2), "primary", atlas)
    alternate = PACKET.EPOCH.build_epoch(
        (2, 2, 2),
        "alternate_port",
        atlas,
        recurrent_override=primary.recurrent,
    )
    bundles = {"primary": primary, "alternate_port": alternate}
    result = {}
    for variant, bundle in bundles.items():
        extension = PACKET.extend_and_walk(bundle)
        counts = {}
        source_boundaries = {}
        for source in extension["sources"]:
            register = int(source["register"])
            field = str(source["field"])
            count = 0
            for slot in extension["slots"]:
                if slot.stage != "E":
                    continue
                for word in slot.words:
                    if word.accesses.get(register) == (field, "read"):
                        count += 1
            counts[field] = count
            source_boundaries[field] = {
                "static_predicate_value": int(source["value"]),
                "liveness_witness_valid": bool(
                    source["liveness_witness"]["valid"]
                ),
            }
        result[variant] = {
            "lawful": bool(extension["lawful"]),
            "sources_clean": bool(extension["sources_clean"]),
            "declared_packet_rows": len(extension["table"]),
            "declared_read_counts": counts,
            "stage_slot_counts": {
                stage: sum(
                    int(slot.stage == stage)
                    for slot in extension["slots"]
                )
                for stage in ("A", "B", "C", "D", "E")
            },
            "source_boundaries": source_boundaries,
            "collision_count": int(extension["walk"]["collision_count"]),
            "violation_count": int(extension["walk"]["violation_count"]),
        }
    return result


def reconstruct_vectors(
    contract: dict[str, object],
    counts: dict[str, object],
    canonical_fixture: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    fixture_vector = np.zeros(10, dtype=float)
    for row in contract["fixture_table"]:
        slot = int(row["slot"])
        variant = str(row["variant"])
        field = str(row["packet_field"])
        fixture_vector[slot] = (
            int(counts[variant]["declared_read_counts"][field])
            * float(canonical_fixture[slot])
        )

    stage_vector = np.zeros(10, dtype=float)
    for row in contract["stage_table"]:
        slot = int(row["slot"])
        variant = str(row["variant"])
        stage = str(row["stage"])
        stage_vector[slot] = float(
            counts[variant]["stage_slot_counts"][stage]
        )
    return fixture_vector, stage_vector


def main() -> int:
    started = perf_counter()
    checks: list[dict[str, object]] = []

    def check(label: str, condition: bool, detail: object = "") -> bool:
        passed = bool(condition)
        checks.append({"label": label, "pass": passed, "detail": detail})
        print(
            "PASS" if passed else "FAIL",
            label,
            "::",
            json.dumps(detail, sort_keys=True, default=str),
        )
        return passed

    contract = parse_primary_contract()
    blocklist_gate = (
        not contract["primary_imported"]
        and PRIMARY_MODULE not in sys.modules
        and not contract["unexpected_science_imports"]
    )
    check(
        (
            "the checker blocks the primary module and allows only the two "
            "declared science imports"
        ),
        blocklist_gate,
        {
            "primary_imported": contract["primary_imported"],
            "primary_in_sys_modules": PRIMARY_MODULE in sys.modules,
            "unexpected_science_imports": (
                contract["unexpected_science_imports"]
            ),
        },
    )

    pins = landed_dependency_pins()
    check(
        "the independently imported landed dependencies equal current HEAD bytes",
        pins["pass"],
        {
            path: row["observed_sha256"]
            for path, row in pins.items()
            if isinstance(row, dict)
        },
    )

    counts = build_independent_counts()
    count_gate = all(
        counts[variant]["lawful"]
        and counts[variant]["sources_clean"]
        and counts[variant]["declared_packet_rows"] == EXPECTED_READ_COUNT
        and counts[variant]["collision_count"] == 0
        and counts[variant]["violation_count"] == 0
        and all(
            value == EXPECTED_READ_COUNT
            for value in counts[variant]["declared_read_counts"].values()
        )
        and all(
            row["static_predicate_value"] == 1
            and row["liveness_witness_valid"]
            for row in counts[variant]["source_boundaries"].values()
        )
        for variant in ("primary", "alternate_port")
    )
    check(
        "an independent slot walk reconstructs both clean 24-row declaration surfaces",
        count_gate,
        {
            variant: {
                "reads": counts[variant]["declared_read_counts"],
                "stages": counts[variant]["stage_slot_counts"],
            }
            for variant in ("primary", "alternate_port")
        },
    )

    table_gate = (
        len(contract["fixture_table"]) == 10
        and len(contract["stage_table"]) == 10
        and {
            int(row["slot"]) for row in contract["fixture_table"]
        }
        == set(range(10))
        and {
            int(row["slot"]) for row in contract["stage_table"]
        }
        == set(range(10))
        and tuple(contract["frozen_stage_vector"])
        == tuple(int(value) for value in EXPECTED_STAGE_VECTOR)
    )
    check(
        "both parsed projection tables assign each tensor coordinate exactly once",
        table_gate,
        {
            "fixture_rows": len(contract["fixture_table"]),
            "stage_rows": len(contract["stage_table"]),
            "frozen_stage_vector": contract["frozen_stage_vector"],
        },
    )

    canonical_fixture, constraint = S1.tensor_source_with_constraints()
    fixture_vector, stage_vector = reconstruct_vectors(
        contract, counts, canonical_fixture
    )
    fixture_residual = float(np.linalg.norm(constraint @ fixture_vector))
    fixture_gate = (
        np.array_equal(
            fixture_vector,
            EXPECTED_READ_COUNT * canonical_fixture,
        )
        and fixture_residual < TOL
    )
    check(
        "raw reconstruction gives the exact homogeneous fixture vector and nullspace residual",
        fixture_gate,
        {
            "scale": EXPECTED_READ_COUNT,
            "residual_norm": fixture_residual,
        },
    )

    best_scale = float(
        np.dot(canonical_fixture, stage_vector)
        / np.dot(canonical_fixture, canonical_fixture)
    )
    nonproportional_residual = float(
        np.linalg.norm(stage_vector - best_scale * canonical_fixture)
    )
    stage_residual = float(np.linalg.norm(constraint @ stage_vector))
    stage_gate = (
        np.array_equal(stage_vector, EXPECTED_STAGE_VECTOR)
        and nonproportional_residual > TOL
        and stage_residual > TOL
    )
    check(
        (
            "raw reconstruction gives the frozen nonproportional stage "
            "vector outside the constraint nullspace"
        ),
        stage_gate,
        {
            "vector": stage_vector.tolist(),
            "least_squares_scale": best_scale,
            "nonproportional_residual": nonproportional_residual,
            "constraint_residual_norm": stage_residual,
        },
    )

    altered = fixture_vector.copy()
    altered[0] = stage_vector[0]
    altered_residual = float(np.linalg.norm(constraint @ altered))
    control_gate = (
        altered_residual > TOL
        and abs(altered_residual - fixture_residual) > TOL
    )
    check(
        "the independent altered-coordinate control changes the raw residual",
        control_gate,
        {
            "original_residual_norm": fixture_residual,
            "altered_residual_norm": altered_residual,
        },
    )

    passing = all(row["pass"] for row in checks)
    report = {
        "status": "PASS" if passing else "FAIL",
        "checks": checks,
        "primary_contract_sha256": contract["primary_sha256"],
        "dependency_byte_pins": pins,
        "independent_counts": counts,
        "raw_reconstruction": {
            "fixture_vector": fixture_vector.tolist(),
            "fixture_constraint_residual_norm": fixture_residual,
            "stage_vector": stage_vector.tolist(),
            "stage_constraint_residual_norm": stage_residual,
            "stage_nonproportional_residual_norm": (
                nonproportional_residual
            ),
        },
        "boundary": (
            "Finite algebra under supplied projections and the generic S1 "
            "matrix only; no register-state, physical source, source law, "
            "Ward identity, composite channel, or no-go claim is derived."
        ),
        "runtime_seconds": perf_counter() - started,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if not passing:
        raise SystemExit(1)
    print(
        "FINAL_TAG: "
        "COMPANION_BANK_PACKET_COUNT_TENSOR_PROJECTION_INDEPENDENT_PASS"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
