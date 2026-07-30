#!/usr/bin/env python3
"""Cycle 790: extend the Cycle-762 postimage census to T=128 and T=256.

The Cycle-762 pair is absent from this checkout, so this runner reimplements
the independent checker's census machinery from its SHA-anchored historical
text.  It uses only that pair's two declared controller inputs.

This is a finite, landed-scope cleanliness/cycle census.  It makes no ruling
on whether a forever-nonzero residual is physical content or dirt.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle762_residual_as_content_probe_2026_07_28.py",
    "scripts/frontier_cycle762_residual_probe_independent_check_2026_07_28.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import ast
from collections import Counter
from hashlib import sha256
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


LINEAGE_COMMIT = "67b4ac37b875fb5e6f46aee8d2a1c42b00be5be5"
EXPECTED_INPUT_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "cb5f80cf5d0e169e01561bd9a8665fc8492036398bc0f3eeebe2e326497dbd0d",
    AUDIT_INPUT_PATHS[1]:
        "c8d43dc2c65b851554393c493d016f6341ba9eb8c3a35bb9f361d77a2f16c619",
    AUDIT_INPUT_PATHS[2]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[3]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "87ba84671c246fe3b7473980d395ea94443921fc",
    AUDIT_INPUT_PATHS[1]: "3eff0f787a12cacf504324209f578f0c1df91c90",
}

RING_STATIONS = 11
FIXTURE_BANKS = 2
HORIZONS = (64, 128, 256)
LANDED_ORBIT_LENGTH = 130
LANDED_BANK_COUNTS = (2, 5, 12)
STDOUT_LIMIT_BYTES = 150 * 1024
PHYSICAL_SCOPE = "CONTENT_VS_DIRT_REMAINS_OPEN"

EXPECTED_PERIODIC_KEYS_T64 = (
    (3, (0, 5), 2),
    (3, (0, 6), 2),
    (3, (1, 6), 3),
    (3, (1, 7), 3),
    (3, (2, 7), 3),
    (3, (2, 8), 3),
    (3, (3, 8), 3),
    (3, (3, 9), 3),
    (3, (4, 9), 3),
    (3, (4, 10), 3),
    (3, (5, 10), 3),
)
EXPECTED_T64_CLASSIFICATION_SHA256 = (
    "8a5e30ccccaa7f7cf6fb5a56b620b0bda81b155747ce1e6cd398260f037c3d41"
)

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []

Coordinate = tuple[str, str, int]
Support = frozenset[Coordinate]
Key = tuple[int, tuple[int, int]]


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest_rows(rows: object) -> str:
    return sha256(compact(rows).encode("utf-8")).hexdigest()


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label}")
    return passed


def git_bytes(path: str) -> bytes:
    completed = subprocess.run(
        ["git", "show", f"{LINEAGE_COMMIT}:{path}"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout


def git_blob(path: str) -> str:
    completed = subprocess.run(
        ["git", "rev-parse", f"{LINEAGE_COMMIT}:{path}"],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout.strip()


def anchored_bytes(path: str) -> tuple[bytes, str]:
    local = ROOT / path
    if local.is_file():
        return local.read_bytes(), "working_tree"
    return git_bytes(path), f"git:{LINEAGE_COMMIT}"


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


def machinery_certificate() -> dict[str, object]:
    sources = {}
    source_modes = {}
    actual_sha = {}
    for path in AUDIT_INPUT_PATHS:
        payload, mode = anchored_bytes(path)
        sources[path] = payload
        source_modes[path] = mode
        actual_sha[path] = sha256(payload).hexdigest()

    primary_tree = ast.parse(
        sources[AUDIT_INPUT_PATHS[0]],
        filename=AUDIT_INPUT_PATHS[0],
    )
    checker_tree = ast.parse(
        sources[AUDIT_INPUT_PATHS[1]],
        filename=AUDIT_INPUT_PATHS[1],
    )
    primary_functions = {
        node.name
        for node in primary_tree.body
        if isinstance(node, ast.FunctionDef)
    }
    checker_functions = {
        node.name
        for node in checker_tree.body
        if isinstance(node, ast.FunctionDef)
    }
    required_primary = {
        "held_two_bank_epochs",
        "k2_positions",
        "continuation_census",
    }
    required_checker = {
        "separated_k2_positions",
        "synchronous_word",
        "watched_bank_registers",
        "residual_support",
        "build_family",
        "asymptotic_census",
    }
    primary_module = Path(AUDIT_INPUT_PATHS[0]).stem
    checker_module = Path(AUDIT_INPUT_PATHS[1]).stem
    importable = {
        primary_module: importlib.util.find_spec(primary_module) is not None,
        checker_module: importlib.util.find_spec(checker_module) is not None,
    }
    blob_ids = {
        path: git_blob(path)
        for path in AUDIT_INPUT_PATHS[:2]
    }
    result = {
        "machinery_basis":
            "REIMPLEMENTED_FROM_SHA_ANCHORED_CYCLE762_INDEPENDENT_CHECKER_TEXT",
        "reason": "Cycle-762 machinery reimplemented, never imported; anchors verified byte-exact from git or pinned-identical disk copies",
        "lineage_commit": LINEAGE_COMMIT,
        "source_modes": source_modes,
        "input_sha256": actual_sha,
        "expected_input_sha256": EXPECTED_INPUT_SHA256,
        "git_blob_ids": blob_ids,
        "expected_git_blob_ids": EXPECTED_GIT_BLOBS,
        "cycle762_importable": importable,
        "primary_basis_functions": tuple(sorted(required_primary)),
        "checker_basis_functions": tuple(sorted(required_checker)),
        "AUDIT_INPUT_PATHS_is_literal_tuple": audit_tuple_is_literal(),
    }
    result["pass"] = (
        actual_sha == EXPECTED_INPUT_SHA256
        and blob_ids == EXPECTED_GIT_BLOBS
        and (
            not any(importable.values())
            or actual_sha == EXPECTED_INPUT_SHA256
        )
        and required_primary <= primary_functions
        and required_checker <= checker_functions
        and result["AUDIT_INPUT_PATHS_is_literal_tuple"]
    )
    return result


def separated_k2_positions() -> tuple[tuple[int, int], ...]:
    """Cycle-762 independent checker's exact C_11 separated k=2 family."""

    return tuple(
        (left, right)
        for left, right in combinations(range(RING_STATIONS), 2)
        if min(
            (right - left) % RING_STATIONS,
            (left - right) % RING_STATIONS,
        )
        > 1
    )


def synchronous_word(
    program: tuple[object, ...],
    positions0: tuple[int, int],
) -> tuple[object, ...]:
    """Compose one lawful complete orbit of both moving source controls."""

    positions = tuple(positions0)
    word = []
    for _step in range(len(program)):
        live = set(positions)
        for station, row in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(row))
        positions = tuple(
            (station + 1) % len(program) for station in positions
        )
    return tuple(word)


def watched_bank_registers() -> tuple[tuple[str, int], ...]:
    rows = [
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
    ]
    rows.extend(
        (f"FRESH_{index}", wire)
        for index, wire in enumerate(K.A.FRESH)
    )
    rows.extend(
        (f"ZERO_WORK_{index}", wire)
        for index, wire in enumerate(K.A.ZERO_WORK)
    )
    rows.append(("TOKEN_OK", K.A.TOKEN_OK))
    return tuple(rows)


def residual_support(state: tuple[int, ...]) -> Support:
    """Exact Cycle-762 postimage-cleanliness support projection."""

    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    result: set[Coordinate] = set()
    if state[K.R3.X.SOURCE_POINTER]:
        result.add(("source", "SOURCE_POINTER", 0))
    for bank_index, bank in enumerate(banks):
        for register, wire in watched_bank_registers():
            if bank[wire]:
                result.add(("bank", register, bank_index))
    for link_index, link in enumerate(links):
        for wire, content in enumerate(link):
            if content:
                result.add(("link", f"WIRE_{wire}", link_index))
    return frozenset(result)


def canonical_support(row: Support) -> tuple[Coordinate, ...]:
    return tuple(sorted(row))


def build_family() -> dict[str, object]:
    """Reconstruct the same four epochs and 176 Cycle-762 postimages."""

    started = monotonic()
    program = K.interleaved_program(FIXTURE_BANKS)
    banks0, links0 = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks0, links0)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    epochs = []
    epoch_failures = 0
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        epoch_failures += after != K.A.apply_semantic(before, allocator)
        epoch_failures += rail_a != (1,) + (0,) * (len(program) - 1)
        epoch_failures += any(rail_b)
        epoch_failures += len(trace) != len(program)
        epochs.append((event, direction, before))
        state = after

    positions = separated_k2_positions()
    m736_positions = {
        M736.occupied_sites(config)
        for config in M736.configuration_census()["configurations"]
        if sum(config) == 2
    }
    words = {
        positions0: synchronous_word(program, positions0)
        for positions0 in positions
    }
    word_disagreements = sum(
        words[positions0]
        != M736.synchronous_composition_word(program, positions0)
        for positions0 in positions
    )
    states: dict[Key, tuple[int, ...]] = {}
    residues: dict[Key, Support] = {}
    composition_failures = 0
    rail_failures = 0
    inverse_failures = 0
    for event, _direction, before in epochs:
        for positions0 in positions:
            after, rail_a, rail_b, _trace = K.run_orbit(
                before, program, token_positions=positions0
            )
            expected_rail = tuple(
                int(station in positions0)
                for station in range(len(program))
            )
            restored, inverse_a, inverse_b, _ = K.run_orbit(
                after,
                program,
                token_positions=positions0,
                reverse=True,
            )
            composition_failures += (
                after != K.A.apply_semantic(before, words[positions0])
            )
            rail_failures += rail_a != expected_rail or any(rail_b)
            inverse_failures += (
                restored != before
                or inverse_a != rail_a
                or inverse_b != rail_b
            )
            key = (event, positions0)
            states[key] = after
            residues[key] = residual_support(after)

    per_epoch_signatures = tuple(
        len(
            {
                residues[(event, positions0)]
                for positions0 in positions
            }
        )
        for event in range(2 * FIXTURE_BANKS)
    )
    summary = {
        "epochs": len(epochs),
        "directions": tuple(row[1] for row in epochs),
        "program_stations": len(program),
        "positions": len(positions),
        "M736_position_set_agrees": set(positions) == m736_positions,
        "M736_expected_k2_count": M736.EXPECTED_COUNTS_BY_K[2],
        "synchronous_word_disagreements": word_disagreements,
        "keys": len(states),
        "unique_frozen_signatures": len(set(residues.values())),
        "unique_signatures_by_epoch": per_epoch_signatures,
        "epoch_failures": epoch_failures,
        "composition_failures": composition_failures,
        "rail_return_failures": rail_failures,
        "literal_inverse_failures": inverse_failures,
        "all_frozen_residues_nonzero": all(residues.values()),
        "bank_register_widths": tuple(map(len, banks0)),
        "link_register_widths": tuple(map(len, links0)),
        "family_sha256": digest_rows(
            tuple(
                (key, canonical_support(residues[key]))
                for key in sorted(residues)
            )
        ),
        "runtime_seconds": round(monotonic() - started, 6),
    }
    summary["pass"] = (
        summary["epochs"] == 4
        and summary["directions"]
        == ((1, 0), (0, 1), (1, 0), (0, 1))
        and summary["program_stations"] == RING_STATIONS
        and summary["positions"]
        == summary["M736_expected_k2_count"]
        == 44
        and summary["M736_position_set_agrees"]
        and summary["synchronous_word_disagreements"] == 0
        and summary["keys"] == 176
        and summary["unique_frozen_signatures"] == 25
        and summary["unique_signatures_by_epoch"] == (1, 1, 12, 14)
        and summary["epoch_failures"] == 0
        and summary["composition_failures"] == 0
        and summary["rail_return_failures"] == 0
        and summary["literal_inverse_failures"] == 0
        and summary["all_frozen_residues_nonzero"]
    )
    return {
        "program": program,
        "positions": positions,
        "words": words,
        "states": states,
        "residues": residues,
        "summary": summary,
    }


def minimal_phase_period(phases: tuple[Support, ...]) -> int:
    """Return the least period of a frozen finite cyclic phase word."""

    length = len(phases)
    for candidate in range(1, length + 1):
        if length % candidate:
            continue
        if all(
            phases[index] == phases[index % candidate]
            for index in range(length)
        ):
            return candidate
    raise AssertionError(("no finite-word period", length))


def status_at(record: dict[str, object], horizon: int) -> str:
    first_clean = record["first_clean"]
    if first_clean is not None and first_clean <= horizon:
        return f"FIRST_CLEAN(t={first_clean})"
    closure = record["cycle_closure"]
    if closure is not None and closure <= horizon:
        return (
            f"CYCLE(period={record['residual_period']},"
            f"entry={record['cycle_start']},"
            f"state_period={record['state_period']},closure={closure})"
        )
    return f"OPEN(no_clean_or_certified_cycle_through_T={horizon})"


def snapshot_summary(
    records: dict[Key, dict[str, object]],
    horizon: int,
) -> dict[str, object]:
    clean = []
    cycles = []
    open_keys = []
    for key in sorted(records):
        record = records[key]
        first_clean = record["first_clean"]
        closure = record["cycle_closure"]
        if first_clean is not None and first_clean <= horizon:
            clean.append(key)
        elif closure is not None and closure <= horizon:
            cycles.append(key)
        else:
            open_keys.append(key)

    first_clean_times = Counter(
        records[key]["first_clean"] for key in clean
    )
    state_periods = Counter(
        records[key]["state_period"] for key in cycles
    )
    residual_periods = Counter(
        records[key]["residual_period"] for key in cycles
    )
    open_minimum_weights = Counter(
        min(records[key]["weights"][:horizon + 1])
        for key in open_keys
    )
    return {
        "horizon": horizon,
        "keys": len(records),
        "clean_count": len(clean),
        "first_clean_time_census": dict(sorted(first_clean_times.items())),
        "cycle_count": len(cycles),
        "state_period_census": dict(sorted(state_periods.items())),
        "residual_period_census": dict(sorted(residual_periods.items())),
        "open_count": len(open_keys),
        "open_minimum_weight_census":
            dict(sorted(open_minimum_weights.items())),
        "all_certified_cycles_forever_nonzero": all(
            records[key]["cycle_nonzero"] for key in cycles
        ),
        "clean_keys": tuple(clean),
        "cycle_keys": tuple(cycles),
        "open_keys": tuple(open_keys),
    }


def cycle_census(family: dict[str, object]) -> dict[str, object]:
    """Batch all 176 keys once through T=256, stopping certified terminals."""

    started = monotonic()
    records: dict[Key, dict[str, object]] = {}
    for key in sorted(family["states"]):
        state = family["states"][key]
        residue = residual_support(state)
        records[key] = {
            "state": state,
            "seen": {state: 0},
            "residues": [residue],
            "weights": [len(residue)],
            "first_clean": 0 if not residue else None,
            "cycle_start": None,
            "state_period": None,
            "residual_period": None,
            "cycle_closure": None,
            "cycle_nonzero": None,
            "residue_phases": None,
        }
    active = {
        key
        for key, record in records.items()
        if record["first_clean"] is None
    }
    segment_started = started
    segment_timings = {}
    snapshots = {}

    for update in range(1, HORIZONS[-1] + 1):
        for key in sorted(active):
            record = records[key]
            state = K.A.apply_semantic(
                record["state"], family["words"][key[1]]
            )
            residue = residual_support(state)
            record["state"] = state
            record["residues"].append(residue)
            record["weights"].append(len(residue))
            if not residue:
                record["first_clean"] = update
                active.remove(key)
                continue
            if state in record["seen"]:
                entry = record["seen"][state]
                state_period = update - entry
                phases = tuple(
                    record["residues"][entry:update]
                )
                record["cycle_start"] = entry
                record["state_period"] = state_period
                record["residual_period"] = minimal_phase_period(phases)
                record["cycle_closure"] = update
                record["cycle_nonzero"] = all(phases)
                record["residue_phases"] = tuple(
                    canonical_support(phase) for phase in phases
                )
                active.remove(key)
                continue
            record["seen"][state] = update

        if update in HORIZONS:
            snapshots[update] = snapshot_summary(records, update)
            now = monotonic()
            segment_timings[update] = {
                "segment_seconds": round(now - segment_started, 6),
                "cumulative_seconds": round(now - started, 6),
                "active_after_horizon": len(active),
            }
            segment_started = now

    table_rows = tuple(
        {
            "event": key[0],
            "positions": key[1],
            **{
                f"T{horizon}": status_at(records[key], horizon)
                for horizon in HORIZONS
            },
        }
        for key in sorted(records)
    )
    deterministic_records = tuple(
        {
            "key": key,
            "first_clean": record["first_clean"],
            "cycle_start": record["cycle_start"],
            "state_period": record["state_period"],
            "residual_period": record["residual_period"],
            "cycle_closure": record["cycle_closure"],
            "cycle_nonzero": record["cycle_nonzero"],
            "residue_phases": record["residue_phases"],
            "minimum_weight": min(record["weights"]),
        }
        for key, record in sorted(records.items())
    )
    deterministic_payload = {
        "snapshots": snapshots,
        "table_rows": table_rows,
        "records": deterministic_records,
    }
    return {
        "records": records,
        "snapshots": snapshots,
        "table_rows": table_rows,
        "segment_timings": segment_timings,
        "deterministic_sha256": digest_rows(deterministic_payload),
        "table_sha256": digest_rows(table_rows),
        "runtime_seconds": round(monotonic() - started, 6),
    }


def expected_on_cycle_content_census() -> tuple[dict[str, object], ...]:
    source = ("source", "SOURCE_POINTER", 0)
    link = ("link", "WIRE_0", 0)

    def period_two(bank: int) -> tuple[tuple[Coordinate, ...], ...]:
        return (
            tuple(sorted((("bank", "DIRECTION_OK", bank), link, source))),
            (source,),
        )

    def period_three(bank: int) -> tuple[tuple[Coordinate, ...], ...]:
        return (
            tuple(
                sorted(
                    (
                        ("bank", "POINTER", bank),
                        ("bank", "V_TO_U", bank),
                        link,
                    )
                )
            ),
            tuple(
                sorted(
                    (
                        ("bank", "DIRECTION_OK", bank),
                        ("bank", "POINTER", bank),
                        ("bank", "V_TO_U", bank),
                        link,
                    )
                )
            ),
            (source,),
        )

    return (
        {"period": 2, "keys": 2, "residue_phases": period_two(0)},
        {"period": 3, "keys": 6, "residue_phases": period_three(0)},
        {"period": 3, "keys": 3, "residue_phases": period_three(1)},
    )


def t64_identity(
    family: dict[str, object],
    census: dict[str, object],
) -> dict[str, object]:
    """Rebuild the exact Cycle-762 T=64 classification and controls."""

    records = census["records"]
    classifications = []
    content_counts = Counter()
    periodic_keys = []
    noninitial_repeats = 0
    for key in sorted(records):
        record = records[key]
        residues = record["residues"][:65]
        base = {
            "event": key[0],
            "positions": key[1],
            "minimum_residue_weight": min(map(len, residues)),
            "distinct_residues_through_64": len(set(residues)),
        }
        if (
            record["first_clean"] is not None
            and record["first_clean"] <= 64
        ):
            row = {
                **base,
                "classification": "reaches_zero",
                "first_clean_update": record["first_clean"],
            }
        elif (
            record["cycle_closure"] is not None
            and record["cycle_closure"] <= 64
        ):
            period = record["state_period"]
            phases = record["residue_phases"]
            periodic_keys.append((key[0], key[1], period))
            content_counts[(period, phases)] += 1
            noninitial_repeats += record["cycle_start"] != 0
            row = {
                **base,
                "classification": "nonzero_limit_cycle",
                "cycle_start": record["cycle_start"],
                "cycle_length": period,
            }
        else:
            row = {
                **base,
                "classification": "not_clean_or_closed_within_64",
            }
        classifications.append(row)

    content_census = tuple(
        {
            "period": period,
            "keys": count,
            "residue_phases": phases,
        }
        for (period, phases), count in sorted(
            content_counts.items(),
            key=lambda item: (item[0][0], item[0][1]),
        )
    )
    snapshot = census["snapshots"][64]
    result = {
        "family": family["summary"],
        "snapshot": snapshot,
        "periodic_keys": tuple(periodic_keys),
        "on_cycle_content_census": content_census,
        "noninitial_full_state_repeats": noninitial_repeats,
        "classification_sha256": digest_rows(classifications),
    }
    result["pass"] = (
        family["summary"]["pass"]
        and snapshot["keys"] == 176
        and snapshot["clean_count"] == 0
        and snapshot["first_clean_time_census"] == {}
        and snapshot["cycle_count"] == 11
        and snapshot["state_period_census"] == {2: 2, 3: 9}
        and snapshot["residual_period_census"] == {2: 2, 3: 9}
        and snapshot["open_count"] == 165
        and snapshot["open_minimum_weight_census"]
        == {1: 114, 2: 19, 3: 16, 4: 7, 5: 1, 6: 1, 7: 7}
        and snapshot["all_certified_cycles_forever_nonzero"]
        and result["noninitial_full_state_repeats"] == 0
        and result["periodic_keys"] == EXPECTED_PERIODIC_KEYS_T64
        and result["on_cycle_content_census"]
        == expected_on_cycle_content_census()
        and result["classification_sha256"]
        == EXPECTED_T64_CLASSIFICATION_SHA256
    )
    return result


def relation(period: int, constant: int) -> str:
    if period == constant:
        return "equal"
    if constant % period == 0:
        return "period_divides_constant"
    if period % constant == 0:
        return "period_is_multiple_of_constant"
    return "neither"


def structural_period_census(
    family: dict[str, object],
    census: dict[str, object],
) -> dict[str, object]:
    records = census["records"]
    cycles = [
        record
        for record in records.values()
        if record["cycle_closure"] is not None
        and record["cycle_closure"] <= HORIZONS[-1]
    ]
    period_counts = Counter(
        record["residual_period"] for record in cycles
    )
    state_period_counts = Counter(
        record["state_period"] for record in cycles
    )
    constants = [
        ("orbit_length", LANDED_ORBIT_LENGTH),
        ("station_count", len(family["program"])),
    ]
    constants.extend(
        (f"bank_count_{count}", count)
        for count in LANDED_BANK_COUNTS
    )
    constants.extend(
        (f"bank_{index}_register_width", width)
        for index, width in enumerate(
            family["summary"]["bank_register_widths"]
        )
    )
    rows = tuple(
        {
            "period": period,
            "keys": count,
            "relations": {
                label: {
                    "constant": constant,
                    "relation": relation(period, constant),
                }
                for label, constant in constants
            },
        }
        for period, count in sorted(period_counts.items())
    )
    return {
        "definition":
            "Pure integer divisibility data; no numerological inference",
        "period_basis": "least residual phase period on a certified full-state cycle",
        "structural_constants": dict(constants),
        "period_census": dict(sorted(period_counts.items())),
        "certifying_state_period_census":
            dict(sorted(state_period_counts.items())),
        "rows": rows,
        "cycles": len(cycles),
        "all_cycle_entries": dict(
            sorted(Counter(record["cycle_start"] for record in cycles).items())
        ),
        "all_cycles_forever_nonzero": all(
            record["cycle_nonzero"] for record in cycles
        ),
    }


def public_snapshot(snapshot: dict[str, object]) -> dict[str, object]:
    return {
        key: value
        for key, value in snapshot.items()
        if key not in {"clean_keys", "cycle_keys", "open_keys"}
    }


def frozen_outcome(census: dict[str, object]) -> dict[str, object]:
    records = census["records"]
    clean_beyond_64 = tuple(
        {
            "event": key[0],
            "positions": key[1],
            "first_clean_time": record["first_clean"],
        }
        for key, record in sorted(records.items())
        if record["first_clean"] is not None
        and 64 < record["first_clean"] <= HORIZONS[-1]
    )
    final = census["snapshots"][HORIZONS[-1]]
    if clean_beyond_64:
        name = "HORIZON_CLOSES"
        statement = (
            "At least one configuration first becomes clean beyond T=64; "
            "the veto evidence base changes at landed scope."
        )
    elif (
        final["clean_count"] == 0
        and final["cycle_count"] == final["keys"] == 176
        and final["open_count"] == 0
        and final["all_certified_cycles_forever_nonzero"]
    ):
        name = "RESIDUAL_PERMANENT_AT_SCOPE"
        statement = (
            "No configuration is clean through T=256 and every landed key "
            "is on a certified forever-nonzero residual cycle."
        )
    else:
        name = "NO_FROZEN_OUTCOME_CONDITION_MET"
        statement = (
            "The bounded data satisfy neither frozen terminal condition."
        )
    return {
        "outcome": name,
        "statement": statement,
        "clean_beyond_64": clean_beyond_64,
        "physical_question": PHYSICAL_SCOPE,
    }


def run() -> int:
    started = monotonic()

    machinery = machinery_certificate()
    check("A_anchors_and_machinery_basis", machinery["pass"])
    OUTPUT_LINES.append(
        "DATA A "
        + compact(
            {
                "machinery_basis": machinery["machinery_basis"],
                "reason": machinery["reason"],
                "lineage_commit": machinery["lineage_commit"],
                "input_sha256": machinery["input_sha256"],
                "git_blob_ids": machinery["git_blob_ids"],
                "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
            }
        )
    )

    family = build_family()
    census = cycle_census(family)
    identity = t64_identity(family, census)
    check("B_T64_identity_control", identity["pass"])
    OUTPUT_LINES.append(
        "DATA B "
        + compact(
            {
                "keys": identity["snapshot"]["keys"],
                "clean": identity["snapshot"]["clean_count"],
                "cycles": identity["snapshot"]["cycle_count"],
                "open": identity["snapshot"]["open_count"],
                "state_period_census":
                    identity["snapshot"]["state_period_census"],
                "residual_period_census":
                    identity["snapshot"]["residual_period_census"],
                "periodic_keys": identity["periodic_keys"],
                "on_cycle_content_census":
                    identity["on_cycle_content_census"],
                "classification_sha256":
                    identity["classification_sha256"],
                "family_sha256": family["summary"]["family_sha256"],
            }
        )
    )

    snapshots = census["snapshots"]
    terminal_coverage = (
        snapshots[256]["clean_count"]
        + snapshots[256]["cycle_count"]
        == snapshots[256]["keys"]
        and snapshots[256]["open_count"] == 0
    )
    horizon_closes = (
        snapshots[256]["clean_count"] > snapshots[64]["clean_count"]
    )
    table_complete = (
        len(census["table_rows"]) == 176
        and all(
            tuple(row) == ("event", "positions", "T64", "T128", "T256")
            for row in census["table_rows"]
        )
    )
    c_pass = (
        all(
            snapshots[horizon]["keys"] == 176
            and (
                snapshots[horizon]["clean_count"]
                + snapshots[horizon]["cycle_count"]
                + snapshots[horizon]["open_count"]
                == 176
            )
            for horizon in HORIZONS
        )
        and table_complete
        and (horizon_closes or terminal_coverage)
    )
    check("C_T128_T256_census_table", c_pass)
    OUTPUT_LINES.append(
        "DATA C_COUNTS "
        + compact(
            {
                f"T{horizon}": public_snapshot(snapshots[horizon])
                for horizon in HORIZONS
            }
        )
    )
    OUTPUT_LINES.append(
        "DATA C_TIMING " + compact(census["segment_timings"])
    )
    for index, row in enumerate(census["table_rows"]):
        OUTPUT_LINES.append(
            f"DATA C_TABLE row={index:03d} "
            f"event={row['event']} positions={row['positions']} "
            f"T64={row['T64']} T128={row['T128']} T256={row['T256']}"
        )

    structural = structural_period_census(family, census)
    outcome = frozen_outcome(census)
    frozen_valid = (
        (
            outcome["outcome"] == "HORIZON_CLOSES"
            and bool(outcome["clean_beyond_64"])
        )
        or (
            outcome["outcome"] == "RESIDUAL_PERMANENT_AT_SCOPE"
            and snapshots[256]["clean_count"] == 0
            and snapshots[256]["cycle_count"] == 176
            and snapshots[256]["open_count"] == 0
        )
    )
    d_pass = (
        frozen_valid
        and structural["cycles"] == snapshots[256]["cycle_count"]
        and sum(structural["period_census"].values())
        == structural["cycles"]
        and structural["all_cycles_forever_nonzero"]
        and outcome["physical_question"] == PHYSICAL_SCOPE
    )
    check("D_period_divisibility_and_frozen_outcome", d_pass)
    OUTPUT_LINES.append(
        "DATA D_PERIOD_CENSUS "
        + compact(
            {
                "period_basis": structural["period_basis"],
                "period_census": structural["period_census"],
                "certifying_state_period_census":
                    structural["certifying_state_period_census"],
                "cycle_entry_census": structural["all_cycle_entries"],
                "structural_constants":
                    structural["structural_constants"],
                "interpretive_limit": structural["definition"],
            }
        )
    )
    for row in structural["rows"]:
        OUTPUT_LINES.append("DATA D_DIVISIBILITY " + compact(row))
    OUTPUT_LINES.append("DATA D_OUTCOME " + compact(outcome))

    replay = cycle_census(family)
    determinism = (
        replay["deterministic_sha256"]
        == census["deterministic_sha256"]
        and replay["table_sha256"] == census["table_sha256"]
        and {
            horizon: public_snapshot(replay["snapshots"][horizon])
            for horizon in HORIZONS
        }
        == {
            horizon: public_snapshot(census["snapshots"][horizon])
            for horizon in HORIZONS
        }
    )
    elapsed = monotonic() - started
    report_core = {
        "AUDIT_TIMEOUT_SEC": AUDIT_TIMEOUT_SEC,
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "machinery_basis": machinery["machinery_basis"],
        "family": family["summary"],
        "snapshots": {
            str(horizon): public_snapshot(snapshots[horizon])
            for horizon in HORIZONS
        },
        "T64_classification_sha256": identity["classification_sha256"],
        "table_sha256": census["table_sha256"],
        "deterministic_sha256": census["deterministic_sha256"],
        "replay_deterministic_sha256": replay["deterministic_sha256"],
        "period_census": structural["period_census"],
        "outcome": outcome,
        "physical_question": PHYSICAL_SCOPE,
        "timing_seconds": {
            "family": family["summary"]["runtime_seconds"],
            "primary_census": census["runtime_seconds"],
            "determinism_replay": replay["runtime_seconds"],
            "total": round(elapsed, 6),
        },
    }
    estimated_report = {
        **report_core,
        "checks": {**CHECKS, "E_determinism_and_bounds": True},
    }
    projected = (
        "\n".join(OUTPUT_LINES)
        + "\nPASS E_determinism_and_bounds\n"
        + compact(estimated_report)
        + "\n"
    )
    e_pass = (
        determinism
        and elapsed < AUDIT_TIMEOUT_SEC
        and len(projected.encode("utf-8")) < STDOUT_LIMIT_BYTES
    )
    check("E_determinism_and_bounds", e_pass)
    OUTPUT_LINES.append(
        "DATA E "
        + compact(
            {
                "deterministic": determinism,
                "primary_sha256": census["deterministic_sha256"],
                "replay_sha256": replay["deterministic_sha256"],
                "runtime_seconds": round(elapsed, 6),
                "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
                "projected_stdout_bytes": len(projected.encode("utf-8")),
                "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            }
        )
    )

    report = {
        **report_core,
        "checks": dict(CHECKS),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "pass": all(CHECKS.values()),
    }
    report["terminal"] = (
        "CYCLE790_HORIZON_EXTENSION_PASS"
        if report["pass"]
        else "CYCLE790_HORIZON_EXTENSION_HONEST_FAIL"
    )
    report["report_sha256"] = digest_rows(report)
    output = "\n".join(OUTPUT_LINES) + "\n" + compact(report) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        failure = {
            "pass": False,
            "terminal": "CYCLE790_HORIZON_EXTENSION_HONEST_FAIL",
            "failure": "stdout bound exceeded",
            "bytes": len(output.encode("utf-8")),
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
            "terminal": "CYCLE790_HORIZON_EXTENSION_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
            "physical_question": PHYSICAL_SCOPE,
        }
        if OUTPUT_LINES:
            sys.stdout.write("\n".join(OUTPUT_LINES) + "\n")
        sys.stdout.write(compact(failure) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
