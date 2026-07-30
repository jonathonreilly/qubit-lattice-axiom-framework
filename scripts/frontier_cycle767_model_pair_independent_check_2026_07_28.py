#!/usr/bin/env python3
"""Cycle 767 independent retained-scope model-pair checker.

The Cycle 767 primary is parsed as inert source data and is import-blocked.
All dynamic certificates are rebuilt from the three declared landed inputs.
In particular, the checker attacks the claimed off-tie invisibility on every
held single-source fixture and every lawful ring-11 k=1 configuration.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/MODEL_PAIR_NONENTAILMENT_CYCLE767_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
BLOCKLIST = (
    "scripts/frontier_cycle767_model_pair_nonentailment_2026_07_28.py",
)
AUDIT_BLOCKLIST = BLOCKLIST

import ast
from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
PRIMARY_MODULE = Path(BLOCKLIST[0]).stem


class _PrimaryImportBlocker:
    """Make an accidental import of the primary a hard checker failure."""

    def find_spec(self, fullname, path=None, target=None):
        if fullname == PRIMARY_MODULE or fullname.startswith(
            PRIMARY_MODULE + "."
        ):
            raise ImportError(
                f"Cycle 767 primary is read-as-data only: {fullname}"
            )
        return None


if PRIMARY_MODULE in sys.modules:
    raise AssertionError(("primary already imported", PRIMARY_MODULE))
_PRIMARY_BLOCKER = _PrimaryImportBlocker()
sys.meta_path.insert(0, _PRIMARY_BLOCKER)

import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
STDOUT_LIMIT_BYTES = 150 * 1024
EXPECTED_FROZEN_K3_TIE = (
    (0, 2, 4),
    (0, 2, 9),
    (0, 7, 9),
)
EXPECTED_THEOREM_STATEMENT = (
    "The retained surface does not entail the realized alternative at the "
    "tie — leg 2 of the axiom-update criterion at RETAINED scope."
)
EXPECTED_SCOPE_STATEMENT = (
    "This is retained-surface non-entailment, not merely bare-axiom "
    "non-entailment. Bare-axiom non-entailment is weaker/easier and follows "
    "a fortiori from this pair only if the retained surface is axiom-derived "
    "so that the required model transfer is valid."
)
EXPECTED_LEG1_STUB = (
    "The tie configurations are lawful, but nothing in the retained "
    "certificates yet shows that nature realizes a multi-source resolution "
    "fact uniquely. Physical requirement for such a fact is therefore not "
    "established."
)
EXPECTED_LEG3_STUB = (
    "Any sentence fixing a tie-breaking convention kills this model pair. "
    "The open issue is justification of one such sentence; the retained "
    "surface currently distinguishes none."
)
EXPECTED_TERMINAL_SCOPE = (
    "Leg 2 alone does not trigger an axiom update: leg 1 is not demonstrated "
    "and leg 3 has no distinguished candidate."
)

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def check(label: str, condition: bool, detail: object = "") -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )
    return passed


def _module_assignments(tree: ast.Module) -> dict[str, ast.expr]:
    result: dict[str, ast.expr] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    result[target.id] = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(
            node.target, ast.Name
        ):
            result[node.target.id] = node.value
    return result


def _functions(tree: ast.Module) -> dict[str, ast.FunctionDef]:
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }


def _dict_map(node: ast.expr) -> dict[str, ast.expr]:
    if not isinstance(node, ast.Dict):
        raise AssertionError(("expected literal dict AST", ast.dump(node)))
    result = {}
    for key, value in zip(node.keys, node.values):
        if not (
            isinstance(key, ast.Constant) and isinstance(key.value, str)
        ):
            raise AssertionError(("nonliteral dict key", ast.dump(key)))
        result[key.value] = value
    return result


def _assigned_literal_dict_keys(
    function: ast.FunctionDef, variable: str
) -> tuple[str, ...]:
    for node in ast.walk(function):
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == variable
                for target in node.targets
            )
            and isinstance(node.value, ast.Dict)
        ):
            return tuple(_dict_map(node.value))
    raise AssertionError(("literal dict assignment not found", function.name))


def _update_literal_dict_keys(
    function: ast.FunctionDef, variable: str
) -> tuple[str, ...]:
    for node in ast.walk(function):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "update"
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == variable
            and len(node.args) == 1
            and isinstance(node.args[0], ast.Dict)
        ):
            return tuple(_dict_map(node.args[0]))
    raise AssertionError(("literal dict update not found", function.name))


def extraction() -> tuple[bool, dict[str, object]]:
    """Parse the blocked primary and extract its complete literal contract."""

    if PRIMARY_MODULE in sys.modules:
        raise AssertionError(("primary import leakage", PRIMARY_MODULE))
    primary_path = ROOT / BLOCKLIST[0]
    source = primary_path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(primary_path))
    assignments = _module_assignments(tree)
    functions = _functions(tree)

    audit_node = assignments["AUDIT_INPUT_PATHS"]
    audit_is_pure_literal = (
        isinstance(audit_node, ast.Tuple)
        and len(audit_node.elts) == 3
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_node.elts
        )
    )
    primary_audit_paths = tuple(ast.literal_eval(audit_node))
    primary_tie = tuple(
        tuple(row)
        for row in ast.literal_eval(assignments["FROZEN_K3_TIE"])
    )
    theorem_statement = ast.literal_eval(
        assignments["THEOREM_STATEMENT"]
    )

    imported = {}
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported[alias.asname or alias.name] = alias.name

    convention_calls = []
    main_node = functions["main"]
    for node in ast.walk(main_node):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "freeze_model"
            and len(node.args) >= 2
        ):
            convention_calls.append(
                (
                    ast.literal_eval(node.args[0]),
                    ast.literal_eval(node.args[1]),
                )
            )
    convention_calls = sorted(convention_calls)

    complete_node = functions["complete_selection"]
    complete_calls = {
        (
            node.func.id
            if isinstance(node.func, ast.Name)
            else node.func.attr
            if isinstance(node.func, ast.Attribute)
            else ""
        )
        for node in ast.walk(complete_node)
        if isinstance(node, ast.Call)
    }
    convention_literals = {
        node.value
        for node in ast.walk(complete_node)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
    }

    battery_function_names = (
        "retained_k_battery",
        "retained_m736_battery",
        "single_source_agreement_certificate",
        "frozen_tie_certificate",
    )
    shared_keys = tuple(
        key
        for name in battery_function_names
        for key in _assigned_literal_dict_keys(functions[name], "battery")
    )
    completion_keys = _update_literal_dict_keys(
        functions["freeze_model"], "battery"
    )
    model_battery_keys = shared_keys + completion_keys
    history_keys = _assigned_literal_dict_keys(
        functions["freeze_model"], "history"
    )

    freeze_literals = {
        node.value
        for node in ast.walk(functions["freeze_model"])
        if isinstance(node, ast.Constant)
    }
    agreement_literals = {
        node.value
        for node in ast.walk(
            functions["single_source_agreement_certificate"]
        )
        if isinstance(node, ast.Constant)
        and isinstance(node.value, int)
        and not isinstance(node.value, bool)
    }

    theorem_return = next(
        node.value
        for node in functions["theorem_note_certificate"].body
        if isinstance(node, ast.Return)
    )
    theorem_map = _dict_map(theorem_return)
    scope_map = _dict_map(theorem_map["scope_chain"])
    leg1_map = _dict_map(theorem_map["leg_1_REQUIREMENT"])
    leg2_map = _dict_map(theorem_map["leg_2_NONENTAILMENT"])
    leg3_map = _dict_map(theorem_map["leg_3_CLEAR"])
    extracted_scope = {
        "scope_statement": ast.literal_eval(scope_map["statement"]),
        "proved_scope": ast.literal_eval(scope_map["proved_scope"]),
        "not_claimed_scope": ast.literal_eval(
            scope_map["not_claimed_scope"]
        ),
        "model_transfer_proved": ast.literal_eval(
            scope_map[
                "full_axiom_derivation_or_model_transfer_proved_here"
            ]
        ),
        "leg1_status": ast.literal_eval(leg1_map["status"]),
        "leg1_stub": ast.literal_eval(leg1_map["argument_not_proof"]),
        "leg2_status": ast.literal_eval(leg2_map["status"]),
        "leg3_status": ast.literal_eval(leg3_map["status"]),
        "leg3_stub": ast.literal_eval(leg3_map["argument_not_proof"]),
        "axiom_update_triggered": ast.literal_eval(
            theorem_map["axiom_update_triggered"]
        ),
        "terminal_statement": ast.literal_eval(
            theorem_map["terminal_statement"]
        ),
    }

    history_blueprints = (
        {
            "model": "MODEL A",
            "convention": "alpha",
            "realized_alternative": min(primary_tie),
            "history_fields": history_keys
            + ("realized_history_sha256",),
        },
        {
            "model": "MODEL B",
            "convention": "beta",
            "realized_alternative": max(primary_tie),
            "history_fields": history_keys
            + ("realized_history_sha256",),
        },
    )
    passed = (
        audit_is_pure_literal
        and primary_audit_paths == AUDIT_INPUT_PATHS
        and isinstance(assignments["DECLARED_INPUT_PATHS"], ast.Name)
        and assignments["DECLARED_INPUT_PATHS"].id
        == "AUDIT_INPUT_PATHS"
        and ast.literal_eval(assignments["AUDIT_TIMEOUT_SEC"]) == 1800
        and ast.literal_eval(assignments["NOTE_PATH"]) == NOTE_PATH
        and primary_tie == EXPECTED_FROZEN_K3_TIE
        and theorem_statement == EXPECTED_THEOREM_STATEMENT
        and {
            "F750":
                "frontier_cycle750_actual_selector_stretch_2026_07_28",
            "M736":
                "frontier_cycle736_pairwise_separated_multisource_2026_07_28",
            "K":
                "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        }.items()
        <= imported.items()
        and convention_calls
        == [("MODEL A", "alpha"), ("MODEL B", "beta")]
        and {"min", "max"} <= complete_calls
        and {"alpha", "beta"} <= convention_literals
        and len(shared_keys) == 22
        and len(completion_keys) == 7
        and len(model_battery_keys) == 29
        and len(set(model_battery_keys)) == 29
        and 38 in agreement_literals
        and "alpha" in freeze_literals
        and history_blueprints[0]["realized_alternative"]
        == (0, 2, 4)
        and history_blueprints[1]["realized_alternative"]
        == (0, 7, 9)
        and extracted_scope["scope_statement"]
        == EXPECTED_SCOPE_STATEMENT
        and extracted_scope["leg1_stub"] == EXPECTED_LEG1_STUB
        and extracted_scope["leg3_stub"] == EXPECTED_LEG3_STUB
        and extracted_scope["terminal_statement"]
        == EXPECTED_TERMINAL_SCOPE
        and PRIMARY_MODULE not in sys.modules
    )
    return passed, {
        "audit_literal_eval": audit_is_pure_literal,
        "primary_sha256": sha256(source.encode("utf-8")).hexdigest(),
        "primary_imported": PRIMARY_MODULE in sys.modules,
        "conventions": convention_calls,
        "shared_battery_checks": len(shared_keys),
        "completion_checks": len(completion_keys),
        "model_battery_checks": len(model_battery_keys),
        "model_battery_keys": model_battery_keys,
        "single_source_fixture_count": 38,
        "frozen_tie": primary_tie,
        "frozen_history_blueprints": history_blueprints,
        "history_fields": history_keys
        + ("realized_history_sha256",),
        "theorem_statement": theorem_statement,
        "scope": extracted_scope,
    }


def independent_complete_selection(
    survivors: tuple[object, ...], convention: str
) -> object | None:
    """The independently implemented completion shared by both models."""

    if len(survivors) == 0:
        return None
    if len(survivors) == 1:
        return survivors[0]
    ordering = sorted(survivors)
    if convention == "alpha":
        return ordering[0]
    if convention == "beta":
        return ordering[-1]
    raise ValueError(("unknown convention", convention))


def independent_clean_postimage(after: int, bank_count: int) -> bool:
    banks, links = K.M.unpack_state(after, bank_count)
    controller_dirty = any(
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
    )
    return (
        not after[K.R3.X.SOURCE_POINTER]
        and not controller_dirty
        and not any(any(link) for link in links)
    )


def independent_enforcement_selector(
    program: tuple[object, ...],
    before: int,
    expected: int,
    bank_count: int,
    alternatives: tuple[int, ...],
) -> tuple[int, ...]:
    """Rebuild the F750 selector without calling its selector implementation."""

    survivors = []
    for position in alternatives:
        expected_a = tuple(
            int(station == position)
            for station in range(len(program))
        )
        expected_b = (0,) * len(program)
        after, rail_a, rail_b, _trace = K.run_orbit(
            before, program, token_positions=(position,)
        )
        if (
            after != expected
            or rail_a != expected_a
            or rail_b != expected_b
        ):
            continue
        restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
            after, program, token_positions=(position,), reverse=True
        )
        if (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
            and independent_clean_postimage(after, bank_count)
        ):
            survivors.append(position)
    return tuple(survivors)


def retained_k_battery() -> tuple[dict[str, bool], dict[str, object]]:
    held = {size: K.held_certificate(size) for size in (2, 5, 12)}
    controls = K.order_and_domain_controls()
    battery = {
        "K_held_orbit_sizes_2_5_12": all(
            row["events"] == 2 * size
            and row["fixed_word_failures"] == 0
            for size, row in held.items()
        ),
        "K_literal_inverse_sizes_2_5_12": all(
            row["inverse_failures"] == 0 for row in held.values()
        ),
        "K_token_return_sizes_2_5_12": all(
            row["token_return_failures"] == 0 for row in held.values()
        ),
        "K_decoded_chain_sizes_2_5_12": all(
            row["logical_failures"] == 0 for row in held.values()
        ),
        "K_clean_postimage_sizes_2_5_12": all(
            row["postimage_failures"] == 0 for row in held.values()
        ),
        "K_Q_before_R_order_control": controls["R_before_Q_changed"],
    }
    return battery, {
        "sizes": tuple(held),
        "events": {str(size): row["events"] for size, row in held.items()},
        "failure_vectors": {
            str(size): {
                key: row[key]
                for key in (
                    "logical_failures",
                    "fixed_word_failures",
                    "inverse_failures",
                    "postimage_failures",
                    "token_return_failures",
                )
            }
            for size, row in held.items()
        },
        "R_before_Q_changed": controls["R_before_Q_changed"],
    }


def retained_m736_battery() -> tuple[
    dict[str, bool],
    dict[str, object],
    tuple[tuple[int, ...], ...],
]:
    program = K.interleaved_program(M736.FIXTURE_BANKS)
    _word, layout, _blocks, _metadata = (
        M736.C731.count_certified_controller_build(
            program, M736.C731.DATA_WIDTH, 0
        )
    )
    anchor = M736.cycle735_regression_anchor(layout)
    census = M736.configuration_census()
    configurations = tuple(census["configurations"])
    template = M736.template_and_covariance_certificate(
        layout, configurations
    )
    count_enforcement = M736.count_k_enforcement_certificate(
        configurations
    )
    orbit = M736.invariant_full_orbit_certificate(configurations)
    adjacency = M736.adjacency_near_miss_controls()
    deletions = M736.multisource_deletion_controls(
        layout, configurations
    )
    battery = {
        "M736_A_Cycle735_regression_anchor":
            anchor["regression_pass"],
        "M736_B_full_199_configuration_census": (
            census["agreement"]
            and census["direct_counts_by_k"]
            == M736.EXPECTED_COUNTS_BY_K
            and census["direct_total"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and census["closed_form_total"]
            == census["lucas_recurrence_total_L11"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and census["maximum_token_count"] == M736.MAX_TOKEN_COUNT
        ),
        "M736_C_template_exactness_and_covariance": (
            template["all_exact"]
            and template["template_cases"]
            == template["expected_template_cases"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and template["covariance_identities"]
            == template["expected_covariance_identities"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            * M736.RING_STATIONS
            and template["AST_no_distinguished_site"]["audit_pass"]
        ),
        "M736_D_count_k_enforcement": (
            count_enforcement["exact"]
            and count_enforcement["acceptance_diagonal"]
            == count_enforcement["expected_acceptance_diagonal"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and count_enforcement["cross_refusal_off_diagonal"]
            == count_enforcement["expected_cross_refusal_off_diagonal"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            * M736.MAX_TOKEN_COUNT
            and count_enforcement["h1_odd_sector_exercised"]
            and count_enforcement["parity_charge_failures"] == 0
        ),
        "M736_E_invariant_full_orbit_all_199": (
            orbit["pairwise_separated_sector_lawful"]
            and orbit["k_source_composition_ring11"]
            and orbit["outcome"]
            == "all_199_pairwise_separated_configurations_lawful"
            and orbit["orbit_configurations"]
            == orbit["expected_orbit_configurations"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and orbit["exact_register_and_inverse_closures"]
            == orbit["expected_exact_closures"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and all(
                value == 0 for value in orbit["failure_census"].values()
            )
            and orbit["frozen_obstruction"] is None
        ),
        "M736_F_adjacency_near_miss_controls": (
            adjacency["exact"]
            and adjacency["wall_name"]
            == "ownership_uniqueness_at_adjacent_Q_sites"
            and adjacency["violating_stations"]
            == adjacency["expected_violating_stations"]
        ),
        "M736_G_multisource_deletion_controls": (
            deletions["every_deletion_detected"]
            and deletions["output_change_detections"]
            == deletions["law_refusals"]
            == deletions["deletion_cases"]
            and deletions["count_refusals"]
            == deletions["expected_count_refusals"]
            == deletions["A_gate_deletions"]
        ),
        "M736_H_honest_sector_boundary": (
            orbit["pairwise_separated_sector_lawful"]
            and M736.MAX_TOKEN_COUNT == 5
            and count_enforcement["h1_odd_sector_exercised"]
            and orbit["k_source_composition_ring11"]
            and "no position-independent allocator-power claim"
            in orbit["composition_definition"]
        ),
    }
    return battery, {
        "configuration_count": len(configurations),
        "counts_by_k": census["direct_counts_by_k"],
        "configuration_table_sha256":
            census["configuration_mask_table_sha256"],
        "template_table_sha256": template["template_table_sha256"],
        "orbit_table_sha256": orbit["orbit_table_sha256"],
        "failure_census": orbit["failure_census"],
    }, configurations


def single_source_battery() -> tuple[
    dict[str, bool], dict[str, object], tuple[dict[str, object], ...]
]:
    prior_pass, prior_fail = F750.PASS, F750.FAIL
    F750.PASS = F750.FAIL = 0
    captured = StringIO()
    try:
        with redirect_stdout(captured):
            landed = F750.enforcement_candidate_census()
        landed_fail = F750.FAIL
    finally:
        F750.PASS, F750.FAIL = prior_pass, prior_fail

    rows = []
    all_agree = True
    alternatives_exhausted = 0
    for bank_count in (2, 5, 12):
        for event, direction, program, before, expected in (
            F750.k_epoch_fixtures(bank_count)
        ):
            alternatives = tuple(range(len(program)))
            selected = independent_enforcement_selector(
                program,
                before,
                expected,
                bank_count,
                alternatives,
            )
            alpha = independent_complete_selection(selected, "alpha")
            beta = independent_complete_selection(selected, "beta")
            agrees = selected == (0,) and alpha == beta == 0
            all_agree &= agrees
            alternatives_exhausted += len(alternatives)
            rows.append(
                {
                    "bank_count": bank_count,
                    "event": event,
                    "direction": direction,
                    "program": program,
                    "before": before,
                    "expected": expected,
                    "selected": selected,
                    "alpha": alpha,
                    "beta": beta,
                    "agrees": agrees,
                }
            )
    battery = {
        "F750_unmodified_single_source_census": (
            landed_fail == 0
            and landed["fixtures_exhausted"] == 38
            and landed["alternatives_exhausted"] == 2578
            and landed["selected_count_range"] == [1, 1]
            and landed["tests"]
            == {
                "totality": True,
                "invariance": True,
                "identification": True,
            }
        ),
        "F750_both_models_agree_on_all_unique_fixtures": (
            all_agree
            and len(rows) == 38
            and alternatives_exhausted == 2578
        ),
        "tie_conventions_invisible_off_tie": all_agree,
    }
    digest_rows = tuple(
        (
            row["bank_count"],
            row["event"],
            row["direction"],
            len(row["program"]),
            row["selected"],
            row["alpha"],
            row["beta"],
            row["agrees"],
        )
        for row in rows
    )
    return battery, {
        "fixtures": len(rows),
        "alternatives_exhausted": alternatives_exhausted,
        "agreements": sum(row["agrees"] for row in rows),
        "disagreements": sum(
            row["alpha"] != row["beta"] for row in rows
        ),
        "fixture_table_sha256": digest(digest_rows),
        "captured_F750_stdout_bytes":
            len(captured.getvalue().encode("utf-8")),
    }, tuple(rows)


def independent_rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted(
            (position + shift) % RING_STATIONS
            for position in positions
        )
    )


def independent_synchronous_word(
    program: tuple[object, ...],
    token_positions: tuple[int, ...],
) -> tuple[object, ...]:
    live = tuple(token_positions)
    gates = []
    for _step in range(len(program)):
        occupied = set(live)
        for station, row in enumerate(program):
            if station in occupied:
                gates.extend(K.mapped_macro(row))
        live = tuple(
            (position + 1) % len(program) for position in live
        )
    return tuple(gates)


def frozen_tie_battery(
    configurations: tuple[tuple[int, ...], ...]
) -> tuple[
    dict[str, bool],
    dict[str, object],
    dict[tuple[int, ...], dict[str, object]],
]:
    event, direction, program, before, _expected_single = (
        F750.k_epoch_fixtures(FIXTURE_BANKS)[0]
    )
    family = tuple(
        sorted(
            {
                independent_rotate_positions((0, 2, 4), shift)
                for shift in range(RING_STATIONS)
            }
        )
    )
    census_positions = {
        M736.occupied_sites(configuration)
        for configuration in configurations
    }
    evaluations = {}
    selected = []
    digest_rows = []
    for positions in family:
        tokens = tuple(
            int(station in positions)
            for station in range(len(program))
        )
        zeros = (0,) * len(program)
        word = independent_synchronous_word(program, positions)
        expected = K.A.apply_semantic(before, word)
        after, rail_a, rail_b, trace = K.run_orbit(
            before, program, token_positions=positions
        )
        restored, inverse_a, inverse_b, inverse_trace = K.run_orbit(
            after, program, token_positions=positions, reverse=True
        )
        conditions = {
            "M736_pairwise_separated":
                M736.is_pairwise_separated(
                    tuple(
                        int(site in positions)
                        for site in range(RING_STATIONS)
                    )
                ),
            "M736_full_census_membership":
                positions in census_positions,
            "M736_synchronous_composition": after == expected,
            "K_token_rail_return":
                rail_a == tokens and rail_b == zeros,
            "K_literal_inverse": (
                restored == before
                and inverse_a == rail_a
                and inverse_b == rail_b
            ),
            "K_clean_postimage":
                independent_clean_postimage(after, FIXTURE_BANKS),
        }
        survivor = all(conditions.values())
        if survivor:
            selected.append(positions)
        evaluation = {
            "positions": positions,
            "conditions": conditions,
            "survivor": survivor,
            "composition_word_sha256": K.gate_digest(word),
            "before_state_sha256": digest(before),
            "after_state_sha256": digest(after),
            "expected_state_sha256": digest(expected),
            "restored_state_sha256": digest(restored),
            "trace": trace,
            "inverse_trace": inverse_trace,
            "trace_sha256": digest(trace),
            "inverse_trace_sha256": digest(inverse_trace),
            "after": after,
            "expected": expected,
            "restored": restored,
            "rail_a": rail_a,
            "rail_b": rail_b,
            "inverse_a": inverse_a,
            "inverse_b": inverse_b,
        }
        evaluations[positions] = evaluation
        digest_rows.append(
            (
                positions,
                tuple(sorted(conditions.items())),
                evaluation["composition_word_sha256"],
                evaluation["after_state_sha256"],
                evaluation["trace_sha256"],
            )
        )
    selected_tuple = tuple(selected)
    battery = {
        "reconstructed_translation_family_has_11_members":
            len(family) == RING_STATIONS,
        "all_family_members_in_M736_lawful_census":
            all(position in census_positions for position in family),
        "frozen_event_is_two_bank_event_0_direction_10": (
            event == 0 and direction == (1, 0)
        ),
        "frozen_survivor_set_exact":
            selected_tuple == EXPECTED_FROZEN_K3_TIE,
        "all_three_tied_alternatives_retained_admissible": all(
            evaluations[position]["survivor"]
            for position in EXPECTED_FROZEN_K3_TIE
        ),
    }
    return battery, {
        "event": event,
        "direction": direction,
        "family_size": len(family),
        "selected": selected_tuple,
        "selected_count": len(selected_tuple),
        "family_evaluation_table_sha256": digest(digest_rows),
    }, evaluations


def independent_record_construction(
    realized: tuple[int, ...], trace_length: int
) -> tuple[dict[str, bool], dict[str, object]]:
    records = tuple(
        {
            "record_id": f"site-{site}",
            "site": site,
            "lineage": (
                "realized_token_lineage"
                if site in realized
                else "realized_vacuum_lineage"
            ),
            "permanent": True,
            "locked_possibility_admissible": True,
        }
        for site in range(RING_STATIONS)
    )
    snapshots = tuple(records for _ in range(trace_length + 1))
    facts = {
        "one_record_per_site": (
            len(records) == RING_STATIONS
            and tuple(record["site"] for record in records)
            == tuple(range(RING_STATIONS))
            and len({record["record_id"] for record in records})
            == RING_STATIONS
        ),
        "records_permanent": (
            all(record["permanent"] for record in records)
            and all(snapshot == records for snapshot in snapshots)
        ),
        "locked_possibility_admissible": (
            all(
                record["locked_possibility_admissible"]
                for record in records
            )
            and all(
                records[site]["lineage"]
                == "realized_token_lineage"
                for site in realized
            )
        ),
    }
    return facts, {
        "site_count": RING_STATIONS,
        "record_count": len(records),
        "boundary_snapshots": len(snapshots),
        "records": records,
        "snapshots": snapshots,
        "record_ledger_sha256": digest(records),
        "permanence_snapshots_sha256": digest(snapshots),
    }


def independent_history(
    model_name: str,
    convention: str,
    evaluation: dict[str, object],
) -> tuple[dict[str, object], dict[str, bool], dict[str, object]]:
    realized = independent_complete_selection(
        EXPECTED_FROZEN_K3_TIE, convention
    )
    if not isinstance(realized, tuple):
        raise AssertionError(("non-tuple tie realization", realized))
    facts, record_detail = independent_record_construction(
        realized, len(evaluation["trace"])
    )
    history = {
        "model": model_name,
        "completion": (
            "lexicographic-least among tied alternatives"
            if convention == "alpha"
            else "lexicographic-greatest among tied alternatives"
        ),
        "convention": convention,
        "realized_alternative": realized,
        "event": 0,
        "direction": (1, 0),
        "before_state_sha256": evaluation["before_state_sha256"],
        "composition_word_sha256":
            evaluation["composition_word_sha256"],
        "after_state_sha256": evaluation["after_state_sha256"],
        "expected_state_sha256":
            evaluation["expected_state_sha256"],
        "restored_state_sha256":
            evaluation["restored_state_sha256"],
        "orbit_trace": evaluation["trace"],
        "inverse_trace_sha256":
            evaluation["inverse_trace_sha256"],
        "retained_conditions": evaluation["conditions"],
        "record_ledger_sha256":
            record_detail["record_ledger_sha256"],
        "permanence_snapshots_sha256":
            record_detail["permanence_snapshots_sha256"],
    }
    history["realized_history_sha256"] = digest(history)
    return history, facts, record_detail


def build_model(
    model_name: str,
    convention: str,
    base_battery: dict[str, bool],
    retained_surface_sha256: str,
    tie_evaluations: dict[tuple[int, ...], dict[str, object]],
) -> dict[str, object]:
    realized = independent_complete_selection(
        EXPECTED_FROZEN_K3_TIE, convention
    )
    if not isinstance(realized, tuple):
        raise AssertionError(("tie realization", realized))
    evaluation = tie_evaluations[realized]
    history, facts, record_detail = independent_history(
        model_name, convention, evaluation
    )
    battery = dict(base_battery)
    battery.update(
        {
            "completion_only_resolves_nonempty_ties": (
                independent_complete_selection((), convention) is None
                and all(
                    independent_complete_selection(
                        (alternative,), convention
                    )
                    == alternative
                    for alternative in EXPECTED_FROZEN_K3_TIE
                )
            ),
            "realized_member_is_in_frozen_retained_tie":
                realized in EXPECTED_FROZEN_K3_TIE,
            "realized_history_passes_all_retained_conditions":
                all(evaluation["conditions"].values()),
            "axiom_one_record_per_site": facts["one_record_per_site"],
            "axiom_records_permanent": facts["records_permanent"],
            "axiom_locked_possibility_admissible":
                facts["locked_possibility_admissible"],
            "retained_surface_signature_unchanged":
                retained_surface_sha256 == digest(base_battery),
        }
    )
    return {
        "name": model_name,
        "convention": convention,
        "realized_alternative": realized,
        "retained_surface_sha256": retained_surface_sha256,
        "battery": dict(sorted(battery.items())),
        "battery_checks_run": len(battery),
        "battery_checks_failed": sum(
            not passed for passed in battery.values()
        ),
        "battery_pass": all(battery.values()),
        "history": history,
        "axiom_facts": facts,
        "record_construction": record_detail,
    }


def battery_recount(
    extraction_detail: dict[str, object],
) -> tuple[bool, dict[str, object], dict[str, object]]:
    k_battery, k_detail = retained_k_battery()
    m_battery, m_detail, configurations = retained_m736_battery()
    single_battery, single_detail, single_rows = (
        single_source_battery()
    )
    tie_battery, tie_detail, tie_evaluations = frozen_tie_battery(
        configurations
    )
    base_battery = {
        **k_battery,
        **m_battery,
        **single_battery,
        **tie_battery,
    }
    retained_surface_sha256 = digest(base_battery)
    model_a = build_model(
        "MODEL A",
        "alpha",
        base_battery,
        retained_surface_sha256,
        tie_evaluations,
    )
    model_b = build_model(
        "MODEL B",
        "beta",
        base_battery,
        retained_surface_sha256,
        tie_evaluations,
    )
    expected_keys = set(extraction_detail["model_battery_keys"])
    passed = (
        len(base_battery) == 22
        and all(base_battery.values())
        and model_a["battery_checks_run"] == 29
        and model_b["battery_checks_run"] == 29
        and model_a["battery_checks_failed"] == 0
        and model_b["battery_checks_failed"] == 0
        and model_a["battery_pass"]
        and model_b["battery_pass"]
        and set(model_a["battery"]) == expected_keys
        and set(model_b["battery"]) == expected_keys
        and model_a["battery"] == model_b["battery"]
        and single_detail["fixtures"]
        == single_detail["agreements"]
        == 38
        and single_detail["disagreements"] == 0
    )
    detail = {
        "shared_battery": {
            "checks_run": len(base_battery),
            "checks_failed": sum(
                not value for value in base_battery.values()
            ),
            "surface_sha256": retained_surface_sha256,
        },
        "MODEL_A": {
            "checks_run": model_a["battery_checks_run"],
            "checks_passed": sum(model_a["battery"].values()),
            "checks_failed": model_a["battery_checks_failed"],
        },
        "MODEL_B": {
            "checks_run": model_b["battery_checks_run"],
            "checks_passed": sum(model_b["battery"].values()),
            "checks_failed": model_b["battery_checks_failed"],
        },
        "single_source": single_detail,
        "tie": tie_detail,
        "K": k_detail,
        "M736": m_detail,
    }
    private = {
        "models": (model_a, model_b),
        "configurations": configurations,
        "single_rows": single_rows,
        "tie_evaluations": tie_evaluations,
    }
    return passed, detail, private


def _mathematical_forward_trace(
    positions: tuple[int, ...],
) -> tuple[tuple[tuple[int, ...], tuple[int, ...], int], ...]:
    return tuple(
        (
            independent_rotate_positions(positions, step),
            independent_rotate_positions(positions, step + 1),
            0,
        )
        for step in range(RING_STATIONS)
    )


def _mathematical_inverse_trace(
    positions: tuple[int, ...],
) -> tuple[tuple[tuple[int, ...], tuple[int, ...], int], ...]:
    return tuple(
        (
            independent_rotate_positions(positions, -step),
            independent_rotate_positions(positions, -(step + 1)),
            0,
        )
        for step in range(RING_STATIONS)
    )


def disagreement_recount(
    extraction_detail: dict[str, object],
    private: dict[str, object],
) -> tuple[bool, dict[str, object]]:
    model_a, model_b = private["models"]
    evaluations = private["tie_evaluations"]
    expected_histories = []
    exact_history_matches = []
    trace_matches = []
    inverse_trace_matches = []
    for model in (model_a, model_b):
        realized = model["realized_alternative"]
        evaluation = evaluations[realized]
        recounted, _facts, _records = independent_history(
            model["name"], model["convention"], evaluation
        )
        expected_histories.append(recounted)
        exact_history_matches.append(recounted == model["history"])
        trace_matches.append(
            evaluation["trace"]
            == _mathematical_forward_trace(realized)
        )
        inverse_trace_matches.append(
            evaluation["inverse_trace"]
            == _mathematical_inverse_trace(realized)
        )
    extracted_fields = tuple(extraction_detail["history_fields"])
    histories = (model_a["history"], model_b["history"])
    digest_integrity = tuple(
        history["realized_history_sha256"]
        == digest(
            {
                key: value
                for key, value in history.items()
                if key != "realized_history_sha256"
            }
        )
        for history in histories
    )
    passed = (
        model_a["realized_alternative"] == (0, 2, 4)
        and model_b["realized_alternative"] == (0, 7, 9)
        and model_a["realized_alternative"]
        != model_b["realized_alternative"]
        and model_a["history"]["realized_history_sha256"]
        != model_b["history"]["realized_history_sha256"]
        and all(exact_history_matches)
        and all(trace_matches)
        and all(inverse_trace_matches)
        and all(digest_integrity)
        and all(tuple(history) == extracted_fields for history in histories)
        and all(
            len(history["orbit_trace"]) == RING_STATIONS
            for history in histories
        )
    )
    return passed, {
        "MODEL_A": {
            "realized_alternative": model_a["realized_alternative"],
            "history_sha256":
                model_a["history"]["realized_history_sha256"],
            "trace_sha256": digest(model_a["history"]["orbit_trace"]),
            "exact_reproduction": exact_history_matches[0],
        },
        "MODEL_B": {
            "realized_alternative": model_b["realized_alternative"],
            "history_sha256":
                model_b["history"]["realized_history_sha256"],
            "trace_sha256": digest(model_b["history"]["orbit_trace"]),
            "exact_reproduction": exact_history_matches[1],
        },
        "histories_differ": (
            model_a["history"]["realized_history_sha256"]
            != model_b["history"]["realized_history_sha256"]
        ),
        "mathematical_forward_traces_exact": all(trace_matches),
        "mathematical_inverse_traces_exact": all(inverse_trace_matches),
        "history_digest_integrity": all(digest_integrity),
    }


def _observable_bundle(
    convention: str,
    survivors: tuple[object, ...],
    before: int,
    program: tuple[object, ...],
    bank_count: int,
) -> dict[str, object]:
    realized = independent_complete_selection(survivors, convention)
    if isinstance(realized, int):
        positions = (realized,)
    elif isinstance(realized, tuple):
        positions = realized
    else:
        raise AssertionError(("lawful singleton did not realize", realized))
    after, rail_a, rail_b, trace = K.run_orbit(
        before, program, token_positions=positions
    )
    restored, inverse_a, inverse_b, inverse_trace = K.run_orbit(
        after, program, token_positions=positions, reverse=True
    )
    facts, records = independent_record_construction(
        positions, len(trace)
    )
    return {
        "realized_positions": positions,
        "after_register_state": after,
        "forward_A_rail": rail_a,
        "forward_B_rail": rail_b,
        "forward_trace": trace,
        "restored_register_state": restored,
        "inverse_A_rail": inverse_a,
        "inverse_B_rail": inverse_b,
        "inverse_trace": inverse_trace,
        "record_facts": facts,
        "record_ledger": records["records"],
        "record_snapshots": records["snapshots"],
    }


def leakage_attack(
    private: dict[str, object],
) -> tuple[bool, dict[str, object]]:
    """Search every declared off-tie family for physical convention leakage."""

    differences = []
    lawfulness_failures = []
    case_rows = []
    for row in private["single_rows"]:
        survivors = tuple(row["selected"])
        alpha = _observable_bundle(
            "alpha",
            survivors,
            row["before"],
            row["program"],
            row["bank_count"],
        )
        beta = _observable_bundle(
            "beta",
            survivors,
            row["before"],
            row["program"],
            row["bank_count"],
        )
        differing_fields = tuple(
            key for key in alpha if alpha[key] != beta[key]
        )
        if differing_fields:
            differences.append(
                {
                    "family": "F750_single_source",
                    "banks": row["bank_count"],
                    "event": row["event"],
                    "fields": differing_fields,
                }
            )
        case_rows.append(
            (
                "F750",
                row["bank_count"],
                row["event"],
                survivors,
                digest(alpha),
                digest(beta),
                differing_fields,
            )
        )

    program = K.interleaved_program(FIXTURE_BANKS)
    _event, _direction, _program, before, _expected = (
        F750.k_epoch_fixtures(FIXTURE_BANKS)[0]
    )
    k1_configurations = tuple(
        config
        for config in private["configurations"]
        if sum(config) == 1
    )
    for config in k1_configurations:
        positions = M736.occupied_sites(config)
        survivors = (positions,)
        alpha = _observable_bundle(
            "alpha", survivors, before, program, FIXTURE_BANKS
        )
        beta = _observable_bundle(
            "beta", survivors, before, program, FIXTURE_BANKS
        )
        differing_fields = tuple(
            key for key in alpha if alpha[key] != beta[key]
        )
        lawful = (
            M736.is_pairwise_separated(config)
            and positions in {
                M736.occupied_sites(row)
                for row in private["configurations"]
            }
            and alpha["after_register_state"]
            == K.A.apply_semantic(
                before,
                independent_synchronous_word(program, positions),
            )
            and alpha["forward_A_rail"] == config
            and not any(alpha["forward_B_rail"])
            and alpha["restored_register_state"] == before
            and alpha["inverse_A_rail"] == config
            and not any(alpha["inverse_B_rail"])
        )
        if differing_fields:
            differences.append(
                {
                    "family": "M736_k1",
                    "positions": positions,
                    "fields": differing_fields,
                }
            )
        if not lawful:
            lawfulness_failures.append(
                {
                    "family": "M736_k1",
                    "positions": positions,
                }
            )
        case_rows.append(
            (
                "M736_k1",
                positions,
                lawful,
                digest(alpha),
                digest(beta),
                differing_fields,
            )
        )

    passed = (
        len(private["single_rows"]) == 38
        and len(k1_configurations) == 11
        and len(case_rows) == 49
        and not differences
        and not lawfulness_failures
        and all(row[-3] == row[-2] for row in case_rows)
    )
    return passed, {
        "attack": (
            "compare traces, register/rail states, inverse restoration, "
            "record ledgers, and permanence snapshots across conventions"
        ),
        "F750_single_source_cases": len(private["single_rows"]),
        "M736_lawful_k1_cases": len(k1_configurations),
        "total_cases": len(case_rows),
        "observable_differences": len(differences),
        "first_difference": differences[0] if differences else None,
        "lawfulness_failures": len(lawfulness_failures),
        "first_lawfulness_failure": (
            lawfulness_failures[0] if lawfulness_failures else None
        ),
        "case_table_sha256": digest(case_rows),
        "clean_scoping_survives_attack": not differences,
        "verdict": (
            "NO_OFF_TIE_LEAKAGE_FOUND"
            if not differences
            else "REFUTED_BY_OFF_TIE_OBSERVABLE_DIFFERENCE"
        ),
    }


def axiom_facts_recount(
    private: dict[str, object],
) -> tuple[bool, dict[str, object]]:
    model_a, model_b = private["models"]
    results = {}
    for model in (model_a, model_b):
        realized = model["realized_alternative"]
        trace_length = len(model["history"]["orbit_trace"])
        facts, records = independent_record_construction(
            realized, trace_length
        )
        results[model["name"]] = {
            "facts": facts,
            "record_count": records["record_count"],
            "boundary_snapshots": records["boundary_snapshots"],
            "record_ledger_sha256":
                records["record_ledger_sha256"],
            "snapshots_sha256":
                records["permanence_snapshots_sha256"],
            "matches_frozen_model": (
                facts == model["axiom_facts"]
                and records["record_ledger_sha256"]
                == model["record_construction"][
                    "record_ledger_sha256"
                ]
                and records["permanence_snapshots_sha256"]
                == model["record_construction"][
                    "permanence_snapshots_sha256"
                ]
            ),
        }
    expected_fact_order = (
        "one_record_per_site",
        "records_permanent",
        "locked_possibility_admissible",
    )
    passed = all(
        tuple(result["facts"]) == expected_fact_order
        and all(result["facts"].values())
        and result["record_count"] == RING_STATIONS
        and result["boundary_snapshots"] == RING_STATIONS + 1
        and result["matches_frozen_model"]
        for result in results.values()
    )
    return passed, results


def discipline(
    extraction_detail: dict[str, object],
    leakage_detail: dict[str, object],
) -> tuple[bool, dict[str, object]]:
    scope = extraction_detail["scope"]
    exact_language = {
        "theorem_statement": (
            extraction_detail["theorem_statement"]
            == EXPECTED_THEOREM_STATEMENT
        ),
        "retained_scope_statement": (
            scope["scope_statement"] == EXPECTED_SCOPE_STATEMENT
        ),
        "leg1_stub": scope["leg1_stub"] == EXPECTED_LEG1_STUB,
        "leg3_stub": scope["leg3_stub"] == EXPECTED_LEG3_STUB,
        "terminal_statement": (
            scope["terminal_statement"] == EXPECTED_TERMINAL_SCOPE
        ),
    }
    passed = (
        all(exact_language.values())
        and scope["proved_scope"] == "RETAINED"
        and scope["not_claimed_scope"] == "bare-axiom"
        and scope["model_transfer_proved"] is False
        and scope["leg1_status"] == "NOT_YET_DEMONSTRATED"
        and scope["leg2_status"] == "PROVED_AT_RETAINED_SCOPE"
        and scope["leg3_status"] == "NO_DISTINGUISHED_CANDIDATE"
        and scope["axiom_update_triggered"] is False
        and leakage_detail["clean_scoping_survives_attack"]
    )
    return passed, {
        "exact_language": exact_language,
        "proved_scope": scope["proved_scope"],
        "not_claimed_scope": scope["not_claimed_scope"],
        "full_axiom_derivation_or_model_transfer_proved_here":
            scope["model_transfer_proved"],
        "leg_1_REQUIREMENT": scope["leg1_status"],
        "leg_2_NONENTAILMENT": scope["leg2_status"],
        "leg_3_CLEAR": scope["leg3_status"],
        "axiom_update_triggered": scope["axiom_update_triggered"],
        "terminal_statement": scope["terminal_statement"],
    }


def main() -> int:
    started = monotonic()

    extraction_pass, extraction_detail = extraction()
    check(
        "extraction_primary_as_data_and_29_check_contract",
        extraction_pass,
        {
            "model_battery_checks":
                extraction_detail["model_battery_checks"],
            "single_source_fixtures":
                extraction_detail["single_source_fixture_count"],
            "primary_imported":
                extraction_detail["primary_imported"],
        },
    )

    battery_pass, battery_detail, private = battery_recount(
        extraction_detail
    )
    check(
        "battery_recount_both_models_29_of_29_and_38_of_38",
        battery_pass,
        {
            "MODEL_A": battery_detail["MODEL_A"],
            "MODEL_B": battery_detail["MODEL_B"],
            "single_source": {
                "fixtures":
                    battery_detail["single_source"]["fixtures"],
                "agreements":
                    battery_detail["single_source"]["agreements"],
                "disagreements":
                    battery_detail["single_source"]["disagreements"],
            },
        },
    )

    disagreement_pass, disagreement_detail = disagreement_recount(
        extraction_detail, private
    )
    check(
        "disagreement_recount_two_exact_frozen_tie_histories",
        disagreement_pass,
        {
            "MODEL_A": disagreement_detail["MODEL_A"],
            "MODEL_B": disagreement_detail["MODEL_B"],
            "histories_differ":
                disagreement_detail["histories_differ"],
        },
    )

    leakage_pass, leakage_detail = leakage_attack(private)
    check(
        "leakage_attack_conventions_invisible_on_lawful_off_tie_families",
        leakage_pass,
        leakage_detail,
    )

    axiom_pass, axiom_detail = axiom_facts_recount(private)
    check(
        "axiom_facts_recount_both_constructions",
        axiom_pass,
        {
            model: {
                "facts": detail["facts"],
                "record_count": detail["record_count"],
                "matches_frozen_model":
                    detail["matches_frozen_model"],
            }
            for model, detail in axiom_detail.items()
        },
    )

    discipline_pass, discipline_detail = discipline(
        extraction_detail, leakage_detail
    )
    check(
        "discipline_retained_scope_only_and_no_update_triggered",
        discipline_pass,
        discipline_detail,
    )

    elapsed = monotonic() - started
    check(
        "runtime_bounded_under_1800_seconds",
        elapsed < AUDIT_TIMEOUT_SEC,
        {
            "runtime_seconds": round(elapsed, 6),
            "timeout_seconds": AUDIT_TIMEOUT_SEC,
        },
    )
    check(
        "primary_remained_import_blocked",
        PRIMARY_MODULE not in sys.modules,
        {"primary_imported": PRIMARY_MODULE in sys.modules},
    )

    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "BLOCKLIST": BLOCKLIST,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "certificates": {
            "extraction": {
                "audit_literal_eval":
                    extraction_detail["audit_literal_eval"],
                "primary_sha256":
                    extraction_detail["primary_sha256"],
                "primary_imported":
                    extraction_detail["primary_imported"],
                "model_battery_checks":
                    extraction_detail["model_battery_checks"],
                "single_source_fixture_count":
                    extraction_detail["single_source_fixture_count"],
                "frozen_history_blueprints":
                    extraction_detail["frozen_history_blueprints"],
                "theorem_statement":
                    extraction_detail["theorem_statement"],
            },
            "battery_recount": battery_detail,
            "disagreement_recount": disagreement_detail,
            "leakage_attack": leakage_detail,
            "axiom_facts_recount": axiom_detail,
            "discipline": discipline_detail,
        },
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "pass": all(CHECKS.values()),
        "runtime_seconds": round(elapsed, 6),
        "terminal": (
            "CYCLE767_MODEL_PAIR_INDEPENDENT_CHECK_PASS"
            if all(CHECKS.values())
            else "CYCLE767_MODEL_PAIR_INDEPENDENT_CHECK_HONEST_FAIL"
        ),
    }
    preliminary = compact(report)
    projected_bytes = (
        len("\n".join(OUTPUT_LINES).encode("utf-8"))
        + len(preliminary.encode("utf-8"))
        + 4096
    )
    check(
        "stdout_under_150KB",
        projected_bytes < STDOUT_LIMIT_BYTES,
        {
            "projected_bytes": projected_bytes,
            "limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(
        not value for value in CHECKS.values()
    )
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE767_MODEL_PAIR_INDEPENDENT_CHECK_PASS"
        if report["pass"]
        else "CYCLE767_MODEL_PAIR_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    report["report_sha256"] = digest(report)
    output = "\n".join(OUTPUT_LINES) + "\n" + compact(report) + "\n"
    output_bytes = len(output.encode("utf-8"))
    if output_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", output_bytes))
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
