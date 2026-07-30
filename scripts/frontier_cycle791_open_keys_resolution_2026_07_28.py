#!/usr/bin/env python3
"""Cycle 791: resolve the Cycle-790 T=256 open keys at T=512/T=1024.

The Cycle-790 primary is importable without executing its guarded main, so
this runner directly reuses that landed census machinery.  Only its 164 open
keys are continued beyond T=256.  Every recurrence digest hit is confirmed by
exact state equality after re-evolving the candidate entry state.

This is a finite evidence census.  Whether nonzero residual support is
physical content or dirt remains open in every outcome branch.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle790_horizon_extension_2026_07_28.py",
    "scripts/frontier_cycle762_residual_as_content_probe_2026_07_28.py",
    "scripts/frontier_cycle762_residual_probe_independent_check_2026_07_28.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import ast
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle790_horizon_extension_2026_07_28 as M790


EXPECTED_INPUT_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "bc1a47b591e4b308ef3e57ea7776a56223c76c0eca3867816d408f5021e86ac6",
    AUDIT_INPUT_PATHS[1]:
        "cb5f80cf5d0e169e01561bd9a8665fc8492036398bc0f3eeebe2e326497dbd0d",
    AUDIT_INPUT_PATHS[2]:
        "c8d43dc2c65b851554393c493d016f6341ba9eb8c3a35bb9f361d77a2f16c619",
    AUDIT_INPUT_PATHS[3]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[4]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}

BASELINE_HORIZON = 256
HORIZONS = (512, 1024)
BATCH_SIZE = 16
FAMILY_SIZE = 176
EXPECTED_BASELINE_CLEAN_KEY = (3, (1, 10))
STDOUT_LIMIT_BYTES = 150 * 1024
PHYSICAL_SCOPE = "CONTENT_VS_DIRT_REMAINS_OPEN"
DERIVATION_BOUNDARY = (
    "HORIZON_EXTENDED_POSTIMAGE_LAW_REMAINS_A_DERIVATION_TARGET"
)

Coordinate = tuple[str, str, int]
Support = frozenset[Coordinate]
Key = tuple[int, tuple[int, int]]

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest_rows(rows: object) -> str:
    return sha256(compact(rows).encode("utf-8")).hexdigest()


def state_digest(state: tuple[int, ...]) -> bytes:
    return sha256(bytes(state)).digest()


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label}")
    return passed


def data(label: str, value: object) -> None:
    OUTPUT_LINES.append(f"DATA {label} {compact(value)}")


def audit_tuple_is_literal() -> bool:
    tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=Path(__file__).name,
    )
    matches = []
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        ):
            matches.append(node.value)
    return (
        len(matches) == 1
        and isinstance(matches[0], ast.Tuple)
        and all(
            isinstance(element, ast.Constant)
            and isinstance(element.value, str)
            for element in matches[0].elts
        )
        and ast.literal_eval(matches[0]) == AUDIT_INPUT_PATHS
    )


def anchor_certificate() -> dict[str, object]:
    actual = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    module_path = Path(M790.__file__).resolve()
    expected_module_path = (ROOT / AUDIT_INPUT_PATHS[0]).resolve()
    result = {
        "machinery_basis": "DIRECT_IMPORT_OF_MAIN_GUARDED_CYCLE790_PRIMARY",
        "cycle790_import_did_not_execute_main":
            not M790.CHECKS and not M790.OUTPUT_LINES,
        "cycle790_module_path": str(module_path),
        "input_sha256": actual,
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_is_literal_tuple": audit_tuple_is_literal(),
        "direct_machinery_imports": (
            "frontier_cycle790_horizon_extension_2026_07_28",
            "frontier_cycle736_pairwise_separated_multisource_2026_07_28",
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        ),
    }
    result["pass"] = (
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and actual == EXPECTED_INPUT_SHA256
        and module_path == expected_module_path
        and result["cycle790_import_did_not_execute_main"]
        and result["AUDIT_INPUT_PATHS_is_literal_tuple"]
        and all(
            hasattr(M790, name)
            for name in (
                "build_family",
                "cycle_census",
                "residual_support",
                "minimal_phase_period",
            )
        )
    )
    return result


def keyset_bytes(keys: object) -> bytes:
    return compact(tuple(sorted(keys))).encode("utf-8")


def build_identity_and_checkpoints() -> tuple[
    dict[str, object],
    dict[Key, dict[str, object]],
    dict[str, object],
]:
    """Run Cycle 790 once and retain compact exact-hash T=256 checkpoints."""

    started = monotonic()
    family = M790.build_family()
    census = M790.cycle_census(family)
    snapshot = census["snapshots"][BASELINE_HORIZON]
    actual_clean = tuple(snapshot["clean_keys"])
    actual_cycles = tuple(snapshot["cycle_keys"])
    actual_open = tuple(snapshot["open_keys"])

    expected_clean = (EXPECTED_BASELINE_CLEAN_KEY,)
    expected_cycles = tuple(
        (event, positions)
        for event, positions, _period in M790.EXPECTED_PERIODIC_KEYS_T64
    )
    expected_open = tuple(
        key
        for key in sorted(family["states"])
        if key not in set(expected_clean) | set(expected_cycles)
    )
    actual_keyset_bytes = {
        "clean": keyset_bytes(actual_clean),
        "cycles": keyset_bytes(actual_cycles),
        "open": keyset_bytes(actual_open),
    }
    expected_keyset_bytes = {
        "clean": keyset_bytes(expected_clean),
        "cycles": keyset_bytes(expected_cycles),
        "open": keyset_bytes(expected_open),
    }
    keyset_byte_agreement = {
        label: actual_keyset_bytes[label] == expected_keyset_bytes[label]
        for label in actual_keyset_bytes
    }
    keyset_sha256 = {
        label: sha256(payload).hexdigest()
        for label, payload in actual_keyset_bytes.items()
    }

    expected_period_by_key = {
        (event, positions): period
        for event, positions, period in M790.EXPECTED_PERIODIC_KEYS_T64
    }
    records = census["records"]
    t256_facts_exact = (
        snapshot["keys"] == FAMILY_SIZE
        and snapshot["clean_count"] == 1
        and snapshot["first_clean_time_census"] == {252: 1}
        and snapshot["cycle_count"] == 11
        and snapshot["state_period_census"] == {2: 2, 3: 9}
        and snapshot["residual_period_census"] == {2: 2, 3: 9}
        and snapshot["open_count"] == 164
        and records[EXPECTED_BASELINE_CLEAN_KEY]["first_clean"] == 252
        and all(
            records[key]["cycle_start"] == 0
            and records[key]["state_period"] == expected_period_by_key[key]
            and records[key]["residual_period"] == expected_period_by_key[key]
            and records[key]["cycle_nonzero"]
            for key in actual_cycles
        )
    )

    checkpoints: dict[Key, dict[str, object]] = {}
    baseline_digest_collisions = 0
    for key in actual_open:
        record = records[key]
        seen_hashes: dict[bytes, list[int]] = {}
        for state, update in sorted(
            record["seen"].items(), key=lambda item: item[1]
        ):
            digest = state_digest(state)
            if digest in seen_hashes:
                baseline_digest_collisions += 1
            seen_hashes.setdefault(digest, []).append(update)
        checkpoints[key] = {
            "state0": family["states"][key],
            "state256": record["state"],
            "supports0_256": tuple(record["residues"]),
            "seen_hash_times": {
                digest: tuple(times)
                for digest, times in seen_hashes.items()
            },
        }

    identity = {
        "cycle790_facts": {
            "T256_clean_count": snapshot["clean_count"],
            "T256_first_clean_time_census":
                snapshot["first_clean_time_census"],
            "T256_cycle_count": snapshot["cycle_count"],
            "T256_state_period_census":
                snapshot["state_period_census"],
            "T256_residual_period_census":
                snapshot["residual_period_census"],
            "T256_open_count": snapshot["open_count"],
        },
        "keyset_byte_agreement": keyset_byte_agreement,
        "keyset_sha256": keyset_sha256,
        "family_sha256": family["summary"]["family_sha256"],
        "baseline_digest_collisions": baseline_digest_collisions,
        "checkpoint_count": len(checkpoints),
        "checkpoint_sha256": digest_rows(
            tuple(
                {
                    "key": key,
                    "state0": state_digest(row["state0"]).hex(),
                    "state256": state_digest(row["state256"]).hex(),
                    "support_trace_sha256": digest_rows(
                        tuple(
                            M790.canonical_support(support)
                            for support in row["supports0_256"]
                        )
                    ),
                    "seen_digest_time_sha256": digest_rows(
                        tuple(
                            (digest.hex(), times)
                            for digest, times in sorted(
                                row["seen_hash_times"].items()
                            )
                        )
                    ),
                }
                for key, row in sorted(checkpoints.items())
            )
        ),
        "runtime_seconds": round(monotonic() - started, 6),
    }
    identity["pass"] = (
        family["summary"]["pass"]
        and t256_facts_exact
        and all(keyset_byte_agreement.values())
        and baseline_digest_collisions == 0
        and len(checkpoints) == 164
        and all(
            len(row["supports0_256"]) == BASELINE_HORIZON + 1
            and len(row["seen_hash_times"]) == BASELINE_HORIZON + 1
            for row in checkpoints.values()
        )
    )
    return identity, checkpoints, family


def exact_state_at(
    key: Key,
    update: int,
    checkpoint: dict[str, object],
    word: tuple[object, ...],
) -> tuple[int, ...]:
    """Re-evolve one candidate state for exact recurrence confirmation."""

    if update >= BASELINE_HORIZON:
        state = checkpoint["state256"]
        start = BASELINE_HORIZON
    else:
        state = checkpoint["state0"]
        start = 0
    for _step in range(start, update):
        state = M790.K.A.apply_semantic(state, word)
    return state


def initialise_resolution_records(
    checkpoints: dict[Key, dict[str, object]],
) -> dict[Key, dict[str, object]]:
    return {
        key: {
            "state": checkpoint["state256"],
            "seen_hash_times": {
                digest: list(times)
                for digest, times in checkpoint[
                    "seen_hash_times"
                ].items()
            },
            "supports": list(checkpoint["supports0_256"]),
            "first_clean": None,
            "cycle_start": None,
            "state_period": None,
            "residual_period": None,
            "cycle_closure": None,
            "cycle_nonzero": None,
            "residue_phases_sha256": None,
            "last_evolved": BASELINE_HORIZON,
            "digest_collisions": 0,
            "exact_recurrence_confirmations": 0,
        }
        for key, checkpoint in checkpoints.items()
    }


def terminal(record: dict[str, object]) -> bool:
    return (
        record["first_clean"] is not None
        or record["cycle_closure"] is not None
    )


def advance_one_key(
    key: Key,
    record: dict[str, object],
    checkpoint: dict[str, object],
    word: tuple[object, ...],
    end_update: int,
) -> int:
    """Advance one open key, confirming every recurrence with exact equality."""

    transitions = 0
    for update in range(record["last_evolved"] + 1, end_update + 1):
        transitions += 1
        state = M790.K.A.apply_semantic(record["state"], word)
        support = M790.residual_support(state)
        record["state"] = state
        record["supports"].append(support)
        record["last_evolved"] = update
        if not support:
            record["first_clean"] = update
            break

        digest = state_digest(state)
        candidate_times = record["seen_hash_times"].get(digest, ())
        exact_entry = None
        for entry in candidate_times:
            candidate_state = exact_state_at(
                key, entry, checkpoint, word
            )
            if candidate_state == state:
                exact_entry = entry
                break
            record["digest_collisions"] += 1
        if exact_entry is not None:
            phases = tuple(
                record["supports"][exact_entry:update]
            )
            record["cycle_start"] = exact_entry
            record["state_period"] = update - exact_entry
            record["residual_period"] = M790.minimal_phase_period(phases)
            record["cycle_closure"] = update
            record["cycle_nonzero"] = all(phases)
            record["residue_phases_sha256"] = digest_rows(
                tuple(
                    M790.canonical_support(phase)
                    for phase in phases
                )
            )
            record["exact_recurrence_confirmations"] += 1
            break
        record["seen_hash_times"].setdefault(digest, []).append(update)
    return transitions


def advance_batches(
    records: dict[Key, dict[str, object]],
    checkpoints: dict[Key, dict[str, object]],
    words: dict[tuple[int, int], tuple[object, ...]],
    keys: tuple[Key, ...],
    end_update: int,
) -> tuple[list[dict[str, object]], int]:
    timings = []
    total_transitions = 0
    for batch_start in range(0, len(keys), BATCH_SIZE):
        batch = keys[batch_start:batch_start + BATCH_SIZE]
        started = monotonic()
        transitions = 0
        for key in batch:
            if not terminal(records[key]):
                transitions += advance_one_key(
                    key,
                    records[key],
                    checkpoints[key],
                    words[key[1]],
                    end_update,
                )
        total_transitions += transitions
        timings.append(
            {
                "horizon": end_update,
                "batch_start": batch_start,
                "batch_stop": batch_start + len(batch),
                "keys": len(batch),
                "transitions": transitions,
                "terminals_after_batch": sum(
                    terminal(records[key]) for key in batch
                ),
                "seconds": round(monotonic() - started, 6),
            }
        )
    return timings, total_transitions


def record_status(
    record: dict[str, object],
    horizon: int,
) -> str:
    if (
        record["first_clean"] is not None
        and record["first_clean"] <= horizon
    ):
        return f"FIRST_CLEAN(t={record['first_clean']})"
    if (
        record["cycle_closure"] is not None
        and record["cycle_closure"] <= horizon
    ):
        return (
            f"CYCLE(state_period={record['state_period']},"
            f"residual_period={record['residual_period']},"
            f"entry={record['cycle_start']},"
            f"closure={record['cycle_closure']})"
        )
    if record["last_evolved"] >= horizon:
        return f"OPEN_THROUGH_T={horizon}"
    return (
        f"UNMEASURED_AFTER_T={record['last_evolved']}"
        f"_FOR_REQUESTED_T={horizon}"
    )


def resolution_snapshot(
    records: dict[Key, dict[str, object]],
    horizon: int,
) -> dict[str, object]:
    clean = []
    cycles = []
    open_keys = []
    uncovered = []
    for key, record in sorted(records.items()):
        status = record_status(record, horizon)
        if status.startswith("FIRST_CLEAN"):
            clean.append(key)
        elif status.startswith("CYCLE"):
            cycles.append(key)
        elif status.startswith("OPEN_THROUGH"):
            open_keys.append(key)
        else:
            uncovered.append(key)

    new_clean_times = dict(
        sorted(
            Counter(records[key]["first_clean"] for key in clean).items()
        )
    )
    new_state_periods = dict(
        sorted(
            Counter(records[key]["state_period"] for key in cycles).items()
        )
    )
    new_residual_periods = dict(
        sorted(
            Counter(
                records[key]["residual_period"] for key in cycles
            ).items()
        )
    )
    family_clean_times = Counter({252: 1})
    family_clean_times.update(new_clean_times)
    family_state_periods = Counter({2: 2, 3: 9})
    family_state_periods.update(new_state_periods)
    family_residual_periods = Counter({2: 2, 3: 9})
    family_residual_periods.update(new_residual_periods)
    family_clean = 1 + len(clean)
    family_cycles = 11 + len(cycles)
    return {
        "horizon": horizon,
        "T256_open_key_population": len(records),
        "new_clean_count": len(clean),
        "new_first_clean_time_census": new_clean_times,
        "new_cycle_count": len(cycles),
        "new_state_period_census": new_state_periods,
        "new_residual_period_census": new_residual_periods,
        "open_count": len(open_keys),
        "uncovered_count": len(uncovered),
        "family_clean_count": family_clean,
        "family_first_clean_time_census":
            dict(sorted(family_clean_times.items())),
        "family_cycle_count": family_cycles,
        "family_state_period_census":
            dict(sorted(family_state_periods.items())),
        "family_residual_period_census":
            dict(sorted(family_residual_periods.items())),
        "family_open_count": len(open_keys),
        "family_uncovered_count": len(uncovered),
        "family_accounting_total":
            family_clean + family_cycles + len(open_keys) + len(uncovered),
        "all_new_cycles_forever_nonzero": all(
            records[key]["cycle_nonzero"] for key in cycles
        ),
        "new_cycle_entry_census": dict(
            sorted(
                Counter(
                    records[key]["cycle_start"] for key in cycles
                ).items()
            )
        ),
        "clean_keys": tuple(clean),
        "cycle_keys": tuple(cycles),
        "open_keys": tuple(open_keys),
        "uncovered_keys": tuple(uncovered),
    }


def public_snapshot(snapshot: dict[str, object]) -> dict[str, object]:
    return {
        key: value
        for key, value in snapshot.items()
        if key not in {
            "clean_keys",
            "cycle_keys",
            "open_keys",
            "uncovered_keys",
        }
    }


def choose_t1024_prefix(
    open_keys: tuple[Key, ...],
    records: dict[Key, dict[str, object]],
    elapsed: float,
    phase512_seconds: float,
    phase512_transitions: int,
) -> tuple[int, dict[str, object]]:
    rate = (
        phase512_seconds / phase512_transitions
        if phase512_transitions
        else 0.0
    )
    active = {
        key for key in open_keys if not terminal(records[key])
    }
    selected = 0
    projected = None
    safety_factor = 2.0
    reserve_seconds = 30.0
    for candidate in range(len(open_keys), -1, -1):
        active_prefix = sum(
            key in active for key in open_keys[:candidate]
        )
        future_transitions_upper = active_prefix * (
            HORIZONS[1] - HORIZONS[0]
        )
        replay_transitions_upper = (
            phase512_transitions + future_transitions_upper
        )
        projected = (
            elapsed
            + safety_factor
            * rate
            * (future_transitions_upper + replay_transitions_upper)
            + reserve_seconds
        )
        if projected < AUDIT_TIMEOUT_SEC:
            selected = candidate
            break
    decision = {
        "policy": (
            "Complete T512 for all 164 first; then choose the largest "
            "sorted T256-open-key prefix whose measured-rate projection, "
            "including determinism replay and reserve, stays below 1500s"
        ),
        "measured_seconds_per_transition": round(rate, 9),
        "phase512_transitions": phase512_transitions,
        "active_at_T512": len(active),
        "safety_factor": safety_factor,
        "reserve_seconds": reserve_seconds,
        "declared_prefix_count": selected,
        "full_T1024_coverage": selected == len(open_keys),
        "projected_total_seconds_for_declared_prefix":
            round(projected or elapsed, 6),
    }
    return selected, decision


def deterministic_resolution_payload(
    records: dict[Key, dict[str, object]],
    snapshots: dict[int, dict[str, object]],
    prefix_count: int,
) -> dict[str, object]:
    rows = tuple(
        {
            "key": key,
            "first_clean": record["first_clean"],
            "cycle_start": record["cycle_start"],
            "state_period": record["state_period"],
            "residual_period": record["residual_period"],
            "cycle_closure": record["cycle_closure"],
            "cycle_nonzero": record["cycle_nonzero"],
            "residue_phases_sha256":
                record["residue_phases_sha256"],
            "last_evolved": record["last_evolved"],
            "digest_collisions": record["digest_collisions"],
            "exact_recurrence_confirmations":
                record["exact_recurrence_confirmations"],
            "T512": record_status(record, HORIZONS[0]),
            "T1024": record_status(record, HORIZONS[1]),
        }
        for key, record in sorted(records.items())
    )
    public_snapshots = {
        horizon: public_snapshot(snapshot)
        for horizon, snapshot in snapshots.items()
    }
    payload = {
        "declared_prefix_count": prefix_count,
        "snapshots": public_snapshots,
        "rows": rows,
    }
    return {
        "rows": rows,
        "public_snapshots": public_snapshots,
        "deterministic_sha256": digest_rows(payload),
        "table_sha256": digest_rows(rows),
    }


def resolution_sweep(
    checkpoints: dict[Key, dict[str, object]],
    family: dict[str, object],
    script_started: float,
    fixed_prefix_count: int | None = None,
) -> dict[str, object]:
    started = monotonic()
    open_keys = tuple(sorted(checkpoints))
    records = initialise_resolution_records(checkpoints)

    phase_started = monotonic()
    timings512, transitions512 = advance_batches(
        records,
        checkpoints,
        family["words"],
        open_keys,
        HORIZONS[0],
    )
    phase512_seconds = monotonic() - phase_started
    snapshot512 = resolution_snapshot(records, HORIZONS[0])

    if fixed_prefix_count is None:
        prefix_count, decision = choose_t1024_prefix(
            open_keys,
            records,
            monotonic() - script_started,
            phase512_seconds,
            transitions512,
        )
    else:
        prefix_count = fixed_prefix_count
        decision = {
            "policy": "DETERMINISM_REPLAY_USES_PRIMARY_DECLARED_PREFIX",
            "declared_prefix_count": prefix_count,
            "full_T1024_coverage": prefix_count == len(open_keys),
        }

    covered_prefix = open_keys[:prefix_count]
    timings1024, transitions1024 = advance_batches(
        records,
        checkpoints,
        family["words"],
        covered_prefix,
        HORIZONS[1],
    )
    snapshot1024 = resolution_snapshot(records, HORIZONS[1])
    snapshots = {
        HORIZONS[0]: snapshot512,
        HORIZONS[1]: snapshot1024,
    }
    deterministic = deterministic_resolution_payload(
        records, snapshots, prefix_count
    )
    return {
        "records": records,
        "snapshots": snapshots,
        "prefix_count": prefix_count,
        "covered_prefix": covered_prefix,
        "coverage_decision": decision,
        "batch_timings": tuple(timings512 + timings1024),
        "transition_counts": {
            "T257_T512": transitions512,
            "T513_T1024": transitions1024,
            "total": transitions512 + transitions1024,
        },
        **deterministic,
        "runtime_seconds": round(monotonic() - started, 6),
    }


def integer_relation(period: int, constant: int) -> str:
    if period == constant:
        return "equal"
    if constant % period == 0:
        return "period_divides_constant"
    if period % constant == 0:
        return "period_is_multiple_of_constant"
    return "neither"


def consecutive_time_clusters(
    census: dict[int, int],
) -> tuple[dict[str, object], ...]:
    times = sorted(census)
    if not times:
        return ()
    groups: list[list[int]] = [[times[0]]]
    for update in times[1:]:
        if update == groups[-1][-1] + 1:
            groups[-1].append(update)
        else:
            groups.append([update])
    return tuple(
        {
            "start": group[0],
            "stop": group[-1],
            "distinct_times": len(group),
            "clean_keys": sum(census[update] for update in group),
            "times": tuple(group),
        }
        for group in groups
    )


def structure_data(
    family: dict[str, object],
    sweep: dict[str, object],
) -> dict[str, object]:
    final = sweep["snapshots"][HORIZONS[1]]
    clean_census = final["family_first_clean_time_census"]
    unique_times = sorted(clean_census)
    gaps = tuple(
        right - left
        for left, right in zip(unique_times, unique_times[1:])
    )
    time_bins = Counter()
    for update, count in clean_census.items():
        lower = (update // 128) * 128
        upper = lower + 127
        time_bins[f"{lower}-{upper}"] += count

    constants = [
        ("orbit_length", M790.LANDED_ORBIT_LENGTH),
        ("station_count", len(family["program"])),
    ]
    constants.extend(
        (f"bank_count_{count}", count)
        for count in M790.LANDED_BANK_COUNTS
    )
    constants.extend(
        (f"bank_{index}_register_width", width)
        for index, width in enumerate(
            family["summary"]["bank_register_widths"]
        )
    )
    divisibility_rows = []
    for horizon in HORIZONS:
        snapshot = sweep["snapshots"][horizon]
        for period, count in sorted(
            snapshot["new_residual_period_census"].items()
        ):
            divisibility_rows.append(
                {
                    "horizon": horizon,
                    "new_residual_period": period,
                    "new_cycle_keys": count,
                    "relations": {
                        label: {
                            "constant": constant,
                            "relation":
                                integer_relation(period, constant),
                        }
                        for label, constant in constants
                    },
                }
            )
    return {
        "first_clean_time_census": clean_census,
        "new_first_clean_times_after_T256": tuple(
            update for update in unique_times if update > BASELINE_HORIZON
        ),
        "consecutive_time_clusters":
            consecutive_time_clusters(clean_census),
        "successive_unique_time_gaps": gaps,
        "clean_time_128_update_bins": dict(sorted(time_bins.items())),
        "t252_has_company": sum(clean_census.values()) > clean_census.get(252, 0),
        "period_basis":
            "least residual phase period on exact certified state cycle",
        "structural_constants": dict(constants),
        "new_period_census_by_horizon": {
            str(horizon): sweep["snapshots"][horizon][
                "new_residual_period_census"
            ]
            for horizon in HORIZONS
        },
        "divisibility_rows": tuple(divisibility_rows),
        "interpretive_limit":
            "Pure integer divisibility data; no numerological inference",
    }


def boundary_data() -> dict[str, object]:
    return {
        "physical_question": PHYSICAL_SCOPE,
        "content_vs_dirt": "OPEN",
        "axiom_update_triggered": False,
        "probabilities_or_weights_assigned": False,
        "postimage_law_status": DERIVATION_BOUNDARY,
        "scope": "FINITE_LANDED_EVIDENCE_CENSUS_ONLY",
    }


def row_for_output(
    key: Key,
    record: dict[str, object],
) -> dict[str, object]:
    return {
        "event": key[0],
        "positions": key[1],
        "T512": record_status(record, HORIZONS[0]),
        "T1024": record_status(record, HORIZONS[1]),
        "first_clean": record["first_clean"],
        "cycle_entry": record["cycle_start"],
        "state_period": record["state_period"],
        "residual_period": record["residual_period"],
        "cycle_closure": record["cycle_closure"],
    }


def run() -> int:
    script_started = monotonic()
    boundaries = boundary_data()

    anchors = anchor_certificate()
    check("A_anchors_and_machinery_basis", anchors["pass"])
    data(
        "A",
        {
            "machinery_basis": anchors["machinery_basis"],
            "cycle790_import_did_not_execute_main":
                anchors["cycle790_import_did_not_execute_main"],
            "input_sha256": anchors["input_sha256"],
            "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
            "direct_machinery_imports":
                anchors["direct_machinery_imports"],
            "boundaries": boundaries,
        },
    )

    identity, checkpoints, family = build_identity_and_checkpoints()
    check("B_cycle790_identity_controls", identity["pass"])
    data("B", {**identity, "boundaries": boundaries})

    primary = resolution_sweep(
        checkpoints, family, script_started
    )
    records = primary["records"]
    snapshot512 = primary["snapshots"][HORIZONS[0]]
    snapshot1024 = primary["snapshots"][HORIZONS[1]]
    declared_prefix = tuple(sorted(checkpoints))[
        :primary["prefix_count"]
    ]
    outside_prefix = set(checkpoints) - set(declared_prefix)
    expected_uncovered = tuple(
        key
        for key in sorted(outside_prefix)
        if not terminal(records[key])
    )
    exact_confirmations = sum(
        record["exact_recurrence_confirmations"]
        for record in records.values()
    )
    digest_collisions = sum(
        record["digest_collisions"] for record in records.values()
    )
    c_pass = (
        snapshot512["family_accounting_total"] == FAMILY_SIZE
        and snapshot512["uncovered_count"] == 0
        and all(
            terminal(record)
            or record["last_evolved"] >= HORIZONS[0]
            for record in records.values()
        )
        and primary["covered_prefix"] == declared_prefix
        and snapshot1024["uncovered_keys"] == expected_uncovered
        and snapshot1024["family_accounting_total"] == FAMILY_SIZE
        and digest_collisions == 0
        and exact_confirmations == snapshot1024["new_cycle_count"]
        and all(
            records[key]["cycle_nonzero"]
            for key in snapshot1024["cycle_keys"]
        )
    )
    check("C_resolution_sweep_honest_coverage", c_pass)
    data(
        "C_COVERAGE",
        {
            **primary["coverage_decision"],
            "T512_population_covered": len(checkpoints),
            "T1024_declared_prefix_sha256":
                sha256(keyset_bytes(declared_prefix)).hexdigest(),
            "T1024_uncovered_keys": expected_uncovered,
            "transition_counts": primary["transition_counts"],
            "exact_recurrence_confirmations": exact_confirmations,
            "digest_collisions": digest_collisions,
            "boundaries": boundaries,
        },
    )
    for row in primary["batch_timings"]:
        data("C_BATCH_TIMING", row)

    structure = structure_data(family, primary)
    fractions = {
        "a_clean_transients":
            f"{snapshot1024['family_clean_count']}/{FAMILY_SIZE}",
        "b_certified_cycles_permanent_residual":
            f"{snapshot1024['family_cycle_count']}/{FAMILY_SIZE}",
        "c_open":
            f"{snapshot1024['family_open_count']}/{FAMILY_SIZE}",
        "uncovered_if_partial":
            f"{snapshot1024['family_uncovered_count']}/{FAMILY_SIZE}",
    }
    table_rows = tuple(
        row_for_output(key, record)
        for key, record in sorted(records.items())
    )
    d_pass = (
        len(table_rows) == 164
        and snapshot512["family_accounting_total"] == FAMILY_SIZE
        and snapshot1024["family_accounting_total"] == FAMILY_SIZE
        and sum(
            snapshot1024["family_first_clean_time_census"].values()
        ) == snapshot1024["family_clean_count"]
        and sum(
            snapshot1024["family_residual_period_census"].values()
        ) == snapshot1024["family_cycle_count"]
        and structure["first_clean_time_census"]
        == snapshot1024["family_first_clean_time_census"]
        and boundaries["content_vs_dirt"] == "OPEN"
        and boundaries["axiom_update_triggered"] is False
        and boundaries["probabilities_or_weights_assigned"] is False
        and boundaries["postimage_law_status"] == DERIVATION_BOUNDARY
    )
    check("D_resolution_table_fractions_structure", d_pass)
    data(
        "D_RESOLUTION_TABLE",
        {
            "T512": public_snapshot(snapshot512),
            "T1024": public_snapshot(snapshot1024),
            "headline_fractions_at_T1024": fractions,
            "table_rows": len(table_rows),
            "table_sha256": primary["table_sha256"],
            "boundaries": boundaries,
        },
    )
    data(
        "D_FIRST_CLEAN_STRUCTURE",
        {
            key: value
            for key, value in structure.items()
            if key not in {"divisibility_rows"}
        },
    )
    for row in structure["divisibility_rows"]:
        data("D_DIVISIBILITY", row)
    for index, row in enumerate(table_rows):
        data(f"D_KEY_ROW_{index:03d}", row)

    replay = resolution_sweep(
        checkpoints,
        family,
        script_started,
        fixed_prefix_count=primary["prefix_count"],
    )
    deterministic = (
        replay["deterministic_sha256"]
        == primary["deterministic_sha256"]
        and replay["table_sha256"] == primary["table_sha256"]
        and replay["public_snapshots"] == primary["public_snapshots"]
        and replay["covered_prefix"] == primary["covered_prefix"]
    )
    elapsed = monotonic() - script_started
    report_core = {
        "cycle": 791,
        "machinery_basis": anchors["machinery_basis"],
        "identity": identity["cycle790_facts"],
        "coverage": primary["coverage_decision"],
        "snapshots": primary["public_snapshots"],
        "headline_fractions_at_T1024": fractions,
        "new_first_clean_times_after_T256":
            structure["new_first_clean_times_after_T256"],
        "new_period_census_at_T1024":
            snapshot1024["new_residual_period_census"],
        "checkpoint_sha256": identity["checkpoint_sha256"],
        "table_sha256": primary["table_sha256"],
        "deterministic_sha256": primary["deterministic_sha256"],
        "replay_deterministic_sha256":
            replay["deterministic_sha256"],
        "boundaries": boundaries,
        "timing_seconds": {
            "identity_and_checkpoint": identity["runtime_seconds"],
            "primary_resolution": primary["runtime_seconds"],
            "determinism_replay": replay["runtime_seconds"],
            "total": round(elapsed, 6),
        },
    }
    projected_report = {
        **report_core,
        "checks": {**CHECKS, "E_determinism_and_bounds": True},
        "pass": True,
    }
    projected_output = (
        "\n".join(OUTPUT_LINES)
        + "\nPASS E_determinism_and_bounds\n"
        + compact(projected_report)
        + "\n"
    )
    e_pass = (
        deterministic
        and digest_collisions == 0
        and elapsed < AUDIT_TIMEOUT_SEC
        and len(projected_output.encode("utf-8")) < STDOUT_LIMIT_BYTES
        and boundaries["physical_question"] == PHYSICAL_SCOPE
    )
    check("E_determinism_and_bounds", e_pass)
    data(
        "E",
        {
            "deterministic": deterministic,
            "primary_sha256": primary["deterministic_sha256"],
            "replay_sha256": replay["deterministic_sha256"],
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "projected_stdout_bytes":
                len(projected_output.encode("utf-8")),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "boundaries": boundaries,
        },
    )

    report = {
        **report_core,
        "checks": dict(CHECKS),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "pass": all(CHECKS.values()),
    }
    report["terminal"] = (
        "CYCLE791_OPEN_KEYS_RESOLUTION_PASS"
        if report["pass"]
        else "CYCLE791_OPEN_KEYS_RESOLUTION_HONEST_FAIL"
    )
    report["report_sha256"] = digest_rows(report)
    output = "\n".join(OUTPUT_LINES) + "\n" + compact(report) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        failure = {
            "pass": False,
            "terminal": "CYCLE791_OPEN_KEYS_RESOLUTION_HONEST_FAIL",
            "failure": "stdout bound exceeded",
            "bytes": len(output.encode("utf-8")),
            "boundaries": boundaries,
        }
        sys.stdout.write(compact(failure) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        failure = {
            "checks": dict(CHECKS),
            "pass": False,
            "terminal": "CYCLE791_OPEN_KEYS_RESOLUTION_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
            "boundaries": boundary_data(),
        }
        if OUTPUT_LINES:
            sys.stdout.write("\n".join(OUTPUT_LINES) + "\n")
        sys.stdout.write(compact(failure) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
