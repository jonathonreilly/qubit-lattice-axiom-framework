#!/usr/bin/env python3
"""Cycle 760 independent checker for the scaled derived comparison."""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/SCALED_DERIVED_COMPARISON_CYCLE760_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle757_derived_occurrence_calibration_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path
import sys
from time import perf_counter
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle758_selector_multisource_2026_07_28 as S758
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle757_derived_occurrence_calibration_2026_07_28 as C757


PRIMARY_PATH = (
    "scripts/frontier_cycle760_scaled_derived_comparison_2026_07_28.py"
)
BLOCKLIST = (
    "scripts/frontier_cycle760_scaled_derived_comparison_2026_07_28.py",
)
STDOUT_LIMIT_BYTES = 150 * 1024
BANK_COUNTS = (2, 5, 12)
EXPECTED_FAMILY_BY_BANK = {2: 44, 5: 350, 12: 2184}
EXPECTED_FAMILY_TOTAL = 2578
EXPECTED_CENSUS = (845, 878, 855)
EXPECTED_SIMPLEX = (
    Fraction(845, 2578),
    Fraction(439, 1289),
    Fraction(855, 2578),
)
EXPECTED_BORN_DISAGREEMENTS = (2, 3, 3, 3)
EXPECTED_C757_DISAGREEMENTS = (2, 2, 3, 3)
EXPECTED_SPLITS = ((390, 424, 475), (455, 454, 380))
EXPECTED_TOTAL_VARIATION = Fraction(95, 1289)
EXPECTED_BOUNDARY_KEYS = (
    "asymptotic_convergence_claimed",
    "born_law_selected",
    "comparison_only",
    "family_exhaustive_within_landed_k1_fixture_scope",
    "mapping_convention_derived",
    "mapping_convention_supplied",
    "sample_size_bound",
    "sample_size_finite",
    "simplex_promoted_to_weight",
    "split_stability_role",
    "verdict_table",
    "verdict_table_role",
    "weight_claim_made",
)
EXPECTED_LIVE_READINGS = (
    "2,578 k=1 families are larger but finite",
    "the outcome-class mapping remains supplied",
    "neither the census nor split comparison is a weight claim.",
)
EXPECTED_BOUNDARY_LINE = (
    "BOUNDARY HONEST CEILING :: "
    "2,578 k=1 families are larger but finite; the outcome-class "
    "mapping remains supplied, and neither the census nor split "
    "comparison is a weight claim."
)


OUTPUT_LINES: list[str] = []
CHECKS: dict[str, bool] = {}


def compact(value: object) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )


def record(label: str, passed: bool, detail: object) -> None:
    CHECKS[label] = bool(passed)
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )


def _top_assignments(tree: ast.Module) -> dict[str, ast.AST]:
    assignments: dict[str, ast.AST] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name):
                assignments[node.target.id] = node.value
    return assignments


def _literal_assignment(
    assignments: dict[str, ast.AST], name: str
) -> object:
    return ast.literal_eval(assignments[name])


def _function(tree: ast.Module, name: str) -> ast.FunctionDef:
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    raise KeyError(name)


def _boundary_data(
    tree: ast.Module,
) -> tuple[tuple[str, ...], dict[str, object], str]:
    function = _function(tree, "boundary_certificate")
    boundary_node: ast.Dict | None = None
    boundary_line = ""
    for node in ast.walk(function):
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "boundary"
            for target in node.targets
        ):
            if isinstance(node.value, ast.Dict):
                boundary_node = node.value
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "OUTPUT_LINES"
            and node.func.attr == "append"
            and len(node.args) == 1
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
            and node.args[0].value.startswith("BOUNDARY HONEST CEILING")
        ):
            boundary_line = node.args[0].value
    if boundary_node is None:
        raise ValueError("primary boundary dictionary not found")

    keys = tuple(ast.literal_eval(key) for key in boundary_node.keys)
    values: dict[str, object] = {}
    for key_node, value_node in zip(
        boundary_node.keys, boundary_node.values, strict=True
    ):
        key = ast.literal_eval(key_node)
        try:
            values[key] = ast.literal_eval(value_node)
        except (ValueError, TypeError):
            values[key] = {"expression": ast.unparse(value_node)}
    return keys, values, boundary_line


def _dict_key_literal_values(
    tree: ast.Module, requested_key: str
) -> tuple[object, ...]:
    values = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for key_node, value_node in zip(
            node.keys, node.values, strict=True
        ):
            try:
                key = ast.literal_eval(key_node)
            except (ValueError, TypeError):
                continue
            if key != requested_key:
                continue
            try:
                values.append(ast.literal_eval(value_node))
            except (ValueError, TypeError):
                values.append({"expression": ast.unparse(value_node)})
    return tuple(values)


def extraction() -> tuple[dict[str, object], ast.Module, str]:
    primary_source = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    primary_tree = ast.parse(primary_source, filename=PRIMARY_PATH)
    assignments = _top_assignments(primary_tree)
    primary_audit_paths = _literal_assignment(
        assignments, "AUDIT_INPUT_PATHS"
    )
    family_by_bank = _literal_assignment(
        assignments, "EXPECTED_FAMILY_COUNTS"
    )
    family_total = _literal_assignment(
        assignments, "EXPECTED_FAMILY_TOTAL"
    )
    census = _literal_assignment(assignments, "EXPECTED_DERIVED_COUNTS")
    splits = _literal_assignment(assignments, "EXPECTED_SPLIT_COUNTS")
    boundary_keys, boundary_values, boundary_line = _boundary_data(
        primary_tree
    )
    simplex = tuple(Fraction(count, family_total) for count in census)
    primary_expected_inputs = (
        "scripts/frontier_cycle757_derived_occurrence_calibration_2026_07_28.py",
        "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
        "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    )
    detail = {
        "audit_literal_eval": primary_audit_paths,
        "banks": family_by_bank,
        "born_disagreements": EXPECTED_BORN_DISAGREEMENTS,
        "boundary_keys": boundary_keys,
        "census": census,
        "cycle757_disagreements": EXPECTED_C757_DISAGREEMENTS,
        "family_size": family_total,
        "simplex": tuple(str(value) for value in simplex),
        "splits": splits,
        "total_variation": str(EXPECTED_TOTAL_VARIATION),
        "weight_claim_made": False,
    }
    passed = (
        primary_audit_paths == primary_expected_inputs
        and isinstance(assignments["AUDIT_INPUT_PATHS"], ast.Tuple)
        and family_by_bank == EXPECTED_FAMILY_BY_BANK
        and family_total == EXPECTED_FAMILY_TOTAL
        and census == EXPECTED_CENSUS
        and simplex == EXPECTED_SIMPLEX
        and splits == EXPECTED_SPLITS
        and boundary_keys == EXPECTED_BOUNDARY_KEYS
        and boundary_values["weight_claim_made"] is False
        and boundary_values["mapping_convention_supplied"] is True
        and boundary_values["mapping_convention_derived"] is False
        and boundary_values["simplex_promoted_to_weight"] is False
        and boundary_values["born_law_selected"] is False
        and boundary_line == EXPECTED_BOUNDARY_LINE
    )
    record("extraction", passed, detail)
    return detail, primary_tree, primary_source


def _s758_k1_stratum() -> tuple[tuple[int, ...], ...]:
    configurations = tuple(
        tuple(
            int(index == position)
            for index in range(S758.RING_STATIONS)
        )
        for position in range(S758.RING_STATIONS)
    )
    return S758.configuration_families(configurations)[1][(0,)]


def family_recount() -> tuple[
    tuple[dict[str, int], ...], dict[str, object]
]:
    k1_stratum = _s758_k1_stratum()
    family: list[dict[str, int]] = []
    family_by_bank: Counter[int] = Counter()
    fixture_by_bank: Counter[int] = Counter()
    program_lengths: dict[int, set[int]] = {
        bank_count: set() for bank_count in BANK_COUNTS
    }
    unique_base_survivors = True
    configuration_evaluations = 0
    fixture_ordinal = 0
    global_ordinal = 0

    for bank_count in BANK_COUNTS:
        fixtures = F750.k_epoch_fixtures(bank_count)
        fixture_by_bank[bank_count] = len(fixtures)
        for event, _direction, program, before, expected in fixtures:
            station_count = len(program)
            program_lengths[bank_count].add(station_count)
            scalar_alternatives = tuple(range(station_count))
            f750_selected = F750.enforcement_lineage_selector(
                program,
                before,
                expected,
                bank_count,
                scalar_alternatives,
            )
            configuration_evaluations += len(scalar_alternatives)
            unique_base_survivors &= f750_selected == (0,)

            if len(f750_selected) == 1:
                base_selected = f750_selected[0]
                for shift in range(station_count):
                    selected = (
                        base_selected - shift
                    ) % station_count
                    family.append(
                        {
                            "alternative_count": station_count,
                            "bank_count": bank_count,
                            "fixture_event": event,
                            "fixture_ordinal": fixture_ordinal,
                            "global_epoch_ordinal": global_ordinal,
                            "program_shift": shift,
                            "selected_alternative": selected,
                        }
                    )
                    family_by_bank[bank_count] += 1
                    global_ordinal += 1
            fixture_ordinal += 1

    detail = {
        "banks": dict(sorted(family_by_bank.items())),
        "construction": "S758 k=1 translation stratum x F750 survivor",
        "configuration_evaluations": configuration_evaluations,
        "fixtures": dict(sorted(fixture_by_bank.items())),
        "k1_stratum": k1_stratum,
        "program_lengths": {
            bank_count: tuple(sorted(lengths))
            for bank_count, lengths in program_lengths.items()
        },
        "total": len(family),
        "weight_claim_made": False,
    }
    passed = (
        k1_stratum
        == tuple((position,) for position in range(S758.RING_STATIONS))
        and S758.RING_STATIONS == 11
        and unique_base_survivors
        and dict(family_by_bank) == EXPECTED_FAMILY_BY_BANK
        and len(family) == EXPECTED_FAMILY_TOTAL
        and configuration_evaluations == EXPECTED_FAMILY_TOTAL
        and dict(fixture_by_bank) == {2: 4, 5: 10, 12: 24}
        and {
            bank_count: tuple(sorted(lengths))
            for bank_count, lengths in program_lengths.items()
        }
        == {2: (11,), 5: (35,), 12: (91,)}
        and all(
            row["selected_alternative"]
            == (
                row["alternative_count"] - row["program_shift"]
            )
            % row["alternative_count"]
            for row in family
        )
    )
    record("family_recount", passed, detail)
    return tuple(family), detail


def _map_family(
    family: tuple[dict[str, int], ...],
) -> tuple[tuple[dict[str, object], ...], tuple[int, ...]]:
    mapped = []
    counts = [0] * len(C757.EFFECT_IDS)
    for row in family:
        outcome_index = (
            row["global_epoch_ordinal"]
            + row["selected_alternative"]
        ) % len(C757.EFFECT_IDS)
        counts[outcome_index] += 1
        mapped.append(
            {
                **row,
                "effect_id": C757.EFFECT_IDS[outcome_index],
                "outcome_index": outcome_index,
            }
        )
    return tuple(mapped), tuple(counts)


def _comparison_table(
    simplex: tuple[Fraction, ...],
    candidate: tuple[float, ...],
    tolerances: tuple[float, ...],
) -> tuple[dict[str, object], ...]:
    table = []
    for tolerance in tolerances:
        effect_rows = []
        for effect_id, empirical, held in zip(
            C757.EFFECT_IDS, simplex, candidate, strict=True
        ):
            residual = float(empirical) - held
            effect_rows.append(
                {
                    "effect_id": effect_id,
                    "empirical": str(empirical),
                    "held_candidate": held,
                    "residual_hex": residual.hex(),
                    "verdict": (
                        "agreement"
                        if abs(residual) <= tolerance
                        else "disagreement"
                    ),
                }
            )
        disagreements = sum(
            row["verdict"] == "disagreement" for row in effect_rows
        )
        table.append(
            {
                "aggregate": (
                    "agreement"
                    if disagreements == 0
                    else "disagreement"
                ),
                "disagreement_count": disagreements,
                "effect_rows": tuple(effect_rows),
                "tolerance": tolerance,
            }
        )
    return tuple(table)


def _cycle757_baseline_counts(
    family: tuple[dict[str, int], ...],
) -> tuple[int, ...]:
    first_by_fixture: dict[int, dict[str, int]] = {}
    for row in family:
        first_by_fixture.setdefault(row["fixture_ordinal"], row)
    counts = [0] * len(C757.EFFECT_IDS)
    for fixture_ordinal, row in sorted(first_by_fixture.items()):
        outcome_index = (
            fixture_ordinal + row["selected_alternative"]
        ) % len(C757.EFFECT_IDS)
        counts[outcome_index] += 1
    return tuple(counts)


def census_recount(
    family: tuple[dict[str, int], ...],
) -> tuple[
    tuple[dict[str, object], ...],
    tuple[Fraction, ...],
    tuple[float, ...],
    tuple[dict[str, object], ...],
    dict[str, object],
]:
    mapped, counts = _map_family(family)
    simplex = tuple(
        Fraction(count, len(mapped)) for count in counts
    )
    effects, captured = C757._landed_contact_trine()
    held_candidate = C757._trace_candidate(effects)
    tolerances = tuple(C757.C748.TOLERANCE_LADDER)
    born_table = _comparison_table(
        simplex, held_candidate, tolerances
    )
    born_disagreements = tuple(
        row["disagreement_count"] for row in born_table
    )

    baseline_counts = _cycle757_baseline_counts(family)
    baseline_simplex = tuple(
        Fraction(count, sum(baseline_counts))
        for count in baseline_counts
    )
    baseline_table = _comparison_table(
        baseline_simplex, held_candidate, tolerances
    )
    baseline_disagreements = tuple(
        row["disagreement_count"] for row in baseline_table
    )

    _port_rows, port_empirical = C757._receive_mapped_family(
        "cycle760-independent-check",
        mapped,
    )
    machinery_table = C757._comparison_table(
        port_empirical, held_candidate
    )
    paired_table = tuple(
        {
            "cycle757_38_epoch": {
                "aggregate": baseline["aggregate"],
                "disagreement_count":
                    baseline["disagreement_count"],
            },
            "cycle760_scaled": {
                "aggregate": current["aggregate"],
                "disagreement_count":
                    current["disagreement_count"],
            },
            "tolerance": current["tolerance"],
        }
        for current, baseline in zip(
            born_table, baseline_table, strict=True
        )
    )
    detail = {
        "born_held_candidate_hex": tuple(
            value.hex() for value in held_candidate
        ),
        "census": counts,
        "cycle757_census": baseline_counts,
        "paired_table": paired_table,
        "simplex": tuple(str(value) for value in simplex),
        "simplex_sum": str(
            sum(simplex, start=Fraction(0, 1))
        ),
        "typed_receiver_agrees": (
            port_empirical.counts == counts
            and port_empirical.simplex == simplex
            and machinery_table == born_table
        ),
        "weight_claim_made": False,
    }
    passed = (
        len(mapped) == EXPECTED_FAMILY_TOTAL
        and counts == EXPECTED_CENSUS
        and simplex == EXPECTED_SIMPLEX
        and sum(simplex, start=Fraction(0, 1))
        == Fraction(1, 1)
        and baseline_counts == C757.EXPECTED_DERIVED_COUNTS
        == (13, 13, 12)
        and tolerances == (0.06, 0.02, 0.002, 0.001)
        and born_disagreements == EXPECTED_BORN_DISAGREEMENTS
        and baseline_disagreements
        == EXPECTED_C757_DISAGREEMENTS
        and tuple(value.hex() for value in held_candidate)
        == C757.C748.FROZEN_HELD_CANDIDATE_HEX
        and captured.count("PASS ") == 4
        and "FAIL " not in captured
        and port_empirical.counts == counts
        and port_empirical.simplex == simplex
        and machinery_table == born_table
        and all(
            row["effect_id"]
            == C757.EFFECT_IDS[row["outcome_index"]]
            and row["outcome_index"]
            == (
                row["global_epoch_ordinal"]
                + row["selected_alternative"]
            )
            % len(C757.EFFECT_IDS)
            for row in mapped
        )
    )
    record("census_recount", passed, detail)
    return mapped, simplex, held_candidate, born_table, detail


def uniformity_probe(
    simplex: tuple[Fraction, ...],
    born_table: tuple[dict[str, object], ...],
) -> dict[str, object]:
    tolerances = tuple(C757.C748.TOLERANCE_LADDER)
    uniform_candidate = (1.0 / 3.0,) * len(simplex)
    uniform_table = _comparison_table(
        simplex, uniform_candidate, tolerances
    )
    table = tuple(
        {
            "born_disagreements": born["disagreement_count"],
            "fits_better_by_disagreement_count": (
                "uniform"
                if uniform["disagreement_count"]
                < born["disagreement_count"]
                else (
                    "born"
                    if born["disagreement_count"]
                    < uniform["disagreement_count"]
                    else "tie"
                )
            ),
            "tolerance": tolerance,
            "uniform_disagreements":
                uniform["disagreement_count"],
        }
        for tolerance, born, uniform in zip(
            tolerances, born_table, uniform_table, strict=True
        )
    )
    expected_table = (
        {
            "born_disagreements": 2,
            "fits_better_by_disagreement_count": "uniform",
            "tolerance": 0.06,
            "uniform_disagreements": 0,
        },
        {
            "born_disagreements": 3,
            "fits_better_by_disagreement_count": "uniform",
            "tolerance": 0.02,
            "uniform_disagreements": 0,
        },
        {
            "born_disagreements": 3,
            "fits_better_by_disagreement_count": "uniform",
            "tolerance": 0.002,
            "uniform_disagreements": 2,
        },
        {
            "born_disagreements": 3,
            "fits_better_by_disagreement_count": "tie",
            "tolerance": 0.001,
            "uniform_disagreements": 3,
        },
    )
    detail = {
        "comparison_only_no_law_claim": True,
        "table": table,
        "uniform_simplex": ("1/3", "1/3", "1/3"),
        "weight_claim_made": False,
    }
    passed = (
        table == expected_table
        and tuple(
            row["disagreement_count"] for row in uniform_table
        )
        == (0, 0, 2, 3)
    )
    record(
        "uniformity_probe THE UNIFORMITY-PROBE TABLE",
        passed,
        detail,
    )
    return detail


def split_recount(
    family: tuple[dict[str, int], ...],
) -> dict[str, object]:
    split_at = len(family) // 2
    _first_mapped, first_counts = _map_family(family[:split_at])
    _second_mapped, second_counts = _map_family(family[split_at:])
    first_simplex = tuple(
        Fraction(count, split_at) for count in first_counts
    )
    second_simplex = tuple(
        Fraction(count, len(family) - split_at)
        for count in second_counts
    )
    differences = tuple(
        first - second
        for first, second in zip(
            first_simplex, second_simplex, strict=True
        )
    )
    total_variation = (
        sum(
            (abs(value) for value in differences),
            start=Fraction(0, 1),
        )
        / 2
    )
    split_table = _comparison_table(
        first_simplex,
        tuple(float(value) for value in second_simplex),
        tuple(C757.C748.TOLERANCE_LADDER),
    )
    detail = {
        "first": {
            "census": first_counts,
            "simplex": tuple(
                str(value) for value in first_simplex
            ),
        },
        "first_minus_second": tuple(
            str(value) for value in differences
        ),
        "sample_sizes": (split_at, len(family) - split_at),
        "second": {
            "census": second_counts,
            "simplex": tuple(
                str(value) for value in second_simplex
            ),
        },
        "split_disagreements": tuple(
            row["disagreement_count"] for row in split_table
        ),
        "total_variation": str(total_variation),
        "weight_claim_made": False,
    }
    passed = (
        (first_counts, second_counts) == EXPECTED_SPLITS
        and split_at == len(family) - split_at == 1289
        and sum(first_simplex, start=Fraction(0, 1))
        == Fraction(1, 1)
        and sum(second_simplex, start=Fraction(0, 1))
        == Fraction(1, 1)
        and total_variation == EXPECTED_TOTAL_VARIATION
        and tuple(
            row["disagreement_count"] for row in split_table
        )
        == (1, 3, 3, 3)
    )
    record("split_recount", passed, detail)
    return detail


def _weight_flags(value: object) -> tuple[object, ...]:
    found: list[object] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "weight_claim_made":
                found.append(child)
            found.extend(_weight_flags(child))
    elif isinstance(value, (tuple, list)):
        for child in value:
            found.extend(_weight_flags(child))
    return tuple(found)


def discipline(
    primary_tree: ast.Module,
    primary_source: str,
    certificates: tuple[dict[str, object], ...],
) -> dict[str, object]:
    checker_source = Path(__file__).read_text(encoding="utf-8")
    checker_tree = ast.parse(checker_source, filename=str(Path(__file__)))
    assignments = _top_assignments(checker_tree)
    audit_node = assignments["AUDIT_INPUT_PATHS"]
    audit_literal = (
        isinstance(audit_node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_node.elts
        )
    )
    imported_modules = tuple(
        alias.name
        for node in checker_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
    )
    blocked_module = Path(BLOCKLIST[0]).stem
    blocked_imports = tuple(
        name for name in imported_modules if name == blocked_module
    )
    imported_attribute_writes = []
    import_aliases = {"S758", "F750", "C757"}
    for node in ast.walk(checker_tree):
        if not isinstance(
            node, (ast.Assign, ast.AnnAssign, ast.AugAssign)
        ):
            continue
        targets = (
            node.targets
            if isinstance(node, ast.Assign)
            else (node.target,)
        )
        for target in targets:
            root = target
            while isinstance(root, ast.Attribute):
                root = root.value
            if (
                isinstance(target, ast.Attribute)
                and isinstance(root, ast.Name)
                and root.id in import_aliases
            ):
                imported_attribute_writes.append(ast.unparse(target))

    primary_weight_values = _dict_key_literal_values(
        primary_tree, "weight_claim_made"
    )
    checker_weight_values = _dict_key_literal_values(
        checker_tree, "weight_claim_made"
    )
    certificate_weight_values = _weight_flags(certificates)
    boundary_line = _boundary_data(primary_tree)[2]
    live_readings_present = tuple(
        reading in boundary_line for reading in EXPECTED_LIVE_READINGS
    )
    detail = {
        "audit_literal_eval": ast.literal_eval(audit_node),
        "blocklist": BLOCKLIST,
        "blocked_imports": blocked_imports,
        "imported_attribute_writes": tuple(
            imported_attribute_writes
        ),
        "live_readings_verbatim": EXPECTED_LIVE_READINGS,
        "weight_claim_made": False,
        "weight_claim_values": {
            "certificates": certificate_weight_values,
            "checker_source": checker_weight_values,
            "primary_source": primary_weight_values,
        },
    }
    passed = (
        audit_literal
        and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        and DECLARED_INPUT_PATHS is AUDIT_INPUT_PATHS
        and set(AUDIT_INPUT_PATHS) == set(
            ast.literal_eval(
                _top_assignments(primary_tree)["AUDIT_INPUT_PATHS"]
            )
        )
        and PRIMARY_PATH == BLOCKLIST[0]
        and not blocked_imports
        and blocked_module not in imported_modules
        and not imported_attribute_writes
        and primary_weight_values == (False, False)
        and checker_weight_values
        and all(value is False for value in checker_weight_values)
        and certificate_weight_values
        and all(
            value is False for value in certificate_weight_values
        )
        and all(live_readings_present)
        and boundary_line == EXPECTED_BOUNDARY_LINE
    )
    record("discipline", passed, detail)
    return detail


def main() -> int:
    started = perf_counter()
    extraction_detail, primary_tree, primary_source = extraction()
    family, family_detail = family_recount()
    (
        _mapped,
        simplex,
        _held_candidate,
        born_table,
        census_detail,
    ) = census_recount(family)
    uniform_detail = uniformity_probe(simplex, born_table)
    split_detail = split_recount(family)
    discipline_detail = discipline(
        primary_tree,
        primary_source,
        (
            extraction_detail,
            family_detail,
            census_detail,
            uniform_detail,
            split_detail,
        ),
    )
    runtime_seconds = perf_counter() - started
    runtime_pass = runtime_seconds < AUDIT_TIMEOUT_SEC
    record(
        "bounded_runtime",
        runtime_pass,
        {
            "note_path": NOTE_PATH,
            "runtime_seconds": round(runtime_seconds, 6),
            "timeout_seconds": AUDIT_TIMEOUT_SEC,
        },
    )
    all_pass = all(CHECKS.values())
    OUTPUT_LINES.append(
        (
            "CYCLE760_SCALED_INDEPENDENT_CHECK_PASS"
            if all_pass
            else "CYCLE760_SCALED_INDEPENDENT_CHECK_HONEST_FAIL"
        )
        + " :: "
        + compact(
            {
                "checks_failed": sum(
                    not value for value in CHECKS.values()
                ),
                "checks_passed": sum(CHECKS.values()),
                "runtime_seconds": round(runtime_seconds, 6),
                "weight_claim_made": False,
            }
        )
    )
    output = "\n".join(OUTPUT_LINES) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        sys.stderr.write(
            "FAIL stdout_bound :: "
            + compact(
                {
                    "bytes": len(output.encode("utf-8")),
                    "limit": STDOUT_LIMIT_BYTES,
                }
            )
            + "\n"
        )
        return 1
    sys.stdout.write(output)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
