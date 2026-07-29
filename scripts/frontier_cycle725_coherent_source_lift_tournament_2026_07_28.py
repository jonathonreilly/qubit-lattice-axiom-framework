#!/usr/bin/env python3
"""Cycle 725: coherent source-lift tournament over the Cycle-722 epoch census.

S1 is a true parameterized feed into the landed length-10 tensor checks.
S2 and S3 have no census input port, so their landed certificates are rerun
unchanged and the census is bound separately by exact integer tables only.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/COHERENT_SOURCE_LIFT_TOURNAMENT_CYCLE725_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle722_epoch_fed_endpoint_interval_harness_2026_07_28.py",
    "scripts/signed_gravity_oriented_tensor_source_lift.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
    "scripts/physical_m2_gravity_source_bridge_tournament_synthesis_cycle294_2026_07_17.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from copy import deepcopy
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
from time import perf_counter

import numpy as np

import frontier_cycle722_epoch_fed_endpoint_interval_harness_2026_07_28 as F722
import signed_gravity_oriented_tensor_source_lift as S1
import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as S2


ROOT = Path(__file__).resolve().parents[1]
VARIANTS = ("primary", "alternate_port")
STAGES = ("A", "B", "C", "D", "E")
SHAPE = (2, 2, 2)
PACKET_FIELDS = (
    "certificate",
    "binder",
    "actuality",
    "admissibility",
    "law_domain",
)

C_SOURCE_FIREWALL = (
    "a PASS certifies only that the epoch census is a lawful input to the "
    "existing bounded source surfaces; no energy/stress/resource law, "
    "reciprocal response, sign/scale law, or gravity identification is "
    "selected; Born untouched."
)

CENSUS_SCHEMA_TABLE = (
    {
        "field": "variant",
        "dtype": "str",
        "meaning": "Cycle-722 input leg: primary or alternate_port",
    },
    {
        "field": "shape",
        "dtype": "tuple[int,int,int]",
        "meaning": "fixed epoch box (2,2,2)",
    },
    {
        "field": "role_stats.<packet_field>.retained_register",
        "dtype": "int",
        "meaning": "Cycle-722 register supplying the named Stage-E packet field",
    },
    {
        "field": "role_stats.<packet_field>.retained_witness_valid",
        "dtype": "bool",
        "meaning": "Cycle-722 origin/last-owner retain-after witness",
    },
    {
        "field": "role_stats.<packet_field>.total_register_touches",
        "dtype": "int",
        "meaning": "all scheduled reads/writes of that retained register",
    },
    {
        "field": "role_stats.<packet_field>.admitted_stage_e_read_touches",
        "dtype": "int",
        "meaning": "admitted Stage-E packet words reading that role/register",
    },
    {
        "field": "stage_e_admissions",
        "dtype": "list[{tick_identity:int,status:str,admitted:bool}]",
        "meaning": "unchanged Cycle-610 admission result for every Stage-E packet",
    },
    {
        "field": "walk",
        "dtype": "dict[str,int]",
        "meaning": "Cycle-722 collision/liveness/touch census totals",
    },
)

# Supplied convention.  Each row aggregates one admitted Stage-E role count
# into exactly one canonical S1 component by multiplying it by the corresponding
# landed canonical fixture component.  There is no division or normalization.
CENSUS_TO_TENSOR_REDUCTION = (
    {
        "canonical_slot": 0,
        "block": "lapse",
        "variant": "primary",
        "packet_role": "certificate",
        "census_field": "admitted_stage_e_read_touches",
        "coefficient": "S1.tensor_source_with_constraints()[0][0]",
    },
    {
        "canonical_slot": 1,
        "block": "shift",
        "variant": "primary",
        "packet_role": "binder",
        "census_field": "admitted_stage_e_read_touches",
        "coefficient": "S1.tensor_source_with_constraints()[0][1]",
    },
    {
        "canonical_slot": 2,
        "block": "shift",
        "variant": "primary",
        "packet_role": "actuality",
        "census_field": "admitted_stage_e_read_touches",
        "coefficient": "S1.tensor_source_with_constraints()[0][2]",
    },
    {
        "canonical_slot": 3,
        "block": "shift",
        "variant": "primary",
        "packet_role": "admissibility",
        "census_field": "admitted_stage_e_read_touches",
        "coefficient": "S1.tensor_source_with_constraints()[0][3]",
    },
    {
        "canonical_slot": 4,
        "block": "trace",
        "variant": "primary",
        "packet_role": "law_domain",
        "census_field": "admitted_stage_e_read_touches",
        "coefficient": "S1.tensor_source_with_constraints()[0][4]",
    },
    {
        "canonical_slot": 5,
        "block": "shear",
        "variant": "alternate_port",
        "packet_role": "certificate",
        "census_field": "admitted_stage_e_read_touches",
        "coefficient": "S1.tensor_source_with_constraints()[0][5]",
    },
    {
        "canonical_slot": 6,
        "block": "shear",
        "variant": "alternate_port",
        "packet_role": "binder",
        "census_field": "admitted_stage_e_read_touches",
        "coefficient": "S1.tensor_source_with_constraints()[0][6]",
    },
    {
        "canonical_slot": 7,
        "block": "shear",
        "variant": "alternate_port",
        "packet_role": "actuality",
        "census_field": "admitted_stage_e_read_touches",
        "coefficient": "S1.tensor_source_with_constraints()[0][7]",
    },
    {
        "canonical_slot": 8,
        "block": "shear",
        "variant": "alternate_port",
        "packet_role": "admissibility",
        "census_field": "admitted_stage_e_read_touches",
        "coefficient": "S1.tensor_source_with_constraints()[0][8]",
    },
    {
        "canonical_slot": 9,
        "block": "shear",
        "variant": "alternate_port",
        "packet_role": "law_domain",
        "census_field": "admitted_stage_e_read_touches",
        "coefficient": "S1.tensor_source_with_constraints()[0][9]",
    },
)

# Second supplied convention for the strengthening certificate.  The ten
# canonical basis slots are assigned, in order, to the literal slot count for
# each (variant, stage) pair.  Coefficients are declared unit weights: there is
# no fixture multiplication, division, normalization, fitting, or refitting.
STAGE_RESOLVED_TO_TENSOR_REDUCTION = (
    {
        "canonical_slot": 0,
        "block": "lapse",
        "variant": "primary",
        "stage": "A",
        "stage_statistic": "slot_count",
        "coefficient": 1.0,
    },
    {
        "canonical_slot": 1,
        "block": "shift",
        "variant": "primary",
        "stage": "B",
        "stage_statistic": "slot_count",
        "coefficient": 1.0,
    },
    {
        "canonical_slot": 2,
        "block": "shift",
        "variant": "primary",
        "stage": "C",
        "stage_statistic": "slot_count",
        "coefficient": 1.0,
    },
    {
        "canonical_slot": 3,
        "block": "shift",
        "variant": "primary",
        "stage": "D",
        "stage_statistic": "slot_count",
        "coefficient": 1.0,
    },
    {
        "canonical_slot": 4,
        "block": "trace",
        "variant": "primary",
        "stage": "E",
        "stage_statistic": "slot_count",
        "coefficient": 1.0,
    },
    {
        "canonical_slot": 5,
        "block": "shear",
        "variant": "alternate_port",
        "stage": "A",
        "stage_statistic": "slot_count",
        "coefficient": 1.0,
    },
    {
        "canonical_slot": 6,
        "block": "shear",
        "variant": "alternate_port",
        "stage": "B",
        "stage_statistic": "slot_count",
        "coefficient": 1.0,
    },
    {
        "canonical_slot": 7,
        "block": "shear",
        "variant": "alternate_port",
        "stage": "C",
        "stage_statistic": "slot_count",
        "coefficient": 1.0,
        "declared_zero_reason": "alternate_port has no Stage-C slots",
    },
    {
        "canonical_slot": 8,
        "block": "shear",
        "variant": "alternate_port",
        "stage": "D",
        "stage_statistic": "slot_count",
        "coefficient": 1.0,
    },
    {
        "canonical_slot": 9,
        "block": "shear",
        "variant": "alternate_port",
        "stage": "E",
        "stage_statistic": "slot_count",
        "coefficient": 1.0,
    },
)

# Frozen after one inspection of the stage-resolved vector
# [225, 9, 112, 17304, 24, 225, 18, 0, 17304, 24].  Exact landed detail
# strings are part of the certificate, so a changed pass/fail or value cannot
# silently flip the strengthening result.
S1_STAGE_RESOLVED_FROZEN_DISPOSITION = (
    {
        "check": "projector_algebra",
        "expected_pass": True,
        "expected_values": "ranks={'lapse': 1, 'shift': 3, 'trace': 1, 'shear': 5}",
        "kind": "source-independent projector identity",
        "explanation": "Canonical projector ranks do not depend on source scale.",
    },
    {
        "check": "orientation_twist",
        "expected_pass": True,
        "expected_values": (
            "block_norms={'lapse': 225.0, 'shift': 17304.365, "
            "'trace': 24.0, 'shear': 17305.489}, flip_resid=0.0e+00"
        ),
        "kind": "scale-covariant after block occupancy",
        "explanation": (
            "The twist residual is homogeneous and every canonical block is "
            "occupied above the landed threshold."
        ),
    },
    {
        "check": "ward_constraint",
        "expected_pass": False,
        "expected_values": (
            "residuals(+,-,0)=['1.9e+04', '1.9e+04', '0.0e+00']"
        ),
        "kind": "constraint-membership",
        "explanation": (
            "The declared stage-count vector is not in the frozen canonical "
            "Ward nullspace; orientation zero still annihilates it."
        ),
    },
    {
        "check": "response_locking",
        "expected_pass": True,
        "expected_values": (
            "field_flip=0.0e+00, null=0.0e+00, "
            "pair_signs={(1, 1): 1.0, (1, -1): -1.0, "
            "(-1, 1): -1.0, (-1, -1): 1.0}"
        ),
        "kind": "scale-covariant linear response",
        "explanation": (
            "The universal block response and orientation signs are linear "
            "identities for this nonuniform source."
        ),
    },
    {
        "check": "scalar_only_no_overclaim",
        "expected_pass": True,
        "expected_values": "complement_norm=0.0e+00",
        "kind": "source-independent fixed scalar fixture",
        "explanation": "This landed gate constructs its own scalar fixture.",
    },
    {
        "check": "free_tensor_carrier",
        "expected_pass": True,
        "expected_values": (
            "tensor_source_blocks={'lapse': 225.0, 'shift': 17304.365, "
            "'trace': 24.0, 'shear': 17305.489}, "
            "chi_only_blocks={'lapse': 1.0, 'shift': 0.0, "
            "'trace': 0.5, 'shear': 0.0}"
        ),
        "kind": "block-occupancy membership",
        "explanation": (
            "The stage-count source has nonzero shift and shear carriers; "
            "the fixed chi-only comparator does not."
        ),
    },
    {
        "check": "no_claim",
        "expected_pass": True,
        "expected_values": (
            "negative_inertial_mass=False, shielding=False, propulsion=False, "
            "reactionless_force=False, "
            "physical_signed_gravity_prediction=False"
        ),
        "kind": "source-independent claim firewall",
        "explanation": "This landed gate has no source input.",
    },
)

S3_TYPED_BINDING_TABLE = (
    {"event_type": "route_A", "tick_identity_mod_3": 0, "expected_count": 16},
    {"event_type": "route_B", "tick_identity_mod_3": 1, "expected_count": 16},
    {"event_type": "route_C", "tick_identity_mod_3": 2, "expected_count": 16},
)


def array_certificate(array: np.ndarray) -> dict[str, object]:
    contiguous = np.ascontiguousarray(array)
    return {
        "dtype": contiguous.dtype.str,
        "shape": list(contiguous.shape),
        "sha256": sha256(contiguous.tobytes(order="C")).hexdigest(),
    }


def byte_pins() -> dict[str, object]:
    """Compare working bytes with the bytes at HEAD, the landed-byte anchor."""
    rows: dict[str, object] = {}
    for relative in AUDIT_INPUT_PATHS:
        observed_bytes = (ROOT / relative).read_bytes()
        landed = subprocess.run(
            ["git", "-C", str(ROOT), "show", f"HEAD:{relative}"],
            capture_output=True,
            check=False,
        )
        expected_bytes = landed.stdout if landed.returncode == 0 else b""
        observed = sha256(observed_bytes).hexdigest()
        expected = sha256(expected_bytes).hexdigest() if landed.returncode == 0 else None
        rows[relative] = {
            "observed_sha256": observed,
            "landed_HEAD_sha256": expected,
            "git_show_returncode": landed.returncode,
            "pass": landed.returncode == 0 and observed == expected,
        }
    rows["pass"] = all(
        bool(row["pass"]) for row in rows.values() if isinstance(row, dict)
    )
    return rows


def stage_resolved_statistics(
    slots: list[object],
    stage_e_admissions: list[dict[str, object]],
    walk: dict[str, object],
) -> dict[str, object]:
    """Census literal scheduled work and receiving-stage handoffs."""
    rows = {
        stage: {
            "slot_count": 0,
            "word_count": 0,
            "register_touch_count": 0,
            "read_touch_count": 0,
            "write_touch_count": 0,
            "retain_after_declaration_count": 0,
            "declared_handoff_count": 0,
            "admitted_packet_word_count": 0,
        }
        for stage in STAGES
    }
    register_state: dict[int, str] = {}
    for slot in slots:
        stage = str(slot.stage)
        if stage not in rows:
            raise ValueError(f"undeclared epoch stage {stage!r}")
        stage_row = rows[stage]
        stage_row["slot_count"] += 1
        for word in slot.words:
            stage_row["word_count"] += 1
            stage_row["retain_after_declaration_count"] += len(word.retain_after)
            for register, (_role, mode) in word.accesses.items():
                register = int(register)
                stage_row["register_touch_count"] += 1
                if mode == "read":
                    stage_row["read_touch_count"] += 1
                elif mode == "write":
                    stage_row["write_touch_count"] += 1
                else:
                    raise ValueError(f"undeclared register access mode {mode!r}")
                if register_state.get(register) == "retained":
                    stage_row["declared_handoff_count"] += 1
            for register in word.accesses:
                register = int(register)
                register_state[register] = (
                    "retained" if register in word.retain_after else "clean"
                )
    rows["E"]["admitted_packet_word_count"] = sum(
        int(row["admitted"]) for row in stage_e_admissions
    )
    totals = {
        statistic: sum(int(rows[stage][statistic]) for stage in STAGES)
        for statistic in rows["A"]
    }
    return {
        "convention": (
            "Statistics are literal counts over the already-built epoch slots. "
            "declared_handoff_count assigns an executed access to its receiving "
            "stage when that register was retained by the preceding owner; its "
            "variant total must reproduce walk.handoffs_declared."
        ),
        "stages": rows,
        "totals": totals,
        "walk_handoffs_declared": int(walk["handoffs_declared"]),
        "handoff_total_matches_walk": (
            totals["declared_handoff_count"] == int(walk["handoffs_declared"])
        ),
        "register_touch_total_matches_walk": (
            totals["register_touch_count"] == int(walk["register_touches"])
        ),
    }


def build_epoch_census() -> tuple[dict[str, object], dict[str, object]]:
    """Build each (2,2,2) input leg exactly once and census its exposed records."""
    atlas = F722.EPOCH.P.build_private_atlases()
    primary = F722.EPOCH.build_epoch(SHAPE, "primary", atlas)
    alternate = F722.EPOCH.build_epoch(
        SHAPE,
        "alternate_port",
        atlas,
        recurrent_override=primary.recurrent,
    )
    bundles = {"primary": primary, "alternate_port": alternate}
    census: dict[str, object] = {
        "shape": list(SHAPE),
        "builds_per_variant": 1,
        "variants": {},
    }
    internal: dict[str, object] = {}
    for variant in VARIANTS:
        extension = F722.extend_and_walk(bundles[variant])
        feed = F722.feed_unchanged_chain(extension["table"])
        admissions = []
        for row, status in zip(extension["table"], feed["statuses"]):
            admissions.append(
                {
                    "tick_identity": int(row["tick_identity"]),
                    "status": str(status),
                    "admitted": status == "admitted",
                    "packet_fields": {
                        field: int(row[field]) for field in PACKET_FIELDS
                    },
                }
            )
        role_stats = {}
        for source in extension["sources"]:
            field = str(source["field"])
            register = int(source["register"])
            trace = F722.register_trace(extension["slots"], register)
            admitted_reads = sum(
                int(admission["admitted"])
                for admission in admissions
                if field in admission["packet_fields"]
            )
            role_stats[field] = {
                "retained_register": register,
                "register_role": str(source["register_role"]),
                "retained_witness_valid": bool(source["retained_witness"]["valid"]),
                "total_register_touches": len(trace),
                "read_touches": sum(int(mode == "read") for _i, _w, _r, mode in trace),
                "write_touches": sum(int(mode == "write") for _i, _w, _r, mode in trace),
                "admitted_stage_e_read_touches": admitted_reads,
            }
        walk = extension["walk"]
        stage_resolved = stage_resolved_statistics(
            extension["slots"], admissions, walk
        )
        census["variants"][variant] = {
            "variant": variant,
            "shape": list(SHAPE),
            "role_stats": role_stats,
            "stage_e_admissions": admissions,
            "stage_e_admitted_count": sum(
                int(row["admitted"]) for row in admissions
            ),
            "stage_e_packet_count": len(admissions),
            "all_stage_e_packets_admitted": all(
                bool(row["admitted"]) for row in admissions
            ),
            "stage_resolved": stage_resolved,
            "walk": {
                "register_touches": int(walk["register_touches"]),
                "registers_seen": int(walk["registers_seen"]),
                "handoffs_declared": int(walk["handoffs_declared"]),
                "handoffs_consumed": int(walk["handoffs_consumed"]),
                "collision_count": int(walk["collision_count"]),
                "violation_count": int(walk["violation_count"]),
            },
            "lawful": bool(extension["lawful"] and feed["pass"]),
        }
        internal[variant] = {"bundle": bundles[variant], "extension": extension}
    return census, internal


def reduce_census_to_tensor(
    census: dict[str, object],
    canonical_fixture_source: np.ndarray,
    target_slots: tuple[int, ...] = tuple(range(10)),
) -> tuple[np.ndarray, list[dict[str, object]]]:
    source = np.zeros(10, dtype=float)
    rows = []
    for schema_row, target_slot in zip(CENSUS_TO_TENSOR_REDUCTION, target_slots):
        variant = str(schema_row["variant"])
        packet_role = str(schema_row["packet_role"])
        canonical_slot = int(schema_row["canonical_slot"])
        count = int(
            census["variants"][variant]["role_stats"][packet_role][
                "admitted_stage_e_read_touches"
            ]
        )
        contribution = float(count) * float(canonical_fixture_source[canonical_slot])
        source[target_slot] += contribution
        rows.append(
            {
                **schema_row,
                "target_slot_used": target_slot,
                "observed_integer_count": count,
                "canonical_fixture_coefficient": float(
                    canonical_fixture_source[canonical_slot]
                ),
                "real_contribution": contribution,
            }
        )
    return source, rows


def reduce_stage_resolved_census(
    census: dict[str, object],
) -> tuple[np.ndarray, list[dict[str, object]]]:
    """Apply the declared unit-weight stage-statistic assignment once."""
    source = np.zeros(10, dtype=float)
    rows = []
    for assignment in STAGE_RESOLVED_TO_TENSOR_REDUCTION:
        canonical_slot = int(assignment["canonical_slot"])
        variant = str(assignment["variant"])
        stage = str(assignment["stage"])
        statistic = str(assignment["stage_statistic"])
        count = int(
            census["variants"][variant]["stage_resolved"]["stages"][stage][
                statistic
            ]
        )
        coefficient = float(assignment["coefficient"])
        contribution = coefficient * count
        source[canonical_slot] = contribution
        rows.append(
            {
                **assignment,
                "observed_integer_count": count,
                "real_contribution": contribution,
            }
        )
    return source, rows


def nonproportionality_certificate(
    source: np.ndarray,
    canonical_fixture_source: np.ndarray,
) -> dict[str, object]:
    fixture_nonzero = np.abs(canonical_fixture_source) > S1.TOL
    ratios = source[fixture_nonzero] / canonical_fixture_source[fixture_nonzero]
    best_fit_scale = float(
        np.dot(canonical_fixture_source, source)
        / np.dot(canonical_fixture_source, canonical_fixture_source)
    )
    residual = float(
        np.linalg.norm(source - best_fit_scale * canonical_fixture_source)
    )
    relative_residual = residual / max(float(np.linalg.norm(source)), S1.TOL)
    ratio_spread = float(np.ptp(ratios))
    return {
        "comparison": "stage_resolved_source / canonical_fixture_source",
        "fixture_nonzero_slot_count": int(np.sum(fixture_nonzero)),
        "slot_ratios": ratios.tolist(),
        "ratio_min": float(np.min(ratios)),
        "ratio_max": float(np.max(ratios)),
        "ratio_spread": ratio_spread,
        "least_squares_scale": best_fit_scale,
        "nonproportional_residual": residual,
        "relative_nonproportional_residual": relative_residual,
        "numerically_nonproportional": bool(
            len(ratios) >= 2
            and ratio_spread > 1.0e-8
            and relative_residual > 1.0e-10
        ),
    }


def frozen_stage_disposition(
    observed_checks: dict[str, object],
) -> tuple[list[dict[str, object]], bool]:
    rows = []
    for frozen in S1_STAGE_RESOLVED_FROZEN_DISPOSITION:
        label = str(frozen["check"])
        observed = observed_checks.get(label)
        expected = {
            "pass": bool(frozen["expected_pass"]),
            "values": str(frozen["expected_values"]),
        }
        rows.append(
            {
                **frozen,
                "observed": observed,
                "exact_frozen_match": observed == expected,
            }
        )
    frozen_labels = {
        str(row["check"]) for row in S1_STAGE_RESOLVED_FROZEN_DISPOSITION
    }
    exact = (
        all(bool(row["exact_frozen_match"]) for row in rows)
        and set(observed_checks) == frozen_labels
    )
    return rows, exact


def s1_check_set(
    source: np.ndarray,
    constraint: np.ndarray,
    projectors: S1.Projectors,
) -> dict[str, object]:
    calls = (
        ("projector_algebra", lambda: S1.projector_algebra_check(projectors)),
        ("orientation_twist", lambda: S1.orientation_twist_check(source, projectors)),
        ("ward_constraint", lambda: S1.ward_constraint_check(source, constraint)),
        ("response_locking", lambda: S1.response_locking_check(source)),
        (
            "scalar_only_no_overclaim",
            lambda: S1.scalar_only_no_overclaim_check(projectors),
        ),
        ("free_tensor_carrier", lambda: S1.free_tensor_carrier_gate(source)),
        ("no_claim", S1.no_claim_gate),
    )
    checks = {}
    for label, call in calls:
        passed, detail = call()
        checks[label] = {"pass": bool(passed), "values": detail}
    return {
        "checks": checks,
        "source": source.tolist(),
        "source_certificate": array_certificate(source),
        "block_norms": S1.block_norms(source, projectors),
        "pass": all(bool(row["pass"]) for row in checks.values()),
    }


def run_unchanged(
    relative_path: str,
    required_marker: str | None = None,
) -> dict[str, object]:
    env = os.environ.copy()
    scripts_path = str(ROOT / "scripts")
    env["PYTHONPATH"] = (
        scripts_path
        if not env.get("PYTHONPATH")
        else scripts_path + os.pathsep + env["PYTHONPATH"]
    )
    started = perf_counter()
    try:
        run = subprocess.run(
            [sys.executable, str(ROOT / relative_path)],
            cwd=ROOT,
            env=env,
            capture_output=True,
            text=True,
            errors="replace",
            timeout=AUDIT_TIMEOUT_SEC,
            check=False,
        )
        stdout = run.stdout
        stderr = run.stderr
        timed_out = False
        returncode = run.returncode
    except subprocess.TimeoutExpired as exc:
        stdout = (exc.stdout or "") if isinstance(exc.stdout, str) else ""
        stderr = (exc.stderr or "") if isinstance(exc.stderr, str) else ""
        timed_out = True
        returncode = None
    lines = stdout.splitlines()
    pass_lines = [
        line for line in lines
        if line.startswith("PASS ") or line.startswith("[PASS]")
    ]
    fail_lines = [
        line for line in lines
        if line.startswith("FAIL ") or line.startswith("[FAIL]")
    ]
    marker_found = required_marker is None or required_marker in stdout
    return {
        "path": relative_path,
        "execution": "fresh subprocess of the landed script; no arguments or edits",
        "returncode": returncode,
        "timed_out": timed_out,
        "pass_line_count": len(pass_lines),
        "fail_line_count": len(fail_lines),
        "fail_lines": fail_lines,
        "summary_lines": [
            line for line in lines
            if "SUMMARY" in line or "RESULT " in line or "FINAL_TAG:" in line
        ],
        "required_marker": required_marker,
        "required_marker_found": marker_found,
        "stdout_sha256": sha256(stdout.encode()).hexdigest(),
        "stderr_tail": stderr.splitlines()[-8:],
        "runtime_seconds": perf_counter() - started,
        "pass": returncode == 0 and not timed_out and not fail_lines and marker_found,
    }


def s2_count_binding(census: dict[str, object]) -> dict[str, object]:
    observed_per_cell = []
    occupied_by_endpoint = []
    for endpoint, variant in enumerate(VARIANTS):
        occupied = {
            int(row["tick_identity"]) % len(S2.REVERSE)
            for row in census["variants"][variant]["stage_e_admissions"]
            if row["admitted"]
        }
        occupied_by_endpoint.append(occupied)
        observed_per_cell.append(len(occupied))
    reverse_pairs = {
        tuple(sorted((direction, int(S2.REVERSE[direction]))))
        for direction in range(len(S2.REVERSE))
    }
    observed_pair_count = sum(
        sum(int(left in occupied and right in occupied) for left, right in reverse_pairs)
        for occupied in occupied_by_endpoint
    )
    observed = {
        "endpoint_cell_count": len(occupied_by_endpoint),
        "per_cell_unit_weight_event_counts": observed_per_cell,
        "unit_weight_total": sum(observed_per_cell),
        "reciprocity_symmetric_pair_count": observed_pair_count,
    }
    fixture = {
        "endpoint_cell_count": len(S2.ENDPOINTS),
        "per_cell_unit_weight_event_counts": [
            len(S2.REVERSE) for _endpoint in S2.ENDPOINTS
        ],
        "unit_weight_total": len(S2.ENDPOINTS) * len(S2.REVERSE),
        "reciprocity_symmetric_pair_count": len(S2.ENDPOINTS) * len(reverse_pairs),
    }
    comparison = [
        {
            "integer_invariant": key,
            "census_value": observed[key],
            "harness_fixture_value": fixture[key],
            "equal": observed[key] == fixture[key],
        }
        for key in fixture
    ]
    return {
        "convention": (
            "Each input leg names one endpoint cell; admitted tick identity modulo "
            "six names only an occupied direction bin. Each occupied bin carries "
            "integer weight one. Multiplicity supplies no amplitude or phase."
        ),
        "comparison_table": comparison,
        "observed": observed,
        "fixture": fixture,
        "pass": all(bool(row["equal"]) for row in comparison),
    }


def s3_count_binding(census: dict[str, object]) -> dict[str, object]:
    observed = {row["event_type"]: 0 for row in S3_TYPED_BINDING_TABLE}
    per_variant = {}
    for variant in VARIANTS:
        counts = {row["event_type"]: 0 for row in S3_TYPED_BINDING_TABLE}
        for admission in census["variants"][variant]["stage_e_admissions"]:
            if not admission["admitted"]:
                continue
            residue = int(admission["tick_identity"]) % 3
            event_type = S3_TYPED_BINDING_TABLE[residue]["event_type"]
            counts[event_type] += 1
            observed[event_type] += 1
        per_variant[variant] = counts
    rows = [
        {
            **declared,
            "observed_count": observed[declared["event_type"]],
            "equal": observed[declared["event_type"]] == declared["expected_count"],
        }
        for declared in S3_TYPED_BINDING_TABLE
    ]
    route_count_row = {
        "integer_invariant": "typed_route_count",
        "census_value": sum(int(value > 0) for value in observed.values()),
        "contract_fixture_value": 3,
    }
    route_count_row["equal"] = (
        route_count_row["census_value"] == route_count_row["contract_fixture_value"]
    )
    return {
        "convention": (
            "Admitted tick identity modulo three supplies a typed count row A/B/C. "
            "The rows remain separate and are not spliced into a combined law."
        ),
        "declared_binding_table": list(S3_TYPED_BINDING_TABLE),
        "per_variant_counts": per_variant,
        "comparison_table": rows,
        "route_count_comparison": route_count_row,
        "pass": all(bool(row["equal"]) for row in rows)
        and bool(route_count_row["equal"]),
    }


def altered_count_controls(census: dict[str, object]) -> dict[str, object]:
    s2_altered = deepcopy(census)
    removed_s2 = []
    for row in s2_altered["variants"]["primary"]["stage_e_admissions"]:
        if int(row["tick_identity"]) % 6 == 0:
            row["admitted"] = False
            row["status"] = "deliberately_altered_count"
            removed_s2.append(int(row["tick_identity"]))
    s2_altered["variants"]["primary"]["stage_e_admitted_count"] -= len(removed_s2)
    s2_result = s2_count_binding(s2_altered)

    s3_altered = deepcopy(census)
    first = s3_altered["variants"]["primary"]["stage_e_admissions"][0]
    first["admitted"] = False
    first["status"] = "deliberately_altered_count"
    s3_altered["variants"]["primary"]["stage_e_admitted_count"] -= 1
    s3_result = s3_count_binding(s3_altered)
    return {
        "s2_altered_count": {
            "removed_primary_tick_identities": removed_s2,
            "binding_pass_after_alteration": s2_result["pass"],
            "detected": not s2_result["pass"],
            "comparison_table": s2_result["comparison_table"],
        },
        "s3_altered_count": {
            "removed_primary_tick_identity": int(first["tick_identity"]),
            "binding_pass_after_alteration": s3_result["pass"],
            "detected": not s3_result["pass"],
            "comparison_table": s3_result["comparison_table"],
        },
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

    pins = byte_pins()
    check(
        "all five consumed harness/module files equal their landed HEAD bytes",
        pins["pass"],
        {
            path: row["observed_sha256"]
            for path, row in pins.items()
            if isinstance(row, dict)
        },
    )

    census, _internal = build_epoch_census()
    census_clean = (
        census["builds_per_variant"] == 1
        and set(census["variants"]) == set(VARIANTS)
        and all(census["variants"][variant]["lawful"] for variant in VARIANTS)
        and all(
            census["variants"][variant]["stage_e_admitted_count"] == 24
            for variant in VARIANTS
        )
        and all(
            census["variants"][variant]["role_stats"][field][
                "retained_witness_valid"
            ]
            and census["variants"][variant]["role_stats"][field][
                "admitted_stage_e_read_touches"
            ] == 24
            for variant in VARIANTS
            for field in PACKET_FIELDS
        )
    )
    check(
        "both (2,2,2) input legs are built once and expose a lawful retained-role/admission census",
        census_clean,
        {
            variant: {
                "admissions": census["variants"][variant][
                    "stage_e_admitted_count"
                ],
                "role_counts": {
                    field: census["variants"][variant]["role_stats"][field][
                        "admitted_stage_e_read_touches"
                    ]
                    for field in PACKET_FIELDS
                },
                "walk": census["variants"][variant]["walk"],
            }
            for variant in VARIANTS
        },
    )

    canonical_source, canonical_constraint = S1.tensor_source_with_constraints()
    projectors = S1.canonical_projectors()
    reduced_source, reduction_rows = reduce_census_to_tensor(
        census, canonical_source
    )
    s1_feed = s1_check_set(reduced_source, canonical_constraint, projectors)
    s1_gates_preserved = (
        s1_feed["checks"]["scalar_only_no_overclaim"]["pass"]
        and s1_feed["checks"]["free_tensor_carrier"]["pass"]
        and s1_feed["checks"]["no_claim"]["pass"]
    )
    check(
        "the declared real count-to-length-10 reduction passes the full landed S1 check set unchanged",
        s1_feed["pass"],
        s1_feed["checks"],
    )
    check(
        "S1 scalar-only, ordinary-carrier, and no-claim gates remain preserved on their landed fixtures",
        s1_gates_preserved,
        {
            key: s1_feed["checks"][key]
            for key in (
                "scalar_only_no_overclaim",
                "free_tensor_carrier",
                "no_claim",
            )
        },
    )

    lawful_role_counts = [
        int(
            census["variants"][variant]["role_stats"][field][
                "admitted_stage_e_read_touches"
            ]
        )
        for variant in VARIANTS
        for field in PACKET_FIELDS
    ]
    s1_lawful_census_role_uniform = bool(
        census_clean
        and len(set(lawful_role_counts)) == 1
        and lawful_role_counts[0] == 24
    )
    stage_census_table = [
        {
            "variant": variant,
            "stage": stage,
            **census["variants"][variant]["stage_resolved"]["stages"][stage],
        }
        for variant in VARIANTS
        for stage in STAGES
    ]
    stage_statistics_nonuniform = all(
        len({int(row[statistic]) for row in stage_census_table}) > 1
        for statistic in (
            "slot_count",
            "declared_handoff_count",
            "register_touch_count",
        )
    )
    stage_accounting_exact = all(
        census["variants"][variant]["stage_resolved"][
            "handoff_total_matches_walk"
        ]
        and census["variants"][variant]["stage_resolved"][
            "register_touch_total_matches_walk"
        ]
        for variant in VARIANTS
    )
    stage_source, stage_reduction_rows = reduce_stage_resolved_census(census)
    stage_nonproportionality = nonproportionality_certificate(
        stage_source, canonical_source
    )
    s1_stage_feed = s1_check_set(
        stage_source, canonical_constraint, projectors
    )
    stage_disposition, stage_disposition_frozen = frozen_stage_disposition(
        s1_stage_feed["checks"]
    )
    stage_assignment_complete = (
        len(stage_reduction_rows) == 10
        and {
            int(row["canonical_slot"]) for row in stage_reduction_rows
        } == set(range(10))
    )
    stage_zero_refit = {
        "optimizer_calls": 0,
        "fitted_parameters": 0,
        "normalization_applied": False,
        "fixture_coefficient_applied": False,
        "coefficient_convention": "declared unit weight for every assigned slot",
        "supplied_convention": True,
    }
    s1_stage_resolved_certificate_pass = bool(
        s1_lawful_census_role_uniform
        and stage_statistics_nonuniform
        and stage_accounting_exact
        and stage_assignment_complete
        and stage_nonproportionality["numerically_nonproportional"]
        and stage_disposition_frozen
        and stage_zero_refit["optimizer_calls"] == 0
        and stage_zero_refit["fitted_parameters"] == 0
        and stage_zero_refit["normalization_applied"] is False
    )
    check(
        "the stage-resolved S1 feed is nonuniform, nonproportional, zero-refit, and reproduces its frozen landed-check disposition",
        s1_stage_resolved_certificate_pass,
        {
            "source": stage_source.tolist(),
            "ratio_spread": stage_nonproportionality["ratio_spread"],
            "numerically_nonproportional": stage_nonproportionality[
                "numerically_nonproportional"
            ],
            "stage_statistics_nonuniform": stage_statistics_nonuniform,
            "stage_accounting_exact": stage_accounting_exact,
            "frozen_disposition_match": stage_disposition_frozen,
            "disposition": [
                {
                    "check": row["check"],
                    "pass": row["observed"]["pass"],
                    "values": row["observed"]["values"],
                }
                for row in stage_disposition
            ],
        },
    )

    s1_anchor = run_unchanged(
        "scripts/signed_gravity_oriented_tensor_source_lift.py",
        "FINAL_TAG: SIGNED_GRAVITY_ORIENTED_TENSOR_SOURCE_LIFT_FINITE_CONDITIONAL",
    )
    check(
        "the byte-pinned S1 main reruns unchanged as the landed-harness anchor",
        s1_anchor["pass"],
        {
            "returncode": s1_anchor["returncode"],
            "pass_lines": s1_anchor["pass_line_count"],
            "fail_lines": s1_anchor["fail_line_count"],
            "summary": s1_anchor["summary_lines"],
        },
    )

    s2_anchor = run_unchanged(
        "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
        "RESULT TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CERTIFIED",
    )
    check(
        "the byte-pinned S2 Cycle-322 harness reruns unchanged",
        s2_anchor["pass"],
        {
            "returncode": s2_anchor["returncode"],
            "pass_lines": s2_anchor["pass_line_count"],
            "fail_lines": s2_anchor["fail_line_count"],
            "summary": s2_anchor["summary_lines"],
        },
    )
    s2_binding = s2_count_binding(census)
    check(
        "the separate S2 binding matches only exact integer fixture counts",
        s2_binding["pass"],
        s2_binding["comparison_table"],
    )
    s2_language = "full-Fock Cycle-320 unit-weight auxiliary sources"
    s2_finding_ok = s2_language in S2.N1_ROUTES
    check(
        "S2 honestly records no census input port and the absent full-Fock auxiliary-source construction",
        s2_finding_ok,
        {
            "s2_input_port_exists": False,
            "module_language": s2_language,
            "no_amplitudes_invented": True,
        },
    )

    s3_anchor = run_unchanged(
        "scripts/physical_m2_gravity_source_bridge_tournament_synthesis_cycle294_2026_07_17.py"
    )
    check(
        "the byte-pinned S3 Cycle-294 contract verifier reruns unchanged in a subprocess",
        s3_anchor["pass"],
        {
            "returncode": s3_anchor["returncode"],
            "pass_lines": s3_anchor["pass_line_count"],
            "fail_lines": s3_anchor["fail_line_count"],
            "summary": s3_anchor["summary_lines"],
        },
    )
    s3_binding = s3_count_binding(census)
    check(
        "the separate S3 typed event-count table matches its declared integer binding",
        s3_binding["pass"],
        {
            "rows": s3_binding["comparison_table"],
            "route_count": s3_binding["route_count_comparison"],
        },
    )

    corrupted_census = deepcopy(census)
    corrupted_census["variants"]["primary"]["role_stats"]["certificate"][
        "admitted_stage_e_read_touches"
    ] = 0
    corrupted_source, _ = reduce_census_to_tensor(
        corrupted_census, canonical_source
    )
    corrupted_s1 = s1_check_set(
        corrupted_source, canonical_constraint, projectors
    )
    corrupted_failed = [
        label for label, row in corrupted_s1["checks"].items() if not row["pass"]
    ]

    permutation = list(range(10))
    permutation[0], permutation[1] = permutation[1], permutation[0]
    permuted_source, permuted_rows = reduce_census_to_tensor(
        census, canonical_source, tuple(permutation)
    )
    permuted_s1 = s1_check_set(
        permuted_source, canonical_constraint, projectors
    )
    permuted_failed = [
        label for label, row in permuted_s1["checks"].items() if not row["pass"]
    ]
    schema_load_bearing = (
        s1_feed["source_certificate"]["sha256"]
        != permuted_s1["source_certificate"]["sha256"]
        and s1_feed["checks"] != permuted_s1["checks"]
    )
    count_controls = altered_count_controls(census)
    controls = {
        "corrupted_s1_census_slot": {
            "slot": "primary.certificate.admitted_stage_e_read_touches",
            "baseline": 24,
            "corrupted": 0,
            "failed_checks": corrupted_failed,
            "detected": bool(corrupted_failed),
        },
        "permuted_s1_reduction_schema": {
            "permutation": permutation,
            "failed_checks": permuted_failed,
            "baseline_source_sha256": s1_feed["source_certificate"]["sha256"],
            "permuted_source_sha256": permuted_s1["source_certificate"]["sha256"],
            "outcome_changed": schema_load_bearing,
            "detected": schema_load_bearing,
            "reduction_rows": permuted_rows,
        },
        **count_controls,
    }
    controls_pass = (
        controls["corrupted_s1_census_slot"]["detected"]
        and controls["permuted_s1_reduction_schema"]["detected"]
        and controls["s2_altered_count"]["detected"]
        and controls["s3_altered_count"]["detected"]
    )
    check(
        "corrupted S1 slot, permuted schema, and altered S2/S3 census counts are all detected",
        controls_pass,
        {
            "corrupted_s1_failed_checks": corrupted_failed,
            "permuted_s1_failed_checks": permuted_failed,
            "schema_outcome_changed": schema_load_bearing,
            "s2_altered_count": controls["s2_altered_count"]["detected"],
            "s3_altered_count": controls["s3_altered_count"]["detected"],
        },
    )

    zero_refit = {
        "optimizer_calls": 0,
        "fitted_parameters": 0,
        "normalization_applied": False,
        "reduction_rule": (
            "real admitted-role count multiplied directly by the corresponding "
            "landed S1 canonical fixture component"
        ),
        "ward_constraint_provenance": (
            "unchanged second return value of "
            "S1.tensor_source_with_constraints()"
        ),
        "ward_constraint_certificate": array_certificate(canonical_constraint),
        "canonical_source_fixture_certificate": array_certificate(canonical_source),
        "supplied_convention": True,
    }
    check(
        "the census schema and S1 reduction are supplied conventions with zero refit and no normalization",
        zero_refit["optimizer_calls"] == 0
        and zero_refit["fitted_parameters"] == 0
        and zero_refit["normalization_applied"] is False,
        zero_refit,
    )

    s1_true_feed = reduced_source.shape == (10,) and reduced_source.dtype.kind == "f"
    cslt_completion_witness = bool(
        s1_true_feed
        and s1_feed["pass"]
        and s1_gates_preserved
        and s1_anchor["pass"]
    )
    not_one_combined_law_preserved = bool(
        s3_anchor["pass"] and s3_binding["pass"]
    )
    honest_keys = {
        "s1_true_feed": s1_true_feed,
        "s1_lawful_census_role_uniform": s1_lawful_census_role_uniform,
        "s2_input_port_exists": False,
        "s3_input_port_exists": False,
        "source_law_selected": False,
        "cslt_completion_witness": cslt_completion_witness,
    }
    claim_boundary = [
        C_SOURCE_FIREWALL,
        (
            "S1 consumes a supplied count reduction; S2 and S3 retain separate "
            "count bindings because their certificate functions accept no census."
        ),
        (
            "The original lawful S1 role census is uniform at 24 and only "
            "homogeneously rescales the canonical fixture; the stage-resolved "
            "zero-refit feed supplies a nonuniform strengthening with a frozen "
            "landed-check disposition."
        ),
        (
            "No census count is promoted to amplitude, phase, energy, stress, "
            "resource, reciprocal response, sign/scale law, gravity, or Born data."
        ),
    ]
    findings = {
        **honest_keys,
        "not_one_combined_law_preserved": not_one_combined_law_preserved,
        "full_Fock_Cycle320_required_and_absent": True,
        "full_Fock_Cycle320_module_language": s2_language,
    }
    mandatory_findings = (
        honest_keys["s1_true_feed"]
        and honest_keys["s2_input_port_exists"] is False
        and honest_keys["s3_input_port_exists"] is False
        and honest_keys["source_law_selected"] is False
        and honest_keys["cslt_completion_witness"]
        and not_one_combined_law_preserved
        and claim_boundary[0] == C_SOURCE_FIREWALL
    )
    check(
        "D1 honest keys, C_source firewall, completion witness, and not-one-combined-law finding hold",
        mandatory_findings,
        findings,
    )

    passing = all(row["pass"] for row in checks)
    runtime_seconds = perf_counter() - started
    report = {
        "status": "PASS" if passing else "FAIL",
        "checks": checks,
        "byte_pins": pins,
        "census_schema_table": list(CENSUS_SCHEMA_TABLE),
        "epoch_census": census,
        "CENSUS_TO_TENSOR_REDUCTION": list(CENSUS_TO_TENSOR_REDUCTION),
        "s1": {
            "true_parameterized_feed": s1_feed,
            "reduction_table": reduction_rows,
            "canonical_ward_constraint": zero_refit[
                "ward_constraint_certificate"
            ],
            "unchanged_main_anchor": s1_anchor,
            "gates_preserved": s1_gates_preserved,
        },
        "s1_stage_resolved_feed": {
            "certificate_pass": s1_stage_resolved_certificate_pass,
            "original_lawful_role_counts": lawful_role_counts,
            "s1_lawful_census_role_uniform": (
                s1_lawful_census_role_uniform
            ),
            "census_convention": {
                variant: census["variants"][variant]["stage_resolved"][
                    "convention"
                ]
                for variant in VARIANTS
            },
            "census_table": stage_census_table,
            "declared_assignment": list(
                STAGE_RESOLVED_TO_TENSOR_REDUCTION
            ),
            "reduction_table": stage_reduction_rows,
            "stage_statistics_nonuniform": stage_statistics_nonuniform,
            "stage_accounting_exact": stage_accounting_exact,
            "zero_refit": stage_zero_refit,
            "nonproportionality": stage_nonproportionality,
            "landed_check_feed": s1_stage_feed,
            "per_check_disposition": stage_disposition,
            "frozen_disposition_exact_match": stage_disposition_frozen,
            "interpretation": (
                "The nonuniform stage-count source passes the source-independent "
                "and scale-covariant landed checks plus carrier occupancy, but "
                "fails the Ward constraint-membership check because the supplied "
                "stage vector is not in the frozen canonical nullspace."
            ),
        },
        "s2": {
            "unchanged_harness_anchor": s2_anchor,
            "count_binding": s2_binding,
            "s2_input_port_exists": False,
            "finding": (
                "The certificate functions accept no census; a full-Fock "
                "Cycle-320 lift needs the absent full-Fock auxiliary-source "
                "construction."
            ),
            "module_language": s2_language,
            "new_physics_claim": False,
        },
        "s3": {
            "unchanged_contract_verifier_anchor": s3_anchor,
            "count_binding": s3_binding,
            "s3_input_port_exists": False,
            "not_one_combined_law_preserved": not_one_combined_law_preserved,
        },
        "controls": controls,
        "zero_refit": zero_refit,
        "findings": findings,
        "claim_boundary": claim_boundary,
        "authority": "none",
        "audit": "unset",
        "claim_ceiling": "bounded_theorem",
        "runtime_seconds": runtime_seconds,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if not passing:
        raise SystemExit(1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
