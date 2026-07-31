#!/usr/bin/env python3
"""Cycle 833 independent adversarial checker: localize the funnel diffs.

The Cycle-833/830/831 primaries are SHA-pinned text/AST controls only.  Funnel
states are reconstructed from the landed Cycle-719 controller, and every
difference is decoded through the packed state's declared source/bank/link
layout and the bank object's named fields.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py",
    "scripts/frontier_cycle715_recurrent_directional_packet_bank_2026_07_26.py",
    "scripts/frontier_cycle833_funnel_family_2026_07_28.py",
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle831_deep_k2_forecast_tests_2026_07_28.py",
)

import ast
from collections import Counter
from hashlib import sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

CORE_PATH = AUDIT_INPUT_PATHS[0]
STATE_OBJECT_PATHS = AUDIT_INPUT_PATHS[1:3]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[3:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "b514b0e20197bb0ce5e5440b4b0c1f2a0f74a1962b127e8a4e4a2e97c8f86a1a",
    AUDIT_INPUT_PATHS[2]:
        "7ffe1dd4b169f774dce5bc9db29c5329c6e06c92e02506fbc734916ff11de884",
    AUDIT_INPUT_PATHS[3]:
        "bd08f5f503e532c724e6ae28915ba2f0b4202360bbe01458924d689e27c79174",
    AUDIT_INPUT_PATHS[4]:
        "b14262f6d54dc4f853bda13f321c816b3e762fa37b0b8276a2bec4955c51c481",
    AUDIT_INPUT_PATHS[5]:
        "624dad4d841e10e24891810dbc500cc4d6ebe871d6f09dd96f89e3189e52e2ff",
}


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if any blocklisted primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


State = tuple[int, ...]
Pair = tuple[int, int]
Key = tuple[int, Pair]
Lane = tuple[int, Pair, str]
MaskedGate = tuple[int, int, int, int, int]

RING_STATIONS = 11
FIXTURE_BANKS = 2
STATE_BITS = 5815
FAMILY_SIZE = 176
EVENT_ORDER = (0, 2, 1)
FUNNEL_MOMENTS = {0: 14739, 2: 33190, 1: 51110}
BACKBONE: tuple[Pair, ...] = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
WITNESS_PAIRS = (BACKBONE[0], BACKBONE[-1])
EXPECTED_WEIGHTS = {0: 44, 2: 45, 1: 46}
EXPECTED_XOR_WEIGHTS = {(0, 2): 25, (0, 1): 26, (2, 1): 27}
EXPECTED_SSTAR_SHA256 = (
    "cdf7e03092c6278b686c1f0edb9ebd716f4a285b1eabc8a7e2780695284a8f1a"
)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def state_sha256(state: State) -> str:
    return sha256(bytes(state)).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches = [
        node.value for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    ]
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def source_controls() -> dict[str, object]:
    payloads = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
        if not Path(path).is_absolute() and (ROOT / path).is_file()
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=Path(__file__).name,
    )
    markers = {
        AUDIT_INPUT_PATHS[3]:
            {"reconstruct_funnels", "exact_diff", "predicate_certificate"},
        AUDIT_INPUT_PATHS[4]:
            {"decode_fixtures", "preimage_tree_certificate"},
        AUDIT_INPUT_PATHS[5]:
            {"build_family", "masked_schedule", "run"},
    }
    functions = {
        path: {
            node.name for node in trees[path].body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        }
        for path in TEXT_AST_ONLY_PATHS
    }
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    sha_rows = {
        path: sha256(payload).hexdigest() for path, payload in payloads.items()
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "existing_worktree_relative":
            len(payloads) == len(AUDIT_INPUT_PATHS),
        "files_read": len(AUDIT_INPUT_PATHS),
        "read_limit": 6,
        "sha256": sha_rows,
        "sha256_expected": EXPECTED_SHA256,
        "state_object_citation": {
            "packing":
                f"{STATE_OBJECT_PATHS[0]}::pack_state/unpack_state",
            "named_bank_fields":
                f"{STATE_OBJECT_PATHS[1]}::CELLS and named registers",
            "runtime_layout":
                "K.M.R12::{SOURCE_WIDTH,BANK_BASES,LINK_BASES,TOTAL_WIRES}",
        },
        "text_AST_only": TEXT_AST_ONLY_PATHS,
        "AST_markers_present":
            all(markers[path] <= functions[path] for path in markers),
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "direct_frontier_imports": direct_frontier_imports,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and len(AUDIT_INPUT_PATHS) <= 6
        and sha_rows == EXPECTED_SHA256
        and result["AST_markers_present"]
        and direct_frontier_imports == (Path(CORE_PATH).stem,)
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


def cyclic_separation(pair: Pair) -> int:
    return min(
        (pair[1] - pair[0]) % RING_STATIONS,
        (pair[0] - pair[1]) % RING_STATIONS,
    )


def separated_pairs() -> tuple[Pair, ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if cyclic_separation(pair) > 1
    )


def orbit_word(program: tuple[object, ...], pair: Pair) -> tuple[object, ...]:
    output: list[object] = []
    for step in range(RING_STATIONS):
        live = {
            (pair[0] + step) % RING_STATIONS,
            (pair[1] + step) % RING_STATIONS,
        }
        for station, row in enumerate(program):
            if station in live:
                output.extend(K.mapped_macro(row))
    return tuple(output)


def build_selected_entrants() -> dict[str, object]:
    """Rebuild only the six needed population states from clean genesis."""
    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    epochs: dict[int, State] = {}
    epoch_failures = 0
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        epoch_failures += int(
            after != K.A.apply_semantic(before, allocator)
        )
        epoch_failures += int(
            rail_a != (1,) + (0,) * (RING_STATIONS - 1)
        )
        epoch_failures += int(any(rail_b) or len(trace) != RING_STATIONS)
        epochs[event] = before
        state = after

    positions = separated_pairs()
    words = {pair: orbit_word(program, pair) for pair in WITNESS_PAIRS}
    entrants: dict[Key, State] = {}
    composition_failures = 0
    rail_failures = 0
    for event in EVENT_ORDER:
        for pair in WITNESS_PAIRS:
            after, rail_a, rail_b, _trace = K.run_orbit(
                epochs[event], program, token_positions=pair
            )
            expected_rail = tuple(
                int(station in pair) for station in range(RING_STATIONS)
            )
            composition_failures += int(
                after != K.A.apply_semantic(epochs[event], words[pair])
            )
            rail_failures += int(rail_a != expected_rail or any(rail_b))
            entrants[(event, pair)] = after
    catalog = tuple(
        (event, pair) for event in range(2 * FIXTURE_BANKS)
        for pair in positions
    )
    summary = {
        "events": len(epochs),
        "separated_pairs": len(positions),
        "catalog_keys": len(catalog),
        "selected_entrants": len(entrants),
        "state_bits": len(next(iter(entrants.values()))),
        "program_stations": len(program),
        "allocator_gates": len(allocator),
        "selected_word_gate_counts":
            tuple(sorted({len(word) for word in words.values()})),
        "epoch_failures": epoch_failures,
        "composition_failures": composition_failures,
        "rail_failures": rail_failures,
    }
    summary["pass"] = (
        summary["events"] == 4
        and summary["separated_pairs"] == 44
        and summary["catalog_keys"] == FAMILY_SIZE
        and summary["selected_entrants"] == 6
        and summary["state_bits"] == STATE_BITS
        and summary["program_stations"] == RING_STATIONS
        and summary["allocator_gates"] == 3106
        and summary["selected_word_gate_counts"] == (6212,)
        and not epoch_failures
        and not composition_failures
        and not rail_failures
    )
    return {
        "program": program,
        "words": words,
        "entrants": entrants,
        "catalog": catalog,
        "summary": summary,
    }


def pack_lanes(states: tuple[State, ...]) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def unpack_lane(columns: list[int], lane: int) -> State:
    return tuple((column >> lane) & 1 for column in columns)


def masked_schedule(
    program: tuple[object, ...],
    lanes: tuple[Lane, ...],
    included_mask: int,
) -> tuple[MaskedGate, ...]:
    output: list[MaskedGate] = []
    for step in range(RING_STATIONS):
        for station, row in enumerate(program):
            mask = sum(
                1 << lane
                for lane, (_event, pair, _role) in enumerate(lanes)
                if included_mask & (1 << lane)
                and station in {
                    (pair[0] + step) % RING_STATIONS,
                    (pair[1] + step) % RING_STATIONS,
                }
            )
            if not mask:
                continue
            for gate in K.mapped_macro(row):
                if gate.kind == "X":
                    output.append((0, gate.wires[0], 0, 0, mask))
                elif gate.kind == "CNOT":
                    output.append(
                        (1, gate.wires[0], gate.wires[1], 0, mask)
                    )
                elif gate.kind == "TOF":
                    output.append((
                        2, gate.wires[0], gate.wires[1],
                        gate.wires[2], mask,
                    ))
                else:
                    raise AssertionError(("non-reversible gate", gate))
    return tuple(output)


def advance(columns: list[int], schedule: tuple[MaskedGate, ...]) -> None:
    for kind, first, second, third, mask in schedule:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first] & mask
        else:
            columns[third] ^= columns[first] & columns[second] & mask


def reconstruct_funnels_independently(
    selected: dict[str, object],
) -> dict[str, object]:
    """Carry first entrant, second entrant, and a determinism duplicate."""
    lanes: tuple[Lane, ...] = tuple(
        (event, pair, role)
        for event in EVENT_ORDER
        for pair, role in (
            (WITNESS_PAIRS[0], "first"),
            (WITNESS_PAIRS[1], "second"),
            (WITNESS_PAIRS[0], "determinism_duplicate"),
        )
    )
    initial = tuple(
        selected["entrants"][(event, pair)]
        for event, pair, _role in lanes
    )
    columns = pack_lanes(initial)
    lane_index = {
        (event, role): index
        for index, (event, _pair, role) in enumerate(lanes)
    }
    duplicate_initial = all(
        initial[lane_index[(event, "first")]]
        == initial[lane_index[(event, "determinism_duplicate")]]
        for event in EVENT_ORDER
    )
    active_mask = (1 << len(lanes)) - 1
    previous = 0
    snapshots: dict[int, dict[str, State]] = {}
    phase_rows = []
    for event in EVENT_ORDER:
        schedule = masked_schedule(
            selected["program"], lanes, active_mask
        )
        phase_started = monotonic()
        for _ in range(previous, FUNNEL_MOMENTS[event]):
            advance(columns, schedule)
        snapshots[event] = {
            role: unpack_lane(columns, lane_index[(event, role)])
            for role in ("first", "second", "determinism_duplicate")
        }
        phase_rows.append({
            "event": event,
            "start_moment": previous,
            "stop_moment": FUNNEL_MOMENTS[event],
            "updates": FUNNEL_MOMENTS[event] - previous,
            "active_lanes": active_mask.bit_count(),
            "instructions_per_update": len(schedule),
            "seconds": round(monotonic() - phase_started, 6),
        })
        active_mask &= ~sum(
            1 << lane_index[(event, role)]
            for role in ("first", "second", "determinism_duplicate")
        )
        previous = FUNNEL_MOMENTS[event]

    rows = []
    for event in EVENT_ORDER:
        first = snapshots[event]["first"]
        second = snapshots[event]["second"]
        duplicate = snapshots[event]["determinism_duplicate"]
        rows.append({
            "event": event,
            "first_key": (event, WITNESS_PAIRS[0]),
            "second_key": (event, WITNESS_PAIRS[1]),
            "funnel_moment": FUNNEL_MOMENTS[event],
            "first_sha256": state_sha256(first),
            "second_sha256": state_sha256(second),
            "hash_verified_vs_second":
                state_sha256(first) == state_sha256(second),
            "full_tuple_verified_vs_second": first == second,
            "determinism_duplicate_exact": first == duplicate,
        })
    funnels = {
        event: snapshots[event]["first"] for event in EVENT_ORDER
    }
    return {
        "funnels": funnels,
        "verification_rows": tuple(rows),
        "phase_rows": tuple(phase_rows),
        "duplicate_initial_exact": duplicate_initial,
        "pass": (
            duplicate_initial
            and all(
                row["hash_verified_vs_second"]
                and row["full_tuple_verified_vs_second"]
                and row["determinism_duplicate_exact"]
                for row in rows
            )
            and state_sha256(funnels[0]) == EXPECTED_SSTAR_SHA256
        ),
    }


def watched_registers() -> tuple[tuple[str, int], ...]:
    return (
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
        *((f"FRESH[{index}]", wire)
          for index, wire in enumerate(K.A.FRESH)),
        *((f"ZERO_WORK[{index}]", wire)
          for index, wire in enumerate(K.A.ZERO_WORK)),
        ("TOKEN_OK", K.A.TOKEN_OK),
    )


def residual_support(state: State) -> tuple[str, ...]:
    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    output: set[str] = set()
    if state[K.R3.X.SOURCE_POINTER]:
        output.add("source.SOURCE_POINTER")
    for bank_index, bank in enumerate(banks):
        for name, wire in watched_registers():
            if bank[wire]:
                output.add(f"bank{bank_index}.{name}")
    for link_index, link in enumerate(links):
        for wire, bit in enumerate(link):
            if bit:
                output.add(f"link{link_index}.wire[{wire}]")
    return tuple(sorted(output))


def anatomy(event: int, state: State) -> dict[str, object]:
    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    occupancy = tuple(
        tuple(bank[int(layout["valid"])] for layout in K.A.CELLS)
        for bank in banks
    )
    tokens = tuple(
        tuple(bank[wire] for wire in K.A.TOKEN) for bank in banks
    )
    link_weights = tuple(map(sum, links))
    residual = residual_support(state)
    return {
        "event": event,
        "name": {0: "S*", 2: "S2", 1: "S1"}[event],
        "funnel_moment": FUNNEL_MOMENTS[event],
        "state_bits": len(state),
        "sha256": state_sha256(state),
        "weight": sum(state),
        "bank_weights": tuple(map(sum, banks)),
        "occupancy": occupancy,
        "tokens": tokens,
        "link_weights": link_weights,
        "residual": residual,
        "source_active_indices": tuple(
            wire for wire in range(K.M.R12.SOURCE_WIDTH) if state[wire]
        ),
        "pass": (
            len(state) == STATE_BITS
            and sum(state) == EXPECTED_WEIGHTS[event]
            and occupancy == ((1, 1), (0, 0))
            and tokens == ((1, 0), (0, 0))
            and link_weights == (0,)
            and residual == (
                "bank0.DIRECTION_OK",
                "source.SOURCE_POINTER",
            )
        ),
    }


def _bank_wire_aliases() -> dict[int, tuple[str, ...]]:
    aliases: dict[int, list[str]] = {
        wire: [] for wire in range(K.A.N)
    }
    for cell, layout in enumerate(K.A.CELLS):
        for field, value in layout.items():
            if field == "payload":
                continue
            if isinstance(value, tuple):
                for index, wire in enumerate(value):
                    aliases[int(wire)].append(
                        f"cell{cell}.{field}[{index}]"
                    )
            else:
                aliases[int(value)].append(f"cell{cell}.{field}")
    for register in ("HEAD", "ROTOR", "TOKEN", "FRESH", "ZERO_WORK"):
        for index, wire in enumerate(getattr(K.A, register)):
            aliases[int(wire)].append(f"{register}[{index}]")
    for register in (
        "POINTER", "U_TO_V", "V_TO_U", "BINDER", "ACTUAL", "ADMISS",
        "LAW", "TOKEN_OK", "DIRECTION_OK", "ENABLE_TARGET",
    ):
        aliases[int(getattr(K.A, register))].append(register)
    return {
        wire: tuple(names) for wire, names in aliases.items()
    }


BANK_WIRE_ALIASES = _bank_wire_aliases()
SOURCE_NAMES = {
    K.R3.X.LEFT_ENDPOINT: "LEFT_ENDPOINT",
    K.R3.X.RIGHT_ENDPOINT: "RIGHT_ENDPOINT",
    K.R3.X.SOURCE_POINTER: "SOURCE_POINTER",
}


def wire_name(wire: int) -> str:
    """Decode a packed index using the cited state-object layout."""
    if wire < K.M.R12.SOURCE_WIDTH:
        return f"source.{SOURCE_NAMES.get(wire, f'wire[{wire}]')}"
    for bank, base in enumerate(
        K.M.R12.BANK_BASES[:FIXTURE_BANKS]
    ):
        if base <= wire < base + K.A.N:
            local = wire - base
            aliases = BANK_WIRE_ALIASES[local]
            label = "|".join(aliases) if aliases else f"wire[{local}]"
            return f"bank{bank}.{label}"
    for link, base in enumerate(
        K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]
    ):
        if base <= wire < base + K.B.LINK_WIDTH:
            return f"link{link}.wire[{wire - base}]"
    return f"unused_padding.wire[{wire}]"


def field_group(name: str) -> str:
    head = name.split("|", 1)[0]
    return head.split("[", 1)[0]


def xor_support(left: State, right: State) -> tuple[int, ...]:
    return tuple(
        wire for wire, (a, b) in enumerate(zip(left, right)) if a != b
    )


def apply_named_xor_update(
    state: State,
    named_mask: tuple[str, ...],
) -> State:
    by_name = {wire_name(wire): wire for wire in range(len(state))}
    if len(by_name) != len(state):
        raise AssertionError("wire decoder is not injective")
    output = list(state)
    for name in named_mask:
        output[by_name[name]] ^= 1
    return tuple(output)


def diff_localization_certificate(
    funnels: dict[int, State],
) -> dict[str, object]:
    pair_rows = []
    masks: dict[str, tuple[str, ...]] = {}
    all_support: set[int] = set()
    for left, right in ((0, 2), (0, 1), (2, 1)):
        support = xor_support(funnels[left], funnels[right])
        all_support.update(support)
        names = tuple(wire_name(wire) for wire in support)
        transitions = tuple(
            f"{wire_name(wire)}:{funnels[left][wire]}->{funnels[right][wire]}"
            for wire in support
        )
        components = Counter(name.split(".", 1)[0] for name in names)
        groups = Counter(map(field_group, names))
        label = f"{left}->{right}"
        masks[label] = names
        pair_rows.append({
            "map": label,
            "xor_weight": len(support),
            "expected_xor_weight": EXPECTED_XOR_WEIGHTS[(left, right)],
            "components": dict(sorted(components.items())),
            "named_field_groups": dict(sorted(groups.items())),
            "field_transitions": transitions,
            "all_fields_named": all(
                ".wire[" not in name and "unused_padding" not in name
                for name in names
            ),
        })

    named_union = tuple(wire_name(wire) for wire in sorted(all_support))
    outside_common = all(
        len({funnels[event][wire] for event in EVENT_ORDER}) == 1
        for wire in range(STATE_BITS) if wire not in all_support
    )
    localized = (
        outside_common
        and all(
            name.startswith((
                "source.LEFT_ENDPOINT",
                "source.RIGHT_ENDPOINT",
                "bank0.",
            ))
            for name in named_union
        )
        and all(
            ".wire[" not in name and "unused_padding" not in name
            for name in named_union
        )
    )

    first_image = apply_named_xor_update(funnels[0], masks["0->2"])
    second_image = apply_named_xor_update(first_image, masks["2->1"])
    first_exact = first_image == funnels[2]
    second_exact = second_image == funnels[1]
    direct_exact = (
        apply_named_xor_update(funnels[0], masks["0->1"])
        == funnels[1]
    )
    induced_map_exact = localized and first_exact and second_exact and direct_exact
    outcome = (
        "PRIMARY NO-MAP CLAIM INVERTED CONSTRUCTIVELY: exact localized "
        "arrival-rank field update maps S* -> S2 -> S1"
        if induced_map_exact else
        "PRIMARY NO-MAP CLAIM TIGHTENS: XOR support is scattered or the "
        "induced field update is not exact"
    )
    return {
        "state_object_citation": {
            "packing":
                f"{STATE_OBJECT_PATHS[0]}::pack_state/unpack_state",
            "bank_fields":
                f"{STATE_OBJECT_PATHS[1]}::CELLS/named registers",
        },
        "pairwise_field_maps": tuple(pair_rows),
        "localized_union_width": len(named_union),
        "localized_union_fields": named_union,
        "outside_union_exactly_common": outside_common,
        "localization":
            "source direction endpoints + named bank0 packet/register fields"
            if localized else "scattered/anonymous support",
        "candidate_transformation": {
            "operation":
                "XOR the listed named-field mask selected by arrival-rank edge",
            "rank0_to_rank1_event0_to_event2": masks["0->2"],
            "rank1_to_rank2_event2_to_event1": masks["2->1"],
            "direct_rank0_to_rank2_event0_to_event1": masks["0->1"],
            "Sstar_to_S2_exact": first_exact,
            "S2_to_S1_exact": second_exact,
            "Sstar_to_S1_direct_exact": direct_exact,
            "scope_honesty":
                "exact observed-three field map; not a future-event law",
        },
        "localized": localized,
        "induced_family_map_exact": induced_map_exact,
        "outcome": outcome,
        "pass": (
            all(
                row["xor_weight"] == row["expected_xor_weight"]
                and row["all_fields_named"]
                for row in pair_rows
            )
            and outside_common
            and first_exact
            and second_exact
            and direct_exact
        ),
    }


def predicate_certificate(catalog: tuple[Key, ...]) -> dict[str, object]:
    """Recompute the key geometry without importing any forecast primary."""
    event_rows = []
    for event in (0, 1, 2):
        declared = tuple((event, pair) for pair in BACKBONE)
        selected = tuple(
            key for key in catalog
            if key[0] == event
            and 0 not in key[1]
            and cyclic_separation(key[1]) == RING_STATIONS // 2
        )
        declared_set = set(declared)
        selected_set = set(selected)
        event_rows.append({
            "event": event,
            "predicate":
                f"event={event} AND origin absent AND max-sep=5",
            "selected_count": len(selected),
            "true_positives": len(declared_set & selected_set),
            "false_positives": tuple(sorted(selected_set - declared_set)),
            "false_negatives": tuple(sorted(declared_set - selected_set)),
            "entrants_imply_predicate": all(
                key in selected_set for key in declared
            ),
            "predicate_implies_entrant": all(
                key in declared_set for key in selected
            ),
            "both_directions_exact": selected == declared,
        })
    pair_selector = tuple(
        pair for pair in separated_pairs()
        if 0 not in pair
        and cyclic_separation(pair) == RING_STATIONS // 2
    )
    result = {
        "own_key_structure": {
            "ring_stations": RING_STATIONS,
            "events": tuple(range(2 * FIXTURE_BANKS)),
            "pair_rule": "unordered pairs with cyclic separation > 1",
            "pair_count": len(separated_pairs()),
            "catalog_count": len(catalog),
        },
        "unified_predicate":
            "event=e AND origin absent AND max-sep=5",
        "pair_selector": pair_selector,
        "event_rows": tuple(event_rows),
        "checked_keys_per_direction": len(catalog),
        "pass": (
            len(catalog) == FAMILY_SIZE
            and len(set(catalog)) == FAMILY_SIZE
            and pair_selector == BACKBONE
            and all(row["both_directions_exact"] for row in event_rows)
        ),
    }
    return result


def weight_law_certificate(
    anatomies: dict[int, dict[str, object]],
) -> dict[str, object]:
    rows = tuple({
        "arrival_rank": rank,
        "event": event,
        "observed_weight": anatomies[event]["weight"],
        "formula_weight": 44 + rank,
        "exact": anatomies[event]["weight"] == 44 + rank,
    } for rank, event in enumerate(EVENT_ORDER))
    return {
        "arrival_order": EVENT_ORDER,
        "weights": tuple(
            anatomies[event]["weight"] for event in EVENT_ORDER
        ),
        "candidate": "weight = 44 + arrival rank",
        "honesty":
            "exact on these three points only; localization supplies the "
            "content, and no future-event theorem is inferred",
        "rows": rows,
        "pass": all(row["exact"] for row in rows),
    }


def stable_output(report: dict[str, object]) -> str:
    report["controls"]["stdout_bytes"] = 0
    for _ in range(12):
        output = compact(report) + "\n"
        size = len(output.encode("utf-8"))
        if report["controls"]["stdout_bytes"] == size:
            return output
        report["controls"]["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    sources = source_controls()
    selected = build_selected_entrants()
    reconstruction = reconstruct_funnels_independently(selected)
    funnels = reconstruction["funnels"]
    anatomies = {
        event: anatomy(event, funnels[event]) for event in EVENT_ORDER
    }
    anatomy_certificate = {
        "finding":
            "S*, S2, S1 independently reconstructed from one entrant each; "
            "each full tuple and SHA-256 verified against a second entrant",
        "verification_rows": reconstruction["verification_rows"],
        "anatomies": tuple(anatomies[event] for event in EVENT_ORDER),
        "expected_pairwise_xor_weights": tuple({
            "left_event": left,
            "right_event": right,
            "xor_weight": weight,
        } for (left, right), weight in EXPECTED_XOR_WEIGHTS.items()),
        "pass": (
            selected["summary"]["pass"]
            and reconstruction["pass"]
            and all(row["pass"] for row in anatomies.values())
            and all(
                len(xor_support(funnels[left], funnels[right])) == expected
                for (left, right), expected in EXPECTED_XOR_WEIGHTS.items()
            )
        ),
    }
    localization = diff_localization_certificate(funnels)
    predicate = predicate_certificate(selected["catalog"])
    weight_law = weight_law_certificate(anatomies)

    elapsed = monotonic() - started
    deterministic = (
        reconstruction["duplicate_initial_exact"]
        and all(
            row["determinism_duplicate_exact"]
            for row in reconstruction["verification_rows"]
        )
    )
    blocklist_clean = (
        not FIREWALL.hits
        and not any(
            name in sys.modules for name in BLOCKLISTED_MODULES
        )
    )
    controls_pass_before_stdout = (
        sources["pass"]
        and deterministic
        and blocklist_clean
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    certificates = {
        "ANATOMY_RE_DERIVATION": anatomy_certificate,
        "THE_DIFF_LOCALIZATION": localization,
        "THE_PREDICATE": predicate,
        "THE_WEIGHT_LAW": weight_law,
    }
    named_checks = {
        name: bool(certificate["pass"])
        for name, certificate in certificates.items()
    }
    named_checks["CONTROLS"] = controls_pass_before_stdout
    report: dict[str, Any] = {
        "cycle": 833,
        "checker": "INDEPENDENT_ADVERSARIAL_DIFF_LOCALIZATION",
        "named_certificates": {
            name: "PASS" if passed else "FAIL"
            for name, passed in named_checks.items()
        },
        "findings_verbatim": {
            "ANATOMY_RE_DERIVATION":
                anatomy_certificate["finding"],
            "THE_DIFF_LOCALIZATION": localization["outcome"],
            "THE_PREDICATE":
                "Unified predicate verified both directions over all 176 keys",
            "THE_WEIGHT_LAW":
                "44/45/46 equals 44 + arrival rank on exactly the three "
                "observed points",
        },
        "selected_family_rebuild": selected["summary"],
        "reconstruction_phases": reconstruction["phase_rows"],
        "certificates": certificates,
        "source_controls": sources,
        "controls": {
            "sha_controls_exact": sources["sha256"] == EXPECTED_SHA256,
            "blocklisted_primaries": TEXT_AST_ONLY_PATHS,
            "blocklist_text_AST_only_clean": blocklist_clean,
            "determinism": deterministic,
            "literal_AUDIT_INPUT_PATHS":
                sources["AUDIT_INPUT_PATHS_literal"],
            "existing_worktree_relative":
                sources["existing_worktree_relative"],
            "files_read": len(AUDIT_INPUT_PATHS),
            "files_read_limit": 6,
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_bytes": 0,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "pass": controls_pass_before_stdout,
        },
        "overall": "PASS" if all(named_checks.values()) else "FAIL",
        "terminal": (
            "CYCLE833_INDEPENDENT_ADVERSARIAL_CHECK_PASS"
            if all(named_checks.values()) else
            "CYCLE833_INDEPENDENT_ADVERSARIAL_CHECK_FAIL"
        ),
    }
    output = stable_output(report)
    stdout_ok = len(output.encode("utf-8")) < STDOUT_LIMIT_BYTES
    if not stdout_ok:
        sys.stdout.write(compact({
            "overall": "FAIL",
            "terminal": "CYCLE833_INDEPENDENT_ADVERSARIAL_CHECK_FAIL",
            "failure": "stdout limit exceeded",
            "stdout_bytes": len(output.encode("utf-8")),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }) + "\n")
        return 1
    report["controls"]["pass"] = controls_pass_before_stdout and stdout_ok
    named_checks["CONTROLS"] = report["controls"]["pass"]
    report["named_certificates"]["CONTROLS"] = (
        "PASS" if named_checks["CONTROLS"] else "FAIL"
    )
    report["overall"] = "PASS" if all(named_checks.values()) else "FAIL"
    report["terminal"] = (
        "CYCLE833_INDEPENDENT_ADVERSARIAL_CHECK_PASS"
        if all(named_checks.values()) else
        "CYCLE833_INDEPENDENT_ADVERSARIAL_CHECK_FAIL"
    )
    output = stable_output(report)
    sys.stdout.write(output)
    return 0 if report["overall"] == "PASS" else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(compact({
            "overall": "FAIL",
            "terminal": "CYCLE833_INDEPENDENT_ADVERSARIAL_CHECK_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
