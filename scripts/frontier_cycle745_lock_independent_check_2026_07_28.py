#!/usr/bin/env python3
"""Independent bounded checker for the Cycle 745 enforced dual-rail lock."""

import ast
from dataclasses import dataclass
from itertools import product
import json
from pathlib import Path
import sys
import time
from typing import Callable


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/ENFORCED_DUAL_RAIL_LOCK_CYCLE745_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py",
)

BLOCKLIST = ("frontier_cycle745_enforced_dual_rail_lock_2026_07_28",)

EXPECTED_RAILS = ("D", "V", "U", "L", "Q_in", "Q_accept", "Q_refuse")
EXPECTED_LAYOUT = {
    "D": (0, 0, 0),
    "V": (1, 0, 0),
    "U": (2, 0, 0),
    "L": (2, 1, 0),
    "Q_in": (3, 1, 0),
    "Q_accept": (4, 1, 0),
    "Q_refuse": (3, 2, 0),
}
EXPECTED_ALPHABET = ("IDLE", "READ", "WRITE[0]", "WRITE[1]")
UNLOCKED = (1, 0)
LOCKED = (0, 1)

State = tuple[int, ...]
Persistent = tuple[int, int, int]
Control = tuple[str, int]


@dataclass(frozen=True)
class GateData:
    """An independently decoded, inert gate description."""

    name: str
    operation: str
    targets: tuple[str, ...]
    controls: tuple[Control, ...]


@dataclass(frozen=True)
class Extracted:
    """Only the declarations needed by the independent checks."""

    rails: tuple[str, ...]
    layout: dict[str, tuple[int, int, int]]
    write_word: tuple[GateData, ...]
    read_word: tuple[GateData, ...]
    idle_word: tuple[GateData, ...]
    alphabet: tuple[str, ...]
    primary_audit_inputs: tuple[object, ...]
    frozen_census: dict[str, int]
    boundary: dict[str, bool]
    boundary_occurrences: dict[str, tuple[object, ...]]
    same_word_ast: bool
    forbidden_claim_hits: tuple[str, ...]


def _named_assignment(
    nodes: list[ast.stmt], name: str, *, literal: bool = False
) -> object:
    matches: list[ast.expr] = []
    for node in nodes:
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
                matches.append(node.value)
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name) and node.target.id == name:
                if node.value is None:
                    raise ValueError(f"{name} has no value")
                matches.append(node.value)
    if len(matches) != 1:
        raise ValueError(f"expected one assignment for {name}, found {len(matches)}")
    return ast.literal_eval(matches[0]) if literal else matches[0]


def _function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise ValueError(f"expected one function {name}, found {len(matches)}")
    return matches[0]


def _nested_assignment(
    function: ast.FunctionDef, name: str, *, literal: bool = False
) -> object:
    matches: list[ast.expr] = []
    for node in ast.walk(function):
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name for target in node.targets
        ):
            matches.append(node.value)
    if len(matches) != 1:
        raise ValueError(
            f"expected one assignment for {name} in {function.name}, found {len(matches)}"
        )
    return ast.literal_eval(matches[0]) if literal else matches[0]


def _literal_tuple(value: object, label: str) -> tuple[object, ...]:
    if not isinstance(value, tuple):
        raise ValueError(f"{label} is not a literal tuple")
    return value


def _decode_gate(node: ast.expr) -> GateData:
    if not (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "Gate"
        and 3 <= len(node.args) <= 4
    ):
        raise ValueError("word element is not a literal Gate(...) call")
    if node.keywords:
        raise ValueError("gate uses unreviewed keyword or expansion syntax")
    name = ast.literal_eval(node.args[0])
    operation = ast.literal_eval(node.args[1])
    targets = ast.literal_eval(node.args[2])
    controls = ast.literal_eval(node.args[3]) if len(node.args) == 4 else ()
    if not isinstance(name, str) or operation not in ("X", "SWAP"):
        raise ValueError("gate name or operation is invalid")
    if not (
        isinstance(targets, tuple)
        and all(isinstance(target, str) for target in targets)
    ):
        raise ValueError(f"{name}: targets are not a literal string tuple")
    if not (
        isinstance(controls, tuple)
        and all(
            isinstance(control, tuple)
            and len(control) == 2
            and isinstance(control[0], str)
            and control[1] in (0, 1)
            for control in controls
        )
    ):
        raise ValueError(f"{name}: controls are not literal binary controls")
    return GateData(name, operation, targets, controls)


def _decode_word(tree: ast.Module, name: str) -> tuple[GateData, ...]:
    node = _named_assignment(tree.body, name)
    if not isinstance(node, ast.Tuple):
        raise ValueError(f"{name} is not a literal tuple")
    return tuple(_decode_gate(element) for element in node.elts)


def _first_write_domain(tree: ast.Module) -> tuple[object, ...]:
    function = _function(tree, "certificate_b")
    matches: list[tuple[object, ...]] = []
    for node in ast.walk(function):
        if (
            isinstance(node, ast.For)
            and isinstance(node.target, ast.Name)
            and node.target.id == "offered"
        ):
            value = ast.literal_eval(node.iter)
            if isinstance(value, tuple):
                matches.append(value)
    if len(matches) != 1:
        raise ValueError(
            f"expected one literal first-write offered domain, found {len(matches)}"
        )
    return matches[0]


def _dict_constants_for_keys(
    tree: ast.Module, keys: tuple[str, ...]
) -> dict[str, tuple[object, ...]]:
    found: dict[str, list[object]] = {key: [] for key in keys}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for key_node, value_node in zip(node.keys, node.values):
            if key_node is None:
                continue
            try:
                key = ast.literal_eval(key_node)
            except (ValueError, TypeError):
                continue
            if key not in found:
                continue
            try:
                value = ast.literal_eval(value_node)
            except (ValueError, TypeError):
                value = "<nonliteral>"
            found[key].append(value)
    return {key: tuple(values) for key, values in found.items()}


def _extract_boundary(tree: ast.Module) -> dict[str, bool]:
    function = _function(tree, "certificate_f")
    node = _nested_assignment(function, "boundary")
    if not isinstance(node, ast.Dict):
        raise ValueError("certificate_f boundary is not a literal-key dict")
    selected: dict[str, bool] = {}
    for key_node, value_node in zip(node.keys, node.values):
        if key_node is None:
            continue
        key = ast.literal_eval(key_node)
        if key not in (
            "mechanism_level_write_once_derived",
            "record_permanence_claimed",
        ):
            continue
        value = ast.literal_eval(value_node)
        if not isinstance(value, bool):
            raise ValueError(f"boundary key {key} is not a literal bool")
        selected[key] = value
    return selected


def extraction(source: str) -> tuple[bool, dict[str, object], Extracted]:
    tree = ast.parse(source, filename=AUDIT_INPUT_PATHS[0])
    rails_raw = _literal_tuple(
        _named_assignment(tree.body, "RAILS", literal=True), "RAILS"
    )
    rails = tuple(rails_raw)
    if not all(isinstance(rail, str) for rail in rails):
        raise ValueError("RAILS contains a non-string entry")

    layout_raw = _named_assignment(tree.body, "SITE_LAYOUT", literal=True)
    if not isinstance(layout_raw, dict):
        raise ValueError("SITE_LAYOUT is not a literal dict")
    layout = dict(layout_raw)

    alphabet_raw = _literal_tuple(
        _named_assignment(tree.body, "ALPHABET_SCOPE", literal=True),
        "ALPHABET_SCOPE",
    )
    alphabet = tuple(alphabet_raw)
    if not all(isinstance(macro, str) for macro in alphabet):
        raise ValueError("ALPHABET_SCOPE contains a non-string entry")

    primary_audit_inputs = _literal_tuple(
        _named_assignment(tree.body, "AUDIT_INPUT_PATHS", literal=True),
        "primary AUDIT_INPUT_PATHS",
    )
    write_word = _decode_word(tree, "WRITE_WORD")
    read_word = _decode_word(tree, "READ_WORD")
    idle_word = _decode_word(tree, "IDLE_WORD")

    predicted_raw = _nested_assignment(
        _function(tree, "certificate_c"), "predicted", literal=True
    )
    if not isinstance(predicted_raw, dict):
        raise ValueError("predicted census is not a literal dict")
    predicted = dict(predicted_raw)
    offered_domain = _first_write_domain(tree)
    frozen_census = {
        "reversible_states": 1 << len(rails),
        "first_write_cases": len(offered_domain),
        "second_write_cases": predicted.get("second_write_cases", -1),
        "second_write_refusals": predicted.get("second_write_refusals", -1),
        "third_write_cases": predicted.get("third_write_cases", -1),
        "third_write_refusals": predicted.get("third_write_refusals", -1),
        "locked_refusal_rows": predicted.get("locked_refusal_rows", -1),
        "dirty_refusal_rows": predicted.get("dirty_refusal_rows", -1),
        "deletion_controls": len(write_word),
    }
    if not all(isinstance(value, int) for value in frozen_census.values()):
        raise ValueError("frozen census contains a non-integer")

    gate_names = tuple(gate.name for gate in write_word)
    ordered_names = ("payload_copy", "accept_route", "lock_transfer")
    same_word_ast = (
        all(name in gate_names for name in ordered_names)
        and gate_names.index("payload_copy")
        < gate_names.index("accept_route")
        < gate_names.index("lock_transfer")
        and not any(
            isinstance(node, ast.Name) and node.id == "LOCK_WORD"
            for node in ast.walk(tree)
        )
    )
    boundary = _extract_boundary(tree)
    boundary_occurrences = _dict_constants_for_keys(
        tree,
        (
            "mechanism_level_write_once_derived",
            "record_permanence_claimed",
        ),
    )
    prohibited_phrases = (
        "axiom-level permanence",
        "axiom level permanence",
        "axiomatic permanence",
        "record permanence is derived",
        "record permanence derived",
    )
    forbidden_claim_hits = tuple(
        value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
        for value in (node.value,)
        if any(phrase in value.lower() for phrase in prohibited_phrases)
    )

    extracted = Extracted(
        rails=rails,
        layout=layout,
        write_word=write_word,
        read_word=read_word,
        idle_word=idle_word,
        alphabet=alphabet,
        primary_audit_inputs=primary_audit_inputs,
        frozen_census=frozen_census,
        boundary=boundary,
        boundary_occurrences=boundary_occurrences,
        same_word_ast=same_word_ast,
        forbidden_claim_hits=forbidden_claim_hits,
    )

    expected_census = {
        "reversible_states": 128,
        "first_write_cases": 2,
        "second_write_cases": 4,
        "second_write_refusals": 4,
        "third_write_cases": 8,
        "third_write_refusals": 8,
        "locked_refusal_rows": 4,
        "dirty_refusal_rows": 8,
        "deletion_controls": 8,
    }
    layout_values = tuple(layout.values())
    rail_references_ok = all(
        target in rails and all(control_name in rails for control_name, _ in gate.controls)
        for gate in write_word + read_word
        for target in gate.targets
    )
    word_shapes_ok = all(
        (gate.operation == "X" and len(gate.targets) == 1)
        or (gate.operation == "SWAP" and len(gate.targets) == 2)
        for gate in write_word + read_word
    )
    passed = (
        rails == EXPECTED_RAILS
        and layout == EXPECTED_LAYOUT
        and set(layout) == set(rails)
        and len(set(layout_values)) == 7
        and len(write_word) == 8
        and len(read_word) == 1
        and len(idle_word) == 0
        and len(set(gate_names)) == len(gate_names)
        and rail_references_ok
        and word_shapes_ok
        and alphabet == EXPECTED_ALPHABET
        and primary_audit_inputs == ("scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py",)
        and frozen_census == expected_census
        and same_word_ast
        and boundary
        == {
            "mechanism_level_write_once_derived": True,
            "record_permanence_claimed": False,
        }
    )
    details: dict[str, object] = {
        "alphabet": list(alphabet),
        "audit_tuple_literal": list(primary_audit_inputs),
        "census": frozen_census,
        "layout_sites": len(layout),
        "rails": list(rails),
        "read_gates": [gate.name for gate in read_word],
        "same_word_ast": same_word_ast,
        "write_gates": list(gate_names),
    }
    return passed, details, extracted


def _indices(extracted: Extracted) -> dict[str, int]:
    return {rail: index for index, rail in enumerate(extracted.rails)}


def _state_from_values(extracted: Extracted, values: dict[str, int]) -> State:
    state = tuple(values.get(rail, 0) for rail in extracted.rails)
    if len(state) != 7 or any(bit not in (0, 1) for bit in state):
        raise ValueError("constructed state is not seven binary rails")
    return state


def _apply_gate(
    extracted: Extracted, state: State, gate: GateData
) -> State:
    indices = _indices(extracted)
    if len(state) != len(extracted.rails) or any(bit not in (0, 1) for bit in state):
        raise ValueError("simulator received an invalid state")
    enabled = all(state[indices[name]] == value for name, value in gate.controls)
    if not enabled:
        return state
    output = list(state)
    if gate.operation == "X" and len(gate.targets) == 1:
        output[indices[gate.targets[0]]] ^= 1
    elif gate.operation == "SWAP" and len(gate.targets) == 2:
        left = indices[gate.targets[0]]
        right = indices[gate.targets[1]]
        output[left], output[right] = output[right], output[left]
    else:
        raise ValueError(f"unsupported decoded gate {gate.name}")
    return tuple(output)


def _apply_word(
    extracted: Extracted, state: State, word: tuple[GateData, ...]
) -> State:
    output = state
    for gate in word:
        output = _apply_gate(extracted, output, gate)
    return output


def _packet(
    extracted: Extracted,
    storage: Persistent,
    offered: int,
    request: int = 1,
) -> State:
    d_bit, u_bit, l_bit = storage
    return _state_from_values(
        extracted,
        {
            "D": d_bit,
            "V": offered,
            "U": u_bit,
            "L": l_bit,
            "Q_in": request,
            "Q_accept": 0,
            "Q_refuse": 0,
        },
    )


def _persistent(extracted: Extracted, state: State) -> Persistent:
    indices = _indices(extracted)
    return (
        state[indices["D"]],
        state[indices["U"]],
        state[indices["L"]],
    )


def _tag(extracted: Extracted, state: State) -> str:
    indices = _indices(extracted)
    route = tuple(
        state[indices[name]] for name in ("Q_in", "Q_accept", "Q_refuse")
    )
    if route == (0, 1, 0):
        return "ACCEPTED"
    if route == (0, 0, 1):
        return "REFUSED"
    return "DIRTY"


def _expected_first(extracted: Extracted, offered: int) -> State:
    return _state_from_values(
        extracted,
        {
            "D": offered,
            "V": offered,
            "U": 0,
            "L": 1,
            "Q_in": 0,
            "Q_accept": 1,
            "Q_refuse": 0,
        },
    )


def _expected_refusal(
    extracted: Extracted, d_bit: int, offered: int, lock: tuple[int, int]
) -> State:
    return _state_from_values(
        extracted,
        {
            "D": d_bit,
            "V": offered,
            "U": lock[0],
            "L": lock[1],
            "Q_in": 0,
            "Q_accept": 0,
            "Q_refuse": 1,
        },
    )


def _run_write_sequence(
    extracted: Extracted, payloads: tuple[int, ...]
) -> tuple[State, ...]:
    storage: Persistent = (0, *UNLOCKED)
    events: list[State] = []
    for offered in payloads:
        event = _apply_word(
            extracted, _packet(extracted, storage, offered), extracted.write_word
        )
        events.append(event)
        storage = _persistent(extracted, event)
    return tuple(events)


def word_recount(extracted: Extracted) -> tuple[bool, dict[str, object]]:
    states = tuple(product((0, 1), repeat=len(extracted.rails)))
    outputs = tuple(
        _apply_word(extracted, state, extracted.write_word) for state in states
    )
    reverse_word = tuple(reversed(extracted.write_word))
    reverse_exact = all(
        _apply_word(extracted, output, reverse_word) == state
        for state, output in zip(states, outputs)
    )
    involutions = all(
        _apply_gate(extracted, _apply_gate(extracted, state, gate), gate) == state
        for gate in extracted.write_word
        for state in states
    )

    first_accepted = 0
    same_word_lock = 0
    for offered in (0, 1):
        event = _apply_word(
            extracted,
            _packet(extracted, (0, *UNLOCKED), offered),
            extracted.write_word,
        )
        exact = event == _expected_first(extracted, offered)
        first_accepted += int(exact and _tag(extracted, event) == "ACCEPTED")
        same_word_lock += int(
            exact and _persistent(extracted, event) == (offered, *LOCKED)
        )

    locked_rows = 0
    locked_byte_exact = 0
    for d_bit, offered in product((0, 1), repeat=2):
        event = _apply_word(
            extracted,
            _packet(extracted, (d_bit, *LOCKED), offered),
            extracted.write_word,
        )
        exact = event == _expected_refusal(extracted, d_bit, offered, LOCKED)
        locked_rows += int(exact and _tag(extracted, event) == "REFUSED")
        locked_byte_exact += int(
            exact
            and bytes((event[_indices(extracted)["D"]],)) == bytes((d_bit,))
        )

    dirty_rows = 0
    for lock in ((0, 0), (1, 1)):
        for d_bit, offered in product((0, 1), repeat=2):
            event = _apply_word(
                extracted,
                _packet(extracted, (d_bit, *lock), offered),
                extracted.write_word,
            )
            dirty_rows += int(
                event == _expected_refusal(extracted, d_bit, offered, lock)
                and _tag(extracted, event) == "REFUSED"
            )

    second_refusals = 0
    second_byte_exact = 0
    for payloads in product((0, 1), repeat=2):
        events = _run_write_sequence(extracted, payloads)
        second_refusals += int(_tag(extracted, events[1]) == "REFUSED")
        second_byte_exact += int(
            bytes((_persistent(extracted, events[1])[0],))
            == bytes((payloads[0],))
            and _persistent(extracted, events[1]) == (payloads[0], *LOCKED)
        )

    third_refusals = 0
    third_byte_exact = 0
    for payloads in product((0, 1), repeat=3):
        events = _run_write_sequence(extracted, payloads)
        third_refusals += int(_tag(extracted, events[2]) == "REFUSED")
        third_byte_exact += int(
            all(
                bytes((_persistent(extracted, event)[0],))
                == bytes((payloads[0],))
                for event in events[1:]
            )
            and _persistent(extracted, events[2]) == (payloads[0], *LOCKED)
        )

    observed = {
        "distinct_reversible_outputs": len(set(outputs)),
        "first_accepted": first_accepted,
        "same_word_lock": same_word_lock,
        "locked_refusal_rows": locked_rows,
        "dirty_refusal_rows": dirty_rows,
        "second_write_refusals": second_refusals,
        "third_write_refusals": third_refusals,
    }
    passed = (
        len(states) == 128
        and len(set(outputs)) == 128
        and reverse_exact
        and involutions
        and first_accepted == 2
        and same_word_lock == 2
        and extracted.same_word_ast
        and locked_rows == 4
        and locked_byte_exact == 4
        and dirty_rows == 8
        and second_refusals == 4
        and second_byte_exact == 4
        and third_refusals == 8
        and third_byte_exact == 8
    )
    return passed, {
        "all_states": len(states),
        "gate_involutions": involutions,
        "locked_content_byte_exact": {
            "direct": locked_byte_exact,
            "second": second_byte_exact,
            "third": third_byte_exact,
        },
        "observed": observed,
        "reverse_exact": reverse_exact,
    }


def _apply_macro(
    extracted: Extracted, storage: Persistent, macro: str
) -> tuple[Persistent, State]:
    if macro == "IDLE":
        event = _apply_word(
            extracted,
            _packet(extracted, storage, 0, request=0),
            extracted.idle_word,
        )
    elif macro == "READ":
        event = _apply_word(
            extracted,
            _packet(extracted, storage, 0, request=0),
            extracted.read_word,
        )
    elif macro == "WRITE[0]":
        event = _apply_word(
            extracted, _packet(extracted, storage, 0), extracted.write_word
        )
    elif macro == "WRITE[1]":
        event = _apply_word(
            extracted, _packet(extracted, storage, 1), extracted.write_word
        )
    else:
        raise ValueError(f"undeclared macro {macro!r}")
    return _persistent(extracted, event), event


def induction_recount(extracted: Extracted) -> tuple[bool, dict[str, object]]:
    # Base cases are recomputed directly from post-first-write events.
    base_passes = 0
    for offered in (0, 1):
        post_first = _apply_word(
            extracted,
            _packet(extracted, (0, *UNLOCKED), offered),
            extracted.write_word,
        )
        storage = _persistent(extracted, post_first)
        base_passes += int(
            storage == (offered, *LOCKED)
            and bytes((storage[0],)) == bytes((offered,))
        )

    # Step cases start independently from every binary locked payload.
    step_passes = 0
    step_cases = 0
    for d_bit in (0, 1):
        before: Persistent = (d_bit, *LOCKED)
        for macro in extracted.alphabet:
            after, _ = _apply_macro(extracted, before, macro)
            step_cases += 1
            step_passes += int(
                after == before
                and bytes((after[0],)) == bytes((before[0],))
                and after[1:] == LOCKED
            )

    altered: list[dict[str, object]] = []
    composition_cases = 0
    for length in range(1, 5):
        for words in product(extracted.alphabet, repeat=length):
            for d_bit in (0, 1):
                original: Persistent = (d_bit, *LOCKED)
                storage = original
                altered_during_composition = False
                for macro in words:
                    storage, _ = _apply_macro(extracted, storage, macro)
                    if (
                        bytes((storage[0],)) != bytes((original[0],))
                        or storage[1:] != LOCKED
                    ):
                        altered_during_composition = True
                composition_cases += 1
                if altered_during_composition or storage != original:
                    if len(altered) < 8:
                        altered.append(
                            {
                                "initial_D": d_bit,
                                "words": list(words),
                                "final": list(storage),
                            }
                        )

    expected_compositions = 2 * sum(
        len(extracted.alphabet) ** length for length in range(1, 5)
    )
    passed = (
        extracted.alphabet == EXPECTED_ALPHABET
        and base_passes == 2
        and step_cases == 8
        and step_passes == 8
        and composition_cases == 680
        and composition_cases == expected_compositions
        and not altered
    )
    return passed, {
        "adversarial_alterations": altered,
        "base": f"{base_passes}/2",
        "composition_cases": composition_cases,
        "composition_max_length": 4,
        "step": f"{step_passes}/{step_cases}",
    }


def _behavior_failures(
    extracted: Extracted, word: tuple[GateData, ...]
) -> list[str]:
    failures: list[str] = []
    for offered in (0, 1):
        event = _apply_word(
            extracted, _packet(extracted, (0, *UNLOCKED), offered), word
        )
        if event != _expected_first(extracted, offered):
            failures.append(f"first-{offered}")
    for d_bit, offered in product((0, 1), repeat=2):
        event = _apply_word(
            extracted, _packet(extracted, (d_bit, *LOCKED), offered), word
        )
        if event != _expected_refusal(extracted, d_bit, offered, LOCKED):
            failures.append(f"locked-{d_bit}-{offered}")
    for lock in ((0, 0), (1, 1)):
        for d_bit, offered in product((0, 1), repeat=2):
            event = _apply_word(
                extracted, _packet(extracted, (d_bit, *lock), offered), word
            )
            if event != _expected_refusal(extracted, d_bit, offered, lock):
                failures.append(f"dirty-{lock[0]}{lock[1]}-{d_bit}-{offered}")
    return failures


def deletion_recount(extracted: Extracted) -> tuple[bool, dict[str, object]]:
    detections: list[dict[str, object]] = []
    for index, deleted in enumerate(extracted.write_word):
        mutant = extracted.write_word[:index] + extracted.write_word[index + 1 :]
        failures = _behavior_failures(extracted, mutant)
        detections.append(
            {
                "deleted": deleted.name,
                "detected": bool(failures),
                "failure_count": len(failures),
                "first_failure": failures[0] if failures else None,
            }
        )
    detected = sum(bool(row["detected"]) for row in detections)
    passed = (
        len(extracted.write_word) == 8
        and len(detections) == 8
        and detected == 8
    )
    return passed, {
        "deleted_gate_count": len(detections),
        "detected": detected,
        "detections": detections,
    }


def discipline(extracted: Extracted) -> tuple[bool, dict[str, object]]:
    loaded_blocklist = tuple(
        module_name
        for module_name in sys.modules
        if any(
            module_name == blocked or module_name.endswith("." + blocked)
            for blocked in BLOCKLIST
        )
    )
    expected_boundary_occurrences = {
        "mechanism_level_write_once_derived": (True, True),
        "record_permanence_claimed": (False, False),
    }
    audit_literal_ok = (
        isinstance(AUDIT_INPUT_PATHS, tuple)
        and AUDIT_INPUT_PATHS
        == ("scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py",)
    )
    passed = (
        audit_literal_ok
        and extracted.primary_audit_inputs == ("scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py",)
        and not loaded_blocklist
        and extracted.boundary
        == {
            "mechanism_level_write_once_derived": True,
            "record_permanence_claimed": False,
        }
        and extracted.boundary_occurrences == expected_boundary_occurrences
        and not extracted.forbidden_claim_hits
    )
    return passed, {
        "audit_input_paths": list(AUDIT_INPUT_PATHS),
        "audit_tuple_literal_ok": audit_literal_ok,
        "blocklist": list(BLOCKLIST),
        "blocked_modules_loaded": list(loaded_blocklist),
        "boundary": extracted.boundary,
        "boundary_occurrences": {
            key: list(values)
            for key, values in extracted.boundary_occurrences.items()
        },
        "forbidden_axiom_claim_hits": list(extracted.forbidden_claim_hits),
        "primary_audit_input_paths": list(extracted.primary_audit_inputs),
    }


def _record(
    label: str,
    outcome: tuple[bool, dict[str, object]],
    results: dict[str, dict[str, object]],
) -> bool:
    passed, details = outcome
    results[label] = {"passed": bool(passed), **details}
    print(f"{'PASS' if passed else 'FAIL'} {label}")
    return bool(passed)


def _honest_failure(
    label: str, error: Exception, results: dict[str, dict[str, object]]
) -> bool:
    message = f"{type(error).__name__}: {error}"
    results[label] = {"passed": False, "error": message[:1000]}
    print(f"FAIL {label}")
    return False


def main() -> int:
    started = time.perf_counter()
    results: dict[str, dict[str, object]] = {}
    root = Path(__file__).resolve().parent.parent
    primary_path = root / AUDIT_INPUT_PATHS[0]

    extracted: Extracted | None = None
    all_pass = True
    try:
        source = primary_path.read_text(encoding="utf-8")
        extraction_outcome = extraction(source)
        extraction_passed, extraction_details, extracted = extraction_outcome
        all_pass &= _record(
            "extraction",
            (extraction_passed, extraction_details),
            results,
        )
    except Exception as error:
        all_pass = _honest_failure("extraction", error, results)

    certificates: tuple[
        tuple[str, Callable[[Extracted], tuple[bool, dict[str, object]]]], ...
    ] = (
        ("word_recount", word_recount),
        ("induction_recount", induction_recount),
        ("deletion_recount", deletion_recount),
        ("discipline", discipline),
    )
    for label, certificate in certificates:
        if extracted is None:
            all_pass = False
            results[label] = {
                "passed": False,
                "error": "extraction unavailable",
            }
            print(f"FAIL {label}")
            continue
        try:
            all_pass &= _record(label, certificate(extracted), results)
        except Exception as error:
            all_pass = _honest_failure(label, error, results)

    runtime_sec = time.perf_counter() - started
    report = {
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "AUDIT_TIMEOUT_SEC": AUDIT_TIMEOUT_SEC,
        "NOTE_PATH": NOTE_PATH,
        "all_pass": bool(all_pass),
        "checks": results,
        "runtime_sec": round(runtime_sec, 6),
        "stdout_limit_bytes": 150_000,
    }
    encoded = json.dumps(report, sort_keys=True, separators=(",", ":"))
    if len(encoded.encode("utf-8")) >= 150_000:
        print("FAIL stdout_bound")
        return 1
    print(encoded)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
