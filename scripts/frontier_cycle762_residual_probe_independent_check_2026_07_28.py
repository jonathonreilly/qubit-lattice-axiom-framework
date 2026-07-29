#!/usr/bin/env python3
"""Independent checker for Cycle 762 plus the horizon-64 residue census.

The Cycle 762 primary is parsed only as AST data.  Its probe algorithms are
not executed or imported.  All dynamics and all four censuses below are
implemented here from the two declared controller inputs.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/RESIDUAL_AS_CONTENT_PROBE_CYCLE762_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import ast
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations
import json
from math import comb
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


PRIMARY_DATA_PATH = (
    "scripts/frontier_cycle762_residual_as_content_probe_2026_07_28.py"
)
PRIMARY_MODULE_NAME = (
    "frontier_cycle762_residual_as_content_probe_2026_07_28"
)
IMPORT_BLOCKLIST = (PRIMARY_MODULE_NAME,)
RING_STATIONS = 11
FIXTURE_BANKS = 2
PRIMARY_HORIZON = 16
ASYMPTOTIC_HORIZON = 64
STDOUT_LIMIT_BYTES = 150 * 1024

OUTCOME = "NO_FAMILY_WIDE_RESIDUAL_CONTENT_LAW"
OUTCOME_STATEMENT = (
    "The 176-key residue changes nonconservatively, the 25 signatures "
    "do not close or support a descended XOR cocycle, and signature "
    "classes split by continued orbit behavior.  These exact negatives "
    "sharpen the forcing entry."
)
OUTCOME_SCOPE = (
    "This is an exhaustive characterization of the supplied 176 "
    "ring-11/two-bank keys through a declared 16-update continuation "
    "window.  Nonclosure within that window is not an infinite-time "
    "aperiodicity claim, and no selection, supplier, higher-k, "
    "arbitrary-ring, genesis, renewal, or W3 conclusion is made."
)

EXPECTED_PERIODIC_KEYS = (
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


def literal_assignment(tree: ast.Module, name: str) -> object:
    matches = []
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        if any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            matches.append(ast.literal_eval(node.value))
    if len(matches) != 1:
        raise AssertionError(("literal assignment", name, len(matches)))
    return matches[0]


def extraction() -> dict[str, object]:
    """Extract only literal declarations and assertion structure from 762."""

    if PRIMARY_MODULE_NAME in sys.modules:
        raise AssertionError("Cycle 762 primary was imported")
    source = (ROOT / PRIMARY_DATA_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_DATA_PATH)
    audit_literals = {
        "AUDIT_TIMEOUT_SEC": literal_assignment(
            tree, "AUDIT_TIMEOUT_SEC"
        ),
        "NOTE_PATH": literal_assignment(tree, "NOTE_PATH"),
        "AUDIT_INPUT_PATHS": literal_assignment(
            tree, "AUDIT_INPUT_PATHS"
        ),
    }
    functions = {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    check_labels = tuple(
        node.args[0].value
        for node in ast.walk(functions["main"])
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "check"
        and node.args
        and isinstance(node.args[0], ast.Constant)
        and isinstance(node.args[0].value, str)
    )
    required_labels = (
        "A_anchors_and_Cycle759_176_key_map_reextracted",
        "B_conservation_transport_period_growth_census_exact",
        "C_25_signature_algebra_and_two_step_cocycle_census_exact",
        "D_signature_sector_orbit_behavior_census_exact",
        "E_honest_outcome_keys_no_selection_or_new_supplier",
        "OUTPUT_stdout_under_150KB_and_runtime_bounded",
    )
    constants = {
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
    }
    expected_functions = {
        "continuation_census",
        "algebra_census",
        "sector_census",
        "outcome_certificate",
    }
    target_censuses = {
        "conservation": {
            "signature_invariant_keys": 0,
            "keys": 176,
            "periodic_within_16": 11,
            "keys_with_weight_decrease": 176,
        },
        "algebra": {
            "ordered_pairs": 625,
            "xor_failures": 588,
            "cocycle_failures": 0,
            "status": "KINEMATIC_COBoundary_IDENTITY",
        },
        "sectors": {
            "split_classes": 16,
            "classes": 28,
            "discordant_pairs": 1960,
        },
        "outcome": OUTCOME,
    }
    passed = (
        audit_literals["AUDIT_TIMEOUT_SEC"] == AUDIT_TIMEOUT_SEC
        and audit_literals["NOTE_PATH"] == NOTE_PATH
        and audit_literals["AUDIT_INPUT_PATHS"] == AUDIT_INPUT_PATHS
        and set(check_labels) == set(required_labels)
        and expected_functions <= set(functions)
        and OUTCOME in constants
        and OUTCOME_STATEMENT in constants
        and OUTCOME_SCOPE in constants
        and PRIMARY_MODULE_NAME not in sys.modules
    )
    return {
        "primary_path": PRIMARY_DATA_PATH,
        "read_as_AST_data_only": True,
        "primary_imported": PRIMARY_MODULE_NAME in sys.modules,
        "AUDIT_literal_eval": audit_literals,
        "primary_check_labels": check_labels,
        "required_probe_functions_present": tuple(
            sorted(expected_functions & set(functions))
        ),
        "target_censuses": target_censuses,
        "outcome_language_verbatim": {
            "outcome": OUTCOME,
            "statement": OUTCOME_STATEMENT,
            "scope": OUTCOME_SCOPE,
        },
        "source_sha256": sha256(source.encode("utf-8")).hexdigest(),
        "pass": passed,
    }


def separated_k2_positions() -> tuple[tuple[int, int], ...]:
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
    program: tuple[object, ...], positions0: tuple[int, int]
) -> tuple[object, ...]:
    """Independent synchronous composition of the two moving controls."""

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
    """Own exact support projection of the postimage-cleanliness registers."""

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
    """Reconstruct the four epochs and 176 post-update states."""

    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
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
        "family_sha256": digest_rows(
            tuple(
                (key, canonical_support(residues[key]))
                for key in sorted(residues)
            )
        ),
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


def probes_recount(family: dict[str, object]) -> dict[str, object]:
    """Independently rerun conservation, algebra, and sector probes."""

    states = family["states"]
    words = family["words"]
    frozen_residues = family["residues"]
    traces: dict[Key, tuple[Support, ...]] = {}
    state_periods: Counter[int | None] = Counter()
    invariant = 0
    fixed_weight_transport = 0
    keys_with_decrease = 0
    noninitial_repeats = 0
    for key, state0 in states.items():
        state = state0
        seen = {state: 0}
        period = None
        trace = [frozen_residues[key]]
        for update in range(1, PRIMARY_HORIZON + 1):
            state = K.A.apply_semantic(state, words[key[1]])
            trace.append(residual_support(state))
            if period is None and state in seen:
                noninitial_repeats += seen[state] != 0
                period = update - seen[state]
            seen.setdefault(state, update)
        traces[key] = tuple(trace)
        weights = tuple(map(len, trace))
        distinct = len(set(trace))
        invariant += distinct == 1
        fixed_weight_transport += len(set(weights)) == 1 and distinct > 1
        keys_with_decrease += any(
            weights[index + 1] < weights[index]
            for index in range(PRIMARY_HORIZON)
        )
        state_periods[period] += 1

    conservation = {
        "keys": len(traces),
        "signature_invariant_keys": invariant,
        "fixed_weight_transport_keys": fixed_weight_transport,
        "exact_full_state_periodic_keys_within_16": sum(
            count
            for period, count in state_periods.items()
            if period is not None
        ),
        "full_state_period_census": {
            ("not_closed_within_16" if period is None else str(period)):
            count
            for period, count in sorted(
                state_periods.items(),
                key=lambda item: (
                    item[0] is None,
                    item[0] if item[0] is not None else 0,
                ),
            )
        },
        "keys_with_a_residual_weight_decrease": keys_with_decrease,
        "noninitial_full_state_repeats": noninitial_repeats,
        "family_wide_conservation_or_transport": (
            invariant == len(traces)
            or fixed_weight_transport == len(traces)
        ),
    }

    frozen = set(frozen_residues.values())
    frozen_with_zero = frozen | {frozenset()}
    pair_cases = 0
    pair_closed = 0
    for left in frozen:
        for right in frozen:
            pair_cases += 1
            pair_closed += (left ^ right) in frozen_with_zero
    cocycle_failures = 0
    absolute_additive_cases = 0
    successor: dict[Support, set[Support]] = defaultdict(set)
    increments: dict[Support, set[Support]] = defaultdict(set)
    for trace in traces.values():
        r0, r1, r2 = trace[:3]
        delta01 = r0 ^ r1
        delta12 = r1 ^ r2
        delta02 = r0 ^ r2
        cocycle_failures += (delta01 ^ delta12) != delta02
        absolute_additive_cases += r2 == (r0 ^ r1)
        successor[r0].add(r1)
        increments[r0].add(delta01)
    successor_splits = sum(len(outputs) > 1 for outputs in successor.values())
    increment_splits = sum(
        len(outputs) > 1 for outputs in increments.values()
    )
    algebra = {
        "frozen_signatures": len(frozen),
        "ordered_frozen_signature_pairs": pair_cases,
        "xor_outputs_in_set_with_zero": pair_closed,
        "xor_outputs_outside_set_with_zero": pair_cases - pair_closed,
        "closed_25_signature_XOR_algebra": pair_closed == pair_cases,
        "two_step_cocycle_cases": len(traces),
        "two_step_cocycle_failures": cocycle_failures,
        "cocycle_status": (
            "KINEMATIC_COBoundary_IDENTITY"
            if cocycle_failures == 0
            else "COCYCLE_FAILURE"
        ),
        "absolute_residue_XOR_additive_cases":
            absolute_additive_cases,
        "successor_split_classes": successor_splits,
        "increment_split_classes": increment_splits,
        "coboundary_only": (
            cocycle_failures == 0
            and pair_closed != pair_cases
            and successor_splits > 0
            and increment_splits > 0
        ),
    }

    total_classes = 0
    homogeneous_classes = 0
    split_classes = 0
    within_pairs = 0
    matching_pairs = 0
    discordant_pairs = 0
    classes_by_epoch = []
    for event in range(2 * FIXTURE_BANKS):
        groups: dict[Support, list[Key]] = defaultdict(list)
        for key, residue in frozen_residues.items():
            if key[0] == event:
                groups[residue].append(key)
        classes_by_epoch.append(len(groups))
        for members in groups.values():
            behaviors = Counter(traces[key][1:] for key in members)
            pairs = comb(len(members), 2)
            matching = sum(
                comb(count, 2) for count in behaviors.values()
            )
            total_classes += 1
            homogeneous_classes += len(behaviors) == 1
            split_classes += len(behaviors) > 1
            within_pairs += pairs
            matching_pairs += matching
            discordant_pairs += pairs - matching
    sectors = {
        "signature_classes_per_epoch": tuple(classes_by_epoch),
        "total_epoch_signature_classes": total_classes,
        "orbit_homogeneous_classes": homogeneous_classes,
        "orbit_split_classes": split_classes,
        "within_signature_unordered_pairs": within_pairs,
        "matching_orbit_behavior_pairs": matching_pairs,
        "discordant_orbit_behavior_pairs": discordant_pairs,
        "derived_quantum_number_on_probe": split_classes == 0,
    }

    outcome = {
        "outcome": OUTCOME,
        "statement": OUTCOME_STATEMENT,
        "scope_statement": OUTCOME_SCOPE,
        "three_failed_candidates": (
            "family-wide conservation or fixed-weight transport",
            "closed descended XOR cocycle algebra",
            "orbit-homogeneous residual-signature sectors",
        ),
    }
    passed = (
        family["summary"]["pass"]
        and conservation["keys"] == 176
        and conservation["signature_invariant_keys"] == 0
        and conservation["exact_full_state_periodic_keys_within_16"] == 11
        and conservation["full_state_period_census"]
        == {"2": 2, "3": 9, "not_closed_within_16": 165}
        and conservation["keys_with_a_residual_weight_decrease"] == 176
        and conservation["noninitial_full_state_repeats"] == 0
        and not conservation["family_wide_conservation_or_transport"]
        and algebra["frozen_signatures"] == 25
        and algebra["ordered_frozen_signature_pairs"] == 625
        and algebra["xor_outputs_in_set_with_zero"] == 37
        and algebra["xor_outputs_outside_set_with_zero"] == 588
        and algebra["two_step_cocycle_cases"] == 176
        and algebra["two_step_cocycle_failures"] == 0
        and algebra["cocycle_status"]
        == "KINEMATIC_COBoundary_IDENTITY"
        and algebra["absolute_residue_XOR_additive_cases"] == 0
        and algebra["successor_split_classes"] == 13
        and algebra["increment_split_classes"] == 13
        and algebra["coboundary_only"]
        and sectors["signature_classes_per_epoch"] == (1, 1, 12, 14)
        and sectors["total_epoch_signature_classes"] == 28
        and sectors["orbit_homogeneous_classes"] == 12
        and sectors["orbit_split_classes"] == 16
        and sectors["within_signature_unordered_pairs"] == 2107
        and sectors["matching_orbit_behavior_pairs"] == 147
        and sectors["discordant_orbit_behavior_pairs"] == 1960
        and not sectors["derived_quantum_number_on_probe"]
    )
    return {
        "family": family["summary"],
        "conservation": conservation,
        "algebra": algebra,
        "sectors": sectors,
        "outcome": outcome,
        "trace_sha256": digest_rows(
            tuple(
                (
                    key,
                    tuple(canonical_support(row) for row in traces[key]),
                )
                for key in sorted(traces)
            )
        ),
        "pass": passed,
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


def asymptotic_census(family: dict[str, object]) -> dict[str, object]:
    """Classify all 176 keys through update 64, freezing exact cycles."""

    states = family["states"]
    words = family["words"]
    delayed_clean_times: Counter[int] = Counter()
    nonzero_cycle_lengths: Counter[int] = Counter()
    classifications = []
    on_cycle_rows = []
    on_cycle_content: Counter[
        tuple[int, tuple[tuple[Coordinate, ...], ...]]
    ] = Counter()
    unresolved_minimum_weights: Counter[int] = Counter()
    noninitial_repeats = 0

    for key in sorted(states):
        state = states[key]
        residues = [residual_support(state)]
        seen = {state: 0}
        first_clean = 0 if not residues[0] else None
        cycle_start = None
        period = None
        for update in range(1, ASYMPTOTIC_HORIZON + 1):
            state = K.A.apply_semantic(state, words[key[1]])
            residue = residual_support(state)
            residues.append(residue)
            if first_clean is None and not residue:
                first_clean = update
            if period is None and state in seen:
                cycle_start = seen[state]
                period = update - cycle_start
                noninitial_repeats += cycle_start != 0
            seen.setdefault(state, update)

        base = {
            "event": key[0],
            "positions": key[1],
            "minimum_residue_weight": min(map(len, residues)),
            "distinct_residues_through_64": len(set(residues)),
        }
        if first_clean is not None:
            delayed_clean_times[first_clean] += 1
            row = {
                **base,
                "classification": "reaches_zero",
                "first_clean_update": first_clean,
            }
        elif period is not None:
            if cycle_start is None:
                raise AssertionError(("missing cycle start", key))
            phases = tuple(
                canonical_support(row)
                for row in residues[
                    cycle_start:cycle_start + period
                ]
            )
            nonzero_cycle_lengths[period] += 1
            on_cycle_content[(period, phases)] += 1
            on_cycle_rows.append(
                {
                    "event": key[0],
                    "positions": key[1],
                    "cycle_start": cycle_start,
                    "cycle_length": period,
                    "residue_phases": phases,
                    "phase_weights": tuple(map(len, phases)),
                }
            )
            row = {
                **base,
                "classification": "nonzero_limit_cycle",
                "cycle_start": cycle_start,
                "cycle_length": period,
            }
        else:
            unresolved_minimum_weights[base["minimum_residue_weight"]] += 1
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
            on_cycle_content.items(),
            key=lambda item: (item[0][0], item[0][1]),
        )
    )
    clean_count = sum(delayed_clean_times.values())
    cycle_count = sum(nonzero_cycle_lengths.values())
    unresolved_count = (
        len(classifications) - clean_count - cycle_count
    )
    periodic_keys = tuple(
        (
            row["event"],
            tuple(row["positions"]),
            row["cycle_length"],
        )
        for row in on_cycle_rows
    )
    result = {
        "definition": (
            "t=0 is each Cycle-762 post-update state; each t=1..64 is "
            "one further lawful exact synchronous k=2 controller update"
        ),
        "keys": len(classifications),
        "horizon_updates": ASYMPTOTIC_HORIZON,
        "projected_states_per_key": ASYMPTOTIC_HORIZON + 1,
        "reaches_zero_keys": clean_count,
        "first_clean_time_census": {
            str(time): count
            for time, count in sorted(delayed_clean_times.items())
        },
        "nonzero_limit_cycle_keys": cycle_count,
        "nonzero_cycle_length_census": {
            str(period): count
            for period, count in sorted(nonzero_cycle_lengths.items())
        },
        "not_clean_or_closed_within_64_keys": unresolved_count,
        "unresolved_minimum_weight_census": {
            str(weight): count
            for weight, count in sorted(
                unresolved_minimum_weights.items()
            )
        },
        "noninitial_full_state_repeats": noninitial_repeats,
        "periodic_keys": periodic_keys,
        "on_cycle_content_census": content_census,
        "on_cycle_rows": tuple(on_cycle_rows),
        "key_classification_rows": tuple(classifications),
        "classification_sha256": digest_rows(classifications),
        "periodic_cycles_are_forever_nonzero": all(
            all(phase for phase in row["residue_phases"])
            for row in on_cycle_rows
        ),
        "delayed_cleanliness_result": (
            "NO_KEY_REACHES_ZERO_THROUGH_T64; THE_11_CLOSED_KEYS_ARE_"
            "EXACT_NONZERO_CYCLES_AND_NEVER_CLEAN; 165_KEYS_REMAIN_"
            "UNRESOLVED_BEYOND_THE_BOUND"
        ),
    }
    result["pass"] = (
        result["keys"] == 176
        and result["horizon_updates"] == 64
        and result["projected_states_per_key"] == 65
        and result["reaches_zero_keys"] == 0
        and result["first_clean_time_census"] == {}
        and result["nonzero_limit_cycle_keys"] == 11
        and result["nonzero_cycle_length_census"]
        == {"2": 2, "3": 9}
        and result["not_clean_or_closed_within_64_keys"] == 165
        and result["unresolved_minimum_weight_census"]
        == {"1": 114, "2": 19, "3": 16, "4": 7, "5": 1, "6": 1, "7": 7}
        and result["noninitial_full_state_repeats"] == 0
        and result["periodic_keys"] == EXPECTED_PERIODIC_KEYS
        and result["on_cycle_content_census"]
        == expected_on_cycle_content_census()
        and result["periodic_cycles_are_forever_nonzero"]
        and (
            result["reaches_zero_keys"]
            + result["nonzero_limit_cycle_keys"]
            + result["not_clean_or_closed_within_64_keys"]
            == result["keys"]
        )
    )
    return result


def discipline(
    extracted: dict[str, object],
    recount: dict[str, object],
    asymptotic: dict[str, object],
) -> dict[str, object]:
    """Audit import isolation, exact language, and the forcing summary."""

    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=Path(__file__).name)
    imported_modules = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_modules.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_modules.append(node.module)
    blocklist_hits = tuple(
        name
        for name in imported_modules
        if any(
            name == blocked or name.startswith(blocked + ".")
            for blocked in IMPORT_BLOCKLIST
        )
    )
    forbidden_execution_calls = tuple(
        node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in {"eval", "exec", "compile", "__import__"}
    )
    header_value = None
    header_is_pure_literal_tuple = False
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name)
                and target.id == "AUDIT_INPUT_PATHS"
                for target in node.targets
            )
        ):
            header_is_pure_literal_tuple = (
                isinstance(node.value, ast.Tuple)
                and all(
                    isinstance(element, ast.Constant)
                    and isinstance(element.value, str)
                    for element in node.value.elts
                )
            )
            if header_is_pure_literal_tuple:
                header_value = ast.literal_eval(node.value)

    forcing_chain_summary = {
        "three_failures": recount["outcome"][
            "three_failed_candidates"
        ],
        "two_exhaustive_observed_families_at_T64": {
            "exact_nonzero_periodic": asymptotic[
                "nonzero_limit_cycle_keys"
            ],
            "not_clean_or_closed_within_bound": asymptotic[
                "not_clean_or_closed_within_64_keys"
            ],
        },
        "zero_reaching_family_is_empty": (
            asymptotic["reaches_zero_keys"] == 0
        ),
        "interpretation": (
            "The three Cycle-762 content-law candidates fail.  At T=64 "
            "the 176 supplied keys split into two nonempty observed "
            "families: 11 exact nonzero-periodic keys, whose frozen "
            "on-cycle residue proves they never clean, and 165 keys "
            "that neither clean nor close within the bound."
        ),
    }
    outcome = recount["outcome"]
    passed = (
        not blocklist_hits
        and not forbidden_execution_calls
        and PRIMARY_MODULE_NAME not in sys.modules
        and header_is_pure_literal_tuple
        and header_value == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS
        == (
            "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
        )
        and extracted["read_as_AST_data_only"]
        and not extracted["primary_imported"]
        and outcome["outcome"] == OUTCOME
        and outcome["statement"] == OUTCOME_STATEMENT
        and outcome["scope_statement"] == OUTCOME_SCOPE
        and len(forcing_chain_summary["three_failures"]) == 3
        and forcing_chain_summary[
            "two_exhaustive_observed_families_at_T64"
        ]
        == {
            "exact_nonzero_periodic": 11,
            "not_clean_or_closed_within_bound": 165,
        }
        and forcing_chain_summary["zero_reaching_family_is_empty"]
    )
    return {
        "blocklist": IMPORT_BLOCKLIST,
        "blocklist_import_hits": blocklist_hits,
        "primary_in_sys_modules": PRIMARY_MODULE_NAME in sys.modules,
        "forbidden_primary_execution_calls": forbidden_execution_calls,
        "AUDIT_INPUT_PATHS_is_pure_literal_tuple":
            header_is_pure_literal_tuple,
        "outcome_language_verbatim": outcome,
        "forcing_chain_summary": forcing_chain_summary,
        "pass": passed,
    }


def run() -> int:
    started = monotonic()
    extracted = extraction()
    check("A_extraction_AST_data_and_AUDIT_literal_eval", extracted["pass"])

    family = build_family()
    recount = probes_recount(family)
    check(
        "B_own_three_probe_recounts_exact",
        recount["pass"],
    )

    asymptotic = asymptotic_census(family)
    check(
        "C_horizon64_asymptotic_census_exhaustive_and_exact",
        asymptotic["pass"],
    )

    disciplined = discipline(extracted, recount, asymptotic)
    check(
        "D_blocklist_outcome_and_forcing_chain_discipline",
        disciplined["pass"],
    )

    elapsed = monotonic() - started
    report = {
        "AUDIT_TIMEOUT_SEC": AUDIT_TIMEOUT_SEC,
        "NOTE_PATH": NOTE_PATH,
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "certificate_1_extraction": extracted,
        "certificate_2_probes_recount": recount,
        "certificate_3_asymptotic_census": asymptotic,
        "certificate_4_discipline": disciplined,
        "runtime_seconds": round(elapsed, 6),
    }
    projected_output = (
        "\n".join(OUTPUT_LINES)
        + "\n"
        + compact(report)
        + "\n"
    )
    check(
        "OUTPUT_runtime_and_stdout_bounded",
        elapsed < AUDIT_TIMEOUT_SEC
        and len(projected_output.encode("utf-8"))
        < STDOUT_LIMIT_BYTES - 4096,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE762_RESIDUAL_PROBE_INDEPENDENT_CHECK_PASS"
        if report["pass"]
        else "CYCLE762_RESIDUAL_PROBE_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    report["report_sha256"] = digest_rows(report)
    output = "\n".join(OUTPUT_LINES) + "\n" + compact(report) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        failure = {
            "pass": False,
            "terminal":
                "CYCLE762_RESIDUAL_PROBE_INDEPENDENT_CHECK_HONEST_FAIL",
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
            "checks": dict(sorted(CHECKS.items())),
            "pass": False,
            "terminal":
                "CYCLE762_RESIDUAL_PROBE_INDEPENDENT_CHECK_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }
        sys.stdout.write("\n".join(OUTPUT_LINES) + "\n")
        sys.stdout.write(compact(failure) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
