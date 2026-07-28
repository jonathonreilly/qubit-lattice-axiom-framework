#!/usr/bin/env python3
"""Finite packet-count projections into the supplied S1 tensor coordinates.

The landed companion-bank packet runner supplies a Stage-E schedule, static
predicate values, and liveness witnesses.  It does not supply register-state
values.  This runner counts declared Stage-E reads and schedule slots, applies
two explicit count-to-vector conventions, and evaluates those vectors against
the generic deterministic constraint matrix returned by the existing S1
fixture generator.

The calculation is a conditional algebraic comparison.  It does not derive a
physical tensor source, a source law, a compiler, or a packet-driven channel.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/COMPANION_BANK_PACKET_COUNT_TENSOR_PROJECTION_CONSTRAINT_"
    "MEMBERSHIP_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_companion_bank_liveness_endpoint_interval_packet_projection_2026_07_28.py",
    "scripts/signed_gravity_oriented_tensor_source_lift.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from hashlib import sha256
import json
from pathlib import Path
import subprocess
from time import perf_counter

import numpy as np

import frontier_companion_bank_liveness_endpoint_interval_packet_projection_2026_07_28 as PACKET
import signed_gravity_oriented_tensor_source_lift as S1


ROOT = Path(__file__).resolve().parents[1]
SHAPE = (2, 2, 2)
VARIANTS = ("primary", "alternate_port")
STAGES = ("A", "B", "C", "D", "E")
PACKET_FIELDS = (
    "certificate",
    "binder",
    "actuality",
    "admissibility",
    "law_domain",
)
EXPECTED_DECLARED_READ_COUNT = 24
CONSTRAINT_TOL = 1.0e-9

# Supplied coordinate convention.  Each Stage-E declared read count multiplies
# the corresponding coordinate of S1's deterministic canonical fixture.
FIXTURE_PROJECTION_TABLE = (
    {"slot": 0, "variant": "primary", "packet_field": "certificate"},
    {"slot": 1, "variant": "primary", "packet_field": "binder"},
    {"slot": 2, "variant": "primary", "packet_field": "actuality"},
    {"slot": 3, "variant": "primary", "packet_field": "admissibility"},
    {"slot": 4, "variant": "primary", "packet_field": "law_domain"},
    {"slot": 5, "variant": "alternate_port", "packet_field": "certificate"},
    {"slot": 6, "variant": "alternate_port", "packet_field": "binder"},
    {"slot": 7, "variant": "alternate_port", "packet_field": "actuality"},
    {"slot": 8, "variant": "alternate_port", "packet_field": "admissibility"},
    {"slot": 9, "variant": "alternate_port", "packet_field": "law_domain"},
)

# Second supplied convention.  The ten extended-schedule slot counts are
# assigned, in this literal order, to the ten S1 fixture coordinates.
STAGE_SLOT_PROJECTION_TABLE = (
    {"slot": 0, "variant": "primary", "stage": "A"},
    {"slot": 1, "variant": "primary", "stage": "B"},
    {"slot": 2, "variant": "primary", "stage": "C"},
    {"slot": 3, "variant": "primary", "stage": "D"},
    {"slot": 4, "variant": "primary", "stage": "E"},
    {"slot": 5, "variant": "alternate_port", "stage": "A"},
    {"slot": 6, "variant": "alternate_port", "stage": "B"},
    {"slot": 7, "variant": "alternate_port", "stage": "C"},
    {"slot": 8, "variant": "alternate_port", "stage": "D"},
    {"slot": 9, "variant": "alternate_port", "stage": "E"},
)
FROZEN_STAGE_SLOT_VECTOR = (
    225,
    9,
    112,
    17304,
    24,
    225,
    18,
    0,
    17304,
    24,
)


def array_certificate(array: np.ndarray) -> dict[str, object]:
    contiguous = np.ascontiguousarray(array)
    return {
        "dtype": contiguous.dtype.str,
        "shape": list(contiguous.shape),
        "sha256": sha256(contiguous.tobytes(order="C")).hexdigest(),
    }


def dependency_byte_pins() -> dict[str, object]:
    """Pin the two imported landed modules to the current HEAD bytes."""
    rows: dict[str, object] = {}
    for relative in AUDIT_INPUT_PATHS:
        observed_bytes = (ROOT / relative).read_bytes()
        landed = subprocess.run(
            ["git", "-C", str(ROOT), "show", f"HEAD:{relative}"],
            capture_output=True,
            check=False,
        )
        observed = sha256(observed_bytes).hexdigest()
        expected = (
            sha256(landed.stdout).hexdigest()
            if landed.returncode == 0
            else None
        )
        rows[relative] = {
            "observed_sha256": observed,
            "HEAD_sha256": expected,
            "git_show_returncode": landed.returncode,
            "pass": landed.returncode == 0 and observed == expected,
        }
    rows["pass"] = all(
        bool(row["pass"])
        for row in rows.values()
        if isinstance(row, dict)
    )
    return rows


def declared_stage_e_read_count(
    extension: dict[str, object],
    source: dict[str, object],
) -> int:
    """Count declared reads; do not interpret them as register-state values."""
    register = int(source["register"])
    field = str(source["field"])
    count = 0
    for slot in extension["slots"]:
        if slot.stage != "E":
            continue
        for word in slot.words:
            role_mode = word.accesses.get(register)
            if role_mode == (field, "read"):
                count += 1
    return count


def build_packet_views() -> dict[str, object]:
    """Build the two held parent variants once and census schedule declarations."""
    atlas = PACKET.EPOCH.P.build_private_atlases()
    primary = PACKET.EPOCH.build_epoch(SHAPE, "primary", atlas)
    alternate = PACKET.EPOCH.build_epoch(
        SHAPE,
        "alternate_port",
        atlas,
        recurrent_override=primary.recurrent,
    )
    bundles = {"primary": primary, "alternate_port": alternate}
    views: dict[str, object] = {}
    for variant in VARIANTS:
        extension = PACKET.extend_and_walk(bundles[variant])
        role_counts = {
            str(source["field"]): declared_stage_e_read_count(
                extension, source
            )
            for source in extension["sources"]
        }
        sources = {
            str(source["field"]): {
                "register": int(source["register"]),
                "register_role": str(source["register_role"]),
                "static_predicate_value": int(source["value"]),
                "liveness_witness_valid": bool(
                    source["liveness_witness"]["valid"]
                ),
                "value_semantics": str(source["value_semantics"]),
            }
            for source in extension["sources"]
        }
        stage_slot_counts = {
            stage: sum(
                int(slot.stage == stage) for slot in extension["slots"]
            )
            for stage in STAGES
        }
        walk = extension["walk"]
        views[variant] = {
            "shape": list(SHAPE),
            "extension_lawful": bool(extension["lawful"]),
            "sources_clean": bool(extension["sources_clean"]),
            "declared_packet_rows": len(extension["table"]),
            "declared_stage_e_read_counts": role_counts,
            "stage_slot_counts": stage_slot_counts,
            "sources": sources,
            "walk": {
                "slots_walked": int(walk["slots_walked"]),
                "handoffs_declared": int(walk["handoffs_declared"]),
                "handoffs_consumed": int(walk["handoffs_consumed"]),
                "collision_count": int(walk["collision_count"]),
                "violation_count": int(walk["violation_count"]),
            },
        }
    return views


def fixture_scaled_projection(
    views: dict[str, object],
    canonical_fixture: np.ndarray,
) -> tuple[np.ndarray, list[dict[str, object]]]:
    vector = np.zeros(10, dtype=float)
    rows = []
    for assignment in FIXTURE_PROJECTION_TABLE:
        slot = int(assignment["slot"])
        variant = str(assignment["variant"])
        field = str(assignment["packet_field"])
        count = int(
            views[variant]["declared_stage_e_read_counts"][field]
        )
        coefficient = float(canonical_fixture[slot])
        vector[slot] = count * coefficient
        rows.append({
            **assignment,
            "declared_read_count": count,
            "canonical_fixture_coefficient": coefficient,
            "projected_coordinate": float(vector[slot]),
        })
    return vector, rows


def stage_slot_projection(
    views: dict[str, object],
) -> tuple[np.ndarray, list[dict[str, object]]]:
    vector = np.zeros(10, dtype=float)
    rows = []
    for assignment in STAGE_SLOT_PROJECTION_TABLE:
        slot = int(assignment["slot"])
        variant = str(assignment["variant"])
        stage = str(assignment["stage"])
        count = int(views[variant]["stage_slot_counts"][stage])
        vector[slot] = float(count)
        rows.append({
            **assignment,
            "slot_count": count,
            "projected_coordinate": float(vector[slot]),
        })
    return vector, rows


def constraint_certificate(
    vector: np.ndarray,
    constraint: np.ndarray,
) -> dict[str, object]:
    residuals = {
        "+1": float(np.linalg.norm(constraint @ vector)),
        "-1": float(np.linalg.norm(constraint @ (-vector))),
        "0": float(np.linalg.norm(constraint @ np.zeros_like(vector))),
    }
    return {
        "constraint_shape": list(constraint.shape),
        "constraint_sha256": array_certificate(constraint)["sha256"],
        "residual_norms": residuals,
        "in_numeric_nullspace": bool(
            max(residuals.values()) < CONSTRAINT_TOL
        ),
        "tolerance": CONSTRAINT_TOL,
    }


def nonproportionality_certificate(
    vector: np.ndarray,
    canonical_fixture: np.ndarray,
) -> dict[str, object]:
    scale = float(
        np.dot(canonical_fixture, vector)
        / np.dot(canonical_fixture, canonical_fixture)
    )
    residual = float(
        np.linalg.norm(vector - scale * canonical_fixture)
    )
    relative = residual / max(float(np.linalg.norm(vector)), S1.TOL)
    ratios = vector / canonical_fixture
    return {
        "least_squares_scale": scale,
        "residual_norm": residual,
        "relative_residual": relative,
        "coordinate_ratio_min": float(np.min(ratios)),
        "coordinate_ratio_max": float(np.max(ratios)),
        "coordinate_ratio_spread": float(np.ptp(ratios)),
        "numerically_nonproportional": bool(relative > 1.0e-10),
    }


def altered_coordinate_control(
    fixture_vector: np.ndarray,
    constraint: np.ndarray,
) -> dict[str, object]:
    altered = fixture_vector.copy()
    altered[0] = float(FROZEN_STAGE_SLOT_VECTOR[0])
    original = float(np.linalg.norm(constraint @ fixture_vector))
    altered_residual = float(np.linalg.norm(constraint @ altered))
    return {
        "alteration": (
            "replace coordinate 0 of the fixture-scaled vector with the "
            "primary Stage-A slot count"
        ),
        "original_residual_norm": original,
        "altered_residual_norm": altered_residual,
        "detected": bool(
            altered_residual > CONSTRAINT_TOL
            and abs(altered_residual - original) > CONSTRAINT_TOL
        ),
        "altered_vector_certificate": array_certificate(altered),
    }


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

    pins = dependency_byte_pins()
    check(
        "the two imported dependency modules equal their current HEAD bytes",
        pins["pass"],
        {
            path: row["observed_sha256"]
            for path, row in pins.items()
            if isinstance(row, dict)
        },
    )

    views = build_packet_views()
    parent_clean = all(
        views[variant]["extension_lawful"]
        and views[variant]["sources_clean"]
        and views[variant]["walk"]["collision_count"] == 0
        and views[variant]["walk"]["violation_count"] == 0
        and all(
            row["liveness_witness_valid"]
            and row["static_predicate_value"] == 1
            for row in views[variant]["sources"].values()
        )
        for variant in VARIANTS
    )
    check(
        "both held parent extensions preserve static-predicate and liveness boundaries",
        parent_clean,
        {
            variant: {
                "lawful": views[variant]["extension_lawful"],
                "sources_clean": views[variant]["sources_clean"],
                "walk": views[variant]["walk"],
            }
            for variant in VARIANTS
        },
    )

    count_gate = all(
        views[variant]["declared_packet_rows"]
        == EXPECTED_DECLARED_READ_COUNT
        and all(
            views[variant]["declared_stage_e_read_counts"][field]
            == EXPECTED_DECLARED_READ_COUNT
            for field in PACKET_FIELDS
        )
        for variant in VARIANTS
    )
    check(
        "each supplied packet role has exactly 24 declared Stage-E reads in each variant",
        count_gate,
        {
            variant: views[variant]["declared_stage_e_read_counts"]
            for variant in VARIANTS
        },
    )

    canonical_fixture, constraint = S1.tensor_source_with_constraints()
    fixture_vector, fixture_rows = fixture_scaled_projection(
        views, canonical_fixture
    )
    fixture_identity = bool(
        np.array_equal(
            fixture_vector,
            EXPECTED_DECLARED_READ_COUNT * canonical_fixture,
        )
    )
    check(
        "the first supplied projection is exactly 24 times the S1 canonical fixture",
        fixture_identity,
        {
            "scale": EXPECTED_DECLARED_READ_COUNT,
            "vector_sha256": array_certificate(fixture_vector)["sha256"],
        },
    )

    fixture_constraint = constraint_certificate(fixture_vector, constraint)
    check(
        "the fixture-scaled vector is numerically in the supplied S1 constraint nullspace",
        fixture_constraint["in_numeric_nullspace"],
        fixture_constraint,
    )

    stage_vector, stage_rows = stage_slot_projection(views)
    stage_frozen = tuple(int(value) for value in stage_vector) == (
        FROZEN_STAGE_SLOT_VECTOR
    )
    stage_assignment_complete = (
        len(stage_rows) == 10
        and {int(row["slot"]) for row in stage_rows} == set(range(10))
    )
    check(
        "the second supplied projection reproduces the ten frozen extended-schedule slot counts",
        stage_frozen and stage_assignment_complete,
        {"vector": stage_vector.tolist(), "assignment_rows": len(stage_rows)},
    )

    nonproportional = nonproportionality_certificate(
        stage_vector, canonical_fixture
    )
    check(
        "the stage-slot vector is not a scalar multiple of the S1 canonical fixture",
        nonproportional["numerically_nonproportional"],
        nonproportional,
    )

    stage_constraint = constraint_certificate(stage_vector, constraint)
    check(
        (
            "the stage-slot vector is outside the supplied S1 constraint "
            "nullspace at the frozen tolerance"
        ),
        not stage_constraint["in_numeric_nullspace"],
        stage_constraint,
    )

    sign_identity = (
        abs(
            stage_constraint["residual_norms"]["+1"]
            - stage_constraint["residual_norms"]["-1"]
        )
        < CONSTRAINT_TOL
        and stage_constraint["residual_norms"]["0"] == 0.0
        and abs(
            fixture_constraint["residual_norms"]["+1"]
            - fixture_constraint["residual_norms"]["-1"]
        )
        < CONSTRAINT_TOL
        and fixture_constraint["residual_norms"]["0"] == 0.0
    )
    check(
        (
            "orientation sign changes preserve each residual norm and "
            "orientation zero annihilates each vector"
        ),
        sign_identity,
        {
            "fixture": fixture_constraint["residual_norms"],
            "stage_slot": stage_constraint["residual_norms"],
        },
    )

    control = altered_coordinate_control(fixture_vector, constraint)
    check(
        "an altered fixture-scaled coordinate is detected by the raw constraint residual",
        control["detected"],
        control,
    )

    passing = all(row["pass"] for row in checks)
    report = {
        "status": "PASS" if passing else "FAIL",
        "claim_type": "bounded_theorem",
        "authority": "none",
        "audit": "unset",
        "retention_disposition": "bounded_support",
        "checks": checks,
        "dependency_byte_pins": pins,
        "parent_packet_schedule_views": views,
        "projections": {
            "fixture_scaled": {
                "convention": (
                    "Each declared Stage-E role-read count multiplies the "
                    "matching coordinate of S1's canonical fixture."
                ),
                "assignment_table": fixture_rows,
                "vector": fixture_vector.tolist(),
                "vector_certificate": array_certificate(fixture_vector),
                "exact_scalar_multiple": fixture_identity,
                "constraint": fixture_constraint,
            },
            "stage_slot_count": {
                "convention": (
                    "The ten primary/alternate Stage-A..E slot counts are "
                    "assigned in listed order to the ten S1 coordinates."
                ),
                "assignment_table": stage_rows,
                "vector": stage_vector.tolist(),
                "vector_certificate": array_certificate(stage_vector),
                "nonproportionality": nonproportional,
                "constraint": stage_constraint,
            },
        },
        "constraint_origin": (
            "The deterministic generic 4x10 matrix returned by "
            "S1.tensor_source_with_constraints(); it is imported as a "
            "supplied fixture and is not derived here from a Ward identity."
        ),
        "control": control,
        "derived": [
            "literal Stage-E declared-read counts and extended-schedule slot counts",
            "the two vectors under the two explicit coordinate assignments",
            "raw finite residual norms against the supplied S1 matrix",
        ],
        "supplied": [
            "the landed packet schedule and its static-predicate/liveness conventions",
            "both count-to-coordinate assignment tables",
            "the S1 deterministic fixture, generic constraint matrix, and numerical tolerance",
        ],
        "not_tested": [
            "register-state readout or a reversible packet encoder",
            "a composite channel or packet feed to JointOrder",
            (
                "a physical tensor source, source law, Ward identity, "
                "gravity identification, or Born content"
            ),
            "selection or classification of physically admissible packet projections",
        ],
        "boundary_flags": {
            "register_state_readout_verified": False,
            "reversible_packet_encoder_verified": False,
            "composite_channel_verified": False,
            "joint_order_packet_feed_verified": False,
            "physical_source_character_derived": False,
            "source_law_selected": False,
            "ward_identity_derived": False,
            "no_go_claimed": False,
        },
        "runtime_seconds": perf_counter() - started,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if not passing:
        raise SystemExit(1)
    print(
        "FINAL_TAG: "
        "COMPANION_BANK_PACKET_COUNT_TENSOR_PROJECTION_FINITE_COMPARISON"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
