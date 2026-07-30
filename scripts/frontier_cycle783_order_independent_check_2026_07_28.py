#!/usr/bin/env python3
"""Independent adversarial checker for Cycle 783's functional-order mapping.

The Cycle-783 primary and the Cycle-752 pair are inert text/AST inputs.  This
checker independently reconstructs the held 752 event surface from the two
landed executable imports, attacks the item/value mapping, searches a bounded
family of other covariant functionals, and recounts every fixed-order edge
orientation class with a local bit simulator.
"""
from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
from time import perf_counter
import types
from typing import Callable


# Literal by audit contract: the Cycle-752 pair plus the only two landed
# modules this checker imports for executable fixture objects.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle752_lawful_adjacency_attempt_2026_07_28.py",
    "scripts/frontier_cycle752_adjacency_independent_check_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle735_separated_pair_lawful_control_2026_07_28.py",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "fb50873dd30a0d580bfd03a19cc4613dd9517816e1e9aab7adba6bd77ed2c2a1",
    AUDIT_INPUT_PATHS[1]:
        "cfff6c6c8acf971c78682caec55f2bd70d661cd21e70d619ef1e1087fc412fd2",
    AUDIT_INPUT_PATHS[2]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[3]:
        "2bfc05e703ab75663360361296fe3f816884faf5397ac04a3e55e277244e5ce7",
}
PRIMARY_PATH = (
    "scripts/frontier_cycle783_functional_order_w2_2026_07_28.py"
)
PRIMARY_MODULE = "frontier_cycle783_functional_order_w2_2026_07_28"
TEXT_ONLY_MODULES = (
    PRIMARY_MODULE,
    "frontier_cycle752_lawful_adjacency_attempt_2026_07_28",
    "frontier_cycle752_adjacency_independent_check_2026_07_28",
)
RING_STATIONS = 11
FIXTURE_BANKS = 2
EXPECTED_COUNT = 2
ROUTE3_FIXED_Q_ORDER = (1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2)
STDOUT_LIMIT_BYTES = 150 * 1024
RUNTIME_LIMIT_SEC = 1500.0


class _TextOnlyImportBlocker:
    """Fail closed if an inert audit source is imported executably."""

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        del path, target
        if fullname in TEXT_ONLY_MODULES:
            raise ImportError(f"{fullname} is text/AST-only audit data")
        return None


_IMPORT_BLOCKER = _TextOnlyImportBlocker()
sys.meta_path.insert(0, _IMPORT_BLOCKER)

# S735.held_fixture_data does not access either historical certificate module.
for _shim_name in (
    "frontier_cycle734_paired_excitation_genesis_2026_07_28",
    "frontier_cycle731_token_count_certificate_2026_07_28",
):
    sys.modules.setdefault(_shim_name, types.ModuleType(_shim_name))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle735_separated_pair_lawful_control_2026_07_28 as S735


ROOT = Path(__file__).resolve().parents[1]
CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def emit(label: str, value: object) -> None:
    OUTPUT_LINES.append(
        f"{label}={json.dumps(value, sort_keys=True, separators=(',', ':'))}"
    )


def check(label: str, condition: bool, findings: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: "
        f"{json.dumps(findings, sort_keys=True, separators=(',', ':'))}"
    )
    return passed


def _assignment_value(tree: ast.AST, name: str) -> ast.expr:
    rows = []
    for node in getattr(tree, "body", ()):
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            rows.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            rows.append(node.value)
    if len(rows) != 1:
        raise AssertionError(("assignment census", name, len(rows)))
    return rows[0]


def _function(tree: ast.AST, name: str) -> ast.FunctionDef:
    rows = [
        node
        for node in getattr(tree, "body", ())
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(rows) != 1:
        raise AssertionError(("function census", name, len(rows)))
    return rows[0]


def command_output(arguments: tuple[str, ...]) -> str:
    completed = subprocess.run(
        arguments,
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def source_and_blocklist_control() -> dict[str, object]:
    primary_bytes = (ROOT / PRIMARY_PATH).read_bytes()
    primary_tree = ast.parse(
        primary_bytes.decode("utf-8"), filename=PRIMARY_PATH
    )
    own_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=__file__
    )
    observed = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    head_blobs = {
        path: command_output(("git", "ls-tree", "HEAD", path)).split()[2]
        for path in AUDIT_INPUT_PATHS
    }
    own_literal = ast.literal_eval(
        _assignment_value(own_tree, "AUDIT_INPUT_PATHS")
    )
    primary_literal = ast.literal_eval(
        _assignment_value(primary_tree, "AUDIT_INPUT_PATHS")
    )
    imported_audit_modules = tuple(
        alias.name
        for node in ast.walk(own_tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    )
    executable_expected = (
        "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        "frontier_cycle735_separated_pair_lawful_control_2026_07_28",
    )
    return {
        "audit_input_paths_literal": own_literal,
        "primary_declared_inputs": primary_literal,
        "observed_sha256": observed,
        "expected_sha256": EXPECTED_SHA256,
        "anchors_match": observed == EXPECTED_SHA256,
        "all_inputs_landed": all(head_blobs.values()),
        "head_blobs": head_blobs,
        "head": command_output(("git", "rev-parse", "HEAD")),
        "primary_sha256": sha256(primary_bytes).hexdigest(),
        "primary_parsed_as_ast": isinstance(primary_tree, ast.Module),
        "executable_audit_imports": imported_audit_modules,
        "executable_imports_exact":
            imported_audit_modules == executable_expected,
        "text_only_modules": TEXT_ONLY_MODULES,
        "text_only_absent_from_sys_modules": all(
            name not in sys.modules for name in TEXT_ONLY_MODULES
        ),
        "blocker_active": _IMPORT_BLOCKER in sys.meta_path,
        "literal_exact": own_literal == AUDIT_INPUT_PATHS,
        "matches_primary_bounded_set":
            tuple(primary_literal) == AUDIT_INPUT_PATHS,
    }


def _apply_gates_in_place(
    bits: list[int],
    word: tuple[object, ...],
) -> None:
    """Independent X/CNOT/TOF basis-state simulator."""

    for gate in word:
        wires = gate.wires
        if gate.kind == "X":
            bits[wires[0]] ^= 1
        elif gate.kind == "CNOT":
            bits[wires[1]] ^= bits[wires[0]]
        elif gate.kind == "TOF":
            bits[wires[2]] ^= bits[wires[0]] & bits[wires[1]]
        else:
            raise AssertionError(("unsupported gate kind", gate.kind))


def apply_word_own(
    state: tuple[int, ...],
    word: tuple[object, ...],
) -> tuple[int, ...]:
    bits = list(state)
    _apply_gates_in_place(bits, word)
    return tuple(bits)


def apply_pair_own(
    data: tuple[int, ...],
    macros: tuple[tuple[object, ...], ...],
    order: tuple[int, int],
) -> tuple[int, ...]:
    output = data
    for station in order:
        output = apply_word_own(output, macros[station])
    return output


def bit_sha256(bits: tuple[int, ...]) -> str:
    return sha256(bytes(bits)).hexdigest()


def l1(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def fixture() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    data = S735.held_fixture_data()
    macros = tuple(K.mapped_macro(row) for row in program)
    data_width = len(data)
    physical_words = tuple(
        tuple(
            K.controlled_macro(
                macros[station],
                data_width + station,
                data_width + 2 * RING_STATIONS + station,
            )
        )
        for station in range(RING_STATIONS)
    )
    physical_counts = tuple(len(word) for word in physical_words)
    physical_vectors = tuple(
        tuple(sum(gate.kind == kind for gate in word) for kind in ("CNOT", "TOF"))
        for word in physical_words
    )
    semantic_vectors = tuple(
        tuple(sum(gate.kind == kind for gate in word) for kind in ("X", "CNOT", "TOF"))
        for word in macros
    )
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    expected = apply_word_own(
        apply_word_own(data, allocator), allocator
    )
    physical_program, track = K.held_physical_program_and_track(
        FIXTURE_BANKS
    )
    if physical_program != program or len(track) != 2 * RING_STATIONS:
        raise AssertionError(("held physical track mismatch", len(track)))
    a_sites = track[::2]
    b_sites = track[1::2]
    rail_hops = tuple(
        (
            l1(a_sites[station], b_sites[station]),
            l1(b_sites[station], a_sites[(station + 1) % RING_STATIONS]),
        )
        for station in range(RING_STATIONS)
    )
    if len(program) != RING_STATIONS:
        raise AssertionError(("held program width", len(program)))
    return {
        "program": program,
        "roles": tuple(row[0] for row in program),
        "data": data,
        "macros": macros,
        "physical_words": physical_words,
        "physical_counts": physical_counts,
        "physical_vectors": physical_vectors,
        "semantic_vectors": semantic_vectors,
        "expected": expected,
        "rail_hops": rail_hops,
    }


def event_surface(fixed: dict[str, object]) -> dict[str, object]:
    """Re-derive the 121 Cycle-752 Q contests from A/B rail transport."""

    roles = fixed["roles"]
    rows = []
    transport_failures = 0
    for start in range(RING_STATIONS):
        a = [
            int(station in (start, (start + 1) % RING_STATIONS))
            for station in range(RING_STATIONS)
        ]
        b = [0] * RING_STATIONS
        for step in range(RING_STATIONS):
            active = tuple(station for station, bit in enumerate(a) if bit)
            expected_active = tuple(
                sorted(
                    (
                        (start + step) % RING_STATIONS,
                        (start + step + 1) % RING_STATIONS,
                    )
                )
            )
            transport_failures += active != expected_active
            rows.append(
                {
                    "start": start,
                    "step": step,
                    "active_A_stations": active,
                    "candidate_roles":
                        tuple(roles[station] for station in active),
                    "candidate_definition": (
                        "occupied A_s selects station-local mapped_macro(program[s]) "
                        "during the Q layer"
                    ),
                }
            )
            for station in range(RING_STATIONS):
                a[station], b[station] = b[station], a[station]
            for station in range(RING_STATIONS):
                target = (station + 1) % RING_STATIONS
                b[station], a[target] = a[target], b[station]
    return {
        "contested_item_kind":
            "two occupied-A station-local Q action candidates",
        "not_item_kinds": (
            "the station label alone",
            "the later lift/land SWAP gates",
            "an extra exchange-candidate register",
        ),
        "events": len(rows),
        "expected_events": RING_STATIONS ** 2,
        "two_items_each": all(
            len(row["active_A_stations"]) == EXPECTED_COUNT
            for row in rows
        ),
        "transport_failures": transport_failures,
        "rows": tuple(rows),
    }


Signature = tuple[int, ...]
ValueFunction = Callable[[int, int, int], object]


def signature_for(
    start: int,
    value_function: ValueFunction,
    descending: bool,
) -> tuple[Signature, tuple[tuple[object, object], ...]]:
    signature = []
    value_rows = []
    for step in range(RING_STATIONS):
        left = (start + step) % RING_STATIONS
        right = (left + 1) % RING_STATIONS
        values = (
            value_function(start, step, left),
            value_function(start, step, right),
        )
        value_rows.append(values)
        if values[0] == values[1]:
            signature.append(2)
        else:
            left_first = values[0] < values[1]
            if descending:
                left_first = not left_first
            signature.append(0 if left_first else 1)
    return tuple(signature), tuple(value_rows)


def evaluate_signature(
    fixed: dict[str, object],
    start: int,
    signature: Signature,
    cache: dict[tuple[int, Signature], dict[str, object]],
) -> dict[str, object]:
    key = (start, signature)
    if key in cache:
        return cache[key]
    macros = fixed["macros"]
    states = {fixed["data"]}
    unresolved = []
    for step, decision in enumerate(signature):
        left = (start + step) % RING_STATIONS
        right = (left + 1) % RING_STATIONS
        if decision in (0, 1):
            order = (left, right) if decision == 0 else (right, left)
            states = {
                apply_pair_own(state, macros, order) for state in states
            }
            continue
        next_states = set()
        differing_inputs = 0
        for state in states:
            forward = apply_pair_own(state, macros, (left, right))
            reverse = apply_pair_own(state, macros, (right, left))
            differing_inputs += forward != reverse
            next_states.add(forward)
            next_states.add(reverse)
        if differing_inputs:
            unresolved.append(
                {
                    "step": step,
                    "items": (left, right),
                    "differing_input_branches": differing_inputs,
                }
            )
        states = next_states
    order_defined = not unresolved
    all_outputs_correct = states == {fixed["expected"]}
    result = {
        "passes": order_defined and all_outputs_correct,
        "order_defined": order_defined,
        "all_outputs_correct": all_outputs_correct,
        "possible_outputs": len(states),
        "possible_output_digests":
            tuple(sorted(bit_sha256(state) for state in states)),
        "unresolved_order_sensitive_ties": tuple(unresolved),
    }
    cache[key] = result
    return result


def functional_battery(
    fixed: dict[str, object],
    name: str,
    value_function: ValueFunction,
    descending: bool,
    cache: dict[tuple[int, Signature], dict[str, object]],
) -> dict[str, object]:
    rows = []
    for start in range(RING_STATIONS):
        signature, values = signature_for(
            start, value_function, descending
        )
        evaluated = evaluate_signature(fixed, start, signature, cache)
        rows.append(
            {
                "start": start,
                "signature": signature,
                "values": values,
                **evaluated,
            }
        )
    correct_positions = tuple(
        row["start"] for row in rows if row["passes"]
    )
    return {
        "name": name,
        "mirror": "DESC" if descending else "ASC",
        "passes": len(correct_positions),
        "correct_positions": correct_positions,
        "starts_with_total_order":
            sum(row["order_defined"] for row in rows),
        "tied_contests": sum(
            decision == 2
            for row in rows
            for decision in row["signature"]
        ),
        "order_sensitive_tied_contests": sum(
            len(row["unresolved_order_sensitive_ties"]) for row in rows
        ),
        "rows": tuple(rows),
    }


def compact_battery(row: dict[str, object]) -> dict[str, object]:
    return {
        "name": row["name"],
        "mirror": row["mirror"],
        "passes": row["passes"],
        "correct_positions": row["correct_positions"],
        "starts_with_total_order": row["starts_with_total_order"],
        "tied_contests": row["tied_contests"],
        "order_sensitive_tied_contests":
            row["order_sensitive_tied_contests"],
        "start_table": tuple(
            {
                "start": item["start"],
                "pass": item["passes"],
                "order_defined": item["order_defined"],
                "all_outputs_correct": item["all_outputs_correct"],
                "possible_outputs": item["possible_outputs"],
                "unresolved_ties":
                    len(item["unresolved_order_sensitive_ties"]),
            }
            for item in row["rows"]
        ),
    }


def mapping_fidelity_attack(
    fixed: dict[str, object],
    surface: dict[str, object],
    cache: dict[tuple[int, Signature], dict[str, object]],
) -> dict[str, object]:
    """Compare the primary port with the natural landed 752 item fields."""

    physical_counts = fixed["physical_counts"]

    def gate_value(_start: int, _step: int, station: int) -> int:
        return physical_counts[station]

    def initial_occupancy(start: int, _step: int, station: int) -> int:
        return int(
            station in (start, (start + 1) % RING_STATIONS)
        )

    def event_local_occupancy(
        start: int, step: int, station: int
    ) -> int:
        return int(
            station
            in (
                (start + step) % RING_STATIONS,
                (start + step + 1) % RING_STATIONS,
            )
        )

    ported = tuple(
        functional_battery(
            fixed,
            name,
            value_function,
            descending,
            cache,
        )
        for name, value_function, descending in (
            ("first_Q_physical_gate_count_ASC", gate_value, False),
            ("first_Q_physical_gate_count_DESC", gate_value, True),
            ("initial_station_occupancy_ASC", initial_occupancy, False),
            ("initial_station_occupancy_DESC", initial_occupancy, True),
        )
    )
    event_local = tuple(
        functional_battery(
            fixed,
            name,
            event_local_occupancy,
            descending,
            cache,
        )
        for name, descending in (
            ("event_local_A_occupancy_ASC", False),
            ("event_local_A_occupancy_DESC", True),
        )
    )
    station_rows = tuple(
        {
            "station": station,
            "program_kind": fixed["program"][station][0],
            "program_index": fixed["program"][station][1],
            "semantic_macro_gates": len(fixed["macros"][station]),
            "first_Q_physical_gate_count":
                fixed["physical_counts"][station],
            "first_Q_physical_gate_vector_CNOT_TOF":
                fixed["physical_vectors"][station],
            "initial_occupancy_by_start": tuple(
                int(
                    station
                    in (start, (start + 1) % RING_STATIONS)
                )
                for start in range(RING_STATIONS)
            ),
        }
        for station in range(RING_STATIONS)
    )
    gate_ties = tuple(
        station
        for station in range(RING_STATIONS)
        if physical_counts[station]
        == physical_counts[(station + 1) % RING_STATIONS]
    )
    primary_counts = {
        row["name"]: row["passes"] for row in ported
    }
    faithful_family = ported + event_local
    faithful_best = max(row["passes"] for row in faithful_family)
    faithful_winners = tuple(
        row["name"] for row in faithful_family if row["passes"]
    )
    if faithful_best == RING_STATIONS:
        finding = (
            "REFUTED NO_ORDER: a faithful landed mapping passes 11/11 "
            f"starts ({faithful_winners})."
        )
        outcome = "REFUTED_NO_ORDER"
    elif faithful_best > 0:
        finding = (
            "WEAKENS NO_ORDER: a faithful landed mapping passes more than "
            f"0/11 starts (best={faithful_best}, candidates={faithful_winners})."
        )
        outcome = "WEAKENS_NO_ORDER"
    else:
        finding = (
            "CONFIRMED at fixture scope: the 752 contended items are the two "
            "occupied-A station-local Q action candidates; station-local "
            "controlled-macro gate count is the faithful first-Q gate value, "
            "while static-initial and event-local occupancies are honest "
            "non-injective preorders. All faithful ASC/DESC reruns pass 0/11."
        )
        outcome = "CONFIRMED"
    return {
        "surface": {
            key: value for key, value in surface.items() if key != "rows"
        },
        "mapping_judgment": {
            "gate_count": (
                "faithful: candidate Q_s is exactly the controlled "
                "mapped_macro(program[s]) block counted by the primary"
            ),
            "static_initial_occupancy": (
                "faithful as the named t=0 station field, but deliberately "
                "non-injective and therefore only a preorder"
            ),
            "event_local_occupancy_control": (
                "also tested because every actual candidate is occupied at "
                "its Q boundary; both candidates receive value 1"
            ),
            "station_index_completion": (
                "not faithful and never appended to a tied value"
            ),
        },
        "station_item_mapping": station_rows,
        "adjacent_gate_ties": gate_ties,
        "ported_results": ported,
        "event_local_controls": event_local,
        "comparison_table": tuple(
            compact_battery(row) for row in faithful_family
        ),
        "primary_claim_counts": primary_counts,
        "faithful_best": faithful_best,
        "faithful_positive_candidates": faithful_winners,
        "outcome": outcome,
        "finding_verbatim": finding,
    }


def alternative_functional_hunt(
    fixed: dict[str, object],
    cache: dict[tuple[int, Signature], dict[str, object]],
) -> dict[str, object]:
    roles = fixed["roles"]
    physical_vectors = fixed["physical_vectors"]
    semantic_vectors = fixed["semantic_vectors"]

    def initial_role_value(role: str) -> ValueFunction:
        return lambda start, _step, station: int(
            roles[station] == role
            and station in (start, (start + 1) % RING_STATIONS)
        )

    def event_role_value(role: str) -> ValueFunction:
        return lambda _start, _step, station: int(
            roles[station] == role
        )

    def physical_vector(
        _start: int, _step: int, station: int
    ) -> tuple[int, int]:
        return physical_vectors[station]

    def semantic_vector(
        _start: int, _step: int, station: int
    ) -> tuple[int, int, int]:
        return semantic_vectors[station]

    def token_travel_distance(
        _start: int, step: int, _station: int
    ) -> int:
        # A_s -> B_s -> A_{s+1}: two unit rail hops per completed tick.
        return 2 * step

    specifications = (
        (
            "initial_relay_occupancy_ASC",
            initial_role_value("relay"),
            False,
        ),
        (
            "initial_relay_occupancy_DESC",
            initial_role_value("relay"),
            True,
        ),
        (
            "initial_handoff_occupancy_ASC",
            initial_role_value("handoff"),
            False,
        ),
        (
            "initial_handoff_occupancy_DESC",
            initial_role_value("handoff"),
            True,
        ),
        (
            "event_relay_occupancy_ASC",
            event_role_value("relay"),
            False,
        ),
        (
            "event_relay_occupancy_DESC",
            event_role_value("relay"),
            True,
        ),
        (
            "event_handoff_occupancy_ASC",
            event_role_value("handoff"),
            False,
        ),
        (
            "event_handoff_occupancy_DESC",
            event_role_value("handoff"),
            True,
        ),
        (
            "physical_gate_vector_CNOT_TOF_LEX_ASC",
            physical_vector,
            False,
        ),
        (
            "physical_gate_vector_CNOT_TOF_LEX_DESC",
            physical_vector,
            True,
        ),
        (
            "semantic_gate_vector_X_CNOT_TOF_LEX_ASC",
            semantic_vector,
            False,
        ),
        (
            "semantic_gate_vector_X_CNOT_TOF_LEX_DESC",
            semantic_vector,
            True,
        ),
        (
            "token_travel_distance_ASC",
            token_travel_distance,
            False,
        ),
        (
            "token_travel_distance_DESC",
            token_travel_distance,
            True,
        ),
    )
    results = tuple(
        functional_battery(
            fixed, name, value_function, descending, cache
        )
        for name, value_function, descending in specifications
    )
    best = max(row["passes"] for row in results)
    best_names = tuple(
        row["name"] for row in results if row["passes"] == best
    )
    beats_baseline = tuple(
        row["name"] for row in results if row["passes"] > 1
    )
    full = tuple(
        row["name"]
        for row in results
        if row["passes"] == RING_STATIONS
    )
    if full:
        finding = (
            "REFUTED NO_ORDER OUTRIGHT: alternative covariant functional(s) "
            f"pass 11/11: {full}."
        )
        outcome = "REFUTED_NO_ORDER"
    elif beats_baseline:
        finding = (
            "WEAKENS NO_ORDER: alternative covariant functional(s) beat the "
            f"1/11 fixed-order baseline: {beats_baseline}."
        )
        outcome = "WEAKENS_NO_ORDER"
    else:
        finding = (
            "CONFIRMED for the bounded alternative hunt: relay and handoff "
            "occupancies (static and event-local), physical and semantic "
            "gate-count vectors, and token rail-travel distance produce no "
            f"candidate above the 1/11 baseline (best={best}/11)."
        )
        outcome = "NO_CANDIDATE_BEATS_BASELINE"
    return {
        "candidate_count": len(results),
        "bounded_candidate_basis": {
            "roles": ("relay", "handoff"),
            "occupancy_times": ("initial", "event-local"),
            "physical_vector_coordinates": ("CNOT", "TOF"),
            "semantic_vector_coordinates": ("X", "CNOT", "TOF"),
            "token_distance": (
                "two unit A_s->B_s->A_{s+1} rail hops per completed tick"
            ),
            "rail_hops_by_station": fixed["rail_hops"],
        },
        "results": results,
        "comparison_table":
            tuple(compact_battery(row) for row in results),
        "best_passes": best,
        "best_candidates": best_names,
        "candidates_beating_baseline": beats_baseline,
        "position_uniform_candidates": full,
        "outcome": outcome,
        "finding_verbatim": finding,
    }


def run_fixed_order(
    fixed: dict[str, object],
    start: int,
    order: tuple[int, ...],
) -> tuple[int, ...]:
    rank = {station: index for index, station in enumerate(order)}
    data = fixed["data"]
    macros = fixed["macros"]
    for step in range(RING_STATIONS):
        left = (start + step) % RING_STATIONS
        right = (left + 1) % RING_STATIONS
        pair_order = (
            (left, right)
            if rank[left] < rank[right]
            else (right, left)
        )
        data = apply_pair_own(data, macros, pair_order)
    return data


def exhaustive_fixed_order_recount(
    fixed: dict[str, object],
) -> dict[str, object]:
    """Enumerate every adjacent-edge orientation independently."""

    size = 1 << RING_STATIONS
    success_start_mask_by_orientation = [0] * size
    macros = fixed["macros"]
    for start in range(RING_STATIONS):
        states = [fixed["data"]]
        for step in range(RING_STATIONS):
            left = (start + step) % RING_STATIONS
            right = (left + 1) % RING_STATIONS
            next_states = []
            for data in states:
                next_states.append(
                    apply_pair_own(data, macros, (left, right))
                )
                next_states.append(
                    apply_pair_own(data, macros, (right, left))
                )
            states = next_states
        for local_mask, output in enumerate(states):
            if output != fixed["expected"]:
                continue
            absolute_mask = 0
            for step in range(RING_STATIONS):
                decision = (
                    local_mask >> (RING_STATIONS - 1 - step)
                ) & 1
                edge = (start + step) % RING_STATIONS
                absolute_mask |= decision << edge
            success_start_mask_by_orientation[absolute_mask] |= 1 << start

    realizable = range(1, size - 1)
    histogram = Counter(
        success_start_mask_by_orientation[mask].bit_count()
        for mask in realizable
    )
    witness_positions = tuple(
        start
        for start in range(RING_STATIONS)
        if run_fixed_order(
            fixed, start, ROUTE3_FIXED_Q_ORDER
        )
        == fixed["expected"]
    )
    local_successes = tuple(
        sum(
            bool(
                success_start_mask_by_orientation[mask]
                & (1 << start)
            )
            for mask in range(size)
        )
        for start in range(RING_STATIONS)
    )
    return {
        "enumerator": (
            "independent branch tree over both orders at each of 11 "
            "successor edges, remapped to absolute edge masks"
        ),
        "edge_orientation_classes": size,
        "fixed_total_order_classes": size - 2,
        "excluded_directed_cycle_classes": (0, size - 1),
        "pass_count_histogram": dict(sorted(histogram.items())),
        "best_fixed_order_passes": max(histogram),
        "position_uniform_fixed_orders": sum(
            success_start_mask_by_orientation[mask] == size - 1
            for mask in realizable
        ),
        "all_local_orientation_success_counts_by_start":
            local_successes,
        "witness_order": ROUTE3_FIXED_Q_ORDER,
        "witness_correct_positions": witness_positions,
        "witness_passes": len(witness_positions),
    }


def fallback_battery(
    fixed: dict[str, object],
    value_function: ValueFunction,
    descending: bool,
    fallback_order: tuple[int, ...],
    cache: dict[tuple[int, Signature], dict[str, object]],
) -> dict[str, object]:
    rank = {
        station: index for index, station in enumerate(fallback_order)
    }
    correct_positions = []
    replaced_ties = 0
    for start in range(RING_STATIONS):
        signature, _values = signature_for(
            start, value_function, descending
        )
        completed = []
        for step, decision in enumerate(signature):
            if decision != 2:
                completed.append(decision)
                continue
            replaced_ties += 1
            left = (start + step) % RING_STATIONS
            right = (left + 1) % RING_STATIONS
            completed.append(0 if rank[left] < rank[right] else 1)
        result = evaluate_signature(
            fixed, start, tuple(completed), cache
        )
        if result["all_outputs_correct"]:
            correct_positions.append(start)
    return {
        "fallback_order": fallback_order,
        "replaced_ties": replaced_ties,
        "passes": len(correct_positions),
        "correct_positions": tuple(correct_positions),
    }


def tie_handling_audit(
    fixed: dict[str, object],
    mapping: dict[str, object],
    cache: dict[tuple[int, Signature], dict[str, object]],
) -> dict[str, object]:
    source = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_PATH)
    function = _function(tree, "functional_battery")
    rendered = ast.unparse(function)
    required_fragments = (
        "if values[0] != values[1]",
        "forward = apply_pair(data, macros, (left, right))",
        "reverse = apply_pair(data, macros, (right, left))",
        "differing_inputs += forward != reverse",
        "next_states.add(forward)",
        "next_states.add(reverse)",
        "defined = not unresolved",
        "'passes': defined and all_outputs_correct",
    )
    forbidden_tie_fallback_fragments = (
        "sorted((left, right)",
        "key=rank",
        "station_index",
    )
    fragment_presence = {
        fragment: fragment in rendered for fragment in required_fragments
    }
    forbidden_presence = {
        fragment: fragment in rendered
        for fragment in forbidden_tie_fallback_fragments
    }
    imported_names = tuple(
        alias.name
        for node in ast.walk(
            ast.parse(
                Path(__file__).read_text(encoding="utf-8"),
                filename=__file__,
            )
        )
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    )

    def initial_occupancy(start: int, _step: int, station: int) -> int:
        return int(
            station in (start, (start + 1) % RING_STATIONS)
        )

    def event_local_occupancy(
        start: int, step: int, station: int
    ) -> int:
        return int(
            station
            in (
                (start + step) % RING_STATIONS,
                (start + step + 1) % RING_STATIONS,
            )
        )

    counterfactuals = {
        "ascending_station_index": fallback_battery(
            fixed,
            initial_occupancy,
            False,
            tuple(range(RING_STATIONS)),
            cache,
        ),
        "descending_station_index": fallback_battery(
            fixed,
            initial_occupancy,
            False,
            tuple(reversed(range(RING_STATIONS))),
            cache,
        ),
        "route3_witness": fallback_battery(
            fixed,
            initial_occupancy,
            False,
            ROUTE3_FIXED_Q_ORDER,
            cache,
        ),
        "all_tied_event_occupancy_route3_witness": fallback_battery(
            fixed,
            event_local_occupancy,
            False,
            ROUTE3_FIXED_Q_ORDER,
            cache,
        ),
    }
    ported_occupancy = tuple(
        row
        for row in mapping["ported_results"]
        if row["name"].startswith("initial_station_occupancy")
    )
    strict_ties = sum(
        row["tied_contests"] for row in ported_occupancy
    )
    strict_sensitive_ties = sum(
        row["order_sensitive_tied_contests"]
        for row in ported_occupancy
    )
    return {
        "primary_function_ast_sha256":
            sha256(rendered.encode()).hexdigest(),
        "required_tie_logic_fragments": fragment_presence,
        "forbidden_fallback_fragments": forbidden_presence,
        "primary_imported_by_checker":
            PRIMARY_MODULE in imported_names,
        "primary_absent_from_sys_modules":
            PRIMARY_MODULE not in sys.modules,
        "strict_ported_occupancy_ties": strict_ties,
        "strict_ported_order_sensitive_ties":
            strict_sensitive_ties,
        "strict_ported_occupancy_counts": {
            row["name"]: row["passes"] for row in ported_occupancy
        },
        "explicit_fallback_counterfactuals": counterfactuals,
        "finding_verbatim": (
            "CONFIRMED: on an equal-valued contest the primary propagates "
            "both left-right and right-left outputs, records a tie only when "
            "those outputs differ, and requires no unresolved tie for PASS. "
            "It does not append station index or any fixed-order rank."
        ),
        "passes": (
            all(fragment_presence.values())
            and not any(forbidden_presence.values())
            and PRIMARY_MODULE not in imported_names
            and PRIMARY_MODULE not in sys.modules
            and strict_ties > 0
            and strict_sensitive_ties > 0
            and counterfactuals[
                "all_tied_event_occupancy_route3_witness"
            ]["passes"]
            == 1
        ),
    }


def core_experiment(fixed: dict[str, object]) -> dict[str, object]:
    cache: dict[tuple[int, Signature], dict[str, object]] = {}
    surface = event_surface(fixed)
    mapping = mapping_fidelity_attack(fixed, surface, cache)
    alternatives = alternative_functional_hunt(fixed, cache)
    baseline = exhaustive_fixed_order_recount(fixed)
    ties = tie_handling_audit(fixed, mapping, cache)
    return {
        "surface": surface,
        "mapping": mapping,
        "alternatives": alternatives,
        "baseline": baseline,
        "ties": ties,
        "signature_evaluations": len(cache),
    }


def deterministic_projection(
    experiment: dict[str, object],
) -> dict[str, object]:
    return {
        "surface": experiment["surface"],
        "mapping_table": experiment["mapping"]["comparison_table"],
        "mapping_outcome": experiment["mapping"]["outcome"],
        "alternative_table":
            experiment["alternatives"]["comparison_table"],
        "alternative_outcome":
            experiment["alternatives"]["outcome"],
        "baseline": experiment["baseline"],
        "tie_audit": experiment["ties"],
        "signature_evaluations":
            experiment["signature_evaluations"],
    }


def main() -> int:
    started = perf_counter()
    source = source_and_blocklist_control()
    fixed = fixture()
    first = core_experiment(fixed)
    second = core_experiment(fixed)
    deterministic = (
        deterministic_projection(first)
        == deterministic_projection(second)
    )
    elapsed_before_output = perf_counter() - started

    surface = first["surface"]
    mapping = first["mapping"]
    alternatives = first["alternatives"]
    baseline = first["baseline"]
    ties = first["ties"]

    emit("CYCLE783_INDEPENDENT_AUDIT_INPUT_PATHS", AUDIT_INPUT_PATHS)
    emit(
        "CYCLE783_INDEPENDENT_SOURCE_CONTROL",
        {
            "head": source["head"],
            "head_blobs": source["head_blobs"],
            "observed_sha256": source["observed_sha256"],
            "expected_sha256": source["expected_sha256"],
            "primary_sha256_text_only": source["primary_sha256"],
            "text_only_modules": source["text_only_modules"],
            "executable_audit_imports":
                source["executable_audit_imports"],
        },
    )
    check(
        "CERTIFICATE_A_SHA_ANCHORS_IMPORT_SCOPE_BLOCKLIST",
        source["anchors_match"]
        and source["all_inputs_landed"]
        and source["primary_parsed_as_ast"]
        and source["literal_exact"]
        and source["matches_primary_bounded_set"]
        and source["executable_imports_exact"]
        and source["text_only_absent_from_sys_modules"]
        and source["blocker_active"],
        {
            "anchors_match": source["anchors_match"],
            "all_inputs_landed": source["all_inputs_landed"],
            "literal_exact": source["literal_exact"],
            "matches_primary_bounded_set":
                source["matches_primary_bounded_set"],
            "executable_imports_exact":
                source["executable_imports_exact"],
            "text_only_absent_from_sys_modules":
                source["text_only_absent_from_sys_modules"],
            "blocker_active": source["blocker_active"],
        },
    )

    emit(
        "CYCLE783_752_CONTENDED_ITEM_DERIVATION",
        {
            key: value for key, value in surface.items() if key != "rows"
        },
    )
    emit(
        "CYCLE783_FAITHFUL_STATION_ITEM_MAPPING",
        mapping["station_item_mapping"],
    )
    emit(
        "CYCLE783_MAPPING_COMPARISON_TABLE",
        mapping["comparison_table"],
    )
    emit(
        "CYCLE783_MAPPING_FIDELITY_FINDING_VERBATIM",
        mapping["finding_verbatim"],
    )
    expected_primary_counts = {
        "first_Q_physical_gate_count_ASC": 0,
        "first_Q_physical_gate_count_DESC": 0,
        "initial_station_occupancy_ASC": 0,
        "initial_station_occupancy_DESC": 0,
    }
    mapping_integrity = (
        surface["events"] == surface["expected_events"] == 121
        and surface["two_items_each"]
        and surface["transport_failures"] == 0
        and fixed["physical_counts"]
        == (9, 1146, 1512, 755, 20, 1146, 1, 20, 749, 1215, 29)
        and not mapping["adjacent_gate_ties"]
        and mapping["primary_claim_counts"] == expected_primary_counts
        and mapping["faithful_best"]
        == max(
            row["passes"]
            for row in (
                mapping["ported_results"]
                + mapping["event_local_controls"]
            )
        )
    )
    check(
        "CERTIFICATE_B_MAPPING_FIDELITY_ATTACK",
        mapping_integrity,
        {
            "contended_item_kind":
                surface["contested_item_kind"],
            "gate_mapping": mapping["mapping_judgment"]["gate_count"],
            "occupancy_mapping":
                mapping["mapping_judgment"]["static_initial_occupancy"],
            "primary_independent_counts":
                mapping["primary_claim_counts"],
            "faithful_best": mapping["faithful_best"],
            "outcome": mapping["outcome"],
            "finding_verbatim": mapping["finding_verbatim"],
        },
    )

    emit(
        "CYCLE783_ALTERNATIVE_FUNCTIONAL_COMPARISON_TABLE",
        alternatives["comparison_table"],
    )
    emit(
        "CYCLE783_ALTERNATIVE_HUNT_FINDING_VERBATIM",
        alternatives["finding_verbatim"],
    )
    alternative_integrity = (
        alternatives["candidate_count"]
        == len(alternatives["results"])
        == 14
        and alternatives["best_passes"]
        == max(row["passes"] for row in alternatives["results"])
        and alternatives["candidates_beating_baseline"]
        == tuple(
            row["name"]
            for row in alternatives["results"]
            if row["passes"] > 1
        )
        and alternatives["position_uniform_candidates"]
        == tuple(
            row["name"]
            for row in alternatives["results"]
            if row["passes"] == RING_STATIONS
        )
        and all(hops == (1, 1) for hops in fixed["rail_hops"])
    )
    check(
        "CERTIFICATE_C_ALTERNATIVE_FUNCTIONAL_HUNT",
        alternative_integrity,
        {
            "candidates_tested": alternatives["candidate_count"],
            "best_score":
                (alternatives["best_passes"], RING_STATIONS),
            "best_candidates": alternatives["best_candidates"],
            "beats_1_of_11":
                alternatives["candidates_beating_baseline"],
            "position_uniform":
                alternatives["position_uniform_candidates"],
            "outcome": alternatives["outcome"],
            "finding_verbatim": alternatives["finding_verbatim"],
        },
    )

    emit("CYCLE783_BASELINE_RECOUNT", baseline)
    baseline_agrees = (
        baseline["edge_orientation_classes"] == 2048
        and baseline["fixed_total_order_classes"] == 2046
        and baseline["excluded_directed_cycle_classes"] == (0, 2047)
        and baseline["pass_count_histogram"] == {0: 1535, 1: 511}
        and baseline["best_fixed_order_passes"] == 1
        and baseline["position_uniform_fixed_orders"] == 0
        and baseline["witness_passes"] == 1
        and baseline["witness_correct_positions"] == (0,)
    )
    check(
        "CERTIFICATE_D_BASELINE_INDEPENDENT_RECOUNT",
        baseline_agrees,
        {
            "witness": (
                baseline["witness_passes"],
                RING_STATIONS,
            ),
            "witness_correct_positions":
                baseline["witness_correct_positions"],
            "fixed_order_classes":
                baseline["fixed_total_order_classes"],
            "histogram": baseline["pass_count_histogram"],
            "position_uniform":
                baseline["position_uniform_fixed_orders"],
        },
    )

    emit(
        "CYCLE783_TIE_HANDLING_AUDIT",
        {
            "finding_verbatim": ties["finding_verbatim"],
            "required_tie_logic_fragments":
                ties["required_tie_logic_fragments"],
            "forbidden_fallback_fragments":
                ties["forbidden_fallback_fragments"],
            "strict_ported_occupancy_ties":
                ties["strict_ported_occupancy_ties"],
            "strict_ported_order_sensitive_ties":
                ties["strict_ported_order_sensitive_ties"],
            "strict_ported_occupancy_counts":
                ties["strict_ported_occupancy_counts"],
            "explicit_fallback_counterfactuals":
                ties["explicit_fallback_counterfactuals"],
        },
    )
    check(
        "CERTIFICATE_E_TIE_HANDLING_NO_SILENT_FALLBACK",
        ties["passes"],
        {
            "primary_imported_by_checker":
                ties["primary_imported_by_checker"],
            "primary_absent_from_sys_modules":
                ties["primary_absent_from_sys_modules"],
            "finding_verbatim": ties["finding_verbatim"],
        },
    )

    if mapping["outcome"] == "REFUTED_NO_ORDER":
        verdict = "REFUTED_NO_ORDER_BY_FAITHFUL_MAPPING"
    elif mapping["outcome"] == "WEAKENS_NO_ORDER":
        verdict = "WEAKENS_NO_ORDER_BY_FAITHFUL_MAPPING"
    elif alternatives["outcome"] == "REFUTED_NO_ORDER":
        verdict = "REFUTED_NO_ORDER_BY_ALTERNATIVE_FUNCTIONAL"
    elif alternatives["outcome"] == "WEAKENS_NO_ORDER":
        verdict = "WEAKENS_NO_ORDER_BY_ALTERNATIVE_FUNCTIONAL"
    else:
        verdict = "NO_ORDER_CONFIRMED_AT_CYCLE752_FIXTURE_SCOPE"

    bytes_before_bounds = len(
        ("\n".join(OUTPUT_LINES) + "\n").encode()
    )
    bounds_pass = (
        deterministic
        and elapsed_before_output < RUNTIME_LIMIT_SEC
        and bytes_before_bounds < STDOUT_LIMIT_BYTES - 4096
    )
    check(
        "CERTIFICATE_F_DETERMINISM_RUNTIME_STDOUT_BOUNDS",
        bounds_pass,
        {
            "deterministic_full_rerun": deterministic,
            "first_signature_evaluations":
                first["signature_evaluations"],
            "second_signature_evaluations":
                second["signature_evaluations"],
            "runtime_sec": round(elapsed_before_output, 6),
            "runtime_limit_sec": RUNTIME_LIMIT_SEC,
            "stdout_bytes_before_F": bytes_before_bounds,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )
    emit(
        "CYCLE783_INDEPENDENT_FINAL",
        {
            "status": "PASS" if all(CHECKS.values()) else "FAIL",
            "verdict": verdict,
            "mapping_fidelity_outcome": mapping["outcome"],
            "mapping_best_score":
                (mapping["faithful_best"], RING_STATIONS),
            "alternative_hunt_outcome": alternatives["outcome"],
            "alternative_best_score":
                (alternatives["best_passes"], RING_STATIONS),
            "baseline": "witness 1/11; 0/2046 position-uniform",
            "W2_closure_claim": False,
            "runtime_sec": round(elapsed_before_output, 6),
            "self_sha256":
                sha256(Path(__file__).read_bytes()).hexdigest(),
        },
    )

    stdout = "\n".join(OUTPUT_LINES) + "\n"
    if len(stdout.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout limit", len(stdout.encode()), STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(stdout)
    return 0 if all(CHECKS.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
