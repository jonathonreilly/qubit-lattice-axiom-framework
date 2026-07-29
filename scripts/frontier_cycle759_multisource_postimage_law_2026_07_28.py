#!/usr/bin/env python3
"""Cycle 759: attempt the derived multisource postimage-law correction.

Cycle 758 found that every lawful k=2 update is vetoed only by the landed
single-source clean-postimage predicate.  This runner freezes the predicate's
exact residual coordinates for all 44 pairwise-separated two-token
configurations in every Cycle-750 two-bank epoch.  A per-source quotient is
eligible for construction only if that residue is one uniform, landed-labeled
bookkeeping block.  Non-uniformity is a scientific outcome, not a runner
failure; no quotient is then supplied by fiat and corrected-law retests are
reported as precondition-blocked.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = (
    "docs/MULTISOURCE_POSTIMAGE_LAW_CYCLE759_BOUNDED_THEOREM_NOTE_"
    "2026-07-28.md"
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


def build_cycle758_sample(
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
    full_counts = {
        count: sum(
            len(alternatives)
            for alternatives in families[count].values()
        )
        for count in range(M736.MAX_TOKEN_COUNT + 1)
    }
    selected_counts = {
        count: sum(
            len(alternatives)
            for observed, _representative, alternatives in selected
            if observed == count
        )
        for count in range(M736.MAX_TOKEN_COUNT + 1)
    }
    selected_counts[0] = 1
    full_family_counts = {
        count: len(families[count])
        for count in range(M736.MAX_TOKEN_COUNT + 1)
    }
    selected_family_counts = {
        count: sum(
            observed == count
            for observed, _representative, _alternatives in selected
        )
        for count in range(M736.MAX_TOKEN_COUNT + 1)
    }
    selected_family_counts[0] = 1
    return tuple(selected), {
        "full_configuration_counts_by_k": full_counts,
        "full_translation_family_counts_by_k": full_family_counts,
        "selected_configuration_counts_by_k": selected_counts,
        "selected_translation_family_counts_by_k":
            selected_family_counts,
        "selected_nonvacuum_configurations":
            sum(selected_counts[count] for count in range(1, 6)),
        "translation_complete": all(
            len(alternatives) == RING_STATIONS
            for _count, _representative, alternatives in selected
        ),
    }


def watched_bank_registers() -> tuple[tuple[str, int], ...]:
    return (
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
        *tuple(
            (f"FRESH[{index}]", wire)
            for index, wire in enumerate(K.A.FRESH)
        ),
        *tuple(
            (f"ZERO_WORK[{index}]", wire)
            for index, wire in enumerate(K.A.ZERO_WORK)
        ),
        ("TOKEN_OK", K.A.TOKEN_OK),
    )


def postimage_residual(
    after: int, bank_count: int
) -> tuple[tuple[str, str, int, int], ...]:
    """Exact nonzero projection used by the landed clean-postimage law.

    Coordinates and names come only from K's landed SOURCE_POINTER, bank
    register, and unpacked link labeling.  The final component is the exact
    binary content, not merely a dirty/clean flag.
    """

    banks, links = K.M.unpack_state(after, bank_count)
    residual = []
    source_content = after[K.R3.X.SOURCE_POINTER]
    if source_content:
        residual.append(
            (
                "source",
                "SOURCE_POINTER",
                K.R3.X.SOURCE_POINTER,
                source_content,
            )
        )
    for bank_index, bank in enumerate(banks):
        for register, wire in watched_bank_registers():
            content = bank[wire]
            if content:
                residual.append(
                    (
                        f"bank[{bank_index}]",
                        register,
                        wire,
                        content,
                    )
                )
    for link_index, link in enumerate(links):
        for wire, content in enumerate(link):
            if content:
                residual.append(
                    (
                        f"link[{link_index}]",
                        f"WIRE[{wire}]",
                        wire,
                        content,
                    )
                )
    return tuple(residual)


def clean_postimage(after: int, bank_count: int) -> bool:
    return not postimage_residual(after, bank_count)


def quotient_postimage(
    residual: tuple[tuple[str, str, int, int], ...],
    owned_bookkeeping: tuple[tuple[str, str, int, int], ...],
) -> bool:
    """Candidate schema: apply clean-postimage after an owned quotient."""

    owned = set(owned_bookkeeping)
    return not any(coordinate not in owned for coordinate in residual)


def evaluate_configuration(
    program: tuple[object, ...],
    before: int,
    positions: tuple[int, ...],
    bank_count: int,
) -> dict[str, object]:
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
    residual = postimage_residual(after, bank_count)
    conditions = {
        "synchronous_composition": after == expected,
        "token_rail_return": rail_a == tokens and rail_b == zeros,
        "literal_inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "clean_postimage": not residual,
    }
    return {
        "positions": positions,
        "conditions": conditions,
        "residual": residual,
    }


def selected_with_landed_law(
    program: tuple[object, ...],
    before: int,
    alternatives: tuple[tuple[int, ...], ...],
    bank_count: int,
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        positions
        for positions in alternatives
        if all(
            evaluate_configuration(
                program, before, positions, bank_count
            )["conditions"].values()
        )
    )


AUDITED_CONSTRUCTION_FUNCTIONS = (
    "configuration_families",
    "build_cycle758_sample",
    "watched_bank_registers",
    "postimage_residual",
    "clean_postimage",
    "quotient_postimage",
    "evaluate_configuration",
    "selected_with_landed_law",
)


def header_and_ast_audit() -> dict[str, object]:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    assignments = {}
    functions = {}
    imports = {}
    imported_from = {}
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
        elif isinstance(node, ast.ImportFrom):
            imported_from[node.module or ""] = tuple(
                alias.name for alias in node.names
            )

    audit_tuple = assignments["AUDIT_INPUT_PATHS"]
    declared = assignments["DECLARED_INPUT_PATHS"]
    pure_literal = (
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
    ast_rows = {
        name: ast.unparse(functions[name])
        for name in AUDITED_CONSTRUCTION_FUNCTIONS
    }
    module_roots = {}
    for name in AUDITED_CONSTRUCTION_FUNCTIONS:
        roots = set()
        for child in ast.walk(functions[name]):
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
    expected_roots = {
        "configuration_families": ("M736",),
        "build_cycle758_sample": ("M736",),
        "watched_bank_registers": ("K",),
        "postimage_residual": ("K",),
        "clean_postimage": (),
        "quotient_postimage": (),
        "evaluate_configuration": ("K", "M736"),
        "selected_with_landed_law": (),
    }
    quotient_body = functions["quotient_postimage"].body
    if (
        quotient_body
        and isinstance(quotient_body[0], ast.Expr)
        and isinstance(quotient_body[0].value, ast.Constant)
        and isinstance(quotient_body[0].value.value, str)
    ):
        quotient_body = quotient_body[1:]
    quotient_constants = tuple(
        child.value
        for statement in quotient_body
        for child in ast.walk(statement)
        if isinstance(child, ast.Constant)
    )
    standard_imports = {
        "ast",
        "collections",
        "contextlib",
        "hashlib",
        "io",
        "json",
        "pathlib",
        "sys",
        "time",
        "__future__",
    }
    observed_import_roots = (
        set(imported_from)
        | {
            module.split(".")[0]
            for alias, module in imports.items()
            if alias not in {"F750", "M736", "K"}
        }
    )
    no_unlisted_import = observed_import_roots <= standard_imports
    header_pass = (
        pure_literal
        and tuple(ast.literal_eval(audit_tuple)) == AUDIT_INPUT_PATHS
        and isinstance(declared, ast.Name)
        and declared.id == "AUDIT_INPUT_PATHS"
        and AUDIT_TIMEOUT_SEC == 1800
        and NOTE_PATH
        == (
            "docs/MULTISOURCE_POSTIMAGE_LAW_CYCLE759_BOUNDED_"
            "THEOREM_NOTE_2026-07-28.md"
        )
        and supplier_imports == expected_imports
    )
    no_new_supplier = (
        supplier_imports == expected_imports
        and no_unlisted_import
        and module_roots == expected_roots
        and not quotient_constants
        and "frontier_cycle758_selector_multisource_2026_07_28"
        not in imports.values()
    )
    return {
        "header_pass": header_pass,
        "pure_literal_audit_tuple": pure_literal,
        "declared_is_audit_name":
            isinstance(declared, ast.Name)
            and declared.id == "AUDIT_INPUT_PATHS",
        "supplier_imports": supplier_imports,
        "no_unlisted_import": no_unlisted_import,
        "construction_module_roots": module_roots,
        "expected_construction_module_roots": expected_roots,
        "quotient_schema_constants": quotient_constants,
        "no_new_supplier": no_new_supplier,
        "construction_ast_sha256": digest_rows(ast_rows),
        "law_ast": {
            "postimage_residual": ast_rows["postimage_residual"],
            "quotient_postimage": ast_rows["quotient_postimage"],
        },
    }


def anchor_certificates() -> tuple[
    dict[str, object], tuple[tuple[int, ...], ...]
]:
    F750.PASS = F750.FAIL = 0
    captured = StringIO()
    with redirect_stdout(captured):
        single_source = F750.enforcement_candidate_census()
    f750 = {
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

    full = M736.configuration_census()
    configurations = full.pop("configurations")
    orbit = M736.invariant_full_orbit_certificate(configurations)
    m736 = {
        "direct_counts_by_k": full["direct_counts_by_k"],
        "direct_total": full["direct_total"],
        "agreement": full["agreement"],
        "configuration_mask_table_sha256":
            full["configuration_mask_table_sha256"],
        "orbit_configurations": orbit["orbit_configurations"],
        "pairwise_separated_sector_lawful":
            orbit["pairwise_separated_sector_lawful"],
        "composition_definition": orbit["composition_definition"],
        "failure_census": orbit["failure_census"],
        "ownership_labeling": (
            "M736 token_positions are the persistent external source labels; "
            "its full-orbit certificate checks ownership at every Q boundary."
        ),
    }
    return {
        "F750_single_source": f750,
        "M736_multisource": m736,
    }, configurations


def build_evaluation_cache(
    sampled_families: tuple[
        tuple[int, tuple[int, ...], tuple[tuple[int, ...], ...]], ...
    ],
    fixtures: tuple[tuple[object, ...], ...],
) -> dict[tuple[int, tuple[int, ...]], dict[str, object]]:
    configurations = tuple(
        sorted(
            {
                positions
                for _count, _representative, alternatives
                in sampled_families
                for positions in alternatives
            },
            key=lambda row: (len(row), row),
        )
    )
    return {
        (event, positions): evaluate_configuration(
            program, before, positions, FIXTURE_BANKS
        )
        for event, _direction, program, before, _expected in fixtures
        for positions in configurations
    }


def cycle758_boundary_certificate(
    sampled_families: tuple[
        tuple[int, tuple[int, ...], tuple[tuple[int, ...], ...]], ...
    ],
    fixtures: tuple[tuple[object, ...], ...],
    cache: dict[
        tuple[int, tuple[int, ...]], dict[str, object]
    ],
) -> dict[str, object]:
    selected_matrix = {}
    failed_conditions: Counter[str] = Counter()
    per_k = {
        str(count): {
            "family_epochs": 0,
            "unique_epochs": 0,
            "zero_survivor_epochs": 0,
            "tie_epochs": 0,
            "survivors": 0,
        }
        for count in range(1, M736.MAX_TOKEN_COUNT + 1)
    }
    for count, representative, alternatives in sampled_families:
        family = f"k{count}:{','.join(map(str, representative))}"
        selected_matrix[family] = []
        for event, _direction, _program, _before, _expected in fixtures:
            evaluations = tuple(
                cache[(event, positions)] for positions in alternatives
            )
            selected = tuple(
                row["positions"]
                for row in evaluations
                if all(row["conditions"].values())
            )
            for row in evaluations:
                for condition, passed in row["conditions"].items():
                    if not passed:
                        failed_conditions[condition] += 1
            selected_count = len(selected)
            selected_matrix[family].append(selected_count)
            aggregate = per_k[str(count)]
            aggregate["family_epochs"] += 1
            aggregate["unique_epochs"] += selected_count == 1
            aggregate["zero_survivor_epochs"] += selected_count == 0
            aggregate["tie_epochs"] += selected_count > 1
            aggregate["survivors"] += selected_count

    first = fixtures[0]
    family_failures = []
    configuration_failures = 0
    invariance_cases = 0
    for count, representative, alternatives in sampled_families:
        base = selected_with_landed_law(
            first[2], first[3], alternatives, FIXTURE_BANKS
        )
        for shift in range(RING_STATIONS):
            rotated_program = first[2][shift:] + first[2][:shift]
            observed = (
                base
                if shift == 0
                else selected_with_landed_law(
                    rotated_program,
                    first[3],
                    alternatives,
                    FIXTURE_BANKS,
                )
            )
            expected = tuple(
                sorted(
                    rotate_positions(positions, -shift)
                    for positions in base
                )
            )
            difference = len(set(observed) ^ set(expected))
            invariance_cases += 1
            configuration_failures += difference
            if observed != expected:
                family_failures.append(
                    {
                        "k": count,
                        "representative": representative,
                        "shift": shift,
                        "membership_failures": difference,
                    }
                )

    k2_positions = tuple(
        sorted(
            {
                positions
                for count, _representative, alternatives
                in sampled_families
                if count == 2
                for positions in alternatives
            }
        )
    )
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    twice = K.A.apply_semantic(
        K.A.apply_semantic(first[3], allocator), allocator
    )
    comparator_matches = sum(
        K.run_orbit(
            first[3], first[2], token_positions=positions
        )[0]
        == twice
        for positions in k2_positions
    )
    return {
        "definition": (
            "Cycle 758 is reproduced without importing it: exact M736 "
            "synchronous composition plus F750 rail-return, literal-inverse, "
            "and landed clean-postimage exclusions."
        ),
        "selected_count_matrix": selected_matrix,
        "failed_condition_census":
            dict(sorted(failed_conditions.items())),
        "per_k_totality": per_k,
        "invariance_family_cases": invariance_cases,
        "invariance_family_failure_count": len(family_failures),
        "invariance_configuration_failures": configuration_failures,
        "invariance_first_failure":
            family_failures[0] if family_failures else None,
        "k1_selected_every_epoch":
            selected_matrix.get("k1:0") == [1, 1, 1, 1],
        "k2_held_comparator": {
            "configurations": len(k2_positions),
            "allocator_squared_matches": comparator_matches,
        },
        "boundary_sha256": digest_rows(
            (
                selected_matrix,
                dict(sorted(failed_conditions.items())),
                per_k,
                family_failures,
            )
        ),
    }


def residual_characterization_census(
    k2_positions: tuple[tuple[int, ...], ...],
    fixtures: tuple[tuple[object, ...], ...],
    cache: dict[
        tuple[int, tuple[int, ...]], dict[str, object]
    ],
) -> dict[str, object]:
    rows = []
    all_signatures = []
    per_epoch = []
    lawful_updates = 0
    clean_updates = 0
    configuration_witness = None
    for event, direction, _program, _before, _expected in fixtures:
        counts: Counter[
            tuple[tuple[str, str, int, int], ...]
        ] = Counter(
            cache[(event, positions)]["residual"]
            for positions in k2_positions
        )
        signatures = tuple(counts)
        all_signatures.extend(
            cache[(event, positions)]["residual"]
            for positions in k2_positions
        )
        if len(signatures) > 1 and configuration_witness is None:
            left = next(
                positions
                for positions in k2_positions
                if cache[(event, positions)]["residual"]
                == signatures[0]
            )
            right = next(
                positions
                for positions in k2_positions
                if cache[(event, positions)]["residual"]
                != signatures[0]
            )
            configuration_witness = {
                "event": event,
                "direction": direction,
                "left_positions": left,
                "left_residual": cache[(event, left)]["residual"],
                "right_positions": right,
                "right_residual": cache[(event, right)]["residual"],
            }
        per_epoch.append(
            {
                "event": event,
                "direction": direction,
                "unique_structural_residues": len(counts),
                "uniform_across_44": len(counts) == 1,
                "signature_counts": tuple(
                    {
                        "residual": signature,
                        "count": count,
                    }
                    for signature, count in sorted(
                        counts.items(),
                        key=lambda item: (
                            -item[1],
                            compact(item[0]),
                        ),
                    )
                ),
            }
        )

    for positions in k2_positions:
        epochs = []
        for event, direction, _program, _before, _expected in fixtures:
            evaluation = cache[(event, positions)]
            other_conditions = tuple(
                passed
                for condition, passed in evaluation["conditions"].items()
                if condition != "clean_postimage"
            )
            lawful_updates += all(other_conditions)
            clean_updates += evaluation["conditions"]["clean_postimage"]
            epochs.append(
                {
                    "event": event,
                    "direction": direction,
                    "residual": evaluation["residual"],
                }
            )
        rows.append(
            {
                "source_labels": positions,
                "epochs": tuple(epochs),
            }
        )

    unique_global = tuple(
        sorted(set(all_signatures), key=compact)
    )
    uniform = len(unique_global) == 1
    return {
        "definition": (
            "Residual delta is the exact nonzero SOURCE_POINTER, named bank "
            "scratch-register, and unpacked link projection relative to the "
            "landed clean value zero.  Each source is labeled by its M736 "
            "initial token position."
        ),
        "configurations": len(k2_positions),
        "epochs_per_configuration": len(fixtures),
        "lawful_updates": lawful_updates,
        "clean_updates": clean_updates,
        "rows": tuple(rows),
        "per_epoch": tuple(per_epoch),
        "unique_global_structural_residues": len(unique_global),
        "uniform": uniform,
        "uniform_signature": unique_global[0] if uniform else None,
        "configuration_dependent": configuration_witness is not None,
        "first_configuration_dependence_witness":
            configuration_witness,
        "ownership_conclusion": (
            "No single landed-labeled register block can be assigned to the "
            "second source across this battery; deriving such an assignment "
            "would require a new supplier."
            if not uniform
            else (
                "The exact uniform block is eligible to be interpreted as "
                "additional-source bookkeeping."
            )
        ),
        "residual_table_sha256": digest_rows(rows),
    }


def law_definition_certificate(
    ast_audit: dict[str, object],
    residual: dict[str, object],
    sampled_families: tuple[
        tuple[int, tuple[int, ...], tuple[tuple[int, ...], ...]], ...
    ],
    fixtures: tuple[tuple[object, ...], ...],
    cache: dict[
        tuple[int, tuple[int, ...]], dict[str, object]
    ],
) -> dict[str, object]:
    k1_positions = tuple(
        sorted(
            {
                positions
                for count, _representative, alternatives
                in sampled_families
                if count == 1
                for positions in alternatives
            }
        )
    )
    reduction_cases = 0
    reduction_failures = 0
    for event, _direction, _program, _before, _expected in fixtures:
        for positions in k1_positions:
            observed = cache[(event, positions)]["residual"]
            reduction_cases += 1
            reduction_failures += (
                quotient_postimage(observed, ())
                != (not observed)
            )
    instantiated = bool(residual["uniform"])
    return {
        "candidate_schema": (
            "Let R(s) be postimage_residual(s) in landed K coordinates and "
            "let B_p be a source-owned bookkeeping block derived from the "
            "M736 source label p.  The corrected predicate is "
            "R(s) minus union_p B_p = empty.  No B_p may be introduced unless "
            "the exhaustive residual census supplies one uniform block."
        ),
        "ast": ast_audit["law_ast"],
        "landed_labeling_only": True,
        "new_numeric_or_string_constants_in_quotient_AST":
            ast_audit["quotient_schema_constants"],
        "derivation_gate": "residual.uniform",
        "gate_value": residual["uniform"],
        "law_instantiated": instantiated,
        "owned_bookkeeping_block":
            residual["uniform_signature"] if instantiated else None,
        "single_source_reduction": {
            "proof": (
                "A one-source state has no additional-source bookkeeping "
                "block.  Therefore R minus the empty set equals R, exactly "
                "the landed clean-postimage predicate."
            ),
            "cases": reduction_cases,
            "failures": reduction_failures,
            "structural_identity": "R\\emptyset=R",
        },
        "blocked_reason": (
            None
            if instantiated
            else (
                "The register/content residue is configuration-dependent; "
                "choosing an owned quotient would derive the law by fiat."
            )
        ),
    }


def corrected_retests(
    residual: dict[str, object],
    sampled_families: tuple[
        tuple[int, tuple[int, ...], tuple[tuple[int, ...], ...]], ...
    ],
    fixtures: tuple[tuple[object, ...], ...],
    cache: dict[
        tuple[int, tuple[int, ...]], dict[str, object]
    ],
    boundary: dict[str, object],
) -> tuple[dict[str, object], dict[str, object]]:
    if not residual["uniform"]:
        k2 = {
            "status": "NOT_RUN_RESIDUAL_NONUNIFORM",
            "reason": (
                "The derived-law precondition is false; no corrected law "
                "exists to retest."
            ),
            "baseline_selected_count_matrix": {
                key: value
                for key, value
                in boundary["selected_count_matrix"].items()
                if key.startswith("k2:")
            },
            "baseline_total_configurations": 44,
            "baseline_comparator":
                boundary["k2_held_comparator"],
            "corrected_totality": None,
            "corrected_invariance": None,
            "corrected_identification": None,
        }
        k3 = {
            "status": "NOT_RUN_RESIDUAL_NONUNIFORM",
            "reason": (
                "A k=3 quotient cannot be extrapolated from a non-uniform "
                "k=2 residue."
            ),
            "baseline_selected_count_matrix": {
                "k3:0,2,4":
                    boundary["selected_count_matrix"]["k3:0,2,4"]
            },
            "baseline_finding": (
                "The Cycle-758 declared k=3 family retains the landed "
                "three-way tie in event 0; no corrected-law finding is made."
            ),
            "corrected_tie_resolved_persisted_or_changed": None,
        }
        return k2, k3

    owned = residual["uniform_signature"]
    matrices = {}
    for count in (1, 2, 3):
        for observed, representative, alternatives in sampled_families:
            if observed != count:
                continue
            key = f"k{count}:{','.join(map(str, representative))}"
            matrices[key] = []
            for event, _direction, _program, _before, _expected in fixtures:
                selected = tuple(
                    positions
                    for positions in alternatives
                    if all(
                        passed
                        for condition, passed
                        in cache[(event, positions)]["conditions"].items()
                        if condition != "clean_postimage"
                    )
                    and quotient_postimage(
                        cache[(event, positions)]["residual"],
                        () if count == 1 else owned,
                    )
                )
                matrices[key].append(selected)
    k2_matrices = {
        key: value for key, value in matrices.items()
        if key.startswith("k2:")
    }
    k2_total = all(
        len(selected) == 1
        for rows in k2_matrices.values()
        for selected in rows
    )
    k3_rows = matrices["k3:0,2,4"]
    baseline_k3 = boundary["selected_count_matrix"]["k3:0,2,4"]
    corrected_counts = [len(selected) for selected in k3_rows]
    return {
        "status": "RUN",
        "selected": k2_matrices,
        "corrected_totality": k2_total,
        "corrected_invariance": None,
        "corrected_identification": None,
    }, {
        "status": "RUN",
        "baseline_counts": baseline_k3,
        "corrected_counts": corrected_counts,
        "corrected_tie_resolved_persisted_or_changed": (
            "resolved"
            if baseline_k3[0] > 1 and corrected_counts[0] == 1
            else (
                "persisted"
                if baseline_k3[0] > 1 and corrected_counts[0] > 1
                else "changed"
            )
        ),
    }


def outcome_certificate(
    residual: dict[str, object],
    law: dict[str, object],
    k2_retest: dict[str, object],
    k3_retest: dict[str, object],
) -> dict[str, object]:
    if not residual["uniform"]:
        outcome = "RESIDUAL_NON_UNIFORM"
        statement = (
            "The named k>=2 correction route stops at its derivation gate: "
            "the exact two-source postimage residue is configuration-dependent "
            "on the full Cycle-758 battery, so no per-source quotient is "
            "available without a new supplier."
        )
    elif law["single_source_reduction"]["failures"]:
        outcome = "CORRECTION_BREAKS_SINGLE_SOURCE_REDUCTION"
        statement = (
            "The candidate quotient fails to reduce to the landed one-source "
            "law; the clean-postimage veto is load-bearing beyond bookkeeping."
        )
    elif (
        k2_retest["corrected_totality"]
        and k2_retest["corrected_invariance"]
        and k2_retest["corrected_identification"]
    ):
        outcome = "DERIVED_CORRECTION_SUCCEEDS"
        statement = (
            "The derived quotient selects multisource actuality on the "
            "declared exhaustive k=2 ring-11 sector."
        )
    else:
        outcome = "DERIVED_CORRECTION_RETEST_FAILS"
        statement = (
            "A uniform correction was derivable but did not pass the complete "
            "k=2 selector battery."
        )
    keys = {
        "derived_correction_succeeds":
            outcome == "DERIVED_CORRECTION_SUCCEEDS",
        "residual_non_uniform":
            outcome == "RESIDUAL_NON_UNIFORM",
        "correction_breaks_single_source_reduction":
            outcome == "CORRECTION_BREAKS_SINGLE_SOURCE_REDUCTION",
        "correction_retest_fails":
            outcome == "DERIVED_CORRECTION_RETEST_FAILS",
        "quotient_instantiated": law["law_instantiated"],
        "k2_corrected_retest_run": k2_retest["status"] == "RUN",
        "k3_corrected_retest_run": k3_retest["status"] == "RUN",
        "cycle750_single_source_scope_unchanged": True,
        "cycle754_scope_unchanged": True,
        "ring11_only": True,
        "pairwise_separated_only": True,
        "program_and_genesis_supplied": True,
        "higher_k_scope_extended": False,
        "w3_closed": False,
    }
    return {
        "outcome": outcome,
        "statement": statement,
        "honest_boundary_keys": keys,
        "scope_statement": (
            "The result is a frozen obstruction on the supplied ring-11, "
            "two-bank Cycle-750 epoch battery.  It neither changes the "
            "Cycle-750 single-source theorem nor any Cycle-754 scope, and it "
            "makes no multisource actuality, arbitrary-ring, renewal, or W3 "
            "closure claim."
        ),
    }


def main() -> int:
    started = monotonic()

    ast_audit = header_and_ast_audit()
    check(
        "A_header_literal_inputs_exact_imports",
        ast_audit["header_pass"],
    )

    anchors, configurations = anchor_certificates()
    check(
        "A_anchors_F750_single_source_and_M736_multisource",
        anchors["F750_single_source"]["fixtures_exhausted"] == 38
        and anchors["F750_single_source"]["alternatives_exhausted"]
        == 2578
        and anchors["F750_single_source"]["selected_count_range"]
        == [1, 1]
        and anchors["F750_single_source"]["tests"]
        == {
            "totality": True,
            "invariance": True,
            "identification": True,
        }
        and anchors["F750_single_source"][
            "internal_check_failures"
        ]
        == 0
        and anchors["M736_multisource"]["agreement"]
        and anchors["M736_multisource"]["direct_counts_by_k"]
        == M736.EXPECTED_COUNTS_BY_K
        and anchors["M736_multisource"]["direct_total"]
        == M736.EXPECTED_TOTAL_CONFIGURATIONS
        and anchors["M736_multisource"][
            "orbit_configurations"
        ]
        == 199
        and anchors["M736_multisource"][
            "pairwise_separated_sector_lawful"
        ]
        and not any(
            anchors["M736_multisource"]["failure_census"].values()
        ),
    )

    sampled_families, strata = build_cycle758_sample(configurations)
    fixtures = F750.k_epoch_fixtures(FIXTURE_BANKS)
    cache = build_evaluation_cache(sampled_families, fixtures)
    boundary = cycle758_boundary_certificate(
        sampled_families, fixtures, cache
    )
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
    check(
        "A_cycle758_boundary_and_veto_reproduced",
        strata["full_configuration_counts_by_k"]
        == {0: 1, 1: 11, 2: 44, 3: 77, 4: 55, 5: 11}
        and strata["full_translation_family_counts_by_k"]
        == {0: 1, 1: 1, 2: 4, 3: 7, 4: 5, 5: 1}
        and strata["selected_configuration_counts_by_k"]
        == {0: 1, 1: 11, 2: 44, 3: 11, 4: 11, 5: 11}
        and strata["selected_translation_family_counts_by_k"]
        == {0: 1, 1: 1, 2: 4, 3: 1, 4: 1, 5: 1}
        and strata["selected_nonvacuum_configurations"] == 88
        and strata["translation_complete"]
        and boundary["selected_count_matrix"] == expected_matrix
        and boundary["failed_condition_census"]
        == {"clean_postimage": 344}
        and boundary["invariance_family_cases"] == 88
        and boundary["invariance_family_failure_count"] == 9
        and boundary["invariance_configuration_failures"] == 27
        and boundary["k2_held_comparator"]
        == {
            "configurations": 44,
            "allocator_squared_matches": 44,
        },
    )

    k2_positions = tuple(
        M736.occupied_sites(config)
        for config in configurations
        if sum(config) == 2
    )
    residual = residual_characterization_census(
        k2_positions, fixtures, cache
    )
    check(
        "B_residual_census_all_44_all_epochs_exact_and_lawful",
        residual["configurations"] == 44
        and residual["epochs_per_configuration"] == 4
        and residual["lawful_updates"] == 176
        and residual["clean_updates"] == 0
        and len(residual["rows"]) == 44
        and all(
            len(row["epochs"]) == 4 for row in residual["rows"]
        )
        and all(
            coordinate[3] == 1
            for row in residual["rows"]
            for epoch in row["epochs"]
            for coordinate in epoch["residual"]
        ),
    )
    check(
        "B_residual_is_configuration_dependent_not_uniform",
        not residual["uniform"]
        and residual["configuration_dependent"]
        and residual["uniform_signature"] is None
        and residual["first_configuration_dependence_witness"]
        is not None
        and tuple(
            row["uniform_across_44"] for row in residual["per_epoch"]
        )
        == (True, True, False, False)
        and tuple(
            row["unique_structural_residues"]
            for row in residual["per_epoch"]
        )
        == (1, 1, 12, 14),
    )

    law = law_definition_certificate(
        ast_audit,
        residual,
        sampled_families,
        fixtures,
        cache,
    )
    check(
        "C_corrected_law_AST_gate_and_single_source_reduction",
        law["landed_labeling_only"]
        and not law[
            "new_numeric_or_string_constants_in_quotient_AST"
        ]
        and law["derivation_gate"] == "residual.uniform"
        and not law["gate_value"]
        and not law["law_instantiated"]
        and law["owned_bookkeeping_block"] is None
        and law["single_source_reduction"]["cases"] == 44
        and law["single_source_reduction"]["failures"] == 0
        and law["blocked_reason"] is not None,
    )

    k2_retest, k3_retest = corrected_retests(
        residual,
        sampled_families,
        fixtures,
        cache,
        boundary,
    )
    check(
        "D_k2_retest_honestly_precondition_blocked",
        k2_retest["status"] == "NOT_RUN_RESIDUAL_NONUNIFORM"
        and k2_retest["baseline_total_configurations"] == 44
        and all(
            counts == [0, 0, 0, 0]
            for counts
            in k2_retest[
                "baseline_selected_count_matrix"
            ].values()
        )
        and k2_retest["baseline_comparator"]
        == {
            "configurations": 44,
            "allocator_squared_matches": 44,
        }
        and k2_retest["corrected_totality"] is None
        and k2_retest["corrected_invariance"] is None
        and k2_retest["corrected_identification"] is None,
    )
    check(
        "E_k3_retest_honestly_precondition_blocked_tie_frozen",
        k3_retest["status"]
        == "NOT_RUN_RESIDUAL_NONUNIFORM"
        and k3_retest["baseline_selected_count_matrix"]
        == {"k3:0,2,4": [3, 0, 0, 1]}
        and k3_retest[
            "corrected_tie_resolved_persisted_or_changed"
        ]
        is None,
    )

    check(
        "F_no_new_supplier_audit",
        ast_audit["no_new_supplier"]
        and ast_audit["supplier_imports"]
        == {
            "F750":
                "frontier_cycle750_actual_selector_stretch_2026_07_28",
            "M736":
                "frontier_cycle736_pairwise_separated_multisource_2026_07_28",
            "K":
                "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        },
    )

    outcome = outcome_certificate(
        residual, law, k2_retest, k3_retest
    )
    keys = outcome["honest_boundary_keys"]
    check(
        "G_honest_nonuniform_outcome_and_scopes_untouched",
        outcome["outcome"] == "RESIDUAL_NON_UNIFORM"
        and not keys["derived_correction_succeeds"]
        and keys["residual_non_uniform"]
        and not keys[
            "correction_breaks_single_source_reduction"
        ]
        and not keys["correction_retest_fails"]
        and not keys["quotient_instantiated"]
        and not keys["k2_corrected_retest_run"]
        and not keys["k3_corrected_retest_run"]
        and keys["cycle750_single_source_scope_unchanged"]
        and keys["cycle754_scope_unchanged"]
        and keys["ring11_only"]
        and keys["pairwise_separated_only"]
        and keys["program_and_genesis_supplied"]
        and not keys["higher_k_scope_extended"]
        and not keys["w3_closed"],
    )

    elapsed = monotonic() - started
    check(
        "H_bounded_runtime_and_note_not_required",
        elapsed < AUDIT_TIMEOUT_SEC and NOTE_PATH.endswith(".md"),
    )

    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "anchors": anchors,
        "ast_audit": ast_audit,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "corrected_law": law,
        "cycle758_boundary": boundary,
        "k2_retest": k2_retest,
        "k3_retest": k3_retest,
        "outcome": outcome,
        "pass": all(CHECKS.values()),
        "residual_characterization": residual,
        "runtime_seconds": round(elapsed, 6),
        "sampled_strata": strata,
        "terminal": (
            "CYCLE759_MULTISOURCE_POSTIMAGE_LAW_PASS"
            if all(CHECKS.values())
            else "CYCLE759_MULTISOURCE_POSTIMAGE_LAW_HONEST_FAIL"
        ),
    }
    preliminary = compact(report)
    projected = (
        "\n".join(OUTPUT_LINES).encode("utf-8")
    )
    check(
        "I_stdout_under_150KB",
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
        "CYCLE759_MULTISOURCE_POSTIMAGE_LAW_PASS"
        if report["pass"]
        else "CYCLE759_MULTISOURCE_POSTIMAGE_LAW_HONEST_FAIL"
    )
    report["report_sha256"] = sha256(
        compact(report).encode("utf-8")
    ).hexdigest()
    final_json = compact(report)
    output = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", len(output.encode("utf-8")))
        )
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
