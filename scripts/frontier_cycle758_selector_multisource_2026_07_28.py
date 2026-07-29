#!/usr/bin/env python3
"""Cycle 758: occurrence-selector extension on the ring-11 multisource sector.

The Cycle-750 alternative "one token at station s" is extended to a lawful
simultaneous token configuration.  A translation family is one epoch's
alternative set.  For every alternative, Cycle 736 independently supplies the
exact synchronous composition word; the Cycle-750 rail-return, literal-inverse,
and clean-postimage exclusions are then applied without an ACTUAL/reference
input.

Scientific non-totality, ties, and covariance failures are frozen findings, not
runner failures.  The theorem scope is all k <= 2 configurations and one
declared translation-complete family in each k = 3, 4, 5 stratum.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = (
    "docs/SELECTOR_MULTISOURCE_CYCLE758_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
STDOUT_LIMIT_BYTES = 150 * 1024
DECLARED_HIGH_K_FAMILY_REPRESENTATIVES = {
    3: ((0, 2, 4),),
    4: ((0, 2, 4, 6),),
    5: ((0, 2, 4, 6, 8),),
}

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []
CERTIFICATE_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest_rows(rows: object) -> str:
    return sha256(compact(rows).encode("utf-8")).hexdigest()


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {passed}"
    )
    return passed


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def configuration_families(
    configurations: tuple[tuple[int, ...], ...],
) -> dict[int, dict[tuple[int, ...], tuple[tuple[int, ...], ...]]]:
    grouped: dict[
        int, dict[tuple[int, ...], set[tuple[int, ...]]]
    ] = {}
    for config in configurations:
        positions = M736.occupied_sites(config)
        count = len(positions)
        representative = (
            min(
                rotate_positions(positions, shift)
                for shift in range(RING_STATIONS)
            )
            if positions
            else ()
        )
        grouped.setdefault(count, {}).setdefault(
            representative, set()
        ).add(positions)
    return {
        count: {
            representative: tuple(sorted(alternatives))
            for representative, alternatives in sorted(families.items())
        }
        for count, families in sorted(grouped.items())
    }


def build_sample(
    configurations: tuple[tuple[int, ...], ...],
) -> tuple[
    tuple[tuple[int, tuple[int, ...], tuple[tuple[int, ...], ...]], ...],
    dict[str, object],
]:
    families = configuration_families(configurations)
    selected = []
    for count in (1, 2):
        for representative, alternatives in families[count].items():
            selected.append((count, representative, alternatives))
    for count, declared in DECLARED_HIGH_K_FAMILY_REPRESENTATIVES.items():
        for representative in declared:
            selected.append(
                (count, representative, families[count][representative])
            )

    selected_counts = {
        count: sum(
            len(alternatives)
            for observed_count, _representative, alternatives in selected
            if observed_count == count
        )
        for count in range(M736.MAX_TOKEN_COUNT + 1)
    }
    selected_counts[0] = len(families[0][()])
    full_counts = {
        count: sum(
            len(alternatives)
            for alternatives in families[count].values()
        )
        for count in range(M736.MAX_TOKEN_COUNT + 1)
    }
    family_counts = {
        count: len(families[count])
        for count in range(M736.MAX_TOKEN_COUNT + 1)
    }
    selected_family_counts = {
        count: sum(
            observed_count == count
            for observed_count, _representative, _alternatives in selected
        )
        for count in range(M736.MAX_TOKEN_COUNT + 1)
    }
    selected_family_counts[0] = 1
    strata = {
        "ring_stations": RING_STATIONS,
        "full_configuration_counts_by_k": full_counts,
        "full_translation_family_counts_by_k": family_counts,
        "selected_configuration_counts_by_k": selected_counts,
        "selected_translation_family_counts_by_k":
            selected_family_counts,
        "declared_high_k_family_representatives":
            DECLARED_HIGH_K_FAMILY_REPRESENTATIVES,
        "configurations_exhausted": sum(selected_counts.values()),
        "nonvacuum_configurations_evaluated":
            sum(selected_counts[count] for count in range(1, 6)),
        "exhausted_strata": tuple(
            count
            for count in range(6)
            if selected_counts[count] == full_counts[count]
        ),
        "sample_only_strata": tuple(
            count
            for count in range(3, 6)
            if selected_counts[count] < full_counts[count]
        ),
        "translation_complete_sample": all(
            len(alternatives) == RING_STATIONS
            for _count, _representative, alternatives in selected
        ),
    }
    return tuple(selected), strata


def clean_postimage(after: int, bank_count: int) -> bool:
    banks, links = K.M.unpack_state(after, bank_count)
    return not any(
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


def multisource_enforcement_lineage_selector(
    program: tuple[object, ...],
    before: int,
    bank_count: int,
    alternatives: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    """Apply F750's exclusions to M736 configuration alternatives."""

    selected = []
    evaluations = []
    for positions in alternatives:
        tokens = tuple(
            int(station in positions) for station in range(len(program))
        )
        zeros = tuple(value ^ value for value in tokens)
        composition_word = M736.synchronous_composition_word(
            program, positions
        )
        expected = K.A.apply_semantic(before, composition_word)
        after, rail_a, rail_b, _trace = K.run_orbit(
            before, program, token_positions=positions
        )
        restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
            after, program, token_positions=positions, reverse=True
        )
        conditions = {
            "synchronous_composition": after == expected,
            "token_rail_return": rail_a == tokens and rail_b == zeros,
            "literal_inverse": (
                restored == before
                and inverse_a == rail_a
                and inverse_b == rail_b
            ),
            "clean_postimage": clean_postimage(after, bank_count),
        }
        if all(conditions.values()):
            selected.append(positions)
        evaluations.append(
            {
                "positions": positions,
                "conditions": conditions,
            }
        )
    return {
        "alternatives": alternatives,
        "selected": tuple(selected),
        "evaluations": tuple(evaluations),
    }


AUDITED_CONSTRUCTION_FUNCTIONS = (
    "rotate_positions",
    "configuration_families",
    "build_sample",
    "clean_postimage",
    "multisource_enforcement_lineage_selector",
)


def header_and_ast_audit() -> dict[str, object]:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    assignments = {}
    functions = {}
    imports = {}
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = (
                node.targets
                if isinstance(node, ast.Assign)
                else (node.target,)
            )
            for target in targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
        elif isinstance(node, ast.FunctionDef):
            functions[node.name] = node
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports[alias.asname or alias.name] = alias.name

    audit_tuple = assignments["AUDIT_INPUT_PATHS"]
    declared = assignments["DECLARED_INPUT_PATHS"]
    literal_tuple = (
        isinstance(audit_tuple, ast.Tuple)
        and len(audit_tuple.elts) == 3
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_tuple.elts
        )
    )
    supplier_imports = {
        alias: imports.get(alias) for alias in ("F750", "M736", "K")
    }
    expected_imports = {
        "F750":
            "frontier_cycle750_actual_selector_stretch_2026_07_28",
        "M736":
            "frontier_cycle736_pairwise_separated_multisource_2026_07_28",
        "K":
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
    }

    ast_rows = {}
    module_roots = {}
    forbidden_identification_inputs = {}
    for name in AUDITED_CONSTRUCTION_FUNCTIONS:
        function = functions[name]
        ast_rows[name] = ast.unparse(function)
        roots = set()
        for child in ast.walk(function):
            if isinstance(child, ast.Attribute):
                root = child
                while isinstance(root, ast.Attribute):
                    root = root.value
                if (
                    isinstance(root, ast.Name)
                    and root.id in {"F750", "M736", "K"}
                ):
                    roots.add(root.id)
        module_roots[name] = tuple(sorted(roots))
        forbidden_identification_inputs[name] = tuple(
            argument.arg
            for argument in function.args.args
            if argument.arg.lower()
            in {"actual", "reference", "selected", "survivor"}
        )

    expected_roots = {
        "rotate_positions": (),
        "configuration_families": ("M736",),
        "build_sample": ("M736",),
        "clean_postimage": ("K",),
        "multisource_enforcement_lineage_selector": ("K", "M736"),
    }
    selector_ast = ast_rows["multisource_enforcement_lineage_selector"]
    construction_exact = all(
        token in selector_ast
        for token in (
            "M736.synchronous_composition_word",
            "K.A.apply_semantic",
            "K.run_orbit",
            "reverse=True",
            "clean_postimage",
        )
    )
    header_pass = (
        literal_tuple
        and tuple(ast.literal_eval(audit_tuple)) == AUDIT_INPUT_PATHS
        and isinstance(declared, ast.Name)
        and declared.id == "AUDIT_INPUT_PATHS"
        and AUDIT_TIMEOUT_SEC == 1800
        and NOTE_PATH
        == (
            "docs/SELECTOR_MULTISOURCE_CYCLE758_BOUNDED_THEOREM_NOTE_"
            "2026-07-28.md"
        )
        and supplier_imports == expected_imports
    )
    supplier_pass = (
        module_roots == expected_roots
        and all(
            not values
            for values in forbidden_identification_inputs.values()
        )
    )
    return {
        "header_pass": header_pass,
        "pure_literal_audit_tuple": literal_tuple,
        "declared_is_audit_name":
            isinstance(declared, ast.Name)
            and declared.id == "AUDIT_INPUT_PATHS",
        "supplier_imports": supplier_imports,
        "construction_functions": AUDITED_CONSTRUCTION_FUNCTIONS,
        "construction_module_roots": module_roots,
        "forbidden_identification_inputs":
            forbidden_identification_inputs,
        "construction_exact": construction_exact,
        "no_new_supplier": supplier_pass,
        "construction_ast_sha256": digest_rows(ast_rows),
        "printed_ast": {
            "multisource_enforcement_lineage_selector":
                ast_rows["multisource_enforcement_lineage_selector"],
            "build_sample": ast_rows["build_sample"],
        },
    }


def anchor_certificates() -> tuple[
    dict[str, object], tuple[tuple[int, ...], ...]
]:
    F750.PASS = F750.FAIL = 0
    captured = StringIO()
    with redirect_stdout(captured):
        single_source = F750.enforcement_candidate_census()
    f750_anchor = {
        "fixtures_exhausted": single_source["fixtures_exhausted"],
        "alternatives_exhausted":
            single_source["alternatives_exhausted"],
        "selected_count_range":
            single_source["selected_count_range"],
        "tests": single_source["tests"],
        "internal_check_failures": F750.FAIL,
        "captured_stdout_bytes":
            len(captured.getvalue().encode("utf-8")),
    }

    full_census = M736.configuration_census()
    configurations = full_census.pop("configurations")
    orbit = M736.invariant_full_orbit_certificate(configurations)
    m736_anchor = {
        "direct_counts_by_k": full_census["direct_counts_by_k"],
        "direct_total": full_census["direct_total"],
        "agreement": full_census["agreement"],
        "configuration_mask_table_sha256":
            full_census["configuration_mask_table_sha256"],
        "orbit_configurations": orbit["orbit_configurations"],
        "pairwise_separated_sector_lawful":
            orbit["pairwise_separated_sector_lawful"],
        "composition_definition": orbit["composition_definition"],
        "failure_census": orbit["failure_census"],
    }
    anchors = {
        "F750_single_source_rerun": f750_anchor,
        "M736_full_census_and_orbit": m736_anchor,
    }
    return anchors, configurations


def epoch_family_census(
    sampled_families: tuple[
        tuple[int, tuple[int, ...], tuple[tuple[int, ...], ...]], ...
    ],
) -> dict[str, object]:
    fixtures = F750.k_epoch_fixtures(FIXTURE_BANKS)
    rows = []
    selected_by_family_event = {}
    failed_conditions: Counter[str] = Counter()

    by_k = {
        str(count): {
            "family_epochs": 0,
            "configuration_evaluations": 0,
            "unique_epochs": 0,
            "zero_survivor_epochs": 0,
            "tie_epochs": 0,
            "survivors": 0,
        }
        for count in range(1, M736.MAX_TOKEN_COUNT + 1)
    }
    for count, representative, alternatives in sampled_families:
        key = f"k{count}:{','.join(map(str, representative))}"
        selected_by_family_event[key] = []
        for event, direction, program, before, _single_expected in fixtures:
            result = multisource_enforcement_lineage_selector(
                program, before, FIXTURE_BANKS, alternatives
            )
            selected = result["selected"]
            selected_by_family_event[key].append(len(selected))
            for evaluation in result["evaluations"]:
                for condition, passed in evaluation["conditions"].items():
                    if not passed:
                        failed_conditions[condition] += 1
            selected_count = len(selected)
            row = {
                "k": count,
                "representative": representative,
                "event": event,
                "direction": direction,
                "alternative_count": len(alternatives),
                "selected_count": selected_count,
                "selected": selected,
            }
            rows.append(row)
            aggregate = by_k[str(count)]
            aggregate["family_epochs"] += 1
            aggregate["configuration_evaluations"] += len(alternatives)
            aggregate["unique_epochs"] += selected_count == 1
            aggregate["zero_survivor_epochs"] += selected_count == 0
            aggregate["tie_epochs"] += selected_count > 1
            aggregate["survivors"] += selected_count

    first_fixture = fixtures[0]
    invariance_family_cases = 0
    invariance_family_failures = []
    invariance_configuration_cases = 0
    invariance_configuration_failures = 0
    invariance_by_k = {
        str(count): {"configuration_cases": 0, "failures": 0}
        for count in range(1, M736.MAX_TOKEN_COUNT + 1)
    }
    for count, representative, alternatives in sampled_families:
        base = multisource_enforcement_lineage_selector(
            first_fixture[2],
            first_fixture[3],
            FIXTURE_BANKS,
            alternatives,
        )["selected"]
        for shift in range(RING_STATIONS):
            rotated_program = (
                first_fixture[2][shift:] + first_fixture[2][:shift]
            )
            observed = (
                base
                if shift == 0
                else multisource_enforcement_lineage_selector(
                    rotated_program,
                    first_fixture[3],
                    FIXTURE_BANKS,
                    alternatives,
                )["selected"]
            )
            expected = tuple(
                sorted(
                    rotate_positions(positions, -shift)
                    for positions in base
                )
            )
            symmetric_difference = len(set(observed) ^ set(expected))
            invariance_family_cases += 1
            invariance_configuration_cases += len(alternatives)
            invariance_configuration_failures += symmetric_difference
            invariance_by_k[str(count)]["configuration_cases"] += (
                len(alternatives)
            )
            invariance_by_k[str(count)]["failures"] += (
                symmetric_difference
            )
            if observed != expected:
                invariance_family_failures.append(
                    {
                        "k": count,
                        "representative": representative,
                        "shift": shift,
                        "observed": observed,
                        "covariant_expected": expected,
                        "configuration_membership_failures":
                            symmetric_difference,
                    }
                )

    return {
        "definition": (
            "A translation family is an epoch alternative set.  Each "
            "configuration's expected data output is independently rebuilt "
            "from M736.synchronous_composition_word; F750's token-return, "
            "literal-inverse, and clean-postimage exclusions are unchanged."
        ),
        "epochs_per_family": len(fixtures),
        "families_evaluated": len(sampled_families),
        "configuration_evaluations": sum(
            row["alternative_count"] for row in rows
        ),
        "rows": rows,
        "selected_count_matrix": selected_by_family_event,
        "per_k_totality_census": by_k,
        "failed_condition_census": dict(sorted(failed_conditions.items())),
        "unique_family_epochs": sum(
            row["selected_count"] == 1 for row in rows
        ),
        "zero_survivor_family_epochs": sum(
            row["selected_count"] == 0 for row in rows
        ),
        "tie_family_epochs": sum(
            row["selected_count"] > 1 for row in rows
        ),
        "invariance_scope":
            "all sampled configurations, all 11 program-ring translations, "
            "first Cycle-750 two-bank epoch",
        "invariance_family_cases": invariance_family_cases,
        "invariance_family_failure_count":
            len(invariance_family_failures),
        "invariance_family_failures": invariance_family_failures,
        "invariance_configuration_cases":
            invariance_configuration_cases,
        "invariance_configuration_failures":
            invariance_configuration_failures,
        "invariance_by_k": invariance_by_k,
        "census_sha256": digest_rows(
            (
                rows,
                selected_by_family_event,
                dict(sorted(failed_conditions.items())),
                invariance_family_failures,
            )
        ),
    }


def identification_certificate(
    configurations: tuple[tuple[int, ...], ...],
    sampled_families: tuple[
        tuple[int, tuple[int, ...], tuple[tuple[int, ...], ...]], ...
    ],
    census: dict[str, object],
) -> dict[str, object]:
    fixtures = F750.k_epoch_fixtures(FIXTURE_BANKS)
    k1_rows = [
        row for row in census["rows"] if row["k"] == 1
    ]
    single_source_identified = all(
        row["selected"] == ((0,),) for row in k1_rows
    )

    k2_configurations = tuple(
        M736.occupied_sites(config)
        for config in configurations
        if sum(config) == 2
    )
    held_event = fixtures[0]
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    twice = K.A.apply_semantic(
        K.A.apply_semantic(held_event[3], allocator), allocator
    )
    k2_comparator_matches = 0
    for positions in k2_configurations:
        after, _rail_a, _rail_b, _trace = K.run_orbit(
            held_event[3],
            held_event[2],
            token_positions=positions,
        )
        k2_comparator_matches += after == twice

    sampled_by_k = {
        count: alternatives
        for count, _representative, alternatives in sampled_families
        if count >= 3
    }
    output_classes_by_k_event = {}
    for count, alternatives in sampled_by_k.items():
        output_classes_by_k_event[str(count)] = []
        for _event, _direction, program, before, _expected in fixtures:
            outputs = tuple(
                K.run_orbit(
                    before, program, token_positions=positions
                )[0]
                for positions in alternatives
            )
            output_classes_by_k_event[str(count)].append(
                len(set(outputs))
            )

    return {
        "k1": {
            "comparator": "F750 supplied source-token reference",
            "family_epochs": len(k1_rows),
            "identified_source": (0,),
            "all_identified": single_source_identified,
        },
        "k2": {
            "comparator": (
                "M736 held event-0 allocator squared; position-independent "
                "only on that landed fixture"
            ),
            "configurations_compared": len(k2_configurations),
            "comparator_matches": k2_comparator_matches,
            "selector_survivors_all_four_families_all_epochs": 0,
            "identification": (
                "available output comparator, but no surviving occurrence "
                "to identify"
            ),
        },
        "k3_to_k5": {
            "position_independent_landed_comparator": False,
            "configuration_specific_composition_checked": True,
            "sample_output_classes_by_k_event":
                output_classes_by_k_event,
            "identification":
                "not forced; the landed M736 law is configuration-specific",
        },
    }


def outcome_certificate(
    strata: dict[str, object],
    census: dict[str, object],
    identification: dict[str, object],
) -> dict[str, object]:
    first_k2_row = next(
        row for row in census["rows"] if row["k"] == 2
    )
    k3_tie = next(
        row
        for row in census["rows"]
        if row["k"] == 3 and row["selected_count"] > 1
    )
    return {
        "outcome": "PARTIAL_EXTENSION",
        "statement": (
            "The selector extends uniquely through the exhaustive k=1 "
            "translation family, but totality first fails at k=2.  The "
            "declared k=3 sample also contains a genuine three-survivor tie "
            "and a cyclic-covariance failure."
        ),
        "exact_boundary": {
            "vacuum_k0":
                "exhausted census control; no occurrence-selector claim",
            "k1": (
                "all 11 configurations exhausted; one survivor in every "
                "Cycle-750 two-bank epoch"
            ),
            "first_break_k": 2,
            "k2": (
                "all 44 configurations in four translation families "
                "exhausted; zero survivors in every epoch"
            ),
            "first_k2_failure": first_k2_row,
            "sampled_k3": (
                "declared translation family has selected counts "
                "[3,0,0,1]"
            ),
            "frozen_k3_tie": k3_tie,
            "sampled_k4": "declared translation family has [0,0,0,0]",
            "sampled_k5": "sole translation family has [0,0,0,0]",
            "higher_k_full_sector_claim": False,
            "sample_only_strata": strata["sample_only_strata"],
        },
        "identification_boundary": identification,
        "no_new_supplier": True,
        "honest_boundary_keys": {
            "selector_multisource_full_extension": False,
            "selector_multisource_partial_extension": True,
            "selector_multisource_blocked": False,
            "first_non_total_k": 2,
            "zero_survivor_boundary_present": True,
            "multisource_tie_present": True,
            "cyclic_invariance_failure_present": True,
            "no_forced_identification_k3_to_k5": True,
            "ring11_only": True,
            "pairwise_separated_only": True,
            "program_and_genesis_supplied": True,
            "higher_k_sample_only": True,
            "w3_fixture_scope_would_extend_if_full": True,
            "w3_fixture_scope_extended": False,
            "w3_closed": False,
        },
        "w3_scope_statement": (
            "A full result would extend the capstone fixture scope from "
            "single-source to the ring-11 pairwise-separated multisource "
            "sector.  This partial result does not extend that scope."
        ),
    }


def main() -> int:
    started = monotonic()

    ast_audit = header_and_ast_audit()
    check(
        "A_header_literal_inputs_and_exact_imports",
        ast_audit["header_pass"],
    )
    check(
        "B_extended_construction_AST_and_no_new_supplier",
        ast_audit["construction_exact"]
        and ast_audit["no_new_supplier"],
    )
    CERTIFICATE_LINES.append(
        "AST multisource_enforcement_lineage_selector :: "
        + compact(
            ast_audit["printed_ast"][
                "multisource_enforcement_lineage_selector"
            ]
        )
    )
    CERTIFICATE_LINES.append(
        "AST build_sample :: "
        + compact(ast_audit["printed_ast"]["build_sample"])
    )

    anchors, configurations = anchor_certificates()
    check(
        "C_anchors_F750_single_source_rerun_and_M736_census",
        anchors["F750_single_source_rerun"]["tests"]
        == {
            "totality": True,
            "invariance": True,
            "identification": True,
        }
        and anchors["F750_single_source_rerun"]["fixtures_exhausted"]
        == 38
        and anchors["F750_single_source_rerun"]["alternatives_exhausted"]
        == 2578
        and anchors["F750_single_source_rerun"][
            "internal_check_failures"
        ]
        == 0
        and anchors["M736_full_census_and_orbit"]["agreement"]
        and anchors["M736_full_census_and_orbit"]["direct_counts_by_k"]
        == M736.EXPECTED_COUNTS_BY_K
        and anchors["M736_full_census_and_orbit"]["direct_total"]
        == M736.EXPECTED_TOTAL_CONFIGURATIONS
        and anchors["M736_full_census_and_orbit"][
            "pairwise_separated_sector_lawful"
        ]
        and not any(
            anchors["M736_full_census_and_orbit"][
                "failure_census"
            ].values()
        ),
    )

    sampled_families, strata = build_sample(configurations)
    CERTIFICATE_LINES.append("STRATA :: " + compact(strata))
    check(
        "D_declared_strata_and_exhaustion_are_frozen",
        strata["full_configuration_counts_by_k"]
        == {0: 1, 1: 11, 2: 44, 3: 77, 4: 55, 5: 11}
        and strata["full_translation_family_counts_by_k"]
        == {0: 1, 1: 1, 2: 4, 3: 7, 4: 5, 5: 1}
        and strata["selected_configuration_counts_by_k"]
        == {0: 1, 1: 11, 2: 44, 3: 11, 4: 11, 5: 11}
        and strata["selected_translation_family_counts_by_k"]
        == {0: 1, 1: 1, 2: 4, 3: 1, 4: 1, 5: 1}
        and strata["configurations_exhausted"] == 89
        and strata["nonvacuum_configurations_evaluated"] == 88
        and strata["exhausted_strata"] == (0, 1, 2, 5)
        and strata["sample_only_strata"] == (3, 4)
        and strata["translation_complete_sample"],
    )

    census = epoch_family_census(sampled_families)
    expected_matrix = {
        "k1:0": [1, 1, 1, 1],
        "k2:0,2": [0, 0, 0, 0],
        "k2:0,3": [0, 0, 0, 0],
        "k2:0,4": [0, 0, 0, 0],
        "k2:0,5": [0, 0, 0, 0],
        "k3:0,2,4": [3, 0, 0, 1],
        "k4:0,2,4,6": [0, 0, 0, 0],
        "k5:0,2,4,6,8": [0, 0, 0, 0],
    }
    expected_totality_by_k = {
        "1": {
            "family_epochs": 4,
            "configuration_evaluations": 44,
            "unique_epochs": 4,
            "zero_survivor_epochs": 0,
            "tie_epochs": 0,
            "survivors": 4,
        },
        "2": {
            "family_epochs": 16,
            "configuration_evaluations": 176,
            "unique_epochs": 0,
            "zero_survivor_epochs": 16,
            "tie_epochs": 0,
            "survivors": 0,
        },
        "3": {
            "family_epochs": 4,
            "configuration_evaluations": 44,
            "unique_epochs": 1,
            "zero_survivor_epochs": 2,
            "tie_epochs": 1,
            "survivors": 4,
        },
        "4": {
            "family_epochs": 4,
            "configuration_evaluations": 44,
            "unique_epochs": 0,
            "zero_survivor_epochs": 4,
            "tie_epochs": 0,
            "survivors": 0,
        },
        "5": {
            "family_epochs": 4,
            "configuration_evaluations": 44,
            "unique_epochs": 0,
            "zero_survivor_epochs": 4,
            "tie_epochs": 0,
            "survivors": 0,
        },
    }
    check(
        "E_per_configuration_totality_and_exclusion_census",
        census["families_evaluated"] == 8
        and census["epochs_per_family"] == 4
        and census["configuration_evaluations"] == 352
        and census["selected_count_matrix"] == expected_matrix
        and census["per_k_totality_census"] == expected_totality_by_k
        and census["unique_family_epochs"] == 5
        and census["zero_survivor_family_epochs"] == 26
        and census["tie_family_epochs"] == 1
        and census["failed_condition_census"]
        == {"clean_postimage": 344},
    )
    check(
        "F_ring_translation_invariance_census_freezes_real_failure",
        census["invariance_family_cases"] == 88
        and census["invariance_family_failure_count"] == 9
        and census["invariance_configuration_cases"] == 968
        and census["invariance_configuration_failures"] == 27
        and census["invariance_by_k"]
        == {
            "1": {"configuration_cases": 121, "failures": 0},
            "2": {"configuration_cases": 484, "failures": 0},
            "3": {"configuration_cases": 121, "failures": 27},
            "4": {"configuration_cases": 121, "failures": 0},
            "5": {"configuration_cases": 121, "failures": 0},
        },
    )

    identification = identification_certificate(
        configurations, sampled_families, census
    )
    check(
        "G_identification_only_where_landed_comparator_exists",
        identification["k1"]["all_identified"]
        and identification["k1"]["family_epochs"] == 4
        and identification["k2"]["configurations_compared"] == 44
        and identification["k2"]["comparator_matches"] == 44
        and identification["k2"][
            "selector_survivors_all_four_families_all_epochs"
        ]
        == 0
        and not identification["k3_to_k5"][
            "position_independent_landed_comparator"
        ]
        and identification["k3_to_k5"][
            "sample_output_classes_by_k_event"
        ]
        == {
            "3": [3, 9, 7, 8],
            "4": [1, 10, 9, 11],
            "5": [10, 11, 11, 10],
        },
    )

    outcome = outcome_certificate(strata, census, identification)
    keys = outcome["honest_boundary_keys"]
    check(
        "H_partial_outcome_honest_boundary_and_w3_scope",
        outcome["outcome"] == "PARTIAL_EXTENSION"
        and outcome["exact_boundary"]["first_break_k"] == 2
        and outcome["exact_boundary"]["frozen_k3_tie"][
            "selected_count"
        ]
        == 3
        and not keys["selector_multisource_full_extension"]
        and keys["selector_multisource_partial_extension"]
        and not keys["selector_multisource_blocked"]
        and keys["first_non_total_k"] == 2
        and keys["zero_survivor_boundary_present"]
        and keys["multisource_tie_present"]
        and keys["cyclic_invariance_failure_present"]
        and keys["no_forced_identification_k3_to_k5"]
        and keys["w3_fixture_scope_would_extend_if_full"]
        and not keys["w3_fixture_scope_extended"]
        and not keys["w3_closed"],
    )

    elapsed = monotonic() - started
    check(
        "I_bounded_runtime_and_note_not_required",
        elapsed < AUDIT_TIMEOUT_SEC and NOTE_PATH.endswith(".md"),
    )

    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "anchors": anchors,
        "ast_audit": ast_audit,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "extended_census": census,
        "identification": identification,
        "outcome": outcome,
        "pass": all(CHECKS.values()),
        "runtime_seconds": round(elapsed, 6),
        "sampled_strata": strata,
        "terminal": (
            "CYCLE758_SELECTOR_MULTISOURCE_PASS"
            if all(CHECKS.values())
            else "CYCLE758_SELECTOR_MULTISOURCE_HONEST_FAIL"
        ),
    }
    preliminary = compact(report)
    projected = (
        "\n".join(OUTPUT_LINES + CERTIFICATE_LINES).encode("utf-8")
    )
    check(
        "J_stdout_under_150KB",
        len(projected) + len(preliminary.encode("utf-8")) + 4096
        < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(
        not value for value in CHECKS.values()
    )
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE758_SELECTOR_MULTISOURCE_PASS"
        if report["pass"]
        else "CYCLE758_SELECTOR_MULTISOURCE_HONEST_FAIL"
    )
    report["report_sha256"] = sha256(
        compact(report).encode("utf-8")
    ).hexdigest()
    final_json = compact(report)
    output = (
        "\n".join(OUTPUT_LINES + CERTIFICATE_LINES)
        + "\n"
        + final_json
        + "\n"
    )
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(output.encode("utf-8"))))
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
