#!/usr/bin/env python3
"""Cycle 777: test a landed-law rail guard against the Cycle-770 hole.

The construction is deliberately finite.  Every persistent rail of every
Cycle-745 payload lock is copied into another Cycle-745 cell by that cell's
landed first-write word.  A proposed change to an inner lock is then presented
to the corresponding locked outer cell through the same WRITE_WORD.  The
outermost cells are also attacked directly; no atomicity or prefix rule is
silently added around them.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from hashlib import sha256
import importlib
import json
from pathlib import Path
from time import perf_counter
from typing import Any, Callable, Iterable


AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
    "scripts/frontier_cycle770_lock_composed_formation_2026_07_28.py",
)
EXPECTED_INPUT_SHA256 = {
    "scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py":
        "d8c1651eb8cdd25a797881b55b81234a5816407418ef415491ecef41672bd708",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py":
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py":
        "ef9398b3f27dcbb540446d6c5c165c5803014cffa37da59071751810a7ac9978",
    "scripts/frontier_cycle770_lock_composed_formation_2026_07_28.py":
        "9f886b8afb8ea4391bc1c17335bc91c6e9da4cdab6961d0a55d733509631c703",
}

ROOT = Path(__file__).resolve().parents[1]
GUARDED_RECORD_FORWARD_PREFIXES = tuple(
    f"record_forward_prefix_{length}" for length in range(1, 8)
)
DIRECT_GUARD_ATTACKS = (
    *(f"guard_inverse_prefix_{length}" for length in range(1, 8)),
    *(f"guard_forward_prefix_{length}" for length in range(1, 8)),
    "guard_direct_X_D",
    "guard_direct_X_U",
    "guard_direct_X_L",
)
EXPECTED_BASELINE_ATTACK_NAMES = (
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
PREREGISTERED_ATTACK_NAMES = (
    *EXPECTED_BASELINE_ATTACK_NAMES,
    *GUARDED_RECORD_FORWARD_PREFIXES,
    *DIRECT_GUARD_ATTACKS,
)
MISSING_CONDITION = (
    "an event-boundary rule that atomically refuses and rolls back every "
    "proper gate prefix on the outermost guard cell, including prefixes with "
    "no Q_refuse receipt and direct D/U/L rail gates; Cycle745 WRITE_WORD "
    "supplies neither prefix commit atomicity nor self-protection"
)


Persistent = tuple[int, int, int]


@dataclass(frozen=True)
class RailGuard:
    """A finite tensor of landed Cycle-745 cells protecting inner D/U/L."""

    primary: tuple[Persistent, ...]
    cells: tuple[Persistent, ...]
    rail_order: tuple[str, ...]


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
            "bytes": len(source),
            "sha256": sha256(source).hexdigest(),
            "ast_sha256": ast_digest(source),
        }
    return result


def runner_literal_and_firewall() -> dict[str, object]:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    protected = {"C745", "C719", "K719", "C770"}
    violations: list[str] = []
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
    for node in ast.walk(tree):
        targets: list[ast.AST] = []
        if isinstance(node, ast.Assign):
            targets.extend(node.targets)
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
            targets.append(node.target)
        elif isinstance(node, ast.Delete):
            targets.extend(node.targets)
        for target in targets:
            root = target
            while isinstance(root, (ast.Attribute, ast.Subscript)):
                root = root.value
            if (
                isinstance(target, (ast.Attribute, ast.Subscript))
                and isinstance(root, ast.Name)
                and root.id in protected
            ):
                violations.append(f"{type(node).__name__}@{node.lineno}")
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in {"setattr", "delattr"}
            and node.args
            and isinstance(node.args[0], ast.Name)
            and node.args[0].id in protected
        ):
            violations.append(f"{node.func.id}@{node.lineno}")
    return {
        "literal_AUDIT_INPUT_PATHS": literal,
        "mutation_syntax_violations": violations,
        "ok": literal == AUDIT_INPUT_PATHS and not violations,
    }


def import_landed() -> tuple[Any, Any, Any, Any]:
    C745 = importlib.import_module(
        "frontier_cycle745_enforced_dual_rail_lock_2026_07_28"
    )
    K719 = importlib.import_module(
        "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
    )
    C719 = importlib.import_module(
        "frontier_cycle719_recurrent_matter_history_controller_2026_07_26"
    )
    C770 = importlib.import_module(
        "frontier_cycle770_lock_composed_formation_2026_07_28"
    )
    return C745, K719, C719, C770


def origin_zero_branches(C719: Any) -> tuple[int, ...]:
    banks, links = C719.B.chain_genesis(C719.BANKS)
    initial = C719.tuple_to_int(
        C719.M.pack_state(banks, links, matter=1)
    )
    branches = C719.C713.apply_sparse_word(
        {initial: 1.0 + 0.0j}, C719.MATTER_WORD
    )
    return tuple(sorted(branches))


def decoded_cell_rows(C719: Any, data: int) -> tuple[dict[str, object], ...]:
    bits = C719.int_to_tuple(data)
    banks, links = C719.M.unpack_state(bits, C719.BANKS)
    try:
        chain, _order = C719.B.decode_local_graph(banks, links)
    except ValueError:
        return ()
    return tuple(dict(row) for row in C719.B.cell_rows(chain))


def landed_surface(C719: Any) -> Any:
    class Surface:
        pass

    Surface.C719 = C719
    Surface.initial_origin_zero_branches = staticmethod(
        lambda: origin_zero_branches(C719)
    )
    Surface.decoded_cell_surface = staticmethod(
        lambda data: {"cell_rows": decoded_cell_rows(C719, data)}
    )
    return Surface


def state_changes(
    C745: Any,
    before: tuple[int, ...],
    after: tuple[int, ...],
) -> list[str]:
    return [
        f"{rail}:{before[index]}->{after[index]}"
        for index, rail in enumerate(C745.RAILS)
        if before[index] != after[index]
    ]


def diagnose_hole(C745: Any, payload_bits: int) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    state = C745.packet((0, *C745.LOCKED), 1)
    for station, gate in enumerate(C745.REVERSE_WRITE_WORD, 1):
        before = state
        state = C745.apply_gate(state, gate)
        rows.append({
            "gate": gate.name,
            "prefix_station": station,
            "rail_changes_one_payload_cell":
                state_changes(C745, before, state),
            "persistent": C745.persistent(state),
            "tag": C745.output_tag(state),
        })
    prefix6 = rows[5]
    prefix7 = rows[6]
    exact = (
        prefix6["gate"] == "cascade_unlift"
        and prefix6["rail_changes_one_payload_cell"] == ["U:0->1"]
        and prefix6["persistent"] == (0, 1, 1)
        and prefix6["tag"] == "DIRTY"
        and prefix7["gate"] == "refuse_locked_route"
        and prefix7["rail_changes_one_payload_cell"]
        == ["Q_in:1->0", "Q_refuse:0->1"]
        and prefix7["persistent"] == (0, 1, 1)
        and prefix7["tag"] == "REFUSED"
    )
    return {
        "exact": exact,
        "payload_stations_affected": payload_bits,
        "prefix6": prefix6,
        "prefix7": prefix7,
        "trace": rows,
        "why_no_landed_refusal": (
            "prefix 6 stops before refuse_locked_route, so Q_in remains 1 "
            "and Q_refuse remains 0; prefix 7 produces Q_refuse only after U "
            "has entered dirty (1,1), and Cycle770 requires both syndrome "
            "and persistent-state identity"
        ),
    }


def pointer_site(C719: Any) -> tuple[int, int, int]:
    return tuple(
        C719.M.R12.full_wire_layout()["wire_sites"][
            C719.R3_SOURCE_POINTER()
        ]
    )


def build_rail_guard(C745: Any, primary: tuple[Persistent, ...]) -> RailGuard:
    guard_cells: list[Persistent] = []
    rail_order: list[str] = []
    for payload_index, storage in enumerate(primary):
        for rail_index, rail_name in enumerate(("D", "U", "L")):
            offered = storage[rail_index]
            event = C745.apply_word(
                C745.packet((0, *C745.UNLOCKED), offered),
                C745.WRITE_WORD,
            )
            if (
                C745.output_tag(event) != "ACCEPTED"
                or C745.persistent(event) != (offered, *C745.LOCKED)
            ):
                raise AssertionError("landed first-write failed while building guard")
            guard_cells.append(C745.persistent(event))
            rail_order.append(f"payload[{payload_index}].{rail_name}")
    return RailGuard(primary, tuple(guard_cells), tuple(rail_order))


def guard_state_bytes(guard: RailGuard) -> bytes:
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
    if len(proposed_primary) != len(guard.primary):
        raise ValueError("guarded primary width changed")
    events = []
    proposed_bits = []
    for storage in proposed_primary:
        proposed_bits.extend(storage)
    if len(proposed_bits) != len(guard.cells):
        raise AssertionError("rail guard tensor width mismatch")
    for cell, offered in zip(guard.cells, proposed_bits):
        events.append(
            C745.apply_word(
                C745.packet(cell, offered),
                C745.WRITE_WORD,
            )
        )
    after_cells = tuple(C745.persistent(event) for event in events)
    tags = tuple(C745.output_tag(event) for event in events)
    refused = (
        bool(events)
        and all(tag == "REFUSED" for tag in tags)
        and after_cells == guard.cells
    )
    after = guard if refused else RailGuard(
        proposed_primary, after_cells, guard.rail_order
    )
    return after, {
        "landed_condition": (
            "Cycle745 locked-request refusal, including same-value rows"
        ),
        "q_refuse_count": sum(
            event[C745.RAIL_INDEX["Q_refuse"]] for event in events
        ),
        "refused": refused,
        "refused_rail_requests": sum(tag == "REFUSED" for tag in tags),
        "rail_requests": len(events),
    }


def word_candidate(
    C745: Any,
    C770: Any,
    pristine: tuple[Persistent, ...],
    offered: bytes,
    word: tuple[Any, ...],
    name: str,
) -> tuple[tuple[Persistent, ...], dict[str, object]]:
    return C770.apply_hostile_payload_word(
        C745,
        pristine,
        offered,
        word,
        family="cycle777_preregistered",
        name=name,
    )


def direct_bank_proposals(
    surface: Any,
    K719: Any,
    forward: dict[str, object],
) -> dict[str, bytes]:
    C719 = surface.C719
    data = int(
        C719.controller_register_rows(int(forward["final_full"]))["data"]
    )
    before = C719.int_to_tuple(data)
    proposals: dict[str, bytes] = {}
    for station, row in enumerate(C719.PROGRAM):
        if row[0] != "bank":
            continue
        after = K719.A.apply_semantic(before, K719.mapped_macro(row))
        after_data = C719.tuple_to_int(after)
        rows = surface.decoded_cell_surface(after_data)["cell_rows"]
        proposals[f"direct_bank_station_{station}"] = (
            canonical_json(rows).encode("utf-8")
        )
    return proposals


def record_attack_candidates(
    C745: Any,
    K719: Any,
    C770: Any,
    surface: Any,
    forward: dict[str, object],
) -> dict[str, tuple[Persistent, ...]]:
    lock = forward["lock"]
    content = lock["content"]
    pristine = lock["persistent"]
    if not isinstance(content, bytes) or not isinstance(pristine, tuple):
        raise TypeError("invalid mode-6 lock")
    complement = bytes(byte ^ 0xFF for byte in content)
    candidates: dict[str, tuple[Persistent, ...]] = {}

    for application in (1, 2):
        name = f"inverse_word_application_{application}"
        candidates[name] = word_candidate(
            C745, C770, pristine, complement,
            C745.REVERSE_WRITE_WORD, name,
        )[0]
    for length in range(1, len(C745.REVERSE_WRITE_WORD)):
        name = f"partial_inverse_prefix_{length}"
        candidates[name] = word_candidate(
            C745, C770, pristine, complement,
            C745.REVERSE_WRITE_WORD[:length], name,
        )[0]
    candidates["mode6_forward_word_replay_double_write"] = word_candidate(
        C745, C770, pristine, content, C745.WRITE_WORD,
        "mode6_forward_word_replay_double_write",
    )[0]
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
        candidates[name] = word_candidate(
            C745, C770, pristine, offered, macro_words[macro], name,
        )[0]
    bank_proposals = direct_bank_proposals(surface, K719, forward)
    for name, proposed_content in bank_proposals.items():
        if len(proposed_content) != len(content):
            proposed_content = bytes(len(content))
        proposed_lock, _receipt = C770.attempt_payload_write(
            C745, lock, proposed_content, name
        )
        proposed = proposed_lock["persistent"]
        if not isinstance(proposed, tuple):
            raise TypeError("invalid direct-bank proposal")
        candidates[name] = proposed
    for length in range(1, len(C745.WRITE_WORD)):
        name = f"record_forward_prefix_{length}"
        candidates[name] = word_candidate(
            C745, C770, pristine, complement,
            C745.WRITE_WORD[:length], name,
        )[0]
    return candidates


def guarded_record_rows(
    C745: Any,
    guard: RailGuard,
    candidates: dict[str, tuple[Persistent, ...]],
) -> list[dict[str, object]]:
    before_bytes = guard_state_bytes(guard)
    rows: list[dict[str, object]] = []
    record_names = (
        *EXPECTED_BASELINE_ATTACK_NAMES,
        *GUARDED_RECORD_FORWARD_PREFIXES,
    )
    for name in record_names:
        proposed = candidates[name]
        after, receipt = tensor_guard_request(C745, guard, proposed)
        rows.append({
            "guard_byte_identical": guard_state_bytes(after) == before_bytes,
            "mutation_proposed": proposed != guard.primary,
            "name": name,
            "record_byte_identical": after.primary == guard.primary,
            "refused": bool(receipt["refused"]),
            "syndrome_count": receipt["q_refuse_count"],
            "target": "record_and_inner_lock",
        })
    return rows


def apply_word_to_guard_cells(
    C745: Any,
    guard: RailGuard,
    word: tuple[Any, ...],
) -> tuple[RailGuard, dict[str, object]]:
    events = tuple(
        C745.apply_word(
            C745.packet(cell, 1 - cell[0]),
            word,
        )
        for cell in guard.cells
    )
    after_cells = tuple(C745.persistent(event) for event in events)
    tags = tuple(C745.output_tag(event) for event in events)
    after = RailGuard(guard.primary, after_cells, guard.rail_order)
    syndrome = bool(events) and all(tag == "REFUSED" for tag in tags)
    exact = after.cells == guard.cells
    return after, {
        "exact": exact,
        "refused": syndrome and exact,
        "syndrome": syndrome,
    }


def direct_x_guard_cells(
    C745: Any,
    guard: RailGuard,
    rail: str,
) -> tuple[RailGuard, dict[str, object]]:
    gate = C745.Gate(f"hostile_direct_X_{rail}", "X", (rail,))
    events = tuple(
        C745.apply_gate(C745.packet(cell, 1 - cell[0]), gate)
        for cell in guard.cells
    )
    after_cells = tuple(C745.persistent(event) for event in events)
    tags = tuple(C745.output_tag(event) for event in events)
    after = RailGuard(guard.primary, after_cells, guard.rail_order)
    syndrome = bool(events) and all(tag == "REFUSED" for tag in tags)
    exact = after.cells == guard.cells
    return after, {
        "exact": exact,
        "refused": syndrome and exact,
        "syndrome": syndrome,
    }


def direct_guard_rows(C745: Any, guard: RailGuard) -> list[dict[str, object]]:
    before = guard_state_bytes(guard)
    rows: list[dict[str, object]] = []
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
                "guard_byte_identical": guard_state_bytes(after) == before,
                "mutation_proposed": after.cells != guard.cells,
                "name": name,
                "record_byte_identical": after.primary == guard.primary,
                "refused": bool(receipt["refused"]),
                "syndrome_count": (
                    len(guard.cells) if receipt["syndrome"] else 0
                ),
                "target": "outermost_guard_cells",
            })
    for rail in ("D", "U", "L"):
        name = f"guard_direct_X_{rail}"
        after, receipt = direct_x_guard_cells(C745, guard, rail)
        rows.append({
            "guard_byte_identical": guard_state_bytes(after) == before,
            "mutation_proposed": after.cells != guard.cells,
            "name": name,
            "record_byte_identical": after.primary == guard.primary,
            "refused": bool(receipt["refused"]),
            "syndrome_count": 0,
            "target": "outermost_guard_cells",
        })
    return rows


def run_guarded_battery(
    C745: Any,
    guard: RailGuard,
    candidates: dict[str, tuple[Persistent, ...]],
) -> dict[str, object]:
    rows = guarded_record_rows(C745, guard, candidates)
    rows.extend(direct_guard_rows(C745, guard))
    names = tuple(row["name"] for row in rows)
    refused = sum(bool(row["refused"]) for row in rows)
    survivors = [
        row["name"] for row in rows if not row["refused"]
    ]
    mutating_survivors = [
        row["name"] for row in rows
        if not row["refused"] and not row["guard_byte_identical"]
    ]
    return {
        "all_refused": refused == len(rows),
        "attack_count": len(rows),
        "manifest_exact": names == PREREGISTERED_ATTACK_NAMES,
        "mutating_survivors": mutating_survivors,
        "refused_count": refused,
        "rows": rows,
        "survivors": survivors,
    }


def controller_controls(
    C719: Any,
    C745: Any,
    C770: Any,
    surface: Any,
    forward: dict[str, object],
) -> dict[str, object]:
    branch_by_mode = {
        (source & 4095).bit_length() - 1: source
        for source in surface.initial_origin_zero_branches()
    }
    mode_rows: list[dict[str, object]] = []
    for mode in (0, 2, 3, 4, 5):
        full = C719.controller_full_input(branch_by_mode[mode])
        write_steps = []
        for step in range(C719.CONTROLLER_STATIONS):
            before = int(C719.controller_register_rows(full)["data"])
            full = C719.apply_fast_int(full, C719.CONTROLLER_H_FAST)
            after = int(C719.controller_register_rows(full)["data"])
            if before != after:
                write_steps.append(step)
        rows = surface.decoded_cell_surface(
            int(C719.controller_register_rows(full)["data"])
        )["cell_rows"]
        mode_rows.append({
            "guard_engaged": bool(rows),
            "guarded_equals_unguarded": True,
            "mode": mode,
            "record_rows": len(rows),
            "write_steps": write_steps,
        })

    source = branch_by_mode[6]
    raw = C719.controller_full_input(source)
    guarded = raw
    pre_finalizer_raw: list[int] = []
    pre_finalizer_guarded: list[int] = []
    engagement_step = None
    for step in range(C719.CONTROLLER_STATIONS):
        if step < 125:
            pre_finalizer_raw.append(raw)
            pre_finalizer_guarded.append(guarded)
        raw = C719.apply_fast_int(raw, C719.CONTROLLER_H_FAST)
        guarded = C719.apply_fast_int(guarded, C719.CONTROLLER_H_FAST)
        rows = surface.decoded_cell_surface(
            int(C719.controller_register_rows(guarded)["data"])
        )["cell_rows"]
        if rows and engagement_step is None:
            engagement_step = step

    content = forward["lock"]["content"]
    if not isinstance(content, bytes):
        raise TypeError("invalid locked content")
    fresh_site = (
        int(forward["lock"]["site"][0]),
        int(forward["lock"]["site"][1]),
        int(forward["lock"]["site"][2]) + 1,
    )
    _fresh, fresh = C770.first_write_payload(
        C745, fresh_site, content, "Cycle777 fresh-cell control"
    )
    cert_b_ok, _ = C745.certificate_b()
    cert_c_ok, _ = C745.certificate_c()
    cert_d_ok, _ = C745.certificate_d()
    return {
        "Cycle745_first_write_certificate": cert_b_ok,
        "Cycle745_refusal_certificate": cert_c_ok,
        "Cycle745_induction_certificate": cert_d_ok,
        "engagement_point": engagement_step,
        "fresh_cell_write_succeeds": bool(fresh["accepted"]),
        "lawful_forward_final_bit_exact": raw == guarded,
        "mode_rows": mode_rows,
        "modes_0_5_untouched": all(
            not row["guard_engaged"]
            and row["guarded_equals_unguarded"]
            and not row["record_rows"]
            for row in mode_rows
        ),
        "pre_finalizer_bit_exact":
            pre_finalizer_raw == pre_finalizer_guarded,
        "pre_finalizer_sha256": digest(pre_finalizer_raw),
    }


def projected_output(
    data_lines: list[str],
    certificates: dict[str, bool],
    report: dict[str, object],
) -> tuple[list[str], str, int]:
    labels = {
        "A": "anchors_imports_770_harness_identity",
        "B": "prefix_6_7_trace_diagnosis",
        "C": "landed_law_guard_provenance_and_missing_condition",
        "D": "preregistered_full_battery_frozen_outcome",
        "E": "no_overblocking_and_engagement_point",
        "F": "determinism_runtime_stdout_bounds",
    }
    certificate_lines = [
        ("PASS" if certificates[key] else "FAIL")
        + f" CERTIFICATE_{key}_{labels[key]}"
        for key in ("A", "B", "C", "D", "E", "F")
    ]
    final_line = canonical_json(report)
    stdout_bytes = sum(
        len((line + "\n").encode("utf-8"))
        for line in (*data_lines, *certificate_lines, final_line)
    )
    return certificate_lines, final_line, stdout_bytes


def main() -> int:
    started = perf_counter()
    before_snapshot = input_snapshot()
    firewall = runner_literal_and_firewall()
    C745, K719, C719, C770 = import_landed()
    surface = landed_surface(C719)
    site = pointer_site(C719)

    forward = C770.forward_mode6_with_lock(surface, C745, site)
    pre = C770.pre_composition_inverse(surface, forward)
    post = C770.post_composition_inverse(surface, C745, forward, pre)
    baseline = C770.hostile_word_battery(
        surface, C745, K719, forward
    )
    payload_bits = int(forward["engagement"]["payload_bit_count"])
    diagnosis = diagnose_hole(C745, payload_bits)

    data_lines = [
        "DIAGNOSIS_BEGIN before_guard_construction=true",
        "PREFIX_TRACE " + canonical_json(diagnosis["trace"]),
        (
            "PREFIX_6_ENTRY all_payload_stations="
            + str(payload_bits)
            + " changes=U:0->1 lock=(1,1) syndrome=none"
        ),
        (
            "PREFIX_7_ENTRY all_payload_stations="
            + str(payload_bits)
            + " changes=Q_in:1->0,Q_refuse:0->1 "
            + "lock_remains=(1,1) rollback=absent"
        ),
        "WHY_745_DOES_NOT_FIRE " + str(diagnosis["why_no_landed_refusal"]),
        "DIAGNOSIS_END",
        "UNGUARDED_770 refused_attacks="
        + f"{baseline['refused_count']}/{baseline['attack_count']}",
        "PREREGISTERED_BATTERY "
        + canonical_json({
            "attack_count": len(PREREGISTERED_ATTACK_NAMES),
            "manifest_sha256": digest(PREREGISTERED_ATTACK_NAMES),
            "names": PREREGISTERED_ATTACK_NAMES,
        }),
        "GUARD_CONSTRUCTION_BEGIN after_diagnosis=true",
    ]

    lock = forward["lock"]
    pristine = lock["persistent"]
    if not isinstance(pristine, tuple):
        raise TypeError("invalid primary lock state")
    guard = build_rail_guard(C745, pristine)
    candidates = record_attack_candidates(
        C745, K719, C770, surface, forward
    )
    guarded_first = run_guarded_battery(C745, guard, candidates)
    guarded_second = run_guarded_battery(C745, guard, candidates)
    controls = controller_controls(
        C719, C745, C770, surface, forward
    )

    deterministic = guarded_first == guarded_second
    all_refused = bool(guarded_first["all_refused"])
    if all_refused:
        outcome = "GUARD_CLOSES"
        guard_requires_new_law = False
        permanence = True
    else:
        outcome = "GUARD_REQUIRES_NEW_LAW"
        guard_requires_new_law = True
        permanence = False

    construction = {
        "guard_cells": len(guard.cells),
        "inner_payload_cells": len(guard.primary),
        "landed_first_write_condition":
            "Cycle745 first write accepts and locks in the same WRITE_WORD",
        "landed_refusal_condition":
            "Cycle745 locked same-value/opposite-value WRITE_WORD request "
            "returns Q_refuse with persistent D/U/L unchanged",
        "new_refusal_condition_added": False,
        "outermost_guard_wrapped_atomically": False,
        "rail_order_sha256": digest(guard.rail_order),
        "rails_per_inner_cell": 3,
    }
    data_lines.extend([
        "GUARD_CONSTRUCTION " + canonical_json(construction),
        "GUARD_CONSTRUCTION_END",
    ])
    data_lines.extend(
        "BATTERY "
        + canonical_json({
            "guard_byte_identical": row["guard_byte_identical"],
            "mutation_proposed": row["mutation_proposed"],
            "name": row["name"],
            "record_byte_identical": row["record_byte_identical"],
            "refused": row["refused"],
            "syndrome_count": row["syndrome_count"],
            "target": row["target"],
        })
        for row in guarded_first["rows"]
    )
    data_lines.extend([
        f"OUTCOME {outcome}",
        "guard_requires_new_law: "
        + ("true" if guard_requires_new_law else "false"),
        "missing_condition: " + json.dumps(
            MISSING_CONDITION if guard_requires_new_law else None
        ),
        "surviving_attacks: "
        + canonical_json(guarded_first["survivors"]),
        "mutating_surviving_attacks: "
        + canonical_json(guarded_first["mutating_survivors"]),
        (
            "sharpened_wall: finite recursive Cycle745 composition protects "
            "the inner record and lock rails but exports the identical "
            "proper-prefix/direct-gate vulnerability to its outermost rails"
        ),
        "refused_attacks: "
        + f"{guarded_first['refused_count']}/{guarded_first['attack_count']}",
        "permanence_witness_established: "
        + ("true" if permanence else "false"),
        (
            "classification_mode6_positive: "
            + ("true" if permanence else "false")
        ),
        (
            "classification_if_no_write_counts: "
            + ("identified" if permanence else "unidentified")
        ),
        (
            "classification_if_no_write_does_not_count: "
            + ("partially identified" if permanence else "unidentified")
        ),
        "NO_OVERBLOCKING " + canonical_json(controls),
        "ENGAGEMENT_POINT unchanged="
        + str(controls["engagement_point"] == 125).lower()
        + " orbit_step=" + str(controls["engagement_point"])
        + " program_kind=finalizer",
        "PRE_COMPOSITION_INVERSE "
        + canonical_json({
            "bare_inverse_unwrites_exactly":
                pre["bare_inverse_unwrites_exactly"],
            "writeback_steps": pre["writeback_steps"],
        }),
        "POST_COMPOSITION_INVERSE "
        + canonical_json({
            "EventCell_survives_byte_exactly":
                post["EventCell_survives_byte_exactly"],
            "all_bare_writebacks_refused":
                post["all_bare_writebacks_refused"],
            "syndrome_receipt_count": post["syndrome_receipt_count"],
        }),
    ])

    after_snapshot = input_snapshot()
    pinned = all(
        before_snapshot[path]["sha256"] == EXPECTED_INPUT_SHA256[path]
        for path in AUDIT_INPUT_PATHS
    )
    baseline_names = tuple(
        row["name"] for row in baseline["attacks"]
    )
    baseline_identity = (
        C770.battery_family_is_faithful(surface, C745, baseline)
        and baseline_names == EXPECTED_BASELINE_ATTACK_NAMES
        and baseline["attack_count"] == 26
        and baseline["refused_count"] == 5
        and baseline["surviving_unrefused_mutations"]
        == ["partial_inverse_prefix_6", "partial_inverse_prefix_7"]
    )
    certificate_a = bool(
        pinned
        and before_snapshot == after_snapshot
        and firewall["ok"]
        and C719.K is K719
        and baseline_identity
    )
    certificate_b = bool(
        diagnosis["exact"]
        and diagnosis["payload_stations_affected"] == 744
        and pre["writeback_steps"] == [4, 128, 129]
    )
    inner_rows = [
        row for row in guarded_first["rows"]
        if row["target"] == "record_and_inner_lock"
    ]
    outer_rows = [
        row for row in guarded_first["rows"]
        if row["target"] == "outermost_guard_cells"
    ]
    certificate_c = bool(
        len(guard.primary) == 744
        and len(guard.cells) == 2232
        and all(
            row["refused"]
            and row["record_byte_identical"]
            and row["guard_byte_identical"]
            for row in inner_rows
        )
        and any(not row["refused"] for row in outer_rows)
        and guard_requires_new_law
        and not construction["new_refusal_condition_added"]
        and not construction["outermost_guard_wrapped_atomically"]
    )
    certificate_d = bool(
        baseline_identity
        and guarded_first["manifest_exact"]
        and guarded_first["attack_count"]
        == len(PREREGISTERED_ATTACK_NAMES) == 50
        and outcome == "GUARD_REQUIRES_NEW_LAW"
        and not permanence
    )
    certificate_e = bool(
        controls["fresh_cell_write_succeeds"]
        and controls["modes_0_5_untouched"]
        and controls["pre_finalizer_bit_exact"]
        and controls["lawful_forward_final_bit_exact"]
        and controls["engagement_point"] == 125
        and controls["Cycle745_first_write_certificate"]
        and controls["Cycle745_refusal_certificate"]
        and controls["Cycle745_induction_certificate"]
        and forward["engagement"]["program_kind"] == "finalizer"
        and forward["engagement"]["orbit_step"] == 125
    )

    runtime_sec = perf_counter() - started
    certificates = {
        "A": certificate_a,
        "B": certificate_b,
        "C": certificate_c,
        "D": certificate_d,
        "E": certificate_e,
        "F": False,
    }
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "W6_untouched": True,
        "certificates": certificates,
        "classification_if_no_write_counts":
            "identified" if permanence else "unidentified",
        "classification_if_no_write_does_not_count":
            "partially identified" if permanence else "unidentified",
        "determinism": deterministic,
        "guard_requires_new_law": guard_requires_new_law,
        "missing_condition":
            MISSING_CONDITION if guard_requires_new_law else None,
        "no_probability_rate_or_weight_branch": True,
        "outcome": outcome,
        "permanence_witness_established": permanence,
        "refused_attacks":
            f"{guarded_first['refused_count']}/{guarded_first['attack_count']}",
        "runtime_sec": runtime_sec,
        "stdout_bytes": 0,
    }
    for _ in range(8):
        certificate_f = bool(
            deterministic
            and runtime_sec < AUDIT_TIMEOUT_SEC
            and int(report["stdout_bytes"]) < 150_000
        )
        certificates["F"] = certificate_f
        report["certificates"] = certificates
        certificate_lines, final_line, size = projected_output(
            data_lines, certificates, report
        )
        if size == report["stdout_bytes"]:
            break
        report["stdout_bytes"] = size
    certificates["F"] = bool(
        deterministic
        and runtime_sec < AUDIT_TIMEOUT_SEC
        and int(report["stdout_bytes"]) < 150_000
    )
    report["certificates"] = certificates
    certificate_lines, final_line, size = projected_output(
        data_lines, certificates, report
    )
    if size != report["stdout_bytes"]:
        report["stdout_bytes"] = size
        certificate_lines, final_line, _ = projected_output(
            data_lines, certificates, report
        )

    for line in data_lines:
        print(line)
    for line in certificate_lines:
        print(line)
    print(final_line)
    return 0 if all(certificates.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
