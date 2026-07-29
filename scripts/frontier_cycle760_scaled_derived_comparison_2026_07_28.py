#!/usr/bin/env python3
"""Cycle 760: scaled derived-occurrence comparison on the k=1 stratum.

Cycle 758's exhaustive k=1 translation-family construction is crossed with
every Cycle 750 enforcement-lineage fixture.  Each cyclic translation is one
finite epoch family.  Cycle 757's declared outcome-class mapping is reused
unchanged, so every census and tolerance verdict below remains comparison
DATA: the mapping is supplied and no occurrence weight is inferred.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = (
    "docs/SCALED_DERIVED_COMPARISON_CYCLE760_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle757_derived_occurrence_calibration_2026_07_28.py",
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import perf_counter


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle757_derived_occurrence_calibration_2026_07_28 as C757
import frontier_cycle758_selector_multisource_2026_07_28 as S758
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750


STDOUT_LIMIT_BYTES = 150 * 1024
BANK_COUNTS = (2, 5, 12)
EXPECTED_FIXTURE_COUNTS = {2: 4, 5: 10, 12: 24}
EXPECTED_PROGRAM_LENGTHS = {2: 11, 5: 35, 12: 91}
EXPECTED_FAMILY_COUNTS = {2: 44, 5: 350, 12: 2184}
EXPECTED_FAMILY_TOTAL = 2578
EXPECTED_CONFIGURATION_EVALUATIONS = 2578
EXPECTED_CYCLIC_COVARIANCE_CASES = 137
EXPECTED_DERIVED_COUNTS = (845, 878, 855)
EXPECTED_REVERSAL_COUNTS = (860, 860, 858)
EXPECTED_SPLIT_COUNTS = ((390, 424, 475), (455, 454, 380))
SAMPLE_SIZE_CEILING = "2,578 finite k=1 translation-expanded epoch families"
MENU_ID = "cycle760-cycle317-contact-trine"
PROGRAM_ID = "cycle760-scaled-f750-k1-family"
EFFECT_IDS = C757.EFFECT_IDS
MAPPING_CONVENTION = C757.MAPPING_CONVENTION

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )


def digest_rows(rows: object) -> str:
    return sha256(compact(rows).encode("utf-8")).hexdigest()


def check(label: str, condition: bool, detail: object = "") -> None:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )


def _sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def header_and_ast_audit() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__)))
    assignments: dict[str, ast.AST] = {}
    imports: dict[str, str] = {}
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
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports[alias.asname or alias.name] = alias.name

    audit_node = assignments["AUDIT_INPUT_PATHS"]
    declared_node = assignments["DECLARED_INPUT_PATHS"]
    literal_tuple = (
        isinstance(audit_node, ast.Tuple)
        and len(audit_node.elts) == 3
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_node.elts
        )
    )
    imported = {
        alias: imports.get(alias) for alias in ("C757", "S758", "F750")
    }
    expected_imported = {
        "C757":
            "frontier_cycle757_derived_occurrence_calibration_2026_07_28",
        "S758":
            "frontier_cycle758_selector_multisource_2026_07_28",
        "F750":
            "frontier_cycle750_actual_selector_stretch_2026_07_28",
    }
    module_aliases = set(expected_imported)
    imported_writes = []
    file_writes = []
    forbidden_targets = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
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
                    and root.id in module_aliases
                ):
                    imported_writes.append(ast.unparse(target))
                for child in ast.walk(target):
                    if (
                        isinstance(child, ast.Name)
                        and isinstance(child.ctx, ast.Store)
                        and (
                            child.id.lower() == "weight"
                            or child.id.lower().endswith("_weight")
                            or "calibrated_weight" in child.id.lower()
                        )
                    ):
                        forbidden_targets.append(child.id)
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr
            in {
                "write_text",
                "write_bytes",
                "unlink",
                "rename",
                "replace",
            }
        ):
            file_writes.append(ast.unparse(node.func))

    detail = {
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "declared_is_audit_name": (
            isinstance(declared_node, ast.Name)
            and declared_node.id == "AUDIT_INPUT_PATHS"
        ),
        "file_write_calls": tuple(file_writes),
        "forbidden_promotion_targets": tuple(sorted(set(forbidden_targets))),
        "imported_module_attribute_writes": tuple(imported_writes),
        "imports": imported,
        "literal_tuple": literal_tuple,
        "note_path": NOTE_PATH,
        "timeout_seconds": AUDIT_TIMEOUT_SEC,
    }
    check(
        "header exact literal inputs, imports, timeout, note, and firewall",
        literal_tuple
        and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        and isinstance(declared_node, ast.Name)
        and declared_node.id == "AUDIT_INPUT_PATHS"
        and imported == expected_imported
        and AUDIT_TIMEOUT_SEC == 1800
        and NOTE_PATH
        == (
            "docs/SCALED_DERIVED_COMPARISON_CYCLE760_"
            "BOUNDED_THEOREM_NOTE_2026-07-28.md"
        )
        and not imported_writes
        and not file_writes
        and not forbidden_targets,
        detail,
    )
    return detail


def k1_stratum_template() -> tuple[tuple[int, ...], ...]:
    configurations = tuple(
        tuple(
            int(index == position)
            for index in range(S758.RING_STATIONS)
        )
        for position in range(S758.RING_STATIONS)
    )
    families = S758.configuration_families(configurations)
    return families[1][(0,)]


def lifted_k1_family(station_count: int) -> tuple[tuple[int, ...], ...]:
    """Lift S758's singleton translation-family rule to an F750 ring."""
    return tuple((position,) for position in range(station_count))


def scaled_k1_occurrences() -> tuple[
    tuple[dict[str, object], ...],
    dict[str, object],
]:
    occurrences = []
    fixture_counts: Counter[int] = Counter()
    family_counts: Counter[int] = Counter()
    program_lengths: dict[int, set[int]] = {
        bank_count: set() for bank_count in BANK_COUNTS
    }
    selected_count_range = [10**9, -1]
    covariance_cases = 0
    covariance_failures = 0
    configuration_evaluations = 0
    global_epoch_ordinal = 0

    for bank_count in BANK_COUNTS:
        fixtures = F750.k_epoch_fixtures(bank_count)
        fixture_counts[bank_count] += len(fixtures)
        first = fixtures[0]
        symmetry = F750.cyclic_enforcement_symmetry(
            bank_count,
            first[3],
            first[4],
        )
        covariance_cases += symmetry["cases"]
        covariance_failures += len(symmetry["failures"])
        for event, direction, program, before, _single_expected in fixtures:
            station_count = len(program)
            program_lengths[bank_count].add(station_count)
            alternatives = lifted_k1_family(station_count)
            result = S758.multisource_enforcement_lineage_selector(
                program,
                before,
                bank_count,
                alternatives,
            )
            selected = result["selected"]
            selected_count_range[0] = min(
                selected_count_range[0], len(selected)
            )
            selected_count_range[1] = max(
                selected_count_range[1], len(selected)
            )
            configuration_evaluations += len(result["evaluations"])
            for shift in range(station_count):
                actual = (
                    (station_count - shift) % station_count
                    if selected == ((0,),)
                    else None
                )
                occurrences.append(
                    {
                        "alternative_count": station_count,
                        "bank_count": bank_count,
                        "direction": tuple(direction),
                        "fixture_event": event,
                        "global_epoch_ordinal": global_epoch_ordinal,
                        "program_shift": shift,
                        "selected_alternative": actual,
                    }
                )
                family_counts[bank_count] += 1
                global_epoch_ordinal += 1

    detail = {
        "configuration_evaluations": configuration_evaluations,
        "construction": (
            "Each F750 fixture's complete S758 singleton family is "
            "exhausted at its base orientation; the landed F750 cyclic "
            "covariance transports its unique survivor through every "
            "translation."
        ),
        "cyclic_covariance_cases": covariance_cases,
        "covariance_failure_count": covariance_failures,
        "family_counts_by_bank": dict(sorted(family_counts.items())),
        "fixture_counts_by_bank": dict(sorted(fixture_counts.items())),
        "program_lengths_by_bank": {
            bank_count: tuple(sorted(lengths))
            for bank_count, lengths in program_lengths.items()
        },
        "selected_count_range": tuple(selected_count_range),
        "total": len(occurrences),
        "row_digest": digest_rows(occurrences),
    }
    return tuple(occurrences), detail


def mapped_events(
    occurrences: tuple[dict[str, object], ...],
    *,
    selector_mode: str,
) -> tuple[dict[str, object], ...]:
    mapped = []
    for occurrence in occurrences:
        actual = occurrence["selected_alternative"]
        if actual is None:
            continue
        if selector_mode == "derived":
            used = actual
        elif selector_mode == "reversal-control":
            used = occurrence["alternative_count"] - 1 - actual
        else:
            raise ValueError(f"unknown selector mode: {selector_mode}")
        outcome_index = (
            occurrence["global_epoch_ordinal"] + used
        ) % len(EFFECT_IDS)
        mapped.append(
            {
                **occurrence,
                "actual_selected_alternative": actual,
                "effect_id": EFFECT_IDS[outcome_index],
                "outcome_index": outcome_index,
                "selector_mode": selector_mode,
                "used_alternative": used,
            }
        )
    return tuple(mapped)


def receive_family(
    family_name: str,
    mapped: tuple[dict[str, object], ...],
) -> tuple[tuple[object, ...], object]:
    port = C757.C744
    exposure_id = f"cycle760-{family_name}-exposure"
    rows = tuple(
        port.RecordRow(
            record_id=f"cycle760-{family_name}-r{index:04d}",
            menu_id=MENU_ID,
            program_id=PROGRAM_ID,
            outcome_index=event["outcome_index"],
            effect_id=event["effect_id"],
            exposure_id=exposure_id,
            record_kind="declared_apparatus_test_row",
            provenance=(
                "cycle760:S758-k1-x-F750-fixtures;"
                f"mapping={MAPPING_CONVENTION['status']};family={family_name}"
            ),
        )
        for index, event in enumerate(mapped)
    )
    identity = port.MenuProgramIdentity(MENU_ID, PROGRAM_ID)
    exposure = port.ExposureDeclaration(
        exposure_id=exposure_id,
        menu_id=MENU_ID,
        program_id=PROGRAM_ID,
        trial_total=len(rows),
        per_effect_eligible_trials=(len(rows),) * len(EFFECT_IDS),
        sampling_protocol="complete-exclusive-common-exposure",
        provenance=(
            "Cycle 760 finite k=1 family census; one declared common "
            "exposure across all translated fixture epochs"
        ),
    )
    metadata = port.EffectIdentityMetadata(
        coarse_grainings=(
            ("all", (0, 1, 2)),
            ("first-two", (0, 1)),
            ("third", (2,)),
        ),
        same_effect_classes=tuple(
            (effect_id,) for effect_id in EFFECT_IDS
        ),
    )
    empirical = port.receive_occurrence_records(
        identity,
        EFFECT_IDS,
        rows,
        exposure,
        metadata,
    )
    return rows, empirical


def split_stability_table(
    first_empirical: object,
    second_empirical: object,
) -> tuple[dict[str, object], ...]:
    table = []
    for tolerance in C757.C748.TOLERANCE_LADDER:
        rows = C757.C744.compare_empirical_to_landed(
            first_empirical,
            tuple(float(value) for value in second_empirical.simplex),
            tolerance=tolerance,
        )
        disagreements = sum(
            row.verdict == "disagreement" for row in rows
        )
        table.append(
            {
                "aggregate": (
                    "agreement" if disagreements == 0 else "disagreement"
                ),
                "disagreement_count": disagreements,
                "effect_rows": tuple(
                    {
                        "effect_id": row.effect_id,
                        "first_simplex": str(
                            first_empirical.simplex[index]
                        ),
                        "residual_hex": row.residual.hex(),
                        "second_simplex": str(
                            second_empirical.simplex[index]
                        ),
                        "verdict": row.verdict,
                    }
                    for index, row in enumerate(rows)
                ),
                "tolerance": tolerance,
            }
        )
    return tuple(table)


def anchor_certificate(
    template: tuple[tuple[int, ...], ...],
    captured_cycle317: str,
    held_candidate: tuple[float, ...],
) -> dict[str, object]:
    imported_paths = tuple(
        str(Path(module.__file__).resolve().relative_to(ROOT))
        for module in (C757, S758, F750)
    )
    detail = {
        "cycle317_captured_pass_lines":
            captured_cycle317.count("PASS "),
        "cycle757_mapping_convention": MAPPING_CONVENTION,
        "frozen_held_candidate_hex":
            tuple(value.hex() for value in held_candidate),
        "imported_paths": imported_paths,
        "k1_representative": (0,),
        "k1_template": template,
        "ring_stations": S758.RING_STATIONS,
    }
    check(
        "A anchors: exact suppliers, S758 k=1 stratum, and C757 map",
        imported_paths == AUDIT_INPUT_PATHS
        and S758.RING_STATIONS == 11
        and template == tuple((position,) for position in range(11))
        and MAPPING_CONVENTION == C757.MAPPING_CONVENTION
        and MAPPING_CONVENTION["status"] == "SUPPLY"
        and MAPPING_CONVENTION["formula"]
        == (
            "outcome_index = (global_epoch_ordinal + "
            "selected_alternative) mod 3"
        )
        and tuple(value.hex() for value in held_candidate)
        == C757.C748.FROZEN_HELD_CANDIDATE_HEX
        and captured_cycle317.count("PASS ") == 4
        and "FAIL " not in captured_cycle317,
        detail,
    )
    return detail


def family_certificate(
    occurrences: tuple[dict[str, object], ...],
    construction: dict[str, object],
) -> dict[str, object]:
    detail = {
        **construction,
        "family_size_ceiling": SAMPLE_SIZE_CEILING,
        "k": 1,
        "scope": "all landed F750 fixtures and all ring translations",
    }
    check(
        "B family construction: every lifted k=1 fixture translation",
        len(occurrences) == EXPECTED_FAMILY_TOTAL
        and construction["total"] == EXPECTED_FAMILY_TOTAL
        and construction["fixture_counts_by_bank"]
        == EXPECTED_FIXTURE_COUNTS
        and construction["program_lengths_by_bank"]
        == {2: (11,), 5: (35,), 12: (91,)}
        and construction["family_counts_by_bank"]
        == EXPECTED_FAMILY_COUNTS
        and construction["configuration_evaluations"]
        == EXPECTED_CONFIGURATION_EVALUATIONS
        and construction["cyclic_covariance_cases"]
        == EXPECTED_CYCLIC_COVARIANCE_CASES
        and construction["selected_count_range"] == (1, 1)
        and construction["covariance_failure_count"] == 0
        and all(
            occurrence["selected_alternative"]
            == (
                occurrence["alternative_count"]
                - occurrence["program_shift"]
            )
            % occurrence["alternative_count"]
            for occurrence in occurrences
        ),
        detail,
    )
    OUTPUT_LINES.append(
        "DATA scaled_family_total :: "
        + compact(
            {
                "by_bank": construction["family_counts_by_bank"],
                "total": len(occurrences),
            }
        )
    )
    return detail


def census_certificate(
    mapped: tuple[dict[str, object], ...],
    rows: tuple[object, ...],
    empirical: object,
) -> dict[str, object]:
    detail = {
        "common_exposure": len(rows),
        "counts": empirical.counts,
        "mapping_convention": MAPPING_CONVENTION,
        "simplex": tuple(str(value) for value in empirical.simplex),
        "simplex_sum": str(
            sum(empirical.simplex, start=Fraction(0, 1))
        ),
    }
    check(
        "C exact census and simplex enter the unchanged typed receiver",
        len(mapped) == len(rows) == EXPECTED_FAMILY_TOTAL
        and empirical.counts == EXPECTED_DERIVED_COUNTS
        and sum(empirical.counts) == EXPECTED_FAMILY_TOTAL
        and empirical.simplex
        == tuple(
            Fraction(count, EXPECTED_FAMILY_TOTAL)
            for count in EXPECTED_DERIVED_COUNTS
        )
        and sum(empirical.simplex, start=Fraction(0, 1))
        == Fraction(1, 1)
        and dict(empirical.coarse_counts)["all"]
        == EXPECTED_FAMILY_TOTAL
        and all(
            event["selector_mode"] == "derived"
            and event["used_alternative"]
            == event["actual_selected_alternative"]
            and event["outcome_index"]
            == (
                event["global_epoch_ordinal"]
                + event["actual_selected_alternative"]
            )
            % len(EFFECT_IDS)
            for event in mapped
        ),
        detail,
    )
    OUTPUT_LINES.append("DATA scaled_census :: " + compact(detail))
    return detail


def comparison_certificate(
    empirical: object,
    held_candidate: tuple[float, ...],
) -> tuple[dict[str, object], tuple[dict[str, object], ...]]:
    current_table = C757._comparison_table(empirical, held_candidate)
    baseline_occurrences = C757._selector_occurrences()
    baseline_mapped = C757._mapped_events(
        baseline_occurrences,
        selector_mode="derived",
    )
    _baseline_rows, baseline_empirical = C757._receive_mapped_family(
        "cycle760-baseline-cycle757",
        baseline_mapped,
    )
    baseline_table = C757._comparison_table(
        baseline_empirical,
        held_candidate,
    )
    paired = tuple(
        {
            "cycle757_38_epoch": {
                "aggregate": baseline["aggregate"],
                "disagreement_count": baseline["disagreement_count"],
            },
            "cycle760_scaled": {
                "aggregate": current["aggregate"],
                "disagreement_count": current["disagreement_count"],
            },
            "tolerance": current["tolerance"],
        }
        for current, baseline in zip(
            current_table, baseline_table, strict=True
        )
    )
    detail = {
        "comparison_kind": (
            "finite derived-occurrence simplexes vs supplied "
            "w(E)=Tr(sigma E)"
        ),
        "cycle757_counts": baseline_empirical.counts,
        "cycle757_table": baseline_table,
        "cycle760_counts": empirical.counts,
        "cycle760_table": current_table,
        "paired_table": paired,
        "table_role": "DATA",
        "tolerance_ladder": C757.C748.TOLERANCE_LADDER,
    }
    check(
        "D frozen 748 tolerances compare Cycle 760 and Cycle 757 as DATA",
        C757.C748.TOLERANCE_LADDER == (0.06, 0.02, 0.002, 0.001)
        and baseline_empirical.counts
        == C757.EXPECTED_DERIVED_COUNTS
        and tuple(
            row["disagreement_count"] for row in baseline_table
        )
        == C757.EXPECTED_DERIVED_DISAGREEMENTS
        and tuple(value.hex() for value in held_candidate)
        == C757.C748.FROZEN_HELD_CANDIDATE_HEX
        and all(
            row["aggregate"] in {"agreement", "disagreement"}
            and len(row["effect_rows"]) == len(EFFECT_IDS)
            for table in (current_table, baseline_table)
            for row in table
        ),
        {
            "paired_table": paired,
            "table_role": "DATA",
            "tolerance_ladder": C757.C748.TOLERANCE_LADDER,
        },
    )
    OUTPUT_LINES.append(
        "DATA comparison_vs_cycle757 :: " + compact(paired)
    )
    return detail, current_table


def controls_certificate(
    occurrences: tuple[dict[str, object], ...],
    derived_empirical: object,
    held_candidate: tuple[float, ...],
) -> dict[str, object]:
    reversal_mapped = mapped_events(
        occurrences,
        selector_mode="reversal-control",
    )
    _reversal_rows, reversal_empirical = receive_family(
        "reversal-control",
        reversal_mapped,
    )
    reversal_table = C757._comparison_table(
        reversal_empirical,
        held_candidate,
    )

    split_at = len(occurrences) // 2
    first_mapped = mapped_events(
        occurrences[:split_at],
        selector_mode="derived",
    )
    second_mapped = mapped_events(
        occurrences[split_at:],
        selector_mode="derived",
    )
    _first_rows, first_empirical = receive_family(
        "split-first-half",
        first_mapped,
    )
    _second_rows, second_empirical = receive_family(
        "split-second-half",
        second_mapped,
    )
    split_table = split_stability_table(
        first_empirical,
        second_empirical,
    )
    exact_delta = tuple(
        first - second
        for first, second in zip(
            first_empirical.simplex,
            second_empirical.simplex,
            strict=True,
        )
    )
    detail = {
        "reversal_permutation": {
            "counts": reversal_empirical.counts,
            "definition": (
                "used_alternative = alternative_count - 1 "
                "- actual_selected_alternative"
            ),
            "detected": (
                reversal_empirical.counts != derived_empirical.counts
            ),
            "verdict_table": reversal_table,
        },
        "split_stability": {
            "exact_first_minus_second":
                tuple(str(value) for value in exact_delta),
            "first": {
                "counts": first_empirical.counts,
                "sample_size": len(first_mapped),
                "simplex":
                    tuple(str(value) for value in first_empirical.simplex),
            },
            "second": {
                "counts": second_empirical.counts,
                "sample_size": len(second_mapped),
                "simplex":
                    tuple(str(value) for value in second_empirical.simplex),
            },
            "table_role": "DATA",
            "tolerance_table": split_table,
            "total_variation": str(
                sum(
                    (abs(value) for value in exact_delta),
                    start=Fraction(0, 1),
                )
                / 2
            ),
        },
    }
    check(
        "E controls: reversal detected and disjoint split compared as DATA",
        reversal_empirical.counts == EXPECTED_REVERSAL_COUNTS
        and reversal_empirical.counts != derived_empirical.counts
        and tuple(
            first_empirical.counts
            for first_empirical in (first_empirical, second_empirical)
        )
        == EXPECTED_SPLIT_COUNTS
        and len(first_mapped) == len(second_mapped) == 1289
        and all(
            row["aggregate"] in {"agreement", "disagreement"}
            and len(row["effect_rows"]) == len(EFFECT_IDS)
            for row in split_table
        ),
        {
            "reversal_counts": reversal_empirical.counts,
            "split_counts": (
                first_empirical.counts,
                second_empirical.counts,
            ),
            "split_disagreements": tuple(
                row["disagreement_count"] for row in split_table
            ),
            "split_table_role": "DATA",
            "total_variation":
                detail["split_stability"]["total_variation"],
        },
    )
    OUTPUT_LINES.append(
        "DATA controls :: "
        + compact(
            {
                "reversal_counts": reversal_empirical.counts,
                "split": detail["split_stability"],
            }
        )
    )
    return detail


def boundary_certificate(
    current_table: tuple[dict[str, object], ...],
) -> dict[str, object]:
    boundary = {
        "asymptotic_convergence_claimed": False,
        "born_law_selected": False,
        "comparison_only": True,
        "family_exhaustive_within_landed_k1_fixture_scope": True,
        "mapping_convention_derived": False,
        "mapping_convention_supplied": True,
        "sample_size_bound": SAMPLE_SIZE_CEILING,
        "sample_size_finite": EXPECTED_FAMILY_TOTAL,
        "simplex_promoted_to_weight": False,
        "split_stability_role": "DATA",
        "verdict_table": current_table,
        "verdict_table_role": "DATA",
        "weight_claim_made": False,
    }
    check(
        "F honest boundary: larger finite ceiling, supplied map, no weight",
        boundary["weight_claim_made"] is False
        and boundary["sample_size_bound"] == SAMPLE_SIZE_CEILING
        and boundary["sample_size_finite"] == EXPECTED_FAMILY_TOTAL
        and boundary["mapping_convention_supplied"] is True
        and boundary["mapping_convention_derived"] is False
        and boundary["simplex_promoted_to_weight"] is False
        and boundary["asymptotic_convergence_claimed"] is False
        and boundary["born_law_selected"] is False
        and boundary["verdict_table_role"] == "DATA"
        and boundary["split_stability_role"] == "DATA",
        boundary,
    )
    OUTPUT_LINES.append(
        "BOUNDARY HONEST CEILING :: "
        "2,578 k=1 families are larger but finite; the outcome-class "
        "mapping remains supplied, and neither the census nor split "
        "comparison is a weight claim."
    )
    return boundary


def main() -> int:
    started = perf_counter()
    input_sha_before = {
        relative: _sha256(ROOT / relative)
        for relative in AUDIT_INPUT_PATHS
    }

    header = header_and_ast_audit()
    template = k1_stratum_template()
    effects, captured_cycle317 = C757._landed_contact_trine()
    held_candidate = C757._trace_candidate(effects)
    anchors = anchor_certificate(
        template,
        captured_cycle317,
        held_candidate,
    )

    occurrences, construction = scaled_k1_occurrences()
    family = family_certificate(occurrences, construction)
    derived_mapped = mapped_events(
        occurrences,
        selector_mode="derived",
    )
    derived_rows, derived_empirical = receive_family(
        "derived-scaled",
        derived_mapped,
    )
    census = census_certificate(
        derived_mapped,
        derived_rows,
        derived_empirical,
    )
    comparison, current_table = comparison_certificate(
        derived_empirical,
        held_candidate,
    )
    controls = controls_certificate(
        occurrences,
        derived_empirical,
        held_candidate,
    )
    boundary = boundary_certificate(current_table)

    input_sha_after = {
        relative: _sha256(ROOT / relative)
        for relative in AUDIT_INPUT_PATHS
    }
    check(
        "A imported inputs remain byte-stable",
        input_sha_before == input_sha_after,
        input_sha_after,
    )
    runtime_seconds = perf_counter() - started
    check(
        "bounded runtime and optional-note contract",
        runtime_seconds < AUDIT_TIMEOUT_SEC,
        {
            "note_path": NOTE_PATH,
            "note_required": False,
            "runtime_seconds": round(runtime_seconds, 6),
            "timeout_seconds": AUDIT_TIMEOUT_SEC,
        },
    )

    report = {
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "certificates": {
            "A_anchors": anchors,
            "B_family_construction": family,
            "C_census_simplex": census,
            "D_comparison_table": comparison,
            "E_controls": controls,
            "F_boundary": boundary,
            "header": header,
        },
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "derived_census": {
            "counts": derived_empirical.counts,
            "family_size": len(occurrences),
            "simplex": tuple(
                str(value) for value in derived_empirical.simplex
            ),
        },
        "family_size": len(occurrences),
        "mapping_convention_supplied": True,
        "note_path": NOTE_PATH,
        "pass": all(CHECKS.values()),
        "runtime_seconds": round(runtime_seconds, 6),
        "sample_size_bound": SAMPLE_SIZE_CEILING,
        "weight_claim_made": False,
    }
    report["terminal"] = (
        "CYCLE760_SCALED_DERIVED_COMPARISON_PASS"
        if report["pass"]
        else "CYCLE760_SCALED_DERIVED_COMPARISON_HONEST_FAIL"
    )
    report["report_sha256"] = digest_rows(report)
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
