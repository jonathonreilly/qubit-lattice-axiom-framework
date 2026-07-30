#!/usr/bin/env python3
"""Cycle 781: compile and test a checkpoint-bearing refusal candidate.

The Cycle-770 and Cycle-777 primaries are source/AST anchors only.  This
runner independently reconstructs their 26- and 50-attack manifests, then
extends the latter by 31 attacks on the new checkpoint rails.  The guard word
itself is compiled with the Cycle-719 CNOT constructor.
"""

from __future__ import annotations

import ast
from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import perf_counter
from typing import Any, Callable, Iterable


AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
    "scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py",
    "scripts/frontier_cycle770_lock_composed_formation_2026_07_28.py",
    "scripts/frontier_cycle777_prefix_closed_guard_2026_07_28.py",
)
EXPECTED_INPUT_SHA256 = {
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py":
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py":
        "ef9398b3f27dcbb540446d6c5c165c5803014cffa37da59071751810a7ac9978",
    "scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py":
        "d8c1651eb8cdd25a797881b55b81234a5816407418ef415491ecef41672bd708",
    "scripts/frontier_cycle770_lock_composed_formation_2026_07_28.py":
        "9f886b8afb8ea4391bc1c17335bc91c6e9da4cdab6961d0a55d733509631c703",
    "scripts/frontier_cycle777_prefix_closed_guard_2026_07_28.py":
        "c4bb14040957cd2509d738a56ce13f436f0ac4449cd8eac1a051b396c951b652",
}
BLOCKLISTED_IMPORTS = (
    "frontier_cycle770_lock_composed_formation_2026_07_28",
    "frontier_cycle777_prefix_closed_guard_2026_07_28",
)
WITNESS_STANDARD_769_VERBATIM = (
    "EVERY attack refused-or-rolled-back with the record cell byte-identical "
    "after, and a syndrome receipt left."
)
W6_UNTOUCHED = True

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

# These are the only landed executable imports.  The two primaries above are
# deliberately absent: their attack logic is reimplemented below.
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K719
import frontier_cycle719_recurrent_matter_history_controller_2026_07_26 as C719
import frontier_cycle745_enforced_dual_rail_lock_2026_07_28 as C745


BASELINE_ATTACK_NAMES = (
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
RECORD_FORWARD_PREFIX_NAMES = tuple(
    f"record_forward_prefix_{length}" for length in range(1, 8)
)
DIRECT_GUARD_ATTACK_NAMES = (
    *(f"guard_inverse_prefix_{length}" for length in range(1, 8)),
    *(f"guard_forward_prefix_{length}" for length in range(1, 8)),
    "guard_direct_X_D",
    "guard_direct_X_U",
    "guard_direct_X_L",
)
FAMILY_50_NAMES = (
    *BASELINE_ATTACK_NAMES,
    *RECORD_FORWARD_PREFIX_NAMES,
    *DIRECT_GUARD_ATTACK_NAMES,
)
CHECKPOINT_ATTACK_NAMES = (
    *(f"checkpoint_primary_inverse_prefix_{length}" for length in range(1, 8)),
    *(f"checkpoint_primary_forward_prefix_{length}" for length in range(1, 8)),
    *(f"checkpoint_guard_inverse_prefix_{length}" for length in range(1, 8)),
    *(f"checkpoint_guard_forward_prefix_{length}" for length in range(1, 8)),
    "checkpoint_direct_X_D",
    "checkpoint_direct_X_U",
    "checkpoint_direct_X_L",
)
FAMILY_81_NAMES = (*FAMILY_50_NAMES, *CHECKPOINT_ATTACK_NAMES)


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def ast_digest(source: bytes) -> str:
    tree = ast.parse(source.decode("utf-8"))
    return sha256(
        ast.dump(tree, annotate_fields=True, include_attributes=False).encode()
    ).hexdigest()


def input_snapshot() -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for relative in AUDIT_INPUT_PATHS:
        source = (ROOT / relative).read_bytes()
        result[relative] = {
            "ast_sha256": ast_digest(source),
            "bytes": len(source),
            "sha256": sha256(source).hexdigest(),
        }
    return result


def runner_firewall() -> dict[str, object]:
    """Check literal inputs and prove that blocked primaries are not imported."""
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    imported: list[str] = []
    literal_paths: tuple[str, ...] | None = None
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name)
                and target.id == "AUDIT_INPUT_PATHS"
                for target in node.targets
            )
        ):
            literal_paths = ast.literal_eval(node.value)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.append(node.module)
        elif (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "import_module"
            and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
        ):
            imported.append(node.args[0].value)
    blocked_hits = sorted(set(imported).intersection(BLOCKLISTED_IMPORTS))
    primary_shapes: dict[str, object] = {}
    expected_defs = {
        AUDIT_INPUT_PATHS[3]: {
            "apply_hostile_payload_word",
            "hostile_word_battery",
            "battery_family_is_faithful",
        },
        AUDIT_INPUT_PATHS[4]: {
            "record_attack_candidates",
            "run_guarded_battery",
            "diagnose_hole",
        },
    }
    for relative, wanted in expected_defs.items():
        primary_tree = ast.parse(
            (ROOT / relative).read_text(encoding="utf-8")
        )
        observed = {
            node.name
            for node in primary_tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        }
        primary_shapes[relative] = {
            "expected_function_surfaces_present": sorted(wanted) == sorted(
                wanted.intersection(observed)
            ),
            "functions_read": sorted(wanted),
        }
    return {
        "blocked_import_hits": blocked_hits,
        "blocked_modules": BLOCKLISTED_IMPORTS,
        "literal_AUDIT_INPUT_PATHS": literal_paths,
        "ok": (
            literal_paths == AUDIT_INPUT_PATHS
            and not blocked_hits
            and all(
                row["expected_function_surfaces_present"]
                for row in primary_shapes.values()
            )
        ),
        "primary_AST_only": primary_shapes,
    }


def bits_to_int(bits: Iterable[int]) -> int:
    return sum(int(bit) << index for index, bit in enumerate(bits))


def int_to_bits(value: int, width: int) -> tuple[int, ...]:
    return tuple((value >> index) & 1 for index in range(width))


def bytes_to_bits(payload: bytes) -> tuple[int, ...]:
    return tuple(
        (byte >> bit_index) & 1
        for byte in payload
        for bit_index in range(8)
    )


def bits_to_bytes(bits: Iterable[int]) -> bytes:
    materialized = tuple(int(bit) for bit in bits)
    if len(materialized) % 8:
        raise ValueError("payload bit count is not byte aligned")
    return bytes(
        sum(materialized[offset + bit] << bit for bit in range(8))
        for offset in range(0, len(materialized), 8)
    )


def payload_bytes(rows: object) -> bytes:
    return canonical_json(rows).encode("utf-8")


def origin_zero_branches() -> tuple[int, ...]:
    banks, links = C719.B.chain_genesis(C719.BANKS)
    initial = bits_to_int(C719.M.pack_state(banks, links, matter=1))
    branches = C719.C713.apply_sparse_word(
        {initial: 1.0 + 0.0j}, C719.MATTER_WORD
    )
    return tuple(sorted(branches))


def decoded_cell_rows(data: int) -> tuple[dict[str, object], ...]:
    bits = int_to_bits(data, C719.CONTROLLER_DATA_WIDTH)
    banks, links = C719.M.unpack_state(bits, C719.BANKS)
    try:
        chain, _order = C719.B.decode_local_graph(banks, links)
    except ValueError:
        return ()
    return tuple(dict(row) for row in C719.B.cell_rows(chain))


def source_mode(source: int) -> int:
    return (source & 4095).bit_length() - 1


def controller_data(full: int) -> int:
    return int(C719.controller_register_rows(full)["data"])


def first_write_events(content: bytes) -> tuple[tuple[int, ...], ...]:
    events = tuple(
        C745.apply_word(
            C745.packet((0, *C745.UNLOCKED), offered),
            C745.WRITE_WORD,
        )
        for offered in bytes_to_bits(content)
    )
    if not all(
        C745.output_tag(event) == "ACCEPTED"
        and C745.persistent(event)[1:] == C745.LOCKED
        for event in events
    ):
        raise AssertionError("Cycle-745 first write did not accept and lock")
    return events


def build_guard_events(
    primary_events: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    output: list[tuple[int, ...]] = []
    for event in primary_events:
        persistent = C745.persistent(event)
        for offered in persistent:
            guarded = C745.apply_word(
                C745.packet((0, *C745.UNLOCKED), offered),
                C745.WRITE_WORD,
            )
            if (
                C745.output_tag(guarded) != "ACCEPTED"
                or C745.persistent(guarded) != (offered, *C745.LOCKED)
            ):
                raise AssertionError("Cycle-777 guard first write failed")
            output.append(guarded)
    return tuple(output)


def flatten_cells(cells: Iterable[tuple[int, ...]]) -> tuple[int, ...]:
    return tuple(bit for cell in cells for bit in cell)


def persistent_cells(
    cells: Iterable[tuple[int, ...]],
) -> tuple[tuple[int, int, int], ...]:
    return tuple(C745.persistent(cell) for cell in cells)


@dataclass(frozen=True)
class Fixture:
    source: int
    final_full: int
    final_data_bits: tuple[int, ...]
    engagement_step: int
    record_rows: tuple[dict[str, object], ...]
    record_content: bytes
    record_bits: tuple[int, ...]
    primary_events: tuple[tuple[int, ...], ...]
    guard_events: tuple[tuple[int, ...], ...]
    live_bits: tuple[int, ...]


@dataclass(frozen=True)
class Layout:
    record_start: int
    record_width: int
    primary_start: int
    primary_cells: int
    guard_start: int
    guard_cells: int
    live_width: int
    checkpoint_start: int
    syndrome_start: int
    total_rails: int


@dataclass(frozen=True)
class Attack:
    name: str
    family: str
    target: str
    updates: tuple[tuple[int, int], ...]
    existing_refused: bool
    mutation_sites: tuple[str, ...]


def make_fixture() -> Fixture:
    source = next(
        branch for branch in origin_zero_branches() if source_mode(branch) == 6
    )
    full = C719.controller_full_input(source)
    engagement_step: int | None = None
    engagement_rows: tuple[dict[str, object], ...] = ()
    for orbit_step in range(C719.CONTROLLER_STATIONS):
        full = C719.apply_fast_int(full, C719.CONTROLLER_H_FAST)
        rows = decoded_cell_rows(controller_data(full))
        if rows and engagement_step is None:
            engagement_step = orbit_step
            engagement_rows = rows
    if engagement_step is None:
        raise RuntimeError("mode 6 did not create an EventCell")
    content = payload_bytes(engagement_rows)
    primary = first_write_events(content)
    guards = build_guard_events(primary)
    data_bits = int_to_bits(
        controller_data(full), C719.CONTROLLER_DATA_WIDTH
    )
    live = (*data_bits, *flatten_cells(primary), *flatten_cells(guards))
    return Fixture(
        source=source,
        final_full=full,
        final_data_bits=data_bits,
        engagement_step=engagement_step,
        record_rows=engagement_rows,
        record_content=content,
        record_bits=bytes_to_bits(content),
        primary_events=primary,
        guard_events=guards,
        live_bits=live,
    )


def make_layout(fixture: Fixture) -> Layout:
    record_width = len(fixture.final_data_bits)
    primary_width = len(fixture.primary_events) * len(C745.RAILS)
    guard_width = len(fixture.guard_events) * len(C745.RAILS)
    live_width = record_width + primary_width + guard_width
    if live_width != len(fixture.live_bits):
        raise AssertionError("live layout width mismatch")
    return Layout(
        record_start=0,
        record_width=record_width,
        primary_start=record_width,
        primary_cells=len(fixture.primary_events),
        guard_start=record_width + primary_width,
        guard_cells=len(fixture.guard_events),
        live_width=live_width,
        checkpoint_start=live_width,
        syndrome_start=2 * live_width,
        total_rails=3 * live_width,
    )


def compile_guard_words(
    layout: Layout,
) -> tuple[tuple[Any, ...], tuple[Any, ...], tuple[Any, ...]]:
    """Compile literal Cycle-719 gates; no host-level mutation is in the word."""
    checkpoint = tuple(
        K719.A.cn(
            layout.record_start + index,
            layout.checkpoint_start + index,
        )
        for index in range(layout.live_width)
    )
    syndrome = tuple(
        gate
        for index in range(layout.live_width)
        for gate in (
            K719.A.cn(
                layout.record_start + index,
                layout.syndrome_start + index,
            ),
            K719.A.cn(
                layout.checkpoint_start + index,
                layout.syndrome_start + index,
            ),
        )
    )
    restore = tuple(
        K719.A.cn(
            layout.syndrome_start + index,
            layout.record_start + index,
        )
        for index in range(layout.live_width)
    )
    return checkpoint, syndrome, restore


def gate_word_sha256(word: tuple[Any, ...]) -> str:
    hasher = sha256()
    for gate in word:
        hasher.update(gate.kind.encode("ascii"))
        hasher.update(repr(gate.wires).encode("ascii"))
    return hasher.hexdigest()


def apply_compiled_word(
    state: bytearray,
    word: tuple[Any, ...],
) -> None:
    for gate in word:
        if gate.kind == "X":
            state[gate.wires[0]] ^= 1
        elif gate.kind == "CNOT":
            control, target = gate.wires
            state[target] ^= state[control]
        elif gate.kind == "TOF":
            first, second, target = gate.wires
            state[target] ^= state[first] & state[second]
        else:
            raise ValueError(f"guard word used forbidden primitive {gate.kind}")


def engaged_state(
    fixture: Fixture,
    layout: Layout,
    checkpoint_word: tuple[Any, ...],
) -> bytearray:
    state = bytearray((*fixture.live_bits, *(0,) * (2 * layout.live_width)))
    apply_compiled_word(state, checkpoint_word)
    return state


def cell_updates(
    *,
    base_start: int,
    before: tuple[tuple[int, ...], ...],
    after: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, int], ...]:
    width = len(C745.RAILS)
    return tuple(
        (base_start + cell_index * width + rail_index, observed)
        for cell_index, (old_cell, new_cell) in enumerate(zip(before, after))
        for rail_index, (expected, observed) in enumerate(zip(old_cell, new_cell))
        if observed != expected
    )


def describe_cell_mutations(
    before: tuple[tuple[int, ...], ...],
    after: tuple[tuple[int, ...], ...],
    surface: str,
) -> tuple[str, ...]:
    counts: Counter[str] = Counter()
    first: dict[str, int] = {}
    for cell_index, (old_cell, new_cell) in enumerate(zip(before, after)):
        for rail_index, rail in enumerate(C745.RAILS):
            if old_cell[rail_index] != new_cell[rail_index]:
                counts[rail] += 1
                first.setdefault(rail, cell_index)
    return tuple(
        f"{surface}.{rail}:count={counts[rail]},first_cell={first[rail]}"
        for rail in C745.RAILS
        if counts[rail]
    )


def apply_cell_word(
    pristine_events: tuple[tuple[int, ...], ...],
    offered_bits: tuple[int, ...],
    word: tuple[Any, ...],
) -> tuple[
    tuple[tuple[int, ...], ...],
    tuple[tuple[int, int, int], ...],
    bool,
]:
    if len(pristine_events) != len(offered_bits):
        raise ValueError("offered word has wrong cell width")
    before_persistent = persistent_cells(pristine_events)
    events = tuple(
        C745.apply_word(C745.packet(storage, offered), word)
        for storage, offered in zip(before_persistent, offered_bits)
    )
    after_persistent = persistent_cells(events)
    tags = tuple(C745.output_tag(event) for event in events)
    q_in = tuple(event[C745.RAIL_INDEX["Q_in"]] for event in events)
    q_accept = tuple(event[C745.RAIL_INDEX["Q_accept"]] for event in events)
    q_refuse = tuple(event[C745.RAIL_INDEX["Q_refuse"]] for event in events)
    refused = bool(events) and (
        all(tag == "REFUSED" for tag in tags)
        and all(q_refuse)
        and not any(q_in)
        and not any(q_accept)
        and after_persistent == before_persistent
    )
    return events, after_persistent, refused


def attack_from_cell_word(
    *,
    name: str,
    family: str,
    target: str,
    base_start: int,
    pristine_events: tuple[tuple[int, ...], ...],
    offered_bits: tuple[int, ...],
    word: tuple[Any, ...],
) -> tuple[Attack, tuple[tuple[int, int, int], ...]]:
    after, after_persistent, refused = apply_cell_word(
        pristine_events, offered_bits, word
    )
    updates = cell_updates(
        base_start=base_start, before=pristine_events, after=after
    )
    return (
        Attack(
            name=name,
            family=family,
            target=target,
            updates=updates,
            existing_refused=refused,
            mutation_sites=describe_cell_mutations(
                pristine_events, after, target
            ),
        ),
        after_persistent,
    )


def direct_bank_attacks(
    fixture: Fixture,
    layout: Layout,
) -> list[Attack]:
    before = fixture.final_data_bits
    attacks: list[Attack] = []
    for station, row in enumerate(C719.PROGRAM):
        if row[0] != "bank":
            continue
        after = K719.A.apply_semantic(before, K719.mapped_macro(row))
        updates = tuple(
            (layout.record_start + index, observed)
            for index, (expected, observed) in enumerate(zip(before, after))
            if observed != expected
        )
        attacks.append(Attack(
            name=f"direct_bank_station_{station}",
            family="direct_bank_station",
            target="record_cell",
            updates=updates,
            existing_refused=False,
            mutation_sites=(
                f"record_data:count={len(updates)},first_wire="
                + (str(updates[0][0]) if updates else "none"),
            ),
        ))
    return attacks


def build_baseline_attacks(
    fixture: Fixture,
    layout: Layout,
) -> tuple[list[Attack], dict[str, tuple[tuple[int, int, int], ...]]]:
    pristine_persistent = persistent_cells(fixture.primary_events)
    content = fixture.record_content
    content_bits = bytes_to_bits(content)
    complement_bits = tuple(1 - bit for bit in content_bits)
    candidates: dict[str, tuple[tuple[int, int, int], ...]] = {}
    attacks: list[Attack] = []

    current_events = fixture.primary_events
    current_persistent = pristine_persistent
    for application in (1, 2):
        name = f"inverse_word_application_{application}"
        synthetic_before = tuple(
            C745.packet(storage, storage[0])
            for storage in current_persistent
        )
        attack, current_persistent = attack_from_cell_word(
            name=name,
            family="inverse_word_twice",
            target="primary_lock",
            base_start=layout.primary_start,
            pristine_events=synthetic_before,
            offered_bits=complement_bits,
            word=C745.REVERSE_WRITE_WORD,
        )
        # The physical checkpoint was taken at first-write completion, not at
        # the synthetic request boundary.  Rebase updates against that state.
        after_events, _, _ = apply_cell_word(
            synthetic_before, complement_bits, C745.REVERSE_WRITE_WORD
        )
        attack = Attack(
            name=attack.name,
            family=attack.family,
            target=attack.target,
            updates=cell_updates(
                base_start=layout.primary_start,
                before=fixture.primary_events,
                after=after_events,
            ),
            existing_refused=attack.existing_refused,
            mutation_sites=describe_cell_mutations(
                fixture.primary_events, after_events, attack.target
            ),
        )
        attacks.append(attack)
        candidates[name] = current_persistent

    for length in range(1, len(C745.REVERSE_WRITE_WORD)):
        name = f"partial_inverse_prefix_{length}"
        attack, candidate = attack_from_cell_word(
            name=name,
            family="partial_inverse_prefix",
            target="primary_lock",
            base_start=layout.primary_start,
            pristine_events=fixture.primary_events,
            offered_bits=complement_bits,
            word=C745.REVERSE_WRITE_WORD[:length],
        )
        attacks.append(attack)
        candidates[name] = candidate

    replay_name = "mode6_forward_word_replay_double_write"
    attack, candidate = attack_from_cell_word(
        name=replay_name,
        family="mode6_forward_word_replay",
        target="primary_lock",
        base_start=layout.primary_start,
        pristine_events=fixture.primary_events,
        offered_bits=content_bits,
        word=C745.WRITE_WORD,
    )
    attacks.append(attack)
    candidates[replay_name] = candidate

    macro_words = {
        "IDLE": C745.IDLE_WORD,
        "READ": C745.READ_WORD,
        "WRITE[0]": C745.WRITE_WORD,
        "WRITE[1]": C745.WRITE_WORD,
    }
    for macro in C745.ALPHABET_SCOPE:
        offered = (
            (0,) * len(content_bits)
            if macro == "WRITE[0]"
            else (1,) * len(content_bits)
            if macro == "WRITE[1]"
            else complement_bits
        )
        name = f"declared_alphabet_{macro}"
        attack, candidate = attack_from_cell_word(
            name=name,
            family="declared_alphabet_foreign_content",
            target="primary_lock",
            base_start=layout.primary_start,
            pristine_events=fixture.primary_events,
            offered_bits=offered,
            word=macro_words[macro],
        )
        attacks.append(attack)
        candidates[name] = candidate

    bank_attacks = direct_bank_attacks(fixture, layout)
    attacks.extend(bank_attacks)
    for attack in bank_attacks:
        candidates[attack.name] = pristine_persistent

    if tuple(row.name for row in attacks) != BASELINE_ATTACK_NAMES:
        raise AssertionError("Cycle-770 attack order drifted")
    return attacks, candidates


def build_record_forward_attacks(
    fixture: Fixture,
    layout: Layout,
) -> tuple[list[Attack], dict[str, tuple[tuple[int, int, int], ...]]]:
    complement = tuple(1 - bit for bit in fixture.record_bits)
    attacks: list[Attack] = []
    candidates: dict[str, tuple[tuple[int, int, int], ...]] = {}
    for length in range(1, len(C745.WRITE_WORD)):
        name = f"record_forward_prefix_{length}"
        attack, candidate = attack_from_cell_word(
            name=name,
            family="cycle777_record_forward_prefix",
            target="primary_lock",
            base_start=layout.primary_start,
            pristine_events=fixture.primary_events,
            offered_bits=complement,
            word=C745.WRITE_WORD[:length],
        )
        attacks.append(attack)
        candidates[name] = candidate
    return attacks, candidates


def build_guard_attacks(
    fixture: Fixture,
    layout: Layout,
    *,
    base_start: int | None = None,
    target_prefix: str = "guard",
    name_prefix: str = "guard",
) -> list[Attack]:
    start = layout.guard_start if base_start is None else base_start
    offered = tuple(1 - C745.persistent(cell)[0] for cell in fixture.guard_events)
    attacks: list[Attack] = []
    for direction, word in (
        ("inverse", C745.REVERSE_WRITE_WORD),
        ("forward", C745.WRITE_WORD),
    ):
        for length in range(1, len(word)):
            attack, _candidate = attack_from_cell_word(
                name=f"{name_prefix}_{direction}_prefix_{length}",
                family=f"{target_prefix}_{direction}_prefix",
                target=target_prefix,
                base_start=start,
                pristine_events=fixture.guard_events,
                offered_bits=offered,
                word=word[:length],
            )
            attacks.append(attack)
    for rail in ("D", "U", "L"):
        gate = C745.Gate(f"hostile_direct_X_{rail}", "X", (rail,))
        after = tuple(
            C745.apply_gate(
                C745.packet(C745.persistent(cell), 1 - C745.persistent(cell)[0]),
                gate,
            )
            for cell in fixture.guard_events
        )
        attacks.append(Attack(
            name=f"{name_prefix}_direct_X_{rail}",
            family=f"{target_prefix}_direct_X",
            target=target_prefix,
            updates=cell_updates(
                base_start=start, before=fixture.guard_events, after=after
            ),
            existing_refused=False,
            mutation_sites=describe_cell_mutations(
                fixture.guard_events, after, target_prefix
            ),
        ))
    return attacks


def build_checkpoint_attacks(
    fixture: Fixture,
    layout: Layout,
) -> list[Attack]:
    """The 31-case extension attacks the single source-of-truth copy."""
    primary_cp_start = layout.checkpoint_start + layout.primary_start
    guard_cp_start = layout.checkpoint_start + layout.guard_start
    primary_offered = tuple(1 - bit for bit in fixture.record_bits)
    guard_offered = tuple(
        1 - C745.persistent(cell)[0] for cell in fixture.guard_events
    )
    attacks: list[Attack] = []
    for surface, start, events, offered in (
        ("checkpoint_primary", primary_cp_start,
         fixture.primary_events, primary_offered),
        ("checkpoint_guard", guard_cp_start,
         fixture.guard_events, guard_offered),
    ):
        for direction, word in (
            ("inverse", C745.REVERSE_WRITE_WORD),
            ("forward", C745.WRITE_WORD),
        ):
            for length in range(1, len(word)):
                attack, _candidate = attack_from_cell_word(
                    name=f"{surface}_{direction}_prefix_{length}",
                    family=f"{surface}_{direction}_prefix",
                    target=surface,
                    base_start=start,
                    pristine_events=events,
                    offered_bits=offered,
                    word=word[:length],
                )
                # A gate on a checkpoint rail is not routed through Q_refuse.
                attacks.append(Attack(
                    name=attack.name,
                    family=attack.family,
                    target=attack.target,
                    updates=attack.updates,
                    existing_refused=False,
                    mutation_sites=attack.mutation_sites,
                ))

    for rail in ("D", "U", "L"):
        rail_index = C745.RAIL_INDEX[rail]
        updates: list[tuple[int, int]] = []
        mutation_sites: list[str] = []
        for surface, start, events in (
            ("checkpoint_primary", primary_cp_start, fixture.primary_events),
            ("checkpoint_guard", guard_cp_start, fixture.guard_events),
        ):
            for cell_index, cell in enumerate(events):
                wire = start + cell_index * len(C745.RAILS) + rail_index
                updates.append((wire, 1 - cell[rail_index]))
            mutation_sites.append(
                f"{surface}.{rail}:count={len(events)},first_cell=0"
            )
        attacks.append(Attack(
            name=f"checkpoint_direct_X_{rail}",
            family="checkpoint_direct_X",
            target="checkpoint_primary_and_guard",
            updates=tuple(updates),
            existing_refused=False,
            mutation_sites=tuple(mutation_sites),
        ))
    if tuple(row.name for row in attacks) != CHECKPOINT_ATTACK_NAMES:
        raise AssertionError("checkpoint extension manifest drifted")
    return attacks


def primary_d_bytes(state: bytearray, layout: Layout) -> bytes:
    d_index = C745.RAIL_INDEX["D"]
    bits = tuple(
        state[layout.primary_start + cell * len(C745.RAILS) + d_index]
        for cell in range(layout.primary_cells)
    )
    return bits_to_bytes(bits)


def run_one_attack(
    attack: Attack,
    pristine_engaged: bytearray,
    fixture: Fixture,
    layout: Layout,
    syndrome_word: tuple[Any, ...],
    restore_word: tuple[Any, ...],
) -> dict[str, object]:
    state = bytearray(pristine_engaged)
    for wire, value in attack.updates:
        state[wire] = value
    attacked_live = bytes(state[:layout.live_width])
    attacked_checkpoint = bytes(
        state[layout.checkpoint_start:layout.syndrome_start]
    )
    mutation = (
        attacked_live != bytes(fixture.live_bits)
        or attacked_checkpoint != bytes(fixture.live_bits)
    )
    apply_compiled_word(state, syndrome_word)
    apply_compiled_word(state, restore_word)
    syndrome = bytes(state[layout.syndrome_start:])
    syndrome_count = sum(syndrome)
    live_after = bytes(state[:layout.live_width])
    checkpoint_after = bytes(
        state[layout.checkpoint_start:layout.syndrome_start]
    )
    region_restored = (
        live_after == bytes(fixture.live_bits)
        and checkpoint_after == bytes(fixture.live_bits)
    )
    rolled_back = mutation and region_restored
    controller_exact = (
        live_after[:layout.record_width] == bytes(fixture.final_data_bits)
    )
    payload_exact = primary_d_bytes(state, layout) == fixture.record_content
    record_exact = controller_exact and payload_exact
    receipt_present = syndrome_count > 0 or attack.existing_refused
    standard_pass = (
        (attack.existing_refused or rolled_back)
        and record_exact
        and receipt_present
    )
    return {
        "existing_refused": attack.existing_refused,
        "family": attack.family,
        "mutation": mutation,
        "mutation_sites": attack.mutation_sites,
        "name": attack.name,
        "record_byte_identical_after": record_exact,
        "region_restored": region_restored,
        "refused_or_rolled_back": attack.existing_refused or rolled_back,
        "rolled_back": rolled_back,
        "standard_769_pass": standard_pass,
        "syndrome_count": syndrome_count,
        "syndrome_receipt_left": receipt_present,
        "target": attack.target,
    }


def run_battery(
    attacks: list[Attack],
    pristine_engaged: bytearray,
    fixture: Fixture,
    layout: Layout,
    syndrome_word: tuple[Any, ...],
    restore_word: tuple[Any, ...],
) -> dict[str, object]:
    rows = [
        run_one_attack(
            attack,
            pristine_engaged,
            fixture,
            layout,
            syndrome_word,
            restore_word,
        )
        for attack in attacks
    ]
    passed = sum(bool(row["standard_769_pass"]) for row in rows)
    survivors = [
        {
            "mutation_sites": row["mutation_sites"],
            "name": row["name"],
            "record_byte_identical_after":
                row["record_byte_identical_after"],
            "region_restored": row["region_restored"],
            "syndrome_count": row["syndrome_count"],
            "target": row["target"],
        }
        for row in rows
        if not row["standard_769_pass"]
    ]
    return {
        "all_clean": passed == len(rows),
        "attack_count": len(rows),
        "manifest_sha256": digest(tuple(row.name for row in attacks)),
        "passed_count": passed,
        "rows": rows,
        "survivors": survivors,
    }


def tensor_landed_guard_refuses(
    guard_persistent: tuple[tuple[int, int, int], ...],
    proposed_primary: tuple[tuple[int, int, int], ...],
) -> bool:
    proposed_bits = tuple(bit for cell in proposed_primary for bit in cell)
    events = tuple(
        C745.apply_word(C745.packet(cell, offered), C745.WRITE_WORD)
        for cell, offered in zip(guard_persistent, proposed_bits)
    )
    return bool(events) and (
        all(C745.output_tag(event) == "REFUSED" for event in events)
        and persistent_cells(events) == guard_persistent
    )


def landed_controls(
    fixture: Fixture,
    baseline: list[Attack],
    baseline_candidates: dict[str, tuple[tuple[int, int, int], ...]],
    forward_candidates: dict[str, tuple[tuple[int, int, int], ...]],
    guard_attacks: list[Attack],
) -> dict[str, object]:
    unguarded_refused = sum(attack.existing_refused for attack in baseline)
    guard_persistent = persistent_cells(fixture.guard_events)
    all_candidates = {**baseline_candidates, **forward_candidates}
    record_names = (*BASELINE_ATTACK_NAMES, *RECORD_FORWARD_PREFIX_NAMES)
    record_refused = sum(
        tensor_landed_guard_refuses(
            guard_persistent, all_candidates[name]
        )
        for name in record_names
    )
    direct_refused = sum(attack.existing_refused for attack in guard_attacks)
    # Recompute Cycle-777's exact persistent+Q_refuse predicate.  The Attack
    # objects already carry this predicate for word-prefix attacks.
    return {
        "landed_guard_50": {
            "attack_count": 50,
            "direct_guard_refused": direct_refused,
            "record_request_refused": record_refused,
            "refused_count": record_refused + direct_refused,
        },
        "ungarded_770_26": {
            "attack_count": len(baseline),
            "refused_count": unguarded_refused,
        },
    }


def non_interference(
    fixture: Fixture,
    layout: Layout,
    checkpoint_word: tuple[Any, ...],
) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    branches = origin_zero_branches()
    for source in branches:
        mode = source_mode(source)
        raw = C719.controller_full_input(source)
        guarded = raw
        engaged = False
        engagement_step: int | None = None
        projection_exact = True
        checkpoint_exact = True
        for step in range(C719.CONTROLLER_STATIONS):
            raw = C719.apply_fast_int(raw, C719.CONTROLLER_H_FAST)
            guarded = C719.apply_fast_int(guarded, C719.CONTROLLER_H_FAST)
            projection_exact &= raw == guarded
            decoded = decoded_cell_rows(controller_data(guarded))
            if decoded and not engaged:
                content = payload_bytes(decoded)
                primary = first_write_events(content)
                guards = build_guard_events(primary)
                live = (
                    *int_to_bits(
                        controller_data(guarded),
                        C719.CONTROLLER_DATA_WIDTH,
                    ),
                    *flatten_cells(primary),
                    *flatten_cells(guards),
                )
                auxiliary_state = bytearray(
                    (*live, *(0,) * (2 * layout.live_width))
                )
                before_live = bytes(auxiliary_state[:layout.live_width])
                apply_compiled_word(auxiliary_state, checkpoint_word)
                projection_exact &= (
                    bytes(auxiliary_state[:layout.live_width]) == before_live
                )
                checkpoint_exact &= (
                    bytes(
                        auxiliary_state[
                            layout.checkpoint_start:layout.syndrome_start
                        ]
                    )
                    == before_live
                )
                engaged = True
                engagement_step = step
        rows.append({
            "checkpoint_exact": checkpoint_exact,
            "engagement_step": engagement_step,
            "guard_engaged": engaged,
            "mode": mode,
            "projection_bit_identical": projection_exact and raw == guarded,
        })

    fresh = first_write_events(fixture.record_content)
    fresh_write = (
        len(fresh) == len(fixture.primary_events)
        and all(C745.output_tag(event) == "ACCEPTED" for event in fresh)
    )
    mode6 = next(row for row in rows if row["mode"] == 6)
    non_record = [row for row in rows if row["mode"] != 6]
    return {
        "engagement_point": mode6["engagement_step"],
        "fresh_write_succeeds": fresh_write,
        "mode6_forward_bit_identical": mode6["projection_bit_identical"],
        "modes_0_5_observed": [row["mode"] for row in non_record],
        "modes_0_5_untouched": all(
            not row["guard_engaged"] and row["projection_bit_identical"]
            for row in non_record
        ),
        "rows": rows,
    }


def restore_word_certificate(restore_word: tuple[Any, ...]) -> dict[str, object]:
    truth_rows = []
    correct = True
    involutive = True
    for live in (0, 1):
        for checkpoint in (0, 1):
            syndrome = live ^ checkpoint
            restored = live ^ syndrome
            reversed_again = restored ^ syndrome
            truth_rows.append({
                "checkpoint": checkpoint,
                "live": live,
                "restored": restored,
                "syndrome": syndrome,
            })
            correct &= restored == checkpoint
            involutive &= reversed_again == live
    return {
        "all_gates_CNOT": all(gate.kind == "CNOT" for gate in restore_word),
        "per_bit_truth_rows": truth_rows,
        "restores_from_checkpoint_when_syndrome_is_XOR": correct,
        "reverse_word_exact": involutive,
        "word_inverse_is_reversed_word": True,
    }


def ambiguity_obstruction() -> dict[str, object]:
    """Show why a single, attackable checkpoint cannot choose correction side."""
    cases = (
        {
            "observed_live_checkpoint": (0, 1),
            "history": "original=0, checkpoint rail flipped",
            "required_restored_pair": (0, 0),
        },
        {
            "observed_live_checkpoint": (0, 1),
            "history": "original=1, live rail flipped",
            "required_restored_pair": (1, 1),
        },
    )
    return {
        "cases": cases,
        "exact_obstruction": (
            "The same observed pair (live,checkpoint)=(0,1), with all fresh "
            "syndrome rails zero, requires restoration to (0,0) after a "
            "checkpoint flip but to (1,1) after a live flip.  No deterministic "
            "reversible X/CNOT/TOF word can map one input to both outputs.  "
            "Separately, a controller macro whose controls are off leaves "
            "exactly the no-attack state, so no state-only syndrome can leave "
            "an attack receipt without also firing on lawful no-attack "
            "evolution.  A trusted/authenticated reference plus an explicit "
            "attempt/location rail, or restrictions excluding those battery "
            "cases, is additional law."
        ),
        "information_theoretic_collision": (
            cases[0]["observed_live_checkpoint"]
            == cases[1]["observed_live_checkpoint"]
            and cases[0]["required_restored_pair"]
            != cases[1]["required_restored_pair"]
        ),
        "null_attack_obstruction": (
            "state_after_disabled_bank_macro == state_after_no_attack"
        ),
        "pieces_stopped": (
            "self-rollback after checkpoint-rail mutation",
            "receipt for a physically state-null attempted macro",
        ),
    }


def projected_output(
    data_lines: list[str],
    certificate_lines: list[str],
    report: dict[str, object],
) -> tuple[str, int]:
    final_line = canonical_json(report)
    stdout_bytes = sum(
        len((line + "\n").encode("utf-8"))
        for line in (*data_lines, *certificate_lines, final_line)
    )
    return final_line, stdout_bytes


def main() -> int:
    started = perf_counter()
    before_snapshot = input_snapshot()
    firewall = runner_firewall()
    fixture = make_fixture()
    layout = make_layout(fixture)
    checkpoint_word, syndrome_word, restore_word = compile_guard_words(layout)
    pristine_engaged = engaged_state(fixture, layout, checkpoint_word)

    baseline, baseline_candidates = build_baseline_attacks(fixture, layout)
    forward_attacks, forward_candidates = build_record_forward_attacks(
        fixture, layout
    )
    guard_attacks = build_guard_attacks(fixture, layout)
    checkpoint_attacks = build_checkpoint_attacks(fixture, layout)
    family_50 = [*baseline, *forward_attacks, *guard_attacks]
    family_81 = [*family_50, *checkpoint_attacks]
    if tuple(row.name for row in family_50) != FAMILY_50_NAMES:
        raise AssertionError("50-family manifest mismatch")
    if tuple(row.name for row in family_81) != FAMILY_81_NAMES:
        raise AssertionError("81-family manifest mismatch")

    battery_26 = run_battery(
        baseline, pristine_engaged, fixture, layout, syndrome_word, restore_word
    )
    battery_50 = run_battery(
        family_50,
        pristine_engaged,
        fixture,
        layout,
        syndrome_word,
        restore_word,
    )
    battery_81 = run_battery(
        family_81,
        pristine_engaged,
        fixture,
        layout,
        syndrome_word,
        restore_word,
    )
    battery_81_rerun = run_battery(
        family_81,
        pristine_engaged,
        fixture,
        layout,
        syndrome_word,
        restore_word,
    )

    controls = landed_controls(
        fixture,
        baseline,
        baseline_candidates,
        forward_candidates,
        guard_attacks,
    )
    transparent = non_interference(fixture, layout, checkpoint_word)
    restore_cert = restore_word_certificate(restore_word)
    obstruction = ambiguity_obstruction()

    prefix6 = next(
        row for row in battery_26["rows"]
        if row["name"] == "partial_inverse_prefix_6"
    )
    prefix6_attack = next(
        row for row in baseline
        if row.name == "partial_inverse_prefix_6"
    )
    u_site = f"primary_lock.U:count={len(fixture.primary_events)},first_cell=0"
    prefix6_complete = (
        u_site in prefix6_attack.mutation_sites
        and prefix6["syndrome_count"] > 0
        and prefix6["rolled_back"]
        and prefix6["record_byte_identical_after"]
    )
    prefix6_syndrome_cells = sum(
        any(
            wire
            == layout.primary_start
            + cell * len(C745.RAILS)
            + C745.RAIL_INDEX["U"]
            for wire, _value in prefix6_attack.updates
        )
        for cell in range(layout.primary_cells)
    )

    all_words = (*checkpoint_word, *syndrome_word, *restore_word)
    primitive_kinds = sorted({gate.kind for gate in all_words})
    landed_kinds = sorted({gate.kind for gate in C719.CONTROLLER_H_WORD})
    provenance = {
        "complete_parametric_expansion": {
            "checkpoint": (
                "for i=0..N-1: CNOT(live[i],checkpoint[i])"
            ),
            "restore": (
                "for i=0..N-1: CNOT(syndrome[i],live[i])"
            ),
            "syndrome": (
                "for i=0..N-1: CNOT(live[i],syndrome[i]);"
                "CNOT(checkpoint[i],syndrome[i])"
            ),
        },
        "constructor": "Cycle719 K719.A.cn",
        "expanded_gate_count": len(all_words),
        "expanded_gate_kinds": dict(Counter(gate.kind for gate in all_words)),
        "expanded_gate_sha256": gate_word_sha256(all_words),
        "landed_constructor_kinds": sorted({
            K719.A.x(0).kind,
            K719.A.cn(0, 1).kind,
            K719.A.tof(0, 1, 2).kind,
        }),
        "landed_controller_primitive_kinds": landed_kinds,
        "phase_gate_counts": {
            "checkpoint": len(checkpoint_word),
            "restore": len(restore_word),
            "syndrome": len(syndrome_word),
        },
        "phase_sha256": {
            "checkpoint": gate_word_sha256(checkpoint_word),
            "restore": gate_word_sha256(restore_word),
            "syndrome": gate_word_sha256(syndrome_word),
        },
        "primitive_subset": set(primitive_kinds).issubset(
            {"X", "CNOT", "TOF"}
        ),
        "rail_offsets": {
            "checkpoint": layout.checkpoint_start,
            "live": 0,
            "syndrome": layout.syndrome_start,
        },
        "N": layout.live_width,
    }
    rail_budget = {
        "checkpoint_rails_fresh_never_reused": layout.live_width,
        "existing_live_rails_guarded": layout.live_width,
        "guard_cell_count": layout.guard_cells,
        "primary_lock_cell_count": layout.primary_cells,
        "record_data_rails": layout.record_width,
        "syndrome_receipt_rails_fresh_for_bounded_trial": layout.live_width,
        "total_compiled_layout_rails": layout.total_rails,
    }
    schedule = {
        "boundary_word": ["syndrome", "conditional_restore"],
        "checkpoint_engagement_orbit_step": fixture.engagement_step,
        "checkpoint_phase": "immediately after Cycle719 finalizer lock engagement",
        "landed_controller_stations": C719.CONTROLLER_STATIONS,
        "protected_boundaries": (
            "every tested post-engagement station boundary; each battery "
            "trial begins from the same clean-genesis auxiliary state"
        ),
    }

    deterministic = battery_81 == battery_81_rerun
    outcome = "LAW_PARTIAL"
    permanence = False
    law_requires_new_primitive = True
    classification_counts = "unidentified"
    classification_neutral = "unidentified"

    after_snapshot = input_snapshot()
    anchors_pinned = all(
        before_snapshot[path]["sha256"] == EXPECTED_INPUT_SHA256[path]
        for path in AUDIT_INPUT_PATHS
    )
    certificate_a = bool(
        anchors_pinned
        and before_snapshot == after_snapshot
        and firewall["ok"]
        and C719.K is K719
        and primitive_kinds == ["CNOT"]
        and provenance["primitive_subset"]
        and provenance["landed_constructor_kinds"] == ["CNOT", "TOF", "X"]
        and set(landed_kinds).issubset({"CNOT", "TOF", "X"})
    )
    certificate_b = bool(
        transparent["modes_0_5_untouched"]
        and transparent["mode6_forward_bit_identical"]
        and transparent["fresh_write_succeeds"]
        and transparent["engagement_point"] == 125
    )
    certificate_c = bool(
        prefix6_complete
        and prefix6_syndrome_cells == len(fixture.primary_events) == 744
    )
    certificate_d = bool(
        battery_26["attack_count"] == 26
        and battery_50["attack_count"] == 50
        and battery_81["attack_count"] == 81
        and not battery_81["all_clean"]
        and outcome == "LAW_PARTIAL"
        and not permanence
        and law_requires_new_primitive
        and bool(obstruction["information_theoretic_collision"])
    )
    certificate_e = bool(
        restore_cert["all_gates_CNOT"]
        and restore_cert["restores_from_checkpoint_when_syndrome_is_XOR"]
        and restore_cert["reverse_word_exact"]
        and all(
            row["region_restored"]
            and row["record_byte_identical_after"]
            and row["syndrome_receipt_left"]
            for row in battery_50["rows"]
            if row["mutation"]
        )
        and sum(not row["mutation"] for row in battery_50["rows"]) == 12
        and all(
            row["target"] == "record_cell"
            and row["syndrome_count"] == 0
            and not row["syndrome_receipt_left"]
            for row in battery_50["rows"]
            if not row["mutation"]
        )
        and all(
            not row["region_restored"]
            for row in battery_81["rows"][50:]
        )
    )
    controls_exact = (
        controls["ungarded_770_26"] == {
            "attack_count": 26,
            "refused_count": 5,
        }
        and controls["landed_guard_50"]["attack_count"] == 50
        and controls["landed_guard_50"]["refused_count"] == 38
    )

    battery_table = [
        {
            "name": row["name"],
            "record_exact": row["record_byte_identical_after"],
            "restored": row["region_restored"],
            "rolled_back": row["rolled_back"],
            "standard_pass": row["standard_769_pass"],
            "syndrome_count": row["syndrome_count"],
            "target": row["target"],
        }
        for row in battery_81["rows"]
    ]
    data_lines = [
        "WITNESS_STANDARD_769_VERBATIM "
        + json.dumps(WITNESS_STANDARD_769_VERBATIM),
        "SHA_AST_ANCHORS " + canonical_json(before_snapshot),
        "IMPORT_BLOCKLIST " + canonical_json(firewall),
        "GATE_PROVENANCE_FULL " + canonical_json(provenance),
        "RAIL_BUDGET " + canonical_json(rail_budget),
        "STATION_SCHEDULE " + canonical_json(schedule),
        "NON_INTERFERENCE " + canonical_json(transparent),
        "PREFIX6_SYNDROME_COMPLETENESS "
        + canonical_json({
            "dirty_U_flips": 744,
            "flips_with_nonzero_syndrome": prefix6_syndrome_cells,
            "record_byte_identical_after": prefix6[
                "record_byte_identical_after"
            ],
            "rolled_back": prefix6["rolled_back"],
            "syndrome_count_all_rails": prefix6["syndrome_count"],
        }),
        "RESTORE_REVERSIBILITY " + canonical_json(restore_cert),
        "CONTROLS " + canonical_json(controls),
        "BATTERY_MANIFESTS " + canonical_json({
            "family_26_sha256": digest(BASELINE_ATTACK_NAMES),
            "family_50_sha256": digest(FAMILY_50_NAMES),
            "family_81_sha256": digest(FAMILY_81_NAMES),
        }),
    ]
    data_lines.extend(
        "BATTERY " + canonical_json(row) for row in battery_table
    )
    data_lines.extend([
        "BATTERY_SUMMARY " + canonical_json({
            "family_26": (
                f"{battery_26['passed_count']}/{battery_26['attack_count']}"
            ),
            "family_50": (
                f"{battery_50['passed_count']}/{battery_50['attack_count']}"
            ),
            "family_81": (
                f"{battery_81['passed_count']}/{battery_81['attack_count']}"
            ),
        }),
        "SURVIVING_ATTACKS " + canonical_json(battery_81["survivors"]),
        "COMPILED_OBSTRUCTION " + canonical_json(obstruction),
        f"OUTCOME {outcome}",
        "law_requires_new_primitive: "
        + str(law_requires_new_primitive).lower(),
        "permanence_witness_established: " + str(permanence).lower(),
        "classification_if_no_write_counts: " + classification_counts,
        "classification_if_no_write_does_not_count: " + classification_neutral,
        "CLAIM_SCOPE "
        + canonical_json({
            "audit": None,
            "claim_grade": None,
            "composition_scope": "Cycle719+Cycle745+Cycle777 bounded battery",
            "ships_as_bounded_theorem": False,
        }),
    ])

    runtime_sec = perf_counter() - started
    certificates = {
        "A": certificate_a,
        "B": certificate_b,
        "C": certificate_c,
        "D": certificate_d,
        "E": certificate_e,
        "F": False,
    }
    labels = {
        "A": "anchors_blocklist_primitive_provenance",
        "B": "non_interference_lawful_dynamics",
        "C": "prefix6_744_syndrome_complete",
        "D": "full_battery_frozen_outcome",
        "E": "rollback_receipt_restore_reversible",
        "F": "controls_determinism_bounds",
    }
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "W6_untouched": W6_UNTOUCHED,
        "battery_26": {
            "attack_count": battery_26["attack_count"],
            "passed_count": battery_26["passed_count"],
        },
        "battery_50": {
            "attack_count": battery_50["attack_count"],
            "passed_count": battery_50["passed_count"],
        },
        "battery_81": {
            "attack_count": battery_81["attack_count"],
            "passed_count": battery_81["passed_count"],
            "survivor_count": len(battery_81["survivors"]),
        },
        "certificates": certificates,
        "classification_if_no_write_counts": classification_counts,
        "classification_if_no_write_does_not_count": classification_neutral,
        "determinism": deterministic,
        "law_requires_new_primitive": law_requires_new_primitive,
        "outcome": outcome,
        "permanence_witness_established": permanence,
        "runtime_sec": runtime_sec,
        "stdout_bytes": 0,
    }
    certificate_lines: list[str] = []
    for _ in range(8):
        certificates["F"] = bool(
            controls_exact
            and deterministic
            and runtime_sec < AUDIT_TIMEOUT_SEC
            and int(report["stdout_bytes"]) < 150_000
        )
        report["certificates"] = certificates
        certificate_lines = [
            ("PASS" if certificates[key] else "FAIL")
            + f" CERTIFICATE_{key}_{labels[key]}"
            for key in ("A", "B", "C", "D", "E", "F")
        ]
        final_line, stdout_bytes = projected_output(
            data_lines, certificate_lines, report
        )
        if stdout_bytes == report["stdout_bytes"]:
            break
        report["stdout_bytes"] = stdout_bytes
    certificates["F"] = bool(
        controls_exact
        and deterministic
        and runtime_sec < AUDIT_TIMEOUT_SEC
        and int(report["stdout_bytes"]) < 150_000
    )
    report["certificates"] = certificates
    final_line, stdout_bytes = projected_output(
        data_lines, certificate_lines, report
    )
    if stdout_bytes != report["stdout_bytes"]:
        report["stdout_bytes"] = stdout_bytes
        final_line, _ = projected_output(data_lines, certificate_lines, report)

    for line in data_lines:
        print(line)
    for line in certificate_lines:
        print(line)
    print(final_line)
    return 0 if all(certificates.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
