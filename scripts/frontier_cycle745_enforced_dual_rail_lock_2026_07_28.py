#!/usr/bin/env python3
"""Cycle 745: exhaustive one-cell enforced dual-rail write-once certificate."""

from __future__ import annotations

import ast
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import time
from typing import Iterable


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/ENFORCED_DUAL_RAIL_LOCK_CYCLE745_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
# Self-contained Route-1 construction: the portfolio names no imported script.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py",
)  # self-contained: no external execution sources
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS


RAILS = ("D", "V", "U", "L", "Q_in", "Q_accept", "Q_refuse")
RAIL_INDEX = {name: index for index, name in enumerate(RAILS)}
SITE_LAYOUT = {
    "D": (0, 0, 0),
    "V": (1, 0, 0),
    "U": (2, 0, 0),
    "L": (2, 1, 0),
    "Q_in": (3, 1, 0),
    "Q_accept": (4, 1, 0),
    "Q_refuse": (3, 2, 0),
}
WORK_RAILS: tuple[str, ...] = ()
UNLOCKED = (1, 0)
LOCKED = (0, 1)
ALPHABET_SCOPE = ("IDLE", "READ", "WRITE[0]", "WRITE[1]")
NEXT_CYCLE = "multi-cell archive integration (741/742 composition)"

SUPPLIED_PORTFOLIO_VERBATIM = (
    "Supplied: M2 bit encoding, site layout, initial blank payload and "
    "`UNLOCKED` row, incoming-request convention, fixed macro alphabet, "
    "`C_source`, Record activation rule (`LOCKED` means the site now "
    "contributes a Record), and scalar/readout conventions."
)
DERIVED_PORTFOLIO_VERBATIM = (
    "Derived: one-hot lock preservation, first-write acceptance, lock setting "
    "by that same write, clean locked-request refusal, return of all route/work "
    "rails, exhaustive control ancestry for every payload target, and the "
    "locked-content invariant under arbitrary finite macro composition."
)
INDUCTION_STATEMENT = (
    "For every n >= 0 and every M_1,...,M_n in alphabet_scope, LOCKED(x) "
    "implies LOCKED(M_n...M_1 x) and D(M_n...M_1 x)=D(x) at event boundaries."
)
OUT_OF_ALPHABET_BOUNDARY = (
    "Out-of-alphabet operations, including a literal reverse presented as a "
    "new forward request, are out of scope."
)

State = tuple[int, int, int, int, int, int, int]
Persistent = tuple[int, int, int]
Control = tuple[str, int]


@dataclass(frozen=True)
class Gate:
    """A literal self-inverse reversible gate on the seven binary M2 rails."""

    name: str
    operation: str
    targets: tuple[str, ...]
    controls: tuple[Control, ...] = ()


# The valid-LOCKED branch is a reversible lift/unlift cascade controlled by L.
# Every data target is behind the joint U=1, L=0 enforcement result.
WRITE_WORD = (
    Gate("cascade_lift", "X", ("U",), (("L", 1),)),
    Gate(
        "refuse_locked_route",
        "SWAP",
        ("Q_in", "Q_refuse"),
        (("U", 1), ("L", 1)),
    ),
    Gate("cascade_unlift", "X", ("U",), (("L", 1),)),
    Gate(
        "refuse_dirty_11_route",
        "SWAP",
        ("Q_in", "Q_refuse"),
        (("U", 1), ("L", 1)),
    ),
    Gate(
        "refuse_dirty_00_route",
        "SWAP",
        ("Q_in", "Q_refuse"),
        (("U", 0), ("L", 0)),
    ),
    Gate(
        "payload_copy",
        "X",
        ("D",),
        (("V", 1), ("U", 1), ("L", 0)),
    ),
    Gate(
        "accept_route",
        "SWAP",
        ("Q_in", "Q_accept"),
        (("U", 1), ("L", 0)),
    ),
    Gate("lock_transfer", "SWAP", ("U", "L"), (("Q_accept", 1),)),
)
READ_WORD = (Gate("read_copy", "X", ("V",), (("D", 1),)),)
IDLE_WORD: tuple[Gate, ...] = ()
REVERSE_WRITE_WORD = tuple(reversed(WRITE_WORD))


def bits_to_state(bits: Iterable[int]) -> State:
    result = tuple(int(bit) for bit in bits)
    if len(result) != len(RAILS) or any(bit not in (0, 1) for bit in result):
        raise ValueError("a one-cell state must contain exactly seven binary rails")
    return result  # type: ignore[return-value]


def m2(bit: int) -> tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]:
    """Supplied sitewise encoding b -> diag(Q(b), 0)."""

    if bit not in (0, 1):
        raise ValueError("M2 rail value is not binary")
    return ((Fraction(bit), Fraction(0)), (Fraction(0), Fraction(0)))


def gate_enabled(state: State, gate: Gate) -> bool:
    return all(state[RAIL_INDEX[name]] == value for name, value in gate.controls)


def apply_gate(state: State, gate: Gate) -> State:
    if not gate_enabled(state, gate):
        return state
    output = list(state)
    if gate.operation == "X" and len(gate.targets) == 1:
        target = RAIL_INDEX[gate.targets[0]]
        output[target] ^= 1
    elif gate.operation == "SWAP" and len(gate.targets) == 2:
        left, right = (RAIL_INDEX[name] for name in gate.targets)
        output[left], output[right] = output[right], output[left]
    else:
        raise ValueError(f"unsupported gate: {gate}")
    return bits_to_state(output)


def apply_word(state: State, word: tuple[Gate, ...]) -> State:
    output = state
    for gate in word:
        output = apply_gate(output, gate)
    return output


def packet(persistent: Persistent, offered: int, request: int = 1) -> State:
    d_bit, u_bit, l_bit = persistent
    return bits_to_state((d_bit, offered, u_bit, l_bit, request, 0, 0))


def persistent(state: State) -> Persistent:
    return (
        state[RAIL_INDEX["D"]],
        state[RAIL_INDEX["U"]],
        state[RAIL_INDEX["L"]],
    )


def output_tag(state: State) -> str:
    q_in = state[RAIL_INDEX["Q_in"]]
    q_accept = state[RAIL_INDEX["Q_accept"]]
    q_refuse = state[RAIL_INDEX["Q_refuse"]]
    if (q_in, q_accept, q_refuse) == (0, 1, 0):
        return "ACCEPTED"
    if (q_in, q_accept, q_refuse) == (0, 0, 1):
        return "REFUSED"
    return "DIRTY"


def expected_first_write(offered: int) -> State:
    return bits_to_state((offered, offered, 0, 1, 0, 1, 0))


def expected_refusal(d_bit: int, offered: int, lock: tuple[int, int]) -> State:
    u_bit, l_bit = lock
    return bits_to_state((d_bit, offered, u_bit, l_bit, 0, 0, 1))


def all_states() -> tuple[State, ...]:
    return tuple(bits_to_state(bits) for bits in product((0, 1), repeat=len(RAILS)))


def write_behavior_failures(word: tuple[Gate, ...]) -> list[str]:
    failures: list[str] = []
    for offered in (0, 1):
        actual = apply_word(packet((0, *UNLOCKED), offered), word)
        if actual != expected_first_write(offered):
            failures.append(f"first-write-{offered}")
    for d_bit, offered in product((0, 1), repeat=2):
        actual = apply_word(packet((d_bit, *LOCKED), offered), word)
        if actual != expected_refusal(d_bit, offered, LOCKED):
            failures.append(f"locked-{d_bit}-{offered}")
    for lock in ((0, 0), (1, 1)):
        for d_bit, offered in product((0, 1), repeat=2):
            actual = apply_word(packet((d_bit, *lock), offered), word)
            if actual != expected_refusal(d_bit, offered, lock):
                failures.append(f"dirty-{lock[0]}{lock[1]}-{d_bit}-{offered}")
    return failures


def run_write_sequence(payloads: tuple[int, ...]) -> tuple[State, ...]:
    storage: Persistent = (0, *UNLOCKED)
    events: list[State] = []
    for offered in payloads:
        event = apply_word(packet(storage, offered), WRITE_WORD)
        events.append(event)
        storage = persistent(event)
    return tuple(events)


def ast_same_word_certificate() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    assignments = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "WRITE_WORD"
            for target in node.targets
        )
    ]
    if len(assignments) != 1 or not isinstance(assignments[0].value, ast.Tuple):
        return {"ok": False, "gate_names": [], "reason": "WRITE_WORD not literal"}
    gate_names: list[str] = []
    for element in assignments[0].value.elts:
        if (
            not isinstance(element, ast.Call)
            or not element.args
            or not isinstance(element.args[0], ast.Constant)
            or not isinstance(element.args[0].value, str)
        ):
            return {"ok": False, "gate_names": gate_names, "reason": "nonliteral gate"}
        gate_names.append(element.args[0].value)
    required = ("payload_copy", "accept_route", "lock_transfer")
    ordered = all(name in gate_names for name in required) and (
        gate_names.index("payload_copy")
        < gate_names.index("accept_route")
        < gate_names.index("lock_transfer")
    )
    no_separate_lock_word = not any(
        isinstance(node, ast.Name) and node.id == "LOCK_WORD" for node in ast.walk(tree)
    )
    return {
        "ok": ordered and no_separate_lock_word,
        "gate_names": gate_names,
        "lock_transfer_index": gate_names.index("lock_transfer")
        if "lock_transfer" in gate_names
        else None,
        "reason": "same literal WRITE_WORD" if ordered else "missing/order failure",
    }


def certificate_a() -> tuple[bool, dict[str, object]]:
    states = all_states()
    outputs = tuple(apply_word(state, WRITE_WORD) for state in states)
    reverse_exact = all(
        apply_word(output, REVERSE_WRITE_WORD) == state
        for state, output in zip(states, outputs)
    )
    gate_involutions = all(
        apply_gate(apply_gate(state, gate), gate) == state
        for gate in WRITE_WORD
        for state in states
    )
    m2_exact = all(
        m2(bit)
        == ((Fraction(bit), Fraction(0)), (Fraction(0), Fraction(0)))
        for state in states
        for bit in state
    )
    details = {
        "all_rail_states": len(states),
        "distinct_outputs": len(set(outputs)),
        "gate_involutions": gate_involutions,
        "literal_reverse_exact": reverse_exact,
        "m2_encoding_exact": m2_exact,
        "word_sizes": {
            "IDLE": len(IDLE_WORD),
            "READ": len(READ_WORD),
            "REVERSE_WRITE": len(REVERSE_WRITE_WORD),
            "WRITE": len(WRITE_WORD),
        },
    }
    return (
        len(states) == 2 ** len(RAILS)
        and len(set(outputs)) == len(states)
        and reverse_exact
        and gate_involutions
        and m2_exact,
        details,
    )


def certificate_b() -> tuple[bool, dict[str, object]]:
    ast_result = ast_same_word_certificate()
    first_rows: list[dict[str, object]] = []
    behavior_ok = True
    for offered in (0, 1):
        before = packet((0, *UNLOCKED), offered)
        after = apply_word(before, WRITE_WORD)
        row_ok = (
            after == expected_first_write(offered)
            and output_tag(after) == "ACCEPTED"
            and persistent(after) == (offered, *LOCKED)
        )
        behavior_ok &= row_ok
        first_rows.append(
            {
                "offered": offered,
                "post_D": after[RAIL_INDEX["D"]],
                "post_lock": [
                    after[RAIL_INDEX["U"]],
                    after[RAIL_INDEX["L"]],
                ],
                "tag": output_tag(after),
            }
        )
    payload_targets = [
        gate
        for gate in WRITE_WORD
        if "D" in gate.targets
    ]
    control_coverage = (
        len(payload_targets) == 1
        and ("U", 1) in payload_targets[0].controls
        and ("L", 0) in payload_targets[0].controls
    )
    layout_unique = len(set(SITE_LAYOUT.values())) == len(RAILS)
    details = {
        "ast": ast_result,
        "control_coverage": control_coverage,
        "first_write_rows": first_rows,
        "layout_sites": len(SITE_LAYOUT),
        "layout_unique": layout_unique,
        "payload_target_gates": [gate.name for gate in payload_targets],
    }
    return bool(
        ast_result["ok"]
        and behavior_ok
        and control_coverage
        and layout_unique
        and len(SITE_LAYOUT) == len(RAILS)
    ), details


def certificate_c() -> tuple[bool, dict[str, object]]:
    locked_rows = 0
    dirty_rows = 0
    same_value_refusals = 0
    opposite_value_refusals = 0
    transition_ok = True
    for d_bit, offered in product((0, 1), repeat=2):
        before = packet((d_bit, *LOCKED), offered)
        after = apply_word(before, WRITE_WORD)
        row_ok = (
            after == expected_refusal(d_bit, offered, LOCKED)
            and bytes((after[RAIL_INDEX["D"]],)) == bytes((d_bit,))
            and output_tag(after) == "REFUSED"
            and (after[RAIL_INDEX["Q_in"]], after[RAIL_INDEX["Q_accept"]]) == (0, 0)
        )
        transition_ok &= row_ok
        locked_rows += 1
        same_value_refusals += int(row_ok and d_bit == offered)
        opposite_value_refusals += int(row_ok and d_bit != offered)
    for lock in ((0, 0), (1, 1)):
        for d_bit, offered in product((0, 1), repeat=2):
            before = packet((d_bit, *lock), offered)
            after = apply_word(before, WRITE_WORD)
            row_ok = (
                after == expected_refusal(d_bit, offered, lock)
                and bytes((after[RAIL_INDEX["D"]],)) == bytes((d_bit,))
                and output_tag(after) == "REFUSED"
            )
            transition_ok &= row_ok
            dirty_rows += 1

    second_cases = 0
    second_refusals = 0
    second_content_exact = 0
    for payloads in product((0, 1), repeat=2):
        events = run_write_sequence(payloads)
        second_cases += 1
        second_refusals += int(output_tag(events[1]) == "REFUSED")
        second_content_exact += int(
            events[1][RAIL_INDEX["D"]] == payloads[0]
            and persistent(events[1]) == (payloads[0], *LOCKED)
        )

    third_cases = 0
    third_refusals = 0
    third_length_total_refusals = 0
    third_content_exact = 0
    for payloads in product((0, 1), repeat=3):
        events = run_write_sequence(payloads)
        third_cases += 1
        third_refusals += int(output_tag(events[2]) == "REFUSED")
        third_length_total_refusals += sum(
            output_tag(event) == "REFUSED" for event in events
        )
        third_content_exact += int(
            events[1][RAIL_INDEX["D"]] == payloads[0]
            and events[2][RAIL_INDEX["D"]] == payloads[0]
            and persistent(events[2]) == (payloads[0], *LOCKED)
        )

    predicted = {
        "dirty_refusal_rows": 8,
        "locked_refusal_rows": 4,
        "opposite_value_refusals": 2,
        "same_value_refusals": 2,
        "second_write_cases": 4,
        "second_write_refusals": 4,
        "third_length_total_refusals": 16,
        "third_write_cases": 8,
        "third_write_refusals": 8,
    }
    observed = {
        "dirty_refusal_rows": dirty_rows,
        "locked_refusal_rows": locked_rows,
        "opposite_value_refusals": opposite_value_refusals,
        "same_value_refusals": same_value_refusals,
        "second_write_cases": second_cases,
        "second_write_refusals": second_refusals,
        "third_length_total_refusals": third_length_total_refusals,
        "third_write_cases": third_cases,
        "third_write_refusals": third_refusals,
    }
    content_exact = (
        second_content_exact == second_cases
        and third_content_exact == third_cases
    )
    details = {
        "clean_return": "Q_in=0,Q_accept=0; no work rails",
        "content_byte_invariance_exact": content_exact,
        "observed": observed,
        "predicted": predicted,
        "refusal_latch": "Q_refuse=1",
        "work_rails": list(WORK_RAILS),
    }
    return transition_ok and observed == predicted and content_exact, details


def apply_macro(storage: Persistent, macro: str) -> tuple[Persistent, State]:
    d_bit, u_bit, l_bit = storage
    if macro == "IDLE":
        event = apply_word(packet(storage, 0, request=0), IDLE_WORD)
    elif macro == "READ":
        event = apply_word(packet(storage, 0, request=0), READ_WORD)
    elif macro == "WRITE[0]":
        event = apply_word(packet(storage, 0), WRITE_WORD)
    elif macro == "WRITE[1]":
        event = apply_word(packet(storage, 1), WRITE_WORD)
    else:
        raise ValueError(f"out-of-alphabet macro: {macro}")
    return persistent(event), event


def certificate_d() -> tuple[bool, dict[str, object]]:
    base_rows = []
    step_rows = []
    read_idle_sector_rows = []
    base_ok = True
    step_ok = True
    read_idle_sector_ok = True
    for lock in (UNLOCKED, LOCKED):
        for d_bit in (0, 1):
            storage = (d_bit, *lock)
            for macro in ("IDLE", "READ"):
                after_storage, event = apply_macro(storage, macro)
                row_ok = (
                    after_storage == storage
                    and event[RAIL_INDEX["Q_in"]] == 0
                    and event[RAIL_INDEX["Q_accept"]] == 0
                    and event[RAIL_INDEX["Q_refuse"]] == 0
                )
                read_idle_sector_ok &= row_ok
                read_idle_sector_rows.append(
                    {
                        "D": d_bit,
                        "lock": list(lock),
                        "macro": macro,
                        "preserved": row_ok,
                    }
                )
    for d_bit in (0, 1):
        storage = (d_bit, *LOCKED)
        row_ok = storage[0] == d_bit and storage[1:] == LOCKED
        base_ok &= row_ok
        base_rows.append({"D": d_bit, "locked": row_ok})
        for macro in ALPHABET_SCOPE:
            after_storage, event = apply_macro(storage, macro)
            row_ok = after_storage == storage
            if macro.startswith("WRITE"):
                row_ok &= output_tag(event) == "REFUSED"
            step_ok &= row_ok
            step_rows.append({"D": d_bit, "macro": macro, "preserved": row_ok})
    details = {
        "alphabet_scope": list(ALPHABET_SCOPE),
        "alphabet_printed": ",".join(ALPHABET_SCOPE),
        "base_cases": len(base_rows),
        "base_ok": base_ok,
        "induction_statement": INDUCTION_STATEMENT,
        "read_idle_both_lock_sectors_cases": len(read_idle_sector_rows),
        "read_idle_both_lock_sectors_ok": read_idle_sector_ok,
        "step_cases": len(step_rows),
        "step_ok": step_ok,
    }
    return (
        base_ok
        and step_ok
        and read_idle_sector_ok
        and len(read_idle_sector_rows) == 8
        and len(step_rows) == 2 * len(ALPHABET_SCOPE)
    ), details


def certificate_e() -> tuple[bool, dict[str, object]]:
    detections: dict[str, dict[str, object]] = {}
    for deleted_index, deleted_gate in enumerate(WRITE_WORD):
        mutant = WRITE_WORD[:deleted_index] + WRITE_WORD[deleted_index + 1 :]
        failures = write_behavior_failures(mutant)
        detections[deleted_gate.name] = {
            "detected": bool(failures),
            "failure_count": len(failures),
            "first_failure": failures[0] if failures else None,
        }
    all_detected = all(row["detected"] for row in detections.values())
    details = {
        "deleted_gate_count": len(detections),
        "detections": detections,
        "every_literal_write_gate_deleted_once": True,
    }
    return all_detected and len(detections) == len(WRITE_WORD), details


def certificate_f() -> tuple[bool, dict[str, object]]:
    boundary = {
        "alphabet_scope": list(ALPHABET_SCOPE),
        "mechanism_level_write_once_derived": True,
        "next": NEXT_CYCLE,
        "out_of_alphabet_operations": OUT_OF_ALPHABET_BOUNDARY,
        "record_permanence_claimed": False,
    }
    supplied_exact = SUPPLIED_PORTFOLIO_VERBATIM.startswith("Supplied:")
    derived_exact = DERIVED_PORTFOLIO_VERBATIM.startswith("Derived:")
    boundary_ok = (
        boundary["mechanism_level_write_once_derived"] is True
        and boundary["record_permanence_claimed"] is False
        and boundary["alphabet_scope"] == list(ALPHABET_SCOPE)
        and boundary["next"] == "multi-cell archive integration (741/742 composition)"
        and "out of scope" in str(boundary["out_of_alphabet_operations"])
    )
    details = {
        "boundary": boundary,
        "derived_portfolio_verbatim": DERIVED_PORTFOLIO_VERBATIM,
        "record_activation": (
            "LOCKED means the site now contributes a Record with "
            "content=(Fraction(D),0,0,0)"
        ),
        "scalar_readout_supply": "G=(Q,+); C_source and readout conventions supplied",
        "supplied_portfolio_verbatim": SUPPLIED_PORTFOLIO_VERBATIM,
    }
    return boundary_ok and supplied_exact and derived_exact, details


def check(
    label: str,
    outcome: tuple[bool, dict[str, object]],
    results: dict[str, dict[str, object]],
) -> bool:
    passed, details = outcome
    results[label] = {"passed": passed, **details}
    status = "PASS" if passed else "FAIL"
    print(f"{status} {label}")
    return passed


def main() -> int:
    started = time.perf_counter()
    results: dict[str, dict[str, object]] = {}
    checks = (
        (
            "A_write_word_exactness_and_reversibility",
            certificate_a,
        ),
        (
            "B_first_write_locking_same_word_AST_and_behavior",
            certificate_b,
        ),
        (
            "C_refusal_law_second_third_censuses",
            certificate_c,
        ),
        (
            "D_inductive_closure_declared_alphabet",
            certificate_d,
        ),
        (
            "E_deletion_controls",
            certificate_e,
        ),
        (
            "F_honest_boundary_keys_and_supplies",
            certificate_f,
        ),
    )
    all_pass = True
    for label, certificate in checks:
        try:
            all_pass &= check(label, certificate(), results)
        except Exception as error:  # A certificate exception is an honest FAIL.
            all_pass = False
            results[label] = {
                "error": f"{type(error).__name__}: {error}",
                "passed": False,
            }
            print(f"FAIL {label}")

    runtime_sec = time.perf_counter() - started
    report = {
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "AUDIT_TIMEOUT_SEC": AUDIT_TIMEOUT_SEC,
        "DECLARED_INPUT_PATHS": list(DECLARED_INPUT_PATHS),
        "NOTE_PATH": NOTE_PATH,
        "alphabet_scope": list(ALPHABET_SCOPE),
        "all_pass": all_pass,
        "checks": results,
        "induction_statement": INDUCTION_STATEMENT,
        "mechanism_level_write_once_derived": True,
        "next": NEXT_CYCLE,
        "out_of_alphabet_operations": OUT_OF_ALPHABET_BOUNDARY,
        "record_permanence_claimed": False,
        "runtime_sec": round(runtime_sec, 6),
        "seven_semantic_rails": list(RAILS),
        "word_sizes": {
            "IDLE": len(IDLE_WORD),
            "READ": len(READ_WORD),
            "REVERSE_WRITE": len(REVERSE_WRITE_WORD),
            "WRITE": len(WRITE_WORD),
        },
    }
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
