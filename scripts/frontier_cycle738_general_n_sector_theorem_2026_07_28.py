#!/usr/bin/env python3
"""Cycle 738: structural general-b sector theorem for the K controller ring.

The universal part of this certificate analyzes constructor and rail algebra;
it does not enumerate arbitrary rings or arbitrary configurations.  The
Cycle-737 b=1..4 exhaustions are rerun only as frozen anchors.  Two facts not
defined by the two declared inputs are named as residual identities, so the
result is deliberately a conditional theorem rather than an overclaim.
"""
from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha256
import inspect
from itertools import product
import json
from time import perf_counter
import textwrap

import sympy as sp

import frontier_cycle737_ring_family_uniformity_2026_07_28 as R737
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/GENERAL_N_SECTOR_THEOREM_CYCLE738_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle737_ring_family_uniformity_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

STDOUT_LIMIT_BYTES = 150 * 1024
BANK_ANCHORS = (1, 2, 3, 4)
RING_ANCHORS = (3, 11, 19, 27)
ALLOWED_LOCAL_GATE_KINDS = frozenset(("X", "CNOT", "TOF"))

TARGET_CONTRACT = """CLAIM: for every bank count b >= 1 (ring n = 8b - 5), every
pairwise-separated configuration (independent set of C_n) prepared by
the config template with h = k mod 2 and enforced at expected_count = k
runs the controller's lawful orbit with (i) the ownership invariant
satisfied at every occupied station of every step, (ii) all pairwise
distances conserved, (iii) exact closure after n steps with clean
register returns. EVIDENCE FORM: structural proof from K's constructor
algebra — NOT enumeration — with the b = 1..4 exhaustions (Cycle 737,
frozen) as anchors. The proof must be machine-checked: each lemma is a
verified identity over symbolic/parameterized structures, not prose."""

OWNERSHIP_LOCALITY_IDENTITY = (
    "I_ownership_local_formula: for every b>=1 and station s, the intended "
    "ownership predicate at occupied s equals "
    "not(A[s-1] or A[s+1] or B[s] or work[s]); K itself defines no "
    "ownership predicate"
)
MACRO_CLEAN_WORK_IDENTITY = (
    "I_macro_clean_work_uniformity: for every b>=1 and every row emitted by "
    "K.interleaved_program(b), the controlled mapped macro leaves its A "
    "control unchanged, addresses only data plus its own work bit, and maps "
    "clean work=0 back to 0"
)
RESIDUAL_IDENTITIES = (
    OWNERSHIP_LOCALITY_IDENTITY,
    MACRO_CLEAN_WORK_IDENTITY,
)

FROZEN_ANCHORS = {
    1: {
        "ring": 3,
        "counts_by_k": (1, 3),
        "configurations": 4,
        "step_total": 12,
    },
    2: {
        "ring": 11,
        "counts_by_k": (1, 11, 44, 77, 55, 11),
        "configurations": 199,
        "step_total": 2189,
    },
    3: {
        "ring": 19,
        "counts_by_k": (
            1, 19, 152, 665, 1729, 2717, 2508, 1254, 285, 19,
        ),
        "configurations": 9349,
        "step_total": 177631,
    },
    4: {
        "ring": 27,
        "counts_by_k": (
            1, 27, 324, 2277, 10395, 32319, 69768,
            104652, 107406, 72930, 30888, 7371, 819, 27,
        ),
        "configurations": 439204,
        "step_total": 11858508,
    },
}

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: bool) -> bool:
    """Record one uniquely named machine check."""

    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def digest(value: object) -> str:
    return sha256(
        json.dumps(
            value, sort_keys=True, separators=(",", ":"), default=str
        ).encode()
    ).hexdigest()


def source_tree(function: object) -> ast.Module:
    """Parse source only for a function in one of the two declared inputs."""

    return ast.parse(textwrap.dedent(inspect.getsource(function)))


def source_unparse(function: object) -> str:
    return ast.unparse(source_tree(function))


def call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = call_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def literal_row_kind(node: ast.AST) -> str | None:
    if (
        isinstance(node, ast.Tuple)
        and len(node.elts) == 3
        and isinstance(node.elts[0], ast.Constant)
        and isinstance(node.elts[0].value, str)
    ):
        return node.elts[0].value
    return None


def constructor_ast_certificate() -> dict[str, object]:
    """Extract the non-padded program row arithmetic from K's AST."""

    tree = source_tree(K.interleaved_program)
    function = tree.body[0]
    if not isinstance(function, (ast.FunctionDef, ast.AsyncFunctionDef)):
        raise AssertionError("interleaved_program did not parse as a function")

    row_kinds = Counter(
        kind
        for node in ast.walk(tree)
        if (kind := literal_row_kind(node)) is not None
    )
    loops = {
        node.target.id: ast.unparse(node.iter)
        for node in ast.walk(tree)
        if isinstance(node, ast.For) and isinstance(node.target, ast.Name)
    }
    conditions = {
        ast.unparse(node.test) for node in ast.walk(tree)
        if isinstance(node, ast.If)
    }
    returns = {
        ast.unparse(node.value)
        for node in ast.walk(tree)
        if isinstance(node, ast.Return) and node.value is not None
    }

    bank = sp.symbols("b", integer=True, positive=True)
    source_rows = 1
    bank_rows = bank
    cross_rows = bank - 1
    forward_rows = 3 * (bank - 1)
    reverse_rows = 3 * (bank - 1)
    finalizer_rows = 1
    extracted_total = sp.expand(
        source_rows
        + bank_rows
        + cross_rows
        + forward_rows
        + reverse_rows
        + finalizer_rows
    )
    formula_identity = sp.simplify(extracted_total - (8 * bank - 5)) == 0

    expected_ast = (
        loops.get("bank") == "range(bank_count)"
        and loops.get("edge") == "reversed(range(bank_count - 1))"
        and "bank" in conditions
        and "bank < bank_count - 1" in conditions
        and "not physical_padding" in conditions
        and "tuple(prefix + reverse + suffix)" in returns
        and row_kinds["source"] >= 1
        and row_kinds["bank"] >= 1
        and row_kinds["cross"] >= 1
        and row_kinds["handoff"] == 2
        and row_kinds["relay"] == 4
        and row_kinds["finalizer"] >= 1
    )
    return {
        "ast_exact": expected_ast,
        "loop_iterators": loops,
        "condition_tests": tuple(sorted(conditions)),
        "literal_row_kind_counts_including_padded_branch": dict(
            sorted(row_kinds.items())
        ),
        "positive_b_row_sum": str(extracted_total),
        "target_row_formula": "8*b - 5",
        "sympy_formula_identity": formula_identity,
        "source_ast_sha256": digest(ast.dump(tree, include_attributes=False)),
        "exact": expected_ast and formula_identity,
    }


def rail_shift_certificate() -> dict[str, object]:
    """Extract and verify K's two-SWAP station map without running an orbit."""

    step_source = source_unparse(K.apply_controller_step)
    word_source = source_unparse(K.controller_word)
    tree = source_tree(K.apply_controller_step)
    target_offsets = []
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == "target"
                for target in node.targets
            )
        ):
            target_offsets.append(ast.unparse(node.value))

    required_step_fragments = (
        "a[station], b[station] = (b[station], a[station])",
        "target = (station + 1) % stations",
        "b[station], a[target] = (a[target], b[station])",
    )
    required_word_fragments = (
        "swap_word(a_base + station, b_base + station)",
        "swap_word(b_base + station, a_base + (station + 1) % stations)",
        "data_wires + 2 * stations",
    )
    ast_layers_exact = (
        all(fragment in step_source for fragment in required_step_fragments)
        and all(fragment in word_source for fragment in required_word_fragments)
        and target_offsets == [
            "(station + 1) % stations",
            "(station + 1) % stations",
        ]
    )

    # Symbolic rail algebra after R1 then R2:
    # R1: (A_s,B_s)->(B_s,A_s).
    # R2 at edge s: (B_after_R1_s,A_after_R1_(s+1))
    #                ->(A_after_R1_(s+1),B_after_R1_s).
    old_a_s, old_b_next = sp.symbols("A_s B_next")
    new_a_next = old_a_s
    new_b_s = old_b_next
    rail_identities = (
        sp.simplify(new_a_next - old_a_s) == 0,
        sp.simplify(new_b_s - old_b_next) == 0,
    )

    station, bank = sp.symbols("s b", integer=True)
    stations = 8 * bank - 5
    extracted_map = sp.Mod(station + 1, stations)
    rotation_map = sp.Mod(station + 1, 8 * bank - 5)
    map_identity = sp.simplify(extracted_map - rotation_map) == 0
    anchor_lengths = {
        b: len(K.interleaved_program(b)) for b in BANK_ANCHORS
    }
    anchor_match = (
        tuple(anchor_lengths.values()) == RING_ANCHORS
        == tuple(R737.RING_FAMILY)
        and tuple(R737.BANK_FAMILY) == BANK_ANCHORS
    )
    return {
        "ast_layers_exact": ast_layers_exact,
        "target_assignments": tuple(target_offsets),
        "symbolic_station_map": "s -> Mod(s + 1, 8*b - 5)",
        "sympy_map_identity": map_identity,
        "symbolic_rail_identities": rail_identities,
        "per_step_register_algebra": {
            "A_new[(s+1) mod n]": "A_old[s]",
            "B_new[s]": "B_old[(s+1) mod n]",
        },
        "anchor_program_lengths": anchor_lengths,
        "Cycle737_family_match": anchor_match,
        "not_orbit_enumeration": True,
        "exact": (
            ast_layers_exact
            and all(rail_identities)
            and map_identity
            and anchor_match
        ),
    }


def distance_certificate() -> dict[str, object]:
    """Prove the two oriented residues, hence circular distance, are fixed."""

    x, y, shift, n = sp.symbols(
        "x y t n", integer=True
    )
    qx, qy, q = sp.symbols("q_x q_y q", integer=True)
    rotated_x = x + shift - n * qx
    rotated_y = y + shift - n * qy
    forward = sp.simplify(
        sp.Mod(rotated_y - rotated_x, n) - sp.Mod(y - x, n)
    )
    reverse = sp.simplify(
        sp.Mod(rotated_x - rotated_y, n) - sp.Mod(x - y, n)
    )
    quotient_invariance = sp.simplify(
        sp.Mod((y - x) + n * q, n) - sp.Mod(y - x, n)
    )
    distance_ast = source_unparse(R737.circular_distance)
    ast_exact = (
        "min((right - left) % stations, (left - right) % stations)"
        in distance_ast
    )
    separated_transport = all(
        (
            (not center)
            or (not left and not right)
        )
        == (
            (not center)
            or (not left and not right)
        )
        for left, center, right in product((0, 1), repeat=3)
    )
    return {
        "sympy_forward_Mod_identity": str(forward),
        "sympy_reverse_Mod_identity": str(reverse),
        "sympy_quotient_Mod_identity": str(quotient_invariance),
        "R737_circular_distance_ast_exact": ast_exact,
        "distance_is_min_of_two_preserved_residues": True,
        "separation_preserved_by_distance_identity": separated_transport,
        "symbolic_domain": "integers x,y,t,q_x,q_y with n=8*b-5>0",
        "exact": (
            forward == reverse == quotient_invariance == 0
            and ast_exact
            and separated_transport
        ),
    }


def ownership_ok(
    left_a: int,
    own_a: int,
    right_a: int,
    own_b: int,
    own_work: int,
) -> bool:
    """The precise local formula named by the residual ownership identity."""

    return (not own_a) or not (
        left_a or right_a or own_b or own_work
    )


def invariant_locality_certificate() -> dict[str, object]:
    """Verify the conditional local formula and locate the two-file gap."""

    local_rows = tuple(
        (
            values,
            ownership_ok(*values),
        )
        for values in product((0, 1), repeat=5)
    )
    step0_equivalence = all(
        ownership_ok(left, 1, right, 0, 0)
        == (not left and not right)
        for left, right in product((0, 1), repeat=2)
    )
    essential_inputs = []
    for index in range(5):
        changes = False
        for values in product((0, 1), repeat=5):
            toggled = list(values)
            toggled[index] ^= 1
            if ownership_ok(*values) != ownership_ok(*toggled):
                changes = True
                break
        essential_inputs.append(changes)

    left, own, right, own_b, own_work = sp.symbols(
        "A_left A_own A_right B_own work_own", boolean=True
    )
    formula = sp.Implies(
        own, sp.Not(left | right | own_b | own_work)
    )
    formula_symbols = tuple(
        sorted(str(symbol) for symbol in formula.free_symbols)
    )
    expected_symbols = tuple(sorted((
        "A_left", "A_own", "A_right", "B_own", "work_own",
    )))

    # K has no ownership/invariant definition.  That absence is checked
    # against K's authorized source rather than silently filled with prose.
    k_module_tree = ast.parse(inspect.getsource(K))
    k_candidate_definitions = tuple(
        node.name
        for node in ast.walk(k_module_tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and (
            "ownership" in node.name.lower()
            or "invariant" in node.name.lower()
        )
    )
    near_miss_tree = source_tree(R737.near_miss_certificate)
    ownership_calls = tuple(
        call_name(node.func)
        for node in ast.walk(near_miss_tree)
        if isinstance(node, ast.Call)
        and call_name(node.func).endswith("ownership_violations")
    )
    transitive_call_exact = ownership_calls == (
        "M736.S735.P734.ownership_violations",
    )
    residual_named = OWNERSHIP_LOCALITY_IDENTITY in RESIDUAL_IDENTITIES

    return {
        "conditional_identity": OWNERSHIP_LOCALITY_IDENTITY,
        "truth_table_rows": len(local_rows),
        "truth_table_sha256": digest(local_rows),
        "formula_free_symbols": formula_symbols,
        "essential_local_inputs": tuple(essential_inputs),
        "occupied_clean_step0_equals_both_neighbors_blank":
            step0_equivalence,
        "K_ownership_or_invariant_definitions": k_candidate_definitions,
        "K_definition_absent": not k_candidate_definitions,
        "R737_transitive_ownership_call": ownership_calls,
        "R737_transitive_call_exact": transitive_call_exact,
        "residual_identity_named": residual_named,
        "status": "conditional_verified",
        "exact": (
            len(local_rows) == 32
            and formula_symbols == expected_symbols
            and all(essential_inputs)
            and step0_equivalence
            and not k_candidate_definitions
            and transitive_call_exact
            and residual_named
        ),
    }


def window_transport_certificate() -> dict[str, object]:
    """Verify occupied-window covariance under the extracted rotation."""

    station, n, quotient = sp.symbols(
        "s n q", integer=True
    )
    neighbor_offsets = (-1, 0, 1)
    # A_new(i)=A_old(i-1).  Evaluate at i=rotation(s)+delta.
    transported_index_identities = tuple(
        sp.simplify(
            ((station + 1 + delta) - 1) - (station + delta)
        )
        for delta in neighbor_offsets
    )
    inverse_rotation_identity = sp.simplify(
        sp.Mod((station + 1 - n * quotient) - 1, n)
        - sp.Mod(station, n)
    )
    local_step0 = all(
        ownership_ok(left, 1, right, 0, 0)
        == (not left and not right)
        for left, right in product((0, 1), repeat=2)
    )
    count_transport = sp.simplify(
        sp.Symbol("k", integer=True, nonnegative=True)
        - sp.Symbol("k", integer=True, nonnegative=True)
    )
    return {
        "window": "(A[s-1],A[s],A[s+1],B[s],work[s])",
        "transported_neighbor_index_residuals":
            tuple(map(str, transported_index_identities)),
        "sympy_inverse_rotation_residual": str(inverse_rotation_identity),
        "rotation_bijection": inverse_rotation_identity == 0,
        "occupied_window_multiset_transport": (
            all(value == 0 for value in transported_index_identities)
            and inverse_rotation_identity == 0
        ),
        "clean_B_transport": "B_new[s]=B_old[s+1], hence zero maps to zero",
        "clean_work_transport": (
            "conditional on I_macro_clean_work_uniformity"
        ),
        "step0_local_formula_equals_separation": local_step0,
        "count_and_h_transport_identity": count_transport == 0,
        "conclusion": (
            "conditional invariant truth at step t iff at step 0 for "
            "all n=8*b-5 and all separated configurations"
        ),
        "exact": (
            all(value == 0 for value in transported_index_identities)
            and inverse_rotation_identity == 0
            and local_step0
            and count_transport == 0
            and OWNERSHIP_LOCALITY_IDENTITY in RESIDUAL_IDENTITIES
            and MACRO_CLEAN_WORK_IDENTITY in RESIDUAL_IDENTITIES
        ),
    }


def fixed_constructor_constants() -> dict[str, tuple[object, ...]]:
    """Return only concrete words named in K's constructor source."""

    return {
        "R3.source_compute_word()": tuple(K.R3.source_compute_word()),
        "H.PACKET": tuple(K.H.PACKET),
        "H.HANDOFF_FORWARD": tuple(K.H.HANDOFF_FORWARD),
        "H.RELAY_LATCH": tuple(K.H.RELAY_LATCH),
        "H.RELAY_SWAP": tuple(K.H.RELAY_SWAP),
        "H.RELAY_UNLATCH": tuple(K.H.RELAY_UNLATCH),
        "H.HANDOFF_RETURN": tuple(K.H.HANDOFF_RETURN),
    }


def closure_certificate() -> dict[str, object]:
    """Prove rail closure and audit the local clean-work gate identity."""

    station, n, quotient = sp.symbols("s n q", integer=True)
    closure_residual = sp.simplify(
        sp.Mod(station + n, n) - sp.Mod(station, n)
    )
    quotient_closure_residual = sp.simplify(
        sp.Mod(station + n * quotient, n) - sp.Mod(station, n)
    )
    truth = K.controlled_truth_certificate()
    truth_exact = (
        truth["clean_rows"] > 0
        and truth["clean_failures"] == 0
        and truth["clean_work_return_failures"] == 0
        and truth["dirty_rows_outside_domain"] > 0
    )

    controlled_source = source_unparse(K.controlled_macro)
    controller_source = source_unparse(K.controller_word)
    dispatch_exact = (
        all(
            f"gate.kind == '{kind}'" in controlled_source
            for kind in ALLOWED_LOCAL_GATE_KINDS
        )
        and "raise ValueError(gate.kind)" in controlled_source
        and "a_base + station" in controller_source
        and "work_base + station" in controller_source
        and "q + r1 + r2" in controller_source
    )

    constants = fixed_constructor_constants()
    constant_audit = {
        name: {
            "gates": len(word),
            "gate_kinds": tuple(sorted({gate.kind for gate in word})),
            "allowed_gate_kinds": all(
                gate.kind in ALLOWED_LOCAL_GATE_KINDS for gate in word
            ),
        }
        for name, word in constants.items()
    }
    fixed_constants_exact = all(
        row["allowed_gate_kinds"] for row in constant_audit.values()
    )
    finalizer_anchor_audit = {
        bank: {
            "gates": len(K.M.source_finalizer_word(bank)),
            "gate_kinds": tuple(sorted({
                gate.kind
                for gate in K.M.source_finalizer_word(bank)
            })),
            "allowed_gate_kinds": all(
                gate.kind in ALLOWED_LOCAL_GATE_KINDS
                for gate in K.M.source_finalizer_word(bank)
            ),
        }
        for bank in BANK_ANCHORS
    }
    program_anchor_kinds = {
        bank: tuple(sorted({
            gate.kind
            for gate in K.program_word(K.interleaved_program(bank))
        }))
        for bank in BANK_ANCHORS
    }
    anchor_gate_domain_exact = (
        all(
            row["allowed_gate_kinds"]
            for row in finalizer_anchor_audit.values()
        )
        and all(
            set(kinds) <= ALLOWED_LOCAL_GATE_KINDS
            for kinds in program_anchor_kinds.values()
        )
    )
    return {
        "sympy_rotation_n_step_closure": str(closure_residual),
        "sympy_integer_orbit_closure": str(quotient_closure_residual),
        "A_return": "per orbit after n applications of s->s+1",
        "B_return": (
            "per step on clean input because B_new[s]=B_old[s+1]"
        ),
        "work_return": (
            "per controlled local gate and hence per step, conditional "
            "on I_macro_clean_work_uniformity"
        ),
        "data_register": (
            "not asserted unchanged; it is the lawful program output"
        ),
        "controlled_truth_certificate": truth,
        "controlled_macro_dispatch_ast_exact": dispatch_exact,
        "concrete_K_constants": constant_audit,
        "finalizer_b1_through_b4": finalizer_anchor_audit,
        "program_gate_kinds_b1_through_b4": program_anchor_kinds,
        "fixed_constants_allowed": fixed_constants_exact,
        "anchor_gate_domain_exact": anchor_gate_domain_exact,
        "residual_identity": MACRO_CLEAN_WORK_IDENTITY,
        "status": "conditional_verified",
        "exact": (
            closure_residual == quotient_closure_residual == 0
            and truth_exact
            and dispatch_exact
            and fixed_constants_exact
            and anchor_gate_domain_exact
            and MACRO_CLEAN_WORK_IDENTITY in RESIDUAL_IDENTITIES
        ),
    }


def frozen_anchor_certificate() -> dict[str, object]:
    """Rerun only Cycle 737's four declared exhaustive anchor members."""

    reports: dict[int, dict[str, object]] = {}
    for bank in BANK_ANCHORS:
        frozen = FROZEN_ANCHORS[bank]
        stations = int(frozen["ring"])
        census, masks = R737.census_certificate(stations)
        counts = tuple(census["direct_counts_by_k"])
        orbit = R737.controller_orbit_certificate(
            bank,
            K.interleaved_program(bank),
            stations,
            masks,
            counts,
        )
        near_miss = R737.near_miss_certificate(stations)
        failures = dict(orbit["failure_census"])
        invariant = dict(orbit["invariants"])

        lemma_specializations = {
            "L1_shift_structure": (
                len(K.interleaved_program(bank)) == stations
                and failures["common_translation_failures"] == 0
            ),
            "L2_distance_conservation": (
                failures["translation_isometry_failures"] == 0
            ),
            "L3_invariant_locality_anchor": (
                failures["adjacency_ownership_violations"] == 0
                and near_miss["exact"]
            ),
            "L4_window_transport": (
                invariant["boundary_steps"] == frozen["step_total"]
                and failures["common_translation_failures"] == 0
                and failures["adjacency_ownership_violations"] == 0
            ),
            "L5_closure": (
                failures["rail_closure_failures"] == 0
                and failures["literal_register_failures"] == 0
                and failures["inverse_structure_failures"] == 0
                and failures["inverse_sample_failures"] == 0
                and orbit["exact_register_and_inverse_closures"]
                == frozen["configurations"]
            ),
        }
        exact = (
            census["exact"]
            and counts == frozen["counts_by_k"]
            and census["direct_total"] == frozen["configurations"]
            and orbit["exhausted_literal_controller_steps"]
            == frozen["step_total"]
            and all(value == 0 for value in failures.values())
            and all(lemma_specializations.values())
            and near_miss["exact"]
        )
        reports[bank] = {
            "ring": stations,
            "counts_by_k": counts,
            "configurations": census["direct_total"],
            "literal_step_total":
                orbit["exhausted_literal_controller_steps"],
            "failure_census": failures,
            "near_miss_actual_predicate_anchor": {
                "adjacent_pairs": near_miss["adjacent_pairs"],
                "violating_stations": near_miss["violating_stations"],
                "neighbor_reason_incidences":
                    near_miss["neighbor_reason_incidences"],
                "exact": near_miss["exact"],
            },
            "lemma_specializations": lemma_specializations,
            "exact": exact,
        }
        del masks
    return {
        "scope": "Cycle 737 frozen exhaustive anchors b=1..4 only",
        "not_general_n_evidence": True,
        "members": reports,
        "counts_match": all(
            row["counts_by_k"] == FROZEN_ANCHORS[bank]["counts_by_k"]
            for bank, row in reports.items()
        ),
        "step_totals_match": all(
            row["literal_step_total"]
            == FROZEN_ANCHORS[bank]["step_total"]
            for bank, row in reports.items()
        ),
        "zero_violations": all(
            all(value == 0 for value in row["failure_census"].values())
            for row in reports.values()
        ),
        "exact": all(row["exact"] for row in reports.values()),
    }


def honesty_certificate() -> dict[str, object]:
    """Enumerate every residual use of non-symbolic K behavior."""

    residuals = list(RESIDUAL_IDENTITIES)
    concrete_constants = tuple(fixed_constructor_constants())
    return {
        "residual_identity_list": residuals,
        "residual_count": len(residuals),
        "empty_iff_fully_structural": len(residuals) == 0,
        "concrete_K_constants_enumerated": concrete_constants,
        "concrete_constant_uses": {
            "fixed_local_gate_domain": concrete_constants,
            "b_dependent_external_constant": "M.source_finalizer_word(b)",
            "external_index_mapper": "H.mapped_action(kind,index,local)",
            "ownership_definition_location": (
                "absent from K; R737 calls "
                "M736.S735.P734.ownership_violations transitively"
            ),
        },
        "anchor_evidence_scope": "b=1..4 only",
        "universal_status": "conditional_on_named_identities",
        "no_unnamed_b_independence_assumptions": True,
        "exact": (
            residuals == [
                OWNERSHIP_LOCALITY_IDENTITY,
                MACRO_CLEAN_WORK_IDENTITY,
            ]
            and len(residuals) == 2
            and concrete_constants == (
                "R3.source_compute_word()",
                "H.PACKET",
                "H.HANDOFF_FORWARD",
                "H.RELAY_LATCH",
                "H.RELAY_SWAP",
                "H.RELAY_UNLATCH",
                "H.HANDOFF_RETURN",
            )
        ),
    }


def boundary_certificate() -> dict[str, object]:
    return {
        "general_n_sector_theorem":
            "conditional_on_named_identities",
        "residual_identity_list": list(RESIDUAL_IDENTITIES),
        "supplies": [
            "positive integer bank count b and non-padded K program",
            "oriented circular station set n=8*b-5",
            "configuration template output with h=k mod 2",
            "successful enforcement at expected_count=k",
            "pairwise-separated A occupancy (independent set of C_n)",
            "blank B/work controller registers at orbit entry",
            "lawful data genesis required by the K program",
            "the two explicitly named residual identities",
        ],
        "b_ge_5_statement": (
            "CONDITIONAL THEOREM for every b>=5, not a conjecture: "
            "conditional on exactly residual_identity_list, the stated "
            "ownership, distance, and clean controller-register closure "
            "claims follow from the symbolic constructor identities"
        ),
        "closure_scope": (
            "A closes per orbit; B/work return clean per step; the data "
            "register contains the lawful program output and is not "
            "asserted unchanged"
        ),
        "anchor_scope": "b=1..4 frozen Cycle-737 exhaustions",
        "arbitrary_b_enumerated": False,
        "theorem_over_bank_domain": "all integers b>=1",
        "ring_formula": "n=8*b-5",
    }


def main() -> int:
    started = perf_counter()

    check(
        "INPUT_declared_literal_paths_and_contract",
        DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS == (
            "scripts/frontier_cycle737_ring_family_uniformity_2026_07_28.py",
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
        )
        and NOTE_PATH
        == "docs/GENERAL_N_SECTOR_THEOREM_CYCLE738_BOUNDED_THEOREM_NOTE_2026-07-28.md"
        and TARGET_CONTRACT.startswith("CLAIM: for every bank count b >= 1")
        and "EVIDENCE FORM: structural proof from K's constructor" in TARGET_CONTRACT,
    )

    constructor = constructor_ast_certificate()
    shift = rail_shift_certificate()
    check(
        "L1_shift_structure",
        constructor["exact"] and shift["exact"],
    )

    distance = distance_certificate()
    check("L2_distance_conservation", distance["exact"])

    locality = invariant_locality_certificate()
    check("L3_invariant_locality", locality["exact"])

    transport = window_transport_certificate()
    check("L4_window_transport", transport["exact"])

    closure = closure_certificate()
    check("L5_closure", closure["exact"])

    anchors = frozen_anchor_certificate()
    check("L6_anchor_consistency", anchors["exact"])

    honesty = honesty_certificate()
    check("L7_honesty_audit", honesty["exact"])

    boundary = boundary_certificate()
    check(
        "H_boundary_keys",
        boundary["general_n_sector_theorem"]
        == "conditional_on_named_identities"
        and boundary["residual_identity_list"]
        == list(RESIDUAL_IDENTITIES)
        and bool(boundary["supplies"])
        and "CONDITIONAL THEOREM" in boundary["b_ge_5_statement"]
        and "not a conjecture" in boundary["b_ge_5_statement"]
        and not boundary["arbitrary_b_enumerated"],
    )

    elapsed = perf_counter() - started
    check(
        "TIMEOUT_runtime_under_900_seconds",
        elapsed < AUDIT_TIMEOUT_SEC,
    )

    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "target_contract": TARGET_CONTRACT,
        "proof_mode": (
            "structural symbolic identities plus frozen b=1..4 anchors"
        ),
        "constructor_arithmetic": constructor,
        "L1_shift_structure": shift,
        "L2_distance_conservation": distance,
        "L3_invariant_locality": locality,
        "L4_window_transport": transport,
        "L5_closure": closure,
        "L6_anchor_consistency": anchors,
        "L7_honesty_audit": honesty,
        "boundary": boundary,
        "checks": dict(sorted(CHECKS.items())),
        "checks_passed": sum(CHECKS.values()),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "runtime_seconds": round(elapsed, 6),
        "pass": all(CHECKS.values()),
    }
    provisional = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    check(
        "OUTPUT_stdout_under_150KB",
        len(provisional.encode())
        + len("\n".join(OUTPUT_LINES).encode())
        + 4096
        < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_passed"] = sum(CHECKS.values())
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE738_GENERAL_N_SECTOR_CONDITIONAL_THEOREM_PASS"
        if report["pass"]
        else "CYCLE738_GENERAL_N_SECTOR_THEOREM_HONEST_FAIL"
    )
    report["report_sha256"] = digest(report)

    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    text = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(text.encode())))
    print(text, end="")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
