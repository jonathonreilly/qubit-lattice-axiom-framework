#!/usr/bin/env python3
"""Cycle 770: compose the landed refusal lock with the formation census.

The bounded experiment changes neither landed runner.  It sends the exactly
decoded mode-6 EventCell payload through independent bitwise instances of the
Cycle-745 WRITE_WORD.  Thus every payload bit is written and locked by the
same landed word.  The exact Cycle-719 inverse write-backs are then replayed
as in-alphabet write requests against that locked candidate site.
"""

from __future__ import annotations

import ast
from hashlib import sha256
import importlib
import json
from pathlib import Path
import sys
from time import perf_counter
from typing import Any


AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle769_formation_census_2026_07_28.py",
    "scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
EXPECTED_INPUT_SHA256 = {
    "scripts/frontier_cycle769_formation_census_2026_07_28.py":
        "249a9f84eb3a89b2a261801e8e2bb15cc0ba1919a61ac6a8e4c731b3ecaedb32",
    "scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py":
        "d8c1651eb8cdd25a797881b55b81234a5816407418ef415491ecef41672bd708",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py":
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def canonical_digest(value: object) -> str:
    return sha256(canonical_json(value).encode()).hexdigest()


def ast_digest(source: bytes) -> str:
    tree = ast.parse(source.decode("utf-8"))
    dump = ast.dump(tree, annotate_fields=True, include_attributes=False)
    return sha256(dump.encode()).hexdigest()


def input_snapshot() -> dict[str, dict[str, object]]:
    snapshot: dict[str, dict[str, object]] = {}
    for relative in AUDIT_INPUT_PATHS:
        source = (ROOT / relative).read_bytes()
        snapshot[relative] = {
            "bytes": len(source),
            "sha256": sha256(source).hexdigest(),
            "ast_sha256": ast_digest(source),
        }
    return snapshot


def root_name(node: ast.AST) -> str | None:
    cursor = node
    while isinstance(cursor, (ast.Attribute, ast.Subscript)):
        cursor = cursor.value
    return cursor.id if isinstance(cursor, ast.Name) else None


def runner_no_import_mutation_firewall() -> dict[str, object]:
    """Reject syntax that could mutate one of the three imported modules."""
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    protected = {"C769", "C745", "K719"}
    violations: list[str] = []
    for node in ast.walk(tree):
        targets: list[ast.AST] = []
        if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
            if isinstance(node, ast.Assign):
                targets.extend(node.targets)
            else:
                targets.append(node.target)
        elif isinstance(node, ast.Delete):
            targets.extend(node.targets)
        for target in targets:
            if (
                isinstance(target, (ast.Attribute, ast.Subscript))
                and root_name(target) in protected
            ):
                violations.append(f"{type(node).__name__}@{node.lineno}")
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in {"setattr", "delattr"}
            and node.args
            and root_name(node.args[0]) in protected
        ):
            violations.append(f"{node.func.id}@{node.lineno}")
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
    return {
        "ok": not violations and literal_paths == AUDIT_INPUT_PATHS,
        "literal_AUDIT_INPUT_PATHS": literal_paths,
        "protected_module_aliases": sorted(protected),
        "mutation_syntax_violations": violations,
    }


def extract_verbatim_769_tests(source: bytes) -> dict[str, str]:
    """Extract, rather than restate, the four frozen Cycle-769 test clauses."""
    tree = ast.parse(source.decode("utf-8"))
    wanted = {
        "record_shaped_write_test",
        "positive_formation_test",
        "negative_formation_test",
        "reversibility_boundary",
    }
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name)
                and target.id == "operationalization"
                for target in node.targets
            )
            and isinstance(node.value, ast.Dict)
        ):
            extracted: dict[str, str] = {}
            for key_node, value_node in zip(node.value.keys, node.value.values):
                key = ast.literal_eval(key_node)
                if key in wanted:
                    extracted[key] = ast.literal_eval(value_node)
            if set(extracted) == wanted:
                return extracted
    raise RuntimeError("Cycle-769 operationalized test clauses were not found")


def payload_bytes(cell_rows: object) -> bytes:
    return canonical_json(cell_rows).encode("utf-8")


def bytes_to_bits(payload: bytes) -> tuple[int, ...]:
    return tuple(
        (byte >> bit_index) & 1
        for byte in payload
        for bit_index in range(8)
    )


def bits_to_bytes(bits: tuple[int, ...]) -> bytes:
    if len(bits) % 8:
        raise ValueError("payload bit count must be byte aligned")
    output = bytearray()
    for offset in range(0, len(bits), 8):
        value = sum(bits[offset + index] << index for index in range(8))
        output.append(value)
    return bytes(output)


def first_write_payload(
    C745: Any,
    site: tuple[int, int, int],
    content: bytes,
    source_word: str,
) -> tuple[dict[str, object], dict[str, object]]:
    """Tensor the landed one-bit first-write law across exact payload bytes."""
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
    stored = bits_to_bytes(tuple(state[0] for state in persistent))
    accepted = (
        bool(input_bits)
        and all(tag == "ACCEPTED" for tag in tags)
        and all(state[1:] == C745.LOCKED for state in persistent)
        and stored == content
    )
    lock = {
        "site": site,
        "content": stored,
        "persistent": persistent,
    }
    evidence = {
        "accepted": accepted,
        "accepted_bit_count": sum(tag == "ACCEPTED" for tag in tags),
        "content_bytes": len(content),
        "content_sha256": sha256(content).hexdigest(),
        "lock_transfer_in_same_WRITE_WORD": bool(
            C745.ast_same_word_certificate()["ok"]
        ),
        "locked_bit_count": sum(
            state[1:] == C745.LOCKED for state in persistent
        ),
        "payload_bit_count": len(input_bits),
        "site": site,
        "source_word": source_word,
    }
    return lock, evidence


def attempt_payload_write(
    C745: Any,
    lock: dict[str, object],
    offered_content: bytes,
    source_word: str,
) -> tuple[dict[str, object], dict[str, object]]:
    """Present a fixed-width request to every locked payload rail."""
    stored_content = lock["content"]
    persistent_before = lock["persistent"]
    if not isinstance(stored_content, bytes) or not isinstance(
        persistent_before, tuple
    ):
        raise TypeError("invalid internal lock representation")
    if len(offered_content) != len(stored_content):
        raise ValueError("locked payload requests must preserve exact byte width")
    offered_bits = bytes_to_bits(offered_content)
    events = tuple(
        C745.apply_word(
            C745.packet(storage, offered),
            C745.WRITE_WORD,
        )
        for storage, offered in zip(persistent_before, offered_bits)
    )
    persistent_after = tuple(C745.persistent(event) for event in events)
    tags = tuple(C745.output_tag(event) for event in events)
    content_after = bits_to_bytes(
        tuple(storage[0] for storage in persistent_after)
    )
    q_refuse = tuple(
        event[C745.RAIL_INDEX["Q_refuse"]] for event in events
    )
    q_in = tuple(event[C745.RAIL_INDEX["Q_in"]] for event in events)
    q_accept = tuple(
        event[C745.RAIL_INDEX["Q_accept"]] for event in events
    )
    refused = (
        all(tag == "REFUSED" for tag in tags)
        and all(q_refuse)
        and not any(q_in)
        and not any(q_accept)
        and persistent_after == persistent_before
        and content_after == stored_content
    )
    after_lock = {
        "site": lock["site"],
        "content": content_after,
        "persistent": persistent_after,
    }
    receipt = {
        "content_survives_byte_exactly": content_after == stored_content,
        "offered_sha256": sha256(offered_content).hexdigest(),
        "payload_bit_count": len(offered_bits),
        "q_accept_count": sum(q_accept),
        "q_in_count": sum(q_in),
        "q_refuse_count": sum(q_refuse),
        "q_refuse_sha256": sha256(bytes(q_refuse)).hexdigest(),
        "refused": refused,
        "refused_bit_count": sum(tag == "REFUSED" for tag in tags),
        "site": lock["site"],
        "source_word": source_word,
        "stored_sha256_after": sha256(content_after).hexdigest(),
        "stored_sha256_before": sha256(stored_content).hexdigest(),
    }
    return after_lock, receipt


def controller_data(C719: Any, full: int) -> int:
    return int(C719.controller_register_rows(full)["data"])


def replace_controller_data(C719: Any, full: int, data: int) -> int:
    return (full & ~C719.CONTROLLER_DATA_MASK) | data


def source_for_mode(C769: Any, mode: int) -> int:
    candidates = [
        source
        for source in C769.initial_origin_zero_branches()
        if (source & 4095).bit_length() - 1 == mode
    ]
    if len(candidates) != 1:
        raise RuntimeError(f"expected one origin-zero mode-{mode} branch")
    return candidates[0]


def forward_mode6_with_lock(
    C769: Any,
    C745: Any,
    pointer_site: tuple[int, int, int],
) -> dict[str, object]:
    C719 = C769.C719
    source = source_for_mode(C769, 6)
    initial_full = C719.controller_full_input(source)
    full = initial_full
    writes: list[dict[str, object]] = []
    lock: dict[str, object] | None = None
    engagement: dict[str, object] | None = None
    for orbit_step in range(C719.CONTROLLER_STATIONS):
        before_registers = C719.controller_register_rows(full)
        before_data = int(before_registers["data"])
        live_a = tuple(
            index
            for index, value in enumerate(before_registers["A"])
            if value
        )
        full = C719.apply_fast_int(full, C719.CONTROLLER_H_FAST)
        after_data = controller_data(C719, full)
        if before_data == after_data:
            continue
        station = live_a[0] if len(live_a) == 1 else None
        kind = C719.PROGRAM[station][0] if station is not None else None
        decoded = C769.decoded_cell_surface(after_data)
        rows = list(decoded["cell_rows"])
        writes.append({
            "accepted_EventCell_present_after": bool(rows),
            "changed_data_bits": (before_data ^ after_data).bit_count(),
            "orbit_step": orbit_step,
            "program_kind": kind,
            "station": station,
        })
        accepted_shape = bool(rows) and all(
            row["binder"] == row["valid"] == 1 for row in rows
        )
        if accepted_shape and lock is None:
            content = payload_bytes(rows)
            lock, engagement = first_write_payload(
                C745,
                pointer_site,
                content,
                "Cycle719 finalizer decoded EventCell",
            )
            engagement["orbit_step"] = orbit_step
            engagement["program_kind"] = kind
            engagement["content_hex"] = content.hex()
    if lock is None or engagement is None:
        raise RuntimeError("mode 6 produced no exactly decodable EventCell to lock")
    return {
        "engagement": engagement,
        "final_full": full,
        "forward_writes": writes,
        "initial_full": initial_full,
        "lock": lock,
        "source": source,
    }


def pre_composition_inverse(C769: Any, forward: dict[str, object]) -> dict[str, object]:
    C719 = C769.C719
    full = int(forward["final_full"])
    initial_full = int(forward["initial_full"])
    writebacks: list[dict[str, object]] = []
    for orbit_step in range(C719.CONTROLLER_STATIONS):
        before_data = controller_data(C719, full)
        attempted = C719.apply_fast_int(full, C719.CONTROLLER_H_INVERSE_FAST)
        after_registers = C719.controller_register_rows(attempted)
        after_data = int(after_registers["data"])
        if before_data != after_data:
            live_a = tuple(
                index
                for index, value in enumerate(after_registers["A"])
                if value
            )
            station = live_a[0] if len(live_a) == 1 else None
            before_rows = list(
                C769.decoded_cell_surface(before_data)["cell_rows"]
            )
            after_rows = list(
                C769.decoded_cell_surface(after_data)["cell_rows"]
            )
            writebacks.append({
                "EventCell_present_after": bool(after_rows),
                "EventCell_present_before": bool(before_rows),
                "changed_data_bits": (before_data ^ after_data).bit_count(),
                "orbit_step": orbit_step,
                "program_kind": (
                    C719.PROGRAM[station][0] if station is not None else None
                ),
                "station": station,
            })
        full = attempted
    return {
        "bare_inverse_unwrites_exactly": full == initial_full,
        "inverse_applications": C719.CONTROLLER_STATIONS,
        "restored_controller_full_sha256": sha256(
            full.to_bytes((full.bit_length() + 7) // 8, "little")
        ).hexdigest(),
        "writeback_steps": [row["orbit_step"] for row in writebacks],
        "writebacks": writebacks,
    }


def post_composition_inverse(
    C769: Any,
    C745: Any,
    forward: dict[str, object],
    pre: dict[str, object],
) -> dict[str, object]:
    """Attack sequential composition and replay every bare write-back request."""
    C719 = C769.C719
    bare = int(forward["final_full"])
    composed = int(forward["final_full"])
    final_data = controller_data(C719, composed)
    lock = dict(forward["lock"])
    original_payload = lock["content"]
    if not isinstance(original_payload, bytes):
        raise TypeError("invalid locked payload")
    replay_receipts: list[dict[str, object]] = []
    sequential_mutation_attempt_steps: list[int] = []
    first_failure_step: int | None = None

    for orbit_step in range(C719.CONTROLLER_STATIONS):
        bare_before_data = controller_data(C719, bare)
        bare_attempted = C719.apply_fast_int(
            bare, C719.CONTROLLER_H_INVERSE_FAST
        )
        bare_after_data = controller_data(C719, bare_attempted)
        if bare_before_data != bare_after_data:
            after_rows = list(
                C769.decoded_cell_surface(bare_after_data)["cell_rows"]
            )
            if after_rows:
                proposed = payload_bytes(after_rows)
                if len(proposed) != len(original_payload):
                    raise RuntimeError(
                        "inverse proposed a differently sized EventCell payload"
                    )
                proposal_kind = "replacement_EventCell"
            else:
                proposed = bytes(len(original_payload))
                proposal_kind = "unwrite_to_blank"
            lock, receipt = attempt_payload_write(
                C745,
                lock,
                proposed,
                f"Cycle719 compiled inverse orbit step {orbit_step}",
            )
            receipt["bare_changed_data_bits"] = (
                bare_before_data ^ bare_after_data
            ).bit_count()
            receipt["orbit_step"] = orbit_step
            receipt["proposal_kind"] = proposal_kind
            replay_receipts.append(receipt)
            if not receipt["refused"] and first_failure_step is None:
                first_failure_step = orbit_step
        bare = bare_attempted

        composed_before_data = controller_data(C719, composed)
        composed_attempted = C719.apply_fast_int(
            composed, C719.CONTROLLER_H_INVERSE_FAST
        )
        composed_after_data = controller_data(C719, composed_attempted)
        if composed_before_data != composed_after_data:
            sequential_mutation_attempt_steps.append(orbit_step)
            matching = next(
                (
                    receipt
                    for receipt in replay_receipts
                    if receipt["orbit_step"] == orbit_step
                ),
                None,
            )
            refused = bool(matching and matching["refused"])
            if refused:
                composed = replace_controller_data(
                    C719, composed_attempted, composed_before_data
                )
            else:
                composed = composed_attempted
                if first_failure_step is None:
                    first_failure_step = orbit_step
        else:
            composed = composed_attempted

    surviving_data = controller_data(C719, composed)
    surviving_rows = list(
        C769.decoded_cell_surface(surviving_data)["cell_rows"]
    )
    surviving_payload = payload_bytes(surviving_rows)
    all_refused = (
        len(replay_receipts) == len(pre["writebacks"])
        and all(receipt["refused"] for receipt in replay_receipts)
    )
    return {
        "all_bare_writebacks_refused": all_refused,
        "bare_inverse_shadow_still_exact": bare == int(forward["initial_full"]),
        "bare_writeback_steps_replayed": [
            receipt["orbit_step"] for receipt in replay_receipts
        ],
        "composed_data_survives_byte_exactly": surviving_data == final_data,
        "composed_EventCell_hex_after": surviving_payload.hex(),
        "composed_EventCell_hex_before": original_payload.hex(),
        "EventCell_survives_byte_exactly": surviving_payload == original_payload,
        "first_refusal_failure_step": first_failure_step,
        "inverse_applications": C719.CONTROLLER_STATIONS,
        "replay_receipts": replay_receipts,
        "sequential_composed_mutation_attempt_steps":
            sequential_mutation_attempt_steps,
        "syndrome_receipt_count": sum(
            bool(receipt["q_refuse_count"]) for receipt in replay_receipts
        ),
    }


def run_composed_census(
    C769: Any,
    C745: Any,
    compiled_anchor: dict[str, object],
    pointer_site: tuple[int, int, int],
    post_attack: dict[str, object],
    hostile_battery: dict[str, object],
    verbatim_tests: dict[str, str],
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    """Rerun the complete 769 census, then engage the lock only when shaped."""
    raw_rows = C769.run_census(compiled_anchor, pointer_site)
    composed_rows: list[dict[str, object]] = []
    for raw in raw_rows:
        row = dict(raw)
        mode = int(row["source_matter_mode"])
        record_shaped = bool(row["reversible_record_shaped_write"])
        row["orbit_steps_scanned"] = C769.C719.CONTROLLER_STATIONS
        row["full_orbit_exhaustive"] = True
        if record_shaped:
            rows = list(row["decoded_EventCell_rows"])
            lock, engagement = first_write_payload(
                C745,
                pointer_site,
                payload_bytes(rows),
                "Cycle719 finalizer decoded EventCell",
            )
            del lock
            positive = bool(
                engagement["accepted"]
                and engagement["lock_transfer_in_same_WRITE_WORD"]
                and post_attack["all_bare_writebacks_refused"]
                and post_attack["EventCell_survives_byte_exactly"]
                and hostile_battery["all_attacks_refused_with_syndrome"]
                and not hostile_battery["witness_refuted"]
            )
            row["lock_composition"] = {
                "engaged": bool(engagement["accepted"]),
                "engagement": engagement,
                "full_inverse_refusal_passed": bool(
                    post_attack["all_bare_writebacks_refused"]
                    and post_attack["EventCell_survives_byte_exactly"]
                ),
                "hostile_battery_passed": bool(
                    hostile_battery["all_attacks_refused_with_syndrome"]
                ),
                "physical_law": (
                    "Cycle745 WRITE_WORD same-word lock transfer plus its "
                    "locked-request refusal and finite-alphabet induction"
                ),
                "survival_attack_passed": bool(
                    post_attack["all_bare_writebacks_refused"]
                    and post_attack["EventCell_survives_byte_exactly"]
                    and hostile_battery["all_attacks_refused_with_syndrome"]
                ),
            }
            row["durable_permanent_record_write"] = positive or None
            row["formation_witness"] = {
                "decision": True if positive else None,
                "negative_nonformation": None,
                "physical_law": row["lock_composition"]["physical_law"],
                "positive_permanent_lock": positive or None,
                "standard_clause_satisfied": (
                    verbatim_tests["positive_formation_test"]
                    if positive
                    else None
                ),
            }
            row["formation_decision"] = True if positive else None
        else:
            row["lock_composition"] = {
                "engaged": False,
                "reason": "no record-shaped write; nothing to lock",
            }
            row["durable_permanent_record_write"] = None
            row["formation_witness"] = {
                "decision": None,
                "negative_nonformation": None,
                "positive_permanent_lock": None,
                "reason": (
                    "No record-shaped output exists; whether the exhaustive "
                    "no-write census is a landed negative is evaluated under "
                    "both requested readings."
                ),
            }
            row["formation_decision"] = None
        row["composition_scope"] = (
            "Cycle745 bitwise tensor at the one candidate EventCell site"
        )
        row["source_matter_mode"] = mode
        composed_rows.append(row)
    return composed_rows, raw_rows


def dual_classification(
    C769: Any,
    composed_rows: list[dict[str, object]],
) -> dict[str, object]:
    mode6 = next(
        row for row in composed_rows if row["source_matter_mode"] == 6
    )
    no_write_rows = [
        row for row in composed_rows if row["source_matter_mode"] != 6
    ]
    mode6_positive = mode6["formation_decision"] is True
    exhaustive_no_write = all(
        row["full_orbit_exhaustive"]
        and row["orbit_steps_scanned"] == C769.C719.CONTROLLER_STATIONS
        and not row["reversible_record_shaped_write"]
        and row["data_write_points"] == []
        and row["record_cell_pipeline_points"] == []
        for row in no_write_rows
    )

    counts_rows: list[dict[str, object]] = []
    does_not_count_rows: list[dict[str, object]] = []
    for row in composed_rows:
        record_shaped = bool(row["reversible_record_shaped_write"])
        positive = row["formation_decision"] is True
        counts_decision: bool | None
        neutral_decision: bool | None
        if positive:
            counts_decision = neutral_decision = True
        elif not record_shaped and exhaustive_no_write:
            counts_decision = False
            neutral_decision = None
        else:
            counts_decision = neutral_decision = None
        counts_rows.append({"formation_decision": counts_decision})
        does_not_count_rows.append({"formation_decision": neutral_decision})

    counts_label, counts_evidence = C769.classify_formation_census(
        counts_rows
    )
    neutral_label, neutral_evidence = C769.classify_formation_census(
        does_not_count_rows
    )
    return {
        "classification_if_no_write_counts": counts_label,
        "classification_if_no_write_does_not_count": neutral_label,
        "evidence_if_no_write_counts": counts_evidence,
        "evidence_if_no_write_does_not_count": neutral_evidence,
        "rule_text": counts_evidence["classification_rule"],
        "subquestion_a": {
            "does_mode6_now_carry_positive_permanence_evidence":
                mode6_positive,
            "answer": mode6_positive,
        },
        "subquestion_b": {
            "does_exhaustive_no_write_count_as_landed_negative": {
                "if_counts_reading": bool(exhaustive_no_write),
                "if_does_not_count_reading": False,
            },
            "exhaustive_full_orbit_no_record_shaped_write_modes_0_2_3_4_5":
                exhaustive_no_write,
            "modes": [0, 2, 3, 4, 5],
        },
    }


def control_experiments(
    C745: Any,
    pointer_site: tuple[int, int, int],
    forward: dict[str, object],
) -> dict[str, object]:
    original_lock = dict(forward["lock"])
    content = original_lock["content"]
    if not isinstance(content, bytes):
        raise TypeError("invalid lock content")
    hostile_payload = bytes(byte ^ 0xFF for byte in content)
    _hostile_lock, hostile_receipt = attempt_payload_write(
        C745,
        original_lock,
        hostile_payload,
        "foreign hostile word",
    )
    fresh_site = (
        pointer_site[0],
        pointer_site[1],
        pointer_site[2] + 1,
    )
    _fresh_lock, fresh_evidence = first_write_payload(
        C745,
        fresh_site,
        content,
        "fresh-cell control word",
    )
    cert_b_ok, cert_b = C745.certificate_b()
    cert_c_ok, cert_c = C745.certificate_c()
    cert_d_ok, cert_d = C745.certificate_d()
    return {
        "Cycle745_same_word_certificate": cert_b_ok,
        "Cycle745_refusal_certificate": cert_c_ok,
        "Cycle745_induction_certificate": cert_d_ok,
        "Cycle745_certificate_details_sha256": canonical_digest({
            "B": cert_b,
            "C": cert_c,
            "D": cert_d,
        }),
        "fresh_cell_first_write": fresh_evidence,
        "fresh_cell_write_succeeds": bool(fresh_evidence["accepted"]),
        "hostile_foreign_write": hostile_receipt,
        "hostile_write_refused": bool(hostile_receipt["refused"]),
        "lock_does_not_overblock": bool(fresh_evidence["accepted"]),
    }


def apply_hostile_payload_word(
    C745: Any,
    pristine: tuple[tuple[int, int, int], ...],
    offered_content: bytes,
    word: tuple[Any, ...],
    *,
    family: str,
    name: str,
) -> tuple[tuple[tuple[int, int, int], ...], dict[str, object]]:
    """Apply one checker-defined hostile word to every payload lock rail."""
    offered_bits = bytes_to_bits(offered_content)
    if len(pristine) != len(offered_bits):
        raise ValueError("hostile payload width differs from locked width")
    events = tuple(
        C745.apply_word(C745.packet(storage, offered), word)
        for storage, offered in zip(pristine, offered_bits)
    )
    after = tuple(C745.persistent(event) for event in events)
    tags = tuple(C745.output_tag(event) for event in events)
    q_in = tuple(
        event[C745.RAIL_INDEX["Q_in"]] for event in events
    )
    q_accept = tuple(
        event[C745.RAIL_INDEX["Q_accept"]] for event in events
    )
    q_refuse = tuple(
        event[C745.RAIL_INDEX["Q_refuse"]] for event in events
    )
    content_after = bits_to_bytes(
        tuple(storage[0] for storage in after)
    )
    content_before = bits_to_bytes(
        tuple(storage[0] for storage in pristine)
    )
    syndrome = (
        all(tag == "REFUSED" for tag in tags)
        and all(q_refuse)
        and not any(q_in)
        and not any(q_accept)
    )
    lock_exact = after == pristine
    receipt = {
        "content_byte_identical": content_after == content_before,
        "content_sha256_after": sha256(content_after).hexdigest(),
        "content_sha256_before": sha256(content_before).hexdigest(),
        "family": family,
        "gate_names": [gate.name for gate in word],
        "lock_rail_mutations": sum(
            observed != expected
            for observed, expected in zip(after, pristine)
        ),
        "lock_state_identical": lock_exact,
        "mutation": after != pristine,
        "name": name,
        "offered_sha256": sha256(offered_content).hexdigest(),
        "q_accept_count": sum(q_accept),
        "q_in_count": sum(q_in),
        "q_refuse_count": sum(q_refuse),
        "refused": syndrome and lock_exact,
        "refused_bit_count": sum(tag == "REFUSED" for tag in tags),
        "syndrome_receipt": syndrome,
        "word_gate_count": len(word),
    }
    return after, receipt


def mode6_forward_replay_attack(
    C769: Any,
    C745: Any,
    forward: dict[str, object],
    pristine: tuple[tuple[int, int, int], ...],
    original_content: bytes,
) -> dict[str, object]:
    """Replay the complete mode-6 word as a double-write request."""
    C719 = C769.C719
    full = int(forward["final_full"])
    before_data = controller_data(C719, full)
    change_steps: list[dict[str, int]] = []
    for orbit_step in range(C719.CONTROLLER_STATIONS):
        previous = controller_data(C719, full)
        full = C719.apply_fast_int(full, C719.CONTROLLER_H_FAST)
        observed = controller_data(C719, full)
        if previous != observed:
            change_steps.append({
                "changed_data_bits": (previous ^ observed).bit_count(),
                "orbit_step": orbit_step,
            })
    after_data = controller_data(C719, full)
    rows = list(C769.decoded_cell_surface(after_data)["cell_rows"])
    proposed = payload_bytes(rows)
    _after, receipt = apply_hostile_payload_word(
        C745,
        pristine,
        proposed,
        C745.WRITE_WORD,
        family="mode6_forward_word_replay",
        name="mode6_forward_word_replay_double_write",
    )
    receipt.update({
        "bare_controller_changed_bits": (
            before_data ^ after_data
        ).bit_count(),
        "bare_controller_change_steps": change_steps,
        "decoded_proposal_equals_locked_content":
            proposed == original_content,
    })
    return receipt


def direct_bank_station_attacks(
    C769: Any,
    K719: Any,
    forward: dict[str, object],
    original_content: bytes,
) -> list[dict[str, object]]:
    """Apply every landed bank macro directly, outside the lock request port."""
    C719 = C769.C719
    data_before = controller_data(C719, int(forward["final_full"]))
    tuple_before = C719.int_to_tuple(data_before)
    candidate_site = tuple(
        C719.M.R12.full_wire_layout()["wire_sites"][
            C719.R3_SOURCE_POINTER()
        ]
    )
    results: list[dict[str, object]] = []
    for station, program_row in enumerate(C719.PROGRAM):
        if program_row[0] != "bank":
            continue
        word = K719.mapped_macro(program_row)
        tuple_after = K719.A.apply_semantic(tuple_before, word)
        data_after = C719.tuple_to_int(tuple_after)
        rows_after = list(
            C769.decoded_cell_surface(data_after)["cell_rows"]
        )
        content_after = payload_bytes(rows_after)
        results.append({
            "bank": int(program_row[1]),
            "bare_controller_changed_bits": (
                data_before ^ data_after
            ).bit_count(),
            "content_byte_identical":
                content_after == original_content,
            "family": "direct_bank_station",
            "lock_rail_mutations": 0,
            "lock_state_identical": True,
            "macro_gate_count": len(word),
            "mutation": content_after != original_content,
            "name": f"direct_bank_station_{station}",
            "q_accept_count": 0,
            "q_in_count": 0,
            "q_refuse_count": 0,
            "refused": False,
            "site": candidate_site,
            "station": station,
            "syndrome_receipt": False,
        })
    return results


def hostile_word_battery(
    C769: Any,
    C745: Any,
    K719: Any,
    forward: dict[str, object],
) -> dict[str, object]:
    """Reproduce the independent checker's complete 26-attack family."""
    lock = forward["lock"]
    if not isinstance(lock, dict):
        raise TypeError("mode-6 composition did not produce a lock")
    content = lock["content"]
    pristine = lock["persistent"]
    if not isinstance(content, bytes) or not isinstance(pristine, tuple):
        raise TypeError("invalid mode-6 lock representation")
    complement = bytes(byte ^ 0xFF for byte in content)
    attacks: list[dict[str, object]] = []

    current = pristine
    for application in (1, 2):
        current, receipt = apply_hostile_payload_word(
            C745,
            current,
            complement,
            C745.REVERSE_WRITE_WORD,
            family="inverse_word_twice",
            name=f"inverse_word_application_{application}",
        )
        attacks.append(receipt)

    for length in range(1, len(C745.REVERSE_WRITE_WORD)):
        _after, receipt = apply_hostile_payload_word(
            C745,
            pristine,
            complement,
            C745.REVERSE_WRITE_WORD[:length],
            family="partial_inverse_prefix",
            name=f"partial_inverse_prefix_{length}",
        )
        receipt["last_gate"] = C745.REVERSE_WRITE_WORD[length - 1].name
        attacks.append(receipt)

    attacks.append(mode6_forward_replay_attack(
        C769, C745, forward, pristine, content
    ))

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
        _after, receipt = apply_hostile_payload_word(
            C745,
            pristine,
            offered,
            macro_words[macro],
            family="declared_alphabet_foreign_content",
            name=f"declared_alphabet_{macro}",
        )
        receipt["macro"] = macro
        attacks.append(receipt)

    attacks.extend(
        direct_bank_station_attacks(C769, K719, forward, content)
    )
    mutations = [
        row["name"] for row in attacks
        if row["mutation"] and not row["refused"]
    ]
    return {
        "all_attacks_refused_with_syndrome": all(
            row["refused"]
            and row["syndrome_receipt"]
            and row["content_byte_identical"]
            for row in attacks
        ),
        "attack_count": len(attacks),
        "attacks": attacks,
        "locked_content_hex": content.hex(),
        "locked_content_sha256": sha256(content).hexdigest(),
        "payload_bit_count": len(pristine),
        "refused_count": sum(bool(row["refused"]) for row in attacks),
        "surviving_unrefused_mutations": mutations,
        "witness_refuted": bool(mutations),
    }


def battery_family_is_faithful(
    C769: Any,
    C745: Any,
    battery: dict[str, object],
) -> bool:
    attacks = list(battery["attacks"])
    expected_names = (
        ["inverse_word_application_1", "inverse_word_application_2"]
        + [
            f"partial_inverse_prefix_{length}"
            for length in range(1, len(C745.REVERSE_WRITE_WORD))
        ]
        + ["mode6_forward_word_replay_double_write"]
        + [
            f"declared_alphabet_{macro}"
            for macro in C745.ALPHABET_SCOPE
        ]
        + [
            f"direct_bank_station_{station}"
            for station, row in enumerate(C769.C719.PROGRAM)
            if row[0] == "bank"
        ]
    )
    families = [row["family"] for row in attacks]
    return (
        battery["attack_count"] == len(expected_names) == 26
        and [row["name"] for row in attacks] == expected_names
        and families.count("inverse_word_twice") == 2
        and families.count("partial_inverse_prefix") == 7
        and families.count("mode6_forward_word_replay") == 1
        and families.count("declared_alphabet_foreign_content") == 4
        and families.count("direct_bank_station") == 12
    )


def main() -> int:
    started = perf_counter()
    before_snapshot = input_snapshot()
    firewall = runner_no_import_mutation_firewall()
    source_769 = (
        ROOT / AUDIT_INPUT_PATHS[0]
    ).read_bytes()
    verbatim_tests = extract_verbatim_769_tests(source_769)

    C769 = importlib.import_module(
        "frontier_cycle769_formation_census_2026_07_28"
    )
    C745 = importlib.import_module(
        "frontier_cycle745_enforced_dual_rail_lock_2026_07_28"
    )
    K719 = importlib.import_module(
        "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
    )

    pointer_site = tuple(
        C769.C719.M.R12.full_wire_layout()["wire_sites"][
            C769.C719.R3_SOURCE_POINTER()
        ]
    )
    compiled_anchor = C769.C719.compiled_H_orbit_certificate()
    anchor_by_mode = {
        int(row["source_matter_mode"]): row
        for row in compiled_anchor["rows"]
    }

    forward = forward_mode6_with_lock(C769, C745, pointer_site)
    pre = pre_composition_inverse(C769, forward)
    post = post_composition_inverse(C769, C745, forward, pre)
    battery = hostile_word_battery(C769, C745, K719, forward)
    battery_rerun = hostile_word_battery(C769, C745, K719, forward)

    baseline_rows = C769.run_census(compiled_anchor, pointer_site)
    composed_first, composed_first_raw = run_composed_census(
        C769,
        C745,
        compiled_anchor,
        pointer_site,
        post,
        battery,
        verbatim_tests,
    )
    composed_second, composed_second_raw = run_composed_census(
        C769,
        C745,
        compiled_anchor,
        pointer_site,
        post,
        battery,
        verbatim_tests,
    )
    first_census_sha = canonical_digest(composed_first)
    second_census_sha = canonical_digest(composed_second)
    classifications = dual_classification(C769, composed_first)
    controls = control_experiments(C745, pointer_site, forward)

    expected_modes = [0, 2, 3, 4, 5, 6]
    observed_modes = [
        int(row["source_matter_mode"]) for row in composed_first
    ]
    baseline_by_mode = {
        int(row["source_matter_mode"]): row for row in baseline_rows
    }
    first_raw_by_mode = {
        int(row["source_matter_mode"]): row for row in composed_first_raw
    }
    second_raw_by_mode = {
        int(row["source_matter_mode"]): row for row in composed_second_raw
    }
    no_write_modes_unchanged = all(
        baseline_by_mode[mode] == first_raw_by_mode[mode]
        == second_raw_by_mode[mode]
        and first_raw_by_mode[mode]["data_write_points"] == []
        and first_raw_by_mode[mode]["record_cell_pipeline_points"] == []
        and not first_raw_by_mode[mode]["reversible_record_shaped_write"]
        for mode in (0, 2, 3, 4, 5)
    )
    mode6_row = next(
        row for row in composed_first if row["source_matter_mode"] == 6
    )
    census_exhaustive = (
        observed_modes == expected_modes
        and all(
            row["orbit_steps_scanned"] == C769.C719.CONTROLLER_STATIONS
            and row["full_orbit_exhaustive"]
            for row in composed_first
        )
        and no_write_modes_unchanged
        and mode6_row["reversible_record_shaped_write"]
        and mode6_row["decoded_EventCell_rows"]
        == [{
            "identity": 0,
            "rotor": 15,
            "carry": 0,
            "predecessor": None,
            "binder": 1,
            "valid": 1,
            "orientation": 1,
        }]
    )
    deterministic = (
        composed_first == composed_second
        and composed_first_raw == composed_second_raw
        and first_census_sha == second_census_sha
        and battery == battery_rerun
    )

    after_snapshot = input_snapshot()
    pinned_hashes = all(
        before_snapshot[path]["sha256"] == EXPECTED_INPUT_SHA256[path]
        for path in AUDIT_INPUT_PATHS
    )
    certificate_a = (
        pinned_hashes
        and before_snapshot == after_snapshot
        and bool(firewall["ok"])
        and C769.K is K719
        and C769.C719.K is K719
    )
    certificate_b = (
        bool(pre["bare_inverse_unwrites_exactly"])
        and pre["writeback_steps"] == [4, 128, 129]
        and [
            row["changed_data_bits"] for row in pre["writebacks"]
        ] == [3, 32, 3]
        and bool(anchor_by_mode[6]["inverse_exact"])
    )
    expected_payload_bits = int(forward["engagement"]["payload_bit_count"])
    prefix_mutations = [
        {
            "lock_rail_mutations": row["lock_rail_mutations"],
            "prefix_length": int(str(row["name"]).rsplit("_", 1)[1]),
        }
        for row in battery["attacks"]
        if row["family"] == "partial_inverse_prefix"
        and row["mutation"]
        and not row["refused"]
    ]
    full_inverse_attacks = [
        row for row in battery["attacks"]
        if row["family"] == "inverse_word_twice"
    ]
    certificate_c = (
        bool(forward["engagement"]["accepted"])
        and forward["engagement"]["orbit_step"] == 125
        and forward["engagement"]["program_kind"] == "finalizer"
        and battery_family_is_faithful(C769, C745, battery)
        and battery["attack_count"] == 26
        and battery["refused_count"] == 5
        and battery["payload_bit_count"] == expected_payload_bits == 744
        and battery["witness_refuted"]
        and not battery["all_attacks_refused_with_syndrome"]
        and battery["surviving_unrefused_mutations"]
        == ["partial_inverse_prefix_6", "partial_inverse_prefix_7"]
        and prefix_mutations == [
            {"lock_rail_mutations": 744, "prefix_length": 6},
            {"lock_rail_mutations": 744, "prefix_length": 7},
        ]
        and len(full_inverse_attacks) == 2
        and all(
            receipt["refused"]
            and not receipt["mutation"]
            and receipt["lock_rail_mutations"] == 0
            for receipt in full_inverse_attacks
        )
        and bool(post["all_bare_writebacks_refused"])
        and bool(post["EventCell_survives_byte_exactly"])
        and bool(post["composed_data_survives_byte_exactly"])
        and post["first_refusal_failure_step"] is None
        and post["bare_writeback_steps_replayed"] == [4, 128, 129]
        and post["syndrome_receipt_count"] == 3
        and all(
            receipt["q_refuse_count"] == expected_payload_bits
            and receipt["refused_bit_count"] == expected_payload_bits
            for receipt in post["replay_receipts"]
        )
        and controls["Cycle745_same_word_certificate"]
        and controls["Cycle745_refusal_certificate"]
        and controls["Cycle745_induction_certificate"]
    )
    certificate_d = census_exhaustive
    certificate_e = (
        classifications["rule_text"]
        == classifications[
            "evidence_if_no_write_does_not_count"
        ]["classification_rule"]
        and classifications["subquestion_a"][
            "does_mode6_now_carry_positive_permanence_evidence"
        ] is False
        and classifications["subquestion_b"][
            "exhaustive_full_orbit_no_record_shaped_write_modes_0_2_3_4_5"
        ]
        and classifications["classification_if_no_write_counts"]
        == "unidentified"
        and classifications[
            "classification_if_no_write_does_not_count"
        ] == "unidentified"
    )

    census_summary = [
        {
            "data_write_steps": [
                point["orbit_step"] for point in row["data_write_points"]
            ],
            "formation_decision": row["formation_decision"],
            "lock_engaged": row["lock_composition"]["engaged"],
            "mode": row["source_matter_mode"],
            "record_shaped_write": row["reversible_record_shaped_write"],
        }
        for row in composed_first
    ]
    anchor_print = {
        path: {
            "ast_sha256": before_snapshot[path]["ast_sha256"],
            "sha256": before_snapshot[path]["sha256"],
        }
        for path in AUDIT_INPUT_PATHS
    }
    failure_mechanism = (
        "truncated reverse prefixes mutate the lock rails without refusal"
    )
    repair_target_open_work = (
        "a prefix-closed refusal law (refusal must engage on every prefix of "
        "every un-writing word) or rail-guarded locking (the lock's own state "
        "protected by the same refusal law it enforces); the landed Cycle-745 "
        "lock object would have to change, and neither exists on the landed "
        "surface today"
    )
    battery_summary = {
        key: battery[key]
        for key in (
            "all_attacks_refused_with_syndrome",
            "attack_count",
            "payload_bit_count",
            "refused_count",
            "surviving_unrefused_mutations",
            "witness_refuted",
        )
    }
    data_lines = [
        "permanence_witness_established: false",
        (
            f"refused_attacks: {battery['refused_count']}"
            f"/{battery['attack_count']}"
        ),
        "failure_mechanism: " + json.dumps(failure_mechanism),
        (
            "truncated_reverse_prefix_mutations: "
            + canonical_json(prefix_mutations)
        ),
        (
            "classification_if_no_write_counts: "
            + classifications["classification_if_no_write_counts"]
        ),
        (
            "classification_if_no_write_does_not_count: "
            + classifications[
                "classification_if_no_write_does_not_count"
            ]
        ),
        "repair_target_open_work: " + json.dumps(repair_target_open_work),
        "SHA256_AST_ANCHORS " + canonical_json(anchor_print),
        "OPERATIONALIZATION_VERBATIM " + canonical_json(verbatim_tests),
        "PRE_COMPOSITION_INVERSE " + canonical_json(pre),
        "POST_COMPOSITION_INVERSE " + canonical_json(post),
        "HOSTILE_BATTERY_SUMMARY " + canonical_json(battery_summary),
    ]
    data_lines.extend(
        "HOSTILE_BATTERY_FINDING " + canonical_json({
            "lock_rail_mutations": row["lock_rail_mutations"],
            "mutation": row["mutation"],
            "name": row["name"],
            "refused": row["refused"],
        })
        for row in battery["attacks"]
    )
    data_lines.extend([
        "COMPOSED_SIX_BRANCH_CENSUS " + canonical_json({
            "census_sha256": first_census_sha,
            "rows": census_summary,
        }),
        "DUAL_READING_CLASSIFICATION " + canonical_json(classifications),
        "CONTROLS " + canonical_json(controls),
    ])

    runtime_sec = perf_counter() - started
    controls_pass = (
        controls["hostile_write_refused"]
        and controls["fresh_cell_write_succeeds"]
        and controls["lock_does_not_overblock"]
    )
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
        "audit_timeout_sec": AUDIT_TIMEOUT_SEC,
        "certificates": certificates,
        "classification_if_no_write_counts":
            classifications["classification_if_no_write_counts"],
        "classification_if_no_write_does_not_count":
            classifications["classification_if_no_write_does_not_count"],
        "composed_census": composed_first,
        "controls": controls,
        "failure_mechanism": failure_mechanism,
        "hostile_battery": battery,
        "permanence_witness_established": False,
        "refused_attacks": (
            f"{battery['refused_count']}/{battery['attack_count']}"
        ),
        "repair_target_open_work": repair_target_open_work,
        "truncated_reverse_prefix_mutations": prefix_mutations,
        "determinism": {
            "byte_identical": deterministic,
            "first_census_sha256": first_census_sha,
            "rerun_census_sha256": second_census_sha,
        },
        "formation_subquestions": {
            "a": classifications["subquestion_a"],
            "b": classifications["subquestion_b"],
        },
        "input_firewall": {
            "after": after_snapshot,
            "before": before_snapshot,
            "runner_AST": firewall,
        },
        "no_fitted_constants": True,
        "no_probability_weights_or_rate_law": True,
        "operationalization_verbatim": verbatim_tests,
        "pass": False,
        "post_composition_inverse": post,
        "pre_composition_inverse": pre,
        "runtime_sec": runtime_sec,
        "stdout_bytes": 0,
        "W6_untouched": True,
    }

    certificate_labels = {
        "A": "landed_769_745_719_imported_unchanged_SHA_AST_firewall",
        "B": "pre_composition_inverse_unwrite_reproduced",
        "C": "corrected_26_attack_battery_refutation",
        "D": "six_branch_recensus_exhaustive_modes_0_2_3_4_5_unchanged",
        "E": "dual_reading_recompute_both_unidentified",
        "F": "controls_determinism_runtime_stdout_bounds",
    }
    for _ in range(8):
        certificate_f = bool(
            controls_pass
            and deterministic
            and runtime_sec < AUDIT_TIMEOUT_SEC
            and int(report["stdout_bytes"]) < 150_000
        )
        certificates["F"] = certificate_f
        report["certificates"] = certificates
        report["pass"] = all(certificates.values())
        certificate_lines = [
            (
                ("PASS" if certificates[key] else "FAIL")
                + f" CERTIFICATE_{key}_{certificate_labels[key]}"
            )
            for key in ("A", "B", "C", "D", "E", "F")
        ]
        final_line = canonical_json(report)
        actual_stdout_bytes = sum(
            len((line + "\n").encode("utf-8"))
            for line in data_lines + certificate_lines + [final_line]
        )
        if actual_stdout_bytes == report["stdout_bytes"]:
            break
        report["stdout_bytes"] = actual_stdout_bytes

    certificates["F"] = bool(
        controls_pass
        and deterministic
        and runtime_sec < AUDIT_TIMEOUT_SEC
        and int(report["stdout_bytes"]) < 150_000
    )
    report["certificates"] = certificates
    report["pass"] = all(certificates.values())
    certificate_lines = [
        (
            ("PASS" if certificates[key] else "FAIL")
            + f" CERTIFICATE_{key}_{certificate_labels[key]}"
        )
        for key in ("A", "B", "C", "D", "E", "F")
    ]
    final_line = canonical_json(report)
    final_actual_bytes = sum(
        len((line + "\n").encode("utf-8"))
        for line in data_lines + certificate_lines + [final_line]
    )
    if final_actual_bytes != report["stdout_bytes"]:
        report["stdout_bytes"] = final_actual_bytes
        final_line = canonical_json(report)

    for line in data_lines:
        print(line)
    for line in certificate_lines:
        print(line)
    print(final_line)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
