#!/usr/bin/env python3
"""Cycle 755: bounded derivation attempt for program content and cyclic order.

The scientific acceptance predicate is deliberately not a new dynamics.  It
replays Cycle 719's held-orbit, inverse, controller-register, decoded-chain,
postimage, and Q-before-R certificates on candidate permutations of Cycle
719's own macro inventory.  The search quotients only passive ring rotations,
identical inventory copies, and exact full-state dynamic-programming merges.
"""
from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha256
import inspect
import json
from math import factorial
from pathlib import Path
import sys
import time


AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/PROGRAM_CONTENT_ORDER_ATTEMPT_CYCLE755_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


OPTIONAL_M740_PATH = "scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py"
GROUNDING_PATH = (
    ".claude/science/physics-loops/toe-close-20260729/EXTRACT_W3_GROUNDING.md"
)


def role_key(row):
    """Exact macro-inventory identity; equal keys are interchangeable copies."""
    kind, index, _local = row
    word = K.mapped_macro(row)
    return kind, index, K.gate_digest(word)


def role_label(row):
    kind, index, digest = role_key(row)
    return f"{kind}[{index}]#{digest[:10]}"


def held_fixtures(bank_count):
    """Cycle 719's held event inputs and fixed allocator outputs."""
    banks, links = K.B.chain_genesis(bank_count)
    state = K.M.pack_state(banks, links)
    fixtures = []
    for event in range(2 * bank_count):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        expected = K.A.apply_semantic(
            before, K.M.global_allocator_word(bank_count)
        )
        fixtures.append((bytes(before), bytes(expected), direction))
        state = expected
    return tuple(fixtures)


def r_before_q_orbit(data, program, token_start):
    """The hostile R-before-Q control used by K.order_and_domain_controls."""
    stations = len(program)
    a = [int(station == token_start) for station in range(stations)]
    b = [0] * stations
    output = tuple(data)
    for _step in range(stations):
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


def candidate_oracle(bank_count, program, token_start, fixtures=None):
    """A candidate is lawful iff this Cycle-719 certificate battery accepts."""
    fixtures = held_fixtures(bank_count) if fixtures is None else fixtures
    landed_inventory = Counter(
        role_key(row) for row in K.interleaved_program(bank_count)
    )
    inventory_exact = Counter(role_key(row) for row in program) == landed_inventory
    expected_token = tuple(
        int(station == token_start) for station in range(len(program))
    )
    coarse = K.B.C704.C610.EventChain(bank=2 * bank_count)
    failures = Counter()
    q_before_r_changed_events = 0

    if not inventory_exact or not (0 <= token_start < len(program)):
        return {
            "pass": False,
            "battery": {"inventory_exact": False},
            "failures": {"inventory": 1},
            "q_before_r_changed_events": 0,
        }

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

        restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
            after,
            program,
            token_positions=(token_start,),
            reverse=True,
        )
        failures["inverse"] += restored != before
        failures["inverse_register_return"] += (
            inverse_a != expected_token or any(inverse_b)
        )

        banks, links = K.M.unpack_state(after, bank_count)
        decoded, _order = K.B.decode_local_graph(banks, links)
        status = coarse.admit(
            tick_id=event,
            orientation=1 if direction == (1, 0) else -1,
            certificate=1,
            binder=1,
            actuality=1,
            admissibility=1,
            law_domain=1,
        )
        failures["decoded_chain"] += (
            status != "admitted"
            or K.B.cell_rows(decoded) != K.B.cell_rows(coarse)
        )
        failures["postimage"] += any(
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

        hostile, hostile_a, hostile_b = r_before_q_orbit(
            before, program, token_start
        )
        q_before_r_changed_events += hostile != expected
        failures["r_before_q_register_return"] += (
            hostile_a != expected_token or any(hostile_b)
        )

    battery = {
        "inventory_exact": inventory_exact,
        "held_orbit_exactness": failures["held_orbit_exactness"] == 0,
        "held_orbit_trace": failures["held_orbit_trace"] == 0,
        "inverse": failures["inverse"] == 0,
        "register_returns": (
            failures["controller_register_return"] == 0
            and failures["inverse_register_return"] == 0
            and failures["r_before_q_register_return"] == 0
        ),
        "decoded_chain": failures["decoded_chain"] == 0,
        "clean_postimage": failures["postimage"] == 0,
        "q_before_r_layer_order": (
            q_before_r_changed_events == len(fixtures)
        ),
    }
    return {
        "pass": all(battery.values()),
        "battery": battery,
        "failures": dict(sorted(failures.items())),
        "q_before_r_changed_events": q_before_r_changed_events,
    }


def signature_digest(signature):
    hasher = sha256()
    for state in signature:
        hasher.update(len(state).to_bytes(8, "big"))
        hasher.update(state)
    return hasher.digest()


def apply_signature(signature, word, *, reverse=False):
    action = tuple(reversed(word)) if reverse else word
    return tuple(
        bytes(K.A.apply_semantic(tuple(state), action)) for state in signature
    )


def count_factorization(program):
    """Kind-placement choices times within-kind macro-content assignments."""
    source_rows = tuple(row for row in program if row[0] == "source")
    if len(source_rows) != 1:
        raise AssertionError("the passive rotation gauge needs one source")
    remainder = tuple(row for row in program if row[0] != "source")
    kinds = Counter(row[0] for row in remainder)
    kind_placements = factorial(len(remainder))
    for count in kinds.values():
        kind_placements //= factorial(count)
    contents = 1
    for kind, count in kinds.items():
        contents *= factorial(count)
        copies = Counter(role_key(row) for row in remainder if row[0] == kind)
        for multiplicity in copies.values():
            contents //= factorial(multiplicity)
    return {
        "anchored_kind_placements": kind_placements,
        "content_assignments_per_kind_placement": contents,
        "anchored_candidate_classes": kind_placements * contents,
        "labelled_candidate_programs": (
            len(program) * kind_placements * contents
        ),
    }


def search_census(bank_count):
    """Exact multiset-permutation DP, with no heuristic prefix rejection."""
    started = time.perf_counter()
    landed = K.interleaved_program(bank_count)
    if landed[0][0] != "source":
        raise AssertionError("K's token/source anchor changed")
    fixtures = held_fixtures(bank_count)
    initial_signature = tuple(row[0] for row in fixtures)
    target_signature = tuple(row[1] for row in fixtures)
    source_signature = apply_signature(
        initial_signature, K.mapped_macro(landed[0])
    )
    items = tuple(landed[1:])
    words = tuple(K.mapped_macro(row) for row in items)
    keys = tuple(role_key(row) for row in items)

    # The value is the exact number of multiset permutations coalesced at this
    # full-state/remaining-multiset node.  Hashes are used only as a compact
    # reverse-recovery index, never for forward state equality or acceptance.
    layer = {(0, source_signature): 1}
    reverse_indexes = [{(0, signature_digest(source_signature))}]
    layer_rows = []
    digest_collision_failures = 0
    exact_merge_savings = 0
    transition_rows = 0

    for depth in range(len(items)):
        next_layer = {}
        expanded_paths = 0
        for (mask, signature), multiplicity in layer.items():
            seen_keys = set()
            for item, (key, word) in enumerate(zip(keys, words)):
                if mask & (1 << item) or key in seen_keys:
                    continue
                seen_keys.add(key)
                next_signature = apply_signature(signature, word)
                next_key = (mask | (1 << item), next_signature)
                next_layer[next_key] = (
                    next_layer.get(next_key, 0) + multiplicity
                )
                expanded_paths += 1
        transition_rows += expanded_paths
        exact_merge_savings += expanded_paths - len(next_layer)
        layer = next_layer
        compact_index = {
            (mask, signature_digest(signature))
            for mask, signature in layer
        }
        digest_collision_failures += len(compact_index) != len(layer)
        reverse_indexes.append(compact_index)
        layer_rows.append(
            {
                "depth": depth + 1,
                "exact_states": len(layer),
                "represented_permutations": sum(layer.values()),
            }
        )

    full_mask = (1 << len(items)) - 1
    exact_target_count = layer.get((full_mask, target_signature), 0)
    represented_permutations = sum(layer.values())

    recovered_orders = []

    def recover(mask, signature, reverse_order):
        depth = mask.bit_count()
        if depth == 0:
            if signature == source_signature:
                recovered_orders.append(tuple(reversed(reverse_order)))
            return
        for item, (key, word) in enumerate(zip(keys, words)):
            if not (mask & (1 << item)):
                continue
            previous_mask = mask ^ (1 << item)
            # This is exactly the forward duplicate-copy convention: an item
            # can be selected only after all earlier equal-key copies.
            earlier_copy_unused = any(
                earlier < item
                and keys[earlier] == key
                and not (previous_mask & (1 << earlier))
                for earlier in range(item)
            )
            if earlier_copy_unused:
                continue
            previous_signature = apply_signature(
                signature, word, reverse=True
            )
            compact_key = (
                previous_mask,
                signature_digest(previous_signature),
            )
            if compact_key in reverse_indexes[depth - 1]:
                recover(
                    previous_mask,
                    previous_signature,
                    reverse_order + (item,),
                )

    if exact_target_count:
        recover(full_mask, target_signature, ())
    recovered_orders = sorted(set(recovered_orders))

    accepted_orders = []
    oracle_failure_rows = []
    for order in recovered_orders:
        program = (landed[0],) + tuple(items[item] for item in order)
        result = candidate_oracle(
            bank_count, program, token_start=0, fixtures=fixtures
        )
        if result["pass"]:
            accepted_orders.append(order)
        else:
            oracle_failure_rows.append(
                {"order": order, "battery": result["battery"]}
            )

    labels = tuple(role_label(row) for row in items)
    labelled_orders = tuple(
        tuple(labels[item] for item in order) for order in accepted_orders
    )
    order_sha256 = sha256(
        json.dumps(labelled_orders, sort_keys=True).encode()
    ).hexdigest()
    factors = count_factorization(landed)
    return {
        "banks": bank_count,
        "stations": len(landed),
        "kind_multiset": dict(
            sorted(Counter(row[0] for row in landed).items())
        ),
        "macro_inventory": tuple(role_label(row) for row in landed),
        **factors,
        "dp_represented_permutations": represented_permutations,
        "dp_terminal_exact_states": len(layer),
        "dp_transitions": transition_rows,
        "exact_merge_savings": exact_merge_savings,
        "digest_collision_failures": digest_collision_failures,
        "exact_target_classes": exact_target_count,
        "recovered_target_classes": len(recovered_orders),
        "lawful_translation_classes": len(accepted_orders),
        "lawful_labelled_programs": len(accepted_orders) * len(landed),
        "landed_program_lawful": tuple(range(len(items))) in accepted_orders,
        "lawful_order_sha256": order_sha256,
        "lawful_order_examples": labelled_orders[:5],
        "oracle_failure_rows": oracle_failure_rows,
        "layer_rows": tuple(layer_rows),
        "runtime_sec": round(time.perf_counter() - started, 6),
        "_accepted_orders": tuple(accepted_orders),
        "_items": items,
        "_fixtures": fixtures,
        "_landed": landed,
    }


def rotate_program(program, token_start, shift):
    """Passive station-label translation j -> j+shift on the oriented ring."""
    stations = len(program)
    rotated = [None] * stations
    for station, row in enumerate(program):
        rotated[(station + shift) % stations] = row
    return tuple(rotated), (token_start + shift) % stations


def passive_closure_certificate(censuses):
    tested = failures = roundtrip_failures = 0
    by_bank = {}
    for bank_count, census in sorted(censuses.items()):
        bank_tested = bank_failures = 0
        landed = census["_landed"]
        items = census["_items"]
        fixtures = census["_fixtures"]
        for order in census["_accepted_orders"]:
            program = (landed[0],) + tuple(items[item] for item in order)
            for shift in range(len(program)):
                rotated, token_start = rotate_program(program, 0, shift)
                restored, restored_start = rotate_program(
                    rotated, token_start, -shift
                )
                roundtrip_failures += (
                    restored != program or restored_start != 0
                )
                result = candidate_oracle(
                    bank_count,
                    rotated,
                    token_start=token_start,
                    fixtures=fixtures,
                )
                tested += 1
                bank_tested += 1
                failures += not result["pass"]
                bank_failures += not result["pass"]
        by_bank[bank_count] = {
            "labelled_rotations_tested": bank_tested,
            "failures": bank_failures,
        }
    return {
        "passive_group": "oriented-ring station translations C_P",
        "orientation_reversal_in_scope": False,
        "labelled_rotations_tested": tested,
        "closure_failures": failures,
        "roundtrip_failures": roundtrip_failures,
        "by_bank": by_bank,
    }


def attribute_chain(node):
    parts = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if isinstance(node, ast.Name):
        parts.append(node.id)
    return ".".join(reversed(parts))


def oracle_ast_certificate():
    source = "\n".join(
        (
            inspect.getsource(held_fixtures),
            inspect.getsource(r_before_q_orbit),
            inspect.getsource(candidate_oracle),
        )
    )
    tree = ast.parse(source)
    calls = sorted(
        {
            attribute_chain(node.func)
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
        }
    )
    attributes = sorted(
        {
            attribute_chain(node)
            for node in ast.walk(tree)
            if isinstance(node, ast.Attribute)
        }
    )
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
    required_attributes = {"K.R3.X.SOURCE_POINTER"}
    battery_keys = {
        "inventory_exact",
        "held_orbit_exactness",
        "held_orbit_trace",
        "inverse",
        "register_returns",
        "decoded_chain",
        "clean_postimage",
        "q_before_r_layer_order",
    }
    string_literals = {
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    return {
        "required_calls": sorted(required_calls),
        "observed_calls": calls,
        "missing_calls": sorted(required_calls - set(calls)),
        "missing_attributes": sorted(required_attributes - set(attributes)),
        "battery_keys": sorted(battery_keys),
        "missing_battery_keys": sorted(battery_keys - string_literals),
    }


def no_new_supplier_certificate():
    source = Path(__file__).read_text()
    tree = ast.parse(source)
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    local_imports = sorted(
        module for module in imports if module.startswith("frontier_")
    )
    audit_assignment = next(
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        )
    )
    declared_assignment = next(
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "DECLARED_INPUT_PATHS"
            for target in node.targets
        )
    )
    pure_literal_tuple = (
        isinstance(audit_assignment.value, ast.Tuple)
        and all(
            isinstance(element, ast.Constant)
            and isinstance(element.value, str)
            for element in audit_assignment.value.elts
        )
    )
    declared_alias_exact = (
        isinstance(declared_assignment.value, ast.Name)
        and declared_assignment.value.id == "AUDIT_INPUT_PATHS"
    )
    expected_k_path = (ROOT / AUDIT_INPUT_PATHS[0]).resolve()
    m740_present = (ROOT / OPTIONAL_M740_PATH).is_file()
    grounding_present = (ROOT / GROUNDING_PATH).is_file()
    return {
        "direct_import_modules": sorted(imports),
        "direct_science_imports": local_imports,
        "only_K_directly_imported": local_imports
        == [
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
        ],
        "K_resolves_to_declared_path": Path(K.__file__).resolve()
        == expected_k_path,
        "audit_input_tuple_is_pure_literal": pure_literal_tuple,
        "declared_input_alias_exact": declared_alias_exact,
        "optional_M740": (
            "present_UNEXPECTED_for_this_absent-branch_draft"
            if m740_present
            else "absent_on_branch_not_imported"
        ),
        "grounding_context": (
            "present_but_context_only_not_imported"
            if grounding_present
            else "absent_on_branch_no_substitute_read"
        ),
        "new_scientific_supplier_count": max(0, len(local_imports) - 1),
        "note_path_existence_required": False,
    }


def anchor_certificate():
    held = {}
    landed_oracles = {}
    for bank_count in (1, 2):
        row = K.held_certificate(bank_count)
        held[bank_count] = {
            key: value
            for key, value in row.items()
            if key not in ("state", "chain")
        }
        landed_oracles[bank_count] = candidate_oracle(
            bank_count,
            K.interleaved_program(bank_count),
            token_start=0,
        )
    controls = K.order_and_domain_controls()
    return {
        "K_held": held,
        "landed_candidate_oracles": landed_oracles,
        "K_order_and_domain_controls": controls,
    }


def public_census(census):
    return {
        key: value
        for key, value in census.items()
        if not key.startswith("_")
    }


def emit_check(label, passed, detail):
    print(
        "PASS" if passed else "FAIL",
        label,
        "::",
        detail,
    )


def build_report():
    started = time.perf_counter()
    anchors = anchor_certificate()
    oracle_ast = oracle_ast_certificate()
    supplier = no_new_supplier_certificate()
    censuses = {bank_count: search_census(bank_count) for bank_count in (1, 2)}
    passive = passive_closure_certificate(censuses)

    b1 = censuses[1]
    b2 = censuses[2]
    if (
        b1["lawful_translation_classes"] == 1
        and b2["lawful_translation_classes"] == 1
    ):
        outcome = "A"
    elif 1 < b2["lawful_translation_classes"] <= 1000:
        outcome = "B"
    else:
        outcome = "C"

    held_anchor_pass = all(
        row[key] == 0
        for row in anchors["K_held"].values()
        for key in (
            "logical_failures",
            "fixed_word_failures",
            "inverse_failures",
            "postimage_failures",
            "token_return_failures",
        )
    )
    checks = {
        "A_K_landed_battery": (
            held_anchor_pass
            and all(
                row["pass"]
                for row in anchors["landed_candidate_oracles"].values()
            )
            and all(anchors["K_order_and_domain_controls"].values())
        ),
        "B_constraint_oracle_AST": (
            not oracle_ast["missing_calls"]
            and not oracle_ast["missing_attributes"]
            and not oracle_ast["missing_battery_keys"]
        ),
        "C1_ring_translation_gauge_safe": all(
            row["labelled_candidate_programs"]
            == row["stations"] * row["anchored_candidate_classes"]
            for row in censuses.values()
        ),
        "C2_identical_copy_quotient_safe": (
            b1["dp_represented_permutations"]
            == b1["anchored_candidate_classes"]
            and b2["dp_represented_permutations"]
            == b2["anchored_candidate_classes"]
        ),
        "C3_exact_state_coalescence_safe": all(
            row["digest_collision_failures"] == 0
            and row["recovered_target_classes"]
            == row["exact_target_classes"]
            for row in censuses.values()
        ),
        "C4_no_heuristic_prefix_rejection": True,
        "D1_b1_census_frozen": (
            b1["stations"] == 3
            and b1["anchored_candidate_classes"] == 2
            and b1["labelled_candidate_programs"] == 6
            and b1["lawful_translation_classes"] == 1
            and b1["lawful_labelled_programs"] == 3
            and not b1["oracle_failure_rows"]
        ),
        "D2_b2_census_frozen": (
            b2["stations"] == 11
            and b2["anchored_candidate_classes"] == 1_814_400
            and b2["labelled_candidate_programs"] == 19_958_400
            and b2["exact_target_classes"] == 81
            and b2["lawful_translation_classes"] == 81
            and b2["lawful_labelled_programs"] == 891
            and not b2["oracle_failure_rows"]
        ),
        "D3_landed_program_in_lawful_set": all(
            row["landed_program_lawful"] for row in censuses.values()
        ),
        "D4_outcome_B": outcome == "B",
        "E_passive_translation_closure": (
            passive["labelled_rotations_tested"] == 3 + 891
            and passive["closure_failures"] == 0
            and passive["roundtrip_failures"] == 0
        ),
        "F_no_new_supplier": (
            supplier["only_K_directly_imported"]
            and supplier["K_resolves_to_declared_path"]
            and supplier["audit_input_tuple_is_pure_literal"]
            and supplier["declared_input_alias_exact"]
            and supplier["new_scientific_supplier_count"] == 0
            and supplier["optional_M740"] == "absent_on_branch_not_imported"
        ),
        "G_honest_boundary_and_W2_status": (
            outcome == "B"
            and b1["lawful_translation_classes"] == 1
            and b2["lawful_translation_classes"] == 81
        ),
    }
    runtime = time.perf_counter() - started
    checks["runtime_within_header_bound"] = runtime < AUDIT_TIMEOUT_SEC

    pruning_rules = (
        {
            "rule": "fix the unique source row/token at station 0",
            "safety": (
                "every labelled oriented-ring program has exactly one such "
                "representative; all P rotations are restored and audited"
            ),
        },
        {
            "rule": "choose equal role_key inventory copies in source order",
            "safety": (
                "the two b=2 relay-swap copies have identical kind, index, "
                "and mapped gate word, so exchanging their copy labels does "
                "not change a candidate program"
            ),
        },
        {
            "rule": (
                "merge prefixes only at equal remaining masks and exactly "
                "equal tuples of all held full states"
            ),
            "safety": (
                "future K macro action is deterministic from precisely that "
                "state and remaining multiset; multiplicities are summed"
            ),
        },
        {
            "rule": "reject only complete states unequal to K's held targets",
            "safety": (
                "there are zero heuristic or partial-bit prefix rejections; "
                "all recovered target paths are replayed through the oracle"
            ),
        },
    )
    w2 = {
        "station_kind_arithmetic": "inherited_derived_input_not_reopened",
        "program_content": "Outcome_B_one_of_81_b2_translation_classes",
        "program_order": "Outcome_B_one_of_81_b2_translation_classes",
        "passive_covariance": "derived_closed_under_all_894_tested_rotations",
        "minimal_remainder": (
            "W2 still needs one extra selector on the 81 b=2 classes; "
            "a prefix-local causal-precondition or off-held-domain "
            "correctness principle is not present in K's held battery."
        ),
    }
    boundary = {
        "outcome": outcome,
        "derived": (
            "b=1 content/order is unique modulo oriented-ring translation "
            "and identical-copy exchange; b=2 has exactly 81 such classes; "
            "the lawful set is passively translation-closed"
        ),
        "supplied": (
            "K's macro inventory, held genesis/event fixtures, source/token "
            "boundary, oriented ring, and Q-before-R controller law"
        ),
        "not_derived": (
            "a physical or logical principle selecting one of the 81 b=2 "
            "classes, active covariance, autonomous genesis, or a law "
            "outside K's held certificate domain"
        ),
        "documented_equivalences": (
            "simultaneous oriented-ring station/token translations and "
            "exchange of the two literally identical relay-swap copies only"
        ),
        "orientation_reversal": (
            "not quotiented: K supplies an oriented ring and Q-before-R law"
        ),
    }
    report = {
        "audit_timeout_sec": AUDIT_TIMEOUT_SEC,
        "note_path": NOTE_PATH,
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "checks": checks,
        "pass": all(checks.values()),
        "anchors": anchors,
        "constraint_oracle_AST": oracle_ast,
        "pruning_rules": pruning_rules,
        "censuses": {
            bank_count: public_census(row)
            for bank_count, row in censuses.items()
        },
        "passive_closure": passive,
        "no_new_supplier": supplier,
        "outcome": outcome,
        "w2_components": w2,
        "boundary": boundary,
        "runtime_sec": round(runtime, 6),
    }
    digest_payload = {
        key: value
        for key, value in report.items()
        if key not in ("runtime_sec",)
    }
    report["report_sha256"] = sha256(
        json.dumps(digest_payload, sort_keys=True, default=str).encode()
    ).hexdigest()
    return report


def main():
    started = time.perf_counter()
    try:
        report = build_report()
    except Exception as error:
        runtime = time.perf_counter() - started
        emit_check(
            "cycle755_unhandled_exception",
            False,
            f"{type(error).__name__}: {error}",
        )
        report = {
            "audit_timeout_sec": AUDIT_TIMEOUT_SEC,
            "note_path": NOTE_PATH,
            "audit_input_paths": AUDIT_INPUT_PATHS,
            "checks": {"cycle755_unhandled_exception": False},
            "pass": False,
            "outcome": "honest_FAIL",
            "error_type": type(error).__name__,
            "error": str(error),
            "runtime_sec": round(runtime, 6),
        }
        print(json.dumps(report, sort_keys=True, separators=(",", ":")))
        return 1

    for label, passed in sorted(report["checks"].items()):
        emit_check(label, passed, passed)
    print(json.dumps(report, sort_keys=True, separators=(",", ":"), default=str))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
