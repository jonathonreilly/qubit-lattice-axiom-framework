#!/usr/bin/env python3
"""Cycle 781 independent adversarial checker.

The Cycle-770, Cycle-777, and Cycle-781 primaries are text/AST evidence only.
Only the three landed construction modules in AUDIT_INPUT_PATHS are imported.
"""

from __future__ import annotations

import ast
from collections import Counter, deque
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import perf_counter
from typing import Any, Iterable


AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
)
TEXT_ONLY_PRIMARY_PATHS = (
    "scripts/frontier_cycle770_lock_composed_formation_2026_07_28.py",
    "scripts/frontier_cycle777_prefix_closed_guard_2026_07_28.py",
    "scripts/frontier_cycle781_checkpoint_refusal_law_2026_07_28.py",
)
BLOCKLISTED_IMPORTS = (
    "frontier_cycle770_lock_composed_formation_2026_07_28",
    "frontier_cycle777_prefix_closed_guard_2026_07_28",
    "frontier_cycle781_checkpoint_refusal_law_2026_07_28",
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
    "scripts/frontier_cycle781_checkpoint_refusal_law_2026_07_28.py":
        "b1158250dcb1449f6abac4f6bb6a0a90f47511a8a0f587e85483f4b6f3624211",
}
WITNESS_STANDARD_769_VERBATIM = (
    "EVERY attack refused-or-rolled-back with the record cell byte-identical "
    "after, and a syndrome receipt left."
)

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
RECORD_FORWARD_NAMES = tuple(
    f"record_forward_prefix_{length}" for length in range(1, 8)
)
DIRECT_GUARD_NAMES = (
    *(f"guard_inverse_prefix_{length}" for length in range(1, 8)),
    *(f"guard_forward_prefix_{length}" for length in range(1, 8)),
    "guard_direct_X_D",
    "guard_direct_X_U",
    "guard_direct_X_L",
)
FAMILY_50_NAMES = (
    *BASELINE_ATTACK_NAMES,
    *RECORD_FORWARD_NAMES,
    *DIRECT_GUARD_NAMES,
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

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle745_enforced_dual_rail_lock_2026_07_28 as C745
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K719
import frontier_cycle719_recurrent_matter_history_controller_2026_07_26 as C719


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def ast_digest(source: bytes) -> str:
    tree = ast.parse(source.decode("utf-8"))
    dumped = ast.dump(tree, annotate_fields=True, include_attributes=False)
    return sha256(dumped.encode("utf-8")).hexdigest()


def evidence_snapshot() -> dict[str, dict[str, object]]:
    snapshot: dict[str, dict[str, object]] = {}
    for relative in (*AUDIT_INPUT_PATHS, *TEXT_ONLY_PRIMARY_PATHS):
        source = (ROOT / relative).read_bytes()
        snapshot[relative] = {
            "ast_sha256": ast_digest(source),
            "bytes": len(source),
            "sha256": sha256(source).hexdigest(),
        }
    return snapshot


def assignment_literal(tree: ast.Module, name: str) -> object:
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            )
        ):
            return ast.literal_eval(node.value)
    raise KeyError(name)


def imported_modules(tree: ast.Module) -> tuple[str, ...]:
    names: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.append(node.module)
        elif (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "import_module"
            and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
        ):
            names.append(node.args[0].value)
    return tuple(names)


def source_firewall() -> dict[str, object]:
    own_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    imports = imported_modules(own_tree)
    literal_inputs = assignment_literal(own_tree, "AUDIT_INPUT_PATHS")
    frontier_imports = tuple(
        name for name in imports if name.startswith("frontier_cycle")
    )
    expected_frontier = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)
    blocked_hits = tuple(sorted(set(imports).intersection(BLOCKLISTED_IMPORTS)))

    required_surfaces = {
        TEXT_ONLY_PRIMARY_PATHS[0]: {
            "apply_hostile_payload_word",
            "hostile_word_battery",
            "battery_family_is_faithful",
        },
        TEXT_ONLY_PRIMARY_PATHS[1]: {
            "record_attack_candidates",
            "run_guarded_battery",
            "diagnose_hole",
        },
        TEXT_ONLY_PRIMARY_PATHS[2]: {
            "compile_guard_words",
            "run_battery",
            "ambiguity_obstruction",
        },
    }
    primary_shapes: dict[str, object] = {}
    witness_from_primary: object = None
    provenance_phrases = (
        "for i=0..N-1: CNOT(live[i],checkpoint[i])",
        "for i=0..N-1: CNOT(syndrome[i],live[i])",
        "for i=0..N-1: CNOT(live[i],syndrome[i]);"
        "CNOT(checkpoint[i],syndrome[i])",
    )
    provenance_present = False
    for relative, required in required_surfaces.items():
        source = (ROOT / relative).read_text(encoding="utf-8")
        tree = ast.parse(source)
        functions = {
            node.name for node in tree.body if isinstance(node, ast.FunctionDef)
        }
        primary_shapes[relative] = {
            "functions_read": sorted(required),
            "required_surfaces_present": required.issubset(functions),
            "text_AST_only": True,
        }
        if relative == TEXT_ONLY_PRIMARY_PATHS[2]:
            witness_from_primary = assignment_literal(
                tree, "WITNESS_STANDARD_769_VERBATIM"
            )
            constant_strings = {
                node.value
                for node in ast.walk(tree)
                if isinstance(node, ast.Constant)
                and isinstance(node.value, str)
            }
            provenance_present = all(
                phrase in constant_strings for phrase in provenance_phrases
            )

    ok = (
        literal_inputs == AUDIT_INPUT_PATHS
        and frontier_imports == expected_frontier
        and not blocked_hits
        and witness_from_primary == WITNESS_STANDARD_769_VERBATIM
        and provenance_present
        and all(
            bool(row["required_surfaces_present"])
            for row in primary_shapes.values()
        )
    )
    return {
        "blocked_import_hits": blocked_hits,
        "blocked_modules": BLOCKLISTED_IMPORTS,
        "frontier_imports": frontier_imports,
        "literal_AUDIT_INPUT_PATHS": literal_inputs,
        "ok": ok,
        "primary_text_AST_only": primary_shapes,
        "provenance_phrases_present": provenance_present,
        "witness_verbatim_matches_primary": (
            witness_from_primary == WITNESS_STANDARD_769_VERBATIM
        ),
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


def payload_bytes(rows: object) -> bytes:
    return canonical_json(rows).encode("utf-8")


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
        raise AssertionError("landed first-write construction failed")
    return events


def outer_guard_events(
    primary_events: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    result: list[tuple[int, ...]] = []
    for event in primary_events:
        for offered in C745.persistent(event):
            guarded = C745.apply_word(
                C745.packet((0, *C745.UNLOCKED), offered),
                C745.WRITE_WORD,
            )
            if (
                C745.output_tag(guarded) != "ACCEPTED"
                or C745.persistent(guarded) != (offered, *C745.LOCKED)
            ):
                raise AssertionError("landed outer-guard construction failed")
            result.append(guarded)
    return tuple(result)


def flatten(cells: Iterable[tuple[int, ...]]) -> tuple[int, ...]:
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
class LiveLayout:
    record_width: int
    primary_start: int
    primary_cells: int
    guard_start: int
    guard_cells: int
    live_width: int


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
    for step in range(C719.CONTROLLER_STATIONS):
        full = C719.apply_fast_int(full, C719.CONTROLLER_H_FAST)
        rows = decoded_cell_rows(controller_data(full))
        if rows and engagement_step is None:
            engagement_step = step
            engagement_rows = rows
    if engagement_step is None:
        raise RuntimeError("mode 6 did not create an EventCell")
    content = payload_bytes(engagement_rows)
    primary = first_write_events(content)
    outer = outer_guard_events(primary)
    data_bits = int_to_bits(controller_data(full), C719.CONTROLLER_DATA_WIDTH)
    live = (*data_bits, *flatten(primary), *flatten(outer))
    return Fixture(
        source=source,
        final_full=full,
        final_data_bits=data_bits,
        engagement_step=engagement_step,
        record_rows=engagement_rows,
        record_content=content,
        record_bits=bytes_to_bits(content),
        primary_events=primary,
        guard_events=outer,
        live_bits=live,
    )


def make_refresh_boundary_fixtures() -> tuple[tuple[int, Fixture], ...]:
    source = next(
        branch for branch in origin_zero_branches() if source_mode(branch) == 6
    )
    full = C719.controller_full_input(source)
    engagement_step: int | None = None
    engagement_rows: tuple[dict[str, object], ...] = ()
    content = b""
    primary: tuple[tuple[int, ...], ...] = ()
    outer: tuple[tuple[int, ...], ...] = ()
    results: list[tuple[int, Fixture]] = []
    for step in range(C719.CONTROLLER_STATIONS):
        full = C719.apply_fast_int(full, C719.CONTROLLER_H_FAST)
        rows = decoded_cell_rows(controller_data(full))
        if rows and engagement_step is None:
            engagement_step = step
            engagement_rows = rows
            content = payload_bytes(rows)
            primary = first_write_events(content)
            outer = outer_guard_events(primary)
        if engagement_step is not None:
            data_bits = int_to_bits(
                controller_data(full), C719.CONTROLLER_DATA_WIDTH
            )
            results.append((step, Fixture(
                source=source,
                final_full=full,
                final_data_bits=data_bits,
                engagement_step=engagement_step,
                record_rows=engagement_rows,
                record_content=content,
                record_bits=bytes_to_bits(content),
                primary_events=primary,
                guard_events=outer,
                live_bits=(*data_bits, *flatten(primary), *flatten(outer)),
            )))
    return tuple(results)


def make_live_layout(fixture: Fixture) -> LiveLayout:
    primary_start = len(fixture.final_data_bits)
    guard_start = primary_start + len(fixture.primary_events) * len(C745.RAILS)
    live_width = guard_start + len(fixture.guard_events) * len(C745.RAILS)
    if live_width != len(fixture.live_bits):
        raise AssertionError("live layout width mismatch")
    return LiveLayout(
        record_width=len(fixture.final_data_bits),
        primary_start=primary_start,
        primary_cells=len(fixture.primary_events),
        guard_start=guard_start,
        guard_cells=len(fixture.guard_events),
        live_width=live_width,
    )


def cell_updates(
    base_start: int,
    before: tuple[tuple[int, ...], ...],
    after: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, int], ...]:
    width = len(C745.RAILS)
    return tuple(
        (base_start + cell * width + rail, observed)
        for cell, (old_cell, new_cell) in enumerate(zip(before, after))
        for rail, (expected, observed) in enumerate(zip(old_cell, new_cell))
        if observed != expected
    )


def mutation_descriptions(
    surface: str,
    before: tuple[tuple[int, ...], ...],
    after: tuple[tuple[int, ...], ...],
) -> tuple[str, ...]:
    counts: Counter[str] = Counter()
    first: dict[str, int] = {}
    for cell, (old_cell, new_cell) in enumerate(zip(before, after)):
        for rail_index, rail in enumerate(C745.RAILS):
            if old_cell[rail_index] != new_cell[rail_index]:
                counts[rail] += 1
                first.setdefault(rail, cell)
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
        raise ValueError("offered word has wrong width")
    storage_before = persistent_cells(pristine_events)
    events = tuple(
        C745.apply_word(C745.packet(storage, offered), word)
        for storage, offered in zip(storage_before, offered_bits)
    )
    storage_after = persistent_cells(events)
    refused = bool(events) and (
        all(C745.output_tag(event) == "REFUSED" for event in events)
        and all(event[C745.RAIL_INDEX["Q_refuse"]] for event in events)
        and not any(event[C745.RAIL_INDEX["Q_in"]] for event in events)
        and not any(event[C745.RAIL_INDEX["Q_accept"]] for event in events)
        and storage_after == storage_before
    )
    return events, storage_after, refused


def attack_from_cell_word(
    *,
    name: str,
    family: str,
    target: str,
    base_start: int,
    pristine_events: tuple[tuple[int, ...], ...],
    offered_bits: tuple[int, ...],
    word: tuple[Any, ...],
    force_unrefused: bool = False,
) -> tuple[Attack, tuple[tuple[int, int, int], ...]]:
    after, candidate, refused = apply_cell_word(
        pristine_events, offered_bits, word
    )
    return (
        Attack(
            name=name,
            family=family,
            target=target,
            updates=cell_updates(base_start, pristine_events, after),
            existing_refused=False if force_unrefused else refused,
            mutation_sites=mutation_descriptions(
                target, pristine_events, after
            ),
        ),
        candidate,
    )


def direct_bank_attacks(
    fixture: Fixture,
    layout: LiveLayout,
) -> list[Attack]:
    before = fixture.final_data_bits
    attacks: list[Attack] = []
    for station, row in enumerate(C719.PROGRAM):
        if row[0] != "bank":
            continue
        after = K719.A.apply_semantic(before, K719.mapped_macro(row))
        updates = tuple(
            (index, observed)
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
    layout: LiveLayout,
) -> tuple[list[Attack], dict[str, tuple[tuple[int, int, int], ...]]]:
    pristine = persistent_cells(fixture.primary_events)
    content_bits = fixture.record_bits
    complement = tuple(1 - bit for bit in content_bits)
    attacks: list[Attack] = []
    candidates: dict[str, tuple[tuple[int, int, int], ...]] = {}

    current = pristine
    for application in (1, 2):
        name = f"inverse_word_application_{application}"
        synthetic = tuple(
            C745.packet(storage, storage[0]) for storage in current
        )
        after, current, refused = apply_cell_word(
            synthetic, complement, C745.REVERSE_WRITE_WORD
        )
        attacks.append(Attack(
            name=name,
            family="inverse_word_twice",
            target="primary_lock",
            updates=cell_updates(
                layout.primary_start, fixture.primary_events, after
            ),
            existing_refused=refused,
            mutation_sites=mutation_descriptions(
                "primary_lock", fixture.primary_events, after
            ),
        ))
        candidates[name] = current

    for length in range(1, len(C745.REVERSE_WRITE_WORD)):
        name = f"partial_inverse_prefix_{length}"
        attack, candidate = attack_from_cell_word(
            name=name,
            family="partial_inverse_prefix",
            target="primary_lock",
            base_start=layout.primary_start,
            pristine_events=fixture.primary_events,
            offered_bits=complement,
            word=C745.REVERSE_WRITE_WORD[:length],
        )
        attacks.append(attack)
        candidates[name] = candidate

    replay = "mode6_forward_word_replay_double_write"
    attack, candidate = attack_from_cell_word(
        name=replay,
        family="mode6_forward_word_replay",
        target="primary_lock",
        base_start=layout.primary_start,
        pristine_events=fixture.primary_events,
        offered_bits=content_bits,
        word=C745.WRITE_WORD,
    )
    attacks.append(attack)
    candidates[replay] = candidate

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
            else complement
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

    for attack in direct_bank_attacks(fixture, layout):
        attacks.append(attack)
        candidates[attack.name] = pristine
    if tuple(row.name for row in attacks) != BASELINE_ATTACK_NAMES:
        raise AssertionError("independent 26-case manifest drifted")
    return attacks, candidates


def build_record_forward_attacks(
    fixture: Fixture,
    layout: LiveLayout,
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
    layout: LiveLayout,
    *,
    base_start: int | None = None,
    target: str = "guard",
    name_prefix: str = "guard",
    force_unrefused: bool = False,
) -> list[Attack]:
    start = layout.guard_start if base_start is None else base_start
    offered = tuple(
        1 - C745.persistent(cell)[0] for cell in fixture.guard_events
    )
    attacks: list[Attack] = []
    for direction, word in (
        ("inverse", C745.REVERSE_WRITE_WORD),
        ("forward", C745.WRITE_WORD),
    ):
        for length in range(1, len(word)):
            attack, _candidate = attack_from_cell_word(
                name=f"{name_prefix}_{direction}_prefix_{length}",
                family=f"{target}_{direction}_prefix",
                target=target,
                base_start=start,
                pristine_events=fixture.guard_events,
                offered_bits=offered,
                word=word[:length],
                force_unrefused=force_unrefused,
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
            family=f"{target}_direct_X",
            target=target,
            updates=cell_updates(start, fixture.guard_events, after),
            existing_refused=False,
            mutation_sites=mutation_descriptions(
                target, fixture.guard_events, after
            ),
        ))
    return attacks


def build_checkpoint_attacks(
    fixture: Fixture,
    layout: LiveLayout,
) -> list[Attack]:
    checkpoint_start = layout.live_width
    attacks = build_guard_attacks(
        fixture,
        layout,
        base_start=checkpoint_start + layout.primary_start,
        target="checkpoint_primary",
        name_prefix="checkpoint_primary",
        force_unrefused=True,
    )
    attacks.extend(build_guard_attacks(
        fixture,
        layout,
        base_start=checkpoint_start + layout.guard_start,
        target="checkpoint_guard",
        name_prefix="checkpoint_guard",
        force_unrefused=True,
    ))
    # The helper above emits direct-X rows per surface.  Cycle 781 instead
    # preregisters three combined direct-X attacks over both checkpoint
    # surfaces, so replace the six helper rows with those three exact cases.
    attacks = [
        attack for attack in attacks
        if "_direct_X_" not in attack.name
    ]
    for rail in ("D", "U", "L"):
        rail_index = C745.RAIL_INDEX[rail]
        updates: list[tuple[int, int]] = []
        sites: list[str] = []
        for surface, start, events in (
            (
                "checkpoint_primary",
                checkpoint_start + layout.primary_start,
                fixture.primary_events,
            ),
            (
                "checkpoint_guard",
                checkpoint_start + layout.guard_start,
                fixture.guard_events,
            ),
        ):
            for cell_index, cell in enumerate(events):
                wire = start + cell_index * len(C745.RAILS) + rail_index
                updates.append((wire, 1 - cell[rail_index]))
            sites.append(f"{surface}.{rail}:count={len(events)},first_cell=0")
        attacks.append(Attack(
            name=f"checkpoint_direct_X_{rail}",
            family="checkpoint_direct_X",
            target="checkpoint_primary_and_guard",
            updates=tuple(updates),
            existing_refused=False,
            mutation_sites=tuple(sites),
        ))
    if tuple(row.name for row in attacks) != CHECKPOINT_ATTACK_NAMES:
        raise AssertionError("independent checkpoint manifest drifted")
    return attacks


@dataclass(frozen=True)
class GuardProgram:
    name: str
    live_width: int
    copy_starts: tuple[int, ...]
    receipt_ranges: tuple[tuple[int, int], ...]
    total_rails: int
    engage_word: tuple[Any, ...]
    boundary_word: tuple[Any, ...]
    fanout_edges: tuple[tuple[int, int], ...]
    metadata: dict[str, object]


def gate_word_sha256(word: tuple[Any, ...]) -> str:
    hasher = sha256()
    for gate in word:
        hasher.update(gate.kind.encode("ascii"))
        hasher.update(repr(gate.wires).encode("ascii"))
    return hasher.hexdigest()


def apply_compiled_word(state: bytearray, word: tuple[Any, ...]) -> None:
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
            raise ValueError(f"forbidden compiled primitive {gate.kind}")


def compile_single_checkpoint(
    live_width: int,
    *,
    name: str,
    refresh_metadata: dict[str, object] | None = None,
) -> GuardProgram:
    checkpoint = live_width
    syndrome = 2 * live_width
    engage = tuple(
        K719.A.cn(index, checkpoint + index)
        for index in range(live_width)
    )
    boundary = tuple(
        gate
        for index in range(live_width)
        for gate in (
            K719.A.cn(index, syndrome + index),
            K719.A.cn(checkpoint + index, syndrome + index),
            K719.A.cn(syndrome + index, index),
        )
    )
    metadata = {
        "construction": (
            "CNOT(live[i],checkpoint[i]); "
            "CNOT(live[i],syndrome[i]); "
            "CNOT(checkpoint[i],syndrome[i]); "
            "CNOT(syndrome[i],live[i])"
        ),
        "restoration": "live := live XOR (live XOR checkpoint)",
    }
    if refresh_metadata:
        metadata.update(refresh_metadata)
    return GuardProgram(
        name=name,
        live_width=live_width,
        copy_starts=(checkpoint,),
        receipt_ranges=((syndrome, syndrome + live_width),),
        total_rails=3 * live_width,
        engage_word=engage,
        boundary_word=boundary,
        fanout_edges=tuple(
            (index, checkpoint + index) for index in range(live_width)
        ),
        metadata=metadata,
    )


def compile_majority_three(live_width: int) -> GuardProgram:
    copies = (live_width, 2 * live_width, 3 * live_width)
    quartet_starts = (0, *copies)
    pairs = tuple(
        (left, right)
        for left in range(len(quartet_starts))
        for right in range(left + 1, len(quartet_starts))
    )
    pairwise_start = 4 * live_width
    majority_start = pairwise_start + len(pairs) * live_width
    correction_start = majority_start + live_width
    engage = tuple(
        K719.A.cn(index, copy + index)
        for index in range(live_width)
        for copy in copies
    )
    boundary_list: list[Any] = []
    for pair_index, (left, right) in enumerate(pairs):
        output = pairwise_start + pair_index * live_width
        for index in range(live_width):
            boundary_list.append(
                K719.A.cn(quartet_starts[left] + index, output + index)
            )
            boundary_list.append(
                K719.A.cn(quartet_starts[right] + index, output + index)
            )
    first, second, third = copies
    for index in range(live_width):
        majority = majority_start + index
        boundary_list.extend((
            K719.A.tof(first + index, second + index, majority),
            K719.A.tof(first + index, third + index, majority),
            K719.A.tof(second + index, third + index, majority),
        ))
    for target_number, target_start in enumerate(quartet_starts):
        correction = correction_start + target_number * live_width
        for index in range(live_width):
            boundary_list.extend((
                K719.A.cn(target_start + index, correction + index),
                K719.A.cn(majority_start + index, correction + index),
                K719.A.cn(correction + index, target_start + index),
            ))
    total = correction_start + len(quartet_starts) * live_width
    return GuardProgram(
        name="majority3",
        live_width=live_width,
        copy_starts=copies,
        receipt_ranges=tuple(
            (
                pairwise_start + pair_index * live_width,
                pairwise_start + (pair_index + 1) * live_width,
            )
            for pair_index in range(len(pairs))
        ),
        total_rails=total,
        engage_word=engage,
        boundary_word=tuple(boundary_list),
        fanout_edges=tuple(
            (index, copy + index)
            for index in range(live_width)
            for copy in copies
        ),
        metadata={
            "checkpoint_copies": 3,
            "pairwise_syndrome_pairs": tuple(
                (
                    ("live", "copy1", "copy2", "copy3")[left],
                    ("live", "copy1", "copy2", "copy3")[right],
                )
                for left, right in pairs
            ),
            "majority_formula_GF2": "ab XOR ac XOR bc",
            "restoration": "live and all three copies := majority(copy1,copy2,copy3)",
        },
    )


def engaged_state(fixture: Fixture, program: GuardProgram) -> bytearray:
    state = bytearray(program.total_rails)
    state[:program.live_width] = bytes(fixture.live_bits)
    apply_compiled_word(state, program.engage_word)
    return state


def receipt_count(state: bytearray, program: GuardProgram) -> int:
    return sum(
        state[index]
        for start, stop in program.receipt_ranges
        for index in range(start, stop)
    )


def protected_regions(
    state: bytearray,
    program: GuardProgram,
) -> tuple[bytes, ...]:
    width = program.live_width
    return (
        bytes(state[:width]),
        *(bytes(state[start:start + width]) for start in program.copy_starts),
    )


def primary_d_bytes(
    state: bytearray,
    fixture: Fixture,
    layout: LiveLayout,
) -> bytes:
    d_index = C745.RAIL_INDEX["D"]
    bits = tuple(
        state[
            layout.primary_start
            + cell * len(C745.RAILS)
            + d_index
        ]
        for cell in range(layout.primary_cells)
    )
    return bits_to_bytes(bits)


def algebraic_boundary(
    attacked_regions: tuple[bytes, ...],
    program: GuardProgram,
) -> tuple[tuple[bytes, ...], int]:
    if program.name in {"single", "refresh"}:
        live, checkpoint = attacked_regions
        syndrome = bytes(a ^ b for a, b in zip(live, checkpoint))
        return (checkpoint, checkpoint), sum(syndrome)
    if program.name != "majority3":
        raise ValueError(program.name)
    live, first, second, third = attacked_regions
    pairwise_count = sum(
        left_bit ^ right_bit
        for left, right in (
            (live, first),
            (live, second),
            (live, third),
            (first, second),
            (first, third),
            (second, third),
        )
        for left_bit, right_bit in zip(left, right)
    )
    majority = bytes(
        (a & b) ^ (a & c) ^ (b & c)
        for a, b, c in zip(first, second, third)
    )
    return (majority, majority, majority, majority), pairwise_count


def run_attack(
    attack: Attack,
    pristine: bytearray,
    fixture: Fixture,
    layout: LiveLayout,
    program: GuardProgram,
) -> dict[str, object]:
    state = bytearray(pristine)
    for wire, value in attack.updates:
        state[wire] = value
    attacked_regions = protected_regions(state, program)
    clean_regions = (
        bytes(fixture.live_bits),
        *(bytes(fixture.live_bits) for _copy in program.copy_starts),
    )
    mutation = attacked_regions != clean_regions
    predicted_regions, predicted_syndrome_count = algebraic_boundary(
        attacked_regions, program
    )
    apply_compiled_word(state, program.boundary_word)
    observed_regions = protected_regions(state, program)
    observed_syndrome_count = receipt_count(state, program)
    region_restored = observed_regions == clean_regions
    rolled_back = mutation and region_restored
    record_exact = (
        bytes(state[:layout.record_width]) == bytes(fixture.final_data_bits)
        and primary_d_bytes(state, fixture, layout) == fixture.record_content
    )
    receipt = observed_syndrome_count > 0 or attack.existing_refused
    standard_pass = (
        (attack.existing_refused or rolled_back)
        and record_exact
        and receipt
    )
    algebra_agreement = (
        observed_regions == predicted_regions
        and observed_syndrome_count == predicted_syndrome_count
    )
    return {
        "algebra_agreement": algebra_agreement,
        "existing_refused": attack.existing_refused,
        "family": attack.family,
        "mutation": mutation,
        "name": attack.name,
        "record_byte_identical_after": record_exact,
        "region_restored": region_restored,
        "refused_or_rolled_back": attack.existing_refused or rolled_back,
        "rolled_back": rolled_back,
        "standard_769_pass": standard_pass,
        "syndrome_count": observed_syndrome_count,
        "syndrome_receipt_left": receipt,
        "target": attack.target,
    }


def run_battery(
    attacks: list[Attack],
    pristine: bytearray,
    fixture: Fixture,
    layout: LiveLayout,
    program: GuardProgram,
) -> dict[str, object]:
    rows = [
        run_attack(attack, pristine, fixture, layout, program)
        for attack in attacks
    ]
    passed = sum(bool(row["standard_769_pass"]) for row in rows)
    return {
        "all_algebra_agree": all(row["algebra_agreement"] for row in rows),
        "all_clean": passed == len(rows),
        "attack_count": len(rows),
        "manifest_sha256": digest(tuple(attack.name for attack in attacks)),
        "passed_count": passed,
        "rows": rows,
        "survivors": tuple(
            row["name"] for row in rows if not row["standard_769_pass"]
        ),
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
    guard_persistent = persistent_cells(fixture.guard_events)
    candidates = {**baseline_candidates, **forward_candidates}
    record_names = (*BASELINE_ATTACK_NAMES, *RECORD_FORWARD_NAMES)
    record_refused = sum(
        tensor_landed_guard_refuses(guard_persistent, candidates[name])
        for name in record_names
    )
    direct_refused = sum(attack.existing_refused for attack in guard_attacks)
    return {
        "landed_guard_38_of_50": {
            "attack_count": 50,
            "direct_guard_refused": direct_refused,
            "record_request_refused": record_refused,
            "refused_count": record_refused + direct_refused,
        },
        "unguarded_5_of_26": {
            "attack_count": len(baseline),
            "refused_count": sum(
                attack.existing_refused for attack in baseline
            ),
        },
    }


def detection_recount(
    fixture: Fixture,
    layout: LiveLayout,
    baseline: list[Attack],
    program: GuardProgram,
) -> dict[str, object]:
    prefix6 = next(
        attack
        for attack in baseline
        if attack.name == "partial_inverse_prefix_6"
    )
    u_index = C745.RAIL_INDEX["U"]
    dirty_updates = tuple(
        (wire, value)
        for wire, value in prefix6.updates
        if (
            wire >= layout.primary_start
            and wire < layout.guard_start
            and (wire - layout.primary_start) % len(C745.RAILS) == u_index
        )
    )
    pristine = engaged_state(fixture, program)
    clean_regions = protected_regions(pristine, program)
    checkpoint = program.copy_starts[0]
    syndrome = program.receipt_ranges[0][0]
    rows: list[dict[str, object]] = []
    for cell, (wire, value) in enumerate(dirty_updates):
        state = bytearray(pristine)
        state[wire] = value
        local_word = (
            K719.A.cn(wire, syndrome + wire),
            K719.A.cn(checkpoint + wire, syndrome + wire),
            K719.A.cn(syndrome + wire, wire),
        )
        compiled_slice = program.boundary_word[3 * wire:3 * wire + 3]
        apply_compiled_word(state, local_word)
        rows.append({
            "byte_exact": protected_regions(state, program) == clean_regions,
            "cell": cell,
            "compiled_slice_exact": tuple(
                (gate.kind, gate.wires) for gate in local_word
            ) == tuple(
                (gate.kind, gate.wires) for gate in compiled_slice
            ),
            "detected": state[syndrome + wire] == 1,
            "rolled_back": state[wire] == pristine[wire],
            "wire": wire,
        })
    return {
        "all_byte_exact": all(row["byte_exact"] for row in rows),
        "all_compiled_slices_exact": all(
            row["compiled_slice_exact"] for row in rows
        ),
        "all_detected": all(row["detected"] for row in rows),
        "all_rolled_back": all(row["rolled_back"] for row in rows),
        "dirty_flip_count": len(rows),
        "first_wire": rows[0]["wire"] if rows else None,
        "last_wire": rows[-1]["wire"] if rows else None,
        "per_flip_digest": digest(rows),
    }


def lawful_non_interference(
    fixture: Fixture,
    programs: tuple[GuardProgram, ...],
) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for source in origin_zero_branches():
        raw = C719.controller_full_input(source)
        mirrored = raw
        engagement_step: int | None = None
        auxiliary_projection_exact = True
        program_copy_exact = {program.name: True for program in programs}
        for step in range(C719.CONTROLLER_STATIONS):
            raw = C719.apply_fast_int(raw, C719.CONTROLLER_H_FAST)
            mirrored = C719.apply_fast_int(mirrored, C719.CONTROLLER_H_FAST)
            if raw != mirrored:
                auxiliary_projection_exact = False
            decoded = decoded_cell_rows(controller_data(mirrored))
            if decoded and engagement_step is None:
                engagement_step = step
                content = payload_bytes(decoded)
                primary = first_write_events(content)
                outer = outer_guard_events(primary)
                live = (
                    *int_to_bits(
                        controller_data(mirrored), C719.CONTROLLER_DATA_WIDTH
                    ),
                    *flatten(primary),
                    *flatten(outer),
                )
                if tuple(live) != fixture.live_bits:
                    auxiliary_projection_exact = False
                for program in programs:
                    state = bytearray(program.total_rails)
                    state[:program.live_width] = bytes(live)
                    before = bytes(state[:program.live_width])
                    apply_compiled_word(state, program.engage_word)
                    copies_exact = all(
                        bytes(state[start:start + program.live_width]) == before
                        for start in program.copy_starts
                    )
                    program_copy_exact[program.name] &= (
                        bytes(state[:program.live_width]) == before
                        and copies_exact
                    )
        rows.append({
            "auxiliary_projection_exact": auxiliary_projection_exact,
            "engagement_step": engagement_step,
            "mode": source_mode(source),
            "program_copy_exact": program_copy_exact,
            "raw_equals_mirrored": raw == mirrored,
        })
    mode6 = next(row for row in rows if row["mode"] == 6)
    nonrecord = tuple(row for row in rows if row["mode"] != 6)
    return {
        "all_lawful_bit_identical": all(
            row["raw_equals_mirrored"] and row["auxiliary_projection_exact"]
            for row in rows
        ),
        "all_program_fanouts_noninterfering": all(
            all(row["program_copy_exact"].values()) for row in rows
        ),
        "engagement_step": mode6["engagement_step"],
        "mode6_bit_identical": mode6["raw_equals_mirrored"],
        "nonrecord_modes": tuple(row["mode"] for row in nonrecord),
        "nonrecord_modes_untouched": all(
            row["engagement_step"] is None and row["raw_equals_mirrored"]
            for row in nonrecord
        ),
        "rows": rows,
    }


def fanout_closure(
    seed: int,
    edges: tuple[tuple[int, int], ...],
) -> tuple[int, ...]:
    adjacency: dict[int, list[int]] = {}
    for source, target in edges:
        adjacency.setdefault(source, []).append(target)
    visited = {seed}
    queue = deque((seed,))
    while queue:
        source = queue.popleft()
        for target in adjacency.get(source, ()):
            if target not in visited:
                visited.add(target)
                queue.append(target)
    return tuple(sorted(visited))


def adaptive_null_attack(
    fixture: Fixture,
    layout: LiveLayout,
    program: GuardProgram,
) -> dict[str, object]:
    seed = layout.primary_start + C745.RAIL_INDEX["D"]
    wires = fanout_closure(seed, program.fanout_edges)
    word = tuple(K719.A.x(wire) for wire in wires)
    state = engaged_state(fixture, program)
    clean_regions = protected_regions(state, program)
    for gate in word:
        apply_compiled_word(state, (gate,))
    attacked_regions = protected_regions(state, program)
    apply_compiled_word(state, program.boundary_word)
    after_regions = protected_regions(state, program)
    syndrome = receipt_count(state, program)
    record_exact = (
        primary_d_bytes(state, fixture, layout) == fixture.record_content
    )
    return {
        "attack_effect": {
            "after_guard_still_mutated": after_regions != clean_regions,
            "attack_mutated_guarded_region": attacked_regions != clean_regions,
            "record_byte_identical_after": record_exact,
            "syndrome_count": syndrome,
            "zero_syndrome": syndrome == 0,
        },
        "attack_name": f"adaptive_fanout_closure_{program.name}",
        "attack_word": tuple(
            {"kind": gate.kind, "wires": gate.wires} for gate in word
        ),
        "compiled_from_guard_fanout": True,
        "fanout_edge_count": len(program.fanout_edges),
        "seed_live_wire": seed,
        "word_gate_count": len(word),
        "word_kinds": tuple(sorted({gate.kind for gate in word})),
        "word_wires": wires,
    }


def regress_theorem_candidate(
    adaptive_rows: dict[str, dict[str, object]],
) -> dict[str, object]:
    mechanical_success = all(
        row["attack_effect"]["attack_mutated_guarded_region"]
        and row["attack_effect"]["after_guard_still_mutated"]
        and row["attack_effect"]["zero_syndrome"]
        and not row["attack_effect"]["record_byte_identical_after"]
        for row in adaptive_rows.values()
    )
    declared_names = set(FAMILY_50_NAMES)
    constructed_names = {
        row["attack_name"] for row in adaptive_rows.values()
    }
    return {
        "arbitrary_M2_result": (
            "PROVED at the stated state-only, fully editable, non-interfering "
            "finite-guard scope: if G admits two lawful zero-syndrome "
            "codewords c(x) and c(x') with different guarded live regions, "
            "the finite X word on exactly the Hamming-difference rails maps "
            "c(x) to c(x'). G then receives a lawful zero-syndrome codeword "
            "and cannot distinguish the attack from no attack."
        ),
        "constructive_proof_executed": mechanical_success,
        "declared_770_777_battery_contains_constructed_word": bool(
            constructed_names.intersection(declared_names)
        ),
        "declared_alphabet_decision": (
            "The declared Cycle-770 26-case and Cycle-777 50-case battery "
            "families do not contain a simultaneous live-plus-all-copies "
            "fanout-closure word. C745.ALPHABET_SCOPE contains only "
            "IDLE, READ, WRITE[0], WRITE[1]."
        ),
        "scope_qualification": (
            "The universal statement requires a state-only guard whose "
            "relevant rails are all attackable, non-interference on at least "
            "two distinct lawful guarded states, and arbitrary finite M2 "
            "rail words. It does not cover an authenticated or inaccessible "
            "reference, nor an attack alphabet restricted to the frozen "
            "26/50 manifests."
        ),
        "under_arbitrary_M2_words": True,
    }


def program_provenance(
    programs: tuple[GuardProgram, ...],
) -> dict[str, object]:
    landed_constructor_kinds = tuple(sorted({
        K719.A.x(0).kind,
        K719.A.cn(0, 1).kind,
        K719.A.tof(0, 1, 2).kind,
    }))
    rows: dict[str, object] = {}
    all_valid = True
    for program in programs:
        word = (*program.engage_word, *program.boundary_word)
        kinds = tuple(sorted({gate.kind for gate in word}))
        valid = set(kinds).issubset({"X", "CNOT", "TOF"})
        all_valid &= valid
        rows[program.name] = {
            "boundary_gate_count": len(program.boundary_word),
            "copy_starts": program.copy_starts,
            "engage_gate_count": len(program.engage_word),
            "expanded_gate_count": len(word),
            "expanded_gate_kinds": dict(Counter(gate.kind for gate in word)),
            "expanded_gate_sha256": gate_word_sha256(word),
            "fanout_edge_count": len(program.fanout_edges),
            "metadata": program.metadata,
            "primitive_subset": valid,
            "receipt_ranges": program.receipt_ranges,
            "total_rails": program.total_rails,
        }
    return {
        "all_program_gates_X_CNOT_TOF": all_valid,
        "constructor": "Cycle719 K719.A.x/cn/tof",
        "landed_constructor_kinds": landed_constructor_kinds,
        "landed_controller_kinds": tuple(sorted({
            gate.kind for gate in C719.CONTROLLER_H_WORD
        })),
        "programs": rows,
    }


def battery_prefix(
    full: dict[str, object],
    count: int,
    names: tuple[str, ...],
) -> dict[str, object]:
    rows = list(full["rows"])[:count]
    return {
        "all_algebra_agree": all(row["algebra_agreement"] for row in rows),
        "all_clean": all(row["standard_769_pass"] for row in rows),
        "attack_count": len(rows),
        "manifest_sha256": digest(names),
        "passed_count": sum(row["standard_769_pass"] for row in rows),
        "rows": rows,
        "survivors": tuple(
            row["name"] for row in rows if not row["standard_769_pass"]
        ),
    }


def projected_stdout_bytes(lines: list[str], report: dict[str, object]) -> int:
    final = canonical_json(report)
    return sum(len((line + "\n").encode("utf-8")) for line in (*lines, final))


def main() -> int:
    started = perf_counter()
    before_snapshot = evidence_snapshot()
    firewall = source_firewall()
    fixture = make_fixture()
    layout = make_live_layout(fixture)

    single = compile_single_checkpoint(layout.live_width, name="single")
    majority = compile_majority_three(layout.live_width)
    refresh = compile_single_checkpoint(
        layout.live_width,
        name="refresh",
        refresh_metadata={
            "checkpoint_refresh": "fresh zero bank at every station boundary",
            "engagement_step": fixture.engagement_step,
            "landed_controller_stations": C719.CONTROLLER_STATIONS,
            "post_engagement_lawful_station_boundaries": (
                C719.CONTROLLER_STATIONS - fixture.engagement_step - 1
            ),
            "landed_orbit_reduction": (
                "Each battery trial attacks immediately after the active "
                "fresh fan-out. Refresh shortens the attack interval but "
                "does not authenticate the newly copied state."
            ),
        },
    )
    programs = (single, majority, refresh)

    baseline, baseline_candidates = build_baseline_attacks(fixture, layout)
    forward, forward_candidates = build_record_forward_attacks(fixture, layout)
    guard_attacks = build_guard_attacks(fixture, layout)
    checkpoint_attacks = build_checkpoint_attacks(fixture, layout)
    family50 = [*baseline, *forward, *guard_attacks]
    family81 = [*family50, *checkpoint_attacks]
    if tuple(attack.name for attack in family50) != FAMILY_50_NAMES:
        raise AssertionError("50-case manifest mismatch")
    if tuple(attack.name for attack in family81) != FAMILY_81_NAMES:
        raise AssertionError("81-case manifest mismatch")

    pristine_single = engaged_state(fixture, single)
    pristine_majority = engaged_state(fixture, majority)
    pristine_refresh = engaged_state(fixture, refresh)
    single81 = run_battery(
        family81, pristine_single, fixture, layout, single
    )
    single26 = battery_prefix(single81, 26, BASELINE_ATTACK_NAMES)
    single50 = battery_prefix(single81, 50, FAMILY_50_NAMES)
    majority81 = run_battery(
        family81, pristine_majority, fixture, layout, majority
    )
    refresh_boundary_rows: list[tuple[int, dict[str, object]]] = []
    for boundary_step, boundary_fixture in make_refresh_boundary_fixtures():
        boundary_layout = make_live_layout(boundary_fixture)
        if boundary_layout != layout:
            raise AssertionError("refresh boundary layout drifted")
        boundary_baseline, _boundary_candidates = build_baseline_attacks(
            boundary_fixture, boundary_layout
        )
        boundary_forward, _boundary_forward_candidates = (
            build_record_forward_attacks(boundary_fixture, boundary_layout)
        )
        boundary_guard = build_guard_attacks(
            boundary_fixture, boundary_layout
        )
        boundary_checkpoint = build_checkpoint_attacks(
            boundary_fixture, boundary_layout
        )
        boundary_family81 = [
            *boundary_baseline,
            *boundary_forward,
            *boundary_guard,
            *boundary_checkpoint,
        ]
        refresh_boundary_rows.append((
            boundary_step,
            run_battery(
                boundary_family81,
                engaged_state(boundary_fixture, refresh),
                boundary_fixture,
                boundary_layout,
                refresh,
            ),
        ))
    refresh_boundary_count = len(refresh_boundary_rows)
    refresh81 = refresh_boundary_rows[-1][1]
    refresh_pass_patterns = tuple(
        tuple(row["standard_769_pass"] for row in battery["rows"])
        for _step, battery in refresh_boundary_rows
    )
    refresh_all_boundaries_agree = (
        len(set(refresh_pass_patterns)) == 1
    )
    refresh_boundary_summaries = tuple(
        {
            "all_algebra_agree": battery["all_algebra_agree"],
            "passed_count": battery["passed_count"],
            "station": step,
        }
        for step, battery in refresh_boundary_rows
    )

    # A second complete evaluation, including the compiled majority word,
    # makes determinism a same-process byte-for-byte result check.
    rerun_payload = {
        "single": run_battery(
            family81, pristine_single, fixture, layout, single
        ),
        "majority3": run_battery(
            family81, pristine_majority, fixture, layout, majority
        ),
        "refresh": run_battery(
            family81, pristine_refresh, fixture, layout, refresh
        ),
    }
    deterministic = rerun_payload == {
        "single": single81,
        "majority3": majority81,
        "refresh": refresh81,
    }

    detection = detection_recount(fixture, layout, baseline, single)
    controls = landed_controls(
        fixture,
        baseline,
        baseline_candidates,
        forward_candidates,
        guard_attacks,
    )
    noninterference = lawful_non_interference(fixture, programs)
    provenance = program_provenance(programs)
    adaptive = {
        program.name: adaptive_null_attack(fixture, layout, program)
        for program in programs
    }
    regress = regress_theorem_candidate(adaptive)
    after_snapshot = evidence_snapshot()
    anchors_pinned = all(
        before_snapshot[path]["sha256"] == EXPECTED_SHA256[path]
        for path in EXPECTED_SHA256
    )

    base_counts = (
        single26["passed_count"],
        single50["passed_count"],
        single81["passed_count"],
    )
    battery_agreement = base_counts == (14, 38, 38)
    per_attack_agreement = all(
        row["algebra_agreement"] for row in single81["rows"]
    )
    majority_closed = bool(majority81["all_clean"])
    refresh_closed = all(
        battery["all_clean"] for _step, battery in refresh_boundary_rows
    )
    adaptive_success = bool(regress["constructive_proof_executed"])
    outcome = (
        "LAW_UPGRADE_CANDIDATE"
        if majority_closed or refresh_closed
        else "REGRESS_CONFIRMED"
    )

    findings = {
        "1_DETECTION_RECOUNT": (
            f"Detection recount: {detection['dirty_flip_count']}/744 "
            "prefix-6 U flips were independently detected and rolled back "
            "byte-exactly."
        ),
        "2_BATTERY_RECOUNT": (
            f"Battery recount: {single26['passed_count']}/26, "
            f"{single50['passed_count']}/50, "
            f"{single81['passed_count']}/81; per-attack compiled/algebra "
            f"agreement={str(per_attack_agreement).lower()}."
        ),
        "3_MAJORITY3_VARIANT": (
            f"Majority-3 full battery: {majority81['passed_count']}/81; "
            f"closes={str(majority_closed).lower()}; "
            f"survivors={len(majority81['survivors'])}."
        ),
        "4_REFRESH_VARIANT": (
            f"Interleaved-refresh full battery: "
            f"{refresh81['passed_count']}/81; "
            f"closes={str(refresh_closed).lower()}; landed engagement at "
            f"{fixture.engagement_step}/{C719.CONTROLLER_STATIONS - 1}; "
            f"actual boundary counts="
            + ",".join(
                f"{row['station']}:{row['passed_count']}/81"
                for row in refresh_boundary_summaries
            )
            + "."
        ),
        "5_ADAPTIVE_COUNTERATTACK": (
            "Adaptive fanout-closure X words defeated single, majority-3, "
            "and refresh with zero syndrome and a changed record; mechanical "
            f"construction success={str(adaptive_success).lower()}."
        ),
        "6_ARBITRARY_M2_REGRESS": (
            "REGRESS_CONFIRMED under arbitrary finite M2 rail words for "
            "fully editable state-only non-interfering guards with at least "
            "two lawful codewords; the frozen Cycle-770/777 battery family "
            "does not contain the constructed simultaneous closure word."
        ),
        "7_PROVENANCE_NONINTERFERENCE": (
            "All compiled guard gates are X/CNOT/TOF from the landed Cycle-719 "
            "constructors, and all lawful controller projections are "
            "bit-identical."
        ),
        "8_CONTROLS_BOUNDS": (
            f"Controls: unguarded={controls['unguarded_5_of_26']['refused_count']}"
            "/26 refused and landed-guard="
            f"{controls['landed_guard_38_of_50']['refused_count']}/50 refused; "
            f"anchors_pinned={str(anchors_pinned).lower()}; "
            f"determinism={str(deterministic).lower()}."
        ),
    }

    certificates = {
        "1_DETECTION_RECOUNT": bool(
            detection["dirty_flip_count"] == 744
            and detection["all_detected"]
            and detection["all_rolled_back"]
            and detection["all_byte_exact"]
            and detection["all_compiled_slices_exact"]
        ),
        "2_BATTERY_RECOUNT": bool(
            battery_agreement
            and per_attack_agreement
            and single26["attack_count"] == 26
            and single50["attack_count"] == 50
            and single81["attack_count"] == 81
        ),
        "3_MAJORITY3_VARIANT": bool(
            majority81["attack_count"] == 81
            and majority81["all_algebra_agree"]
        ),
        "4_REFRESH_VARIANT": bool(
            refresh81["attack_count"] == 81
            and all(
                row["all_algebra_agree"]
                for row in refresh_boundary_summaries
            )
            and refresh_boundary_count == 5
            and refresh.metadata[
                "post_engagement_lawful_station_boundaries"
            ] == 4
            and refresh_all_boundaries_agree
        ),
        "5_ADAPTIVE_COUNTERATTACK": adaptive_success,
        "6_ARBITRARY_M2_REGRESS": bool(
            regress["constructive_proof_executed"]
            and regress["under_arbitrary_M2_words"]
            and not regress[
                "declared_770_777_battery_contains_constructed_word"
            ]
        ),
        "7_PROVENANCE_NONINTERFERENCE": bool(
            provenance["all_program_gates_X_CNOT_TOF"]
            and provenance["landed_constructor_kinds"]
            == ("CNOT", "TOF", "X")
            and set(provenance["landed_controller_kinds"]).issubset(
                {"CNOT", "TOF", "X"}
            )
            and noninterference["all_lawful_bit_identical"]
            and noninterference["all_program_fanouts_noninterfering"]
            and noninterference["engagement_step"] == 125
        ),
        "8_CONTROLS_BOUNDS": False,
    }

    attack_table = []
    for index, (base_row, majority_row, refresh_row) in enumerate(zip(
        single81["rows"], majority81["rows"], refresh81["rows"]
    )):
        attack_table.append({
            "agreement": base_row["algebra_agreement"],
            "base_standard_pass": base_row["standard_769_pass"],
            "family26_member": index < 26,
            "family50_member": index < 50,
            "majority3_standard_pass": majority_row["standard_769_pass"],
            "name": base_row["name"],
            "refresh_standard_pass": refresh_row["standard_769_pass"],
            "single_syndrome_count": base_row["syndrome_count"],
            "target": base_row["target"],
        })

    data_lines = [
        "WITNESS_STANDARD_769_VERBATIM "
        + json.dumps(WITNESS_STANDARD_769_VERBATIM),
        "SHA_AST_ANCHORS " + canonical_json(before_snapshot),
        "IMPORT_BLOCKLIST " + canonical_json(firewall),
        "DETECTION_RECOUNT " + canonical_json(detection),
        "BATTERY_SUMMARY " + canonical_json({
            "single_26": f"{single26['passed_count']}/26",
            "single_50": f"{single50['passed_count']}/50",
            "single_81": f"{single81['passed_count']}/81",
        }),
    ]
    data_lines.extend(
        "BATTERY_ATTACK_AGREEMENT " + canonical_json(row)
        for row in attack_table
    )
    variant_table = [
        {
            "base_pass": base["standard_769_pass"],
            "majority3_pass": maj["standard_769_pass"],
            "name": base["name"],
            "refresh_pass": ref["standard_769_pass"],
        }
        for base, maj, ref in zip(
            single81["rows"], majority81["rows"], refresh81["rows"]
        )
    ]
    if majority_closed or refresh_closed:
        data_lines.append("LAW_UPGRADE_CANDIDATE")
        data_lines.append(
            "LAW_UPGRADE_CANDIDATE_FULL_TABLE " + canonical_json(variant_table)
        )
    else:
        data_lines.append("NO_LAW_UPGRADE_CANDIDATE")
        data_lines.append("VARIANT_FULL_TABLE " + canonical_json(variant_table))
    data_lines.extend([
        "VARIANT_SUMMARY " + canonical_json({
            "majority3": {
                "passed": majority81["passed_count"],
                "total": majority81["attack_count"],
                "survivors": majority81["survivors"],
            },
            "refresh": {
                "boundary_summaries": refresh_boundary_summaries,
                "passed": refresh81["passed_count"],
                "total": refresh81["attack_count"],
                "survivors": refresh81["survivors"],
            },
        }),
        "ADAPTIVE_COUNTERATTACKS " + canonical_json(adaptive),
        "ALPHABET_SCOPE_AND_REGRESS_THEOREM " + canonical_json(regress),
        "REGRESS_CONFIRMED" if adaptive_success else "REGRESS_NOT_CONFIRMED",
        "GATE_PROVENANCE_FULL " + canonical_json(provenance),
        "NON_INTERFERENCE " + canonical_json(noninterference),
        "CONTROLS " + canonical_json(controls),
    ])
    for key, finding in findings.items():
        data_lines.append(f"FINDING_{key} " + json.dumps(finding))

    runtime_sec = perf_counter() - started
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "battery": {
            "26": single26["passed_count"],
            "50": single50["passed_count"],
            "81": single81["passed_count"],
        },
        "certificates": certificates,
        "determinism": deterministic,
        "majority3": {
            "all_clean": majority_closed,
            "passed_count": majority81["passed_count"],
        },
        "outcome": outcome,
        "refresh": {
            "all_clean": refresh_closed,
            "boundary_summaries": refresh_boundary_summaries,
            "passed_count": refresh81["passed_count"],
        },
        "regress_confirmed": adaptive_success,
        "runtime_sec": runtime_sec,
        "stdout_bytes": 0,
    }
    certificate_lines: list[str] = []
    for _iteration in range(8):
        certificates["8_CONTROLS_BOUNDS"] = bool(
            controls["unguarded_5_of_26"] == {
                "attack_count": 26,
                "refused_count": 5,
            }
            and controls["landed_guard_38_of_50"]["attack_count"] == 50
            and controls["landed_guard_38_of_50"]["refused_count"] == 38
            and anchors_pinned
            and before_snapshot == after_snapshot
            and firewall["ok"]
            and deterministic
            and runtime_sec < AUDIT_TIMEOUT_SEC
            and int(report["stdout_bytes"]) < 150_000
        )
        report["certificates"] = certificates
        certificate_lines = [
            ("PASS" if value else "FAIL") + f" CERTIFICATE_{key}"
            for key, value in certificates.items()
        ]
        candidate_lines = [*data_lines, *certificate_lines]
        size = projected_stdout_bytes(candidate_lines, report)
        if size == report["stdout_bytes"]:
            break
        report["stdout_bytes"] = size

    final_lines = [*data_lines, *certificate_lines]
    final_size = projected_stdout_bytes(final_lines, report)
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
