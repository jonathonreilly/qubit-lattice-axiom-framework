#!/usr/bin/env python3
"""Cycle 805 independent adversarial relabeling check and full-family extension.

The Cycle-805 primary is a SHA-pinned text/AST comparator only.  This checker
rebuilds the selector batteries from the landed Cycle-719 construction,
attacks commutation at intermediate controller-step checkpoints, and closes
the omitted bank-5/12 scope by an exhaustive one-token operator conjugacy.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle805_supply_relabeling_tournament_2026_07_28.py",
    "scripts/frontier_cycle802_enlarged_born_table_2026_07_28.py",
    "scripts/frontier_cycle802_enlarged_table_independent_check_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from hashlib import sha256
import importlib.abc
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
START = monotonic()
PRIMARY_MODULE = "frontier_cycle805_supply_relabeling_tournament_2026_07_28"
EXPECTED_INPUT_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "04432816e3844043b419de8d91001003cd7fb8de76635658c3367574c3e44b9a",
    AUDIT_INPUT_PATHS[1]:
        "9670fdfcbd0b982484811abe5d91d7099afb815bcc5d5ee2929dc41633ab0fdd",
    AUDIT_INPUT_PATHS[2]:
        "e76535b6576ff1665e618170ece068404bf7b47557b9a0f2a27c058f75440e33",
    AUDIT_INPUT_PATHS[3]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
BANKS_FULL = (1, 2, 3, 5, 12)
PRIMARY_BANKS = (1, 2, 3)
EXTENSION_BANKS = (5, 12)
LAYER_CHOICES = (
    ("Q_then_R", "ascending"),
    ("Q_then_R", "descending"),
    ("Q_then_R", "even_then_odd"),
    ("R_then_Q", "ascending"),
    ("R_then_Q", "descending"),
    ("R_then_Q", "even_then_odd"),
)
FROZEN_ASSIGNMENT = (
    (0, 1, 2),
    (1, 2, 0),
    (2, 0, 1),
)
LANDED_38_COUNTS = (
    (13, 128, 68),
    (232, 97, 1),
    (146, 5, 432),
    (391, 230, 501),
)
PRIMITIVE_MULTIPLICITIES = (17, 29, 54)

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


class _PrimaryBlocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname == PRIMARY_MODULE:
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


PRIMARY_BLOCKER = _PrimaryBlocker()
sys.meta_path.insert(0, PRIMARY_BLOCKER)
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K719


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def file_sha256(path: str) -> str:
    return sha256((ROOT / path).read_bytes()).hexdigest()


def emit(*parts: object) -> None:
    OUTPUT_LINES.append(" ".join(str(part) for part in parts))


def check(label: str, condition: bool, detail: object) -> None:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    emit("PASS" if passed else "FAIL", label, "::", compact(detail))


def rotate_left(values: tuple, amount: int) -> tuple:
    amount %= len(values)
    return values[amount:] + values[:amount]


def q_order(stations: int, mode: str) -> tuple[int, ...]:
    if mode == "ascending":
        return tuple(range(stations))
    if mode == "descending":
        return tuple(reversed(range(stations)))
    if mode == "even_then_odd":
        return tuple(range(0, stations, 2)) + tuple(range(1, stations, 2))
    raise ValueError(mode)


def settings(
    supply_id: str,
    choice: str,
    stations: int,
) -> dict[str, object]:
    if supply_id == "inherited_1":
        source = {
            "source_index=0": 0,
            "source_index=1": 1,
            "source_index=stations-1": stations - 1,
        }[choice]
        return {
            "supply_id": supply_id,
            "choice": choice,
            "program_rotation": (-source) % stations,
            "layer_order": "Q_then_R",
            "order_mode": "ascending",
        }
    if supply_id == "inherited_2":
        rotation = {
            "left_rotation=0": 0,
            "left_rotation=1": 1,
            "left_rotation=stations-1": stations - 1,
        }[choice]
        return {
            "supply_id": supply_id,
            "choice": choice,
            "program_rotation": rotation,
            "layer_order": "Q_then_R",
            "order_mode": "ascending",
        }
    if supply_id == "inherited_3":
        layer_order, order_mode = choice.split(";Q_order=")
        return {
            "supply_id": supply_id,
            "choice": choice,
            "program_rotation": 0,
            "layer_order": layer_order.removeprefix("layers="),
            "order_mode": order_mode,
        }
    raise ValueError(supply_id)


def alternative_settings(stations: int) -> tuple[dict[str, object], ...]:
    choices = (
        ("inherited_1", "source_index=1"),
        ("inherited_1", "source_index=stations-1"),
        ("inherited_2", "left_rotation=1"),
        ("inherited_2", "left_rotation=stations-1"),
        *(
            (
                "inherited_3",
                f"layers={layer_order};Q_order={order_mode}",
            )
            for layer_order, order_mode in LAYER_CHOICES[1:]
        ),
    )
    return tuple(settings(supply, choice, stations) for supply, choice in choices)


def sample_settings(stations: int) -> tuple[dict[str, object], ...]:
    return (
        settings("inherited_1", "source_index=1", stations),
        settings("inherited_2", "left_rotation=1", stations),
        settings(
            "inherited_3",
            "layers=R_then_Q;Q_order=descending",
            stations,
        ),
    )


def phase_offset(row: dict[str, object]) -> int:
    return int(row["layer_order"] == "R_then_Q")


def station_shift(row: dict[str, object], stations: int) -> int:
    return (
        -int(row["program_rotation"]) - phase_offset(row)
    ) % stations


def station_map(stations: int, shift: int) -> tuple[int, ...]:
    return tuple((station + shift) % stations for station in range(stations))


def advance_rails(
    a_tokens: tuple[int, ...],
    b_tokens: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    a = list(a_tokens)
    b = list(b_tokens)
    for station in range(len(a)):
        a[station], b[station] = b[station], a[station]
    for station in range(len(a)):
        target = (station + 1) % len(a)
        b[station], a[target] = a[target], b[station]
    return tuple(a), tuple(b)


def retreat_rails(
    a_tokens: tuple[int, ...],
    b_tokens: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    a = list(a_tokens)
    b = list(b_tokens)
    for station in reversed(range(len(a))):
        target = (station + 1) % len(a)
        b[station], a[target] = a[target], b[station]
    for station in reversed(range(len(a))):
        a[station], b[station] = b[station], a[station]
    return tuple(a), tuple(b)


def apply_live_macro(
    data: tuple[int, ...],
    program: tuple,
    a_tokens: tuple[int, ...],
    *,
    reverse: bool,
    order_mode: str,
) -> tuple[int, ...]:
    output = data
    for station in q_order(len(program), order_mode):
        if a_tokens[station]:
            word = K719.mapped_macro(program[station])
            if reverse:
                word = tuple(reversed(word))
            output = K719.A.apply_semantic(output, word)
    return output


def run_orbit(
    data: tuple[int, ...],
    program: tuple,
    *,
    token_position: int,
    reverse: bool,
    layer_order: str,
    order_mode: str,
    checkpoints: bool = False,
) -> tuple[
    tuple[int, ...],
    tuple[int, ...],
    tuple[int, ...],
    tuple[tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]], ...],
]:
    stations = len(program)
    a = tuple(int(index == token_position) for index in range(stations))
    b = (0,) * stations
    output = data
    trace = []
    for _step in range(stations):
        if not reverse and layer_order == "Q_then_R":
            output = apply_live_macro(
                output,
                program,
                a,
                reverse=False,
                order_mode=order_mode,
            )
            a, b = advance_rails(a, b)
        elif not reverse and layer_order == "R_then_Q":
            a, b = advance_rails(a, b)
            output = apply_live_macro(
                output,
                program,
                a,
                reverse=False,
                order_mode=order_mode,
            )
        elif reverse and layer_order == "Q_then_R":
            a, b = retreat_rails(a, b)
            output = apply_live_macro(
                output,
                program,
                a,
                reverse=True,
                order_mode=order_mode,
            )
        elif reverse and layer_order == "R_then_Q":
            output = apply_live_macro(
                output,
                program,
                a,
                reverse=True,
                order_mode=order_mode,
            )
            a, b = retreat_rails(a, b)
        else:
            raise ValueError((reverse, layer_order))
        if checkpoints:
            trace.append((output, a, b))
    return output, a, b, tuple(trace)


def postimage_clean(after: tuple[int, ...], bank_count: int) -> bool:
    banks, links = K719.M.unpack_state(after, bank_count)
    bank_dirty = any(
        bank[wire]
        for bank in banks
        for wire in (
            K719.A.POINTER,
            K719.A.U_TO_V,
            K719.A.V_TO_U,
            K719.A.DIRECTION_OK,
            *K719.A.FRESH,
            *K719.A.ZERO_WORK,
            K719.A.TOKEN_OK,
        )
    )
    return not any(
        (
            after[K719.R3.X.SOURCE_POINTER],
            bank_dirty,
            any(any(link) for link in links),
        )
    )


def station_trial(
    program: tuple,
    before: tuple[int, ...],
    expected: tuple[int, ...],
    bank_count: int,
    position: int,
    row: dict[str, object],
) -> dict[str, object]:
    tokens = tuple(
        int(index == position) for index in range(len(program))
    )
    zeros = (0,) * len(program)
    after, rail_a, rail_b, _trace = run_orbit(
        before,
        program,
        token_position=position,
        reverse=False,
        layer_order=str(row["layer_order"]),
        order_mode=str(row["order_mode"]),
    )
    restored, inverse_a, inverse_b, _inverse_trace = run_orbit(
        after,
        program,
        token_position=position,
        reverse=True,
        layer_order=str(row["layer_order"]),
        order_mode=str(row["order_mode"]),
    )
    criteria = {
        "composition": after == expected,
        "rail": rail_a == tokens and rail_b == zeros,
        "inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "postimage": postimage_clean(after, bank_count),
    }
    failed = tuple(name for name, passed in criteria.items() if not passed)
    return {
        "criteria": criteria,
        "mask": "+".join(failed) if failed else "survivor",
        "selected": not failed,
        "after_sha256": digest(after),
    }


def epoch_fixtures(
    bank_count: int,
) -> tuple[dict[str, object], ...]:
    banks, links = K719.B.chain_genesis(bank_count)
    state = K719.M.pack_state(banks, links)
    allocator = K719.M.global_allocator_word(bank_count)
    rows = []
    for event in range(2 * bank_count):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K719.M.prepare_endpoint(state, direction)
        expected = K719.A.apply_semantic(before, allocator)
        rows.append(
            {
                "event": event,
                "direction": direction,
                "before": before,
                "expected": expected,
            }
        )
        state = expected
    return tuple(rows)


def landed_settings() -> dict[str, object]:
    return {
        "supply_id": "landed",
        "choice": "landed",
        "program_rotation": 0,
        "layer_order": "Q_then_R",
        "order_mode": "ascending",
    }


def direct_battery(
    bank_count: int,
    row: dict[str, object],
) -> dict[str, object]:
    base_program = K719.interleaved_program(bank_count)
    program = rotate_left(base_program, int(row["program_rotation"]))
    outputs = []
    for fixture in epoch_fixtures(bank_count):
        trials = tuple(
            station_trial(
                program,
                fixture["before"],
                fixture["expected"],
                bank_count,
                position,
                row,
            )
            for position in range(len(program))
        )
        outputs.append(
            {
                "event": fixture["event"],
                "direction": fixture["direction"],
                "selected": tuple(
                    position
                    for position, trial in enumerate(trials)
                    if trial["selected"]
                ),
                "position_masks": tuple(
                    trial["mask"] for trial in trials
                ),
                "after_sha256": tuple(
                    trial["after_sha256"] for trial in trials
                ),
            }
        )
    return {
        "bank_count": bank_count,
        "stations": len(program),
        "settings": dict(row),
        "rows": tuple(outputs),
    }


def relabeled_program(
    base_program: tuple,
    mapping: tuple[int, ...],
) -> tuple:
    output = [None] * len(base_program)
    for base_station, alternative_station in enumerate(mapping):
        output[alternative_station] = base_program[base_station]
    if any(item is None for item in output):
        raise AssertionError("incomplete relabeled program")
    return tuple(output)


def mapping_certificate(
    bank_count: int,
    row: dict[str, object],
) -> dict[str, object]:
    stations = len(K719.interleaved_program(bank_count))
    epochs = 2 * bank_count
    shift = station_shift(row, stations)
    mapping = station_map(stations, shift)
    q_positions = {
        station: slot
        for slot, station in enumerate(
            q_order(stations, str(row["order_mode"]))
        )
    }
    q_station_map = tuple(
        (mapping[station] + phase_offset(row)) % stations
        for station in range(stations)
    )
    physical_map = tuple(
        (
            2 * station + parity,
            2 * mapping[station] + parity,
        )
        for station in range(stations)
        for parity in (0, 1)
    )
    layer_map = (
        ((0, 1), (1, 0))
        if row["layer_order"] == "R_then_Q"
        else ((0, 0), (1, 1))
    )
    q_traversal_map = tuple(
        (base_slot, q_positions[q_station_map[base_slot]])
        for base_slot in range(stations)
    )
    base_program = K719.interleaved_program(bank_count)
    alternative_program = rotate_left(
        base_program, int(row["program_rotation"])
    )
    incidence = tuple(
        alternative_program[q_station_map[station]]
        == base_program[station]
        for station in range(stations)
    )
    domains = {
        "station_labels": (
            len(set(mapping)) == stations
            and set(mapping) == set(range(stations))
        ),
        "physical_track_site_slots": (
            len({target for _source, target in physical_map})
            == 2 * stations
        ),
        "logical_bank_indices": (
            tuple(range(bank_count)) == tuple(range(bank_count))
        ),
        "epochs": tuple(range(epochs)) == tuple(range(epochs)),
        "layer_slots": (
            {source for source, _target in layer_map}
            == {target for _source, target in layer_map}
            == {0, 1}
        ),
        "q_traversal_slots": (
            {source for source, _target in q_traversal_map}
            == {target for _source, target in q_traversal_map}
            == set(range(stations))
        ),
        "program_role_incidence": all(incidence),
    }
    return {
        "bank_count": bank_count,
        "choice": row["choice"],
        "shift": shift,
        "mapping": mapping,
        "q_station_map": q_station_map,
        "layer_map": layer_map,
        "domains": domains,
        "all_domains_bijective": all(domains.values()),
        "mapping_sha256": digest(
            {
                "station": mapping,
                "physical": physical_map,
                "bank": tuple(range(bank_count)),
                "epoch": tuple(range(epochs)),
                "layer": layer_map,
                "q": q_traversal_map,
            }
        ),
    }


def derived_battery(
    base: dict[str, object],
    row: dict[str, object],
) -> dict[str, object]:
    stations = int(base["stations"])
    rotation = int(row["program_rotation"])
    phase = phase_offset(row)
    outputs = []
    for base_row in base["rows"]:
        effective = tuple(
            (position + rotation + phase) % stations
            for position in range(stations)
        )
        outputs.append(
            {
                "event": base_row["event"],
                "direction": base_row["direction"],
                "selected": tuple(
                    position
                    for position, base_position in enumerate(effective)
                    if base_position in base_row["selected"]
                ),
                "position_masks": tuple(
                    base_row["position_masks"][base_position]
                    for base_position in effective
                ),
                "after_sha256": tuple(
                    base_row["after_sha256"][base_position]
                    for base_position in effective
                ),
            }
        )
    return {
        "bank_count": base["bank_count"],
        "stations": stations,
        "settings": dict(row),
        "rows": tuple(outputs),
    }


def transport_comparison(
    base: dict[str, object],
    alternative: dict[str, object],
    row: dict[str, object],
) -> dict[str, object]:
    stations = int(base["stations"])
    shift = station_shift(row, stations)
    mapping = station_map(stations, shift)
    event_rows = []
    mask_rows = []
    state_rows = []
    for base_row, alternative_row in zip(
        base["rows"], alternative["rows"], strict=True
    ):
        mapped_selected = tuple(
            sorted(mapping[position] for position in base_row["selected"])
        )
        event_rows.append(
            (
                base_row["event"] == alternative_row["event"]
                and base_row["direction"] == alternative_row["direction"]
                and mapped_selected == alternative_row["selected"]
            )
        )
        mask_rows.extend(
            alternative_row["position_masks"][mapping[position]]
            == base_row["position_masks"][position]
            for position in range(stations)
        )
        state_rows.extend(
            alternative_row["after_sha256"][mapping[position]]
            == base_row["after_sha256"][position]
            for position in range(stations)
        )
    return {
        "event_transport_count": len(event_rows),
        "all_events_transport": all(event_rows),
        "all_exclusion_masks_transport": all(mask_rows),
        "all_forward_states_transport": all(state_rows),
        "transport_sha256": digest(
            {
                "event": event_rows,
                "mask": mask_rows,
                "state": state_rows,
            }
        ),
    }


def symbolic_commutation(
    bank_count: int,
    row: dict[str, object],
) -> dict[str, object]:
    base_program = K719.interleaved_program(bank_count)
    stations = len(base_program)
    shift = station_shift(row, stations)
    mapping = station_map(stations, shift)
    relabeled = relabeled_program(base_program, mapping)
    alternative = rotate_left(
        base_program, int(row["program_rotation"])
    )
    order = q_order(stations, str(row["order_mode"]))
    failures = []
    comparisons = 0
    for base_start in range(stations):
        alternative_start = mapping[base_start]
        for step in range(stations):
            landed_q_station = (alternative_start + step) % stations
            alternative_q_station = (
                alternative_start + step + phase_offset(row)
            ) % stations
            expected_row = base_program[(base_start + step) % stations]
            forward_ok = (
                relabeled[landed_q_station] == expected_row
                and alternative[alternative_q_station] == expected_row
                and (alternative_start + step + 1) % stations
                == (mapping[(base_start + step + 1) % stations])
            )
            landed_inverse_q_station = (
                alternative_start - step - 1
            ) % stations
            alternative_inverse_q_station = (
                alternative_start
                - step
                - int(row["layer_order"] == "Q_then_R")
            ) % stations
            expected_inverse_row = base_program[
                (base_start - step - 1) % stations
            ]
            inverse_ok = (
                relabeled[landed_inverse_q_station]
                == expected_inverse_row
                and alternative[alternative_inverse_q_station]
                == expected_inverse_row
                and (alternative_start - step - 1) % stations
                == mapping[(base_start - step - 1) % stations]
            )
            comparisons += 2
            if not forward_ok or not inverse_ok:
                failures.append(
                    {
                        "base_start": base_start,
                        "step": step,
                        "forward_ok": forward_ok,
                        "inverse_ok": inverse_ok,
                    }
                )
                break
        if failures:
            break
    return {
        "bank_count": bank_count,
        "choice": row["choice"],
        "station_positions_exhausted": stations,
        "steps_per_orbit": stations,
        "forward_inverse_operator_comparisons": comparisons,
        "q_order_is_permutation": (
            len(set(order)) == stations
            and set(order) == set(range(stations))
        ),
        "one_token_active_Q_count_per_step": 1,
        "failures": failures,
        "commutes_for_arbitrary_data_state": (
            not failures
            and len(set(order)) == stations
            and set(order) == set(range(stations))
        ),
    }


def actual_commutation(
    bank_count: int,
    row: dict[str, object],
) -> dict[str, object]:
    base_program = K719.interleaved_program(bank_count)
    stations = len(base_program)
    mapping = station_map(stations, station_shift(row, stations))
    relabeled = relabeled_program(base_program, mapping)
    alternative = rotate_left(
        base_program, int(row["program_rotation"])
    )
    landed = landed_settings()
    checkpoint_count = 0
    failures = []
    for fixture in epoch_fixtures(bank_count):
        landed_after, landed_a, landed_b, landed_trace = run_orbit(
            fixture["before"],
            relabeled,
            token_position=mapping[0],
            reverse=False,
            layer_order=str(landed["layer_order"]),
            order_mode=str(landed["order_mode"]),
            checkpoints=True,
        )
        alternative_after, alternative_a, alternative_b, alternative_trace = (
            run_orbit(
                fixture["before"],
                alternative,
                token_position=mapping[0],
                reverse=False,
                layer_order=str(row["layer_order"]),
                order_mode=str(row["order_mode"]),
                checkpoints=True,
            )
        )
        forward_equal = (
            landed_after == alternative_after
            and landed_a == alternative_a
            and landed_b == alternative_b
            and landed_trace == alternative_trace
        )
        landed_restored, landed_ia, landed_ib, landed_inverse_trace = run_orbit(
            landed_after,
            relabeled,
            token_position=mapping[0],
            reverse=True,
            layer_order=str(landed["layer_order"]),
            order_mode=str(landed["order_mode"]),
            checkpoints=True,
        )
        (
            alternative_restored,
            alternative_ia,
            alternative_ib,
            alternative_inverse_trace,
        ) = run_orbit(
            alternative_after,
            alternative,
            token_position=mapping[0],
            reverse=True,
            layer_order=str(row["layer_order"]),
            order_mode=str(row["order_mode"]),
            checkpoints=True,
        )
        inverse_equal = (
            landed_restored == alternative_restored
            and landed_ia == alternative_ia
            and landed_ib == alternative_ib
            and landed_inverse_trace == alternative_inverse_trace
        )
        checkpoint_count += len(landed_trace) + len(landed_inverse_trace)
        if not forward_equal or not inverse_equal:
            failures.append(
                {
                    "event": fixture["event"],
                    "forward_equal": forward_equal,
                    "inverse_equal": inverse_equal,
                    "landed_after_sha256": digest(landed_after),
                    "alternative_after_sha256": digest(alternative_after),
                }
            )
    return {
        "bank_count": bank_count,
        "supply_id": row["supply_id"],
        "choice": row["choice"],
        "declared_checkpoints":
            "after every complete controller step, forward and inverse",
        "checkpoint_count": checkpoint_count,
        "events": 2 * bank_count,
        "failures": failures,
        "all_checkpoint_states_equal": not failures,
    }


def run_length_word(values: tuple[str, ...]) -> tuple[tuple[str, int], ...]:
    if not values:
        return ()
    rows = []
    current = values[0]
    count = 1
    for value in values[1:]:
        if value == current:
            count += 1
        else:
            rows.append((current, count))
            current = value
            count = 1
    rows.append((current, count))
    return tuple(rows)


def fine_invariants(battery: dict[str, object]) -> dict[str, str]:
    stations = int(battery["stations"])
    row = battery["settings"]
    rotation = int(row["program_rotation"])
    phase = phase_offset(row)
    program = K719.interleaved_program(int(battery["bank_count"]))
    columns = []
    temporal_words = []
    for position in range(stations):
        effective = (position + rotation + phase) % stations
        masks = tuple(
            event_row["position_masks"][position]
            for event_row in battery["rows"]
        )
        selected = tuple(
            int(position in event_row["selected"])
            for event_row in battery["rows"]
        )
        states = tuple(
            event_row["after_sha256"][position]
            for event_row in battery["rows"]
        )
        role = tuple(program[effective][:2])
        columns.append((role, masks, selected, states))
        temporal_words.append((role, run_length_word(masks), selected))
    event_directions = tuple(
        event_row["direction"] for event_row in battery["rows"]
    )
    cross_epoch = []
    for left in range(len(battery["rows"])):
        for right in range(len(battery["rows"])):
            census = Counter(
                (
                    battery["rows"][left]["position_masks"][position],
                    battery["rows"][right]["position_masks"][position],
                    int(position in battery["rows"][left]["selected"]),
                    int(position in battery["rows"][right]["selected"]),
                )
                for position in range(stations)
            )
            cross_epoch.append(tuple(sorted(census.items())))
    survivor_roles = tuple(
        tuple(
            sorted(
                tuple(
                    program[
                        (position + rotation + phase) % stations
                    ][:2]
                )
                for position in event_row["selected"]
            )
        )
        for event_row in battery["rows"]
    )
    return {
        "epoch_graph_isomorphism_class": digest(
            (event_directions, tuple(sorted(columns, key=compact)))
        ),
        "temporal_exclusion_word_spectrum": digest(
            tuple(sorted(temporal_words, key=compact))
        ),
        "cross_epoch_decorated_relation_tensor": digest(tuple(cross_epoch)),
        "program_role_event_correspondence": digest(
            (event_directions, survivor_roles)
        ),
    }


def add_counts(
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(a + b for a, b in zip(left_row, right_row, strict=True))
        for left_row, right_row in zip(left, right, strict=True)
    )


def extension_counts(
    selected_by_bank: dict[int, int],
) -> tuple[tuple[int, ...], ...]:
    census = [[0, 0, 0] for _scope in range(3)]
    full_offset = 0
    for bank_count in (2, 5, 12, 1, 3):
        stations = len(K719.interleaved_program(bank_count))
        for _event in range(2 * bank_count):
            if bank_count in (1, 3):
                associated = full_offset % 3
                quota = min(
                    PRIMITIVE_MULTIPLICITIES[associated], stations
                )
                selected = selected_by_bank.get(bank_count, 0)
                for local_seed_ordinal in range(quota):
                    shift = (
                        associated + local_seed_ordinal
                    ) % stations
                    actual = (selected - shift) % stations
                    feature = (full_offset + shift + actual) % 3
                    mapped = FROZEN_ASSIGNMENT[associated][feature]
                    census[associated][mapped] += 1
            full_offset += stations
    per_scope = tuple(tuple(row) for row in census)
    pooled = tuple(
        sum(row[effect] for row in per_scope)
        for effect in range(3)
    )
    return per_scope + (pooled,)


def cycle802_variations(stations: int) -> tuple[dict[str, object], ...]:
    rows = []
    for choice in (
        "source_index=0",
        "source_index=1",
        "source_index=stations-1",
    ):
        rows.append(settings("inherited_1", choice, stations))
    for choice in (
        "left_rotation=0",
        "left_rotation=1",
        "left_rotation=stations-1",
    ):
        rows.append(settings("inherited_2", choice, stations))
    for layer_order, order_mode in LAYER_CHOICES[:4]:
        rows.append(
            settings(
                "inherited_3",
                f"layers={layer_order};Q_order={order_mode}",
                stations,
            )
        )
    return tuple(rows)


def cycle802_reconciliation() -> dict[str, object]:
    landed = tuple(tuple(row) for row in LANDED_38_COUNTS)
    base_new = extension_counts({1: 0, 3: 0})
    baseline = add_counts(landed, base_new)
    variation_rows = []
    for bank_count in (1, 3):
        stations = len(K719.interleaved_program(bank_count))
        for row in cycle802_variations(stations):
            shift = station_shift(row, stations)
            selected = {1: 0, 3: 0}
            selected[bank_count] = shift
            varied = add_counts(landed, extension_counts(selected))
            base_events = tuple(
                (
                    bank_count,
                    event,
                    (1, 0) if event % 2 == 0 else (0, 1),
                    0,
                )
                for event in range(2 * bank_count)
            )
            alternative_events = tuple(
                (bank, event, direction, shift)
                for bank, event, direction, _station in base_events
            )
            mapped_events = tuple(
                (
                    bank,
                    event,
                    direction,
                    (station + shift) % stations,
                )
                for bank, event, direction, station in base_events
            )
            unlabeled_base = tuple(event[:3] for event in base_events)
            unlabeled_alternative = tuple(
                event[:3] for event in alternative_events
            )
            variation_rows.append(
                {
                    "bank_count": bank_count,
                    "supply_id": row["supply_id"],
                    "choice": row["choice"],
                    "shift": shift,
                    "event_transport": mapped_events == alternative_events,
                    "unlabeled_content_invariant":
                        unlabeled_base == unlabeled_alternative,
                    "labeled_table_moved": varied != baseline,
                    "labeled_table_sha256": digest(varied),
                }
            )
    moved = [row for row in variation_rows if row["labeled_table_moved"]]
    return {
        "variation_count": len(variation_rows),
        "labeled_table_move_count": len(moved),
        "unlabeled_move_count": sum(
            not row["unlabeled_content_invariant"]
            for row in variation_rows
        ),
        "event_transport_failures": tuple(
            row for row in variation_rows if not row["event_transport"]
        ),
        "baseline_46_counts": baseline,
        "baseline_46_counts_sha256": digest(baseline),
        "moved_choices": tuple(
            (row["bank_count"], row["supply_id"], row["choice"])
            for row in moved
        ),
        "variation_rows": tuple(variation_rows),
    }


def run_core() -> dict[str, object]:
    bases = {
        bank_count: direct_battery(bank_count, landed_settings())
        for bank_count in PRIMARY_BANKS
    }

    sample_cases = []
    for bank_count in PRIMARY_BANKS:
        for row in sample_settings(int(bases[bank_count]["stations"])):
            alternative = direct_battery(bank_count, row)
            mapping = mapping_certificate(bank_count, row)
            transport = transport_comparison(
                bases[bank_count], alternative, row
            )
            sample_cases.append(
                {
                    "bank_count": bank_count,
                    "supply_id": row["supply_id"],
                    "choice": row["choice"],
                    "mapping_domains": mapping["domains"],
                    "mapping_sha256": mapping["mapping_sha256"],
                    **transport,
                }
            )
    base_event_lists_exact = all(
        all(
            event_row["selected"] == (0,)
            for event_row in battery["rows"]
        )
        for battery in bases.values()
    )
    attack_1 = {
        "sample_bijection_count": len(sample_cases),
        "sample_event_transport_count": sum(
            row["event_transport_count"] for row in sample_cases
        ),
        "base_event_lists_exact": base_event_lists_exact,
        "all_sample_domains_bijective": all(
            all(row["mapping_domains"].values()) for row in sample_cases
        ),
        "all_sample_events_transport": all(
            row["all_events_transport"] for row in sample_cases
        ),
        "all_sample_masks_transport": all(
            row["all_exclusion_masks_transport"] for row in sample_cases
        ),
        "all_sample_states_transport": all(
            row["all_forward_states_transport"] for row in sample_cases
        ),
        "first_failure": next(
            (
                row
                for row in sample_cases
                if not all(
                    (
                        all(row["mapping_domains"].values()),
                        row["all_events_transport"],
                        row["all_exclusion_masks_transport"],
                        row["all_forward_states_transport"],
                    )
                )
            ),
            None,
        ),
        "sample_cases_sha256": digest(sample_cases),
    }
    attack_1["pass"] = all(
        (
            attack_1["sample_bijection_count"] == 9,
            attack_1["sample_event_transport_count"] == 36,
            attack_1["base_event_lists_exact"],
            attack_1["all_sample_domains_bijective"],
            attack_1["all_sample_events_transport"],
            attack_1["all_sample_masks_transport"],
            attack_1["all_sample_states_transport"],
        )
    )

    commutation_cases = tuple(
        actual_commutation(
            3,
            row,
        )
        for row in sample_settings(int(bases[3]["stations"]))
    )
    attack_2 = {
        "variation_count": len(commutation_cases),
        "supplies": tuple(
            row["supply_id"] for row in commutation_cases
        ),
        "declared_checkpoints":
            "after every complete controller step, forward and inverse",
        "checkpoint_count": sum(
            row["checkpoint_count"] for row in commutation_cases
        ),
        "all_checkpoint_states_equal": all(
            row["all_checkpoint_states_equal"]
            for row in commutation_cases
        ),
        "first_failure": next(
            (
                row
                for row in commutation_cases
                if not row["all_checkpoint_states_equal"]
            ),
            None,
        ),
        "cases_sha256": digest(commutation_cases),
    }
    attack_2["pass"] = all(
        (
            set(attack_2["supplies"])
            == {"inherited_1", "inherited_2", "inherited_3"},
            attack_2["checkpoint_count"] == 684,
            attack_2["all_checkpoint_states_equal"],
        )
    )

    extension_cases = []
    for bank_count in EXTENSION_BANKS:
        stations = len(K719.interleaved_program(bank_count))
        for row in alternative_settings(stations):
            mapping = mapping_certificate(bank_count, row)
            commute = symbolic_commutation(bank_count, row)
            extension_cases.append(
                {
                    "bank_count": bank_count,
                    "supply_id": row["supply_id"],
                    "choice": row["choice"],
                    "shift": mapping["shift"],
                    "all_domains_bijective":
                        mapping["all_domains_bijective"],
                    "commutes_for_arbitrary_data_state":
                        commute["commutes_for_arbitrary_data_state"],
                    "operator_comparisons":
                        commute["forward_inverse_operator_comparisons"],
                    "event_transports": 2 * bank_count,
                    "failure": commute["failures"][:1],
                }
            )
    added_event_transports = sum(
        row["event_transports"] for row in extension_cases
    )
    attack_3 = {
        "banks": EXTENSION_BANKS,
        "variation_count": len(extension_cases),
        "added_epochs": sum(2 * bank for bank in EXTENSION_BANKS),
        "added_event_transports": added_event_transports,
        "operator_schedule_comparisons": sum(
            row["operator_comparisons"] for row in extension_cases
        ),
        "epoch_instantiated_checkpoint_bound": sum(
            row["operator_comparisons"] * (2 * row["bank_count"])
            for row in extension_cases
        ),
        "honest_bound": (
            "All 9 non-landed choices at each of banks 5 and 12; every "
            "station label; every forward and inverse controller step. "
            "The arbitrary-data operator identity is then instantiated "
            "on all 34 extension epochs, with no sampled epoch."
        ),
        "all_domains_bijective": all(
            row["all_domains_bijective"] for row in extension_cases
        ),
        "all_constructions_commute": all(
            row["commutes_for_arbitrary_data_state"]
            for row in extension_cases
        ),
        "first_failure": next(
            (
                row
                for row in extension_cases
                if not row["all_domains_bijective"]
                or not row["commutes_for_arbitrary_data_state"]
            ),
            None,
        ),
        "full_family_epochs": sum(2 * bank for bank in BANKS_FULL),
        "full_family_event_transports": 108 + added_event_transports,
        "cases_sha256": digest(extension_cases),
    }
    attack_3["pass"] = all(
        (
            attack_3["variation_count"] == 18,
            attack_3["added_epochs"] == 34,
            attack_3["added_event_transports"] == 306,
            attack_3["operator_schedule_comparisons"] == 171108,
            attack_3["all_domains_bijective"],
            attack_3["all_constructions_commute"],
            attack_3["full_family_epochs"] == 46,
            attack_3["full_family_event_transports"] == 414,
        )
    )

    invariant_rows = []
    cross_bank_base: dict[tuple[str, str], list[str]] = {}
    cross_bank_alternative: dict[tuple[str, str], list[str]] = {}
    for bank_count in PRIMARY_BANKS:
        base_invariants = fine_invariants(bases[bank_count])
        stations = int(bases[bank_count]["stations"])
        for row in alternative_settings(stations):
            alternative = derived_battery(bases[bank_count], row)
            alternative_invariants = fine_invariants(alternative)
            key = (str(row["supply_id"]), str(row["choice"]))
            cross_bank_base.setdefault(key, []).append(
                base_invariants["program_role_event_correspondence"]
            )
            cross_bank_alternative.setdefault(key, []).append(
                alternative_invariants[
                    "program_role_event_correspondence"
                ]
            )
            invariant_rows.append(
                {
                    "bank_count": bank_count,
                    "supply_id": row["supply_id"],
                    "choice": row["choice"],
                    "base": base_invariants,
                    "alternative": alternative_invariants,
                    "equal": base_invariants == alternative_invariants,
                }
            )
    invariant_names = tuple(
        fine_invariants(bases[1]).keys()
    )
    cross_bank_equal = {
        key: tuple(cross_bank_base[key])
        == tuple(cross_bank_alternative[key])
        for key in sorted(cross_bank_base)
    }
    attack_4 = {
        "primary_bijection_count": len(invariant_rows),
        "finer_invariant_names": invariant_names,
        "finer_invariant_count": len(invariant_names),
        "all_27_match": all(row["equal"] for row in invariant_rows),
        "cross_bank_correspondence_cases": len(cross_bank_equal),
        "cross_bank_correspondence_all_match": all(
            cross_bank_equal.values()
        ),
        "first_separation": next(
            (row for row in invariant_rows if not row["equal"]),
            None,
        ),
        "rows_sha256": digest(invariant_rows),
        "cross_bank_sha256": digest(tuple(sorted(cross_bank_equal.items()))),
    }
    attack_4["pass"] = all(
        (
            attack_4["primary_bijection_count"] == 27,
            attack_4["finer_invariant_count"] >= 3,
            attack_4["all_27_match"],
            attack_4["cross_bank_correspondence_cases"] == 9,
            attack_4["cross_bank_correspondence_all_match"],
        )
    )

    reconciliation = cycle802_reconciliation()
    attack_5 = {
        **{
            key: value
            for key, value in reconciliation.items()
            if key != "variation_rows"
        },
        "rows_sha256": digest(reconciliation["variation_rows"]),
    }
    attack_5["pass"] = all(
        (
            attack_5["variation_count"] == 20,
            attack_5["labeled_table_move_count"] == 10,
            attack_5["unlabeled_move_count"] == 0,
            not attack_5["event_transport_failures"],
        )
    )
    return {
        "attack_1": attack_1,
        "attack_2": attack_2,
        "attack_3": attack_3,
        "attack_4": attack_4,
        "attack_5": attack_5,
    }


def top_level_assignments(tree: ast.Module) -> dict[str, ast.AST]:
    rows = {}
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        for target in targets:
            if isinstance(target, ast.Name):
                rows[target.id] = node.value
    return rows


def control_audit() -> dict[str, object]:
    own_source = Path(__file__).read_text(encoding="utf-8")
    own_tree = ast.parse(own_source, filename=__file__)
    assignments = top_level_assignments(own_tree)
    audit_node = assignments["AUDIT_INPUT_PATHS"]
    declared_node = assignments["DECLARED_INPUT_PATHS"]
    imported = []
    for node in own_tree.body:
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module or "")
    primary_source = (ROOT / AUDIT_INPUT_PATHS[0]).read_text(
        encoding="utf-8"
    )
    primary_tree = ast.parse(
        primary_source, filename=AUDIT_INPUT_PATHS[0]
    )
    try:
        __import__(PRIMARY_MODULE)
    except ImportError as exc:
        runtime_blocked = (
            str(exc) == f"BLOCKLIST forbids import of {PRIMARY_MODULE}"
        )
        block_message = str(exc)
    else:
        runtime_blocked = False
        block_message = "IMPORT_UNEXPECTEDLY_SUCCEEDED"
    return {
        "audit_input_paths_literal_tuple": (
            isinstance(audit_node, ast.Tuple)
            and all(
                isinstance(item, ast.Constant)
                and isinstance(item.value, str)
                for item in audit_node.elts
            )
            and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        ),
        "declared_paths_alias": (
            isinstance(declared_node, ast.Name)
            and declared_node.id == "AUDIT_INPUT_PATHS"
        ),
        "paths_worktree_relative": all(
            not Path(path).is_absolute()
            and ".." not in Path(path).parts
            for path in AUDIT_INPUT_PATHS
        ),
        "all_paths_exist": all(
            (ROOT / path).is_file() for path in AUDIT_INPUT_PATHS
        ),
        "primary_not_imported_by_ast": PRIMARY_MODULE not in imported,
        "primary_not_loaded": PRIMARY_MODULE not in sys.modules,
        "runtime_blocker_installed": PRIMARY_BLOCKER in sys.meta_path,
        "runtime_import_blocked": runtime_blocked,
        "runtime_block_message": block_message,
        "primary_text_ast_only": (
            isinstance(primary_tree, ast.Module)
            and sha256(primary_source.encode("utf-8")).hexdigest()
            == EXPECTED_INPUT_SHA256[AUDIT_INPUT_PATHS[0]]
        ),
    }


def main() -> int:
    input_sha_before = {
        path: file_sha256(path) for path in AUDIT_INPUT_PATHS
    }
    controls = control_audit()
    first = run_core()

    finding_1 = (
        "Independent direct recomputation found 9/9 sampled station maps "
        "bijective on every declared label domain and transported all 36 "
        "sampled events, every exclusion mask, and every forward state."
        if first["attack_1"]["pass"]
        else (
            "REFUTATION: a sampled Cycle-805 bijection, full event list, "
            "exclusion mask, or forward state failed exact transport."
        )
    )
    check(
        "CERTIFICATE_1_BIJECTION_VALIDITY_AND_EVENT_TRANSPORT",
        first["attack_1"]["pass"],
        {"finding": finding_1, **first["attack_1"]},
    )
    emit("FINDING_1", finding_1)

    finding_2 = (
        "The relabeled BASE configuration commutes with each selecting "
        "supply: 684 declared intermediate forward/inverse controller-step "
        "checkpoint states equal the alternative construction exactly."
        if first["attack_2"]["pass"]
        else (
            "REFUTATION: an end-matching variation fails construction "
            "commutation at an intermediate controller-step checkpoint."
        )
    )
    check(
        "CERTIFICATE_2_CONSTRUCTION_COMMUTATION_ATTACK",
        first["attack_2"]["pass"],
        {"finding": finding_2, **first["attack_2"]},
    )
    emit("FINDING_2", finding_2)

    finding_3 = (
        "All 306 bank-5/12 event transports exist for every declared "
        "variation; together with the original 108 this covers the FULL "
        "46-epoch family with 414 exact transports."
        if first["attack_3"]["pass"]
        else (
            "REFUTATION: the Cycle-805 claim remains scoped to its verified "
            "banks; at least one bank-5/12 variation is a PHYSICAL supply."
        )
    )
    check(
        "CERTIFICATE_3_BANK_5_12_FULL_EXTENSION",
        first["attack_3"]["pass"],
        {"finding": finding_3, **first["attack_3"]},
    )
    emit("FINDING_3", finding_3)
    if not first["attack_3"]["pass"]:
        emit(
            "LOUD_REFUTATION_BANK_5_12_PHYSICAL_WITNESS",
            compact(first["attack_3"]["first_failure"]),
        )

    finding_4 = (
        "Four finer invariants—decorated epoch-graph class, temporal "
        "exclusion words, cross-epoch relation tensor, and program-role "
        "event correspondence—match on all 27 original bijections; the "
        "nine cross-bank correspondence structures also match."
        if first["attack_4"]["pass"]
        else (
            "REFUTATION: a finer relabeling-invariant separates a base "
            "battery from a claimed variation."
        )
    )
    check(
        "CERTIFICATE_4_FINER_RELABELING_INVARIANTS",
        first["attack_4"]["pass"],
        {"finding": finding_4, **first["attack_4"]},
    )
    emit("FINDING_4", finding_4)
    if not first["attack_4"]["pass"]:
        emit(
            "LOUD_REFUTATION_FINER_INVARIANT_WITNESS",
            compact(first["attack_4"]["first_separation"]),
        )

    finding_5 = (
        "Cycle 802 and Cycle 805 are consistent: all 20 shared variations "
        "preserve unlabeled occurrence content under transport, while "
        "exactly 10/20 move the numeric-station-labeled frozen table; the "
        "802 sensitivity is description-dependence."
        if first["attack_5"]["pass"]
        else (
            "REFUTATION: the 20-row reconciliation either moves unlabeled "
            "content or fails to reproduce the 10/20 labeled-table moves."
        )
    )
    check(
        "CERTIFICATE_5_CYCLE802_RECONCILIATION",
        first["attack_5"]["pass"],
        {"finding": finding_5, **first["attack_5"]},
    )
    emit("FINDING_5", finding_5)

    second = run_core()
    input_sha_after = {
        path: file_sha256(path) for path in AUDIT_INPUT_PATHS
    }
    elapsed = monotonic() - START
    deterministic = first == second
    stdout_before_6 = len(
        ("\n".join(OUTPUT_LINES) + "\n").encode("utf-8")
    )
    control_values = {
        key: value
        for key, value in controls.items()
        if isinstance(value, bool)
    }
    controls_pass = all(
        (
            all(control_values.values()),
            input_sha_before == input_sha_after
            == EXPECTED_INPUT_SHA256,
            deterministic,
            elapsed < AUDIT_TIMEOUT_SEC,
            stdout_before_6 + 16 * 1024 < STDOUT_LIMIT_BYTES,
        )
    )
    finding_6 = (
        "SHA anchors, literal existing worktree-relative inputs, the "
        "Cycle-805 text/AST-only runtime blocklist, input stability, clean "
        "repeat determinism, runtime, and stdout bounds all hold."
        if controls_pass
        else (
            "CHECKER CONTROL FAILURE: a SHA, path, blocklist, determinism, "
            "runtime, or stdout guard failed."
        )
    )
    check(
        "CERTIFICATE_6_CONTROLS_DETERMINISM_AND_BOUNDS",
        controls_pass,
        {
            "finding": finding_6,
            "control_audit": controls,
            "deterministic": deterministic,
            "first_core_sha256": digest(first),
            "repeat_core_sha256": digest(second),
            "input_sha256_before": input_sha_before,
            "input_sha256_after": input_sha_after,
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_bytes_before_certificate_6": stdout_before_6,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )
    emit("FINDING_6", finding_6)

    science_pass = all(
        first[f"attack_{index}"]["pass"] for index in range(1, 6)
    )
    if science_pass:
        composite_scope = (
            "FULL_46_EPOCH_FAMILY_CANONICAL_UP_TO_RELABELING"
        )
    elif (
        first["attack_1"]["pass"]
        and first["attack_2"]["pass"]
        and first["attack_4"]["pass"]
        and first["attack_5"]["pass"]
        and not first["attack_3"]["pass"]
    ):
        composite_scope = (
            "SCOPED_TO_BANKS_1_2_3_WITH_BANK_5_12_PHYSICAL_WITNESS"
        )
    else:
        composite_scope = "RELABELING_VERDICT_REFUTED"
    report = {
        "cycle": 805,
        "role": "INDEPENDENT_ADVERSARIAL_CHECKER",
        "pass": all(CHECKS.values()),
        "certificates": dict(CHECKS),
        "checks_passed": sum(CHECKS.values()),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "composite_scope": composite_scope,
        "full_family_epochs": first["attack_3"]["full_family_epochs"],
        "full_family_event_transports":
            first["attack_3"]["full_family_event_transports"],
        "cycle802_labeled_moves":
            first["attack_5"]["labeled_table_move_count"],
        "cycle802_variations": first["attack_5"]["variation_count"],
        "cycle802_unlabeled_moves":
            first["attack_5"]["unlabeled_move_count"],
        "runtime_seconds": round(elapsed, 6),
        "terminal": (
            "CYCLE805_RELABELING_INDEPENDENT_CHECK_PASS"
            if all(CHECKS.values())
            else "CYCLE805_RELABELING_INDEPENDENT_CHECK_FAIL"
        ),
    }
    report["report_sha256"] = digest(report)
    emit("SUMMARY_JSON", compact(report))
    output = "\n".join(OUTPUT_LINES) + "\n"
    output_bytes = len(output.encode("utf-8"))
    if output_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", output_bytes, STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
