#!/usr/bin/env python3
"""Cycle 770 independent adversarial checker for the permanence witness.

The Cycle-770 primary is blocklisted: this checker reads its text/AST for the
engagement audit but never imports or executes it.  All dynamics and hostile
words are rebuilt from the landed Cycle-769, Cycle-745, and Cycle-719 inputs.
"""

from __future__ import annotations

import ast
from hashlib import sha256
import importlib
import json
from pathlib import Path
import sys
from time import perf_counter
from typing import Any, Iterable


AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle769_formation_census_2026_07_28.py",
    "scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
BLOCKLIST = (
    "scripts/frontier_cycle770_lock_composed_formation_2026_07_28.py",
)
EXPECTED_SHA256 = {
    "scripts/frontier_cycle769_formation_census_2026_07_28.py":
        "249a9f84eb3a89b2a261801e8e2bb15cc0ba1919a61ac6a8e4c731b3ecaedb32",
    "scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py":
        "d8c1651eb8cdd25a797881b55b81234a5816407418ef415491ecef41672bd708",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py":
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    "scripts/frontier_cycle770_lock_composed_formation_2026_07_28.py":
        "9f886b8afb8ea4391bc1c17335bc91c6e9da4cdab6961d0a55d733509631c703",
}

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

C769 = importlib.import_module(
    "frontier_cycle769_formation_census_2026_07_28"
)
C745 = importlib.import_module(
    "frontier_cycle745_enforced_dual_rail_lock_2026_07_28"
)
K719 = importlib.import_module(
    "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
)

PRIMARY_MODULE = "frontier_cycle770_lock_composed_formation_2026_07_28"


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(canonical_json(value).encode()).hexdigest()


def ast_sha(source: bytes) -> str:
    tree = ast.parse(source.decode("utf-8"))
    frozen = ast.dump(tree, annotate_fields=True, include_attributes=False)
    return sha256(frozen.encode()).hexdigest()


def source_snapshot() -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for relative in AUDIT_INPUT_PATHS + BLOCKLIST:
        source = (ROOT / relative).read_bytes()
        result[relative] = {
            "bytes": len(source),
            "sha256": sha256(source).hexdigest(),
            "ast_sha256": ast_sha(source),
        }
    return result


def literal_assignment(tree: ast.Module, name: str) -> object:
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            )
        ):
            return ast.literal_eval(node.value)
    raise RuntimeError(f"literal assignment {name} was not found")


def checker_import_firewall() -> dict[str, object]:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    frontier_imports = []
    importlib_frontier_calls = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            frontier_imports.extend(
                alias.name for alias in node.names
                if alias.name.startswith("frontier_cycle")
            )
        elif (
            isinstance(node, ast.ImportFrom)
            and node.module
            and node.module.startswith("frontier_cycle")
        ):
            frontier_imports.append(node.module)
        elif (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "importlib"
            and node.func.attr == "import_module"
            and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
            and node.args[0].value.startswith("frontier_cycle")
        ):
            importlib_frontier_calls.append(node.args[0].value)
    literal_inputs = literal_assignment(tree, "AUDIT_INPUT_PATHS")
    literal_blocklist = literal_assignment(tree, "BLOCKLIST")
    expected_modules = [
        Path(relative).stem for relative in AUDIT_INPUT_PATHS
    ]
    blocked_imported = (
        PRIMARY_MODULE in sys.modules
        or PRIMARY_MODULE in frontier_imports
        or PRIMARY_MODULE in importlib_frontier_calls
    )
    return {
        "blocked_primary_imported": blocked_imported,
        "frontier_import_statements": sorted(frontier_imports),
        "importlib_frontier_calls": importlib_frontier_calls,
        "literal_AUDIT_INPUT_PATHS": literal_inputs,
        "literal_BLOCKLIST": literal_blocklist,
        "ok": (
            literal_inputs == AUDIT_INPUT_PATHS
            and literal_blocklist == BLOCKLIST
            and importlib_frontier_calls == expected_modules
            and not blocked_imported
        ),
    }


def extract_769_verbatim(source: bytes) -> dict[str, object]:
    tree = ast.parse(source.decode("utf-8"))
    positive_standard: str | None = None
    rule: dict[str, str] | None = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            target_names = {
                target.id for target in node.targets
                if isinstance(target, ast.Name)
            }
            if "operationalization" in target_names and isinstance(
                node.value, ast.Dict
            ):
                for key, value in zip(node.value.keys, node.value.values):
                    if (
                        key is not None
                        and ast.literal_eval(key)
                        == "positive_formation_test"
                    ):
                        positive_standard = ast.literal_eval(value)
        if isinstance(node, ast.Dict):
            try:
                mapping = {
                    ast.literal_eval(key): ast.literal_eval(value)
                    for key, value in zip(node.keys, node.values)
                    if key is not None
                }
            except (ValueError, TypeError):
                continue
            if set(mapping) == {"empty", "all", "structured", "unidentified"}:
                rule = mapping
    if positive_standard is None or rule is None:
        raise RuntimeError("verbatim Cycle-769 standard/rule extraction failed")
    return {
        "positive_standard": positive_standard,
        "classification_rule": rule,
    }


def bits(payload: bytes) -> tuple[int, ...]:
    return tuple(
        (byte >> bit_index) & 1
        for byte in payload
        for bit_index in range(8)
    )


def unbits(payload_bits: Iterable[int]) -> bytes:
    values = tuple(int(value) for value in payload_bits)
    if len(values) % 8:
        raise ValueError("bit vector is not byte aligned")
    return bytes(
        sum(values[offset + bit_index] << bit_index for bit_index in range(8))
        for offset in range(0, len(values), 8)
    )


def payload_bytes(rows: object) -> bytes:
    return canonical_json(rows).encode()


def locked_payload(content: bytes) -> tuple[tuple[int, int, int], ...]:
    rails = []
    for offered in bits(content):
        event = C745.apply_word(
            C745.packet((0, *C745.UNLOCKED), offered),
            C745.WRITE_WORD,
        )
        if (
            C745.output_tag(event) != "ACCEPTED"
            or C745.persistent(event) != (offered, *C745.LOCKED)
        ):
            raise RuntimeError("Cycle-745 first-write lock did not engage")
        rails.append(C745.persistent(event))
    return tuple(rails)


def controller_data(full: int) -> int:
    return int(C769.C719.controller_register_rows(full)["data"])


def source_for_mode(mode: int) -> int:
    candidates = [
        source for source in C769.initial_origin_zero_branches()
        if (source & 4095).bit_length() - 1 == mode
    ]
    if len(candidates) != 1:
        raise RuntimeError(f"expected one origin-zero mode-{mode} branch")
    return candidates[0]


def int_sha(value: int) -> str:
    width = max(1, (value.bit_length() + 7) // 8)
    return sha256(value.to_bytes(width, "little")).hexdigest()


def run_branch(
    mode: int,
    *,
    compose: bool,
) -> dict[str, object]:
    """Run a literal compiled branch; composition is a write-once sidecar."""
    C719 = C769.C719
    source = source_for_mode(mode)
    initial_full = C719.controller_full_input(source)
    full = initial_full
    trace: list[dict[str, object]] = []
    lock: tuple[tuple[int, int, int], ...] | None = None
    engagement: dict[str, object] | None = None
    for orbit_step in range(C719.CONTROLLER_STATIONS):
        before = C719.controller_register_rows(full)
        before_data = int(before["data"])
        live_a = tuple(
            index for index, value in enumerate(before["A"]) if value
        )
        full = C719.apply_fast_int(full, C719.CONTROLLER_H_FAST)
        after_data = controller_data(full)
        decoded = C769.decoded_cell_surface(after_data)
        rows = list(decoded["cell_rows"])
        trace.append({
            "data_sha256": int_sha(after_data),
            "full_sha256": int_sha(full),
            "orbit_step": orbit_step,
        })
        accepted_shape = bool(rows) and all(
            row["binder"] == row["valid"] == 1 for row in rows
        )
        if compose and accepted_shape and lock is None:
            content = payload_bytes(rows)
            lock = locked_payload(content)
            station = live_a[0] if len(live_a) == 1 else None
            engagement = {
                "content_hex": content.hex(),
                "content_sha256": sha256(content).hexdigest(),
                "orbit_step": orbit_step,
                "program_kind": (
                    C719.PROGRAM[station][0]
                    if station is not None else None
                ),
                "site": tuple(
                    C719.M.R12.full_wire_layout()["wire_sites"][
                        C719.R3_SOURCE_POINTER()
                    ]
                ),
            }
        if before_data != after_data:
            trace[-1]["changed_data_bits"] = (
                before_data ^ after_data
            ).bit_count()
    final_rows = list(
        C769.decoded_cell_surface(controller_data(full))["cell_rows"]
    )
    return {
        "engagement": engagement,
        "final_full": full,
        "final_rows": final_rows,
        "initial_full": initial_full,
        "lock": lock,
        "mode": mode,
        "source": source,
        "trace": trace,
        "trace_sha256": digest(trace),
    }


def apply_payload_word(
    pristine: tuple[tuple[int, int, int], ...],
    offered_content: bytes,
    word: tuple[Any, ...],
    *,
    family: str,
    name: str,
) -> tuple[tuple[tuple[int, int, int], ...], dict[str, object]]:
    offered = bits(offered_content)
    if len(pristine) != len(offered):
        raise ValueError("hostile payload width differs from locked width")
    events = tuple(
        C745.apply_word(C745.packet(storage, bit), word)
        for storage, bit in zip(pristine, offered)
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
    content_after = unbits(storage[0] for storage in after)
    content_before = unbits(storage[0] for storage in pristine)
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
    forward: dict[str, object],
    pristine: tuple[tuple[int, int, int], ...],
    original_content: bytes,
) -> dict[str, object]:
    C719 = C769.C719
    full = int(forward["final_full"])
    before_data = controller_data(full)
    change_steps = []
    for orbit_step in range(C719.CONTROLLER_STATIONS):
        previous = controller_data(full)
        full = C719.apply_fast_int(full, C719.CONTROLLER_H_FAST)
        observed = controller_data(full)
        if previous != observed:
            change_steps.append({
                "changed_data_bits": (previous ^ observed).bit_count(),
                "orbit_step": orbit_step,
            })
    after_data = controller_data(full)
    rows = list(C769.decoded_cell_surface(after_data)["cell_rows"])
    proposed = payload_bytes(rows)
    _after, receipt = apply_payload_word(
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
        "decoded_proposal_equals_locked_content": proposed == original_content,
    })
    return receipt


def direct_bank_station_attacks(
    forward: dict[str, object],
    original_content: bytes,
) -> list[dict[str, object]]:
    """Apply every landed bank macro directly, outside the lock request port."""
    C719 = C769.C719
    data_before = controller_data(int(forward["final_full"]))
    tuple_before = C719.int_to_tuple(data_before)
    candidate_site = tuple(
        C719.M.R12.full_wire_layout()["wire_sites"][
            C719.R3_SOURCE_POINTER()
        ]
    )
    results = []
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
            "content_byte_identical": content_after == original_content,
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
    forward: dict[str, object],
) -> dict[str, object]:
    rows = list(forward["final_rows"])
    content = payload_bytes(rows)
    pristine = locked_payload(content)
    complement = bytes(byte ^ 0xFF for byte in content)
    attacks: list[dict[str, object]] = []

    current = pristine
    for application in (1, 2):
        current, receipt = apply_payload_word(
            current,
            complement,
            C745.REVERSE_WRITE_WORD,
            family="inverse_word_twice",
            name=f"inverse_word_application_{application}",
        )
        attacks.append(receipt)

    for length in range(1, len(C745.REVERSE_WRITE_WORD)):
        _after, receipt = apply_payload_word(
            pristine,
            complement,
            C745.REVERSE_WRITE_WORD[:length],
            family="partial_inverse_prefix",
            name=f"partial_inverse_prefix_{length}",
        )
        receipt["last_gate"] = C745.REVERSE_WRITE_WORD[length - 1].name
        attacks.append(receipt)

    attacks.append(mode6_forward_replay_attack(
        forward, pristine, content
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
        _after, receipt = apply_payload_word(
            pristine,
            offered,
            macro_words[macro],
            family="declared_alphabet_foreign_content",
            name=f"declared_alphabet_{macro}",
        )
        receipt["macro"] = macro
        attacks.append(receipt)

    attacks.extend(direct_bank_station_attacks(forward, content))
    mutations = [
        row["name"] for row in attacks
        if row["mutation"] and not row["refused"]
    ]
    return {
        "all_attacks_refused_with_syndrome": all(
            row["refused"] and row["syndrome_receipt"]
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


def primary_engagement_ast_audit(primary_source: bytes) -> dict[str, object]:
    tree = ast.parse(primary_source.decode("utf-8"))
    functions = [
        node for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == "forward_mode6_with_lock"
    ]
    if len(functions) != 1:
        return {"ok": False, "reason": "forward function not unique"}
    function = functions[0]

    def call_name(call: ast.Call) -> str:
        cursor = call.func
        return cursor.attr if isinstance(cursor, ast.Attribute) else (
            cursor.id if isinstance(cursor, ast.Name) else ""
        )

    call_lines: dict[str, list[int]] = {}
    for node in ast.walk(function):
        if isinstance(node, ast.Call):
            call_lines.setdefault(call_name(node), []).append(node.lineno)
    assignments = []
    for node in ast.walk(function):
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name) and target.id == "full"
            for target in node.targets
        ):
            assignments.append({
                "line": node.lineno,
                "value": ast.get_source_segment(
                    primary_source.decode("utf-8"), node.value
                ),
            })
    guarded_first_write = False
    for node in ast.walk(function):
        if not isinstance(node, ast.If):
            continue
        test_dump = ast.dump(node.test, include_attributes=False)
        contains_first_write = any(
            isinstance(child, ast.Call)
            and call_name(child) == "first_write_payload"
            for statement in node.body
            for child in ast.walk(statement)
        )
        if "accepted_shape" in test_dump and contains_first_write:
            guarded_first_write = True
    apply_lines = call_lines.get("apply_fast_int", [])
    decode_lines = call_lines.get("decoded_cell_surface", [])
    write_lines = call_lines.get("first_write_payload", [])
    ordered = (
        len(apply_lines) == len(decode_lines) == len(write_lines) == 1
        and apply_lines[0] < decode_lines[0] < write_lines[0]
    )
    full_assignment_ok = (
        len(assignments) == 2
        and assignments[0]["value"] == "initial_full"
        and "apply_fast_int" in str(assignments[1]["value"])
    )
    return {
        "apply_fast_int_lines": apply_lines,
        "decoded_cell_surface_lines": decode_lines,
        "first_write_payload_lines": write_lines,
        "full_assignments": assignments,
        "guarded_by_accepted_shape": guarded_first_write,
        "ok": ordered and full_assignment_ok and guarded_first_write,
        "ordered_apply_decode_engage": ordered,
    }


def engagement_point_audit(
    baseline: dict[str, object],
    composed: dict[str, object],
    primary_source: bytes,
) -> dict[str, object]:
    baseline_prefix = list(baseline["trace"])[:126]
    composed_prefix = list(composed["trace"])[:126]
    engagement = composed["engagement"]
    if not isinstance(engagement, dict):
        raise RuntimeError("composed mode 6 did not engage")
    ast_result = primary_engagement_ast_audit(primary_source)
    exact = baseline_prefix == composed_prefix
    return {
        "ast_audit": ast_result,
        "baseline_trace_sha256_through_step_125": digest(baseline_prefix),
        "composed_trace_sha256_through_step_125": digest(composed_prefix),
        "early_engagement_found": engagement["orbit_step"] < 125,
        "engagement_orbit_step": engagement["orbit_step"],
        "engagement_program_kind": engagement["program_kind"],
        "landed_trace_bit_identical_through_step_125": exact,
        "ok": (
            ast_result["ok"]
            and exact
            and engagement["orbit_step"] == 125
            and engagement["program_kind"] == "finalizer"
        ),
    }


def fresh_site_write_controls(
    candidate_site: tuple[int, int, int],
    content: bytes,
    candidate_lock: tuple[tuple[int, int, int], ...],
) -> dict[str, object]:
    other_sites = (
        (candidate_site[0] + 1, candidate_site[1], candidate_site[2]),
        (candidate_site[0], candidate_site[1] + 1, candidate_site[2]),
        (candidate_site[0], candidate_site[1], candidate_site[2] + 1),
    )
    archive = {candidate_site: candidate_lock}
    rows = []
    for site in other_sites:
        before_absent = site not in archive
        archive[site] = locked_payload(content)
        stored = unbits(storage[0] for storage in archive[site])
        rows.append({
            "accepted": before_absent and stored == content,
            "content_sha256": sha256(stored).hexdigest(),
            "site": site,
        })
    return {
        "candidate_lock_unchanged": archive[candidate_site] == candidate_lock,
        "fresh_site_count": len(rows),
        "fresh_writes": rows,
        "other_sites_succeed": all(row["accepted"] for row in rows),
    }


def collateral_attack(
    mode6_composed: dict[str, object],
) -> dict[str, object]:
    C719 = C769.C719
    no_write_rows = []
    for mode in (0, 2, 3, 4, 5):
        baseline = run_branch(mode, compose=False)
        composed = run_branch(mode, compose=True)
        unchanged = (
            baseline["trace"] == composed["trace"]
            and baseline["final_full"] == composed["final_full"]
            and baseline["final_rows"] == composed["final_rows"]
            and composed["engagement"] is None
        )
        no_write_rows.append({
            "bit_identical": unchanged,
            "composed_trace_sha256": composed["trace_sha256"],
            "data_write_steps": [
                row["orbit_step"] for row in baseline["trace"]
                if "changed_data_bits" in row
            ],
            "mode": mode,
            "uncomposed_trace_sha256": baseline["trace_sha256"],
        })

    mode0 = run_branch(0, compose=True)
    host_data, host_a, host_b, _host_trace = K719.run_orbit(
        C719.int_to_tuple(int(mode0["source"])),
        C719.PROGRAM,
    )
    registers = C719.controller_register_rows(int(mode0["final_full"]))
    controller_identity = {
        "A0_return": registers["A"] == host_a == (
            (1,) + (0,) * (C719.CONTROLLER_STATIONS - 1)
        ),
        "B_vacuum_return": registers["B"] == host_b == (
            (0,) * C719.CONTROLLER_STATIONS
        ),
        "compiled_equals_host": (
            int(registers["data"]) == C719.tuple_to_int(host_data)
        ),
        "full_branch_mode": 0,
        "lock_engaged": mode0["engagement"] is not None,
        "work_return": not any(registers["work"]),
    }

    engagement = mode6_composed["engagement"]
    lock = mode6_composed["lock"]
    if not isinstance(engagement, dict) or not isinstance(lock, tuple):
        raise RuntimeError("mode-6 composition did not produce a sidecar lock")
    content = bytes.fromhex(str(engagement["content_hex"]))
    fresh = fresh_site_write_controls(
        tuple(engagement["site"]), content, lock
    )
    no_write_unchanged = all(row["bit_identical"] for row in no_write_rows)
    identities_hold = (
        controller_identity["compiled_equals_host"]
        and controller_identity["A0_return"]
        and controller_identity["B_vacuum_return"]
        and controller_identity["work_return"]
        and not controller_identity["lock_engaged"]
    )
    return {
        "collateral_breakage_found": not (
            no_write_unchanged
            and fresh["other_sites_succeed"]
            and identities_hold
        ),
        "controller_identity_before_any_lock": controller_identity,
        "fresh_site_controls": fresh,
        "modes_0_2_3_4_5_bit_identical": no_write_unchanged,
        "no_write_mode_rows": no_write_rows,
        "ok": (
            no_write_unchanged
            and fresh["other_sites_succeed"]
            and fresh["candidate_lock_unchanged"]
            and identities_hold
        ),
    }


def witness_standard_recount(
    standard: str,
    forward: dict[str, object],
    battery: dict[str, object],
) -> dict[str, object]:
    engagement = forward["engagement"]
    if not isinstance(engagement, dict):
        raise RuntimeError("missing engagement evidence")
    rows = list(forward["final_rows"])
    decoded = payload_bytes(rows)
    candidate_site = tuple(
        C769.C719.M.R12.full_wire_layout()["wire_sites"][
            C769.C719.R3_SOURCE_POINTER()
        ]
    )
    clauses = {
        "locked_content_equals_decoded_possibility": (
            battery["locked_content_sha256"] == sha256(decoded).hexdigest()
        ),
        "permanence_by_named_refusal_law": bool(
            battery["all_attacks_refused_with_syndrome"]
        ),
        "record_shaped_output": bool(rows) and all(
            row["binder"] == row["valid"] == 1 for row in rows
        ),
        "site_equals_candidate_site": (
            tuple(engagement["site"]) == candidate_site == (-8, -1, 1)
        ),
    }
    return {
        "all_clauses_met": all(clauses.values()),
        "clauses": clauses,
        "decoded_possibility": rows,
        "declared_law_scope": list(C745.ALPHABET_SCOPE),
        "law_name_verbatim": C745.INDUCTION_STATEMENT,
        "out_of_alphabet_boundary_verbatim": C745.OUT_OF_ALPHABET_BOUNDARY,
        "positive_standard_verbatim": standard,
        "unmet_clauses": [
            name for name, met in clauses.items() if not met
        ],
    }


def independent_classify(decisions: list[bool | None]) -> str:
    if any(value is None for value in decisions):
        return "unidentified"
    if not any(decisions):
        return "empty"
    if all(decisions):
        return "all"
    return "structured"


def dual_reading_recount(
    rule: dict[str, str],
    witness: dict[str, object],
    collateral: dict[str, object],
) -> dict[str, object]:
    mode6 = True if witness["all_clauses_met"] else None
    no_write_modes_exhaustive = all(
        not row["data_write_steps"]
        for row in collateral["no_write_mode_rows"]
    )
    counts = [
        False if no_write_modes_exhaustive else None
        for _mode in (0, 2, 3, 4, 5)
    ] + [mode6]
    neutral = [None, None, None, None, None, mode6]
    counts_label = independent_classify(counts)
    neutral_label = independent_classify(neutral)
    return {
        "classification_if_no_write_counts": counts_label,
        "classification_if_no_write_does_not_count": neutral_label,
        "counts_decisions_modes_0_2_3_4_5_6": counts,
        "does_not_count_decisions_modes_0_2_3_4_5_6": neutral,
        "no_write_modes_exhaustive": no_write_modes_exhaustive,
        "primary_labels_confirmed": (
            counts_label == "structured"
            and neutral_label == "unidentified"
        ),
        "rule_text_verbatim": rule,
        "selected_rule_if_counts": rule[counts_label],
        "selected_rule_if_does_not_count": rule[neutral_label],
    }


def run_experiment(verbatim: dict[str, object], primary_source: bytes) -> dict[str, object]:
    baseline = run_branch(6, compose=False)
    composed = run_branch(6, compose=True)
    battery = hostile_word_battery(composed)
    collateral = collateral_attack(composed)
    engagement = engagement_point_audit(
        baseline, composed, primary_source
    )
    witness = witness_standard_recount(
        str(verbatim["positive_standard"]), composed, battery
    )
    classifications = dual_reading_recount(
        dict(verbatim["classification_rule"]), witness, collateral
    )
    return {
        "battery": battery,
        "classifications": classifications,
        "collateral": collateral,
        "engagement": engagement,
        "mode6": {
            "baseline_final_full_sha256": int_sha(
                int(baseline["final_full"])
            ),
            "composed_final_full_sha256": int_sha(
                int(composed["final_full"])
            ),
            "decoded_EventCell_rows": composed["final_rows"],
            "engagement": composed["engagement"],
            "trace_bit_identical_full_orbit": (
                baseline["trace"] == composed["trace"]
            ),
        },
        "witness": witness,
    }


def battery_faithful(battery: dict[str, object]) -> bool:
    attacks = list(battery["attacks"])
    families = [row["family"] for row in attacks]
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
    return (
        battery["attack_count"] == len(expected_names) == 26
        and [row["name"] for row in attacks] == expected_names
        and families.count("inverse_word_twice") == 2
        and families.count("partial_inverse_prefix") == 7
        and families.count("mode6_forward_word_replay") == 1
        and families.count("declared_alphabet_foreign_content") == 4
        and families.count("direct_bank_station") == 12
        and all(
            all(
                key in row for key in (
                    "content_byte_identical",
                    "mutation",
                    "name",
                    "refused",
                    "syndrome_receipt",
                )
            )
            for row in attacks
        )
    )


def collateral_faithful(collateral: dict[str, object]) -> bool:
    rows = list(collateral["no_write_mode_rows"])
    identity = collateral["controller_identity_before_any_lock"]
    fresh = collateral["fresh_site_controls"]
    return (
        [row["mode"] for row in rows] == [0, 2, 3, 4, 5]
        and len(rows) == 5
        and fresh["fresh_site_count"] == 3
        and identity["full_branch_mode"] == 0
        and all(
            key in identity for key in (
                "A0_return",
                "B_vacuum_return",
                "compiled_equals_host",
                "work_return",
            )
        )
    )


def build_lines(
    headline: str,
    report: dict[str, object],
) -> list[str]:
    experiment = report["experiment"]
    lines = [
        headline,
        "SHA256_AST_ANCHORS " + canonical_json(report["anchors"]),
        "BLOCKLIST_FIREWALL " + canonical_json(report["blocklist_firewall"]),
        "STANDARD_769_VERBATIM " + canonical_json(
            report["verbatim_769"]
        ),
        "HOSTILE_BATTERY_SUMMARY " + canonical_json({
            key: experiment["battery"][key]
            for key in (
                "all_attacks_refused_with_syndrome",
                "attack_count",
                "payload_bit_count",
                "refused_count",
                "surviving_unrefused_mutations",
                "witness_refuted",
            )
        }),
    ]
    lines.extend(
        "HOSTILE_FINDING " + canonical_json(row)
        for row in experiment["battery"]["attacks"]
    )
    lines.extend([
        "COLLATERAL_FINDING " + canonical_json(experiment["collateral"]),
        "ENGAGEMENT_POINT_FINDING " + canonical_json(
            experiment["engagement"]
        ),
        "WITNESS_STANDARD_RECOUNT " + canonical_json(
            experiment["witness"]
        ),
        "DUAL_READING_RECOUNT " + canonical_json(
            experiment["classifications"]
        ),
    ])
    lines.extend(
        ("PASS" if passed else "FAIL") + " " + label
        for label, passed in report["certificates"].items()
    )
    lines.append("FINAL_REPORT " + canonical_json(report))
    return lines


def main() -> int:
    started = perf_counter()
    before = source_snapshot()
    primary_source = (ROOT / BLOCKLIST[0]).read_bytes()
    source_769 = (ROOT / AUDIT_INPUT_PATHS[0]).read_bytes()
    verbatim = extract_769_verbatim(source_769)
    firewall = checker_import_firewall()

    first = run_experiment(verbatim, primary_source)
    second = run_experiment(verbatim, primary_source)
    deterministic = first == second
    after = source_snapshot()

    expected_anchors = all(
        before[path]["sha256"] == EXPECTED_SHA256[path]
        for path in AUDIT_INPUT_PATHS + BLOCKLIST
    )
    unchanged = before == after
    module_identity = (
        C769.K is K719
        and C769.C719.K is K719
        and PRIMARY_MODULE not in sys.modules
    )
    anchors = {
        path: {
            "ast_sha256": before[path]["ast_sha256"],
            "sha256": before[path]["sha256"],
        }
        for path in AUDIT_INPUT_PATHS + BLOCKLIST
    }

    battery = first["battery"]
    collateral = first["collateral"]
    engagement = first["engagement"]
    witness = first["witness"]
    classifications = first["classifications"]
    mutation_names = list(battery["surviving_unrefused_mutations"])
    primary_survives = bool(
        battery["all_attacks_refused_with_syndrome"]
        and collateral["ok"]
        and engagement["ok"]
        and witness["all_clauses_met"]
        and classifications["primary_labels_confirmed"]
    )
    if mutation_names:
        headline = (
            "HEADLINE: PRIMARY PERMANENCE WITNESS REFUTED — "
            "UNREFUSED LOCKED-CELL MUTATION(S): "
            + ",".join(mutation_names)
        )
    elif not primary_survives:
        headline = (
            "HEADLINE: PRIMARY PERMANENCE WITNESS REFUTED — "
            "required hostile refusal/permanence clause failed"
        )
    else:
        headline = (
            "HEADLINE: PRIMARY PERMANENCE WITNESS SURVIVED THIS BATTERY"
        )

    runtime_sec = perf_counter() - started
    certificate_labels = {
        "CERTIFICATE_1_HOSTILE_WORD_BATTERY_ATTACK_EXECUTED":
            battery_faithful(battery),
        "CERTIFICATE_2_OVERBLOCK_COLLATERAL_ATTACK_EXECUTED":
            collateral_faithful(collateral),
        "CERTIFICATE_3_ENGAGEMENT_POINT_AST_TRACE_AUDIT_EXECUTED": (
            len(engagement[
                "baseline_trace_sha256_through_step_125"
            ]) == 64
            and len(engagement[
                "composed_trace_sha256_through_step_125"
            ]) == 64
            and engagement["ast_audit"]["ordered_apply_decode_engage"]
        ),
        "CERTIFICATE_4_WITNESS_STANDARD_RECOUNT_EXECUTED": (
            witness["positive_standard_verbatim"]
            == verbatim["positive_standard"]
            and set(witness["clauses"]) == {
                "locked_content_equals_decoded_possibility",
                "permanence_by_named_refusal_law",
                "record_shaped_output",
                "site_equals_candidate_site",
            }
        ),
        "CERTIFICATE_5_DUAL_READING_CLASSIFICATION_RECOUNT_EXECUTED": (
            set(verbatim["classification_rule"])
            == {"empty", "all", "structured", "unidentified"}
            and classifications[
                "classification_if_no_write_counts"
            ] in verbatim["classification_rule"]
            and classifications[
                "classification_if_no_write_does_not_count"
            ] in verbatim["classification_rule"]
        ),
        "CERTIFICATE_6_CONTROLS_SHA_BLOCKLIST_DETERMINISM_BOUNDS": False,
    }
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "AUDIT_TIMEOUT_SEC": AUDIT_TIMEOUT_SEC,
        "BLOCKLIST": list(BLOCKLIST),
        "W6_untouched": True,
        "anchors": anchors,
        "blocklist_firewall": firewall,
        "certificates": certificate_labels,
        "checker_pass": False,
        "determinism": {
            "exact_rerun_equal": deterministic,
            "first_sha256": digest(first),
            "rerun_sha256": digest(second),
        },
        "experiment": first,
        "no_probability_weights_or_rate_law": True,
        "primary_claim_survives": primary_survives,
        "runtime_sec": runtime_sec,
        "status": "SURVIVED" if primary_survives else "REFUTED",
        "stdout_bytes": 0,
        "verbatim_769": verbatim,
    }

    for _iteration in range(12):
        certificate_labels[
            "CERTIFICATE_6_CONTROLS_SHA_BLOCKLIST_DETERMINISM_BOUNDS"
        ] = bool(
            expected_anchors
            and unchanged
            and firewall["ok"]
            and module_identity
            and deterministic
            and runtime_sec < AUDIT_TIMEOUT_SEC
            and int(report["stdout_bytes"]) < 150_000
        )
        report["certificates"] = certificate_labels
        report["checker_pass"] = all(certificate_labels.values())
        rendered = build_lines(headline, report)
        stdout_bytes = sum(
            len((line + "\n").encode()) for line in rendered
        )
        if stdout_bytes == report["stdout_bytes"]:
            break
        report["stdout_bytes"] = stdout_bytes

    final_lines = build_lines(headline, report)
    actual_stdout = sum(len((line + "\n").encode()) for line in final_lines)
    if actual_stdout != report["stdout_bytes"]:
        report["stdout_bytes"] = actual_stdout
        certificate_labels[
            "CERTIFICATE_6_CONTROLS_SHA_BLOCKLIST_DETERMINISM_BOUNDS"
        ] = bool(
            expected_anchors
            and unchanged
            and firewall["ok"]
            and module_identity
            and deterministic
            and runtime_sec < AUDIT_TIMEOUT_SEC
            and actual_stdout < 150_000
        )
        report["checker_pass"] = all(certificate_labels.values())
        final_lines = build_lines(headline, report)

    for line in final_lines:
        print(line)
    return 0 if report["checker_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
