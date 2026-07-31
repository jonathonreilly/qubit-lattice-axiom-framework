#!/usr/bin/env python3
"""Independent bounded checker for Cycle 755 program content/order claims.

The Cycle 755 primary is parsed as inert text.  It is never imported or
executed.  Cycle 719 is the sole scientific supplier and is imported as K.
"""

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/PROGRAM_CONTENT_ORDER_ATTEMPT_CYCLE755_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import ast
from collections import Counter
from hashlib import sha256
from itertools import product
import json
from math import factorial
from pathlib import Path
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = (
    "scripts/frontier_cycle755_program_content_order_attempt_2026_07_28.py"
)
BLOCKLIST = (PRIMARY_PATH,)
K_MODULE = "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
OUTCOME_LANGUAGE = "81 of 1,814,400 fixed-inventory arrangements"
SCOPE_LANGUAGE = "b<=2"

sys.path.insert(0, str(ROOT / "scripts"))
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


# These are inventory-type orders after the unique source anchor.  Type
# numbers are assigned by first occurrence in K.interleaved_program(b)[1:].
# The b=2 rows are the primary's five reported accepted-example ranks, encoded
# without relying on its labels.  They are frozen independently of execution.
FROZEN_ACCEPTED_ORDERS = {
    1: ((0, 1),),
    2: (
        (0, 1, 2, 3, 4, 3, 5, 6, 7, 8),
        (0, 1, 2, 3, 4, 3, 6, 5, 7, 8),
        (0, 1, 2, 3, 4, 5, 3, 6, 7, 8),
        (0, 2, 1, 3, 4, 3, 5, 6, 7, 8),
        (0, 2, 1, 3, 4, 3, 6, 5, 7, 8),
    ),
}
FROZEN_REJECTED_ORDERS = {
    1: ((1, 0),),
    2: (
        (0, 1, 3, 2, 4, 3, 5, 6, 7, 8),
        (0, 1, 2, 4, 3, 3, 5, 6, 7, 8),
        (0, 1, 2, 3, 3, 4, 5, 6, 7, 8),
    ),
}
FROZEN_REJECTED_CERTIFICATES = {
    1: ("clean_postimage", "decoded_chain", "held_orbit_exactness"),
    2: ("clean_postimage", "decoded_chain", "held_orbit_exactness"),
}


def chain(node):
    """Return a dotted name for an AST Name/Attribute expression."""
    parts = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if isinstance(node, ast.Name):
        parts.append(node.id)
    return ".".join(reversed(parts))


def subscript_name_key(node):
    if not isinstance(node, ast.Subscript) or not isinstance(node.value, ast.Name):
        return None
    key = node.slice
    if isinstance(key, ast.Constant) and isinstance(key.value, str):
        return node.value.id, key.value
    return None


def safe_integer(node):
    """Evaluate only integer literals joined by + or -."""
    if isinstance(node, ast.Constant) and type(node.value) is int:
        return node.value
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -safe_integer(node.operand)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        return safe_integer(node.left) + safe_integer(node.right)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Sub):
        return safe_integer(node.left) - safe_integer(node.right)
    raise ValueError(ast.dump(node))


def function_node(tree, name):
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name:
            return node
    raise AssertionError(f"missing function {name}")


def assignment_node(nodes, name):
    for node in nodes:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name:
                    return node.value
        if isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name) and node.target.id == name:
                return node.value
    raise AssertionError(f"missing assignment {name}")


def extract_primary():
    """Extract Cycle 755's claims and predicate wiring from inert AST data."""
    source = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_PATH)

    audit_value = assignment_node(tree.body, "AUDIT_INPUT_PATHS")
    audit_paths = ast.literal_eval(audit_value)
    if not isinstance(audit_paths, tuple):
        raise AssertionError("primary AUDIT_INPUT_PATHS is not a tuple literal")

    candidate = function_node(tree, "candidate_acceptance_predicate")
    fixtures = function_node(tree, "held_fixtures")
    hostile = function_node(tree, "r_before_q_orbit")
    anchor = function_node(tree, "anchor_certificate")
    search = function_node(tree, "search_census")
    predicate_nodes = (candidate, fixtures, hostile)
    predicate_calls = sorted(
        {
            chain(node.func)
            for function in predicate_nodes
            for node in ast.walk(function)
            if isinstance(node, ast.Call)
        }
    )
    anchor_calls = sorted(
        {
            chain(node.func)
            for node in ast.walk(anchor)
            if isinstance(node, ast.Call)
        }
    )
    battery_value = assignment_node(candidate.body, "battery")
    if not isinstance(battery_value, ast.Dict):
        raise AssertionError("primary battery is not a dict")
    battery_keys = tuple(
        sorted(
            key.value
            for key in battery_value.keys
            if isinstance(key, ast.Constant) and isinstance(key.value, str)
        )
    )

    build = function_node(tree, "build_report")
    pruning_value = next(
        assignment_node(node.body, "pruning_rules")
        for node in ast.walk(build)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node is build
    )
    pruning_rules = ast.literal_eval(pruning_value)

    census_literals = {"b1": {}, "b2": {}, "passive": {}}
    for node in ast.walk(build):
        if not isinstance(node, ast.Compare) or len(node.ops) != 1:
            continue
        if not isinstance(node.ops[0], ast.Eq) or len(node.comparators) != 1:
            continue
        named = subscript_name_key(node.left)
        if named is None:
            continue
        variable, key = named
        if variable not in census_literals:
            continue
        try:
            value = safe_integer(node.comparators[0])
        except (TypeError, ValueError):
            continue
        census_literals[variable][key] = value

    scope_value = assignment_node(build.body, "scope_status")
    scope_status = ast.literal_eval(scope_value)
    boundary_value = assignment_node(build.body, "boundary")
    if not isinstance(boundary_value, ast.Dict):
        raise AssertionError("primary boundary is not a dict literal")
    boundary_keys = tuple(
        key.value
        for key in boundary_value.keys
        if isinstance(key, ast.Constant) and isinstance(key.value, str)
    )
    boundary_strings = tuple(
        value.value
        for value in boundary_value.values
        if isinstance(value, ast.Constant) and isinstance(value.value, str)
    )

    outcome_branches = sorted(
        {
            node.value.value
            for node in ast.walk(build)
            if isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == "outcome"
                for target in node.targets
            )
            and isinstance(node.value, ast.Constant)
            and isinstance(node.value.value, str)
        }
    )
    literal_strings = {
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }

    required_calls = {
        "K.A.apply_semantic",
        "K.B.cell_rows",
        "K.B.chain_genesis",
        "K.B.decode_local_graph",
        "K.M.global_allocator_word",
        "K.M.pack_state",
        "K.M.prepare_endpoint",
        "K.M.unpack_state",
        "K.interleaved_program",
        "K.mapped_macro",
        "K.run_orbit",
        "r_before_q_orbit",
    }
    required_battery = {
        "inventory_exact",
        "held_orbit_exactness",
        "held_orbit_trace",
        "inverse",
        "register_returns",
        "decoded_chain",
        "clean_postimage",
        "q_before_r_layer_order",
    }
    required_anchor_calls = {
        "K.held_certificate",
        "K.order_and_domain_controls",
    }
    expected_boundary_keys = {
        "outcome",
        "derived",
        "supplied",
        "not_derived",
        "documented_equivalences",
        "orientation_reversal",
    }
    accepted_example_limit = None
    for node in ast.walk(search):
        if not isinstance(node, ast.Return) or not isinstance(node.value, ast.Dict):
            continue
        for key, value in zip(node.value.keys, node.value.values):
            if (
                isinstance(key, ast.Constant)
                and key.value == "accepted_order_examples"
                and isinstance(value, ast.Subscript)
                and isinstance(value.value, ast.Name)
                and value.value.id == "labelled_orders"
                and isinstance(value.slice, ast.Slice)
                and isinstance(value.slice.upper, ast.Constant)
                and type(value.slice.upper.value) is int
            ):
                accepted_example_limit = value.slice.upper.value
    return {
        "audit_input_paths": audit_paths,
        "audit_tuple_literal": isinstance(audit_value, ast.Tuple)
        and all(
            isinstance(element, ast.Constant)
            and isinstance(element.value, str)
            for element in audit_value.elts
        ),
        "predicate_calls": predicate_calls,
        "anchor_calls": anchor_calls,
        "battery_keys": battery_keys,
        "missing_predicate_calls": sorted(required_calls - set(predicate_calls)),
        "missing_anchor_calls": sorted(required_anchor_calls - set(anchor_calls)),
        "missing_battery_keys": sorted(required_battery - set(battery_keys)),
        "pruning_rules": pruning_rules,
        "census_literals": census_literals,
        "outcome_branches": outcome_branches,
        "scope_status": scope_status,
        "boundary_keys": boundary_keys,
        "boundary_strings": boundary_strings,
        "missing_boundary_keys": sorted(
            expected_boundary_keys - set(boundary_keys)
        ),
        "outcome_B_81_of_1814400_present": (
            "B" in outcome_branches
            and any("one_of_81" in value for value in scope_status.values())
            and any(
                "81 accepted arrangements of 1,814,400 candidates" in value
                for value in boundary_strings
            )
        ),
        "accepted_example_limit": accepted_example_limit,
        "primary_sha256": sha256(source.encode()).hexdigest(),
        "blocklist_path": PRIMARY_PATH,
        "blocklist_module_absent": (
            Path(PRIMARY_PATH).stem not in sys.modules
        ),
        "literal_string_count": len(literal_strings),
    }


def role_key(row):
    return row[0], row[1], K.gate_digest(K.mapped_macro(row))


def make_fixtures(bank_count):
    """Independently construct K's held event domain."""
    banks, links = K.B.chain_genesis(bank_count)
    state = K.M.pack_state(banks, links)
    rows = []
    for event in range(2 * bank_count):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        expected = K.A.apply_semantic(
            before, K.M.global_allocator_word(bank_count)
        )
        rows.append((bytes(before), bytes(expected), direction))
        state = expected
    return tuple(rows)


def hostile_r_before_q(data, program, token_start):
    stations = len(program)
    a = [int(index == token_start) for index in range(stations)]
    b = [0] * stations
    output = tuple(data)
    for _ in range(stations):
        for station in range(stations):
            a[station], b[station] = b[station], a[station]
        for station in range(stations):
            target = (station + 1) % stations
            b[station], a[target] = a[target], b[station]
        for station in range(stations):
            if a[station]:
                output = K.A.apply_semantic(
                    output, K.mapped_macro(program[station])
                )
    return output, tuple(a), tuple(b)


def acceptance_predicate(bank_count, program, token_start, fixtures=None):
    """Replay every Cycle 719 certificate used by the primary candidate law."""
    fixtures = make_fixtures(bank_count) if fixtures is None else fixtures
    expected_inventory = Counter(
        role_key(row) for row in K.interleaved_program(bank_count)
    )
    inventory_exact = (
        0 <= token_start < len(program)
        and Counter(role_key(row) for row in program) == expected_inventory
    )
    battery_names = (
        "inventory_exact",
        "held_orbit_exactness",
        "held_orbit_trace",
        "inverse",
        "register_returns",
        "decoded_chain",
        "clean_postimage",
        "q_before_r_layer_order",
    )
    if not inventory_exact:
        battery = {name: name != "inventory_exact" for name in battery_names}
        battery["inventory_exact"] = False
        return {
            "pass": False,
            "battery": battery,
            "failed_certificates": ("inventory_exact",),
            "failure_counts": {"inventory_exact": 1},
        }

    expected_token = tuple(
        int(index == token_start) for index in range(len(program))
    )
    failures = Counter()
    changed = 0
    coarse = K.B.C704.C610.EventChain(bank=2 * bank_count)
    for event, (before_bytes, expected_bytes, direction) in enumerate(fixtures):
        before = tuple(before_bytes)
        expected = tuple(expected_bytes)
        after, a, b, trace = K.run_orbit(
            before, program, token_positions=(token_start,)
        )
        failures["held_orbit_exactness"] += after != expected
        failures["controller_register_return"] += (
            a != expected_token or any(b)
        )
        expected_trace = tuple(
            (
                ((token_start + step) % len(program),),
                ((token_start + step + 1) % len(program),),
                0,
            )
            for step in range(len(program))
        )
        failures["held_orbit_trace"] += trace != expected_trace

        restored, inverse_a, inverse_b, _ = K.run_orbit(
            after,
            program,
            token_positions=(token_start,),
            reverse=True,
        )
        failures["inverse"] += restored != before
        failures["inverse_register_return"] += (
            inverse_a != expected_token or any(inverse_b)
        )

        status = coarse.admit(
            tick_id=event,
            orientation=1 if direction == (1, 0) else -1,
            certificate=1,
            binder=1,
            actuality=1,
            admissibility=1,
            law_domain=1,
        )
        try:
            banks, links = K.M.unpack_state(after, bank_count)
            decoded, _ = K.B.decode_local_graph(banks, links)
            failures["decoded_chain"] += (
                status != "admitted"
                or K.B.cell_rows(decoded) != K.B.cell_rows(coarse)
            )
            failures["clean_postimage"] += any(
                (
                    after[K.R3.X.SOURCE_POINTER],
                    any(
                        bank[wire]
                        for bank in banks
                        for wire in (
                            K.A.POINTER,
                            K.A.U_TO_V,
                            K.A.V_TO_U,
                            K.A.DIRECTION_OK,
                            *K.A.FRESH,
                            *K.A.ZERO_WORK,
                            K.A.TOKEN_OK,
                        )
                    ),
                    any(any(link) for link in links),
                )
            )
        except (AssertionError, IndexError, KeyError, TypeError, ValueError) as error:
            failures["decoded_chain"] += 1
            failures["clean_postimage"] += 1
            failures[
                "malformed_postimage_" + type(error).__name__
            ] += 1

        hostile, hostile_a, hostile_b = hostile_r_before_q(
            before, program, token_start
        )
        changed += hostile != expected
        failures["r_before_q_register_return"] += (
            hostile_a != expected_token or any(hostile_b)
        )

    battery = {
        "inventory_exact": True,
        "held_orbit_exactness": failures["held_orbit_exactness"] == 0,
        "held_orbit_trace": failures["held_orbit_trace"] == 0,
        "inverse": failures["inverse"] == 0,
        "register_returns": (
            failures["controller_register_return"] == 0
            and failures["inverse_register_return"] == 0
            and failures["r_before_q_register_return"] == 0
        ),
        "decoded_chain": failures["decoded_chain"] == 0,
        "clean_postimage": failures["clean_postimage"] == 0,
        "q_before_r_layer_order": changed == len(fixtures),
    }
    return {
        "pass": all(battery.values()),
        "battery": battery,
        "failed_certificates": tuple(
            sorted(key for key, passed in battery.items() if not passed)
        ),
        "failure_counts": dict(sorted(failures.items())),
        "q_before_r_changed_events": changed,
    }


def apply_signature(signature, word, reverse=False):
    action = tuple(reversed(word)) if reverse else word
    return tuple(
        bytes(K.A.apply_semantic(tuple(state), action)) for state in signature
    )


def inventory_types(program):
    rows = []
    counts = []
    by_key = {}
    order = []
    for row in program[1:]:
        key = role_key(row)
        if key not in by_key:
            by_key[key] = len(rows)
            rows.append(row)
            counts.append(0)
        type_index = by_key[key]
        counts[type_index] += 1
        order.append(type_index)
    return tuple(rows), tuple(counts), tuple(order)


def unique_sequences(counts):
    counts = list(counts)
    sequence = []

    def visit():
        if not any(counts):
            yield tuple(sequence)
            return
        for index, count in enumerate(counts):
            if not count:
                continue
            counts[index] -= 1
            sequence.append(index)
            yield from visit()
            sequence.pop()
            counts[index] += 1

    yield from visit()


def partial_multiset_count(totals, depth):
    total = 0
    for used in product(*(range(value + 1) for value in totals)):
        if sum(used) != depth:
            continue
        ways = factorial(depth)
        for value in used:
            ways //= factorial(value)
        total += ways
    return total


def signature_from_order(source_signature, words, order):
    signature = source_signature
    for type_index in order:
        signature = apply_signature(signature, words[type_index])
    return signature


def enumerate_census(bank_count, deadline):
    """Full exact counter-state DP over every anchored multiset permutation."""
    started = time.perf_counter()
    landed = K.interleaved_program(bank_count)
    if landed[0][0] != "source":
        raise AssertionError("unique source anchor moved")
    if sum(row[0] == "source" for row in landed) != 1:
        raise AssertionError("source is not unique")

    fixtures = make_fixtures(bank_count)
    initial = tuple(row[0] for row in fixtures)
    target = tuple(row[1] for row in fixtures)
    source_signature = apply_signature(initial, K.mapped_macro(landed[0]))
    rows, totals, landed_order = inventory_types(landed)
    words = tuple(K.mapped_macro(row) for row in rows)
    zero = (0,) * len(rows)

    layer = {(zero, source_signature): 1}
    indexes = [set(layer)]
    witnesses = {(zero, source_signature): ()}
    layer_rows = []
    merge_examples = []
    exact_merge_savings = 0

    for depth in range(len(landed) - 1):
        if time.perf_counter() > deadline:
            raise TimeoutError(f"b={bank_count} census exceeded audit timeout")
        following = {}
        following_witnesses = {}
        transitions = 0
        for (used, signature), multiplicity in layer.items():
            for type_index, total_count in enumerate(totals):
                if used[type_index] >= total_count:
                    continue
                transitions += 1
                next_used_list = list(used)
                next_used_list[type_index] += 1
                next_used = tuple(next_used_list)
                next_signature = apply_signature(signature, words[type_index])
                key = (next_used, next_signature)
                next_path = witnesses[(used, signature)] + (type_index,)
                if key in following:
                    following[key] += multiplicity
                    if (
                        len(merge_examples) < 12
                        and sum(totals) - sum(next_used) <= 4
                        and following_witnesses[key] != next_path
                    ):
                        merge_examples.append(
                            {
                                "used": next_used,
                                "left": following_witnesses[key],
                                "right": next_path,
                            }
                        )
                else:
                    following[key] = multiplicity
                    following_witnesses[key] = next_path
        exact_merge_savings += transitions - len(following)
        layer = following
        witnesses = following_witnesses
        indexes.append(set(layer))
        represented = sum(layer.values())
        expected = partial_multiset_count(totals, depth + 1)
        layer_rows.append(
            {
                "depth": depth + 1,
                "exact_states": len(layer),
                "represented_paths": represented,
                "expected_paths": expected,
                "complete_no_prefix_rejection": represented == expected,
            }
        )

    terminal_key = (totals, target)
    target_multiplicity = layer.get(terminal_key, 0)
    recovered = []

    def recover(used, signature, reverse_order):
        depth = sum(used)
        if depth == 0:
            if used == zero and signature == source_signature:
                recovered.append(tuple(reversed(reverse_order)))
            return
        for type_index, used_count in enumerate(used):
            if not used_count:
                continue
            previous = list(used)
            previous[type_index] -= 1
            previous = tuple(previous)
            previous_signature = apply_signature(
                signature, words[type_index], reverse=True
            )
            if (previous, previous_signature) in indexes[depth - 1]:
                recover(
                    previous,
                    previous_signature,
                    reverse_order + (type_index,),
                )

    if target_multiplicity:
        recover(totals, target, ())
    recovered = tuple(sorted(set(recovered)))

    predicate_rows = []
    accepted = []
    for order in recovered:
        program = (landed[0],) + tuple(rows[index] for index in order)
        predicate = acceptance_predicate(bank_count, program, 0, fixtures)
        predicate_rows.append(
            {
                "order": order,
                "pass": predicate["pass"],
                "failed_certificates": predicate["failed_certificates"],
            }
        )
        if predicate["pass"]:
            accepted.append(order)

    anchored_candidates = factorial(sum(totals))
    for count in totals:
        anchored_candidates //= factorial(count)
    order_digest = sha256(
        json.dumps(accepted, separators=(",", ":")).encode()
    ).hexdigest()
    return {
        "banks": bank_count,
        "stations": len(landed),
        "landed": landed,
        "landed_order": landed_order,
        "fixtures": fixtures,
        "type_rows": rows,
        "type_words": words,
        "type_totals": totals,
        "source_signature": source_signature,
        "target_signature": target,
        "anchored_candidates": anchored_candidates,
        "station_labelled_candidates": len(landed) * anchored_candidates,
        "terminal_represented_candidates": sum(layer.values()),
        "target_multiplicity": target_multiplicity,
        "recovered_orders": recovered,
        "accepted_orders": tuple(accepted),
        "accepted_classes": len(accepted),
        "accepted_station_rotations": len(accepted) * len(landed),
        "landed_accepted": landed_order in accepted,
        "predicate_rows": tuple(predicate_rows),
        "order_sha256": order_digest,
        "accepted_order_sample": tuple(accepted[:5]),
        "layer_rows": tuple(layer_rows),
        "merge_examples": tuple(merge_examples),
        "exact_merge_savings": exact_merge_savings,
        "runtime_sec": round(time.perf_counter() - started, 6),
    }


def program_from_order(census, order):
    return (census["landed"][0],) + tuple(
        census["type_rows"][index] for index in order
    )


def rotate_program(program, token_start, shift):
    count = len(program)
    rotated = [None] * count
    for station, row in enumerate(program):
        rotated[(station + shift) % count] = row
    return tuple(rotated), (token_start + shift) % count


def adjacent_swap_from_accepted(order, accepted_orders):
    for index in range(len(order) - 1):
        candidate = list(order)
        candidate[index], candidate[index + 1] = (
            candidate[index + 1],
            candidate[index],
        )
        if tuple(candidate) in accepted_orders:
            return True
    return False


def predicate_recount(censuses, primary):
    held = {}
    landed = {}
    frozen_accepted = []
    frozen_rejected = []
    for bank_count in (1, 2):
        held_row = K.held_certificate(bank_count)
        held[bank_count] = {
            key: value
            for key, value in held_row.items()
            if key not in ("state", "chain")
        }
        census = censuses[bank_count]
        landed[bank_count] = acceptance_predicate(
            bank_count,
            census["landed"],
            0,
            census["fixtures"],
        )
        for order in FROZEN_ACCEPTED_ORDERS[bank_count]:
            result = acceptance_predicate(
                bank_count,
                program_from_order(census, order),
                0,
                census["fixtures"],
            )
            frozen_accepted.append(
                {
                    "banks": bank_count,
                    "order": order,
                    "member_of_recounted_accepted_set": (
                        order in census["accepted_orders"]
                    ),
                    "pass": result["pass"],
                    "failed_certificates": result["failed_certificates"],
                }
            )
        for order in FROZEN_REJECTED_ORDERS[bank_count]:
            result = acceptance_predicate(
                bank_count,
                program_from_order(census, order),
                0,
                census["fixtures"],
            )
            frozen_rejected.append(
                {
                    "banks": bank_count,
                    "order": order,
                    "outside_recounted_accepted_set": (
                        order not in census["accepted_orders"]
                    ),
                    "adjacent_swap_from_accepted_boundary": (
                        adjacent_swap_from_accepted(
                            order, census["accepted_orders"]
                        )
                    ),
                    "pass": result["pass"],
                    "recorded_failed_certificates": (
                        result["failed_certificates"]
                    ),
                    "expected_failed_certificates": (
                        FROZEN_REJECTED_CERTIFICATES[bank_count]
                    ),
                    "certificate_record_matches": (
                        result["failed_certificates"]
                        == FROZEN_REJECTED_CERTIFICATES[bank_count]
                    ),
                    "failure_counts": result["failure_counts"],
                }
            )

    controls = K.order_and_domain_controls()
    held_pass = all(
        row[key] == 0
        for row in held.values()
        for key in (
            "logical_failures",
            "fixed_word_failures",
            "inverse_failures",
            "postimage_failures",
            "token_return_failures",
        )
    )
    frozen_sample_matches = all(
        FROZEN_ACCEPTED_ORDERS[bank_count]
        == censuses[bank_count]["accepted_orders"][
            : primary["accepted_example_limit"]
        ]
        for bank_count in (1, 2)
    )
    return {
        "K_held_certificates": held,
        "K_order_and_domain_controls": controls,
        "landed": landed,
        "frozen_accepted": frozen_accepted,
        "frozen_accepted_matches_primary_example_ranks": (
            frozen_sample_matches
        ),
        "frozen_rejected": frozen_rejected,
        "pass": (
            held_pass
            and all(controls.values())
            and all(row["pass"] for row in landed.values())
            and all(
                row["pass"] and row["member_of_recounted_accepted_set"]
                for row in frozen_accepted
            )
            and frozen_sample_matches
            and all(
                not row["pass"]
                and row["outside_recounted_accepted_set"]
                and row["adjacent_swap_from_accepted_boundary"]
                and bool(row["recorded_failed_certificates"])
                and row["certificate_record_matches"]
                for row in frozen_rejected
            )
        ),
    }


def validate_merge_windows(census):
    checked = failures = suffixes_checked = 0
    totals = census["type_totals"]
    words = census["type_words"]
    source = census["source_signature"]
    for example in census["merge_examples"]:
        left = signature_from_order(source, words, example["left"])
        right = signature_from_order(source, words, example["right"])
        if left != right:
            failures += 1
            continue
        remaining = tuple(
            total - used
            for total, used in zip(totals, example["used"])
        )
        for suffix in unique_sequences(remaining):
            left_end = signature_from_order(left, words, suffix)
            right_end = signature_from_order(right, words, suffix)
            suffixes_checked += 1
            failures += left_end != right_end
        checked += 1
    return {
        "merge_windows_checked": checked,
        "suffixes_checked": suffixes_checked,
        "failures": failures,
    }


def pruning_validation(censuses, primary):
    b1 = censuses[1]
    b2 = censuses[2]

    # Full b=1 enumeration before source anchoring: all 3! station-labelled
    # programs collapse to exactly the two anchored classes.
    full_rows = tuple(b1["landed"])
    full_orders = tuple(unique_sequences((1,) * len(full_rows)))
    canonical = set()
    rotation_predicate_failures = 0
    for permutation in full_orders:
        program = tuple(full_rows[index] for index in permutation)
        source_station = next(
            index for index, row in enumerate(program) if row[0] == "source"
        )
        anchored, token = rotate_program(
            program, source_station, -source_station
        )
        canonical.add(tuple(role_key(row) for row in anchored))
        base = acceptance_predicate(1, anchored, token, b1["fixtures"])["pass"]
        for shift in range(len(program)):
            rotated, shifted_token = rotate_program(anchored, token, shift)
            observed = acceptance_predicate(
                1, rotated, shifted_token, b1["fixtures"]
            )["pass"]
            rotation_predicate_failures += observed != base

    duplicates = [
        (left, right)
        for left, left_row in enumerate(b2["landed"])
        for right, right_row in enumerate(b2["landed"])
        if left < right and role_key(left_row) == role_key(right_row)
    ]
    duplicate_word_failures = sum(
        b2["landed"][left] != b2["landed"][right]
        or K.mapped_macro(b2["landed"][left])
        != K.mapped_macro(b2["landed"][right])
        for left, right in duplicates
    )

    b1_naive_accepted = []
    for order in unique_sequences(b1["type_totals"]):
        if acceptance_predicate(
            1, program_from_order(b1, order), 0, b1["fixtures"]
        )["pass"]:
            b1_naive_accepted.append(order)

    merge_windows = {
        bank_count: validate_merge_windows(censuses[bank_count])
        for bank_count in (1, 2)
    }
    complete_only = all(
        row["complete_no_prefix_rejection"]
        for census in censuses.values()
        for row in census["layer_rows"]
    )
    primary_rules = tuple(
        (row.get("rule"), row.get("safety"))
        for row in primary["pruning_rules"]
    )
    rules = {
        "unique_source_rotation": {
            "pass": (
                len(full_orders) == 6
                and len(canonical) == 2
                and rotation_predicate_failures == 0
                and all(
                    row["station_labelled_candidates"]
                    == row["stations"] * row["anchored_candidates"]
                    for row in censuses.values()
                )
            ),
            "full_b1_programs": len(full_orders),
            "full_b1_anchored_classes": len(canonical),
            "rotation_predicate_failures": rotation_predicate_failures,
            "justification": (
                "The source is unique, so every oriented-ring station "
                "translation orbit has one source-at-zero representative."
            ),
        },
        "identical_copy_exchange": {
            "pass": (
                duplicates == [(4, 7)]
                and duplicate_word_failures == 0
                and b2["anchored_candidates"] * 2 == factorial(10)
            ),
            "duplicate_station_pairs": duplicates,
            "duplicate_word_failures": duplicate_word_failures,
            "raw_copy_labelled_orders": factorial(10),
            "quotiented_orders": b2["anchored_candidates"],
            "justification": (
                "The only repeated role is the literally equal relay-swap "
                "row; exchanging its two artificial copy labels changes no "
                "program row or K action."
            ),
        },
        "exact_state_merge": {
            "pass": (
                b2["exact_merge_savings"] > 0
                and all(
                    row["failures"] == 0
                    for row in merge_windows.values()
                )
                and merge_windows[2]["merge_windows_checked"] > 0
            ),
            "merge_savings": {
                bank_count: census["exact_merge_savings"]
                for bank_count, census in censuses.items()
            },
            "windows": merge_windows,
            "justification": (
                "K macro action is deterministic; byte-identical tuples of "
                "all held states with identical used counts have identical "
                "future actions. Twelve sampled merge nodes are rechecked "
                "over all 252 compatible suffixes in those samples."
            ),
        },
        "complete_only_rejection": {
            "pass": (
                complete_only
                and tuple(b1_naive_accepted) == b1["accepted_orders"]
                and all(
                    census["terminal_represented_candidates"]
                    == census["anchored_candidates"]
                    for census in censuses.values()
                )
            ),
            "all_layer_path_counts_exact": complete_only,
            "b1_naive_accepted": tuple(b1_naive_accepted),
            "justification": (
                "Every partial multiset path is represented at every depth; "
                "only complete signatures unequal to K's held target fail."
            ),
        },
    }
    return {
        "primary_rules_extracted": primary_rules,
        "rules": rules,
        "pass": len(primary_rules) == 4
        and all(row["pass"] for row in rules.values()),
    }


def translation_equivariance_recount(censuses):
    tested = failures = roundtrip_failures = 0
    by_bank = {}
    for bank_count in (1, 2):
        census = censuses[bank_count]
        local_tested = local_failures = 0
        for order in census["accepted_orders"]:
            program = program_from_order(census, order)
            for shift in range(len(program)):
                rotated, token = rotate_program(program, 0, shift)
                restored, restored_token = rotate_program(
                    rotated, token, -shift
                )
                roundtrip_failures += (
                    restored != program or restored_token != 0
                )
                result = acceptance_predicate(
                    bank_count,
                    rotated,
                    token,
                    census["fixtures"],
                )
                tested += 1
                local_tested += 1
                failures += not result["pass"]
                local_failures += not result["pass"]
        by_bank[bank_count] = {
            "translation_checks": local_tested,
            "failures": local_failures,
        }
    return {
        "translation_checks": tested,
        "closure_failures": failures,
        "roundtrip_failures": roundtrip_failures,
        "by_bank": by_bank,
        "pass": (
            tested == 894
            and failures == 0
            and roundtrip_failures == 0
            and by_bank[1]["translation_checks"] == 3
            and by_bank[2]["translation_checks"] == 891
        ),
    }


def public_census(census):
    return {
        key: value
        for key, value in census.items()
        if key
        not in {
            "landed",
            "fixtures",
            "type_rows",
            "type_words",
            "source_signature",
            "target_signature",
            "recovered_orders",
            "accepted_orders",
            "predicate_rows",
            "merge_examples",
        }
    }


def without_runtime_fields(value):
    """Remove all timing observations from a report-digest payload."""
    if isinstance(value, dict):
        return {
            key: without_runtime_fields(item)
            for key, item in value.items()
            if key != "runtime_sec"
        }
    if isinstance(value, list):
        return [without_runtime_fields(item) for item in value]
    if isinstance(value, tuple):
        return tuple(without_runtime_fields(item) for item in value)
    return value


def build_report():
    started = time.perf_counter()
    deadline = started + AUDIT_TIMEOUT_SEC
    primary = extract_primary()
    censuses = {
        bank_count: enumerate_census(bank_count, deadline)
        for bank_count in (1, 2)
    }
    predicate = predicate_recount(censuses, primary)
    pruning = pruning_validation(censuses, primary)
    passive = translation_equivariance_recount(censuses)

    b1 = censuses[1]
    b2 = censuses[2]
    primary_census = primary["census_literals"]
    extraction_pass = (
        primary["audit_tuple_literal"]
        and primary["audit_input_paths"] == AUDIT_INPUT_PATHS
        and not primary["missing_predicate_calls"]
        and not primary["missing_anchor_calls"]
        and not primary["missing_battery_keys"]
        and len(primary["pruning_rules"]) == 4
        and primary_census["b1"].get("anchored_candidate_classes") == 2
        and primary_census["b1"].get("accepted_arrangement_classes") == 1
        and primary_census["b2"].get("anchored_candidate_classes")
        == 1_814_400
        and primary_census["b2"].get("exact_target_classes") == 81
        and primary_census["b2"].get("accepted_arrangement_classes") == 81
        and primary_census["passive"].get("labelled_rotations_tested") == 894
        and not primary["missing_boundary_keys"]
        and primary["outcome_B_81_of_1814400_present"]
        and primary["accepted_example_limit"] == 5
    )
    census_pass = (
        b1["anchored_candidates"] == 2
        and b1["terminal_represented_candidates"] == 2
        and b1["target_multiplicity"] == 1
        and b1["accepted_classes"] == 1
        and b1["landed_accepted"]
        and b2["anchored_candidates"] == 1_814_400
        and b2["terminal_represented_candidates"] == 1_814_400
        and b2["target_multiplicity"] == 81
        and b2["accepted_classes"] == 81
        and b2["landed_accepted"]
    )
    boundary_statement = (
        "Within b<=2, the supplied Cycle 719 held-fixture predicate accepts "
        "81 of 1,814,400 fixed-inventory arrangements at b=2 (Outcome B); "
        "it does not select one arrangement and makes no claim beyond b<=2."
    )
    discipline = {
        "blocklist": BLOCKLIST,
        "blocklist_clean": (
            primary["blocklist_module_absent"]
            and Path(K.__file__).resolve()
            == (ROOT / AUDIT_INPUT_PATHS[0]).resolve()
        ),
        "only_scientific_import": K_MODULE,
        "outcome": "B",
        "outcome_language": OUTCOME_LANGUAGE,
        "scope_language": SCOPE_LANGUAGE,
        "boundary_statement": boundary_statement,
        "language_verbatim": (
            OUTCOME_LANGUAGE in boundary_statement
            and boundary_statement.count(SCOPE_LANGUAGE) >= 2
        ),
    }
    runtime = time.perf_counter() - started
    checks = {
        "extraction": extraction_pass,
        "predicate_recount": predicate["pass"],
        "census_recount_full_b1_b2": census_pass,
        "pruning_validation": pruning["pass"],
        "translation_equivariance_894": passive["pass"],
        "discipline": (
            discipline["blocklist_clean"]
            and discipline["language_verbatim"]
            and discipline["outcome"] == "B"
        ),
        "runtime_within_1800_seconds": runtime < AUDIT_TIMEOUT_SEC,
    }
    report = {
        "audit_timeout_sec": AUDIT_TIMEOUT_SEC,
        "note_path": NOTE_PATH,
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "checks": checks,
        "pass": all(checks.values()),
        "extraction": primary,
        "predicate_recount": predicate,
        "census_recount": {
            bank_count: public_census(census)
            for bank_count, census in censuses.items()
        },
        "pruning_validation": pruning,
        "translation_equivariance_recount": passive,
        "discipline": discipline,
        "runtime_sec": round(runtime, 6),
    }
    digestable = without_runtime_fields(report)
    report["report_sha256"] = sha256(
        json.dumps(digestable, sort_keys=True, default=str).encode()
    ).hexdigest()
    return report


def emit(label, passed, detail):
    print("PASS" if passed else "FAIL", label, "::", detail)


def main():
    started = time.perf_counter()
    try:
        report = build_report()
    except Exception as error:
        emit(
            "cycle755_independent_checker_exception",
            False,
            f"{type(error).__name__}: {error}",
        )
        summary = {
            "pass": False,
            "error_type": type(error).__name__,
            "error": str(error),
            "runtime_sec": round(time.perf_counter() - started, 6),
        }
        print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
        return 1

    for label, passed in report["checks"].items():
        emit(label, passed, passed)
    payload = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    if len(payload.encode()) >= 145_000:
        emit("stdout_payload_under_150KB", False, len(payload.encode()))
        return 1
    emit("stdout_payload_under_150KB", True, len(payload.encode()))
    print("SUMMARY_JSON", payload)
    print(
        "CYCLE755_PROGRAM_ORDER_INDEPENDENT_CHECK_PASS"
        if report["pass"]
        else "CYCLE755_PROGRAM_ORDER_INDEPENDENT_CHECK_FAIL"
    )
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
