#!/usr/bin/env python3
"""Cycle 801: bounded deep scan of the Cycle-798 silent higher-k strata.

The Cycle-798 zero-survivor family-epoch catalog is reconstructed from its
pinned disk text and landed Cycle-719 controller.  Its 38 keys still open at
T=2048 are continued in measured batches: every key reaches T=4096, followed
by the largest declared sorted prefix that safely fits through T=8192.

Horizon indices count complete controller orbits after the canonical
postimage.  This fixture calculation does not identify physical time,
actuality, probability, or whether a nonzero residual is content or dirt.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle762_residual_as_content_probe_2026_07_28.py",
    "scripts/frontier_cycle762_residual_probe_independent_check_2026_07_28.py",
    "scripts/frontier_cycle790_horizon_extension_2026_07_28.py",
    "scripts/frontier_cycle791_open_keys_resolution_2026_07_28.py",
    "scripts/frontier_cycle797_deep_horizon_continuation_2026_07_28.py",
    "scripts/frontier_cycle798_higher_k_horizon_scan_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from hashlib import sha1, sha256
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle798_higher_k_horizon_scan_2026_07_28 as F798


BASELINE_T = 2048
MANDATORY_ALL_KEYS_T = 4096
TARGET_T = 8192
BATCH_SIZE = 8
TARGET_STRATA = (3, 4, 5)
EXPECTED_ZERO_COUNTS = {3: 18, 4: 20, 5: 4}
EXPECTED_T2048_TRANSIENT_MOMENTS = {3: (444, 532, 681, 1385), 4: (), 5: ()}
EXPECTED_T2048_OPEN_COUNTS = {3: 14, 4: 20, 5: 4}
EXPECTED_T2048_CYCLE_COUNTS = {3: 0, 4: 0, 5: 0}

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "cb5f80cf5d0e169e01561bd9a8665fc8492036398bc0f3eeebe2e326497dbd0d",
    AUDIT_INPUT_PATHS[3]:
        "c8d43dc2c65b851554393c493d016f6341ba9eb8c3a35bb9f361d77a2f16c619",
    AUDIT_INPUT_PATHS[4]:
        "bc1a47b591e4b308ef3e57ea7776a56223c76c0eca3867816d408f5021e86ac6",
    AUDIT_INPUT_PATHS[5]:
        "3380b3f0820a74e0f538b54144bb926a2a4be9041ed21ae5181216f481c8a98a",
    AUDIT_INPUT_PATHS[6]:
        "7ece6f7c818a4dcffb3019c610ca0861998f19cfae0287e23fe98562c1a09698",
    AUDIT_INPUT_PATHS[7]:
        "f6ec49636ecb7ec09808eed7d38f2085f6145cd383c306370502c547741942b1",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "8ddd84104dc0729107cebfb0d0cd694fe78af1af",
    AUDIT_INPUT_PATHS[2]: "87ba84671c246fe3b7473980d395ea94443921fc",
    AUDIT_INPUT_PATHS[3]: "3eff0f787a12cacf504324209f578f0c1df91c90",
    AUDIT_INPUT_PATHS[4]: "c322bb975900b2611c3f42d19da347a1dd5bfc56",
    AUDIT_INPUT_PATHS[5]: "f026960526f2f2a8d990a5a7856b02217ea798ce",
    AUDIT_INPUT_PATHS[6]: "5d70ba232efcbd4f8c0a2d798f735907d4207b81",
    AUDIT_INPUT_PATHS[7]: "9de34ad5adcbf484d4f0c7e6aec13375ed465aab",
}
FETCHED_REFERENCE_PROVENANCE = {
    AUDIT_INPUT_PATHS[7]:
        "DISK_COPY from origin/physics-loop/proof-grade-blockF9-20260729",
}

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []

Key = tuple[int, tuple[int, ...], int]


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob_sha(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def check(label: str, condition: bool, detail: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )
    return passed


def source_anchors() -> dict[str, object]:
    required_functions = {
        AUDIT_INPUT_PATHS[0]: {
            "interleaved_program", "mapped_macro",
            "apply_controller_step", "run_orbit",
        },
        AUDIT_INPUT_PATHS[1]: {"synchronous_composition_word"},
        AUDIT_INPUT_PATHS[2]: {"continuation_census"},
        AUDIT_INPUT_PATHS[3]: {"residual_support"},
        AUDIT_INPUT_PATHS[4]: {"cycle_census"},
        AUDIT_INPUT_PATHS[5]: {"advance_batches"},
        AUDIT_INPUT_PATHS[6]: {"run_continuation"},
        AUDIT_INPUT_PATHS[7]: {
            "build_zero_survivor_catalog", "scan_key",
        },
    }
    rows: dict[str, object] = {}
    all_ast_controls = True
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        payload = path.read_bytes() if path.is_file() else b""
        try:
            tree = ast.parse(payload, filename=relative)
            names = {
                node.name
                for node in tree.body
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            }
            ast_control = required_functions[relative] <= names
        except (SyntaxError, ValueError):
            ast_control = False
        all_ast_controls = all_ast_controls and ast_control
        actual_sha = sha256(payload).hexdigest()
        actual_blob = git_blob_sha(payload)
        rows[relative] = {
            "existing_DISK_path": path.is_file(),
            "sha256": actual_sha,
            "expected_sha256": EXPECTED_SHA256[relative],
            "git_blob_sha": actual_blob,
            "expected_git_blob_sha": EXPECTED_GIT_BLOBS[relative],
            "required_function_AST_present": ast_control,
            "execution_mode": (
                "PINNED_TEXT_REFERENCE"
                if relative != AUDIT_INPUT_PATHS[0]
                else "LANDED_IMPORT_TRANSITIVELY_VIA_CYCLE798"
            ),
            "fetch_provenance":
                FETCHED_REFERENCE_PROVENANCE.get(relative, "LANDED_DISK"),
            "match": (
                path.is_file()
                and actual_sha == EXPECTED_SHA256[relative]
                and actual_blob == EXPECTED_GIT_BLOBS[relative]
            ),
        }

    runner_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=__file__
    )
    assignments = [
        node
        for node in runner_tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        )
    ]
    literal_tuple = (
        len(assignments) == 1
        and isinstance(assignments[0].value, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in assignments[0].value.elts
        )
        and tuple(ast.literal_eval(assignments[0].value))
        == AUDIT_INPUT_PATHS
    )
    no_git_reference_strings = all(
        not any(token in relative for token in ("origin/", "refs/", ".git"))
        for relative in AUDIT_INPUT_PATHS
    )
    imported_exact_disk_copy = (
        Path(F798.__file__).resolve()
        == (ROOT / AUDIT_INPUT_PATHS[7]).resolve()
    )
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_tuple": literal_tuple,
        "path_count": len(AUDIT_INPUT_PATHS),
        "existing_disk_only": all(
            (ROOT / relative).is_file() for relative in AUDIT_INPUT_PATHS
        ),
        "no_git_reference_strings": no_git_reference_strings,
        "no_docs_or_ledgers": all(
            relative.startswith("scripts/") and relative.endswith(".py")
            for relative in AUDIT_INPUT_PATHS
        ),
        "imported_cycle798_exact_disk_copy": imported_exact_disk_copy,
        "rows": rows,
    }
    result["pass"] = (
        literal_tuple
        and len(AUDIT_INPUT_PATHS) == 8
        and result["existing_disk_only"]
        and no_git_reference_strings
        and result["no_docs_or_ledgers"]
        and imported_exact_disk_copy
        and all_ast_controls
        and all(row["match"] for row in rows.values())
    )
    return result


def initialise_catalog_records(
    catalog: dict[str, object],
) -> dict[Key, dict[str, object]]:
    fixture_by_event = {
        row[0]: row for row in catalog["fixtures"]
    }
    records: dict[Key, dict[str, object]] = {}
    for catalog_row in catalog["zero_rows"]:
        k = catalog_row["k"]
        positions = catalog_row["representative"]
        event = catalog_row["event"]
        _event, direction, program, before = fixture_by_event[event]
        word = F798.synchronous_composition_word(program, positions)
        initial, rail_a, rail_b, _trace = F798.K.run_orbit(
            before, program, token_positions=positions
        )
        expected_initial = F798.K.A.apply_semantic(before, word)
        expected_rail = tuple(
            int(station in positions) for station in range(len(program))
        )
        support0 = F798.residual_support(initial)
        key = (k, positions, event)
        if key in records:
            raise AssertionError(("duplicate catalog key", key))
        records[key] = {
            "key": key,
            "k": k,
            "positions": positions,
            "event": event,
            "direction": direction,
            "word": word,
            "initial_state": initial,
            "state": initial,
            "last_t": 0,
            "first_clean_t": 0 if not support0 else None,
            "cycle_start_t": None,
            "cycle_period": None,
            "cycle_closure_t": None,
            "cycle_nonzero": None,
            "minimum_residual_weight": len(support0),
            "initial_residual_weight": len(support0),
            "initial_composition_exact": initial == expected_initial,
            "initial_rails_exact":
                rail_a == expected_rail and not any(rail_b),
            "initial_clean_equivalence":
                F798.clean_postimage(initial, F798.FIXTURE_BANKS)
                == (not support0),
            "initial_state_sha256":
                sha256(str(initial).encode("ascii")).hexdigest(),
        }
    return records


def terminal(record: dict[str, object]) -> bool:
    return (
        record["first_clean_t"] is not None
        or record["cycle_closure_t"] is not None
    )


def advance_one_record(
    record: dict[str, object], end_t: int
) -> int:
    transitions = 0
    for horizon_t in range(record["last_t"] + 1, end_t + 1):
        transitions += 1
        state = F798.K.A.apply_semantic(
            record["state"], record["word"]
        )
        support = F798.residual_support(state)
        record["state"] = state
        record["last_t"] = horizon_t
        record["minimum_residual_weight"] = min(
            record["minimum_residual_weight"], len(support)
        )
        if not support:
            record["first_clean_t"] = horizon_t
            break
        if state == record["initial_state"]:
            record["cycle_start_t"] = 0
            record["cycle_period"] = horizon_t
            record["cycle_closure_t"] = horizon_t
            record["cycle_nonzero"] = True
            break
    return transitions


def advance_batches(
    records: dict[Key, dict[str, object]],
    keys: tuple[Key, ...],
    end_t: int,
    phase: str,
) -> tuple[tuple[dict[str, object], ...], int, float]:
    timings = []
    phase_started = monotonic()
    total_transitions = 0
    for batch_start in range(0, len(keys), BATCH_SIZE):
        batch = keys[batch_start:batch_start + BATCH_SIZE]
        batch_started = monotonic()
        transitions = 0
        for key in batch:
            if not terminal(records[key]):
                transitions += advance_one_record(records[key], end_t)
        total_transitions += transitions
        timings.append(
            {
                "phase": phase,
                "horizon_t": end_t,
                "batch_start": batch_start,
                "batch_stop": batch_start + len(batch),
                "keys": len(batch),
                "transitions": transitions,
                "terminals_after_batch": sum(
                    terminal(records[key]) for key in batch
                ),
                "seconds": round(monotonic() - batch_started, 6),
            }
        )
    return (
        tuple(timings),
        total_transitions,
        monotonic() - phase_started,
    )


def clone_records(
    source: dict[Key, dict[str, object]], keys: tuple[Key, ...]
) -> dict[Key, dict[str, object]]:
    return {key: dict(source[key]) for key in keys}


def open_keys_at(
    records: dict[Key, dict[str, object]], horizon_t: int
) -> tuple[Key, ...]:
    return tuple(
        sorted(
            key
            for key, record in records.items()
            if not terminal(record) and record["last_t"] >= horizon_t
        )
    )


def choose_target_prefix(
    remaining4096: tuple[Key, ...],
    script_elapsed: float,
    phase4096_seconds: float,
    phase4096_transitions: int,
) -> tuple[int, dict[str, object]]:
    rate = (
        phase4096_seconds / phase4096_transitions
        if phase4096_transitions
        else 0.0
    )
    safety_factor = 1.5
    reserve_seconds = 45.0
    per_key_upper = TARGET_T - MANDATORY_ALL_KEYS_T

    def projected(candidate: int) -> float:
        primary_target_upper = candidate * per_key_upper
        replay_mandatory_exact = phase4096_transitions
        replay_target_upper = candidate * per_key_upper
        return (
            script_elapsed
            + safety_factor
            * rate
            * (
                primary_target_upper
                + replay_mandatory_exact
                + replay_target_upper
            )
            + reserve_seconds
        )

    selected = 0
    for candidate in range(len(remaining4096), -1, -1):
        if projected(candidate) < AUDIT_TIMEOUT_SEC:
            selected = candidate
            break
    next_projection = (
        projected(selected + 1)
        if selected < len(remaining4096)
        else None
    )
    decision = {
        "policy": (
            "All 38 Cycle-798 T2048-open keys first complete T4096. "
            "Then select the largest sorted T4096-open-key prefix whose "
            "measured-rate projection includes the primary T4097..8192 "
            "continuation, an independent fixed-prefix replay from the "
            "T2048 checkpoints, a 1.5 safety factor, and 45s reserve."
        ),
        "measured_seconds_per_transition": round(rate, 12),
        "phase_T2049_T4096_seconds": round(phase4096_seconds, 6),
        "phase_T2049_T4096_transitions": phase4096_transitions,
        "T4096_remaining_open": len(remaining4096),
        "declared_T8192_prefix_count": selected,
        "full_T8192_coverage": selected == len(remaining4096),
        "safety_factor": safety_factor,
        "reserve_seconds": reserve_seconds,
        "projected_total_seconds": round(projected(selected), 6),
        "projected_next_prefix_seconds": (
            None if next_projection is None else round(next_projection, 6)
        ),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
    }
    return selected, decision


def record_outcome(record: dict[str, object]) -> str:
    if record["first_clean_t"] is not None:
        return "TRANSIENT_CLEAN"
    if record["cycle_closure_t"] is not None:
        return "CYCLE_CERTIFIED_NONZERO"
    return "OPEN"


def record_fingerprint(record: dict[str, object]) -> dict[str, object]:
    state = record["state"]
    return {
        "key": record["key"],
        "outcome": record_outcome(record),
        "first_clean_t": record["first_clean_t"],
        "cycle_start_t": record["cycle_start_t"],
        "cycle_period": record["cycle_period"],
        "cycle_closure_t": record["cycle_closure_t"],
        "cycle_nonzero": record["cycle_nonzero"],
        "open_through_t":
            record["last_t"] if not terminal(record) else None,
        "last_evaluated_t": record["last_t"],
        "minimum_residual_weight": record["minimum_residual_weight"],
        "final_state_sha256":
            sha256(str(state).encode("ascii")).hexdigest(),
    }


def resolution_row(record: dict[str, object]) -> dict[str, object]:
    outcome = record_outcome(record)
    if outcome == "TRANSIENT_CLEAN":
        resolution = f"FIRST_CLEAN_T={record['first_clean_t']}"
    elif outcome == "CYCLE_CERTIFIED_NONZERO":
        resolution = (
            "CYCLE_CERTIFIED_NONZERO:"
            f"ENTRY_T={record['cycle_start_t']}:"
            f"PERIOD={record['cycle_period']}:"
            f"CLOSURE_T={record['cycle_closure_t']}"
        )
    else:
        resolution = f"OPEN_THROUGH_T={record['last_t']}"
    return {
        "k": record["k"],
        "key": record["key"],
        "event": record["event"],
        "direction": record["direction"],
        "family_representative": record["positions"],
        "resolution": resolution,
        **record_fingerprint(record),
    }


def run_deep_primary(
    baseline_records: dict[Key, dict[str, object]],
    open2048: tuple[Key, ...],
    script_started: float,
) -> dict[str, object]:
    records = clone_records(baseline_records, open2048)
    timings4096, transitions4096, seconds4096 = advance_batches(
        records,
        open2048,
        MANDATORY_ALL_KEYS_T,
        "PRIMARY_ALL_T2049_T4096",
    )
    remaining4096 = open_keys_at(records, MANDATORY_ALL_KEYS_T)
    prefix_count, decision = choose_target_prefix(
        remaining4096,
        monotonic() - script_started,
        seconds4096,
        transitions4096,
    )
    covered8192 = remaining4096[:prefix_count]
    timings8192, transitions8192, seconds8192 = advance_batches(
        records,
        covered8192,
        TARGET_T,
        "PRIMARY_PREFIX_T4097_T8192",
    )
    rows = tuple(resolution_row(records[key]) for key in open2048)
    payload = {
        "open2048": open2048,
        "remaining4096": remaining4096,
        "covered8192": covered8192,
        "rows": rows,
    }
    return {
        "records": records,
        "remaining4096": remaining4096,
        "covered8192": covered8192,
        "prefix_count": prefix_count,
        "coverage_decision": decision,
        "rows": rows,
        "table_sha256": digest(rows),
        "deterministic_sha256": digest(payload),
        "batch_timings": timings4096 + timings8192,
        "transition_counts": {
            "T2049_T4096": transitions4096,
            "T4097_T8192": transitions8192,
            "total": transitions4096 + transitions8192,
        },
        "phase_seconds": {
            "T2049_T4096": round(seconds4096, 6),
            "T4097_T8192": round(seconds8192, 6),
        },
    }


def replay_deep_fixed_prefix(
    baseline_records: dict[Key, dict[str, object]],
    open2048: tuple[Key, ...],
    fixed_prefix: tuple[Key, ...],
) -> dict[str, object]:
    records = clone_records(baseline_records, open2048)
    timings4096, transitions4096, seconds4096 = advance_batches(
        records,
        open2048,
        MANDATORY_ALL_KEYS_T,
        "REPLAY_ALL_T2049_T4096",
    )
    replay_remaining = open_keys_at(records, MANDATORY_ALL_KEYS_T)
    if fixed_prefix != replay_remaining[:len(fixed_prefix)]:
        raise AssertionError(
            ("fixed prefix not replay prefix", fixed_prefix, replay_remaining)
        )
    timings8192, transitions8192, seconds8192 = advance_batches(
        records,
        fixed_prefix,
        TARGET_T,
        "REPLAY_PREFIX_T4097_T8192",
    )
    rows = tuple(resolution_row(records[key]) for key in open2048)
    payload = {
        "open2048": open2048,
        "remaining4096": replay_remaining,
        "covered8192": fixed_prefix,
        "rows": rows,
    }
    return {
        "records": records,
        "remaining4096": replay_remaining,
        "covered8192": fixed_prefix,
        "rows": rows,
        "table_sha256": digest(rows),
        "deterministic_sha256": digest(payload),
        "batch_timings": timings4096 + timings8192,
        "transition_counts": {
            "T2049_T4096": transitions4096,
            "T4097_T8192": transitions8192,
            "total": transitions4096 + transitions8192,
        },
        "phase_seconds": {
            "T2049_T4096": round(seconds4096, 6),
            "T4097_T8192": round(seconds8192, 6),
        },
    }


def stratum_fractions(
    baseline_records: dict[Key, dict[str, object]],
    deep_records: dict[Key, dict[str, object]],
) -> dict[int, dict[str, object]]:
    combined = {
        key: deep_records.get(key, baseline)
        for key, baseline in baseline_records.items()
    }
    result = {}
    for k in TARGET_STRATA:
        rows = tuple(
            record
            for key, record in sorted(combined.items())
            if key[0] == k
        )
        total = len(rows)
        transient = sum(
            record_outcome(record) == "TRANSIENT_CLEAN"
            for record in rows
        )
        cycle = sum(
            record_outcome(record) == "CYCLE_CERTIFIED_NONZERO"
            for record in rows
        )
        open_count = total - transient - cycle
        open8192 = sum(
            record_outcome(record) == "OPEN"
            and record["last_t"] >= TARGET_T
            for record in rows
        )
        open4096_only = sum(
            record_outcome(record) == "OPEN"
            and MANDATORY_ALL_KEYS_T <= record["last_t"] < TARGET_T
            for record in rows
        )
        target_covered = sum(
            terminal(record) or record["last_t"] >= TARGET_T
            for record in rows
        )
        new_transient = sum(
            record["first_clean_t"] is not None
            and record["first_clean_t"] > BASELINE_T
            for record in rows
        )
        new_cycle = sum(
            record["cycle_closure_t"] is not None
            and record["cycle_closure_t"] > BASELINE_T
            for record in rows
        )
        result[k] = {
            "stratum_total": total,
            "transient_total": transient,
            "cycle_total": cycle,
            "open_total": open_count,
            "new_transient_after_T2048": new_transient,
            "new_cycle_after_T2048": new_cycle,
            "open_through_T8192": open8192,
            "open_through_T4096_only": open4096_only,
            "transient_fraction": f"{transient}/{total}",
            "cycle_fraction": f"{cycle}/{total}",
            "resolved_fraction": f"{transient + cycle}/{total}",
            "open_fraction": f"{open_count}/{total}",
            "T8192_coverage_fraction": f"{target_covered}/{total}",
        }
    return result


def main() -> int:
    script_started = monotonic()
    anchors = source_anchors()
    catalog = F798.build_zero_survivor_catalog()
    baseline_records = initialise_catalog_records(catalog)
    all_catalog_keys = tuple(sorted(baseline_records))

    baseline_timings, baseline_transitions, baseline_seconds = advance_batches(
        baseline_records,
        all_catalog_keys,
        BASELINE_T,
        "IDENTITY_ALL_T1_T2048",
    )
    baseline_transient_moments = {
        k: tuple(
            sorted(
                record["first_clean_t"]
                for record in baseline_records.values()
                if record["k"] == k
                and record["first_clean_t"] is not None
            )
        )
        for k in TARGET_STRATA
    }
    baseline_open_counts = {
        k: sum(
            record["k"] == k and not terminal(record)
            for record in baseline_records.values()
        )
        for k in TARGET_STRATA
    }
    baseline_cycle_counts = {
        k: sum(
            record["k"] == k
            and record["cycle_closure_t"] is not None
            for record in baseline_records.values()
        )
        for k in TARGET_STRATA
    }
    open2048 = tuple(
        sorted(
            key
            for key, record in baseline_records.items()
            if not terminal(record)
            and record["last_t"] == BASELINE_T
        )
    )
    baseline_transient_rows = tuple(
        resolution_row(record)
        for _key, record in sorted(baseline_records.items())
        if record["first_clean_t"] is not None
    )
    baseline_identity_payload = {
        "catalog_sha256": catalog["catalog_sha256"],
        "catalog_zero_counts": catalog["zero_counts"],
        "T2048_transient_moments": baseline_transient_moments,
        "T2048_transient_rows": baseline_transient_rows,
        "T2048_cycle_counts": baseline_cycle_counts,
        "T2048_open_counts": baseline_open_counts,
        "T2048_open_key_sha256": digest(open2048),
    }
    baseline_sha = digest(
        tuple(
            record_fingerprint(baseline_records[key])
            for key in all_catalog_keys
        )
    )

    OUTPUT_LINES.append(
        "AUDIT_INPUT_PATHS_LITERAL " + repr(AUDIT_INPUT_PATHS)
    )
    OUTPUT_LINES.append("SOURCE_ANCHORS " + compact(anchors))
    OUTPUT_LINES.append(
        "FETCHED_REFERENCE_DECLARATION "
        + compact(FETCHED_REFERENCE_PROVENANCE)
    )
    OUTPUT_LINES.append(
        "CATALOG_IDENTITY "
        + compact(
            {
                "configuration_counts":
                    catalog["configuration_counts"],
                "family_counts": catalog["family_counts"],
                "class_counts": catalog["class_counts"],
                "zero_counts": catalog["zero_counts"],
                "zero_family_epoch_keys": len(catalog["zero_rows"]),
                "catalog_sha256": catalog["catalog_sha256"],
            }
        )
    )
    OUTPUT_LINES.append(
        "T2048_IDENTITY " + compact(baseline_identity_payload)
    )
    for timing in baseline_timings:
        OUTPUT_LINES.append("IDENTITY_BATCH_RATE " + compact(timing))

    certificate_a = (
        anchors["pass"]
        and catalog["pass"]
        and catalog["zero_counts"] == EXPECTED_ZERO_COUNTS
        and len(catalog["zero_rows"]) == 42
        and F798.EXPECTED_ZERO_FAMILY_EPOCHS
        == EXPECTED_ZERO_COUNTS
        and baseline_transient_moments
        == EXPECTED_T2048_TRANSIENT_MOMENTS
        and baseline_open_counts == EXPECTED_T2048_OPEN_COUNTS
        and baseline_cycle_counts == EXPECTED_T2048_CYCLE_COUNTS
        and len(open2048) == 38
        and all(
            record["initial_composition_exact"]
            and record["initial_rails_exact"]
            and record["initial_clean_equivalence"]
            and record["initial_residual_weight"] > 0
            for record in baseline_records.values()
        )
    )
    check(
        "CERTIFICATE_A_ANCHORS_AND_CATALOG_IDENTITY_CONTROLS",
        certificate_a,
        {
            "anchors_pass": anchors["pass"],
            "catalog_pass": catalog["pass"],
            "catalog_zero_counts": catalog["zero_counts"],
            "T2048_transient_moments": baseline_transient_moments,
            "T2048_cycle_counts": baseline_cycle_counts,
            "T2048_open_counts": baseline_open_counts,
            "T2048_open_keys": len(open2048),
            "baseline_transitions": baseline_transitions,
            "baseline_seconds": round(baseline_seconds, 6),
            "baseline_sha256": baseline_sha,
        },
    )

    primary = run_deep_primary(
        baseline_records, open2048, script_started
    )
    primary_records = primary["records"]
    remaining4096 = primary["remaining4096"]
    covered8192 = primary["covered8192"]
    decision = primary["coverage_decision"]
    covered8192_set = set(covered8192)
    not_covered8192 = tuple(
        key for key in remaining4096 if key not in covered8192_set
    )
    full_t4096 = all(
        terminal(primary_records[key])
        or primary_records[key]["last_t"] >= MANDATORY_ALL_KEYS_T
        for key in open2048
    )
    target_coverage_valid = all(
        terminal(primary_records[key])
        or primary_records[key]["last_t"] >= TARGET_T
        for key in covered8192
    )
    uncovered_stops_at_4096 = all(
        not terminal(primary_records[key])
        and primary_records[key]["last_t"] == MANDATORY_ALL_KEYS_T
        for key in not_covered8192
    )
    largest_prefix_honest = (
        covered8192 == remaining4096[:primary["prefix_count"]]
        and decision["projected_total_seconds"] < AUDIT_TIMEOUT_SEC
        and (
            decision["full_T8192_coverage"]
            or (
                decision["projected_next_prefix_seconds"] is not None
                and decision["projected_next_prefix_seconds"]
                >= AUDIT_TIMEOUT_SEC
            )
        )
    )

    def resolved_by(record: dict[str, object], horizon_t: int) -> bool:
        return (
            record["first_clean_t"] is not None
            and record["first_clean_t"] <= horizon_t
        ) or (
            record["cycle_closure_t"] is not None
            and record["cycle_closure_t"] <= horizon_t
        )

    coverage_by_stratum = {
        k: {
            "T2048_open_input": sum(key[0] == k for key in open2048),
            "terminal_by_T4096": sum(
                key[0] == k
                and resolved_by(
                    primary_records[key], MANDATORY_ALL_KEYS_T
                )
                for key in open2048
            ),
            "open_through_T4096": sum(
                key[0] == k
                and not resolved_by(
                    primary_records[key], MANDATORY_ALL_KEYS_T
                )
                and primary_records[key]["last_t"]
                >= MANDATORY_ALL_KEYS_T
                for key in open2048
            ),
            "T8192_prefix_keys": sum(
                key[0] == k for key in covered8192
            ),
            "terminal_or_open_through_T8192": sum(
                key[0] == k
                and (
                    terminal(primary_records[key])
                    or primary_records[key]["last_t"] >= TARGET_T
                )
                for key in open2048
            ),
        }
        for k in TARGET_STRATA
    }
    OUTPUT_LINES.append(
        "DEEP_SCAN_COVERAGE_DECISION " + compact(decision)
    )
    OUTPUT_LINES.append(
        "DEEP_SCAN_HONEST_COVERAGE "
        + compact(
            {
                "T2048_open_keys": len(open2048),
                "T4096_all_keys_complete": full_t4096,
                "T4096_remaining_open": len(remaining4096),
                "T8192_declared_prefix_count": len(covered8192),
                "T8192_full_coverage":
                    decision["full_T8192_coverage"],
                "not_covered_beyond_T4096": not_covered8192,
                "coverage_by_stratum": coverage_by_stratum,
                "transition_counts": primary["transition_counts"],
                "phase_seconds": primary["phase_seconds"],
            }
        )
    )
    for timing in primary["batch_timings"]:
        OUTPUT_LINES.append("DEEP_SCAN_BATCH_RATE " + compact(timing))

    cycle_records = tuple(
        record
        for record in primary_records.values()
        if record["cycle_closure_t"] is not None
    )
    transient_records = tuple(
        record
        for record in primary_records.values()
        if record["first_clean_t"] is not None
    )
    terminal_certificates_exact = (
        all(
            not F798.residual_support(record["state"])
            for record in transient_records
        )
        and all(
            record["cycle_start_t"] == 0
            and record["cycle_period"] == record["cycle_closure_t"]
            and record["cycle_nonzero"] is True
            and record["state"] == record["initial_state"]
            for record in cycle_records
        )
    )
    certificate_b = (
        len(open2048) == 38
        and full_t4096
        and target_coverage_valid
        and uncovered_stops_at_4096
        and largest_prefix_honest
        and terminal_certificates_exact
        and sum(
            primary["transition_counts"][phase]
            for phase in ("T2049_T4096", "T4097_T8192")
        )
        == primary["transition_counts"]["total"]
    )
    check(
        "CERTIFICATE_B_DEEP_SCAN_WITH_HONEST_COVERAGE",
        certificate_b,
        {
            "all_38_complete_T4096": full_t4096,
            "coverage_decision": decision,
            "coverage_by_stratum": coverage_by_stratum,
            "target_coverage_valid": target_coverage_valid,
            "uncovered_stops_exactly_T4096": uncovered_stops_at_4096,
            "terminal_certificates_exact":
                terminal_certificates_exact,
            "deep_scan_sha256": primary["deterministic_sha256"],
        },
    )

    fractions = stratum_fractions(
        baseline_records, primary_records
    )
    new_transients = tuple(
        sorted(
            (
                resolution_row(record)
                for record in primary_records.values()
                if record["first_clean_t"] is not None
                and record["first_clean_t"] > BASELINE_T
            ),
            key=lambda row: (row["first_clean_t"], row["key"]),
        )
    )
    new_cycles = tuple(
        sorted(
            (
                resolution_row(record)
                for record in primary_records.values()
                if record["cycle_closure_t"] is not None
                and record["cycle_closure_t"] > BASELINE_T
            ),
            key=lambda row: (row["cycle_closure_t"], row["key"]),
        )
    )
    for row in primary["rows"]:
        OUTPUT_LINES.append("RESOLUTION_ROW " + compact(row))
    OUTPUT_LINES.append("UPDATED_STRATUM_FRACTIONS " + compact(fractions))
    OUTPUT_LINES.append(
        "NEW_RESOLUTIONS "
        + compact(
            {
                "transients": new_transients,
                "cycles": new_cycles,
                "by_stratum": {
                    k: {
                        "new_transient":
                            fractions[k]["new_transient_after_T2048"],
                        "new_cycle":
                            fractions[k]["new_cycle_after_T2048"],
                    }
                    for k in TARGET_STRATA
                },
            }
        )
    )
    for row in new_transients:
        OUTPUT_LINES.append(
            "NEW_SELECTION_TEST_AVAILABLE "
            + compact(
                {
                    "k": row["k"],
                    "key": row["key"],
                    "first_clean_t": row["first_clean_t"],
                    "selection_test_run_here": False,
                }
            )
        )
    OUTPUT_LINES.append(
        "NEW_SELECTION_TEST_COUNT "
        + compact(
            {
                "count": len(new_transients),
                "selection_tests_run_here": 0,
            }
        )
    )
    fraction_totals_exact = (
        set(fractions) == set(TARGET_STRATA)
        and all(
            fractions[k]["stratum_total"] == EXPECTED_ZERO_COUNTS[k]
            and (
                fractions[k]["transient_total"]
                + fractions[k]["cycle_total"]
                + fractions[k]["open_total"]
                == fractions[k]["stratum_total"]
            )
            for k in TARGET_STRATA
        )
    )
    table_keys = tuple(row["key"] for row in primary["rows"])
    resolution_table_complete = (
        len(primary["rows"]) == len(open2048) == 38
        and len(set(table_keys)) == 38
        and tuple(sorted(table_keys)) == open2048
        and all(
            row["outcome"]
            in {"TRANSIENT_CLEAN", "CYCLE_CERTIFIED_NONZERO", "OPEN"}
            for row in primary["rows"]
        )
    )
    certificate_c = (
        resolution_table_complete
        and fraction_totals_exact
        and len(new_transients)
        == sum(
            fractions[k]["new_transient_after_T2048"]
            for k in TARGET_STRATA
        )
        and len(new_cycles)
        == sum(
            fractions[k]["new_cycle_after_T2048"]
            for k in TARGET_STRATA
        )
    )
    check(
        "CERTIFICATE_C_RESOLUTION_TABLE_AND_UPDATED_FRACTIONS",
        certificate_c,
        {
            "resolution_rows": len(primary["rows"]),
            "table_sha256": primary["table_sha256"],
            "updated_stratum_fractions": fractions,
            "new_transient_count": len(new_transients),
            "new_cycle_count": len(new_cycles),
            "selection_tests_run_here": 0,
        },
    )

    boundaries = {
        "fixture_scope_only": True,
        "actuality_claim": False,
        "horizon_is_physical_time": False,
        "probability_claim": False,
        "fractions_are_exact_census_counts_not_probabilities": True,
        "content_vs_dirt": "OPEN",
        "content_vs_dirt_open": True,
        "selection_test_run_here": False,
        "axiom_update_triggered": False,
        "cycle_certificate_basis": (
            "exact return of the full state to its T=0 state under the "
            "fixed reversible semantic word, after every earlier "
            "projected residual was checked nonzero"
        ),
    }
    OUTPUT_LINES.append("BOUNDARIES " + compact(boundaries))
    OUTPUT_LINES.append("axiom_update_triggered: false")
    certificate_d = (
        boundaries["fixture_scope_only"]
        and not boundaries["actuality_claim"]
        and not boundaries["horizon_is_physical_time"]
        and not boundaries["probability_claim"]
        and boundaries[
            "fractions_are_exact_census_counts_not_probabilities"
        ]
        and boundaries["content_vs_dirt_open"]
        and not boundaries["selection_test_run_here"]
        and not boundaries["axiom_update_triggered"]
    )
    check(
        "CERTIFICATE_D_BOUNDARIES",
        certificate_d,
        boundaries,
    )

    replay = replay_deep_fixed_prefix(
        baseline_records, open2048, covered8192
    )
    for timing in replay["batch_timings"]:
        OUTPUT_LINES.append("DETERMINISM_REPLAY_BATCH " + compact(timing))
    deterministic = (
        replay["remaining4096"] == primary["remaining4096"]
        and replay["covered8192"] == primary["covered8192"]
        and replay["rows"] == primary["rows"]
        and replay["table_sha256"] == primary["table_sha256"]
        and replay["deterministic_sha256"]
        == primary["deterministic_sha256"]
        and replay["transition_counts"] == primary["transition_counts"]
    )
    elapsed = monotonic() - script_started
    projected_stdout_bytes = (
        len("\n".join(OUTPUT_LINES).encode("utf-8")) + 32 * 1024
    )
    certificate_e = (
        deterministic
        and baseline_sha == digest(
            tuple(
                record_fingerprint(baseline_records[key])
                for key in all_catalog_keys
            )
        )
        and elapsed < AUDIT_TIMEOUT_SEC
        and projected_stdout_bytes < STDOUT_LIMIT_BYTES
    )
    check(
        "CERTIFICATE_E_DETERMINISM_AND_BOUNDS",
        certificate_e,
        {
            "primary_sha256": primary["deterministic_sha256"],
            "replay_sha256": replay["deterministic_sha256"],
            "primary_table_sha256": primary["table_sha256"],
            "replay_table_sha256": replay["table_sha256"],
            "deterministic": deterministic,
            "primary_transitions": primary["transition_counts"],
            "replay_transitions": replay["transition_counts"],
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "projected_stdout_bytes": projected_stdout_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )

    passed = all(CHECKS.values())
    terminal_summary = {
        "terminal": (
            "CYCLE801_SILENT_STRATA_DEEP_SCAN_PASS"
            if passed
            else "CYCLE801_SILENT_STRATA_DEEP_SCAN_HONEST_FAIL"
        ),
        "pass": passed,
        "new_resolutions_by_stratum": {
            k: {
                "transient":
                    fractions[k]["new_transient_after_T2048"],
                "cycle": fractions[k]["new_cycle_after_T2048"],
            }
            for k in TARGET_STRATA
        },
        "T4096_all_38_complete": full_t4096,
        "T8192_full_coverage": decision["full_T8192_coverage"],
        "T8192_declared_prefix_count": len(covered8192),
        "T4096_remaining_open": len(remaining4096),
        "updated_stratum_fractions": fractions,
        "determinism_sha256": primary["deterministic_sha256"],
        "runtime_seconds": round(elapsed, 6),
        "axiom_update_triggered": False,
    }
    output = (
        "\n".join(OUTPUT_LINES)
        + "\nFINAL "
        + compact(terminal_summary)
        + "\n"
    )
    output_bytes = len(output.encode("utf-8"))
    if output_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", output_bytes))
    sys.stdout.write(output)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
