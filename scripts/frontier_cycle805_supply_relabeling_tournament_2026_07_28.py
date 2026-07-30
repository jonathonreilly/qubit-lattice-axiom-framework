#!/usr/bin/env python3
"""Cycle 805: exact selecting-supply relabeling-equivalence tournament.

The new tournament imports only the Python standard library and the pinned
carried constructor modules.  Both Cycle-788 runners are source/hash inputs
and are runtime-blocklisted: none of their computed verdicts is imported.

The event family is the typed occurrence set
    (bank_count, epoch, direction, surviving_station).
For every lawful alternative, the runner exhausts the cyclic station-label
group and verifies transport epoch-by-epoch and survivor-by-survivor.  The
physical track-site, logical-bank, epoch, layer-slot, and Q-traversal-slot
extensions of each station bijection are printed explicitly.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1200
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle788_selector_scope_extension_2026_07_28.py",
    "scripts/frontier_cycle788_extension_independent_check_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/protected_recurrent_actual_history_selection_cycle335_2026_07_18.py",
    "scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py",
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


START = monotonic()
ROOT = Path(__file__).resolve().parents[1]
BLOCKLISTED_MODULES = (
    "frontier_cycle788_selector_scope_extension_2026_07_28",
    "frontier_cycle788_extension_independent_check_2026_07_28",
)
EXPECTED_INPUT_SHA256 = {
    "scripts/frontier_cycle788_selector_scope_extension_2026_07_28.py":
        "5af27fd61c20fe3b25e9a172b63339d5fd4f5112631fe6d31c6e0fa95a7486f1",
    "scripts/frontier_cycle788_extension_independent_check_2026_07_28.py":
        "345ae7c423c529b080ce87647909472453f64119282aa41b8aa4ffbecbf4286e",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py":
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    "scripts/protected_recurrent_actual_history_selection_cycle335_2026_07_18.py":
        "5a45d24c439fe5dc4903c1064213ad8a287ed489ed5736f7a18b34e4cc03db5f",
    "scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py":
        "de7883fe45ce248427e8e44294d77fce56394e5ed14724e9056a65b43e0a4415",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py":
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py":
        "0008837e938fdc589473967763c5319aeb5fc4996bd8380d5d33c3ec61062691",
}
BANK_COUNTS = (1, 2, 3)
LAYER_CHOICES = (
    ("Q_then_R", "ascending"),
    ("Q_then_R", "descending"),
    ("Q_then_R", "even_then_odd"),
    ("R_then_Q", "ascending"),
    ("R_then_Q", "descending"),
    ("R_then_Q", "even_then_odd"),
)
PASS = 0
FAIL = 0
STDOUT_BYTES = 0


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def emit(*parts: object) -> None:
    global STDOUT_BYTES
    line = " ".join(str(part) for part in parts)
    STDOUT_BYTES += len((line + "\n").encode("utf-8"))
    print(line)


def check(label: str, condition: bool, detail: object) -> bool:
    global PASS, FAIL
    if condition:
        PASS += 1
        emit("PASS", label, "::", compact(detail))
    else:
        FAIL += 1
        emit("FAIL", label, "::", compact(detail))
    return condition


def source_hashes() -> dict[str, str]:
    return {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }


INITIAL_INPUT_SHA256 = source_hashes()


class _Cycle788Blocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname in BLOCKLISTED_MODULES:
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


CYCLE788_BLOCKER = _Cycle788Blocker()
sys.meta_path.insert(0, CYCLE788_BLOCKER)
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as S750
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K719


def own_epoch_fixtures(
    bank_count: int,
) -> tuple[tuple[int, tuple[int, int], tuple[int, ...], tuple[int, ...]], ...]:
    banks, links = K719.B.chain_genesis(bank_count)
    state = K719.M.pack_state(banks, links)
    word = K719.M.global_allocator_word(bank_count)
    rows = []
    for event in range(2 * bank_count):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K719.M.prepare_endpoint(state, direction)
        expected = K719.A.apply_semantic(before, word)
        rows.append((event, direction, before, expected))
        state = expected
    return tuple(rows)


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


def apply_live_macros(
    data: tuple[int, ...],
    program: tuple,
    a_tokens: tuple[int, ...],
    *,
    reverse: bool,
    order_mode: str,
) -> tuple[int, ...]:
    order = q_order(len(program), order_mode)
    output = data
    for station in order:
        if a_tokens[station]:
            word = K719.mapped_macro(program[station])
            if reverse:
                word = tuple(reversed(word))
            output = K719.A.apply_semantic(output, word)
    return output


def run_rq_orbit(
    data: tuple[int, ...],
    program: tuple,
    *,
    token_position: int,
    reverse: bool,
    order_mode: str,
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    stations = len(program)
    a = tuple(int(index == token_position) for index in range(stations))
    b = (0,) * stations
    output = data
    for _step in range(stations):
        if reverse:
            output = apply_live_macros(
                output,
                program,
                a,
                reverse=True,
                order_mode=order_mode,
            )
            a, b = retreat_rails(a, b)
        else:
            a, b = advance_rails(a, b)
            output = apply_live_macros(
                output,
                program,
                a,
                reverse=False,
                order_mode=order_mode,
            )
    return output, a, b


def run_choice_orbit(
    data: tuple[int, ...],
    program: tuple,
    *,
    token_position: int,
    reverse: bool,
    layer_order: str,
    order_mode: str,
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    if layer_order == "Q_then_R":
        order = q_order(len(program), order_mode)
        orders = (order,) * len(program)
        output, a, b, _trace = K719.run_orbit(
            data,
            program,
            token_positions=(token_position,),
            reverse=reverse,
            q_orders=orders,
        )
        return output, a, b
    if layer_order == "R_then_Q":
        return run_rq_orbit(
            data,
            program,
            token_position=token_position,
            reverse=reverse,
            order_mode=order_mode,
        )
    raise ValueError(layer_order)


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


def station_exclusions(
    program: tuple,
    before: tuple[int, ...],
    expected: tuple[int, ...],
    bank_count: int,
    position: int,
    *,
    layer_order: str,
    order_mode: str,
) -> dict[str, bool]:
    tokens = tuple(int(index == position) for index in range(len(program)))
    zeros = (0,) * len(program)
    after, rail_a, rail_b = run_choice_orbit(
        before,
        program,
        token_position=position,
        reverse=False,
        layer_order=layer_order,
        order_mode=order_mode,
    )
    restored, inverse_a, inverse_b = run_choice_orbit(
        after,
        program,
        token_position=position,
        reverse=True,
        layer_order=layer_order,
        order_mode=order_mode,
    )
    return {
        "composition": after == expected,
        "rail": rail_a == tokens and rail_b == zeros,
        "inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "postimage": postimage_clean(after, bank_count),
    }


def selector_battery(
    bank_count: int,
    *,
    program_rotation: int = 0,
    layer_order: str = "Q_then_R",
    order_mode: str = "ascending",
) -> dict[str, object]:
    base_program = K719.interleaved_program(bank_count)
    program = rotate_left(base_program, program_rotation)
    rows = []
    total_masks: Counter[str] = Counter()
    landed_mismatches = []
    for event, direction, before, expected in own_epoch_fixtures(bank_count):
        selected = []
        position_masks = []
        for position in range(len(program)):
            criteria = station_exclusions(
                program,
                before,
                expected,
                bank_count,
                position,
                layer_order=layer_order,
                order_mode=order_mode,
            )
            failed = tuple(name for name, passed in criteria.items() if not passed)
            mask = "+".join(failed) if failed else "survivor"
            total_masks[mask] += 1
            position_masks.append(mask)
            if not failed:
                selected.append(position)
        selected_tuple = tuple(selected)
        if (
            program_rotation == 0
            and layer_order == "Q_then_R"
            and order_mode == "ascending"
        ):
            landed = S750.enforcement_lineage_selector(
                program,
                before,
                expected,
                bank_count,
                tuple(range(len(program))),
            )
            if selected_tuple != landed:
                landed_mismatches.append(event)
        rows.append(
            {
                "event": event,
                "direction": list(direction),
                "selected": list(selected_tuple),
                "position_masks": position_masks,
            }
        )
    return {
        "banks": bank_count,
        "epochs": len(rows),
        "program_stations": len(program),
        "selector_outputs": rows,
        "survivor_signature": [row["selected"] for row in rows],
        "selected_count_range": [
            min(len(row["selected"]) for row in rows),
            max(len(row["selected"]) for row in rows),
        ],
        "tie_epochs": [
            row["event"] for row in rows if len(row["selected"]) > 1
        ],
        "empty_epochs": [
            row["event"] for row in rows if not row["selected"]
        ],
        "exclusion_mask_census": dict(sorted(total_masks.items())),
        "landed_selector_mismatches": landed_mismatches,
        "settings": {
            "program_rotation": program_rotation % len(program),
            "layer_order": layer_order,
            "order_mode": order_mode,
        },
    }


def identity_projection(battery: dict[str, object]) -> dict[str, object]:
    return {
        "banks": battery["banks"],
        "epochs": battery["epochs"],
        "program_stations": battery["program_stations"],
        "survivor_signature": battery["survivor_signature"],
        "selected_count_range": battery["selected_count_range"],
        "tie_epochs": battery["tie_epochs"],
        "empty_epochs": battery["empty_epochs"],
        "exclusion_mask_census": battery["exclusion_mask_census"],
        "landed_selector_mismatches": battery["landed_selector_mismatches"],
    }


EXPECTED_BASE_IDENTITIES = {
    "1": {
        "banks": 1,
        "epochs": 2,
        "program_stations": 3,
        "survivor_signature": [[0], [0]],
        "selected_count_range": [1, 1],
        "tie_epochs": [],
        "empty_epochs": [],
        "exclusion_mask_census": {
            "composition+postimage": 4,
            "survivor": 2,
        },
        "landed_selector_mismatches": [],
    },
    "2": {
        "banks": 2,
        "epochs": 4,
        "program_stations": 11,
        "survivor_signature": [[0], [0], [0], [0]],
        "selected_count_range": [1, 1],
        "tie_epochs": [],
        "empty_epochs": [],
        "exclusion_mask_census": {
            "composition+postimage": 40,
            "survivor": 4,
        },
        "landed_selector_mismatches": [],
    },
    "3": {
        "banks": 3,
        "epochs": 6,
        "program_stations": 19,
        "survivor_signature": [[0], [0], [0], [0], [0], [0]],
        "selected_count_range": [1, 1],
        "tie_epochs": [],
        "empty_epochs": [],
        "exclusion_mask_census": {
            "composition+postimage": 108,
            "survivor": 6,
        },
        "landed_selector_mismatches": [],
    },
}


def relabeling_invariants(battery: dict[str, object]) -> dict[str, object]:
    rows = battery["selector_outputs"]
    stations = int(battery["program_stations"])
    frequencies: Counter[int] = Counter()
    cooccurrences: Counter[tuple[int, int]] = Counter()
    for row in rows:
        selected = tuple(row["selected"])
        frequencies.update(selected)
        for left_index, left in enumerate(selected):
            for right in selected[left_index + 1:]:
                cooccurrences[tuple(sorted((left, right)))] += 1
    selected_sets = [set(row["selected"]) for row in rows]
    return {
        "per_epoch_survivor_multiplicities": [
            len(row["selected"]) for row in rows
        ],
        "survivor_frequency_multiset": sorted(
            frequencies.get(station, 0) for station in range(stations)
        ),
        "cooccurrence_multiplicity_multiset": sorted(cooccurrences.values()),
        "cross_epoch_coincidence_matrix": [
            [len(left & right) for right in selected_sets]
            for left in selected_sets
        ],
        "per_epoch_exclusion_mask_multiplicity_multisets": [
            sorted(Counter(row["position_masks"]).values()) for row in rows
        ],
        "direction_sequence": [row["direction"] for row in rows],
    }


def cyclic_map(stations: int, shift: int) -> tuple[int, ...]:
    return tuple((station + shift) % stations for station in range(stations))


def event_transport_rows(
    base: dict[str, object],
    alternative: dict[str, object],
    station_map: tuple[int, ...],
) -> list[dict[str, object]]:
    rows = []
    for base_row, alternative_row in zip(
        base["selector_outputs"],
        alternative["selector_outputs"],
    ):
        mapped = sorted(station_map[station] for station in base_row["selected"])
        rows.append(
            {
                "bank_count": base["banks"],
                "epoch": base_row["event"],
                "direction": base_row["direction"],
                "base_survivors": base_row["selected"],
                "mapped_survivors": mapped,
                "alternative_survivors": alternative_row["selected"],
                "event_equal": (
                    base_row["event"] == alternative_row["event"]
                    and base_row["direction"] == alternative_row["direction"]
                    and mapped == alternative_row["selected"]
                ),
            }
        )
    return rows


def matching_cyclic_shifts(
    base: dict[str, object],
    alternative: dict[str, object],
) -> list[int]:
    stations = int(base["program_stations"])
    return [
        shift
        for shift in range(stations)
        if all(
            row["event_equal"]
            for row in event_transport_rows(
                base,
                alternative,
                cyclic_map(stations, shift),
            )
        )
    ]


def mapping_table(
    bank_count: int,
    epochs: int,
    stations: int,
    shift: int,
    *,
    layer_order: str,
    order_mode: str,
) -> dict[str, object]:
    station_map = cyclic_map(stations, shift)
    alternative_q_order = q_order(stations, order_mode)
    alternative_q_positions = {
        station: slot for slot, station in enumerate(alternative_q_order)
    }
    layer_slot_map = (
        ((0, 1), (1, 0))
        if layer_order == "R_then_Q"
        else ((0, 0), (1, 1))
    )
    table = {
        "bank_count": bank_count,
        "cyclic_shift": shift,
        "station_labels": [
            [station, station_map[station]] for station in range(stations)
        ],
        "physical_track_site_slots": [
            [2 * station + parity, 2 * station_map[station] + parity]
            for station in range(stations)
            for parity in (0, 1)
        ],
        "logical_bank_indices": [
            [bank, bank] for bank in range(bank_count)
        ],
        "epochs": [[epoch, epoch] for epoch in range(epochs)],
        "layer_slots": [list(pair) for pair in layer_slot_map],
        "layer_kinds": [["Q", "Q"], ["R", "R"]],
        "q_traversal_slots": [
            [base_slot, alternative_q_positions[station_map[base_slot]]]
            for base_slot in range(stations)
        ],
    }
    table["table_sha256"] = digest(table)
    return table


def settings_for_choice(
    supply_id: str,
    choice: str,
    stations: int,
) -> dict[str, object]:
    if supply_id == "inherited_1":
        source_index = {
            "source_index=0": 0,
            "source_index=1": 1,
            "source_index=stations-1": stations - 1,
        }[choice]
        return {
            "program_rotation": (-source_index) % stations,
            "layer_order": "Q_then_R",
            "order_mode": "ascending",
            "choice_value": source_index,
        }
    if supply_id == "inherited_2":
        rotation = {
            "left_rotation=0": 0,
            "left_rotation=1": 1,
            "left_rotation=stations-1": stations - 1,
        }[choice]
        return {
            "program_rotation": rotation,
            "layer_order": "Q_then_R",
            "order_mode": "ascending",
            "choice_value": rotation,
        }
    if supply_id == "inherited_3":
        layer_order, order_mode = choice.split(";Q_order=")
        layer_order = layer_order.removeprefix("layers=")
        return {
            "program_rotation": 0,
            "layer_order": layer_order,
            "order_mode": order_mode,
            "choice_value": [layer_order, order_mode],
        }
    raise ValueError(supply_id)


SUPPLY_CHOICES = {
    "inherited_1": (
        "source_index=0",
        "source_index=1",
        "source_index=stations-1",
    ),
    "inherited_2": (
        "left_rotation=0",
        "left_rotation=1",
        "left_rotation=stations-1",
    ),
    "inherited_3": tuple(
        f"layers={layer_order};Q_order={order_mode}"
        for layer_order, order_mode in LAYER_CHOICES
    ),
}


def constructor_asymmetry_audit() -> dict[str, object]:
    controller_path = (
        ROOT
        / "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
    )
    selector_path = (
        ROOT / "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py"
    )
    controller = " ".join(
        controller_path.read_text(encoding="utf-8").split()
    )
    selector = " ".join(selector_path.read_text(encoding="utf-8").split())
    anchors = {
        "unique_typed_source_row":
            'prefix = [("source", 0, R3.source_compute_word())]' in controller,
        "unique_typed_finalizer_row":
            'suffix = [("finalizer", 0, M.source_finalizer_word(bank_count))]'
            in controller,
        "cyclic_successor_rule":
            "target = (station + 1) % stations" in controller,
        "landed_q_then_r_concatenation":
            "return q + r1 + r2" in controller,
        "selector_source_reference_not_input":
            "The supplied source-token reference is deliberately not an input."
            in selector,
        "selector_exhausts_positions":
            "for position in alternatives:" in selector,
    }
    return {
        "source_anchors": anchors,
        "all_source_anchors_present": all(anchors.values()),
        "per_supply": {
            "inherited_1": {
                "apparent_asymmetry":
                    "the source macro is the unique typed source row",
                "landed_value_named_by_invariant": False,
                "reason":
                    "the type names the source role, not an absolute station "
                    "label; rotating the complete typed program transports it",
            },
            "inherited_2": {
                "apparent_asymmetry":
                    "the rail law uses the cyclic successor station+1",
                "landed_value_named_by_invariant": False,
                "reason":
                    "the successor relation fixes cyclic chirality but no "
                    "origin; every declared rotation is an automorphism",
            },
            "inherited_3": {
                "apparent_asymmetry":
                    "the landed implementation concatenates Q then R",
                "landed_value_named_by_invariant": False,
                "reason":
                    "implementation order alone is not an invariant; the "
                    "six declared split-step choices are tested below, and "
                    "R-then-Q is transported by a station shift and layer-slot swap",
            },
        },
    }


def build_tournament() -> dict[str, object]:
    cache: dict[tuple, dict[str, object]] = {}

    def battery(
        bank_count: int,
        program_rotation: int = 0,
        layer_order: str = "Q_then_R",
        order_mode: str = "ascending",
    ) -> dict[str, object]:
        stations = len(K719.interleaved_program(bank_count))
        key = (
            bank_count,
            program_rotation % stations,
            layer_order,
            order_mode,
        )
        if key not in cache:
            cache[key] = selector_battery(
                bank_count,
                program_rotation=program_rotation,
                layer_order=layer_order,
                order_mode=order_mode,
            )
        return cache[key]

    bases = {bank: battery(bank) for bank in BANK_COUNTS}
    supplies = {}
    for supply_id, choices in SUPPLY_CHOICES.items():
        alternatives = []
        for choice in choices[1:]:
            per_bank = []
            for bank_count in BANK_COUNTS:
                base = bases[bank_count]
                stations = int(base["program_stations"])
                settings = settings_for_choice(supply_id, choice, stations)
                alternative = battery(
                    bank_count,
                    program_rotation=int(settings["program_rotation"]),
                    layer_order=str(settings["layer_order"]),
                    order_mode=str(settings["order_mode"]),
                )
                invariants_base = relabeling_invariants(base)
                invariants_alternative = relabeling_invariants(alternative)
                shifts = matching_cyclic_shifts(base, alternative)
                witnesses = []
                for shift in shifts:
                    station_map = cyclic_map(stations, shift)
                    transport = event_transport_rows(
                        base,
                        alternative,
                        station_map,
                    )
                    table = mapping_table(
                        bank_count,
                        int(base["epochs"]),
                        stations,
                        shift,
                        layer_order=str(settings["layer_order"]),
                        order_mode=str(settings["order_mode"]),
                    )
                    witnesses.append(
                        {
                            "shift": shift,
                            "mapping_table": table,
                            "event_transport": transport,
                            "all_events_transport": all(
                                row["event_equal"] for row in transport
                            ),
                        }
                    )
                per_bank.append(
                    {
                        "bank_count": bank_count,
                        "choice_value": settings["choice_value"],
                        "settings": {
                            key: value
                            for key, value in settings.items()
                            if key != "choice_value"
                        },
                        "lawful": (
                            alternative["selected_count_range"] == [1, 1]
                            and not alternative["tie_epochs"]
                            and not alternative["empty_epochs"]
                        ),
                        "base_invariants": invariants_base,
                        "alternative_invariants": invariants_alternative,
                        "invariants_match":
                            invariants_base == invariants_alternative,
                        "cyclic_group_size": stations,
                        "matching_cyclic_shifts": shifts,
                        "witnesses": witnesses,
                    }
                )
            alternatives.append(
                {
                    "choice": choice,
                    "per_bank": per_bank,
                    "all_banks_relabel": all(
                        row["lawful"]
                        and row["invariants_match"]
                        and bool(row["witnesses"])
                        and all(
                            witness["all_events_transport"]
                            for witness in row["witnesses"]
                        )
                        for row in per_bank
                    ),
                }
            )
        supplies[supply_id] = {
            "landed_choice": choices[0],
            "lawful_choice_count": len(choices),
            "lawful_choices": list(choices),
            "alternatives": alternatives,
            "verdict": (
                "RELABELING"
                if all(row["all_banks_relabel"] for row in alternatives)
                else "PHYSICAL"
            ),
            "convention_status": (
                "PURE_CONVENTION"
                if all(row["all_banks_relabel"] for row in alternatives)
                else "REQUIRED_INPUT"
            ),
        }
    return {
        "bank_counts": list(BANK_COUNTS),
        "base_identities": {
            str(bank): identity_projection(base)
            for bank, base in bases.items()
        },
        "supplies": supplies,
        "cache_entries": len(cache),
    }


def print_tournament_witnesses(tournament: dict[str, object]) -> None:
    for supply_id, supply in tournament["supplies"].items():
        for alternative in supply["alternatives"]:
            choice = alternative["choice"]
            for bank_row in alternative["per_bank"]:
                invariant_detail = {
                    "bank_count": bank_row["bank_count"],
                    "choice_value": bank_row["choice_value"],
                    "base": bank_row["base_invariants"],
                    "alternative": bank_row["alternative_invariants"],
                    "equal": bank_row["invariants_match"],
                }
                emit(
                    "RELABELING_INVARIANT",
                    supply_id,
                    choice,
                    "::",
                    compact(invariant_detail),
                )
                for witness in bank_row["witnesses"]:
                    emit(
                        "BIJECTION_FOUND",
                        supply_id,
                        choice,
                        f"bank={bank_row['bank_count']}",
                        "::",
                        compact(witness["mapping_table"]),
                    )
                    for event_row in witness["event_transport"]:
                        emit(
                            "EVENT_TRANSPORT",
                            supply_id,
                            choice,
                            "::",
                            compact(event_row),
                        )
        if supply["verdict"] == "RELABELING":
            emit(
                "SEPARATING_INVARIANT",
                supply_id,
                "NONE",
                "::",
                "all declared alternatives have explicit event-family bijections",
            )
        else:
            for alternative in supply["alternatives"]:
                for bank_row in alternative["per_bank"]:
                    if not bank_row["invariants_match"]:
                        emit(
                            "SEPARATING_INVARIANT",
                            supply_id,
                            alternative["choice"],
                            "::",
                            compact(
                                {
                                    "bank_count": bank_row["bank_count"],
                                    "base": bank_row["base_invariants"],
                                    "alternative":
                                        bank_row["alternative_invariants"],
                                }
                            ),
                        )


def literal_and_blocklist_audit() -> dict[str, object]:
    own_source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(own_source)
    assignments: dict[str, ast.AST] = {}
    imported_names = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
        elif isinstance(node, ast.Import):
            imported_names.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported_names.append(node.module or "")
    audit_node = assignments["AUDIT_INPUT_PATHS"]
    declared_node = assignments["DECLARED_INPUT_PATHS"]
    return {
        "audit_input_paths_literal_tuple": (
            isinstance(audit_node, ast.Tuple)
            and all(
                isinstance(item, ast.Constant) and isinstance(item.value, str)
                for item in audit_node.elts
            )
            and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        ),
        "declared_paths_alias_audit": (
            isinstance(declared_node, ast.Name)
            and declared_node.id == "AUDIT_INPUT_PATHS"
        ),
        "paths_are_worktree_relative": all(
            not Path(path).is_absolute()
            and ".." not in Path(path).parts
            for path in AUDIT_INPUT_PATHS
        ),
        "all_paths_exist": all(
            (ROOT / path).is_file() for path in AUDIT_INPUT_PATHS
        ),
        "blocklisted_modules_not_imported_by_ast": all(
            module not in imported_names for module in BLOCKLISTED_MODULES
        ),
        "blocklisted_modules_not_loaded": all(
            module not in sys.modules for module in BLOCKLISTED_MODULES
        ),
        "runtime_blocker_installed": CYCLE788_BLOCKER in sys.meta_path,
    }


def compact_supply_summary(tournament: dict[str, object]) -> dict[str, object]:
    return {
        supply_id: {
            "verdict": supply["verdict"],
            "convention_status": supply["convention_status"],
            "landed_choice": supply["landed_choice"],
            "lawful_choices": supply["lawful_choices"],
            "alternative_witness_sha256": {
                alternative["choice"]: digest(
                    [
                        {
                            "bank_count": row["bank_count"],
                            "matching_cyclic_shifts":
                                row["matching_cyclic_shifts"],
                            "mapping_table_sha256": [
                                witness["mapping_table"]["table_sha256"]
                                for witness in row["witnesses"]
                            ],
                            "event_transport_sha256": [
                                digest(witness["event_transport"])
                                for witness in row["witnesses"]
                            ],
                        }
                        for row in alternative["per_bank"]
                    ]
                )
                for alternative in supply["alternatives"]
            },
        }
        for supply_id, supply in tournament["supplies"].items()
    }


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    asymmetry = constructor_asymmetry_audit()
    first = build_tournament()
    print_tournament_witnesses(first)
    supply_summary = compact_supply_summary(first)
    for supply_id in ("inherited_1", "inherited_2", "inherited_3"):
        emit(
            "CONSTRUCTOR_ASYMMETRY_AUDIT",
            supply_id,
            "::",
            compact(asymmetry["per_supply"][supply_id]),
        )
        emit(
            "SUPPLY_VERDICT",
            supply_id,
            supply_summary[supply_id]["verdict"],
            supply_summary[supply_id]["convention_status"],
        )

    certificate_a = (
        asymmetry["all_source_anchors_present"]
        and all(
            not row["landed_value_named_by_invariant"]
            for row in asymmetry["per_supply"].values()
        )
        and all(
            row["verdict"] == "RELABELING"
            and row["convention_status"] == "PURE_CONVENTION"
            for row in supply_summary.values()
        )
    )
    check(
        "CERTIFICATE_A_PER_SUPPLY_VERDICTS_WITH_WITNESSES",
        certificate_a,
        {
            "constructor_asymmetry_audit": asymmetry,
            "supply_verdicts": supply_summary,
            "decision_priority": [
                "FORCED constructor-invariant audit",
                "PHYSICAL relabeling-invariant comparison",
                "RELABELING exhaustive cyclic-bijection construction",
            ],
        },
    )

    observed_identities = first["base_identities"]
    certificate_b = observed_identities == EXPECTED_BASE_IDENTITIES
    check(
        "CERTIFICATE_B_CYCLE788_PINNED_BASE_IDENTITIES",
        certificate_b,
        {
            "observed": observed_identities,
            "expected": EXPECTED_BASE_IDENTITIES,
            "extension_banks": [1, 3],
            "landed_control_bank": 2,
            "event_count": sum(
                row["epochs"] for row in observed_identities.values()
            ),
            "landed_38_epoch_context": 2 * (2 + 5 + 12),
        },
    )

    composite_status = (
        "CANONICAL_UP_TO_RELABELING"
        if certificate_a
        else "PHYSICAL_INPUT_REMAINS"
    )
    certificate_c = (
        composite_status == "CANONICAL_UP_TO_RELABELING"
        and set(supply_summary)
        == {"inherited_1", "inherited_2", "inherited_3"}
    )
    check(
        "CERTIFICATE_C_COMPOSITE_VERDICT",
        certificate_c,
        {
            "composite_status": composite_status,
            "scope":
                "Cycle-788 occurrence-event family at extension banks 1/3 "
                "and landed control bank 2",
            "three_selecting_supplies": supply_summary,
            "required_physical_input_from_W3_convention_layer": False,
        },
    )

    second = build_tournament()
    final_input_sha256 = source_hashes()
    blocklist = literal_and_blocklist_audit()
    no_mutation = (
        INITIAL_INPUT_SHA256
        == final_input_sha256
        == EXPECTED_INPUT_SHA256
    )
    certificate_d = all(blocklist.values()) and no_mutation
    for path in AUDIT_INPUT_PATHS:
        emit("COPIED_INPUT_SHA256", path, final_input_sha256[path])
    check(
        "CERTIFICATE_D_BLOCKLIST_AND_NO_MUTATION",
        certificate_d,
        {
            "blocklist": blocklist,
            "blocklisted_modules": list(BLOCKLISTED_MODULES),
            "before_sha256": INITIAL_INPUT_SHA256,
            "after_sha256": final_input_sha256,
            "expected_sha256": EXPECTED_INPUT_SHA256,
            "no_mutation": no_mutation,
        },
    )

    first_digest = digest(first)
    second_digest = digest(second)
    deterministic = first == second and first_digest == second_digest
    elapsed = monotonic() - START
    output_reserve = 4096
    bounds_pass = (
        elapsed < AUDIT_TIMEOUT_SEC
        and STDOUT_BYTES + output_reserve < STDOUT_LIMIT_BYTES
    )
    certificate_e = deterministic and bounds_pass
    check(
        "CERTIFICATE_E_RUNTIME_AND_DETERMINISM_ECHO",
        certificate_e,
        {
            "deterministic": deterministic,
            "first_tournament_sha256": first_digest,
            "repeat_tournament_sha256": second_digest,
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_bytes_before_certificate_e": STDOUT_BYTES,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "reserved_terminal_bytes": output_reserve,
        },
    )

    stable_report = {
        "audit_input_paths": list(AUDIT_INPUT_PATHS),
        "input_sha256": final_input_sha256,
        "supply_summary": supply_summary,
        "base_identities": observed_identities,
        "composite_status": composite_status,
        "tournament_sha256": first_digest,
        "certificates": {
            "A": certificate_a,
            "B": certificate_b,
            "C": certificate_c,
            "D": certificate_d,
            "E": certificate_e,
        },
    }
    emit(
        "SUMMARY",
        "::",
        compact(
            {
                "supply_verdicts": {
                    supply_id: row["verdict"]
                    for supply_id, row in supply_summary.items()
                },
                "convention_statuses": {
                    supply_id: row["convention_status"]
                    for supply_id, row in supply_summary.items()
                },
                "composite_status": composite_status,
                "certificates": stable_report["certificates"],
                "pass_count": PASS,
                "fail_count": FAIL,
                "report_sha256": digest(stable_report),
                "runtime_seconds": round(elapsed, 6),
                "stdout_bytes_final_upper_bound": STDOUT_BYTES + 1024,
            }
        ),
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
