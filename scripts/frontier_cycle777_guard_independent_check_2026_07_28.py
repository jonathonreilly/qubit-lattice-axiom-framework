#!/usr/bin/env python3
"""Independent adversarial check of the Cycle-777 prefix-closed guard claim.

This checker does not import or execute either the Cycle-770 or Cycle-777
primary.  It rebuilds their finite composition from the landed Cycle-745 and
Cycle-719 modules, inventories other refusal/guard/syndrome surfaces by AST,
and attacks the proposed guard beyond the primary's frozen battery.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from hashlib import sha256
import importlib
import json
from pathlib import Path
import re
from time import perf_counter
from typing import Any, Iterable


AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
)
BLOCKLIST_TEXT_PATHS = (
    "scripts/frontier_cycle770_lock_composed_formation_2026_07_28.py",
    "scripts/frontier_cycle777_prefix_closed_guard_2026_07_28.py",
)
EXPECTED_SHA256 = {
    "scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py":
        "d8c1651eb8cdd25a797881b55b81234a5816407418ef415491ecef41672bd708",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py":
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py":
        "ef9398b3f27dcbb540446d6c5c165c5803014cffa37da59071751810a7ac9978",
    "scripts/frontier_cycle770_lock_composed_formation_2026_07_28.py":
        "9f886b8afb8ea4391bc1c17335bc91c6e9da4cdab6961d0a55d733509631c703",
    "scripts/frontier_cycle777_prefix_closed_guard_2026_07_28.py":
        "c4bb14040957cd2509d738a56ce13f436f0ac4449cd8eac1a051b396c951b652",
}
FOCUS_INVENTORY_PATHS = (
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
    "scripts/frontier_cycle717_interbank_allocator_handoff_2026_07_26.py",
    "scripts/frontier_cycle724_local_token_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle730_charge_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
    "scripts/frontier_cycle743_law_flag_derived_2026_07_28.py",
    "scripts/frontier_cycle747_admiss_verdict_binding_2026_07_28.py",
    "scripts/frontier_cycle754_composed_four_flag_acceptance_2026_07_28.py",
)
EXPECTED_BASELINE_NAMES = (
    "inverse_word_application_1",
    "inverse_word_application_2",
    *(f"partial_inverse_prefix_{length}" for length in range(1, 8)),
    "mode6_forward_word_replay_double_write",
    "declared_alphabet_IDLE",
    "declared_alphabet_READ",
    "declared_alphabet_WRITE[0]",
    "declared_alphabet_WRITE[1]",
    *(f"direct_bank_station_{station}" for station in (
        1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55
    )),
)
EXPECTED_SHARED_GUARD_NAMES = (
    *EXPECTED_BASELINE_NAMES,
    *(f"record_forward_prefix_{length}" for length in range(1, 8)),
    *(f"guard_inverse_prefix_{length}" for length in range(1, 8)),
    *(f"guard_forward_prefix_{length}" for length in range(1, 8)),
    "guard_direct_X_D",
    "guard_direct_X_U",
    "guard_direct_X_L",
)
ROOT = Path(__file__).resolve().parents[1]
SCAN_PATTERN = re.compile(
    r"\b(?:Q_refuse|REFUSED|refus[a-z_]*|syndrome[a-z_]*|guard[a-z_]*)\b",
    re.IGNORECASE,
)
ROLLBACK_PATTERN = re.compile(
    r"\b(?:rollback|roll_back|atomic|restore|restoration)\b",
    re.IGNORECASE,
)


Persistent = tuple[int, int, int]


@dataclass(frozen=True)
class RailGuard:
    primary: tuple[Persistent, ...]
    cells: tuple[Persistent, ...]
    rail_order: tuple[str, ...]


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def ast_digest(source: bytes) -> str:
    tree = ast.parse(source.decode("utf-8"))
    dumped = ast.dump(tree, annotate_fields=True, include_attributes=False)
    return sha256(dumped.encode("utf-8")).hexdigest()


def file_snapshot(paths: Iterable[str]) -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for relative in paths:
        source = (ROOT / relative).read_bytes()
        result[relative] = {
            "ast_sha256": ast_digest(source),
            "bytes": len(source),
            "sha256": sha256(source).hexdigest(),
        }
    return result


def bytes_to_bits(payload: bytes) -> tuple[int, ...]:
    return tuple(
        (byte >> bit_index) & 1
        for byte in payload
        for bit_index in range(8)
    )


def bits_to_bytes(bits: Iterable[int]) -> bytes:
    row = tuple(int(bit) for bit in bits)
    if len(row) % 8:
        raise ValueError("payload bit count must be byte aligned")
    return bytes(
        sum(row[offset + index] << index for index in range(8))
        for offset in range(0, len(row), 8)
    )


def payload_bytes(rows: object) -> bytes:
    return canonical_json(rows).encode("utf-8")


def import_landed() -> tuple[Any, Any, Any]:
    C745 = importlib.import_module(
        "frontier_cycle745_enforced_dual_rail_lock_2026_07_28"
    )
    K719 = importlib.import_module(
        "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
    )
    C719 = importlib.import_module(
        "frontier_cycle719_recurrent_matter_history_controller_2026_07_26"
    )
    return C745, K719, C719


def origin_zero_branches(C719: Any) -> tuple[int, ...]:
    banks, links = C719.B.chain_genesis(C719.BANKS)
    initial = C719.tuple_to_int(
        C719.M.pack_state(banks, links, matter=1)
    )
    branches = C719.C713.apply_sparse_word(
        {initial: 1.0 + 0.0j}, C719.MATTER_WORD
    )
    return tuple(sorted(branches))


def decoded_rows(C719: Any, data: int) -> tuple[dict[str, object], ...]:
    bits = C719.int_to_tuple(data)
    banks, links = C719.M.unpack_state(bits, C719.BANKS)
    try:
        chain, _order = C719.B.decode_local_graph(banks, links)
    except ValueError:
        return ()
    return tuple(dict(row) for row in C719.B.cell_rows(chain))


def first_write_payload(
    C745: Any,
    content: bytes,
) -> tuple[tuple[Persistent, ...], dict[str, object]]:
    input_bits = bytes_to_bits(content)
    events = tuple(
        C745.apply_word(
            C745.packet((0, *C745.UNLOCKED), offered),
            C745.WRITE_WORD,
        )
        for offered in input_bits
    )
    persistent = tuple(C745.persistent(event) for event in events)
    tags = tuple(C745.output_tag(event) for event in events)
    stored = bits_to_bytes(state[0] for state in persistent)
    accepted = (
        bool(input_bits)
        and all(tag == "ACCEPTED" for tag in tags)
        and all(state[1:] == C745.LOCKED for state in persistent)
        and stored == content
    )
    return persistent, {
        "accepted": accepted,
        "content": stored,
        "payload_bits": len(input_bits),
    }


def forward_mode6(C745: Any, C719: Any) -> dict[str, object]:
    branches = {
        (source & 4095).bit_length() - 1: source
        for source in origin_zero_branches(C719)
    }
    source = branches[6]
    initial_full = C719.controller_full_input(source)
    full = initial_full
    engagement: dict[str, object] | None = None
    persistent: tuple[Persistent, ...] | None = None
    content: bytes | None = None
    for orbit_step in range(C719.CONTROLLER_STATIONS):
        before = C719.controller_register_rows(full)
        before_data = int(before["data"])
        live_a = tuple(index for index, value in enumerate(before["A"]) if value)
        full = C719.apply_fast_int(full, C719.CONTROLLER_H_FAST)
        after_data = int(C719.controller_register_rows(full)["data"])
        if before_data == after_data:
            continue
        rows = decoded_rows(C719, after_data)
        accepted_shape = bool(rows) and all(
            row["binder"] == row["valid"] == 1 for row in rows
        )
        if accepted_shape and engagement is None:
            content = payload_bytes(rows)
            persistent, evidence = first_write_payload(C745, content)
            station = live_a[0] if len(live_a) == 1 else None
            engagement = {
                **evidence,
                "orbit_step": orbit_step,
                "program_kind": (
                    C719.PROGRAM[station][0] if station is not None else None
                ),
                "station": station,
            }
    if engagement is None or persistent is None or content is None:
        raise RuntimeError("mode 6 produced no decodable EventCell")
    return {
        "content": content,
        "engagement": engagement,
        "final_full": full,
        "initial_full": initial_full,
        "persistent": persistent,
        "source": source,
    }


def apply_payload_word(
    C745: Any,
    before: tuple[Persistent, ...],
    offered_content: bytes,
    word: tuple[Any, ...],
    name: str,
) -> tuple[tuple[Persistent, ...], dict[str, object]]:
    offered_bits = bytes_to_bits(offered_content)
    if len(before) != len(offered_bits):
        raise ValueError("payload width mismatch")
    events = tuple(
        C745.apply_word(C745.packet(storage, offered), word)
        for storage, offered in zip(before, offered_bits)
    )
    after = tuple(C745.persistent(event) for event in events)
    tags = tuple(C745.output_tag(event) for event in events)
    q_in = tuple(event[C745.RAIL_INDEX["Q_in"]] for event in events)
    q_accept = tuple(
        event[C745.RAIL_INDEX["Q_accept"]] for event in events
    )
    q_refuse = tuple(
        event[C745.RAIL_INDEX["Q_refuse"]] for event in events
    )
    syndrome = (
        bool(events)
        and all(tag == "REFUSED" for tag in tags)
        and all(q_refuse)
        and not any(q_in)
        and not any(q_accept)
    )
    exact = after == before
    return after, {
        "exact": exact,
        "mutation": not exact,
        "name": name,
        "q_accept_count": sum(q_accept),
        "q_in_count": sum(q_in),
        "q_refuse_count": sum(q_refuse),
        "refused": syndrome and exact,
        "syndrome": syndrome,
    }


def direct_bank_proposals(
    K719: Any,
    C719: Any,
    final_full: int,
) -> dict[str, bytes]:
    data = int(C719.controller_register_rows(final_full)["data"])
    before = C719.int_to_tuple(data)
    proposals: dict[str, bytes] = {}
    for station, row in enumerate(C719.PROGRAM):
        if row[0] != "bank":
            continue
        after = K719.A.apply_semantic(before, K719.mapped_macro(row))
        rows = decoded_rows(C719, C719.tuple_to_int(after))
        proposals[f"direct_bank_station_{station}"] = payload_bytes(rows)
    return proposals


def baseline_battery(
    C745: Any,
    K719: Any,
    C719: Any,
    forward: dict[str, object],
) -> tuple[dict[str, object], dict[str, tuple[Persistent, ...]]]:
    content = forward["content"]
    pristine = forward["persistent"]
    final_full = forward["final_full"]
    if (
        not isinstance(content, bytes)
        or not isinstance(pristine, tuple)
        or not isinstance(final_full, int)
    ):
        raise TypeError("invalid independent mode-6 representation")
    complement = bytes(byte ^ 0xFF for byte in content)
    rows: list[dict[str, object]] = []
    candidates: dict[str, tuple[Persistent, ...]] = {}

    current = pristine
    for application in (1, 2):
        name = f"inverse_word_application_{application}"
        current, receipt = apply_payload_word(
            C745, current, complement, C745.REVERSE_WRITE_WORD, name
        )
        rows.append(receipt)
        candidates[name] = current

    for length in range(1, len(C745.REVERSE_WRITE_WORD)):
        name = f"partial_inverse_prefix_{length}"
        after, receipt = apply_payload_word(
            C745,
            pristine,
            complement,
            C745.REVERSE_WRITE_WORD[:length],
            name,
        )
        rows.append(receipt)
        candidates[name] = after

    name = "mode6_forward_word_replay_double_write"
    after, receipt = apply_payload_word(
        C745, pristine, content, C745.WRITE_WORD, name
    )
    rows.append(receipt)
    candidates[name] = after

    macro_words = {
        "IDLE": C745.IDLE_WORD,
        "READ": C745.READ_WORD,
        "WRITE[0]": C745.WRITE_WORD,
        "WRITE[1]": C745.WRITE_WORD,
    }
    for macro in C745.ALPHABET_SCOPE:
        if macro == "WRITE[0]":
            offered = bytes(len(content))
        elif macro == "WRITE[1]":
            offered = bytes([0xFF]) * len(content)
        else:
            offered = complement
        name = f"declared_alphabet_{macro}"
        after, receipt = apply_payload_word(
            C745, pristine, offered, macro_words[macro], name
        )
        rows.append(receipt)
        candidates[name] = after

    proposals = direct_bank_proposals(K719, C719, final_full)
    for name, proposed in proposals.items():
        # Cycle-770 treats direct-bank changes outside the lock request port.
        # Reproduce its mutation criterion, then separately build the proposed
        # lock state via an ordinary locked request for the guard battery.
        bare_mutation = proposed != content
        rows.append({
            "exact": not bare_mutation,
            "mutation": bare_mutation,
            "name": name,
            "q_accept_count": 0,
            "q_in_count": 0,
            "q_refuse_count": 0,
            "refused": False,
            "syndrome": False,
        })
        fixed = proposed if len(proposed) == len(content) else bytes(len(content))
        after, _receipt = apply_payload_word(
            C745, pristine, fixed, C745.WRITE_WORD, name
        )
        candidates[name] = after

    names = tuple(row["name"] for row in rows)
    mutations = [
        str(row["name"])
        for row in rows
        if row["mutation"] and not row["refused"]
    ]
    return {
        "attack_count": len(rows),
        "manifest_exact": names == EXPECTED_BASELINE_NAMES,
        "refused_count": sum(bool(row["refused"]) for row in rows),
        "rows": rows,
        "surviving_unrefused_mutations": mutations,
    }, candidates


def build_guard(C745: Any, primary: tuple[Persistent, ...]) -> RailGuard:
    cells: list[Persistent] = []
    order: list[str] = []
    for payload_index, storage in enumerate(primary):
        for rail_index, rail in enumerate(("D", "U", "L")):
            offered = storage[rail_index]
            event = C745.apply_word(
                C745.packet((0, *C745.UNLOCKED), offered),
                C745.WRITE_WORD,
            )
            if (
                C745.output_tag(event) != "ACCEPTED"
                or C745.persistent(event) != (offered, *C745.LOCKED)
            ):
                raise AssertionError("landed guard-cell first write failed")
            cells.append(C745.persistent(event))
            order.append(f"payload[{payload_index}].{rail}")
    return RailGuard(primary, tuple(cells), tuple(order))


def guard_bytes(guard: RailGuard) -> bytes:
    return bytes(
        bit
        for storage in (*guard.primary, *guard.cells)
        for bit in storage
    )


def tensor_guard_request(
    C745: Any,
    guard: RailGuard,
    proposed_primary: tuple[Persistent, ...],
) -> tuple[RailGuard, dict[str, object]]:
    proposed_bits = tuple(bit for storage in proposed_primary for bit in storage)
    if len(proposed_bits) != len(guard.cells):
        raise ValueError("guard tensor width mismatch")
    events = tuple(
        C745.apply_word(C745.packet(cell, offered), C745.WRITE_WORD)
        for cell, offered in zip(guard.cells, proposed_bits)
    )
    after_cells = tuple(C745.persistent(event) for event in events)
    tags = tuple(C745.output_tag(event) for event in events)
    refused = (
        bool(events)
        and all(tag == "REFUSED" for tag in tags)
        and after_cells == guard.cells
    )
    after = (
        guard
        if refused
        else RailGuard(proposed_primary, after_cells, guard.rail_order)
    )
    return after, {
        "q_refuse_count": sum(
            event[C745.RAIL_INDEX["Q_refuse"]] for event in events
        ),
        "refused": refused,
    }


def apply_word_to_guard_cells(
    C745: Any,
    guard: RailGuard,
    word: tuple[Any, ...],
    *,
    event_repetitions: int = 1,
) -> tuple[RailGuard, dict[str, object]]:
    cells = guard.cells
    final_events: tuple[tuple[int, ...], ...] = ()
    for _repeat in range(event_repetitions):
        final_events = tuple(
            C745.apply_word(
                C745.packet(cell, 1 - cell[0]),
                word,
            )
            for cell in cells
        )
        cells = tuple(C745.persistent(event) for event in final_events)
    tags = tuple(C745.output_tag(event) for event in final_events)
    syndrome = (
        bool(final_events)
        and all(tag == "REFUSED" for tag in tags)
    )
    exact = cells == guard.cells
    return RailGuard(guard.primary, cells, guard.rail_order), {
        "exact": exact,
        "mutated_cells": sum(
            observed != expected
            for observed, expected in zip(cells, guard.cells)
        ),
        "q_refuse_count": sum(
            event[C745.RAIL_INDEX["Q_refuse"]] for event in final_events
        ),
        "refused": syndrome and exact,
        "syndrome": syndrome,
    }


def direct_x_guard_cells(
    C745: Any,
    guard: RailGuard,
    rails: tuple[str, ...],
) -> tuple[RailGuard, dict[str, object]]:
    word = tuple(
        C745.Gate(f"independent_hostile_X_{rail}", "X", (rail,))
        for rail in rails
    )
    return apply_word_to_guard_cells(C745, guard, word)


def apply_event_sequence_to_guard_cells(
    C745: Any,
    guard: RailGuard,
    words: tuple[tuple[Any, ...], ...],
) -> tuple[RailGuard, dict[str, object]]:
    cells = guard.cells
    final_events: tuple[tuple[int, ...], ...] = ()
    syndrome_events = 0
    for word in words:
        final_events = tuple(
            C745.apply_word(C745.packet(cell, 1 - cell[0]), word)
            for cell in cells
        )
        tags = tuple(C745.output_tag(event) for event in final_events)
        syndrome_events += int(
            bool(final_events) and all(tag == "REFUSED" for tag in tags)
        )
        cells = tuple(C745.persistent(event) for event in final_events)
    final_tags = tuple(C745.output_tag(event) for event in final_events)
    final_syndrome = (
        bool(final_events)
        and all(tag == "REFUSED" for tag in final_tags)
    )
    exact = cells == guard.cells
    return RailGuard(guard.primary, cells, guard.rail_order), {
        "exact": exact,
        "mutated_cells": sum(
            observed != expected
            for observed, expected in zip(cells, guard.cells)
        ),
        "refused": final_syndrome and exact,
        "syndrome": bool(syndrome_events),
        "syndrome_event_count": syndrome_events,
    }


def shared_guard_battery(
    C745: Any,
    guard: RailGuard,
    baseline_candidates: dict[str, tuple[Persistent, ...]],
    content: bytes,
) -> dict[str, object]:
    candidates = dict(baseline_candidates)
    complement = bytes(byte ^ 0xFF for byte in content)
    for length in range(1, len(C745.WRITE_WORD)):
        name = f"record_forward_prefix_{length}"
        candidates[name] = apply_payload_word(
            C745,
            guard.primary,
            complement,
            C745.WRITE_WORD[:length],
            name,
        )[0]

    before_bytes = guard_bytes(guard)
    rows: list[dict[str, object]] = []
    for name in (
        *EXPECTED_BASELINE_NAMES,
        *(f"record_forward_prefix_{length}" for length in range(1, 8)),
    ):
        proposed = candidates[name]
        after, receipt = tensor_guard_request(C745, guard, proposed)
        rows.append({
            "byte_identical": guard_bytes(after) == before_bytes,
            "mutation": after != guard,
            "name": name,
            "refused": receipt["refused"],
            "target": "record_and_inner_lock",
        })

    for direction, word in (
        ("inverse", C745.REVERSE_WRITE_WORD),
        ("forward", C745.WRITE_WORD),
    ):
        for length in range(1, len(word)):
            name = f"guard_{direction}_prefix_{length}"
            after, receipt = apply_word_to_guard_cells(
                C745, guard, word[:length]
            )
            rows.append({
                "byte_identical": guard_bytes(after) == before_bytes,
                "mutation": after != guard,
                "name": name,
                "refused": receipt["refused"],
                "target": "outermost_guard_cells",
            })
    for rail in ("D", "U", "L"):
        name = f"guard_direct_X_{rail}"
        after, receipt = direct_x_guard_cells(C745, guard, (rail,))
        rows.append({
            "byte_identical": guard_bytes(after) == before_bytes,
            "mutation": after != guard,
            "name": name,
            "refused": receipt["refused"],
            "target": "outermost_guard_cells",
        })

    names = tuple(str(row["name"]) for row in rows)
    return {
        "attack_count": len(rows),
        "manifest_exact": names == EXPECTED_SHARED_GUARD_NAMES,
        "mutating_survivors": [
            str(row["name"])
            for row in rows
            if row["mutation"] and not row["refused"]
        ],
        "refused_count": sum(bool(row["refused"]) for row in rows),
        "rows": rows,
        "survivors": [
            str(row["name"]) for row in rows if not row["refused"]
        ],
    }


def extension_battery(C745: Any, guard: RailGuard) -> dict[str, object]:
    """Attack every one of the 2,232 outer cells with three new families."""
    rows: list[dict[str, object]] = []

    # Gate-level interleave: reverse prefix, one lawful forward-word gate,
    # then resume the reverse suffix.  Test every possible forward gate.
    for prefix in range(1, len(C745.REVERSE_WRITE_WORD)):
        for forward_index, forward_gate in enumerate(C745.WRITE_WORD, 1):
            word = (
                C745.REVERSE_WRITE_WORD[:prefix]
                + (forward_gate,)
                + C745.REVERSE_WRITE_WORD[prefix:]
            )
            name = (
                f"interleaved_inverse_prefix_{prefix}"
                f"_forward_gate_{forward_index}_resume"
            )
            after, receipt = apply_word_to_guard_cells(C745, guard, word)
            rows.append({
                "mutated_cells": receipt["mutated_cells"],
                "mutation": after != guard,
                "name": name,
                "refused": receipt["refused"],
                "syndrome": receipt["syndrome"],
            })

    # Event-boundary interleave: the requested prefix event, one complete
    # lawful forward WRITE event, then the remaining inverse gates as an event.
    for prefix in range(1, len(C745.REVERSE_WRITE_WORD)):
        name = f"interleaved_inverse_prefix_{prefix}_lawful_WRITE_resume"
        after, receipt = apply_event_sequence_to_guard_cells(
            C745,
            guard,
            (
                C745.REVERSE_WRITE_WORD[:prefix],
                C745.WRITE_WORD,
                C745.REVERSE_WRITE_WORD[prefix:],
            ),
        )
        rows.append({
            "mutated_cells": receipt["mutated_cells"],
            "mutation": after != guard,
            "name": name,
            "refused": receipt["refused"],
            "syndrome": receipt["syndrome"],
        })

    # Repeat each proper prefix both continuously and across event boundaries.
    for prefix in range(1, len(C745.REVERSE_WRITE_WORD)):
        partial = C745.REVERSE_WRITE_WORD[:prefix]
        for boundary, word, repeats in (
            ("same_event", partial + partial, 1),
            ("new_event", partial, 2),
        ):
            name = f"repeated_inverse_prefix_{prefix}_{boundary}"
            after, receipt = apply_word_to_guard_cells(
                C745, guard, word, event_repetitions=repeats
            )
            rows.append({
                "mutated_cells": receipt["mutated_cells"],
                "mutation": after != guard,
                "name": name,
                "refused": receipt["refused"],
                "syndrome": receipt["syndrome"],
            })

    # Direct combinations supplement the primary's one-rail attacks.
    for rails in (("D", "U"), ("D", "L"), ("U", "L"), ("D", "U", "L")):
        name = "guard_direct_" + "_then_".join(f"X_{rail}" for rail in rails)
        after, receipt = direct_x_guard_cells(C745, guard, rails)
        rows.append({
            "mutated_cells": receipt["mutated_cells"],
            "mutation": after != guard,
            "name": name,
            "refused": receipt["refused"],
            "syndrome": receipt["syndrome"],
        })

    mutating_survivors = [
        str(row["name"])
        for row in rows
        if row["mutation"] and not row["refused"]
    ]
    return {
        "attack_count": len(rows),
        "guard_cells_targeted_per_attack": len(guard.cells),
        "mutating_survivor_count": len(mutating_survivors),
        "mutating_survivors": mutating_survivors,
        "refused_count": sum(bool(row["refused"]) for row in rows),
        "rows": rows,
    }


def node_verbatim(source: str, node: ast.AST) -> str:
    segment = ast.get_source_segment(source, node)
    return (segment if segment is not None else ast.unparse(node)).strip()


def assignment_names(node: ast.AST) -> tuple[str, ...]:
    targets: list[ast.AST] = []
    if isinstance(node, ast.Assign):
        targets.extend(node.targets)
    elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
        targets.append(node.target)
    names: list[str] = []
    for target in targets:
        for item in ast.walk(target):
            if isinstance(item, ast.Name):
                names.append(item.id)
    return tuple(names)


def cycle745_ast_inventory() -> dict[str, object]:
    """Exhaustively select the refusal/syndrome AST under printed rules."""
    path = ROOT / AUDIT_INPUT_PATHS[0]
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)

    refusal_gates = []
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "Gate"
            and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
            and "refuse" in node.args[0].value.lower()
        ):
            refusal_gates.append({
                "line": node.lineno,
                "name": node.args[0].value,
                "verbatim": node_verbatim(source, node),
            })

    marker = re.compile(
        r"(?:refus|dirty|LOCKED|Q_in|Q_accept|Q_refuse|"
        r"output_tag|expected_refusal)"
    )
    condition_rows = []
    for node in ast.walk(tree):
        candidates: list[tuple[str, ast.AST]] = []
        if isinstance(node, ast.If):
            candidates.append(("If", node.test))
        elif isinstance(node, ast.IfExp):
            candidates.append(("IfExp", node.test))
        elif isinstance(node, ast.Assert):
            candidates.append(("Assert", node.test))
        elif isinstance(node, ast.comprehension):
            candidates.extend(("comprehension_if", test) for test in node.ifs)
        for kind, test in candidates:
            verbatim = node_verbatim(source, test)
            if marker.search(verbatim):
                condition_rows.append({
                    "kind": kind,
                    "line": getattr(test, "lineno", node.lineno),
                    "verbatim": verbatim,
                })

    computation_rows = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
            continue
        names = assignment_names(node)
        verbatim = node_verbatim(source, node)
        if (
            any(re.search(r"(?:refus|syndrome)", name, re.I) for name in names)
            or re.search(
                r"(?:Q_refuse|output_tag|expected_refusal)", verbatim
            )
        ):
            computation_rows.append({
                "line": node.lineno,
                "targets": names,
                "verbatim": verbatim,
            })

    result = {
        "condition_selection_rule": (
            "all If/IfExp/Assert/comprehension tests lexically containing "
            "refus|dirty|LOCKED|Q_in|Q_accept|Q_refuse|output_tag|"
            "expected_refusal"
        ),
        "conditions": sorted(
            condition_rows, key=lambda row: (int(row["line"]), str(row["kind"]))
        ),
        "refusal_gate_calls": sorted(
            refusal_gates, key=lambda row: int(row["line"])
        ),
        "syndrome_computation_selection_rule": (
            "all assignment nodes with refusal/syndrome target names or "
            "Q_refuse/output_tag/expected_refusal in the assigned expression"
        ),
        "syndrome_computations": sorted(
            computation_rows, key=lambda row: int(row["line"])
        ),
    }
    return {
        **result,
        "manifest_sha256": digest(result),
    }


def conditional_u_inventory(relative: str) -> dict[str, object]:
    source = (ROOT / relative).read_text(encoding="utf-8")
    tree = ast.parse(source)
    rows = []
    for node in ast.walk(tree):
        tests: list[ast.AST] = []
        if isinstance(node, (ast.If, ast.IfExp, ast.Assert)):
            tests.append(node.test)
        elif isinstance(node, ast.comprehension):
            tests.extend(node.ifs)
        for test in tests:
            verbatim = node_verbatim(source, test)
            if re.search(r"\bU\b|U_TO_V|V_TO_U", verbatim):
                rows.append({
                    "line": getattr(test, "lineno", node.lineno),
                    "verbatim": verbatim,
                })
    return {
        "path": relative,
        "conditional_count": len(rows),
        "conditionals": sorted(rows, key=lambda row: int(row["line"])),
    }


def function_source(path: str, name: str) -> str | None:
    source = (ROOT / path).read_text(encoding="utf-8")
    tree = ast.parse(source)
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name == name:
                return node_verbatim(source, node)
    source_name = name + "_SOURCE"
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name)
                and target.id == source_name
                for target in node.targets
            )
            and isinstance(node.value, ast.Call)
            and isinstance(node.value.func, ast.Attribute)
            and node.value.func.attr == "strip"
            and isinstance(node.value.func.value, ast.Constant)
            and isinstance(node.value.func.value.value, str)
        ):
            embedded = node.value.func.value.value
            embedded_tree = ast.parse(embedded)
            for definition in embedded_tree.body:
                if (
                    isinstance(
                        definition, (ast.FunctionDef, ast.AsyncFunctionDef)
                    )
                    and definition.name == name
                ):
                    return ast.unparse(definition)
    return None


def content_inventory_search() -> dict[str, object]:
    """Search all scripts, then AST-read only the content-search matches."""
    matched: list[str] = []
    function_hits: list[tuple[str, str]] = []
    function_tests: dict[tuple[str, str], dict[str, object]] = {}
    conditional_hits: list[tuple[str, int, str]] = []
    potential_conditional_closers: list[dict[str, object]] = []
    q_refuse_paths: list[str] = []
    relevant_rollback_paths: list[str] = []
    current = str(Path(__file__).resolve().relative_to(ROOT))

    for path in sorted((ROOT / "scripts").glob("*.py")):
        relative = str(path.relative_to(ROOT))
        text = path.read_text(encoding="utf-8")
        if not SCAN_PATTERN.search(text):
            continue
        matched.append(relative)
        tree = ast.parse(text)
        for node in tree.body:
            if (
                isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                and SCAN_PATTERN.search(node.name)
            ):
                function_hits.append((relative, node.name))
                snippet = node_verbatim(text, node)
                function_tests[(relative, node.name)] = {
                    "closes_prefix6_syndrome": False,
                    "line": node.lineno,
                    "name": node.name,
                    "path": relative,
                    "reason": (
                        "no literal Cycle745 Q_refuse+U input edge"
                        if not (
                            "Q_refuse" in snippet
                            and bool(re.search(r"""["']U["']""", snippet))
                        )
                        else "same-rail signature requires explicit review"
                    ),
                    "same_rail_signature": (
                        "Q_refuse" in snippet
                        and bool(re.search(r"""["']U["']""", snippet))
                    ),
                    "snippet_sha256": sha256(
                        snippet.encode("utf-8")
                    ).hexdigest(),
                    "supplies_rollback": bool(
                        "Q_refuse" in snippet
                        and ROLLBACK_PATTERN.search(snippet)
                    ),
                }
        for node in ast.walk(tree):
            tests: list[ast.AST] = []
            if isinstance(node, (ast.If, ast.IfExp, ast.Assert)):
                tests.append(node.test)
            elif isinstance(node, ast.comprehension):
                tests.extend(node.ifs)
            for test in tests:
                snippet = node_verbatim(text, test)
                if not SCAN_PATTERN.search(snippet):
                    continue
                row = (
                    relative,
                    getattr(test, "lineno", getattr(node, "lineno", 0)),
                    sha256(snippet.encode("utf-8")).hexdigest(),
                )
                conditional_hits.append(row)
                same_rail = (
                    "Q_refuse" in snippet
                    and bool(re.search(r"""["']U["']""", snippet))
                )
                rollback = (
                    "Q_refuse" in snippet
                    and bool(ROLLBACK_PATTERN.search(snippet))
                )
                if same_rail or rollback:
                    potential_conditional_closers.append({
                        "line": row[1],
                        "path": relative,
                        "same_rail_signature": same_rail,
                        "supplies_rollback": rollback,
                        "verbatim": snippet,
                    })
        if "Q_refuse" in text:
            q_refuse_paths.append(relative)
            if (
                relative not in BLOCKLIST_TEXT_PATHS
                and relative != current
                and ROLLBACK_PATTERN.search(text)
            ):
                relevant_rollback_paths.append(relative)

    focus_functions = {
        "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py":
            ("local_refusal_primitive",),
        "scripts/frontier_cycle717_interbank_allocator_handoff_2026_07_26.py":
            ("refusal_and_token_domain_certificate",),
        "scripts/frontier_cycle724_local_token_row_enforcement_2026_07_28.py":
            ("local_or_compute", "refusing_controlled_macro"),
        "scripts/frontier_cycle730_charge_row_enforcement_2026_07_28.py":
            ("local_or_compute", "lifted_refusing_macro"),
        "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py":
            ("local_or_compute", "comparison_compute_word"),
        "scripts/frontier_cycle743_law_flag_derived_2026_07_28.py":
            ("LAW_PREDICATE",),
        "scripts/frontier_cycle747_admiss_verdict_binding_2026_07_28.py":
            ("ADMISS_PREDICATE",),
        "scripts/frontier_cycle754_composed_four_flag_acceptance_2026_07_28.py":
            ("four_flags", "composed_admit"),
    }
    focus_presence: dict[str, dict[str, object]] = {}
    for path, names in focus_functions.items():
        snippets = {
            name: function_source(path, name)
            for name in names
        }
        focus_presence[path] = {
            "functions_found": sorted(
                name for name, snippet in snippets.items()
                if snippet is not None
            ),
            "functions_missing": sorted(
                name for name, snippet in snippets.items()
                if snippet is None
            ),
            "mentions_Cycle745_Q_refuse": any(
                snippet is not None
                and "Q_refuse" in snippet
                and re.search(r"""["']U["']""", snippet)
                for snippet in snippets.values()
            ),
            "mentions_rollback": any(
                snippet is not None and bool(ROLLBACK_PATTERN.search(snippet))
                for snippet in snippets.values()
            ),
            "snippet_sha256": digest(snippets),
        }
        for name, snippet in snippets.items():
            if snippet is None or (path, name) in function_tests:
                continue
            function_tests[(path, name)] = {
                "closes_prefix6_syndrome": False,
                "line": None,
                "name": name,
                "path": path,
                "reason": "typed focus surface has no Cycle745 Q_refuse+U edge",
                "same_rail_signature": (
                    "Q_refuse" in snippet
                    and bool(re.search(r"""["']U["']""", snippet))
                ),
                "snippet_sha256": sha256(
                    snippet.encode("utf-8")
                ).hexdigest(),
                "supplies_rollback": bool(
                    "Q_refuse" in snippet
                    and ROLLBACK_PATTERN.search(snippet)
                ),
            }

    candidate_tests = [
        row
        for (path, _name), row in sorted(function_tests.items())
        if path != current and path != BLOCKLIST_TEXT_PATHS[1]
    ]
    candidate_conditional_hits = [
        row for row in conditional_hits
        if row[0] != current and row[0] != BLOCKLIST_TEXT_PATHS[1]
    ]
    possible_function_closers = [
        row for row in candidate_tests
        if row["same_rail_signature"] or row["supplies_rollback"]
    ]

    return {
        "candidate_function_surface_count": len(candidate_tests),
        "candidate_function_surface_tests": candidate_tests,
        "candidate_conditional_surface_count":
            len(candidate_conditional_hits),
        "candidate_conditional_surfaces_sha256":
            digest(sorted(candidate_conditional_hits)),
        "conditional_hit_count": len(conditional_hits),
        "conditional_hits_sha256": digest(sorted(conditional_hits)),
        "focus_presence": focus_presence,
        "function_hit_count": len(function_hits),
        "function_hits_sha256": digest(function_hits),
        "matched_path_count": len(matched),
        "matched_paths_sha256": digest(matched),
        "q_refuse_paths": q_refuse_paths,
        "q_refuse_paths_sha256": digest(q_refuse_paths),
        "relevant_q_refuse_rollback_paths": relevant_rollback_paths,
        "possible_conditional_closers": potential_conditional_closers,
        "possible_function_closers": possible_function_closers,
    }


def inventory_candidates(
    C719: Any,
    search: dict[str, object],
) -> list[dict[str, object]]:
    local = C719.local_refusal_primitive()
    common = {
        "prefix6_observed_persistent": "(D,1,1)",
        "rollback_test": "no state-restoration branch in candidate AST",
    }
    return [
        {
            **common,
            "candidate": "Cycle745 refuse_locked/dirty gate controls + output_tag",
            "actual_key": "Q rails and U/L controls at their literal word positions",
            "counterfactual_alias_detects": True,
            "detects_prefix6_in_landed_execution": False,
            "detects_prefix7_in_landed_execution": True,
            "reason": (
                "the reverse prefix stops immediately after cascade_unlift; "
                "the dirty-route gates have already passed and Q_refuse is zero"
            ),
            "supplies_rollback": False,
        },
        {
            **common,
            "candidate": "Cycle719 local_refusal_primitive",
            "actual_key": "controller B or work at one Q station",
            "counterfactual_alias_detects": True,
            "detects_prefix6_in_landed_execution": False,
            "local_truth_certificate": {
                key: local[key] for key in (
                    "clean_syndrome_rows",
                    "invalid_live_token_rows_refused",
                    "truth_failures",
                    "route_failures",
                )
            },
            "reason": (
                "the landed primitive has no input edge from Cycle745 U/L; "
                "identifying U with controller B/work would add wiring"
            ),
            "supplies_rollback": False,
        },
        {
            **common,
            "candidate": "Cycle717 refusal_and_token_domain_certificate",
            "actual_key": "BINDER/ACTUAL/ADMISS/LAW plus controller token domain",
            "counterfactual_alias_detects": False,
            "detects_prefix6_in_landed_execution": False,
            "reason": "exact state-identity refusal has no Cycle745 rail input",
            "supplies_rollback": False,
        },
        {
            **common,
            "candidate": "Cycle724 refusing_controlled_macro",
            "actual_key": (
                "controller station B/work and neighboring A/B token rows"
            ),
            "counterfactual_alias_detects": True,
            "detects_prefix6_in_landed_execution": False,
            "reason": (
                "pre-action controller-row guard; no Cycle745 U/L input and "
                "no post-action restoration"
            ),
            "supplies_rollback": False,
        },
        {
            **common,
            "candidate": "Cycle730 lifted_refusing_macro",
            "actual_key": "Cycle724 rows plus local charge mismatch",
            "counterfactual_alias_detects": True,
            "detects_prefix6_in_landed_execution": False,
            "reason": "typed to controller/charge rows, not Cycle745 U/L",
            "supplies_rollback": False,
        },
        {
            **common,
            "candidate": "Cycle731 count-certified refusal latch",
            "actual_key": "global A-token count mismatch plus Cycle730 rows",
            "counterfactual_alias_detects": True,
            "detects_prefix6_in_landed_execution": False,
            "reason": "count/charge/controller inputs contain no lock-rail edge",
            "supplies_rollback": False,
        },
        {
            **common,
            "candidate": "Cycle743 LAW_PREDICATE",
            "actual_key": "charge/count/parity event-state flags",
            "counterfactual_alias_detects": False,
            "detects_prefix6_in_landed_execution": False,
            "reason": "admission law flag has no Cycle745 rail input",
            "supplies_rollback": False,
        },
        {
            **common,
            "candidate": "Cycle747 ADMISS_PREDICATE",
            "actual_key": "Cycle332 verdict tuple",
            "counterfactual_alias_detects": False,
            "detects_prefix6_in_landed_execution": False,
            "reason": "verdict adapter has no Cycle745 rail input",
            "supplies_rollback": False,
        },
        {
            **common,
            "candidate": "Cycle754 composed four-flag admission",
            "actual_key": "LAW/ADMISS/BINDER/ACTUAL flags",
            "counterfactual_alias_detects": False,
            "detects_prefix6_in_landed_execution": False,
            "reason": "downstream admission refusal does not restore a lock cell",
            "supplies_rollback": False,
        },
    ]


def primary_guard_provenance_audit() -> dict[str, object]:
    path = ROOT / BLOCKLIST_TEXT_PATHS[1]
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    guard_functions = {
        "build_rail_guard",
        "tensor_guard_request",
        "apply_word_to_guard_cells",
        "direct_x_guard_cells",
    }
    function_nodes = {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name in guard_functions
    }
    dotted_calls: list[str] = []
    refused_expressions: list[dict[str, object]] = []
    for name, function in sorted(function_nodes.items()):
        for node in ast.walk(function):
            if isinstance(node, ast.Call):
                dotted_calls.append(ast.unparse(node.func))
            if isinstance(node, ast.Assign) and "refused" in assignment_names(node):
                refused_expressions.append({
                    "function": name,
                    "line": node.lineno,
                    "verbatim": node_verbatim(source, node),
                })
            if isinstance(node, ast.Dict):
                for key, value in zip(node.keys, node.values):
                    if (
                        isinstance(key, ast.Constant)
                        and key.value == "refused"
                    ):
                        refused_expressions.append({
                            "function": name,
                            "line": value.lineno,
                            "verbatim": node_verbatim(source, value),
                        })

    construction = node_verbatim(source, function_nodes["build_rail_guard"])
    tensor = node_verbatim(source, function_nodes["tensor_guard_request"])
    landed_calls_present = all(
        token in construction + tensor
        for token in (
            "C745.apply_word",
            "C745.packet",
            "C745.WRITE_WORD",
            "C745.persistent",
            "C745.output_tag",
        )
    )
    invented_refusal_gate = any(
        isinstance(node, ast.Call)
        and ast.unparse(node.func).endswith("Gate")
        and node.args
        and isinstance(node.args[0], ast.Constant)
        and isinstance(node.args[0].value, str)
        and "refus" in node.args[0].value.lower()
        for name, function in function_nodes.items()
        if name != "direct_x_guard_cells"
        for node in ast.walk(function)
    )
    approved_refusal_leaf_names = {
        "REFUSED",
        "after_cells",
        "all",
        "and",
        "bool",
        "cells",
        "events",
        "exact",
        "for",
        "guard",
        "in",
        "refused",
        "syndrome",
        "tag",
        "tags",
    }
    observed_refusal_leaf_names = sorted({
        token
        for row in refused_expressions
        for token in re.findall(
            r"\b[A-Za-z_][A-Za-z0-9_]*\b", str(row["verbatim"])
        )
        if token not in {"False", "True"}
    })
    unapproved_refusal_leaf_names = sorted(
        set(observed_refusal_leaf_names) - approved_refusal_leaf_names
    )
    return {
        "dotted_calls_sha256": digest(sorted(dotted_calls)),
        "functions_found": sorted(function_nodes),
        "guard_uses_C719_condition": any(
            "C719." in node_verbatim(source, function)
            for function in function_nodes.values()
        ),
        "invented_refusal_gate": invented_refusal_gate,
        "landed_C745_calls_present": landed_calls_present,
        "observed_refusal_leaf_names": observed_refusal_leaf_names,
        "ok": (
            set(function_nodes) == guard_functions
            and landed_calls_present
            and not invented_refusal_gate
            and not unapproved_refusal_leaf_names
            and bool(refused_expressions)
        ),
        "refused_expressions": refused_expressions,
        "unapproved_refusal_leaf_names": unapproved_refusal_leaf_names,
    }


def self_blocklist_firewall() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    literal: tuple[str, ...] | None = None
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name)
                and target.id == "AUDIT_INPUT_PATHS"
                for target in node.targets
            )
        ):
            literal = ast.literal_eval(node.value)
    imported = []
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and ast.unparse(node.func) == "importlib.import_module"
            and node.args
            and isinstance(node.args[0], ast.Constant)
        ):
            imported.append(str(node.args[0].value))
    expected_modules = [
        Path(path).stem for path in AUDIT_INPUT_PATHS
    ]
    forbidden_modules = {
        Path(path).stem for path in BLOCKLIST_TEXT_PATHS
    }
    protected = {"C745", "K719", "C719"}
    mutations = []
    for node in ast.walk(tree):
        targets: list[ast.AST] = []
        if isinstance(node, ast.Assign):
            targets.extend(node.targets)
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
            targets.append(node.target)
        elif isinstance(node, ast.Delete):
            targets.extend(node.targets)
        for target in targets:
            cursor = target
            while isinstance(cursor, (ast.Attribute, ast.Subscript)):
                cursor = cursor.value
            if (
                isinstance(target, (ast.Attribute, ast.Subscript))
                and isinstance(cursor, ast.Name)
                and cursor.id in protected
            ):
                mutations.append(f"{type(node).__name__}@{node.lineno}")
    return {
        "blocklisted_imports": sorted(forbidden_modules & set(imported)),
        "imported_modules": imported,
        "literal_AUDIT_INPUT_PATHS": literal,
        "mutation_syntax_violations": mutations,
        "ok": (
            literal == AUDIT_INPUT_PATHS
            and imported == expected_modules
            and not forbidden_modules.intersection(imported)
            and not mutations
        ),
    }


def diagnosis_recount(
    C745: Any,
    pristine: tuple[Persistent, ...],
    content: bytes,
) -> dict[str, object]:
    complement = bytes(byte ^ 0xFF for byte in content)
    offered_bits = bytes_to_bits(complement)
    prefix6_states = []
    prefix7_states = []
    trace_one = []
    for cell_index, (storage, offered) in enumerate(
        zip(pristine, offered_bits)
    ):
        state = C745.packet(storage, offered)
        local_trace = []
        for station, gate in enumerate(C745.REVERSE_WRITE_WORD, 1):
            before = state
            state = C745.apply_gate(state, gate)
            local_trace.append({
                "changes": [
                    f"{rail}:{before[index]}->{state[index]}"
                    for index, rail in enumerate(C745.RAILS)
                    if before[index] != state[index]
                ],
                "gate": gate.name,
                "persistent": C745.persistent(state),
                "prefix": station,
                "q_refuse": state[C745.RAIL_INDEX["Q_refuse"]],
                "tag": C745.output_tag(state),
            })
            if station == 6:
                prefix6_states.append(state)
            if station == 7:
                prefix7_states.append(state)
        if cell_index == 0:
            trace_one = local_trace

    prefix6_dirty = sum(
        C745.persistent(state)[1:] == (1, 1)
        for state in prefix6_states
    )
    prefix6_syndromes = sum(
        state[C745.RAIL_INDEX["Q_refuse"]] == 1
        and C745.output_tag(state) == "REFUSED"
        for state in prefix6_states
    )
    prefix7_dirty = sum(
        C745.persistent(state)[1:] == (1, 1)
        for state in prefix7_states
    )
    prefix7_syndromes = sum(
        state[C745.RAIL_INDEX["Q_refuse"]] == 1
        for state in prefix7_states
    )
    prefix7_restored = sum(
        C745.persistent(state) == before
        for state, before in zip(prefix7_states, pristine)
    )
    return {
        "exact": (
            len(pristine) == 744
            and prefix6_dirty == 744
            and prefix6_syndromes == 0
            and prefix7_dirty == 744
            and prefix7_syndromes == 744
            and prefix7_restored == 0
        ),
        "prefix6": {
            "dirty_U_L_11": prefix6_dirty,
            "landed_Q_refuse_syndromes": prefix6_syndromes,
            "payload_cells": len(pristine),
        },
        "prefix7": {
            "dirty_U_L_11": prefix7_dirty,
            "payload_cells": len(pristine),
            "q_refuse_receipts": prefix7_syndromes,
            "restored_cells": prefix7_restored,
        },
        "trace_one_cell": trace_one,
    }


def controller_controls(
    C745: Any,
    C719: Any,
    forward: dict[str, object],
) -> dict[str, object]:
    branches = {
        (source & 4095).bit_length() - 1: source
        for source in origin_zero_branches(C719)
    }
    rows = []
    for mode in sorted(branches):
        full = C719.controller_full_input(branches[mode])
        engagement_steps = []
        data_write_steps = []
        for step in range(C719.CONTROLLER_STATIONS):
            before_data = int(C719.controller_register_rows(full)["data"])
            full = C719.apply_fast_int(full, C719.CONTROLLER_H_FAST)
            after_data = int(C719.controller_register_rows(full)["data"])
            if before_data != after_data:
                data_write_steps.append(step)
            if decoded_rows(C719, after_data):
                engagement_steps.append(step)
        rows.append({
            "data_write_steps": data_write_steps,
            "engagement_steps": engagement_steps,
            "mode": mode,
        })

    content = forward["content"]
    if not isinstance(content, bytes):
        raise TypeError("invalid content")
    _fresh, fresh = first_write_payload(C745, content)
    cert_b, _ = C745.certificate_b()
    cert_c, _ = C745.certificate_c()
    cert_d, _ = C745.certificate_d()
    no_write = [row for row in rows if row["mode"] in (0, 2, 3, 4, 5)]
    mode6 = next(row for row in rows if row["mode"] == 6)
    return {
        "Cycle745_first_write_certificate": cert_b,
        "Cycle745_induction_certificate": cert_d,
        "Cycle745_refusal_certificate": cert_c,
        "engagement_point": forward["engagement"]["orbit_step"],
        "fresh_write_succeeds": fresh["accepted"],
        "lawful_mode6_first_decoded_step": min(mode6["engagement_steps"]),
        "mode1_absent_from_origin_zero_support": 1 not in branches,
        "mode_rows": rows,
        "modes_0_2_3_4_5_untouched": all(
            not row["engagement_steps"] and not row["data_write_steps"]
            for row in no_write
        ),
        "observed_origin_zero_modes": sorted(branches),
    }


def projected_stdout_size(
    data_lines: list[str],
    certificate_lines: list[str],
    report: dict[str, object],
) -> int:
    final = canonical_json(report)
    return sum(
        len((line + "\n").encode("utf-8"))
        for line in (*data_lines, *certificate_lines, final)
    )


def main() -> int:
    started = perf_counter()
    all_anchor_paths = (*AUDIT_INPUT_PATHS, *BLOCKLIST_TEXT_PATHS)
    before_snapshot = file_snapshot(all_anchor_paths)
    firewall = self_blocklist_firewall()
    C745, K719, C719 = import_landed()

    forward = forward_mode6(C745, C719)
    content = forward["content"]
    pristine = forward["persistent"]
    if not isinstance(content, bytes) or not isinstance(pristine, tuple):
        raise TypeError("invalid mode-6 result")

    baseline_first, candidates_first = baseline_battery(
        C745, K719, C719, forward
    )
    baseline_second, candidates_second = baseline_battery(
        C745, K719, C719, forward
    )
    guard = build_guard(C745, pristine)
    shared_first = shared_guard_battery(
        C745, guard, candidates_first, content
    )
    shared_second = shared_guard_battery(
        C745, guard, candidates_second, content
    )
    extensions_first = extension_battery(C745, guard)
    extensions_second = extension_battery(C745, guard)
    diagnosis = diagnosis_recount(C745, pristine, content)

    c745_inventory = cycle745_ast_inventory()
    search = content_inventory_search()
    candidates = inventory_candidates(C719, search)
    u_conditions = [
        conditional_u_inventory(AUDIT_INPUT_PATHS[1]),
        conditional_u_inventory(AUDIT_INPUT_PATHS[2]),
    ]
    provenance = primary_guard_provenance_audit()
    controls = controller_controls(C745, C719, forward)
    after_snapshot = file_snapshot(all_anchor_paths)

    holes_closed = sum(
        bool(row["detects_prefix6_in_landed_execution"])
        + bool(row["supplies_rollback"])
        for row in candidates
    )
    unclassified_rollback = list(
        search["relevant_q_refuse_rollback_paths"]
    )
    inventory_exhausted = (
        all(
            not row["functions_missing"]
            for row in search["focus_presence"].values()
        )
        and not unclassified_rollback
        and not search["possible_conditional_closers"]
        and not search["possible_function_closers"]
        and len(candidates) == 9
    )
    candidate_conditions_tested = (
        1
        + int(search["candidate_function_surface_count"])
        + int(search["candidate_conditional_surface_count"])
    )
    if holes_closed:
        scientific_outcome = "REFUTED: GUARD_FROM_LANDED_LAW"
        guard_requires_new_law = False
    else:
        scientific_outcome = "CONFIRMED: GUARD_REQUIRES_NEW_LAW"
        guard_requires_new_law = True

    anchors_ok = (
        before_snapshot == after_snapshot
        and all(
            before_snapshot[path]["sha256"] == EXPECTED_SHA256[path]
            for path in all_anchor_paths
        )
    )
    baseline_ok = (
        baseline_first == baseline_second
        and baseline_first["manifest_exact"]
        and baseline_first["attack_count"] == 26
        and baseline_first["refused_count"] == 5
        and baseline_first["surviving_unrefused_mutations"]
        == ["partial_inverse_prefix_6", "partial_inverse_prefix_7"]
    )
    shared_ok = (
        shared_first == shared_second
        and shared_first["manifest_exact"]
        and shared_first["attack_count"] == 50
        and shared_first["refused_count"] == 38
    )
    extensions_deterministic = extensions_first == extensions_second
    controls_ok = (
        controls["fresh_write_succeeds"]
        and controls["modes_0_2_3_4_5_untouched"]
        and controls["mode1_absent_from_origin_zero_support"]
        and controls["engagement_point"] == 125
        and controls["lawful_mode6_first_decoded_step"] == 125
        and controls["Cycle745_first_write_certificate"]
        and controls["Cycle745_refusal_certificate"]
        and controls["Cycle745_induction_certificate"]
    )

    certificate_1 = (
        inventory_exhausted
        and holes_closed == 0
        and guard_requires_new_law
        and len(c745_inventory["refusal_gate_calls"]) == 3
    )
    certificate_2 = (
        baseline_ok
        and shared_ok
        and extensions_deterministic
        and extensions_first["guard_cells_targeted_per_attack"] == 2232
        and extensions_first["attack_count"] > 0
    )
    certificate_3 = bool(diagnosis["exact"])
    certificate_4 = bool(
        provenance["ok"]
        and not provenance["invented_refusal_gate"]
    )

    data_lines = [
        "INDEPENDENT_BLOCKLIST "
        + canonical_json({
            "executed": False,
            "imported": False,
            "paths": BLOCKLIST_TEXT_PATHS,
            "use": "text_AST_and_sha_only",
        }),
        "SHA_ANCHORS " + canonical_json({
            path: before_snapshot[path]["sha256"]
            for path in all_anchor_paths
        }),
        "C745_AST_REFUSAL_INVENTORY " + canonical_json(c745_inventory),
        "C719_U_CONDITIONAL_INVENTORY " + canonical_json(u_conditions),
        "CONTENT_SEARCH_INVENTORY " + canonical_json(search),
    ]
    data_lines.extend(
        "INVENTORY_CANDIDATE " + canonical_json(row)
        for row in candidates
    )
    data_lines.extend([
        (
            f"INVENTORY_HUNT candidates_tested={candidate_conditions_tested} "
            f"focus_families={len(candidates)} "
            f"holes_closed={holes_closed} "
            f"unclassified_rollback_hits={len(unclassified_rollback)}"
        ),
        scientific_outcome
        + f" refused_attacks={shared_first['refused_count']}"
        + f"/{shared_first['attack_count']}",
        "UNGUARDED_RECOUNT " + canonical_json({
            "attack_count": baseline_first["attack_count"],
            "refused_count": baseline_first["refused_count"],
            "surviving_unrefused_mutations":
                baseline_first["surviving_unrefused_mutations"],
        }),
        "GUARDED_SHARED_RECOUNT " + canonical_json({
            "attack_count": shared_first["attack_count"],
            "mutating_survivors": shared_first["mutating_survivors"],
            "refused_count": shared_first["refused_count"],
            "survivors": shared_first["survivors"],
        }),
        "EXTENDED_BATTERY_TOTAL " + canonical_json({
            "attack_count": extensions_first["attack_count"],
            "guard_cells_targeted_per_attack":
                extensions_first["guard_cells_targeted_per_attack"],
            "mutating_survivor_count":
                extensions_first["mutating_survivor_count"],
            "refused_count": extensions_first["refused_count"],
        }),
        "NEW_HOLES_LOUD " + canonical_json(
            extensions_first["mutating_survivors"]
        ),
        "DIAGNOSIS_RECOUNT " + canonical_json(diagnosis),
        "PRIMARY_GUARD_PROVENANCE " + canonical_json(provenance),
        "CONTROLS " + canonical_json(controls),
    ])

    runtime_sec = perf_counter() - started
    certificates = {
        "1": certificate_1,
        "2": certificate_2,
        "3": certificate_3,
        "4": certificate_4,
        "5": False,
    }
    labels = {
        "1": "THE_LANDED_INVENTORY_HUNT",
        "2": "BATTERY_RECOUNT_AND_EXTENSION",
        "3": "DIAGNOSIS_RECOUNT",
        "4": "PRIMARY_GUARD_PROVENANCE_AUDIT",
        "5": "CONTROLS_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT",
    }
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "battery_extension": {
            "attacks": extensions_first["attack_count"],
            "mutating_survivors":
                extensions_first["mutating_survivor_count"],
            "refused": extensions_first["refused_count"],
        },
        "battery_guarded_shared": (
            f"{shared_first['refused_count']}/{shared_first['attack_count']}"
        ),
        "battery_unguarded": (
            f"{baseline_first['refused_count']}/{baseline_first['attack_count']}"
        ),
        "certificates": certificates,
        "determinism": (
            baseline_first == baseline_second
            and shared_first == shared_second
            and extensions_deterministic
        ),
        "guard_requires_new_law": guard_requires_new_law,
        "inventory_candidates_tested": candidate_conditions_tested,
        "inventory_focus_families": len(candidates),
        "inventory_holes_closed": holes_closed,
        "outcome": scientific_outcome,
        "permanence_witness_established": False,
        "runtime_sec": runtime_sec,
        "stdout_bytes": 0,
    }
    for _iteration in range(8):
        certificate_5 = bool(
            anchors_ok
            and firewall["ok"]
            and C719.K is K719
            and controls_ok
            and report["determinism"]
            and runtime_sec < AUDIT_TIMEOUT_SEC
            and int(report["stdout_bytes"]) < 150_000
        )
        certificates["5"] = certificate_5
        report["certificates"] = certificates
        certificate_lines = [
            ("PASS" if certificates[key] else "FAIL")
            + f" CERTIFICATE_{key}_{labels[key]}"
            for key in ("1", "2", "3", "4", "5")
        ]
        size = projected_stdout_size(data_lines, certificate_lines, report)
        if size == report["stdout_bytes"]:
            break
        report["stdout_bytes"] = size

    certificates["5"] = bool(
        anchors_ok
        and firewall["ok"]
        and C719.K is K719
        and controls_ok
        and report["determinism"]
        and runtime_sec < AUDIT_TIMEOUT_SEC
        and int(report["stdout_bytes"]) < 150_000
    )
    report["certificates"] = certificates
    certificate_lines = [
        ("PASS" if certificates[key] else "FAIL")
        + f" CERTIFICATE_{key}_{labels[key]}"
        for key in ("1", "2", "3", "4", "5")
    ]
    final_size = projected_stdout_size(data_lines, certificate_lines, report)
    if final_size != report["stdout_bytes"]:
        report["stdout_bytes"] = final_size

    for line in data_lines:
        print(line)
    for line in certificate_lines:
        print(line)
    print(canonical_json(report))
    return 0 if all(certificates.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
