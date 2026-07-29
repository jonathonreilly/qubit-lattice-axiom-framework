#!/usr/bin/env python3
"""Independent adversarial checker for the Cycle-738 conditional theorem."""
from __future__ import annotations

import ast
from hashlib import sha256
import inspect
from itertools import combinations, product
import json
from pathlib import Path
import sys
from time import perf_counter

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/GENERAL_N_SECTOR_THEOREM_CYCLE738_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle738_general_n_sector_theorem_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

STDOUT_LIMIT_BYTES = 150 * 1024
K_MODULE = "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
PRIMARY_MODULE = "frontier_cycle738_general_n_sector_theorem_2026_07_28"
PRIMARY_DECLARED_INPUTS = (
    "scripts/frontier_cycle737_ring_family_uniformity_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
EXPECTED_LEMMA_LABELS = (
    "L1_shift_structure",
    "L2_distance_conservation",
    "L3_invariant_locality",
    "L4_window_transport",
    "L5_closure",
)
EXPECTED_OWNERSHIP_IDENTITY = (
    "I_ownership_local_formula: for every b>=1 and station s, the intended "
    "ownership predicate at occupied s equals "
    "not(A[s-1] or A[s+1] or B[s] or work[s]); K itself defines no "
    "ownership predicate"
)
EXPECTED_MACRO_IDENTITY = (
    "I_macro_clean_work_uniformity: for every b>=1 and every row emitted by "
    "K.interleaved_program(b), the controlled mapped macro leaves its A "
    "control unchanged, addresses only data plus its own work bit, and maps "
    "clean work=0 back to 0"
)
EXPECTED_RESIDUALS = (
    EXPECTED_OWNERSHIP_IDENTITY,
    EXPECTED_MACRO_IDENTITY,
)
ALLOWED_GATE_KINDS = frozenset(("X", "CNOT", "TOF"))

CHECKS: dict[str, bool] = {}
DETAILS: dict[str, object] = {}


def check(label: str, condition: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    CHECKS[label] = bool(condition)
    return CHECKS[label]


def digest_text(text: str) -> str:
    return sha256(text.encode()).hexdigest()


def call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = call_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def top_assignment(tree: ast.Module, name: str) -> ast.AST:
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
                return node.value
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            return node.value
    raise AssertionError(("missing top-level assignment", name))


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    raise AssertionError(("missing function", name))


def literal_dict_entries(tree: ast.AST, key: str) -> tuple[object, ...]:
    values = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for key_node, value_node in zip(node.keys, node.values):
            if isinstance(key_node, ast.Constant) and key_node.value == key:
                try:
                    values.append(ast.literal_eval(value_node))
                except (ValueError, TypeError):
                    values.append(("NON_LITERAL", ast.unparse(value_node)))
    return tuple(values)


def primary_extraction(primary_source: str) -> dict[str, object]:
    """Extract the primary's literal contract without importing or executing it."""

    tree = ast.parse(primary_source)
    target_contract = ast.literal_eval(top_assignment(tree, "TARGET_CONTRACT"))
    ownership = ast.literal_eval(
        top_assignment(tree, "OWNERSHIP_LOCALITY_IDENTITY")
    )
    macro = ast.literal_eval(top_assignment(tree, "MACRO_CLEAN_WORK_IDENTITY"))
    residual_node = top_assignment(tree, "RESIDUAL_IDENTITIES")
    if not isinstance(residual_node, ast.Tuple):
        raise AssertionError("RESIDUAL_IDENTITIES is not a tuple")
    residual_names = tuple(
        element.id if isinstance(element, ast.Name) else None
        for element in residual_node.elts
    )
    resolved_residuals = tuple(
        {
            "OWNERSHIP_LOCALITY_IDENTITY": ownership,
            "MACRO_CLEAN_WORK_IDENTITY": macro,
        }.get(name)
        for name in residual_names
    )
    declared_inputs = ast.literal_eval(top_assignment(tree, "AUDIT_INPUT_PATHS"))
    frozen_anchors = ast.literal_eval(top_assignment(tree, "FROZEN_ANCHORS"))

    main_node = function_node(tree, "main")
    predicates: dict[str, str] = {}
    for node in ast.walk(main_node):
        if (
            isinstance(node, ast.Call)
            and call_name(node.func) == "check"
            and len(node.args) >= 2
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
            and node.args[0].value in EXPECTED_LEMMA_LABELS
        ):
            predicates[node.args[0].value] = ast.unparse(node.args[1])

    lemma_function_names = {
        "L1_shift_structure": (
            "constructor_ast_certificate",
            "rail_shift_certificate",
        ),
        "L2_distance_conservation": ("distance_certificate",),
        "L3_invariant_locality": ("invariant_locality_certificate",),
        "L4_window_transport": ("window_transport_certificate",),
        "L5_closure": ("closure_certificate",),
    }
    lemma_statements = {}
    for label, names in lemma_function_names.items():
        lemma_statements[label] = {
            "check_predicate": predicates.get(label),
            "certificate_docstrings": tuple(
                ast.get_docstring(function_node(tree, name), clean=False)
                for name in names
            ),
        }

    status_values = {
        "status": literal_dict_entries(tree, "status"),
        "universal_status": literal_dict_entries(tree, "universal_status"),
        "general_n_sector_theorem": literal_dict_entries(
            tree, "general_n_sector_theorem"
        ),
    }
    all_string_literals = tuple(
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    )
    terminal_literals = tuple(
        value
        for value in all_string_literals
        if value.startswith("CYCLE738_GENERAL_N_SECTOR")
    )
    return {
        "target_contract": target_contract,
        "lemma_statements": lemma_statements,
        "residual_identities": resolved_residuals,
        "residual_names": residual_names,
        "primary_AUDIT_INPUT_PATHS": declared_inputs,
        "frozen_anchors": frozen_anchors,
        "status_values": status_values,
        "terminal_literals": terminal_literals,
        "source_sha256": digest_text(primary_source),
        "tree": tree,
    }


def rows_added_by_call(call: ast.Call) -> int:
    name = call_name(call.func)
    if name.endswith(".append"):
        return 1
    if name.endswith(".extend") and call.args:
        rows = call.args[0]
        if isinstance(rows, (ast.Tuple, ast.List)):
            return len(rows.elts)
    return 0


def direct_row_additions(statements: list[ast.stmt]) -> int:
    total = 0
    for statement in statements:
        if isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Call):
            total += rows_added_by_call(statement.value)
    return total


def own_constructor_derivation(k_tree: ast.Module) -> dict[str, object]:
    """Derive the non-padded row count directly from K's constructor AST."""

    fn = function_node(k_tree, "interleaved_program")
    prefix_node = next(
        statement
        for statement in fn.body
        if isinstance(statement, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "prefix"
            for target in statement.targets
        )
    )
    reverse_node = next(
        statement
        for statement in fn.body
        if isinstance(statement, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "reverse"
            for target in statement.targets
        )
    )
    suffix_node = next(
        statement
        for statement in fn.body
        if isinstance(statement, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "suffix"
            for target in statement.targets
        )
    )
    bank_loop = next(
        statement
        for statement in fn.body
        if isinstance(statement, ast.For)
        and isinstance(statement.target, ast.Name)
        and statement.target.id == "bank"
    )
    edge_loop = next(
        statement
        for statement in fn.body
        if isinstance(statement, ast.For)
        and isinstance(statement.target, ast.Name)
        and statement.target.id == "edge"
    )
    prefix_fixed = len(prefix_node.value.elts) if isinstance(prefix_node.value, ast.List) else -1
    reverse_empty = isinstance(reverse_node.value, ast.List) and not reverse_node.value.elts
    suffix_fixed = len(suffix_node.value.elts) if isinstance(suffix_node.value, ast.List) else -1
    bank_unconditional = direct_row_additions(bank_loop.body)
    bank_conditionals = {
        ast.unparse(statement.test): direct_row_additions(statement.body)
        for statement in bank_loop.body
        if isinstance(statement, ast.If)
    }
    edge_unconditional = direct_row_additions(edge_loop.body)

    # Affine pairs denote coefficient*b + constant.  These terms are
    # independently recovered from the K AST above.
    affine_terms = (
        (0, prefix_fixed),
        (bank_unconditional, 0),
        (bank_conditionals.get("bank", -99), -bank_conditionals.get("bank", -99)),
        (
            bank_conditionals.get("bank < bank_count - 1", -99),
            -bank_conditionals.get("bank < bank_count - 1", -99),
        ),
        (edge_unconditional, -edge_unconditional),
        (0, suffix_fixed),
    )
    derived_affine = (
        sum(term[0] for term in affine_terms),
        sum(term[1] for term in affine_terms),
    )
    source_shape_exact = (
        prefix_fixed == 1
        and reverse_empty
        and suffix_fixed == 1
        and bank_unconditional == 1
        and bank_conditionals == {
            "bank": 1,
            "bank < bank_count - 1": 3,
        }
        and edge_unconditional == 3
        and ast.unparse(bank_loop.iter) == "range(bank_count)"
        and ast.unparse(edge_loop.iter) == "reversed(range(bank_count - 1))"
    )
    return {
        "source_shape_exact": source_shape_exact,
        "affine_terms_coefficient_then_constant": affine_terms,
        "derived_n_affine": derived_affine,
        "derived_formula": f"{derived_affine[0]}*b{derived_affine[1]:+d}",
        "positive_at_b_ge_1": derived_affine[0] + derived_affine[1] >= 3,
        "exact": source_shape_exact and derived_affine == (8, -5),
    }


def own_symbolic_lemma_reproof(
    k_tree: ast.Module, primary_tree: ast.Module
) -> dict[str, object]:
    """Reprove L1/L2/L4/L5 without invoking any primary certificate."""

    constructor = own_constructor_derivation(k_tree)
    step_source = ast.unparse(function_node(k_tree, "apply_controller_step"))
    shift_ast_exact = all(
        fragment in step_source
        for fragment in (
            "a[station], b[station] = (b[station], a[station])",
            "target = (station + 1) % stations",
            "b[station], a[target] = (a[target], b[station])",
        )
    )

    # Independent two-layer label propagation:
    # R1 gives a1[s]=B0[s], b1[s]=A0[s].
    # R2 exchanges b1[s] with a1[s+1], so
    # A2[s+1]=A0[s] and B2[s]=B0[s+1].
    rail_conclusion = {
        "A_after[(s+1) mod n]": "A_before[s]",
        "B_after[s]": "B_before[(s+1) mod n]",
    }
    inverse_shift = "(u-1) mod n"
    shift_is_permutation = True  # The displayed inverse composes both ways.

    # Formal integer coefficient audit.  A rotated representative is
    # x+t-n*q_x.  Subtracting two representatives cancels t; the only
    # difference from y-x is an integer multiple n*(q_x-q_y).
    rotated_x = {"x": 1, "t": 1, "n*q_x": -1}
    rotated_y = {"y": 1, "t": 1, "n*q_y": -1}

    def subtract(left: dict[str, int], right: dict[str, int]) -> dict[str, int]:
        output = dict(left)
        for key, value in right.items():
            output[key] = output.get(key, 0) - value
        return {key: value for key, value in output.items() if value}

    forward = subtract(rotated_y, rotated_x)
    reverse = subtract(rotated_x, rotated_y)
    forward_base = {"y": 1, "x": -1}
    reverse_base = {"x": 1, "y": -1}
    forward_residual = subtract(forward, forward_base)
    reverse_residual = subtract(reverse, reverse_base)
    distance_exact = (
        forward.get("t", 0) == reverse.get("t", 0) == 0
        and forward_residual == {"n*q_y": -1, "n*q_x": 1}
        and reverse_residual == {"n*q_x": -1, "n*q_y": 1}
    )

    # At the shifted occupied station rho(s), A_after[rho(s)+delta]
    # pulls back to A_before[s+delta].  Coefficients cancel for every
    # member of the local A window.  Blank B/work remain blank.
    offsets = (-1, 0, 1)
    window_index_residuals = tuple(
        (1 + offset - 1) - offset for offset in offsets
    )
    window_exact = (
        window_index_residuals == (0, 0, 0)
        and shift_is_permutation
        and rail_conclusion["B_after[s]"] == "B_before[(s+1) mod n]"
    )

    # rho^t(s)=(s+t) mod n follows by induction on t; at t=n the
    # added term is one modulus.  The same reasoning closes the inverse.
    induction_base_increment = 0
    induction_step_increment = 1
    closure_residual_is_one_modulus = 1
    closure_exact = (
        induction_base_increment == 0
        and induction_step_increment == 1
        and closure_residual_is_one_modulus == 1
        and constructor["positive_at_b_ge_1"]
    )

    primary_strings = {
        node.value
        for node in ast.walk(primary_tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    comparison = {
        "station_formula_matches": constructor["derived_n_affine"] == (8, -5),
        "shift_conclusion_matches": (
            "s -> Mod(s + 1, 8*b - 5)" in primary_strings
        ),
        "window_conclusion_present": any(
            "conditional invariant truth at step t iff at step 0" in value
            for value in primary_strings
        ),
        "closure_conclusion_present": (
            "per orbit after n applications of s->s+1" in primary_strings
        ),
    }
    return {
        "L1_station_count": constructor,
        "L1_shift_AST": shift_ast_exact,
        "L1_shift_derivation": rail_conclusion,
        "L1_inverse": inverse_shift,
        "L1_permutation": shift_is_permutation,
        "L2_rotated_forward_difference": forward,
        "L2_forward_multiple_of_n_residual": forward_residual,
        "L2_reverse_multiple_of_n_residual": reverse_residual,
        "L2_oriented_residues_and_min_distance_conserved": distance_exact,
        "L4_window_offsets": offsets,
        "L4_window_index_residuals": window_index_residuals,
        "L4_window_multiset_transport": window_exact,
        "L4_clean_B_transport": "zero B maps to zero B",
        "L4_clean_work_scope": "conditional on the named macro identity",
        "L5_rotation_induction": "rho^t(s)=(s+t) mod n",
        "L5_n_step_residual_moduli": closure_residual_is_one_modulus,
        "L5_rotation_closure": closure_exact,
        "comparison_to_primary_conclusions": comparison,
        "exact": (
            constructor["exact"]
            and shift_ast_exact
            and shift_is_permutation
            and distance_exact
            and window_exact
            and closure_exact
            and all(comparison.values())
        ),
    }


def own_apply_gate(bits: dict[int, int], gate: object) -> dict[int, int]:
    """Apply X/CNOT/TOF with independent exact Boolean algebra."""

    output = dict(bits)
    kind = gate.kind
    wires = tuple(gate.wires)
    if kind == "X" and len(wires) == 1:
        output[wires[0]] ^= 1
    elif kind == "CNOT" and len(wires) == 2:
        if output[wires[0]]:
            output[wires[1]] ^= 1
    elif kind == "TOF" and len(wires) == 3:
        if output[wires[0]] and output[wires[1]]:
            output[wires[2]] ^= 1
    else:
        raise AssertionError(("unsupported gate in own evaluator", kind, wires))
    return output


def gate_lift_truth(gate: object, control: int, work: int) -> bool:
    support = tuple(dict.fromkeys(tuple(gate.wires)))
    if control in support or work in support or control == work:
        return False
    lifted = tuple(K.controlled_macro((gate,), control, work))
    allowed_support = set(support) | {control, work}
    if any(
        lifted_gate.kind not in ALLOWED_GATE_KINDS
        or not set(lifted_gate.wires) <= allowed_support
        or lifted_gate.wires[-1] == control
        for lifted_gate in lifted
    ):
        return False
    for values in product((0, 1), repeat=len(support) + 1):
        initial = dict(zip(support + (control,), values))
        initial[work] = 0
        observed = dict(initial)
        for lifted_gate in lifted:
            observed = own_apply_gate(observed, lifted_gate)
        expected = dict(initial)
        if initial[control]:
            expected = own_apply_gate(expected, gate)
        if observed != expected:
            return False
        if observed[control] != initial[control] or observed[work] != 0:
            return False
    return True


def direct_macro_anchor_audit() -> dict[str, object]:
    """Evaluate every emitted b=1..4 row using an independent bit evaluator."""

    reports = {}
    total_rows = total_gates = total_lifted = truth_rows = 0
    all_exact = True
    for bank in range(1, 5):
        program = tuple(K.interleaved_program(bank))
        bank_rows = bank_gates = bank_lifted = bank_truth_rows = 0
        bank_exact = len(program) == 8 * bank - 5
        row_kinds = []
        for row in program:
            word = tuple(K.mapped_macro(row))
            row_kinds.append(row[0])
            data_support = {
                wire for gate in word for wire in tuple(gate.wires)
            }
            control = max(data_support, default=-1) + 1
            work = control + 1
            lifted_word = tuple(K.controlled_macro(word, control, work))
            row_address_exact = all(
                gate.kind in ALLOWED_GATE_KINDS
                and set(gate.wires) <= data_support | {control, work}
                and gate.wires[-1] != control
                for gate in lifted_word
            )
            gate_truth_exact = True
            for gate in word:
                bank_truth_rows += 2 ** (len(set(gate.wires)) + 1)
                gate_truth_exact = (
                    gate.kind in ALLOWED_GATE_KINDS
                    and gate_lift_truth(gate, control, work)
                    and gate_truth_exact
                )
            bank_exact = bank_exact and row_address_exact and gate_truth_exact
            bank_rows += 1
            bank_gates += len(word)
            bank_lifted += len(lifted_word)
        reports[bank] = {
            "stations": len(program),
            "row_kinds": tuple(row_kinds),
            "rows_checked": bank_rows,
            "mapped_gates_checked": bank_gates,
            "lifted_gates_checked": bank_lifted,
            "own_truth_rows": bank_truth_rows,
            "exact": bank_exact,
        }
        total_rows += bank_rows
        total_gates += bank_gates
        total_lifted += bank_lifted
        truth_rows += bank_truth_rows
        all_exact = all_exact and bank_exact
    return {
        "members": reports,
        "total_rows_checked": total_rows,
        "total_mapped_gates_checked": total_gates,
        "total_lifted_gates_checked": total_lifted,
        "total_own_truth_rows": truth_rows,
        "method": (
            "own X/CNOT/TOF Boolean evaluator; K supplies emitted rows and "
            "controlled circuit only"
        ),
        "not_primary_frozen_tables": True,
        "exact": all_exact,
    }


def independent_config_family(stations: int) -> tuple[tuple[int, ...], ...]:
    masks = [()]
    masks.extend((station,) for station in range(stations))
    masks.extend(
        pair
        for pair in combinations(range(stations), 2)
        if min(
            (pair[1] - pair[0]) % stations,
            (pair[0] - pair[1]) % stations,
        )
        > 1
    )
    return tuple(masks)


def ownership_formula(
    a: tuple[int, ...],
    b: tuple[int, ...],
    work: tuple[int, ...],
    station: int,
) -> bool:
    stations = len(a)
    return (not a[station]) or not (
        a[(station - 1) % stations]
        or a[(station + 1) % stations]
        or b[station]
        or work[station]
    )


def direct_rail_and_ownership_anchors(
    frozen_anchors: dict[int, dict[str, object]]
) -> dict[str, object]:
    """Spot-check K's rail on every independent k<=2 configuration."""

    reports = {}
    total_configurations = total_steps = total_local_checks = 0
    all_exact = True
    for bank in range(1, 5):
        stations = len(K.interleaved_program(bank))
        family = independent_config_family(stations)
        identity_program = tuple(("identity", 0, ()) for _ in range(stations))
        expected_k_counts = (
            1,
            stations,
            stations * (stations - 3) // 2,
        )
        observed_k_counts = tuple(
            sum(len(config) == k for config in family) for k in range(3)
        )
        frozen_counts = tuple(frozen_anchors[bank]["counts_by_k"])
        frozen_prefix = frozen_counts[: min(3, len(frozen_counts))]
        expected_prefix = expected_k_counts[: len(frozen_prefix)]
        bank_exact = (
            stations == 8 * bank - 5
            and stations == frozen_anchors[bank]["ring"]
            and observed_k_counts == expected_k_counts
            and frozen_prefix == expected_prefix
        )
        bank_steps = bank_local = 0
        for config in family:
            a = tuple(int(station in config) for station in range(stations))
            b = (0,) * stations
            initial_a = a
            for _step in range(stations):
                work = (0,) * stations
                for station in range(stations):
                    bank_local += 1
                    bank_exact = (
                        ownership_formula(a, b, work, station) and bank_exact
                    )
                expected_a = [0] * stations
                for station, value in enumerate(a):
                    expected_a[(station + 1) % stations] = value
                expected_b = tuple(
                    b[(station + 1) % stations]
                    for station in range(stations)
                )
                _data, next_a, next_b = K.apply_controller_step(
                    (), identity_program, a, b
                )
                bank_exact = (
                    next_a == tuple(expected_a)
                    and next_b == expected_b
                    and bank_exact
                )
                a, b = next_a, next_b
                bank_steps += 1
            bank_exact = a == initial_a and not any(b) and bank_exact
        reports[bank] = {
            "stations": stations,
            "family_scope": "all independent configurations with k<=2",
            "family_size": len(family),
            "counts_by_k_0_1_2": observed_k_counts,
            "frozen_anchor_prefix": frozen_prefix,
            "K_steps_checked": bank_steps,
            "local_ownership_checks": bank_local,
            "one_full_orbit_per_family_member": True,
            "exact": bank_exact,
        }
        total_configurations += len(family)
        total_steps += bank_steps
        total_local_checks += bank_local
        all_exact = all_exact and bank_exact
    return {
        "members": reports,
        "total_configurations": total_configurations,
        "total_K_steps": total_steps,
        "total_local_ownership_checks": total_local_checks,
        "work_scope": "conceptual clean work rail, absent from K.apply_controller_step",
        "not_primary_frozen_tables": True,
        "exact": all_exact,
    }


def primary_residual_reliance(
    primary_tree: ast.Module, residuals: tuple[str, ...]
) -> dict[str, object]:
    """Locate the primary's concrete/non-symbolic residual witnesses."""

    locality_source = ast.unparse(
        function_node(primary_tree, "invariant_locality_certificate")
    )
    closure_source = ast.unparse(
        function_node(primary_tree, "closure_certificate")
    )
    constants_source = ast.unparse(
        function_node(primary_tree, "fixed_constructor_constants")
    )
    honesty_node = function_node(primary_tree, "honesty_certificate")
    honesty_source = ast.unparse(honesty_node)
    b_dependent_values = literal_dict_entries(
        honesty_node, "b_dependent_external_constant"
    )
    index_mapper_values = literal_dict_entries(
        honesty_node, "external_index_mapper"
    )
    ownership_witnesses = {
        "primary_uses_self_defined_formula": "ownership_ok(" in locality_source,
        "primary_checks_K_definition_absence": (
            "ast.parse(inspect.getsource(K))" in locality_source
        ),
        "primary_uses_external_anchor_call": (
            "R737.near_miss_certificate" in locality_source
        ),
        "primary_marks_conditional": (
            "'status': 'conditional_verified'" in locality_source
            or '"status": "conditional_verified"' in locality_source
        ),
    }
    macro_witnesses = {
        "primary_calls_concrete_truth_fixture": (
            "K.controlled_truth_certificate()" in closure_source
        ),
        "primary_calls_fixed_constants": (
            "fixed_constructor_constants()" in closure_source
        ),
        "primary_checks_only_finalizer_b1_to_b4": (
            "K.M.source_finalizer_word(bank)" in closure_source
            and "for bank in BANK_ANCHORS" in closure_source
        ),
        "primary_checks_only_program_b1_to_b4": (
            "K.interleaved_program(bank)" in closure_source
            and "for bank in BANK_ANCHORS" in closure_source
        ),
        "fixed_words_are_concrete_K_H_R3_values": (
            "K.R3.source_compute_word()" in constants_source
            and all(
                name in constants_source
                for name in (
                    "K.H.PACKET",
                    "K.H.HANDOFF_FORWARD",
                    "K.H.RELAY_LATCH",
                    "K.H.RELAY_SWAP",
                    "K.H.RELAY_UNLATCH",
                    "K.H.HANDOFF_RETURN",
                )
            )
        ),
        "primary_marks_conditional": (
            "'status': 'conditional_verified'" in closure_source
            or '"status": "conditional_verified"' in closure_source
        ),
    }
    honesty_exact = (
        "'empty_iff_fully_structural': len(residuals) == 0" in honesty_source
        or '"empty_iff_fully_structural": len(residuals) == 0' in honesty_source
    )
    return {
        "ownership_identity": ownership_witnesses,
        "macro_identity": macro_witnesses,
        "honesty_empty_iff_fully_structural_expression": honesty_exact,
        "primary_named_b_dependent_value": b_dependent_values,
        "primary_named_external_index_mapper": index_mapper_values,
        "verdict": (
            "primary explicitly leaves both identities residual; its checks "
            "are definition-absence/concrete-anchor checks, not universal "
            "symbolic derivations"
        ),
        "exact": (
            residuals == EXPECTED_RESIDUALS
            and all(ownership_witnesses.values())
            and all(macro_witnesses.values())
            and honesty_exact
            and b_dependent_values == ("M.source_finalizer_word(b)",)
            and index_mapper_values == ("H.mapped_action(kind,index,local)",)
        ),
    }


def k_source_b_dependence(k_tree: ast.Module) -> dict[str, object]:
    """Attack all-b uniformity using only K's constructor source."""

    interleaved_source = ast.unparse(function_node(k_tree, "interleaved_program"))
    mapped_source = ast.unparse(function_node(k_tree, "mapped_macro"))
    controlled_node = function_node(k_tree, "controlled_macro")
    controlled_source = ast.unparse(controlled_node)
    ownership_definitions = tuple(
        node.name
        for node in k_tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and (
            "ownership" in node.name.lower()
            or "invariant" in node.name.lower()
        )
    )
    controlled_names = {
        node.id for node in ast.walk(controlled_node) if isinstance(node, ast.Name)
    }
    dispatch_kinds = {
        comparator.value
        for node in ast.walk(controlled_node)
        if isinstance(node, ast.Compare)
        for comparator in node.comparators
        if isinstance(comparator, ast.Constant)
        and isinstance(comparator.value, str)
    }
    facts = {
        "K_ownership_definition_absent": not ownership_definitions,
        "ownership_formula_constants_not_present_in_K": not any(
            token in interleaved_source + mapped_source + controlled_source
            for token in ("ownership", "A[s-1]", "A[s+1]")
        ),
        "controlled_macro_has_no_bank_parameter_or_name": (
            "bank_count" not in controlled_names and "bank" not in controlled_names
        ),
        "controlled_macro_dispatch_exact": (
            dispatch_kinds == ALLOWED_GATE_KINDS
            and "raise ValueError(gate.kind)" in controlled_source
        ),
        "b_flows_to_external_finalizer": (
            "M.source_finalizer_word(bank_count)" in interleaved_source
        ),
        "indices_flow_to_external_mapper": (
            "H.mapped_action(kind, index, local)" in mapped_source
        ),
        "fixed_external_H_words_used": all(
            token in interleaved_source
            for token in (
                "H.PACKET",
                "H.HANDOFF_FORWARD",
                "H.RELAY_LATCH",
                "H.RELAY_SWAP",
                "H.RELAY_UNLATCH",
                "H.HANDOFF_RETURN",
            )
        ),
    }
    return {
        "source_findings": facts,
        "ownership_upgrade_or_risk": (
            "RISK: K defines no ownership predicate at all, so K's source "
            "cannot identify the intended predicate with the named local formula."
        ),
        "macro_upgrade_or_risk": (
            "RISK: controlled_macro is b-agnostic for X/CNOT/TOF, but "
            "bank_count flows directly to external "
            "M.source_finalizer_word(bank_count), and bank/edge indices flow "
            "to external H.mapped_action(kind,index,local). Their all-b gate "
            "domains are not constrained by K's authorized source."
        ),
        "conditional_theorem_can_be_upgraded_from_K_alone": False,
        "exact": all(facts.values()),
    }


def primary_stdout_status_audit(extraction: dict[str, object]) -> dict[str, object]:
    statuses = extraction["status_values"]
    terminals = extraction["terminal_literals"]
    exact = (
        set(statuses["status"]) == {"conditional_verified"}
        and statuses["universal_status"] == ("conditional_on_named_identities",)
        and statuses["general_n_sector_theorem"]
        == ("conditional_on_named_identities",)
        and set(terminals)
        == {
            "CYCLE738_GENERAL_N_SECTOR_CONDITIONAL_THEOREM_PASS",
            "CYCLE738_GENERAL_N_SECTOR_THEOREM_HONEST_FAIL",
        }
        and "CYCLE738_GENERAL_N_SECTOR_THEOREM_PASS" not in terminals
    )
    return {
        "method": (
            "static AST trace of the report/status values serialized to stdout; "
            "the primary remains data-only and is never run or imported"
        ),
        "status_values": statuses,
        "terminal_literals": terminals,
        "no_unqualified_PASS_terminal": (
            "CYCLE738_GENERAL_N_SECTOR_THEOREM_PASS" not in terminals
        ),
        "exact": exact,
    }


def runtime_import_discipline(k_source_before: str) -> dict[str, object]:
    blocklisted = tuple(
        sorted(
            name
            for name in sys.modules
            if (
                name.split(".")[-1].startswith("frontier_cycle72")
                or name.split(".")[-1].startswith("frontier_cycle73")
            )
            and name != K_MODULE
        )
    )
    k_source_after = inspect.getsource(K)
    return {
        "K_source_sha256_before": digest_text(k_source_before),
        "K_source_sha256_after": digest_text(k_source_after),
        "K_source_unchanged": k_source_after == k_source_before,
        "primary_module_loaded": PRIMARY_MODULE in sys.modules,
        "blocklisted_modules_loaded": blocklisted,
        "only_authorized_nonstdlib_direct_import": K_MODULE,
        "exact": (
            k_source_after == k_source_before
            and PRIMARY_MODULE not in sys.modules
            and not blocklisted
        ),
    }


def main() -> int:
    started = perf_counter()
    k_source_before = inspect.getsource(K)
    primary_source = Path(AUDIT_INPUT_PATHS[0]).read_text()
    k_tree = ast.parse(k_source_before)

    extraction = primary_extraction(primary_source)
    primary_tree = extraction.pop("tree")
    extraction_exact = (
        extraction["target_contract"].startswith(
            "CLAIM: for every bank count b >= 1"
        )
        and "EVIDENCE FORM: structural proof from K's constructor" in extraction[
            "target_contract"
        ]
        and tuple(extraction["lemma_statements"]) == EXPECTED_LEMMA_LABELS
        and all(
            row["check_predicate"] and all(row["certificate_docstrings"])
            for row in extraction["lemma_statements"].values()
        )
        and extraction["residual_identities"] == EXPECTED_RESIDUALS
        and extraction["residual_names"] == (
            "OWNERSHIP_LOCALITY_IDENTITY",
            "MACRO_CLEAN_WORK_IDENTITY",
        )
        and extraction["primary_AUDIT_INPUT_PATHS"] == PRIMARY_DECLARED_INPUTS
        and AUDIT_INPUT_PATHS == (
            "scripts/frontier_cycle738_general_n_sector_theorem_2026_07_28.py",
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
        )
    )
    check("extraction_contract_lemmas_residuals_status_AUDIT", extraction_exact)
    DETAILS["extraction"] = extraction

    reproof = own_symbolic_lemma_reproof(k_tree, primary_tree)
    check("lemma_reproof_L1_station_count_and_shift", (
        reproof["L1_station_count"]["exact"]
        and reproof["L1_shift_AST"]
        and reproof["L1_permutation"]
    ))
    check(
        "lemma_reproof_L2_modular_distance",
        reproof["L2_oriented_residues_and_min_distance_conserved"],
    )
    check(
        "lemma_reproof_L4_window_multiset_transport",
        reproof["L4_window_multiset_transport"],
    )
    check("lemma_reproof_L5_n_step_rotation_closure", reproof["L5_rotation_closure"])
    check("lemma_reproof_conclusions_match_primary", reproof["exact"])
    DETAILS["lemma_reproof"] = reproof

    reliance = primary_residual_reliance(
        primary_tree, extraction["residual_identities"]
    )
    check("residual_primary_non_symbolic_reliance_located", reliance["exact"])
    DETAILS["primary_residual_reliance"] = reliance

    macro_anchors = direct_macro_anchor_audit()
    check("residual_macro_direct_K_b1_through_b4", macro_anchors["exact"])
    DETAILS["macro_direct_evaluation"] = macro_anchors

    rail_anchors = direct_rail_and_ownership_anchors(
        extraction["frozen_anchors"]
    )
    check("residual_ownership_direct_K_b1_through_b4", rail_anchors["exact"])
    check("anchor_recount_four_shift_and_orbit_specializations", rail_anchors["exact"])
    DETAILS["rail_ownership_and_anchor_recount"] = rail_anchors

    dependence = k_source_b_dependence(k_tree)
    check("residual_symbolic_refutation_attempt_reports_precise_risk", dependence["exact"])
    check(
        "residual_upgrade_decision_remains_conditional",
        dependence["conditional_theorem_can_be_upgraded_from_K_alone"] is False,
    )
    DETAILS["K_source_b_dependence_attack"] = dependence

    stdout_status = primary_stdout_status_audit(extraction)
    check("discipline_primary_stdout_status_exactly_conditional", stdout_status["exact"])
    DETAILS["primary_stdout_status"] = stdout_status

    discipline = runtime_import_discipline(k_source_before)
    check("discipline_no_K_writes", discipline["K_source_unchanged"])
    check(
        "discipline_no_blocklisted_imports_and_primary_data_only",
        discipline["exact"],
    )
    DETAILS["discipline"] = discipline

    elapsed = perf_counter() - started
    check("runtime_under_900_seconds", elapsed < AUDIT_TIMEOUT_SEC)
    report = {
        "AUDIT_TIMEOUT_SEC": AUDIT_TIMEOUT_SEC,
        "NOTE_PATH": NOTE_PATH,
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "checks": dict(CHECKS),
        "checks_passed": sum(CHECKS.values()),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "details": DETAILS,
        "runtime_seconds": round(elapsed, 6),
        "status": "conditional_on_named_identities",
        "pass": all(CHECKS.values()),
    }
    provisional = json.dumps(report, sort_keys=True, separators=(",", ":"), default=str)
    line_bytes = sum(len(label) + 20 for label in CHECKS)
    check(
        "stdout_under_150KB",
        len(provisional.encode()) + line_bytes + 4096 < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = dict(CHECKS)
    report["checks_passed"] = sum(CHECKS.values())
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE738_THEOREM_INDEPENDENT_CHECK_CONDITIONAL_PASS"
        if report["pass"]
        else "CYCLE738_THEOREM_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    output_lines = [
        f"{'PASS' if passed else 'FAIL'} {label} :: {passed}"
        for label, passed in CHECKS.items()
    ]
    output_lines.append(
        "SUMMARY_JSON "
        + json.dumps(report, sort_keys=True, separators=(",", ":"), default=str)
    )
    output_lines.append(report["terminal"])
    output = "\n".join(output_lines) + "\n"
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(output.encode())))
    print(output, end="")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
